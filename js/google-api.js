/**
 * Google Gemini & Cloud API Client for Gemma 4 (gemma-4-26b-a4b-it)
 * Follows official guide: https://ai.google.dev/gemma/docs/core/gemma_on_gemini_api
 * Also supports OpenRouter (sk-or-v1-...) as an alternative cloud provider.
 */
class GoogleGemmaClient {
  constructor(config = {}) {
    this.apiKey = config.apiKey || localStorage.getItem('gemma_google_api_key') || '';
    this.model = config.model || 'gemma-4-26b-a4b-it';
    this.baseUrl = config.baseUrl || 'https://generativelanguage.googleapis.com/v1beta';
    this.abortController = null;
  }

  setApiKey(key) {
    this.apiKey = key.trim();
    localStorage.setItem('gemma_google_api_key', this.apiKey);
  }

  getApiKey() {
    return this.apiKey || localStorage.getItem('gemma_google_api_key') || '';
  }

  isOpenRouterKey() {
    const key = this.getApiKey();
    return key.startsWith('sk-or-');
  }

  abort() {
    if (this.abortController) {
      this.abortController.abort();
      this.abortController = null;
    }
  }

  /**
   * Generates content using Server-Sent Events (SSE) streaming
   */
  async generateStream({
    prompt,
    systemInstruction = '',
    thinkingLevel = 'high',
    imageAttachment = null,
    onToken,
    onThought,
    onComplete,
    onError,
    onTtft
  }) {
    const key = this.getApiKey();
    if (!key) {
      if (onError) {
        const err = new Error("Google Gemini API Key is missing. Click the settings gear icon to configure your key.");
        err.isMissingKey = true;
        onError(err);
      }
      return;
    }

    // Check if OpenRouter key was provided
    if (this.isOpenRouterKey()) {
      return this.generateOpenRouterStream({
        prompt,
        systemInstruction,
        imageAttachment,
        onToken,
        onThought,
        onComplete,
        onError,
        onTtft
      });
    }

    this.abort();
    this.abortController = new AbortController();

    const startTime = performance.now();
    let ttft = null;
    let fullText = '';
    let accumulatedThought = '';
    let tokenCount = 0;

    // Assemble parts (text + optional multimodal image)
    const userParts = [];
    if (imageAttachment && imageAttachment.base64) {
      userParts.push({
        inlineData: {
          mimeType: imageAttachment.mimeType || 'image/jpeg',
          data: imageAttachment.base64.replace(/^data:image\/[a-z]+;base64,/, '')
        }
      });
    }
    userParts.push({ text: prompt });

    const payload = {
      contents: [{
        role: "user",
        parts: userParts
      }]
    };

    if (systemInstruction && systemInstruction.trim()) {
      payload.systemInstruction = {
        parts: [{ text: systemInstruction.trim() }]
      };
    }

    payload.generationConfig = {
      temperature: 0.7,
      topP: 0.95
    };

    if (thinkingLevel && thinkingLevel !== 'off') {
      payload.generationConfig.thinkingConfig = {
        thinkingLevel: thinkingLevel.toUpperCase()
      };
    }

    const endpoint = `${this.baseUrl}/models/${encodeURIComponent(this.model)}:streamGenerateContent?key=${encodeURIComponent(key)}&alt=sse`;

    try {
      const response = await fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
        signal: this.abortController.signal
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        const message = errorData.error?.message || `HTTP error ${response.status}: ${response.statusText}`;
        throw new Error(message);
      }

      const reader = response.body.getReader();
      const decoder = new TextDecoder('utf-8');
      let buffer = '';

      while (true) {
        const { value, done } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split('\n');
        buffer = lines.pop();

        for (const line of lines) {
          const trimmed = line.trim();
          if (!trimmed.startsWith('data:')) continue;

          const jsonStr = trimmed.substring(5).trim();
          if (!jsonStr || jsonStr === '[DONE]') continue;

          try {
            const data = JSON.parse(jsonStr);
            const candidates = data.candidates || [];
            if (!candidates.length) continue;

            const candidate = candidates[0];
            const parts = candidate.content?.parts || [];

            for (const part of parts) {
              if (part.thought) {
                accumulatedThought += part.text || '';
                if (onThought) onThought(accumulatedThought);
              } else if (part.text) {
                if (ttft === null) {
                  ttft = Math.round(performance.now() - startTime);
                  if (onTtft) onTtft(ttft);
                }

                fullText += part.text;
                tokenCount += Math.max(1, Math.round(part.text.length / 4));

                const currentDuration = (performance.now() - startTime) / 1000;
                const speed = currentDuration > 0 ? (tokenCount / currentDuration).toFixed(1) : 0;

                if (onToken) {
                  onToken(part.text, fullText, {
                    ttft: ttft + ' ms',
                    speed: speed + ' tok/s',
                    duration: currentDuration.toFixed(2) + ' s',
                    tokens: tokenCount
                  });
                }
              }
            }

            if (data.usageMetadata?.candidatesTokenCount) {
              tokenCount = data.usageMetadata.candidatesTokenCount;
            }
          } catch (e) {
            console.warn('Error parsing SSE JSON:', e);
          }
        }
      }

      const totalDuration = ((performance.now() - startTime) / 1000).toFixed(2);
      const finalSpeed = totalDuration > 0 ? (tokenCount / totalDuration).toFixed(1) : 0;

      if (onComplete) {
        onComplete(fullText, {
          ttft: (ttft || Math.round(performance.now() - startTime)) + ' ms',
          speed: finalSpeed + ' tok/s',
          duration: totalDuration + ' s',
          tokens: tokenCount,
          thought: accumulatedThought
        });
      }
    } catch (err) {
      if (err.name === 'AbortError') {
        console.log('Google API generation aborted by user.');
      } else {
        console.error('Google API Error:', err);
        if (onError) onError(err);
      }
    } finally {
      this.abortController = null;
    }
  }

  /**
   * Streaming support for OpenRouter API keys (sk-or-v1-...)
   */
  async generateOpenRouterStream({
    prompt,
    systemInstruction = '',
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
    let tokenCount = 0;

    const messages = [];
    if (systemInstruction) {
      messages.push({ role: 'system', content: systemInstruction });
    }
    messages.push({ role: 'user', content: prompt });

    const openRouterModel = this.model.includes('/') ? this.model : `google/${this.model}`;

    try {
      const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.getApiKey()}`,
          'Content-Type': 'application/json',
          'HTTP-Referer': 'http://localhost:3000',
          'X-Title': 'Gemma 4 Arena'
        },
        body: JSON.stringify({
          model: openRouterModel,
          messages: messages,
          stream: true,
          temperature: 0.7
        }),
        signal: this.abortController.signal
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        const msg = errorData.error?.message || `OpenRouter error ${response.status}: ${response.statusText}`;
        throw new Error(msg);
      }

      const reader = response.body.getReader();
      const decoder = new TextDecoder('utf-8');
      let buffer = '';

      while (true) {
        const { value, done } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split('\n');
        buffer = lines.pop();

        for (const line of lines) {
          const trimmed = line.trim();
          if (!trimmed.startsWith('data:')) continue;
          const jsonStr = trimmed.substring(5).trim();
          if (!jsonStr || jsonStr === '[DONE]') continue;

          try {
            const data = JSON.parse(jsonStr);
            const delta = data.choices?.[0]?.delta?.content || '';
            if (delta) {
              if (ttft === null) {
                ttft = Math.round(performance.now() - startTime);
                if (onTtft) onTtft(ttft);
              }
              fullText += delta;
              tokenCount += Math.max(1, Math.round(delta.length / 4));

              const currentDuration = (performance.now() - startTime) / 1000;
              const speed = currentDuration > 0 ? (tokenCount / currentDuration).toFixed(1) : 0;

              if (onToken) {
                onToken(delta, fullText, {
                  ttft: ttft + ' ms',
                  speed: speed + ' tok/s',
                  duration: currentDuration.toFixed(2) + ' s',
                  tokens: tokenCount
                });
              }
            }
          } catch (e) {
            console.warn('Error parsing OpenRouter chunk:', e);
          }
        }
      }

      const totalDuration = ((performance.now() - startTime) / 1000).toFixed(2);
      const finalSpeed = totalDuration > 0 ? (tokenCount / totalDuration).toFixed(1) : 0;

      if (onComplete) {
        onComplete(fullText, {
          ttft: (ttft || Math.round(performance.now() - startTime)) + ' ms',
          speed: finalSpeed + ' tok/s',
          duration: totalDuration + ' s',
          tokens: tokenCount
        });
      }
    } catch (err) {
      if (err.name === 'AbortError') {
        console.log('OpenRouter generation aborted.');
      } else {
        console.error('OpenRouter Error:', err);
        if (onError) onError(err);
      }
    } finally {
      this.abortController = null;
    }
  }

  /**
   * Simulated interactive demo stream showing exact Gemma 4 MoE + CoT behavior
   */
  async simulateDemo({ onToken, onThought, onComplete, onTtft }) {
    this.abort();
    this.abortController = new AbortController();

    const startTime = performance.now();
    const demo = window.GEMMA_DEMO_DATA || { thought: "Processing...", content: "Hello from Gemma 4!" };

    // Emit thought first
    if (onThought && demo.thought) {
      onThought(demo.thought);
      await new Promise(r => setTimeout(r, 600));
    }

    const words = demo.content.split(' ');
    let accumulated = '';
    let tokenCount = 0;
    const ttft = 142; // typical MoE TTFT in ms
    if (onTtft) onTtft(ttft);

    for (let i = 0; i < words.length; i++) {
      if (this.abortController?.signal?.aborted) break;
      const word = (i === 0 ? '' : ' ') + words[i];
      accumulated += word;
      tokenCount += Math.max(1, Math.round(word.length / 4));

      const duration = (performance.now() - startTime) / 1000;
      const speed = duration > 0 ? (tokenCount / duration).toFixed(1) : '54.2';

      if (onToken) {
        onToken(word, accumulated, {
          ttft: ttft + ' ms',
          speed: speed + ' tok/s',
          duration: duration.toFixed(2) + ' s',
          tokens: tokenCount
        });
      }
      await new Promise(r => setTimeout(r, 35));
    }

    const finalDuration = ((performance.now() - startTime) / 1000).toFixed(2);
    if (onComplete) {
      onComplete(accumulated, {
        ttft: ttft + ' ms',
        speed: (tokenCount / finalDuration).toFixed(1) + ' tok/s',
        duration: finalDuration + ' s',
        tokens: tokenCount,
        thought: demo.thought
      });
    }
    this.abortController = null;
  }
}

window.GoogleGemmaClient = GoogleGemmaClient;
