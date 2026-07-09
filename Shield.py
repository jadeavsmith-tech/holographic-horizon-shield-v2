from layers.entropy_layer import entropy_boundary_scan
from layers.toxicity_layer import toxicity_scan
from layers.output_filter import output_filter
from geometric_engine import get_geometric_state
from evolving_geometry import EvolvingShield

class HolographicShield:
    def __init__(self):
        self.evolver = EvolvingShield()
    
    def scan(self, prompt: str):
        """Main scan method — advanced orchestrator"""
        entropy_result = entropy_boundary_scan(prompt)
        toxicity_result = toxicity_scan(prompt)
        
        threat_level = max(entropy_result[2] if len(entropy_result) > 2 else 0.0, 0.0)
        
        if not entropy_result[0] or not toxicity_result[0]:
            threat_level = 0.85
        
        geo = get_geometric_state(threat_level)
        evolved_geo = self.evolver.get_evolved_state(geo)
        
        return {
            "safe": entropy_result[0] and toxicity_result[0],
            "reason": entropy_result[1],
            "geo": evolved_geo,
            "threat_level": threat_level
        }
