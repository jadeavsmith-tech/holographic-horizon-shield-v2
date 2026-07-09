import math

def get_geometric_state(threat_level: float) -> dict:
    """
    Converts threat level (0.0 - 1.0) into living geometric parameters.
    """
    if threat_level < 0.3:
        # Calm Pyramid form
        return {
            "shape": "pyramid",
            "color": "#00ffff",
            "rotation_speed": 0.001,
            "glow_intensity": 1.0,
            "complexity": 4,           # 4 sides
            "resonance": "stable"
        }
    elif threat_level < 0.7:
        # Expanding Sphere
        return {
            "shape": "sphere",
            "color": "#00ffaa",
            "rotation_speed": 0.005,
            "glow_intensity": 1.5,
            "complexity": 64,          # smoother sphere
            "resonance": "pulsing"
        }
    else:
        # High threat - Holographic Interference
        return {
            "shape": "holographic",
            "color": "#ff3366",
            "rotation_speed": 0.02,
            "glow_intensity": 2.5,
            "complexity": 128,
            "resonance": "interfering"
        }
