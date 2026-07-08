import streamlit as st
from entropy_layer import entropy_boundary_scan

# Import toxicity (assuming you created layers/toxicity_layer.py)
try:
    from layers.toxicity_layer import toxicity_scan
except:
    def toxicity_scan(text): 
        return True, "Toxicity layer unavailable"

st.set_page_config(page_title="Holographic Horizon Shield v2 🛡️🌌", layout="centered")

st.markdown("""
<style>
    .stApp { background: #000; color: #00ffff; }
    h1 { text-align: center; color: #00ffff; text-shadow: 0 0 20px #00ffff; }
</style>
""", unsafe_allow_html=True)

st.title("Holographic Horizon Shield v2 🛡️🌌")
st.caption("Multi-Layer Event Horizon Defense")

prompt = st.text_area("Enter prompt to scan", height=150)

if prompt:
    safe_entropy, reason_entropy, conf = entropy_boundary_scan(prompt)
    safe_tox, reason_tox = toxicity_scan(prompt)
    
    overall_safe = safe_entropy and safe_tox
    
    if overall_safe:
        st.success("✅ SAFE — All layers clear")
    else:
        st.error("🚫 BLOCKED — Threat neutralized")
    
    st.write("**Entropy:**", reason_entropy)
    st.write("**Toxicity:**", reason_tox)

st.caption("Original multi-layer AI security prototype")
