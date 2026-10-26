# Gemma 4 Arena: Google DeepMind Open Model Workbench

A high-performance, dual-mode AI Playground & Benchmark application comparing **Google Cloud API** (`gemma-4-26b-a4b-it`) and **Local Ollama** (`gemma4`) side-by-side with real-time streaming, telemetry metrics, and native Chain-of-Thought (CoT) reasoning.

Built strictly according to [`brand/STYLE_GUIDE.md`](brand/STYLE_GUIDE.md), [`brand/template.html`](brand/template.html), and [`brand/theme.css`](brand/theme.css).

---

## 🌟 Key Highlights

1. **Brand Design System**:
   - Master layout in [`brand/template.html`](brand/template.html) and design tokens in [`brand/theme.css`](brand/theme.css).
   - Glassmorphic Obsidian canvas (`#06080f`) with Gemma auroral gradients (`#3B82F6` to `#8B5CF6`).
   - Compliant with Google DeepMind open model trademark attribution standards.

2. **Google Cloud Gemini API Integration**:
   - Model: `gemma-4-26b-a4b-it` (MoE architecture with ~4B active / 26B total parameters).
   - Follows [Google AI Gemma documentation](https://ai.google.dev/gemma/docs/core/gemma_on_gemini_api).
   - Server-Sent Events (SSE) streaming with active `thinking_config` (`HIGH` / `LOW` / `OFF`).
   - Multimodal image attachment support.

3. **Local Ollama Integration**:
   - Model: `gemma4` (running locally at `http://127.0.0.1:11434/api/chat`).
   - Automatic daemon health detection and model listing (`/api/tags`).
   - Zero external latency, 100% private and offline inference.

4. **Dual-Mode Arena & Benchmark Telemetry**:
   - **Side-by-Side Arena**: Simultaneously dispatch identical prompts to Cloud and Local models.
   - **Real-Time Telemetry HUD**: Time-To-First-Token (TTFT), tokens/sec throughput, generation duration, and token count.
   - **Collapsible Reasoning Drawer**: Live visualization of Gemma 4's internal thought process.

---

## 🚀 Quick Start

### 1. Launch the Application

The workbench comes with a zero-dependency server that also provides an optional CORS proxy for Ollama:

```bash
npm start
```
Or with Node directly:
```bash
node server.js
```
Open **[http://localhost:3000](http://localhost:3000)** in your browser.

> You can also open `index.html` directly in any modern browser!

---

## ⚙️ Configuration & Model Setup

### A. Google Cloud API (`gemma-4-26b-a4b-it`)
1. Click the **Settings** (gear icon) in the top-right corner of the workbench.
2. Enter your Google AI Studio API key (stored securely in browser `localStorage`).
3. You can obtain a free key at [Google AI Studio](https://aistudio.google.com/app/apikey).
4. Configure the desired **Reasoning Level**:
   - `High`: Full DeepMind Chain-of-Thought (CoT) reasoning.
   - `Low`: Concise thinking before response.
   - `Off`: Direct generation.

### B. Local Ollama (`gemma4`)
1. Ensure Ollama is installed and running on your system:
   ```bash
   ollama serve
   ```
2. Pull the Gemma 4 model:
   ```bash
   ollama pull gemma4
   # or pull a specific Gemma variant:
   ollama pull gemma:latest
   ```
3. The status indicator in the header will automatically switch to **Ollama (Online)** with a glowing mint badge.

---

## 📁 Repository Structure

```
.
├── brand/
│   ├── STYLE_GUIDE.md        # Comprehensive brand guide for Gemma 4 & design system
│   ├── theme.css             # Unified CSS tokens, animations, responsive grid, glassmorphism
│   └── template.html         # Master semantic layout blueprint
├── js/
│   ├── app.js                # Application controller & dual-stream synchronization
│   ├── google-api.js         # Gemini API client for gemma-4-26b-a4b-it (SSE streaming)
│   ├── ollama-api.js         # Local Ollama client (127.0.0.1:11434/api/chat)
│   ├── markdown-renderer.js  # Streaming markdown parser with syntax highlighted code blocks
│   └── presets.js            # Curated benchmarks (Deep Reasoning, MoE Router, Latency)
├── index.html                # Main application interface using brand template & theme
├── server.js                 # Zero-dependency static server + streaming CORS proxy
├── package.json              # Project scripts and metadata
└── README.md                 # Complete documentation and setup guide
```

---

## ⚖️ License & Attribution

*Gemma is an open model family developed by Google DeepMind. Google, Gemma, and Gemini are trademarks of Google LLC.*
