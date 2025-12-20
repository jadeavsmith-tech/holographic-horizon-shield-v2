import streamlit as st
import numpy as np
from scipy.stats import entropy
import pandas as pd
import plotly.express as px
from transformers import AutoTokenizer
import torch
from layers.entropy_layer import calculate_entropy  # Keep your existing entropy func
# Assume your shield import
from shield_core import HolographicHorizonShield  # or wherever the class is

st.set_page_config(page_title="Horizon Shield v2", layout="wide", initial_sidebar_state="expanded")

# Dark neon theme vibe
st.markdown("""
<style>
    .main {background: black; color: cyan;}
    .stPlotlyChart {background: #111 !important;}
</style>
""", unsafe_allow_html=True)

st.title("🛡️ Holographic Horizon Shield v2 🌌")
st.markdown("**Live entropy charts update as you type • Full layered scan on demand**")

# Cache tokenizer for live tokenization
@st.cache_resource
def load_tokenizer():
    return AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct", trust_remote_code=True)

tokenizer = load_tokenizer()

# Cache shield for full scan
@st.cache_resource
def load_shield():
    return HolographicHorizonShield()  # Your shield class

shield = load_shield()

prompt = st.text_area("Enter prompt — watch the horizon react live:", height=250, placeholder="Type here for instant boundary scan...")

# === LIVE ENTROPY CHARTS (updates on every keystroke) ===
if prompt.strip():
    # Tokenize live
    inputs = tokenizer(prompt, return_tensors="pt")
    tokens = inputs.input_ids[0].cpu().numpy()

    if len(tokens) > 10:
        unique, counts = np.unique(tokens, return_counts=True)
        probs = counts / counts.sum()
        token_entropy = entropy(probs)

        df = pd.DataFrame({
            'Token ID': unique,
            'Probability': probs
        }).sort_values('Probability', ascending=False)

        col1, col2 = st.columns(2)

        with col1:
            fig_bar = px.bar(
                df.head(50),
                x='Token ID',
                y='Probability',
                title=f"Live Token Distribution (Entropy: {token_entropy:.2f})",
                color='Probability',
                color_continuous_scale="plasma"
            )
            fig_bar.update_layout(plot_bgcolor="#111", paper_bgcolor="#111", font_color="cyan")
            st.plotly_chart(fig_bar, use_container_width=True)

        with col2:
            fig_hist = px.histogram(
                df,
                x='Probability',
                nbins=30,
                title="Probability Distribution Histogram",
                color_discrete_sequence=["#ff00ff"]
            )
            fig_hist.update_layout(plot_bgcolor="#111", paper_bgcolor="#111", font_color="cyan")
            st.plotly_chart(fig_hist, use_container_width=True)

        # Metrics
        colm1, colm2 = st.columns(2)
        with colm1:
            st.metric("Live Token Entropy", f"{token_entropy:.2f}", help="Higher = more chaotic/anomalous")
        with colm2:
            words = prompt.lower().split()
            diversity = len(set(words)) / len(words) if words else 0
            st.metric("Word Diversity (QKD Proxy)", f"{diversity:.3f}", help="Lower = repetitive patterns")

    else:
        st.info("Keep typing — entropy visualization activates soon...")

# === FULL SHIELD SCAN BUTTON (your existing logic, enhanced) ===
if st.button("Activate Full Horizon Scan", type="primary"):
    if prompt.strip():
        with st.spinner("Scanning layers across the event horizon..."):
            safe, reason = shield.full_horizon_scan(prompt)
        
        st.markdown(f"### **VERDICT: {reason}**")
        
        if safe:
            st.success("SAFE — Prompt granted passage")
        else:
            st.error("BLOCKED — Threat neutralized!")
        
        # Your existing entropy gauge
        entropy_val = calculate_entropy(prompt)
        progress_val = min(entropy_val / 8.0, 1.0)
        st.progress(progress_val)
        
        st.metric(label="Prompt Entropy Level", value=f"{entropy_val:.2f} bits/char")
        if entropy_val < 3.0:
            st.warning("Low entropy anomaly — Repetitive injection neutralized")
        elif entropy_val > 6.5:
            st.warning("High entropy anomaly — Obfuscated payload blocked")
        else:
            st.info("Entropy nominal — Natural language flow")
    else:
        st.warning("Enter a prompt first, captain.")

st.caption("Nothing crosses the horizon unchanged.")
