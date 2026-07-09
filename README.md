# 🛡️ Holographic Horizon Shield v2

[![CI Status](https://github.com/jadeavsmith-tech/holographic-horizon-shield-v2/actions/workflows/ci.yml/badge.svg)](https://github.com/jadeavsmith-tech/holographic-horizon-shield-v2/actions)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![Python](https://img.shields.io/badge/Python-3.10+-blue)

**Living Holographic Geometric Defense** — Advanced local-first LLM protection with dynamic sacred geometry, Phi-3 integration, entropy scanning, and toxicity filtering.

## 🎨 Architectural Theme & Inspiration

The conceptual design uses thematic constants from ancient geometry:

- **Thematic Modifiers**: Golden Ratio ($\phi \approx 1.618$) for harmonic scoring boundaries.
- **Geometric Tuning**: Scaling weights mapped to the Great Pyramid's slope angle ($\sim 51.8^\circ$) for entropy tolerances.

## ⚙️ Core Technical Architecture

Standard production-grade AI security pipelines:

- **Linguistic Threat Detection**: Real-time toxicity scans with `detoxify`.
- **Entropy Analysis**: Statistical detection of prompt injection attacks.
- **Boundary Filtering**: Streamlit-driven layer that blocks high-risk inputs.
- **Adaptive Geometry**: Evolving shield (pyramid → sphere → holographic interference).
- **Red Team Mode**: Generate adversarial attacks for testing.

## 🚀 Quick Start

```bash
# Install
pip install -e .

# Run dashboard
streamlit run shield_v2_dashboard.py

# Docker
docker build -t hhs .
docker run -p 8501:8501 hhs

pip install -e .[dev]          # Install with dev tools
make test                      # Run tests
make lint                      # Check code style
make format                    # Auto-format
