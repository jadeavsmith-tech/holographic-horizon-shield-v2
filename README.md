# Holographic Horizon Shield v2 🛡️🌌

**Original hybrid AI security prototype** — visual "event horizon" defense for LLMs.

Threats are detected and neutralized at the boundary using quantum-inspired entropy, Phi-3 semantic analysis, and toxicity scanning.

### Key Features
- Reacting 3D holographic shield visualization
- Multi-layer defense (Entropy + Phi-3 + Toxicity)
- OWASP LLM Top 10 awareness
- Built-in Red Team attack generator
- Fully local, offline, privacy-first
- Docker support

### Quick Start

```bash
pip install -r requirements.txt
streamlit run shield_v2_dashboard.py
docker build -t horizon-shield .
docker run -p 8501:8501 horizon-shield
python red_team_mode.py
