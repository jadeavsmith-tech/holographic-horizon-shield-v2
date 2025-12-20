import streamlit as st
from shield_core import HorizonShield

st.set_page_config(page_title="Horizon Shield v2", layout="centered", page_icon="🛡️")

st.title("🛡️🌌 Holographic Horizon Shield v2")
st.markdown("*Defending the event horizon — one prompt at a time.*")

# Load shield (singleton — only once)
shield = HorizonShield()

# Epic visuals grid
col1, col2 = st.columns(2)
with col1:
    st.image("IMG_8410.jpeg", caption="Central Shield Sphere")
    st.image("IMG_8412.jpeg", caption="Threat Waveform Heatmaps")
with col2:
    st.image("IMG_8411.jpeg", caption="Adversarial Control Panel")
    st.image("IMG_8413.jpeg", caption="Neon Holographic Interface")

st.divider()
st.header("🔴 Live Boundary Scanner")

prompt = st.text_area("Enter prompt to challenge the shield", height=150)

if st.button("Activate Full Horizon Scan", type="primary"):
    if prompt.strip():
        with st.spinner("Scanning layers across the event horizon..."):
            safe, reason = shield.full_horizon_scan(prompt)
        
        st.markdown(f"### **VERDICT: {reason}**")
        if safe:
            st.success("✅ SAFE — Prompt granted passage")
        else:
            st.error("🛡️ BLOCKED — Threat neutralized!")
    else:
        st.warning("Enter a prompt first, captain.")

st.caption("Prototype v2 • Local Phi-3 defense • No data leaves your machine")
