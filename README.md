# Holographic Horizon Shield v2 🛡️🌌

![Central holographic shield sphere activated](https://raw.githubusercontent.com/jadeavsmith-tech/holographic-horizon-shield-v2/main/IMG_8410.jpeg)
*<p align="center">Central holographic shield sphere activated — wireframe boundary with real-time gauges and threat indicators monitoring the event horizon</p>*

**Local-first LLM defenses with Phi-3 integration, boundary scans, and quantum-inspired entropy layers**

Inspired by black hole event horizons and the holographic principle: threats are detected at the boundary before they cross.

Fully offline, privacy-focused prototype using Microsoft's **Phi-3-mini** as lightweight on-device guard.

### Live Interactive Demo

Try the shield right now — no install needed!

Test classic jailbreaks, watch real-time entropy spikes disintegrate threats, see PII redaction in action, and explore layered verdicts — all in the neon holographic dashboard.

👉 [Activate the Horizon Here](https://holographic-horizon-shield-v2.streamlit.app)

*(Replace the URL above with your actual Streamlit link after deployment)*

![Neon Reactor Core Interface](https://raw.githubusercontent.com/jadeavsmith-tech/holographic-horizon-shield-v2/main/IMG_8411.jpeg)
*<p align="center">Neon reactor core at 96% — pulsing waveforms during live boundary scans and adversarial simulations</p>*

## Key Features

- **Holographic Boundary Scanner** — Token-level anomaly detection
- **QKD-Inspired Entropy Monitor** — Irreversible shift detection for injections
- **Phi-3 Guard Layer** — Semantic risk scoring
- **Modular Layers** — Extensible in `layers/`
- **Real-Time Dashboard** — Interactive monitoring with live Plotly entropy charts that update as you type
- **Preset Jailbreak Tests** — One-click evaluation of classic attacks
- **PII Redaction & Toxicity Blocking** — Automatic privacy safeguards

## Quick Start

```bash
git clone https://github.com/jadeavsmith-tech/holographic-horizon-shield-v2.git
cd holographic-horizon-shield-v2

pip install -r requirements.txt

# Download Phi-3-mini (one-time ~3GB)
python -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='microsoft/Phi-3-mini-4k-instruct')"

# Launch the interactive holographic dashboard
streamlit run shield_v2_dashboard.py
