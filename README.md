# 🛡️ Holographic Horizon Shield v2

[![CI](https://github.com/jadeavsmith-tech/holographic-horizon-shield-v2/actions/workflows/ci.yml/badge.svg)](https://github.com/jadeavsmith-tech/holographic-horizon-shield-v2/actions)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![Python](https://img.shields.io/badge/Python-3.10+-blue)

**Living Holographic Geometric Defense** — Advanced local-first LLM protection with dynamic sacred geometry, Phi-3 integration, entropy scanning, and toxicity filtering.

## ✨ Features
- Dynamic evolving geometry (pyramid → sphere → holographic interference)
- Hybrid layers: Entropy + Detoxify + Phi-3
- Real-time 3D reacting dashboard (Streamlit)
- Red Team attack generation mode
- Fully offline & privacy-first

## 🚀 Quick Start

```bash
pip install -e .
streamlit run shield_v2_dashboard.py

docker build -t hhs .
docker run -p 8501:8501 hhs

flowchart TD
    A[User Prompt] --> B[Entropy Layer]
    A --> C[Toxicity Layer]
    A --> D[Phi-3 Analysis]
    B & C & D --> E[Threat Score]
    E --> F[Adaptive Geometric Shield]
    F --> G[Output Filter]
    G --> H[Safe Output / Blocked]

pip install -e .[dev]
make test
make lint
make format
