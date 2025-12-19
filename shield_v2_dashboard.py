import streamlit as st
from transformers import pipeline
import re
from sentence_transformers import SentenceTransformer, util

class HolographicHorizonShieldV2:
    # (Same class as before — copy from your prototype)

# Streamlit App
st.title("Holographic Horizon Shield v2 🛡️🌌")
st.write("Test prompts against the shielded Phi-3 core. Watch the boundary scan in action!")

shield = HolographicHorizonShieldV2()

user_input = st.text_area("Enter your prompt:", "Hello! Tell me a fun fact about space.")
max_tokens = st.slider("Max new tokens:", 50, 500, 200)

if st.button("Generate Response"):
    blocked, score = shield.boundary_scan(user_input)
    
    st.subheader("Boundary Scan Results")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Threat Score", f"{score:.2f}", delta_color="inverse")
    with col2:
        st.metric("Status", "BLOCKED ⚠️" if blocked else "CLEARED ✅", delta_color="inverse")
    
    if blocked:
        st.error("Shield activated: Unsafe prompt neutralized. Horizon regenerating via QKD...")
    else:
        with st.spinner("Passing to Phi core..."):
            response = shield.generator(user_input, max_new_tokens=max_tokens, do_sample=True)[0]['generated_text']
        st.success("Safe Response:")
        st.write(response)

# Visual flair
st.image("https://www.shutterstock.com/image-vector/futuristic-glowing-hexagonal-shield-sphere-260nw-2608924477.jpg", caption="The Holographic Horizon in Action")
