/**
 * Local Ollama API Client for Gemma 4 (gemma4)
 * Endpoint: http://127.0.0.1:11434/api/chat
 */
class OllamaGemmaClient {
  constructor(config = {}) {
    this.endpoint = config.endpoint || localStorage.getItem('gemma_ollama_endpoint') || 'http://127.0.0.1:11434';
    this.model = config.model || localStorage.getItem('gemma_ollama_model') || 'gemma4';
    this.abortController = null;
  }

  setEndpoint(url) {
    this.endpoint = url.trim().replace(/\/+$/, '');
    localStorage.setItem('gemma_ollama_endpoint', this.endpoint);
  }

  setModel(model) {
    this.model = model.trim();
    localStorage.setItem('gemma_ollama_model', this.model);
  }

  abort() {
    if (this.abortController) {
      this.abortController.abort();
      this.abortController = null;
    }
  }

  /**
   * Health ping to /api/tags to check if Ollama daemon is active
   */
  async checkHealth() {
    try {
      // First try direct endpoint
      let res = await fetch(`${this.endpoint}/api/tags`, { method: 'GET' }).catch(() => null);
      
      // If direct fetch blocked by CORS, try local proxy route
      if (!res || !res.ok) {
        res = await fetch(`/api/ollama/api/tags`, { method: 'GET' }).catch(() => null);
      }

      if (res && res.ok) {
        const data = await res.json();
        const models = (data.models || []).map(m => m.name);
        const hasGemma = models.some(m => m.includes('gemma'));
        return { online: true, models, hasGemma };
      }
      return { online: false, error: 'Ollama is unreachable' };
    } catch (err) {
      return { online: false, error: err.message };
    }
  }

  /**
   * Generates content using Ollama streaming /api/chat
   */
  async generateStream({
    prompt,
    systemInstruction = '',
    imageAttachment = null, // { mimeType, base64 }
    onToken,
    onThought,
    onComplete,
    onError,
    onTtft
  }) {
    this.abort();
    this.abortController = new AbortController();

    const startTime = performance.now();
    let ttft = null;
    let fullText = '';
    let accumulatedThought = '';
    let tokenCount = 0;

    const messages = [];

    if (systemInstruction && systemInstruction.trim()) {
      messages.push({
        role: "system",
        content: systemInstruction.trim()
      });
    }

    const userMessage = {
      role: "user",
      content: prompt
    };

    if (imageAttachment && imageAttachment.base64) {
      // Ollama expects array of raw base64 strings in images property
      const cleanB64 = imageAttachment.base64.replace(/^data:image\/[a-z]+;base64,/, '');
      userMessage.images = [cleanB64];
    }

    messages.push(userMessage);

    const payload = {
      model: this.model,
      messages: messages,
      stream: true,
      options: {
        temperature: 0.7
      }
    };

    // Determine target URL (try direct first, fallback to proxy)
    let targetUrl = `${this.endpoint}/api/chat`;

    try {
      let response;
      try {
        response = await fetch(targetUrl, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload),
          signal: this.abortController.signal
        });
      } catch (directErr) {
        // Fallback to proxy if direct request fails (e.g. CORS)
        targetUrl = `/api/ollama/api/chat`;
        response = await fetch(targetUrl, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload),
          signal: this.abortController.signal
        });
      }

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        const message = errorData.error || `Ollama error ${response.status}: ${response.statusText}`;
        throw new Error(message);
      }

      const reader = response.body.getReader();
      const decoder = new TextDecoder('utf-8');
      let buffer = '';
      let finalOllamaTelemetry = null;

      while (true) {
        const { value, done } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split('\n');
        buffer = lines.pop();

        for (const line of lines) {
          const trimmed = line.trim();
          if (!trimmed) continue;

          try {
            const data = JSON.parse(trimmed);

            if (data.message && data.message.content) {
              const chunk = data.message.content;

              if (ttft === null) {
                ttft = Math.round(performance.now() - startTime);
                if (onTtft) onTtft(ttft);
              }

              fullText += chunk;
              tokenCount += Math.max(1, Math.round(chunk.length / 4));

              // Check for thought/reasoning tags in the stream
              if (chunk.includes('<thought>') || chunk.includes('<think>')) {
                // start of reasoning
              }

              const currentDuration = (performance.now() - startTime) / 1000;
              const speed = currentDuration > 0 ? (tokenCount / currentDuration).toFixed(1) : 0;

              if (onToken) {
                onToken(chunk, fullText, {
                  ttft: ttft + ' ms',
                  speed: speed + ' tok/s',
                  duration: currentDuration.toFixed(2) + ' s',
                  tokens: tokenCount
                });
              }
            }

            if (data.done) {
              finalOllamaTelemetry = data;
            }
          } catch (e) {
            console.warn('Error parsing Ollama JSON line:', e);
          }
        }
      }

      // Check if text has <thought> tags to extract
      const extracted = window.MarkdownRenderer ? window.MarkdownRenderer.extractThoughts(fullText) : { thought: '', response: fullText };
      if (extracted.thought && onThought) {
        onThought(extracted.thought);
        fullText = extracted.response;
      }

      const totalDuration = ((performance.now() - startTime) / 1000).toFixed(2);
      let finalSpeed = totalDuration > 0 ? (tokenCount / totalDuration).toFixed(1) : 0;

      // Use Ollama's exact nanosecond telemetry if provided
      if (finalOllamaTelemetry) {
        if (finalOllamaTelemetry.eval_count) {
          tokenCount = finalOllamaTelemetry.eval_count;
        }
        if (finalOllamaTelemetry.eval_duration && finalOllamaTelemetry.eval_count) {
          const evalSec = finalOllamaTelemetry.eval_duration / 1e9;
          finalSpeed = (finalOllamaTelemetry.eval_count / evalSec).toFixed(1);
        }
      }

      if (onComplete) {
        onComplete(fullText, {
          ttft: (ttft || Math.round(performance.now() - startTime)) + ' ms',
          speed: finalSpeed + ' tok/s',
          duration: totalDuration + ' s',
          tokens: tokenCount,
          thought: extracted.thought
        });
      }
    } catch (err) {
      if (err.name === 'AbortError') {
        console.log('Ollama generation aborted by user.');
      } else {
        console.error('Ollama API Error:', err);
        const detailedMsg = err.message.includes('Failed to fetch') 
          ? `Could not reach Ollama at ${this.endpoint}. Make sure the Ollama daemon is running (run 'ollama serve' in your terminal).`
          : err.message;
        if (onError) onError(new Error(detailedMsg));
      }
    } finally {
      this.abortController = null;
    }
  }
}

window.OllamaGemmaClient = OllamaGemmaClient;
