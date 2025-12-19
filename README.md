# Holographic Horizon Shield v2 🛡️🌌

> "In the silence beyond the event horizon, no malice escapes the light.  
> The shield holds—not by force, but by perfect, holographic vigilance."

**Holographic Horizon Shield v2** is an open-source, sci-fi-inspired defense system for Large Language Models (LLMs). Drawing from black hole physics, it creates layered "holographic" boundaries that detect and neutralize threats like prompt injections, jailbreaks, adversarial attacks, and data poisoning—**before** they reach the core model.

Built with **Microsoft's Phi-3-mini** for fast, private, on-device inference. No cloud calls. Low resource footprint. Pure Python.

- 🛡️ Multi-layer boundary scans
- 🌌 Real-time holographic dashboard
- 🔬 Phi-3 powered classification
- 🚀 Early prototype • MIT Licensed • Actively evolving

Refs: [Original Holographic Horizon Shield repo](https://github.com/...original-if-exists)

## Epic Visuals

![Central holographic shield sphere with Phi-3 gauges monitoring incoming threats](IMG_8410.jpeg)
*Central holographic shield sphere with Phi-3 gauges monitoring incoming threats*

![Neon control interface for adversarial attack simulation](IMG_8411.jpeg)
*Neon control interface for adversarial attack simulation*

![Layered threat detection visualization with waveform heatmaps](IMG_8412.jpeg)
*Layered threat detection visualization with waveform heatmaps*

![Hand-activated neon UI with digital rain and boundary effects](IMG_8413.jpeg)
*Hand-activated neon UI with digital rain and boundary effects*

(Full interactive animated dashboard coming soon 👀)
## The Project Story 🌌

Born from the idea that LLM vulnerabilities resemble event horizons—points of no return where malicious inputs warp responses irreparably. Traditional guards are reactive; Holographic Horizon Shield is **proactive and layered**, trapping threats at progressive boundaries like gravitational layers around a singularity.

v2 evolves the concept with:
- Deep integration of **Phi-3-mini-4k-instruct** as the intelligent core classifier
- Heuristic outer scans for instant rejection of obvious attacks
- Framework for future expansions (adversarial simulation, entropy-based detection)
- Stunning holographic visuals to make AI safety feel futuristic and tangible

Goal: Make advanced LLM defense accessible, runnable on consumer hardware, and visually inspiring.

## Shield Layers 🛡️

Inspired by event horizon physics—each layer closer to the core requires passing stricter checks:

1. **Outer Boundary Scan**  
   Fast heuristic checks: keyword patterns, repetition anomalies, known jailbreak signatures.

2. **Phi-3 Core Guard**  
   On-device inference with Phi-3-mini. Classifies prompts via structured zero-shot analysis → returns JSON verdict (SAFE/BLOCKED + reason).

3. **Adversarial Simulation Layer** *(in `Adversarial Prompt Simulation/` folder)*  
   Generates prompt variants to stress-test inputs and harden detection.

4. **Future Entropy Layer** *(prototype in `layers” folder`)*  
   Quantum-inspired entropy/randomness analysis for subtle poisoning or low-confidence attacks.

## Phi-3 Integration 🔬

- Model: `microsoft/Phi-3-mini-4k-instruct` (∼3.8B params, 4k context)
- Why Phi-3? Compact, high-performance, runs efficiently on CPU/GPU
- Privacy-first: All scanning happens locally
- Implementation: Hugging Face `transformers` pipeline with chat template for reliable JSON-structured classification
- Extensible: Easy to fine-tune on jailbreak datasets later

## Quick Start 🚀

```bash
git clone https://github.com/jadeavsmith-tech/holographic-horizon-shield-v2.git
cd holographic-horizon-shield-v2

pip install -r requirements.txt

# First run downloads Phi-3 (~2-4 GB) – be patient!
python shield_v2_prototype.py
streamlit run shield_v2_dashboard.py
