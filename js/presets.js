/**
 * Gemma 4 Curated Prompt Presets
 * Designed for evaluating reasoning, MoE dynamics, coding, and latency.
 */
window.GEMMA_PRESETS = {
  reasoning: {
    title: "Deep Reasoning Challenge",
    prompt: `Solve this complex logic puzzle with step-by-step reasoning:

A group of 3 philosophers (Alice, Bob, and Charlie) are sitting in a circle. Each wears a red or blue hat.
- Alice sees Bob's hat is blue and Charlie's hat is red.
- Bob sees Alice's hat is blue and Charlie's hat is red.
- Charlie sees Alice's hat is blue and Bob's hat is blue.

A referee announces: "At least one of you has a red hat."
The referee then asks Alice: "Do you know your hat color?" Alice answers: "No."
The referee asks Bob: "Do you know your hat color?" Bob answers: "No."
What does Charlie answer, and what is Charlie's hat color? Explain your deduction step-by-step.`
  },
  coding: {
    title: "MoE Router Code Challenge",
    prompt: `Write a clean, production-ready Python class implementing a top-k Mixture-of-Experts (MoE) routing layer like the one used in Gemma 4:
1. Softmax gating over N experts with top-k selection (e.g. N=16, k=2 or top-8).
2. Capacity factor and auxiliary load balancing loss calculation.
3. Include clear docstrings, type annotations, and an example tensor forward pass.`
  },
  creative: {
    title: "Scientific Metaphor",
    prompt: `Explain how Gemma 4's Mixture-of-Experts (MoE) architecture works using the metaphor of a busy renaissance artisan workshop or orchestra. Keep the tone engaging, visually evocative, yet technically precise regarding active vs total parameters.`
  },
  speed: {
    title: "Latency Benchmark (100 tok)",
    prompt: `List the top 5 key architectural innovations in Google's Gemma 4 family. Keep each point to exactly two concise sentences so we can measure exact throughput and Time-To-First-Token (TTFT).`
  }
};

window.GEMMA_DEMO_DATA = {
  thought: `1. Analyzing the user input: "hey".
2. Intent: Greeting and initial connection verification.
3. Architecture check: Operating in Gemma 4 MoE mode (~4B active parameters routed across 26B total parameters via top-8 fine-grained expert routing).
4. Formulating response: Deliver a crisp, friendly greeting, outline active workbench features, and prompt the user for their first query or benchmark test.`,
  content: `Hello! 👋 I'm **Gemma 4**, Google DeepMind's open Mixture-of-Experts (MoE) model running with native Chain-of-Thought reasoning.

The **Gemma 4 Arena Workbench** is operational:
- **Cloud API (`gemma-4-26b-a4b-it`)**: High-throughput MoE with DeepMind reasoning.
- **Local Ollama (`gemma4`)**: Privacy-first, local zero-cloud inference at \`127.0.0.1:11434\`.
- **Side-by-Side Arena**: Compare latency (TTFT), tokens/sec, and thought depth.

Feel free to try the **presets** above or ask a complex logic, coding, or science question!`
};

