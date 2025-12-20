# Holographic Horizon Shield v2 🛡️🌌

**Advanced LLM defenses with Phi-3 integration and boundary scans**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)

![Holographic Horizon Banner](https://perezcalzadilla.com/wp-content/uploads/2025/05/Screenshot-2025-05-22-171346-1.png)
*<p align="center">A glowing holographic boundary encodes and protects the information horizon — inspired by black hole physics and quantum principles</p>*

## Project Story

The **Holographic Horizon Shield** is born from the holographic principle in physics: all information inside a volume is encoded on its boundary surface. In LLMs, the "horizon" is the input prompt boundary — the critical surface where adversarial attacks (jailbreaks, injections) attempt to cross.

v2 evolves the original HSS by erecting a multi-layered defense system:
- **Boundary scans** for token-level anomalies
- **QKD-inspired entropy monitoring** to detect irreversible information leaks
- **Phi-3 guard model** for lightweight, local semantic validation

The vision: unbreakable, offline-first safeguards that run efficiently on consumer hardware while blocking sophisticated attacks.

## Key Features

- **Holographic Boundary Scanner** – Token distribution and statistical anomaly detection
- **QKD-Inspired Entropy Monitor** – Quantum-analog checks for prompt injection attempts
- **Phi-3 Guard Layer** – On-device inference with Microsoft's Phi-3-mini for safety scoring
- **Modular Pipeline** – Easy to extend or customize layers
- **Minimal Dependencies** – Core scans need no external API calls

## Architecture Overview

Concentric defense layers protect the LLM core, inspired by defense-in-depth principles:

![Layered Defense Architecture](https://cdn2.hubspot.net/hubfs/99242/Blog_Images/7%20layers%20of%20cybersecurity.png)
*<p align="center">Multi-layered concentric shields — each layer catches what the outer ones miss</p>*

### Shield Layers

1. **Outer Horizon: Boundary Scanner**  
   Detects statistical anomalies (entropy spikes, unusual token distributions).  
   ![Boundary Anomaly Visualization](https://www.mdpi.com/entropy/entropy-17-02367/article_deploy/html/images/entropy-17-02367f13-1024.png)

2. **Mid Layer: QKD Entropy Monitor**  
   Tracks information flow like the BB84 protocol — flags irreversible entropy changes from injections.  
   ![QKD Protocol Flow](https://www.researchgate.net/publication/349618491/figure/fig1/AS:1013479695736832@1618643797205/The-chart-of-quantum-key-distribution-protocol-BB84-steps.png)

3. **Inner Core: Phi-3 Guard**  
   Semantic evaluation of suspicious inputs using Phi-3-mini.  
   ![Phi-3 Model Family](https://news.microsoft.com/source/wp-content/uploads/2024/04/The-Phi-3-small-language-models-with-big-potential-1.jpg)

## Quick Start

```bash
git clone https://github.com/jadeavsmith-tech/holographic-horizon-shield-v2.git
cd holographic-horizon-shield-v2

pip install -r requirements.txt

# Download Phi-3-mini (Hugging Face)
python -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='microsoft/Phi-3-mini-4k-instruct')"

# Run demo
python examples/basic_shield_test.py
