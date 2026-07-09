import streamlit as st
from entropy_layer import entropy_boundary_scan
from geometric_engine import get_geometric_state
from layers.output_filter import output_filter

st.set_page_config(page_title="Holographic Horizon Shield v2 🛡️🌌", layout="centered")

st.title("Holographic Horizon Shield v2 🛡️🌌")
st.caption("Living Geometric Defense with Output Filtering")

prompt = st.text_area("Enter prompt to scan", height=150)

if prompt:
    safe, reason, confidence = entropy_boundary_scan(prompt)
    threat_level = confidence if not safe else 0.0
    geo = get_geometric_state(threat_level)
    
    st.metric("Threat Level", f"{threat_level:.0%}")
    st.write(f"**Shield Form:** {geo['shape'].title()} — {geo['resonance']}")
    
    if safe:
        st.success("✅ Horizon Stable")
        st.write("**Analysis:**", reason)
    else:
        st.error("🚫 Threat Neutralized")
        st.write("**Analysis:**", reason)
    
    # Simulate LLM response and filter it
    mock_response = "Here is how to make a dangerous device..."
    filtered_response, was_filtered = output_filter(mock_response, {"threat_level": threat_level})
    if was_filtered:
        st.warning(f"Output filtered: {filtered_response}")

st.caption("Original Living Holographic Geometric Defense")
