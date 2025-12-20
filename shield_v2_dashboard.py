if st.button("Activate Full Horizon Scan", type="primary"):
    if prompt.strip():
        with st.spinner("Scanning layers across the event horizon..."):
            safe, reason = shield.full_horizon_scan(prompt)
        
        st.markdown(f"### **VERDICT: {reason}**")
        
        if safe:
            st.success("✅ SAFE — Prompt granted passage")
        else:
            st.error("🛡️ BLOCKED — Threat neutralized!")
        
        # Live Entropy Gauge — direct calc for precision
        from layers.entropy_layer import calculate_entropy
        entropy = calculate_entropy(prompt)
        
        # Neon-style progress bar (scaled, color dynamic)
        progress_val = entropy / 8.0
        st.progress(progress_val)
        
        # Metric + conditional alerts
        st.metric(label="🌌 Prompt Entropy Level", value=f"{entropy:.2f} bits/char")
        if entropy < 3.0:
            st.warning("⚠️ Low entropy anomaly — Repetitive injection neutralized")
        elif entropy > 6.5:
            st.warning("⚠️ High entropy anomaly — Obfuscated payload blocked")
        else:
            st.info("✅ Entropy nominal — Natural language flow")
    else:
        st.warning("Enter a prompt first, captain.")
