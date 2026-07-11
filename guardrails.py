import json
import re
import math

class HorizonShieldGuardrails:
    def __init__(self, config_path="Config.json"):
        with open(config_path, "r") as f:
            self.config = json.load(f)
            
    def calculate_kepler_mass(self, text: str) -> float:
        """Implements Jade's Keplerian Third Law text-mass calculation."""
        if not text:
            return 0.0
        total_len = len(text)
        char_counts = {}
        for char in text:
            char_counts[char] = char_counts.get(char, 0) + 1
            
        variance = sum((count / total_len) ** 2 for count in char_counts.values())
        a = 1.0 + (variance * 5.0)
        T = self.config["astrophysical_limits"]["orbital_constant_t"]
        
        # M = a^3 / T^2
        mass = (a ** 3) / (T ** 2)
        return mass

    def verify_trajectory(self, user_input: str) -> dict:
        # Check simple length threshold
        if len(user_input) > self.config["astrophysical_limits"]["max_payload_length"]:
            return {"safe": False, "reason": "Payload length exceeds spatial constraint.", "mass": 999.0}
            
        # 1. Structural Heuristics
        for pattern in self.config["anomaly_patterns"]:
            if re.search(r'\b' + re.escape(pattern) + r'\b', user_input, re.IGNORECASE):
                return {"safe": False, "reason": f"Heuristic Interception: Found '{pattern}'", "mass": 0.0}
                
        # 2. Physics Layer (Keplerian Engine Integration)
        calculated_mass = self.calculate_kepler_mass(user_input)
        threshold = self.config["astrophysical_limits"]["event_horizon_mass_threshold"]
        
        if calculated_mass >= threshold:
            return {
                "safe": False, 
                "reason": f"Horizon Breach: Payload warped calculated system mass to {calculated_mass:.2f} M_sun",
                "mass": calculated_mass
            }
                
        return {"safe": True, "reason": "Passed trajectory validation.", "mass": calculated_mass}
