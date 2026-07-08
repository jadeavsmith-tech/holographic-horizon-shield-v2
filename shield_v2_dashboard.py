import streamlit as st
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

# 3D Reacting Shield
shield_html = """
<div style="width:100%; height:600px; position:relative;">
    <canvas id="canvas" style="position:absolute; top:0; left:0;"></canvas>
</div>
<script src="https://cdn.jsdelivr.net/npm/three@0.168.0/build/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.168.0/examples/js/controls/OrbitControls.js"></script>
<script>
    const renderer = new THREE.WebGLRenderer({canvas: document.getElementById('canvas'), antialias:true, alpha:true});
    renderer.setSize(window.innerWidth, 600);
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(60, window.innerWidth/600, 0.1, 100);
    camera.position.set(0,5,20);
    const controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.autoRotate = true;
    const material = new THREE.ShaderMaterial({
        uniforms: { uTime: {value:0}, uThreat: {value:0.0} },
        vertexShader: `uniform float uTime; varying vec3 vPos; void main(){ vec4 mv = modelViewMatrix * vec4(position,1); gl_Position = projectionMatrix * mv; vPos = position; }`,
        fragmentShader: `uniform float uTime; uniform float uThreat; varying vec3 vPos; void main(){
            float scan = sin(vPos.y*20 - uTime*3)*0.05 + 0.95;
            vec3 color = mix(vec3(0.0,1.0,1.0), vec3(1.0,0.0,0.0), uThreat);
            float fres = pow(1.0-dot(normalize(vPos),vec3(0,0,1)),2);
            gl_FragColor = vec4(color*(scan+fres), fres*0.8 + scan*0.2);
        }`,
        transparent:true, side:THREE.DoubleSide
    });
    const shield = new THREE.Mesh(new THREE.SphereGeometry(8,128,128), material);
    scene.add(shield);
    const clock = new THREE.Clock();
    function anim(){ 
        material.uniforms.uTime.value = clock.getElapsedTime(); 
        shield.rotation.y += 0.001; 
        controls.update(); 
        renderer.render(scene, camera); 
        requestAnimationFrame(anim); 
    }
    anim();
</script>
"""
st.components.v1.html(shield_html, height=600)

st.title("Holographic Horizon Shield v2 🛡️🌌")

prompt = st.text_area("Enter prompt to scan", height=150)

if prompt:
    safe, reason, confidence = entropy_boundary_scan(prompt)
    
    # Reacting shield (JavaScript can be enhanced later, for now we show visual feedback)
    threat_level = confidence if not safe else 0.0
    st.success("Shield reacting to threat level: " + str(round(threat_level*100)) + "%") if not safe else st.success("Horizon stable")
    
    st.write(f"**Verdict:** {reason}")
    if not safe:
        st.error("🚨 Threat neutralized at the event horizon")

st.caption("Reacting holographic prototype • Original AI security defense")
