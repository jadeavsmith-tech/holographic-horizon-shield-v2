# Holographic Horizon Shield v2 🛡️🌌

![Horizon Shield v2 Core Hologram](IMG_8410.jpeg)
*<p align="center">Horizon Shield v2 activated — Massive glowing blue wireframe holographic sphere with real-time Phi-3 powered gauges, dials, and threat indicators monitoring the event horizon</p>*

**Advanced local-first LLM defenses with Phi-3 integration, boundary scans, and quantum-inspired entropy monitoring**

Inspired by black hole event horizons and the holographic principle: all threats are detected and neutralized at the boundary before they can cross into the core.

This v2 prototype runs **fully offline** on consumer hardware, using Microsoft's lightweight **Phi-3-mini** as an on-device guard model. No API calls, maximum privacy.

## Key Features

- **Holographic Boundary Scanner** — Token-level statistical anomaly detection
- **QKD-Inspired Entropy Monitor** — Detects irreversible information shifts (prompt injections, poisoning attempts)
- **Phi-3 Semantic Guard** — Lightweight local inference for jailbreak/harm scoring
- **Modular Layered Pipeline** — Extensible design with code in `layers/`
- **Real-Time Interactive Dashboard** — Live monitoring and testing via Streamlit (`shield_v2_dashboard.py`)

![Neon Core Reactor Interface](IMG_8411.jpeg)
*<p align="center">Core reactor at peak — Pulsing neon waveforms and gauges during live boundary scans and adversarial simulations</p>*

## Shield Layers (Concentric Defense)

1. **Outer Horizon — Boundary Scanner**  
   Statistical analysis of token distributions and entropy spikes.

2. **Mid Layer — QKD Entropy Monitor**  
   Quantum-key-distribution analog: flags irreversible entropy changes indicative of attacks.

3. **Inner Core — Phi-3 Guard**  
   Semantic evaluation with Phi-3-mini: scores prompts for risk and blocks high-threat inputs.

![Crystalline Entropy Dashboard](IMG_8412.jpeg)
*<p align="center">Triple-screen crystalline holograms with real-time entropy heatmaps and anomaly tracking</p>*

## Quick Start

```bash
# Clone the repo
git clone https://github.com/jadeavsmith-tech/holographic-horizon-shield-v2.git
cd holographic-horizon-shield-v2

# Install dependencies
pip install -r requirements.txt

# Download Phi-3-mini model (one-time, ~2-4 GB quantized)
python -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='microsoft/Phi-3-mini-4k-instruct')"

# Run the core prototype
python shield_v2_prototype.py

# Launch the interactive holographic dashboard
streamlit run shield_v2_dashboard.py
