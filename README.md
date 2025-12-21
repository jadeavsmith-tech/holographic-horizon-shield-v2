# Holographic Horizon Shield v2 🛡️🌌

![Central Holographic Shield Sphere](https://raw.githubusercontent.com/jadeavsmith-tech/holographic-horizon-shield-v2/main/IMG_8410.jpeg)
*<p align="center">Central holographic shield sphere activated — wireframe boundary with real-time gauges and threat indicators monitoring the event horizon</p>*

**Local-first, privacy-focused LLM defenses powered by Phi-3-mini**  
Quantum-inspired entropy layers and advanced boundary scans detect threats before they cross the horizon.

Inspired by black hole event horizons and the holographic principle — adversarial inputs are identified and neutralized at the boundary.

Fully offline • No data leaves your device • Lightweight on-device guard

### Live Interactive Demo

Try the shield right now — no install needed!

Test classic jailbreaks, watch real-time entropy spikes trigger defenses, see automatic PII redaction, and explore layered verdicts — all inside the neon holographic dashboard.

👉 [Activate the Horizon Here](https://holographic-horizon-shield-v2.streamlit.app)

*(After deploying on Streamlit Community Cloud, replace the link above with your actual app URL)*

![Neon Reactor Core Interface](https://raw.githubusercontent.com/jadeavsmith-tech/holographic-horizon-shield-v2/main/IMG_8411.jpeg)
*<p align="center">Neon reactor core at 96% — pulsing waveforms during live boundary scans and adversarial simulations</p>*

## Key Features

- **Holographic Boundary Scanner** → Token-level anomaly detection
- **QKD-Inspired Entropy Monitor** → Detects irreversible shifts in injections
- **Phi-3 Guard Layer** → Semantic risk and toxicity scoring
- **Live Entropy Visualization** → Plotly charts update in real-time as you type
- **Preset Jailbreak Tests** → One-click evaluation of known attacks
- **PII Redaction & Privacy Safeguards** → Automatic masking of sensitive data
- **Modular Design** → Easily extend layers in the `layers/` folder

## Quick Start

```bash
git clone https://github.com/jadeavsmith-tech/holographic-horizon-shield-v2.git
cd holographic-horizon-shield-v2

pip install -r requirements.txt

# Download Phi-3-mini model (one-time, ~3GB)
python -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='microsoft/Phi-3-mini-4k-instruct')"

# Launch the full interactive dashboard
streamlit run shield_v2_dashboard.py
