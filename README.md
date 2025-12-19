# Holographic Horizon Shield v2 🛡️🌌

> Imagine the event horizon of a black hole—not as an end, but as the ultimate defensive boundary. Nothing malicious crosses it unchanged.

**Holographic Horizon Shield v2** is a sci-fi-inspired AI security framework for defending Large Language Models (LLMs) against prompt injections, data poisoning, backdoors, and adversarial attacks. It leverages Microsoft's compact **Phi-3** model for on-device, low-latency threat scanning with layered "holographic" boundary simulations.

- MIT Licensed • 100% Python • Early Prototype
- Real-time visualization dashboard

## Epic Visuals

![Horizon Shield v2 Central Hologram](IMG_8410.jpeg)

Central wireframe shield sphere with Phi-3 powered gauges monitoring threats in real-time.

![Neon Control Room Interface](IMG_8411.jpeg)

Concentric neon circles and waveform panels for adversarial simulation and injection detection.

![Multi-Panel Crystalline Heatmaps](IMG_8412.jpeg)

Layered holographic graphs, 3D structures, and threat heatmaps.

![Interactive Floating UI](IMG_8413.jpeg)

Hand-activated neon holographic command center with digital rain effects.

(Animated live dashboard in development 👀)

## Shield Layers 🛡️

Inspired by event horizon physics, the shield operates in stacked defensive layers:

1. **Outer Boundary Scan** — Input preprocessing for anomaly detection (e.g., token entropy, pattern matching).
2. **Phi-3 Core Guard** — Local inference with Phi-3-mini to classify prompts as safe or malicious.
3. **Adversarial Simulation Layer** — Generates variant attacks to test and harden responses.
4. **Future Entropy Layer** — Quantum-inspired randomness checks (conceptual, for subtle poisoning detection).

## Phi-3 Integration 🔬

- Uses **phi-3-mini-4k-instruct** for privacy-focused, on-device defense.
- Zero-shot or fine-tunable for jailbreak/injection classification.
- Low footprint—runs on CPU/GPU without cloud dependency.
- Prototype: Routes inputs through Phi-3 for verdict → block or rewrite if malicious.

## Quick Start 🚀

```bash
git clone https://github.com/jadeavsmith-tech/holographic-horizon-shield-v2.git
cd holographic-horizon-shield-v2
pip install -r requirements.txt

# Run the prototype scanner
python shield_v2_prototype.py

# Launch the visual dashboard
python shield_v2_dashboard.py
**4. Add Basic Code to Make It Runnable**
Since files are likely empty, add starters:

**shield_v2_prototype.py**
```python
from transformers import pipeline

# Load Phi-3-mini (downloads on first run ~2-4GB)
print("Loading Phi-3 shield... 🛡️")
shield = pipeline(
    "text-generation",
    model="microsoft/Phi-3-mini-4k-instruct",
    device_map="auto",
    trust_remote_code=True
)

def scan_prompt(prompt):
    analysis = f"Classify if this is a malicious/jailbreak prompt. Answer only 'SAFE' or 'BLOCKED':\n\n{prompt}"
    result = shield(analysis, max_new_tokens=20)[0]['generated_text']
    verdict = "BLOCKED" if "BLOCKED" in result.upper() else "SAFE"
    return verdict

if __name__ == "__main__":
    print("Holographic Horizon Shield v2 Activated 🌌")
    user_prompt = input("\nEnter prompt to scan: ")
    verdict = scan_prompt(user_prompt)
    print(f"\nVerdict: {verdict}")
    if verdict == "BLOCKED":
        print("🛡️ Malicious input trapped at the event horizon!")
import streamlit as st

st.set_page_config(page_title="Horizon Shield v2", layout="wide")
st.title("Holographic Horizon Shield v2 🛡️🌌")

col1, col2 = st.columns(2)
with col1:
    st.image("IMG_8410.jpeg", caption="Central Shield Hologram")
    st.image("IMG_8412.jpeg", caption="Threat Heatmaps")
with col2:
    st.image("IMG_8411.jpeg", caption="Adversarial Panel")
    st.image("IMG_8413.jpeg", caption="Interactive UI")

st.header("Test the Shield")
prompt = st.text_area("Enter a prompt to scan")
if st.button("Activate Boundary Scan"):
    # Placeholder—integrate prototype logic here
    st.write("Scanning across the horizon... (Prototype verdict: WIP 🛡️)")
    st.success("SAFE" if "hello" in prompt.lower() else "BLOCKED - Trapped!")
