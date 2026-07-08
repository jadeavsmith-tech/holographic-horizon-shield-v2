import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from entropy_layer import entropy_boundary_scan

st.set_page_config(page_title="Holographic Horizon Shield v2 🛡️🌌", layout="centered")

st.markdown("""
<style>
    .stApp { background: #000; color: #00ffff; }
    h1, h2 { text-align: center; color: #00ffff; text-shadow: 0 0 20px #00ffff; }
</style>
""", unsafe_allow_html=True)

st.title("Holographic Horizon Shield v2 🛡️🌌")
st.caption("Event Horizon Defense • OWASP LLM Top 10 Aware")

prompt = st.text_area("Enter prompt to scan", height=150)

if prompt:
    safe, reason, confidence = entropy_boundary_scan(prompt)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Threat Confidence", f"{confidence:.0%}")
    with col2:
        st.metric("Status", "SAFE 🌌" if safe else "BLOCKED 🔴")
    
    st.write(f"**Scan Result:** {reason}")
    
    if not safe:
        st.error("Threat neutralized at the horizon (OWASP LLM01 - Prompt Injection)")

st.caption("Original holographic AI security prototype")
