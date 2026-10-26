/**
 * Gemma 4 Arena App Controller
 * Orchestrates dual-mode streaming, telemetry, view switching, and settings.
 */
document.addEventListener('DOMContentLoaded', () => {
  // Instantiate API Clients
  const googleClient = new GoogleGemmaClient();
  const ollamaClient = new OllamaGemmaClient();

  // State
  let currentMode = 'dual'; // 'dual', 'cloud', 'ollama'
  let isReasoningEnabled = true;
  let isGenerating = false;
  let currentAttachment = null; // { file, mimeType, base64 }

  // DOM Elements
  const arenaGrid = document.getElementById('arenaGrid');
  const modeDualBtn = document.getElementById('modeDualBtn');
  const modeCloudBtn = document.getElementById('modeCloudBtn');
  const modeOllamaBtn = document.getElementById('modeOllamaBtn');

  // Status Indicators
  const cloudStatusDot = document.getElementById('cloudStatusDot');
  const ollamaStatusDot = document.getElementById('ollamaStatusDot');
  const ollamaStatusText = document.getElementById('ollamaStatusText');

  // Panels
  const panelCloud = document.getElementById('panelCloud');
  const panelOllama = document.getElementById('panelOllama');
  const cloudMessageFeed = document.getElementById('cloudMessageFeed');
  const ollamaMessageFeed = document.getElementById('ollamaMessageFeed');
  const cloudEmptyState = document.getElementById('cloudEmptyState');
  const ollamaEmptyState = document.getElementById('ollamaEmptyState');

  // Telemetry Elements
  const cloudTtft = document.getElementById('cloudTtft');
  const cloudSpeed = document.getElementById('cloudSpeed');
  const cloudDuration = document.getElementById('cloudDuration');
  const cloudTokens = document.getElementById('cloudTokens');

  const ollamaTtft = document.getElementById('ollamaTtft');
  const ollamaSpeed = document.getElementById('ollamaSpeed');
  const ollamaDuration = document.getElementById('ollamaDuration');
  const ollamaTokens = document.getElementById('ollamaTokens');

  // Input & Controls
  const promptInput = document.getElementById('promptInput');
  const sendBtn = document.getElementById('sendBtn');
  const thinkingToggleBtn = document.getElementById('thinkingToggleBtn');
  const attachImageBtn = document.getElementById('attachImageBtn');
  const imageFileInput = document.getElementById('imageFileInput');
  const attachmentStaging = document.getElementById('attachmentStaging');
  const attachmentThumbnail = document.getElementById('attachmentThumbnail');
  const attachmentFileName = document.getElementById('attachmentFileName');
  const removeAttachmentBtn = document.getElementById('removeAttachmentBtn');
  const clearChatBtn = document.getElementById('clearChatBtn');
  const runDemoPresetBtn = document.getElementById('runDemoPresetBtn');

  // Settings Modal Elements
  const settingsBtn = document.getElementById('settingsBtn');
  const settingsModal = document.getElementById('settingsModal');
  const closeSettingsBtn = document.getElementById('closeSettingsBtn');
  const saveSettingsBtn = document.getElementById('saveSettingsBtn');
  const resetDefaultsBtn = document.getElementById('resetDefaultsBtn');
  const googleApiKeyInput = document.getElementById('googleApiKeyInput');
  const googleModelSelect = document.getElementById('googleModelSelect');
  const thinkingLevelSelect = document.getElementById('thinkingLevelSelect');
  const ollamaEndpointInput = document.getElementById('ollamaEndpointInput');
  const ollamaModelInput = document.getElementById('ollamaModelInput');
  const systemPromptInput = document.getElementById('systemPromptInput');

  // 1. Initialise Settings & Status Check
  function initSettings() {
    googleApiKeyInput.value = googleClient.getApiKey();
    googleModelSelect.value = googleClient.model;
    ollamaEndpointInput.value = ollamaClient.endpoint;
    ollamaModelInput.value = ollamaClient.model;
    thinkingLevelSelect.value = localStorage.getItem('gemma_thinking_level') || 'high';
    systemPromptInput.value = localStorage.getItem('gemma_system_prompt') || '';

    updateCloudStatusBadge();
    checkOllamaHealth();
  }

  function updateCloudStatusBadge() {
    if (googleClient.getApiKey()) {
      cloudStatusDot.className = 'status-dot active-cloud';
      const isOR = googleClient.isOpenRouterKey();
      cloudStatusDot.parentElement.title = isOR ? 'OpenRouter API Key Configured' : 'Google Cloud API Key Configured';
      const label = cloudStatusDot.parentElement.querySelector('span:last-child');
      if (label) label.innerText = isOR ? 'OpenRouter API' : 'Google API';
    } else {
      cloudStatusDot.className = 'status-dot warning';
      cloudStatusDot.parentElement.title = 'Click Settings to add your Google or OpenRouter API Key';
    }
  }

  async function checkOllamaHealth() {
    const status = await ollamaClient.checkHealth();
    if (status.online) {
      ollamaStatusDot.className = 'status-dot active-ollama';
      ollamaStatusText.innerText = 'Ollama (Online)';
      ollamaStatusDot.parentElement.title = `Ollama Online: Models: ${status.models.join(', ') || 'none'}`;
      
      const emptyDesc = document.getElementById('ollamaEmptyDesc');
      if (emptyDesc) {
        emptyDesc.innerHTML = `Ollama is <strong>online</strong>. Using model <code>${ollamaClient.model}</code>. Ready for inference!`;
      }
    } else {
      ollamaStatusDot.className = 'status-dot offline';
      ollamaStatusText.innerText = 'Ollama (Offline)';
      ollamaStatusDot.parentElement.title = `Ollama Unreachable at ${ollamaClient.endpoint}. Run 'ollama serve'`;
    }
  }

  // Periodic Ollama Health Ping
  setInterval(checkOllamaHealth, 15000);

  // 2. View Mode Navigation
  function setViewMode(mode) {
    currentMode = mode;
    [modeDualBtn, modeCloudBtn, modeOllamaBtn].forEach(b => b.classList.remove('active'));
    arenaGrid.classList.remove('single-cloud-mode', 'single-ollama-mode');

    if (mode === 'dual') {
      modeDualBtn.classList.add('active');
    } else if (mode === 'cloud') {
      modeCloudBtn.classList.add('active');
      arenaGrid.classList.add('single-cloud-mode');
    } else if (mode === 'ollama') {
      modeOllamaBtn.classList.add('active');
      arenaGrid.classList.add('single-ollama-mode');
    }
  }

  modeDualBtn.addEventListener('click', () => setViewMode('dual'));
  modeCloudBtn.addEventListener('click', () => setViewMode('cloud'));
  modeOllamaBtn.addEventListener('click', () => setViewMode('ollama'));

  // 3. Thinking Toggle
  thinkingToggleBtn.addEventListener('click', () => {
    isReasoningEnabled = !isReasoningEnabled;
    thinkingToggleBtn.classList.toggle('active', isReasoningEnabled);
    thinkingToggleBtn.setAttribute('aria-pressed', isReasoningEnabled);
  });

  // 4. Multimodal Image Attachment
  attachImageBtn.addEventListener('click', () => imageFileInput.click());

  imageFileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (event) => {
      currentAttachment = {
        name: file.name,
        mimeType: file.type || 'image/jpeg',
        base64: event.target.result
      };
      attachmentThumbnail.src = currentAttachment.base64;
      attachmentFileName.innerText = file.name;
      attachmentStaging.style.display = 'flex';
    };
    reader.readAsDataURL(file);
  });

  removeAttachmentBtn.addEventListener('click', () => {
    currentAttachment = null;
    imageFileInput.value = '';
    attachmentStaging.style.display = 'none';
  });

  // 5. Preset Chips & Suggestion Chips
  document.querySelectorAll('.preset-chip[data-preset]').forEach(btn => {
    btn.addEventListener('click', () => {
      const presetKey = btn.getAttribute('data-preset');
      const preset = window.GEMMA_PRESETS && window.GEMMA_PRESETS[presetKey];
      if (preset) {
        promptInput.value = preset.prompt;
        adjustPromptHeight();
        promptInput.focus();
      }
    });
  });

  if (runDemoPresetBtn) {
    runDemoPresetBtn.addEventListener('click', () => {
      promptInput.value = "Explain Gemma 4's Mixture-of-Experts (MoE) routing dynamics and active parameter efficiency.";
      adjustPromptHeight();
      executePrompt(true); // force demo mode simulation
    });
  }

  document.querySelectorAll('.quick-chip').forEach(chip => {
    chip.addEventListener('click', () => {
      promptInput.value = chip.getAttribute('data-prompt');
      adjustPromptHeight();
      executePrompt();
    });
  });

  // 6. Textarea Auto-Resize & Keyboard
  function adjustPromptHeight() {
    promptInput.style.height = 'auto';
    promptInput.style.height = Math.min(promptInput.scrollHeight, 120) + 'px';
  }

  promptInput.addEventListener('input', adjustPromptHeight);

  promptInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      executePrompt();
    }
  });

  sendBtn.addEventListener('click', () => {
    if (isGenerating) {
      stopGeneration();
    } else {
      executePrompt();
    }
  });

  function stopGeneration() {
    googleClient.abort();
    ollamaClient.abort();
    setGeneratingState(false);
  }

  function setGeneratingState(generating) {
    isGenerating = generating;
    sendBtn.classList.toggle('is-generating', generating);
    if (generating) {
      sendBtn.innerHTML = `<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="6" width="12" height="12" rx="2"/></svg>`;
      sendBtn.title = "Stop Generation";
      panelCloud.classList.add('is-generating');
      panelOllama.classList.add('is-generating');
    } else {
      sendBtn.innerHTML = `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>`;
      sendBtn.title = "Send Prompt (Enter)";
      panelCloud.classList.remove('is-generating');
      panelOllama.classList.remove('is-generating');
    }
  }

  // 7. Message Elements Builder
  function appendUserMessage(feed, text, attachment) {
    const msgDiv = document.createElement('div');
    msgDiv.className = 'chat-message user-message';
    
    let contentHtml = '';
    if (attachment && attachment.base64) {
      contentHtml += `<img src="${attachment.base64}" class="message-attachment-preview" alt="Uploaded Image">`;
    }
    contentHtml += `<div class="message-bubble">${window.MarkdownRenderer ? window.MarkdownRenderer.render(text) : text}</div>`;
    
    msgDiv.innerHTML = contentHtml;
    feed.appendChild(msgDiv);
    feed.scrollTop = feed.scrollHeight;
  }

  function createModelMessageCard(feed, providerLabel) {
    const msgDiv = document.createElement('div');
    msgDiv.className = 'chat-message model-message';

    const reasoningBlock = document.createElement('div');
    reasoningBlock.className = 'reasoning-block';
    reasoningBlock.style.display = 'none';
    reasoningBlock.innerHTML = `
      <div class="reasoning-header">
        <div class="reasoning-header-left">
          <span class="reasoning-pulse-dot"></span>
          <span>✦ Thought Process (Reasoning)</span>
        </div>
        <span class="toggle-icon">▼</span>
      </div>
      <div class="reasoning-content"></div>
    `;

    // Collapsible click
    const header = reasoningBlock.querySelector('.reasoning-header');
    header.addEventListener('click', () => {
      reasoningBlock.classList.toggle('collapsed');
      const icon = header.querySelector('.toggle-icon');
      icon.innerText = reasoningBlock.classList.contains('collapsed') ? '▶' : '▼';
    });

    const bubble = document.createElement('div');
    bubble.className = 'message-bubble markdown-body';
    bubble.innerHTML = '<span class="status-dot" style="display:inline-block; animation: pulse 1s infinite;"></span> <em style="color: var(--text-muted)">Thinking...</em>';

    msgDiv.appendChild(reasoningBlock);
    msgDiv.appendChild(bubble);
    feed.appendChild(msgDiv);
    feed.scrollTop = feed.scrollHeight;

    return {
      container: msgDiv,
      reasoningBlock,
      reasoningContent: reasoningBlock.querySelector('.reasoning-content'),
      bubble,
      updateThought: (thought) => {
        if (!thought) return;
        reasoningBlock.style.display = 'block';
        reasoningBlock.querySelector('.reasoning-content').innerText = thought;
        feed.scrollTop = feed.scrollHeight;
      },
      updateContent: (content) => {
        bubble.innerHTML = window.MarkdownRenderer ? window.MarkdownRenderer.render(content) : content;
        feed.scrollTop = feed.scrollHeight;
      },
      setInteractiveApiKeyCard: (promptText) => {
        bubble.innerHTML = `
          <div style="padding: 12px 14px; background: rgba(59, 130, 246, 0.08); border: 1px solid rgba(59, 130, 246, 0.25); border-radius: 10px;">
            <div style="font-weight: 600; color: #93c5fd; margin-bottom: 6px; display: flex; align-items: center; gap: 6px;">
              <span>🔑 Google Cloud or OpenRouter API Key</span>
            </div>
            <div style="font-size: 0.82rem; color: #cbd5e1; margin-bottom: 10px;">
              Paste your Google AI Studio key (<code>AIzaSy...</code>) or OpenRouter key (<code>sk-or-v1-...</code>) to stream <code>gemma-4-26b-a4b-it</code>:
            </div>
            <div style="display: flex; gap: 8px; margin-bottom: 10px;">
              <input type="password" id="inlineKeyInput_${Date.now()}" class="form-input inline-key-input" style="flex: 1; padding: 7px 10px; font-size: 0.82rem;" placeholder="AIzaSy... or sk-or-v1-...">
              <button class="btn-primary inline-key-save-btn" style="padding: 7px 14px; font-size: 0.82rem; white-space: nowrap;">Save &amp; Run</button>
            </div>
            <div style="display: flex; align-items: center; justify-content: space-between; font-size: 0.74rem; flex-wrap: wrap; gap: 6px;">
              <span style="color: var(--text-secondary);">
                Get key: <a href="https://aistudio.google.com/app/apikey" target="_blank" rel="noopener" style="color: #60a5fa; text-decoration: underline;">Google AI Studio (Free)</a> or <a href="https://openrouter.ai/keys" target="_blank" rel="noopener" style="color: #c084fc; text-decoration: underline;">OpenRouter</a>
              </span>
              <button class="inline-demo-btn" style="background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255,255,255,0.18); color: #fff; padding: 4px 10px; border-radius: 6px; cursor: pointer; font-size: 0.74rem;">▶ Try Interactive Demo</button>
            </div>
          </div>
        `;

        const input = bubble.querySelector('.inline-key-input');
        const saveBtn = bubble.querySelector('.inline-key-save-btn');
        const demoBtn = bubble.querySelector('.inline-demo-btn');

        saveBtn.addEventListener('click', () => {
          const val = input.value.trim();
          if (val) {
            googleClient.setApiKey(val);
            googleApiKeyInput.value = val;
            updateCloudStatusBadge();
            bubble.innerHTML = '<span class="status-dot" style="display:inline-block; animation: pulse 1s infinite;"></span> <em style="color: var(--text-muted)">Key saved. Starting generation...</em>';
            executePrompt();
          } else {
            input.focus();
          }
        });

        demoBtn.addEventListener('click', () => {
          bubble.innerHTML = '<span class="status-dot" style="display:inline-block; animation: pulse 1s infinite;"></span> <em style="color: var(--text-muted)">Streaming simulated Gemma 4 MoE response...</em>';
          googleClient.simulateDemo({
            onThought: (th) => {
              reasoningBlock.style.display = 'block';
              reasoningBlock.querySelector('.reasoning-content').innerText = th;
              feed.scrollTop = feed.scrollHeight;
            },
            onToken: (tok, acc, telemetry) => {
              bubble.innerHTML = window.MarkdownRenderer ? window.MarkdownRenderer.render(acc) : acc;
              cloudSpeed.innerText = telemetry.speed;
              cloudDuration.innerText = telemetry.duration;
              cloudTokens.innerText = telemetry.tokens;
              feed.scrollTop = feed.scrollHeight;
            },
            onComplete: (acc, telemetry) => {
              bubble.innerHTML = window.MarkdownRenderer ? window.MarkdownRenderer.render(acc) : acc;
              cloudTtft.innerText = telemetry.ttft;
              cloudSpeed.innerText = telemetry.speed;
              cloudDuration.innerText = telemetry.duration;
              cloudTokens.innerText = telemetry.tokens;
            }
          });
        });

        feed.scrollTop = feed.scrollHeight;
      },
      setInteractiveOllamaCard: () => {
        bubble.innerHTML = `
          <div style="padding: 12px 14px; background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 10px;">
            <div style="font-weight: 600; color: #34d399; margin-bottom: 6px;">🖥️ Local Ollama Setup (127.0.0.1:11434)</div>
            <div style="font-size: 0.82rem; color: #cbd5e1; margin-bottom: 8px;">
              Could not reach local daemon at <code>${ollamaClient.endpoint}</code>. To start:
            </div>
            <div style="background: rgba(0,0,0,0.4); padding: 8px 10px; border-radius: 6px; font-family: var(--font-mono); font-size: 0.76rem; color: #a7f3d0; margin-bottom: 10px; line-height: 1.6;">
              1. Run in terminal: <code>ollama serve</code><br>
              2. Pull model: <code>ollama pull ${ollamaClient.model}</code>
            </div>
            <div style="display: flex; gap: 8px; flex-wrap: wrap;">
              <button class="btn-secondary inline-ollama-check-btn" style="font-size: 0.78rem; padding: 5px 12px;">🔄 Check Connection</button>
              <button class="inline-ollama-demo-btn" style="background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.35); color: #34d399; font-size: 0.78rem; padding: 5px 12px; border-radius: 6px; cursor: pointer;">▶ Try Simulated Local Stream</button>
            </div>
          </div>
        `;

        const checkBtn = bubble.querySelector('.inline-ollama-check-btn');
        const demoBtn = bubble.querySelector('.inline-ollama-demo-btn');

        checkBtn.addEventListener('click', async () => {
          checkBtn.innerText = 'Checking...';
          const res = await ollamaClient.checkHealth();
          if (res.online) {
            checkBtn.innerText = 'Online!';
            checkOllamaHealth();
            setTimeout(() => executePrompt(), 500);
          } else {
            checkBtn.innerText = 'Still Offline';
            setTimeout(() => checkBtn.innerText = '🔄 Check Connection', 2000);
          }
        });

        demoBtn.addEventListener('click', () => {
          bubble.innerHTML = '<span class="status-dot" style="display:inline-block; animation: pulse 1s infinite;"></span> <em style="color: var(--text-muted)">Streaming simulated Local Ollama response...</em>';
          googleClient.simulateDemo({
            onThought: (th) => {
              reasoningBlock.style.display = 'block';
              reasoningBlock.querySelector('.reasoning-content').innerText = th;
              feed.scrollTop = feed.scrollHeight;
            },
            onToken: (tok, acc, telemetry) => {
              bubble.innerHTML = window.MarkdownRenderer ? window.MarkdownRenderer.render(acc) : acc;
              ollamaSpeed.innerText = '68.4 tok/s';
              ollamaDuration.innerText = telemetry.duration;
              ollamaTokens.innerText = telemetry.tokens;
              feed.scrollTop = feed.scrollHeight;
            },
            onComplete: (acc, telemetry) => {
              bubble.innerHTML = window.MarkdownRenderer ? window.MarkdownRenderer.render(acc) : acc;
              ollamaTtft.innerText = '85 ms';
              ollamaSpeed.innerText = '71.2 tok/s';
              ollamaDuration.innerText = telemetry.duration;
              ollamaTokens.innerText = telemetry.tokens;
            }
          });
        });

        feed.scrollTop = feed.scrollHeight;
      },
      setError: (errMsg) => {
        bubble.innerHTML = `<span style="color: var(--gemma-danger)">⚠️ ${window.MarkdownRenderer ? window.MarkdownRenderer.escapeHtml(errMsg) : errMsg}</span>`;
      }
    };
  }

  // 8. Main Execution Orchestrator
  async function executePrompt(forceDemo = false) {
    const text = promptInput.value.trim();
    if (!text && !currentAttachment && !forceDemo) return;

    const promptText = text || "Describe this image in detail.";
    const attachment = currentAttachment;

    promptInput.value = '';
    adjustPromptHeight();
    currentAttachment = null;
    imageFileInput.value = '';
    attachmentStaging.style.display = 'none';

    if (cloudEmptyState) cloudEmptyState.style.display = 'none';
    if (ollamaEmptyState) ollamaEmptyState.style.display = 'none';

    setGeneratingState(true);

    const systemPrompt = localStorage.getItem('gemma_system_prompt') || '';
    const thinkingLevel = isReasoningEnabled ? (localStorage.getItem('gemma_thinking_level') || 'high') : 'off';

    const tasks = [];

    // Target 1: Google Cloud Gemma
    if (currentMode === 'dual' || currentMode === 'cloud') {
      appendUserMessage(cloudMessageFeed, promptText, attachment);
      const cloudCard = createModelMessageCard(cloudMessageFeed, 'Google Cloud');

      cloudTtft.innerText = '...';
      cloudSpeed.innerText = '...';
      cloudDuration.innerText = '...';
      cloudTokens.innerText = '...';

      if (forceDemo) {
        const demoTask = googleClient.simulateDemo({
          onThought: (th) => cloudCard.updateThought(th),
          onToken: (tok, acc, telemetry) => {
            cloudCard.updateContent(acc);
            cloudSpeed.innerText = telemetry.speed;
            cloudDuration.innerText = telemetry.duration;
            cloudTokens.innerText = telemetry.tokens;
          },
          onComplete: (acc, telemetry) => {
            cloudCard.updateContent(acc);
            cloudTtft.innerText = telemetry.ttft;
            cloudSpeed.innerText = telemetry.speed;
            cloudDuration.innerText = telemetry.duration;
            cloudTokens.innerText = telemetry.tokens;
          }
        });
        tasks.push(demoTask);
      } else {
        const cloudTask = googleClient.generateStream({
          prompt: promptText,
          systemInstruction: systemPrompt,
          thinkingLevel: thinkingLevel,
          imageAttachment: attachment,
          onTtft: (ttft) => {
            cloudTtft.innerText = ttft + ' ms';
          },
          onThought: (thought) => {
            cloudCard.updateThought(thought);
          },
          onToken: (token, fullText, telemetry) => {
            cloudCard.updateContent(fullText);
            cloudSpeed.innerText = telemetry.speed;
            cloudDuration.innerText = telemetry.duration;
            cloudTokens.innerText = telemetry.tokens;
          },
          onComplete: (fullText, telemetry) => {
            cloudCard.updateContent(fullText);
            if (telemetry.thought) {
              cloudCard.updateThought(telemetry.thought);
              cloudCard.reasoningBlock.classList.add('collapsed');
              cloudCard.reasoningBlock.querySelector('.toggle-icon').innerText = '▶';
            }
            cloudTtft.innerText = telemetry.ttft;
            cloudSpeed.innerText = telemetry.speed;
            cloudDuration.innerText = telemetry.duration;
            cloudTokens.innerText = telemetry.tokens;
          },
          onError: (err) => {
            if (err.isMissingKey || !googleClient.getApiKey()) {
              cloudCard.setInteractiveApiKeyCard(promptText);
            } else {
              cloudCard.setError(err.message);
            }
          }
        });
        tasks.push(cloudTask);
      }
    }

    // Target 2: Local Ollama Gemma
    if (currentMode === 'dual' || currentMode === 'ollama') {
      appendUserMessage(ollamaMessageFeed, promptText, attachment);
      const ollamaCard = createModelMessageCard(ollamaMessageFeed, 'Local Ollama');

      ollamaTtft.innerText = '...';
      ollamaSpeed.innerText = '...';
      ollamaDuration.innerText = '...';
      ollamaTokens.innerText = '...';

      if (forceDemo) {
        const ollamaDemoTask = googleClient.simulateDemo({
          onThought: (th) => ollamaCard.updateThought(th),
          onToken: (tok, acc, telemetry) => {
            ollamaCard.updateContent(acc);
            ollamaSpeed.innerText = '74.8 tok/s';
            ollamaDuration.innerText = telemetry.duration;
            ollamaTokens.innerText = telemetry.tokens;
          },
          onComplete: (acc, telemetry) => {
            ollamaCard.updateContent(acc);
            ollamaTtft.innerText = '72 ms';
            ollamaSpeed.innerText = '76.1 tok/s';
            ollamaDuration.innerText = telemetry.duration;
            ollamaTokens.innerText = telemetry.tokens;
          }
        });
        tasks.push(ollamaDemoTask);
      } else {
        const ollamaTask = ollamaClient.generateStream({
          prompt: promptText,
          systemInstruction: systemPrompt,
          imageAttachment: attachment,
          onTtft: (ttft) => {
            ollamaTtft.innerText = ttft + ' ms';
          },
          onThought: (thought) => {
            ollamaCard.updateThought(thought);
          },
          onToken: (token, fullText, telemetry) => {
            ollamaCard.updateContent(fullText);
            ollamaSpeed.innerText = telemetry.speed;
            ollamaDuration.innerText = telemetry.duration;
            ollamaTokens.innerText = telemetry.tokens;
          },
          onComplete: (fullText, telemetry) => {
            ollamaCard.updateContent(fullText);
            if (telemetry.thought) {
              ollamaCard.updateThought(telemetry.thought);
              ollamaCard.reasoningBlock.classList.add('collapsed');
              ollamaCard.reasoningBlock.querySelector('.toggle-icon').innerText = '▶';
            }
            ollamaTtft.innerText = telemetry.ttft;
            ollamaSpeed.innerText = telemetry.speed;
            ollamaDuration.innerText = telemetry.duration;
            ollamaTokens.innerText = telemetry.tokens;
          },
          onError: (err) => {
            ollamaCard.setInteractiveOllamaCard();
          }
        });
        tasks.push(ollamaTask);
      }
    }

    try {
      await Promise.allSettled(tasks);
    } finally {
      setGeneratingState(false);
    }
  }

  // 9. Clear Chat
  clearChatBtn.addEventListener('click', () => {
    if (confirm('Clear conversation history from both panels?')) {
      cloudMessageFeed.innerHTML = '';
      ollamaMessageFeed.innerHTML = '';
      if (cloudEmptyState) {
        cloudMessageFeed.appendChild(cloudEmptyState);
        cloudEmptyState.style.display = 'block';
      }
      if (ollamaEmptyState) {
        ollamaMessageFeed.appendChild(ollamaEmptyState);
        ollamaEmptyState.style.display = 'block';
      }
      cloudTtft.innerText = '—';
      cloudSpeed.innerText = '— tok/s';
      cloudDuration.innerText = '—';
      cloudTokens.innerText = '—';
      ollamaTtft.innerText = '—';
      ollamaSpeed.innerText = '— tok/s';
      ollamaDuration.innerText = '—';
      ollamaTokens.innerText = '—';
    }
  });

  // 10. Copy Responses
  document.getElementById('copyCloudResponseBtn').addEventListener('click', () => {
    const bubbles = cloudMessageFeed.querySelectorAll('.model-message .message-bubble');
    if (bubbles.length) {
      const text = bubbles[bubbles.length - 1].innerText;
      navigator.clipboard.writeText(text);
      alert('Copied latest Google Cloud Gemma response!');
    }
  });

  document.getElementById('copyOllamaResponseBtn').addEventListener('click', () => {
    const bubbles = ollamaMessageFeed.querySelectorAll('.model-message .message-bubble');
    if (bubbles.length) {
      const text = bubbles[bubbles.length - 1].innerText;
      navigator.clipboard.writeText(text);
      alert('Copied latest Local Ollama response!');
    }
  });

  // 11. Settings Dialog
  function openSettings() {
    settingsModal.classList.add('open');
  }

  function closeSettings() {
    settingsModal.classList.remove('open');
  }

  settingsBtn.addEventListener('click', openSettings);
  closeSettingsBtn.addEventListener('click', closeSettings);

  settingsModal.addEventListener('click', (e) => {
    if (e.target === settingsModal) closeSettings();
  });

  saveSettingsBtn.addEventListener('click', () => {
    googleClient.setApiKey(googleApiKeyInput.value);
    googleClient.model = googleModelSelect.value.trim() || 'gemma-4-26b-a4b-it';
    ollamaClient.setEndpoint(ollamaEndpointInput.value);
    ollamaClient.setModel(ollamaModelInput.value);

    localStorage.setItem('gemma_thinking_level', thinkingLevelSelect.value);
    localStorage.setItem('gemma_system_prompt', systemPromptInput.value);

    document.getElementById('cloudModelChip').innerText = googleClient.model;
    document.getElementById('ollamaModelChip').innerText = ollamaClient.model;

    updateCloudStatusBadge();
    checkOllamaHealth();
    closeSettings();
  });

  resetDefaultsBtn.addEventListener('click', () => {
    googleModelSelect.value = 'gemma-4-26b-a4b-it';
    thinkingLevelSelect.value = 'high';
    ollamaEndpointInput.value = 'http://127.0.0.1:11434';
    ollamaModelInput.value = 'gemma4';
    systemPromptInput.value = '';
  });

  // Run initial setup
  initSettings();
});
