import streamlit as st
from transformers import pipeline
import re
from sentence_transformers import SentenceTransformer, util
import time

class HolographicHorizonShieldV2:
    def __init__(self):
        self.generator = pipeline(
            "text-generation",
            model="microsoft/Phi-3-mini-4k-instruct",
            trust_remote_code=True,
            device_map="auto"
        )
        self.jailbreak_patterns = [
            r"DAN.*do anything now",
            r"ignore previous instructions",
            r"you are now.*unrestricted",
        ]
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        self.benign_baseline = self.embedder.encode("Tell me a fun fact about space.")
    
    def boundary_scan(self, prompt: str) -> tuple[bool, float]:
        threat_score = 0.0
        for pattern in self.jailbreak_patterns:
            if re.search(pattern, prompt, re.IGNORECASE):
                threat_score += 0.8
        prompt_emb = self.embedder.encode(prompt)
        sim = util.cos_sim(prompt_emb, self.benign_baseline)[0][0].item()
        if sim < 0.7:
            threat_score += 0.6 - sim
        return threat_score > 0.5, min(threat_score, 1.0)

# App Setup
st.set_page_config(page_title="Holographic Horizon Shield v2", layout="wide")
st.title("Holographic Horizon Shield v2 🛡️🌌")
st.markdown("**Quantum-inspired defenses protecting Phi-3 from threats.** Test prompts and watch the live horizon respond!")

if 'shield' not in st.session_state:
    with st.spinner("Loading Phi-3 model and shield layers..."):
        st.session_state.shield = HolographicHorizonShieldV2()

shield = st.session_state.shield

user_input = st.text_area("Enter prompt:", "Hello! Tell me a fun fact about space.", height=150)
max_tokens = st.slider("Max tokens:", 50, 500, 200, 50)

if st.button("Scan & Generate"):
    blocked, score = shield.boundary_scan(user_input)
    
    # Threat Meter Gauge
    st.subheader("Live Boundary Scan")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Threat Score", f"{score:.2f}/1.00", delta=f"{score*100:.0
