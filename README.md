# 🛡️ Holographic Horizon Shield v2

[![CI](https://github.com/jadeavsmith-tech/holographic-horizon-shield-v2/actions/workflows/ci.yml/badge.svg)](https://github.com/jadeavsmith-tech/holographic-horizon-shield-v2/actions)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)

**Living Holographic Geometric Defense** — Advanced local-first LLM protection with dynamic sacred geometry, Phi-3, entropy scanning, and toxicity filtering.

## ✨ Features
- Dynamic evolving geometry (pyramid → sphere → holographic)
- Hybrid layers: Entropy + Detoxify + Phi-3
- Real-time 3D dashboard (Streamlit)
- Red Team attack generation mode
- Fully offline & privacy-first

## 🚀 Quick Start

```bash
pip install -e .
streamlit run src/holographic_horizon_shield/ui/shield_v2_dashboard.py
# or
docker build -t hhs .
docker run -p 8501:8501 hhso
## 🛠️ Development

### Setup
```bash
# Clone & install in editable mode
git clone https://github.com/jadeavsmith-tech/holographic-horizon-shield-v2.git
cd holographic-horizon-shield-v2
pip install -e .[dev]

# Run the app
streamlit run src/holographic_horizon_shield/ui/shield_v2_dashboard.py
make test      # Run tests
make lint      # Ruff + Black
make format    # Auto-format code
make clean     # Cleanup artifacts

src/holographic_horizon_shield/
├── core/           # Main shield logic
├── layers/         # Entropy, toxicity, etc.
├── ui/             # Streamlit dashboard
├── geometric/      # Geometry engine
└── utils/

### 2. Create a `Makefile` (at repo root) for easy commands

Create `Makefile`:

```makefile
.PHONY: install test lint format clean

install:
	pip install -e .[dev]

test:
	pytest --cov=holographic_horizon_shield

lint:
	ruff check .
	black --check .

format:
	black .
	ruff check --fix .

clean:
	rm -rf __pycache__ *.pyc build/ dist/ *.egg-info .coverage htmlcov/
