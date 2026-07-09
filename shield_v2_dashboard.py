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
st.caption("Living Geometric Defense Prototype")

prompt = st.text_area("Enter prompt to scan", height=150)

if prompt:
    # Threat analysis
    safe, reason, confidence = entropy_boundary_scan(prompt)
    threat_level = confidence if not safe else 0.0
    
    # Get living geometric state
    geo = get_geometric_state(threat_level)
    
    # Show geometric state
    st.write(f"**Current Shield State:** {geo['shape'].title()} - {geo['resonance']}")
    st.metric("Threat Level", f"{threat_level:.0%}")
    
    if safe:
        st.success("✅ Horizon Stable")
    else:
        st.error("🚫 Threat Neutralized at the Boundary")
    
    st.write("**Analysis:**", reason)

st.caption("Dynamic sacred geometry defense • Original prototype")
