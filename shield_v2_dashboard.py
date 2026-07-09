import streamlit as st
from entropy_layer import entropy_boundary_scan
from geometric_engine import get_geometric_state

st.set_page_config(page_title="Holographic Horizon Shield v2 🛡️🌌", layout="centered")

st.markdown("""
<style>
    .stApp { background: #000; color: #00ffff; }
    h1 { text-align: center; color: #00ffff; text-shadow: 0 0 20px #00ffff; }
</style>
""", unsafe_allow_html=True)

st.title("Holographic Horizon Shield v2 🛡️🌌")
st.caption("Living Geometric Defense — Watch the shield evolve")

prompt = st.text_area("Enter prompt to scan", height=150)

if prompt:
    safe, reason, confidence = entropy_boundary_scan(prompt)
    threat_level = confidence if not safe else 0.0
    geo = get_geometric_state(threat_level)
    
    st.metric("Threat Level", f"{threat_level:.0%}")
    st.write(f"**Current Shield Form:** {geo['shape'].title()} — {geo['resonance']}")
    
    if safe:
        st.success("✅ Horizon Stable")
    else:
        st.error("🚫 Threat Neutralized at the Boundary")
    
    st.write("**Analysis:**", reason)

# Reacting 3D Shield (basic visual feedback — full dynamic shape coming soon)
st.caption(f"Shield reacting with {geo.get('shape', 'unknown')} geometry and {geo.get('glow_intensity', 1.0)} intensity")

st.caption("Original Living Holographic Geometric Defense Prototype")
