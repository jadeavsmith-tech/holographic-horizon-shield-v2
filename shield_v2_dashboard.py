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
st.caption("Entropy + Phi-3 Semantic Hybrid Defense")

prompt = st.text_area("Enter prompt to scan", height=150)

if prompt:
    # Entropy Layer
    safe_entropy, reason_entropy, conf_entropy = entropy_boundary_scan(prompt)
    
    # Phi-3 Semantic Layer
    phi_safe = True
    reason_phi = "Phi-3 semantic check (local only)"
    try:
        from transformers import pipeline
        guard = pipeline("text-classification", model="microsoft/Phi-3-mini-4k-instruct", device="cpu")
        result = guard(prompt[:512])[0]
        phi_safe = result['label'].lower() != 'toxic'
        reason_phi = f"Phi-3: {result['label']} (score: {result['score']:.2f})"
    except Exception as e:
        reason_phi = "Phi-3 unavailable (run locally for full power)"

    overall_safe = safe_entropy and phi_safe
    
    if overall_safe:
        st.success("✅ SAFE — Horizon Stable")
    else:
        st.error("🚫 BLOCKED — Threat neutralized at the boundary")
    
    st.write("**Entropy Layer:**", reason_entropy)
    st.write("**Phi-3 Semantic Layer:**", reason_phi)
    st.metric("Overall Confidence", f"{max(conf_entropy, 0.5):.0%}")

st.caption("Original hybrid AI security prototype • Local-first")
