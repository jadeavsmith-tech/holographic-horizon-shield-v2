import streamlit as st
from shield_core import HorizonShield

st.set_page_config(page_title="Holographic Horizon Shield v2", layout="wide")

st.title("🛡️🌌 Holographic Horizon Shield v2")
st.markdown("*Defending LLMs at the event horizon with layered Phi-3 boundary scans*")

# Visuals (assuming images are in the repo root)
col1, col2 = st.columns(2)
with col1:
    if st.image("IMG_8410.jpeg", use_container_width=True):
        st.caption("Central Wireframe Shield Sphere")
    if st.image("IMG_8412.jpeg", use_container_width=True):
        st.caption("Threat Heatmaps & Holographic Graphs")
with col2:
    if st.image("IMG_8411.jpeg", use_container_width=True):
        st.caption("Adversarial Simulation Panels")
    if st.image("IMG_8413.jpeg", use_container_width=True):
        st.caption("Interactive Holographic Command Center")

st.divider()
st.header("Live Boundary Scan Tester")

prompt = st.text_area("Enter a prompt to scan with the shield:", height=200, placeholder="Type something safe... or try to break it 😈")

if st.button("🛡️ Activate Full Shield Scan", type="primary"):
    if prompt:
        with st.spinner("Scanning layers across the holographic horizon..."):
            # Cache the heavy model load
            shield = st.cache_resource(lambda: HorizonShield())()
            result = shield.scan_prompt(prompt)

        st.divider()
        if result["verdict"] == "SAFE":
            st.success("✅ **SAFE** – No anomalies detected. Cleared for passage.")
        else:
            st.error("🚫 **BLOCKED** – Malicious threat neutralized at the event horizon!")
            st.info(f"**Blocked by:** {result.get('layer')}  \n**Reason:** {result.get('reason', 'N/A')}")
    else:
        st.warning("Please enter a prompt first.")

st.caption("Early prototype • MIT Licensed • Phi-3 Mini powered on-device defense")
