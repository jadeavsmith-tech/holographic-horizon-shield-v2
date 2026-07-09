from layers.entropy_layer import entropy_boundary_scan
from layers.toxicity_layer import toxicity_scan
from layers.output_filter import output_filter
from geometric_engine import get_geometric_state
from evolving_geometry import EvolvingShield

class HolographicShield:
    def __init__(self):
        self.evolver = EvolvingShield()
    
    def scan(self, prompt: str):
        results = {
            "entropy": entropy_boundary_scan(prompt),
            "toxicity": toxicity_scan(prompt),
        }
        
        threat_level = max(results["entropy"][2], 0.0)
        if not results["entropy"][0] or not results["toxicity"][0]:
            threat_level = 0.8
        
        geo = get_geometric_state(threat_level)
        evolved = self.evolver.get_evolved_state(geo)
        
        return {
            "safe": results["entropy"][0] and results["toxicity"][0],
            "reason": results["entropy"][1],
            "geo": evolved,
            "threat_level": threat_level
        }
