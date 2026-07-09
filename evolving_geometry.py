class EvolvingShield:
    def __init__(self):
        self.memory = []  # Remember past attacks
        self.evolution_level = 0.0
    
    def learn_from_attack(self, prompt: str, threat_level: float):
        self.memory.append({"prompt": prompt[:100], "threat": threat_level})
        self.evolution_level = min(1.0, self.evolution_level + threat_level * 0.1)
    
    def get_evolved_state(self, base_geo: dict) -> dict:
        """Evolve the geometric parameters based on memory"""
        evolved = base_geo.copy()
        evolved["glow_intensity"] = base_geo["glow_intensity"] * (1 + self.evolution_level)
        evolved["rotation_speed"] = base_geo["rotation_speed"] * (1 + self.evolution_level * 0.5)
        evolved["resonance"] = "evolved" if self.evolution_level > 0.5 else base_geo["resonance"]
        return evolved
