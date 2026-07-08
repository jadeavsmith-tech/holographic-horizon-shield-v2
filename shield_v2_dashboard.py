import streamlit as st
from entropy_layer import entropy_boundary_scan

st.set_page_config(page_title="Holographic Horizon Shield v2 🛡️🌌", layout="centered")

st.markdown("""
<style>
    .stApp { background: #000; color: #00ffff; }
    h1 { text-align: center; color: #00ffff; text-shadow: 0 0 20px #00ffff; }
</style>
""", unsafe_allow_html=True)

st.title("Holographic Horizon Shield v2 🛡️🌌")
st.caption("Entropy + Phi-3 Semantic Defense")

prompt = st.text_area("Enter prompt to scan", height=150)

if prompt:
    # Entropy layer
    safe_entropy, reason_entropy, conf_entropy = entropy_boundary_scan(prompt)
    
    # Phi-3 layer (local only)
    phi_safe = True
    reason_phi = "Phi-3 semantic check skipped (cloud mode)"
    try:
        from transformers import pipeline
        guard = pipeline("text-classification", model="microsoft/Phi-3-mini-4k-instruct", device="cpu")
        result = guard(prompt[:500])[0]
        phi_safe = result['label'] != 'toxic'  # Simple example
        reason_phi = f"Phi-3: {result['label']} ({result['score']:.2f})"
    except:
        pass  # Graceful fallback
    
    overall_safe = safe_entropy and phi_safe
    
    if overall_safe:
        st.success("✅ SAFE — Horizon Stable")
    else:
        st.error("🚫 BLOCKED — Threat at the boundary")
    
    st.write("**Entropy:**", reason_entropy)
    st.write("**Phi-3 Semantic:**", reason_phi)

st.caption("Hybrid Entropy + Phi-3 • Original local AI security prototype")
