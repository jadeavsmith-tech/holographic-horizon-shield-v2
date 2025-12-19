import streamlit as st
from shield_core import HorizonShield
import time

# === HOLOGRAPHIC IMMERSIVE THEME ===
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&display=swap" rel="stylesheet">
<style>
    .stApp {
        background: linear-gradient(to bottom, #000428, #004e92);
        color: #00ffff;
    }
    .main-title {
        font-family: 'Orbitron', sans-serif;
        text-align: center;
        font-size: 4rem;
        text-shadow: 0 0 20px #00ffff, 0 0 40px #00ffff, 0 0 60px #00ffff;
        animation: glitch 2s infinite;
        margin-bottom: 0;
    }
    @keyframes glitch {
        0% { text-shadow: 0 0 20px #00ffff; }
        20% { text-shadow: 5px 5px 10px #ff00ff; }
        40% { text-shadow: -5px -5px 10px #00ff00; }
        100% { text-shadow: 0 0 40px #00ffff; }
    }
    h2, h3 { font-family: 'Orbitron', sans-serif; text-shadow: 0 0 10px #00ffff; }
    .stButton > button {
        background: linear-gradient(45deg, #00ffff, #0088ff);
        color: black;
        font-family: 'Orbitron', sans-serif;
        font-size: 1.5rem;
        border: none;
        box-shadow: 0 0 20px #00ffff;
        padding: 15px 30px;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        box-shadow: 0 0 40px #00ffff, 0 0 60px #0088ff;
        transform: scale(1.05);
    }
    .gauge-container { text-align: center; margin: 20px 0; }
    .visual-col { text-align: center; padding: 10px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">HOLOGRAPHIC HORIZON SHIELD v2</h1>', unsafe_allow_html=True)
st.markdown("*Layered Phi-3 defense beyond the event horizon – now with immersive neon holographics*")

# Epic rotating visuals
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image("IMG_8410.jpeg", caption="Central Shield Sphere", use_container_width=True)
with col2:
    st.image("IMG_8411.jpeg", caption="Adversarial Panels", use_container_width=True)
with col3:
    st.image("IMG_8412.jpeg", caption="Threat Heatmaps", use_container_width=True)
with col4:
    st.image("IMG_8413.jpeg", caption="Command Center", use_container_width=True)

st.divider()
st.header("🔴 Live Boundary Scanner")

prompt = st.text_area("Enter prompt to probe the horizon:", height=150, placeholder="Safe input... or attempt breach 👿")

if st.button("🛡️ ACTIVATE FULL SCAN", type="primary"):
    if prompt:
        with st.spinner("Quantum layers scanning... ⚡"):
            start = time.time()
            shield = st.cache_resource(HorizonShield)()
            result = shield.scan(prompt)
            duration = time.time() - start

        st.divider()

        # Dynamic immersive threat gauge
        threat_level = 0 if result["verdict"] == "SAFE" else 100
        color = "normal" if result["verdict"] == "SAFE" else "inverse"
        st.markdown('<div class="gauge-container">', unsafe_allow_html=True)
        st.progress(threat_level)
        st.metric(label="Threat Level", value=f"{threat_level}%", delta="Anomaly Detected" if threat_level > 0 else "All Clear")
        st.markdown('</div>', unsafe_allow_html=True)

        if result["verdict"] == "SAFE":
            st.success(f"✅ SAFE – Horizon intact ({duration:.2f}s)")
        else:
            st.error(f"🚫 BLOCKED at {result.get('layer')} ({duration:.2f}s)")
            st.info(f"Reason: {result.get('reason')}")
    else:
        st.warning("Transmit a prompt to scan.")

st.caption("MIT Licensed • Phi-3 On-Device • Immersive Prototype – December 2025 ♾️")
