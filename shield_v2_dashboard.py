import streamlit as st
from entropy_layer import entropy_boundary_scan
from geometric_engine import get_geometric_state
from evolving_geometry import EvolvingShield

st.set_page_config(page_title="Holographic Horizon Shield v2 🛡️🌌", layout="centered")

st.title("Holographic Horizon Shield v2 🛡️🌌")
st.caption("Living + Evolving Geometric Defense")

# Initialize evolving shield
if "shield" not in st.session_state:
    st.session_state.shield = EvolvingShield()

prompt = st.text_area("Enter prompt to scan", height=150)

if prompt:
    safe, reason, confidence = entropy_boundary_scan(prompt)
    threat_level = confidence if not safe else 0.0
    base_geo = get_geometric_state(threat_level)
    
    # Evolve based on threat
    if not safe:
        st.session_state.shield.learn_from_attack(prompt, threat_level)
    evolved_geo = st.session_state.shield.get_evolved_state(base_geo)
    
    st.metric("Threat Level", f"{threat_level:.0%}")
    st.metric("Evolution Level", f"{st.session_state.shield.evolution_level:.0%}")
    st.write(f"**Shield Form:** {evolved_geo['shape'].title()} — {evolved_geo['resonance']}")
    
    if safe:
        st.success("✅ Horizon Stable")
    else:
        st.error("🚫 Threat Neutralized — Shield Evolving")
    
    st.write("**Analysis:**", reason)

st.caption("The shield learns from attacks and grows stronger • Original prototype")
