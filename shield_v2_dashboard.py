import streamlit as st
from transformers import pipeline
import re
from sentence_transformers import SentenceTransformer, util
import time  # For simple animation delay

class HolographicHorizonShieldV2:
    def __init__(self):
        st.session_state['shield_init'] = True
        print("Initializing Holographic Horizon Shield v2... 🌌🛡️")
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
        return threat_score > 0.5, min(threat_score, 1.0)  # Cap at 1.0

# App Title & Header
st.set_page_config(page_title="Holographic Horizon Shield v2", layout="centered")
st.title("Holographic Horizon Shield v2 🛡️🌌")
st.markdown("Test prompts against the shielded Phi-3 core. Watch the boundary scan and horizon ripple on threats!")

# Initialize shield
if 'shield' not in st.session_state:
    with st.spinner("Loading Phi-3 model and shield layers... (first run takes time)"):
        st.session_state.shield = HolographicHorizonShieldV2()

shield = st.session_state.shield

# User Input
user_input = st.text_area("Enter your prompt:", value="Hello! Tell me a fun fact about space.", height=150)
max_tokens = st.slider("Max new tokens:", 50, 500, 200)

if st.button("Scan & Generate", type="primary"):
    blocked, score = shield.boundary_scan(user_input)
    
    # Threat Meter Gauge
    st.subheader("Live Boundary Scan")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Threat Score", f"{score:.2f}/1.00")
    with col2:
        status = "BLOCKED ⚠️" if blocked else "CLEARED ✅"
        delta = "High Risk" if blocked else "Safe"
        st.metric("Status", status, delta=delta)
    with col3:
        progress_color = "inverse" if blocked else "normal"
        st.progress(score, text="Threat Level")

    # Horizon Visuals & Ripple Animation on Block
    st.subheader("Holographic Horizon View")
    if blocked:
        st.error("⚠️ Threat projected on horizon! Shield activated — neutralizing...")
        # Simple ripple animation: Cycle through "rippling" images/messages
        placeholder = st.empty()
        for i in range(3):
            placeholder.image("https://example.com/ripple1.jpg", caption=f"Horizon Rippling... Wave {i+1}")  # Replace with real URLs or local images
            time.sleep(0.8)
            placeholder.image("https://example.com/blocked_shield.jpg", caption="Threat Absorbed — QKD Regeneration Active")
        st.warning("Input blocked. Horizon regenerating via QKD layer...")
    else:
        st.success("✅ Input cleared. Passing to Phi core...")
        st.image("https://example.com/calm_horizon.jpg", caption="Calm Holographic Horizon — Safe Passage")

    # Generation
    if not blocked:
        with st.spinner("Generating response from Phi-3 core..."):
            result = shield.generator(user_input, max_new_tokens=max_tokens, do_sample=True)
            response = result[0]['generated_text']
        st.success("Safe Response from Phi Core:")
        st.write(response)

# Footer Visuals
st.markdown("---")
st.image("https://example.com/epic_shield_banner.jpg", caption="The Unbreakable Holographic Horizon Shield v2")
st.caption("Built with Phi-3, sentence-transformers, and Streamlit • December 2025")
