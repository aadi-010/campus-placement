/**
 * Google Gemini API Client for Gemma 4 (gemma-4-26b-a4b-it)
 * Follows official guide: https://ai.google.dev/gemma/docs/core/gemma_on_gemini_api
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
    thinkingLevel = 'high', // 'high', 'low', 'off'
    imageAttachment = null, // { mimeType, base64 }
    onToken,
    onThought,
    onComplete,
    onError,
    onTtft
  }) {
    const key = this.getApiKey();
    if (!key) {
      if (onError) onError(new Error("Google Gemini API Key is missing. Click the settings gear icon to configure your key."));
      return;
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

    // System instruction
    if (systemInstruction && systemInstruction.trim()) {
      payload.systemInstruction = {
        parts: [{ text: systemInstruction.trim() }]
      };
    }

    // Generation Config & Thinking Configuration
    payload.generationConfig = {
      temperature: 0.7,
      topP: 0.95
    };

    if (thinkingLevel && thinkingLevel !== 'off') {
      payload.generationConfig.thinkingConfig = {
        thinkingLevel: thinkingLevel.toUpperCase() // HIGH or LOW
      };
    }

    const endpoint = `${this.baseUrl}/models/${encodeURIComponent(this.model)}:streamGenerateContent?key=${encodeURIComponent(key)}&alt=sse`;

    try {
      const response = await fetch(endpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
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
        buffer = lines.pop(); // keep partial line in buffer

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
              // Check for thought tokens
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

            // Usage metadata token count if provided by API
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
}

window.GoogleGemmaClient = GoogleGemmaClient;
