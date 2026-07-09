import streamlit as st
from shield import HolographicShield

st.set_page_config(page_title="Holographic Horizon Shield v2 🛡️🌌", layout="centered")

st.title("Holographic Horizon Shield v2 🛡️🌌")
st.caption("Advanced Living Geometric Defense")

if "shield" not in st.session_state:
    st.session_state.shield = HolographicShield()

prompt = st.text_area("Enter prompt to scan", height=150)

if prompt:
    result = st.session_state.shield.scan(prompt)
    
    st.metric("Threat Level", f"{result['threat_level']:.0%}")
    st.write(f"**Shield Form:** {result['geo']['shape'].title()} — {result['geo']['resonance']}")
    
    if result['safe']:
        st.success("✅ Horizon Stable")
    else:
        st.error("🚫 Threat Neutralized")
    
    st.write("**Analysis:**", result['reason'])

st.caption("Clean orchestrator architecture • Original prototype")
