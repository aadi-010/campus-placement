# Gemma 4 Brand & Design System Style Guide

> **Version:** 1.0.0  
> **Target Models:** Google Cloud API (`gemma-4-26b-a4b-it`) & Local Ollama (`gemma4`)  
> **Brand Standard:** Google DeepMind Open Model Aesthetics  

---

## 1. Brand Identity & Vision

Gemma is Google’s open-weights family of state-of-the-art models built from Gemini 3 research. The design language for Gemma applications merges **scientific precision**, **computational intelligence**, and **ethereal warmth**. 

Applications built on this brand standard must balance:
- **Clarity over Clutter:** High data-density interfaces designed for developers, researchers, and engineers without sensory overload.
- **Glassmorphic Depth:** Subtle multi-layered elevation with translucent backdrops (`rgba(17, 24, 39, 0.75)`) and ultra-fine boundary borders (`rgba(255, 255, 255, 0.08)`).
- **Dynamic Dual-Core Telemetry:** Clear visual dichotomy between **Google Cloud API** (Azure & Cyber Violet) and **Local Ollama Inference** (Emerald Mint & Jade).

---

## 2. Color Palette & Design Tokens

### Primary Canvas (Dark Theme Native)
- `--bg-canvas`: `#06080F` (Infinite obsidian deep canvas)
- `--bg-surface`: `#0B0F19` (Card and panel surface)
- `--bg-surface-elevated`: `#121826` (Floating menus, modals, tooltips)
- `--bg-glass`: `rgba(15, 23, 42, 0.65)` with `backdrop-filter: blur(16px)`

### Gemma Auroral Accent Gradient
- `--gradient-gemma`: `linear-gradient(135deg, #3B82F6 0%, #8B5CF6 45%, #EC4899 100%)`
- `--gradient-gemma-glow`: `radial-gradient(circle at 50% 0%, rgba(139, 92, 246, 0.18) 0%, transparent 70%)`

### Provider Distinction Tokens
| Provider | Primary Accent | Glow Token | Status Badge Token |
| :--- | :--- | :--- | :--- |
| **Google Cloud (`gemma-4-26b-a4b-it`)** | `#3B82F6` (Electric Blue) | `rgba(59, 130, 246, 0.25)` | Blue Glow (`#60A5FA`) |
| **Local Ollama (`gemma4`)** | `#10B981` (Emerald Mint) | `rgba(16, 185, 129, 0.25)` | Mint Pulse (`#34D399`) |
| **Comparative Arena** | `#F59E0B` (Amber Radiant) | `rgba(245, 158, 11, 0.25)` | Amber Flare (`#FBBF24`) |

### Text & Hierarchy
- `--text-primary`: `#F8FAFC` (Highest contrast typography, 100% legibility)
- `--text-secondary`: `#94A3B8` (Labels, metadata, descriptive hints)
- `--text-muted`: `#64748B` (Inactive states, placeholders, timestamps)
- `--border-subtle`: `rgba(255, 255, 255, 0.08)`
- `--border-focus`: `rgba(139, 92, 246, 0.5)`

---

## 3. Typography Standards

The typography system relies on three complementary typefaces loaded via Google Fonts:

1. **Brand Headings & Displays:**  
   `font-family: 'Outfit', sans-serif;`  
   Weight: `600`, `700`. Used for Hero titles, modal headings, and telemetry numbers.

2. **Interface & Message Content:**  
   `font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;`  
   Weight: `400`, `500`. Engineered for optimal screen readability during long conversation flows.

3. **Code & Telemetry HUD:**  
   `font-family: 'JetBrains Mono', 'Fira Code', monospace;`  
   Weight: `400`, `500`. Used for code blocks, token counters, latency metrics, and API paths.

---

## 4. UI Layout & Architecture

Every Gemma interface must conform to the **Tri-Zone Responsive Layout**:

```
+------------------------------------------------------------------------+
| TOP BAR: Brand Badge | Provider Status Pills | Mode Tabs | Settings     |
+------------------------------------------------------------------------+
|                                                                        |
|  [SPLIT COMPARISON / SINGLE CHAT / BENCHMARK WORKSPACE]                |
|  +--------------------------------+  +--------------------------------+ |
|  | GOOGLE CLOUD INFERENCE         |  | LOCAL OLLAMA INFERENCE         | |
|  | Model: gemma-4-26b-a4b-it      |  | Model: gemma4 (127.0.0.1:11434)| |
|  | - Telemetry: TTFT, tok/s, ms   |  | - Telemetry: TTFT, tok/s, ms   | |
|  | - Collapsible Reasoning drawer |  | - Collapsible Reasoning drawer | |
|  | - Live streaming chat stream   |  | - Live streaming chat stream   | |
|  +--------------------------------+  +--------------------------------+ |
|                                                                        |
+------------------------------------------------------------------------+
| PROMPT DOCK: Multimodal Attachment | Reasoning Toggle | Send Button     |
+------------------------------------------------------------------------+
```

---

## 5. Gemma 4 MoE & Reasoning Visual Conventions

Gemma 4 introduces **Mixture-of-Experts (MoE)** and native **Reasoning (Chain of Thought)**:

1. **Reasoning Collapsible Accordion:**
   - Must be styled in a subtle tinted container (`background: rgba(139, 92, 246, 0.06); border-left: 3px solid #8B5CF6`).
   - Includes a collapsible header: `✦ Thought Process (Reasoning)` with token count and computation duration.
   - Defaults to open while streaming thoughts, gracefully folds once final response generation starts.

2. **Telemetry Badges:**
   - Every completed generation displays:
     * **Time To First Token (TTFT)**
     * **Throughput (Tokens / Sec)**
     * **Total Latency (ms or s)**
     * **Active Parameters** (e.g. `~4B active / 26B total`)

3. **Live Streaming Indicators:**
   - Active streams feature a gentle pulse cursor (`animation: pulse 1s infinite`).
   - Stop generation button with tactile red accent (`#EF4444`).

---

## 6. Legal & Attribution Notice

All deployments must display the trademark attribution line in the footer:
> *"Gemma is an open model family developed by Google DeepMind. Google, Gemma, and Gemini are trademarks of Google LLC."*
