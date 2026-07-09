import math
import time
import random
from pydantic import BaseModel

class CosmicTelemetry(BaseModel):
    calculated_parallax_mas: float = 2.09
    parallax_error_mas: float = 0.02
    calculated_distance_pc: float = 478.46
    calculated_distance_ly: float = 1560.4
    orbital_period_days: float = 185.59
    resolved_mass_solar_units: float = 9.62
    mass_error_solar_units: float = 0.18

class BlackHoleEngine:
    """
    Active MMT LLM Sinkhole Framework.
    Converts astrophysical equations into an active payload isolation engine.
    """
    def __init__(self):
        # Establish hard coded physical boundary constants from system telemetry
        self.telemetry = CosmicTelemetry()
        self.max_allowable_distance_ly = self.telemetry.calculated_distance_ly
        self.singularity_mass_threshold = self.telemetry.resolved_mass_solar_units

    def calculate_token_distance(self, prompt_entropy: float, prompt_length: int) -> float:
        """
        Maps token chaos and length to an abstract spatial distance.
        Simulates the parallax equation: d = 1 / w
        """
        # Base simulated parallax derived dynamically from inbound prompt metrics
        simulated_parallax_mas = max(0.001, (prompt_entropy / max(1, prompt_length)) * 10)
        simulated_parallax_arcsec = simulated_parallax_mas / 1000.0
        
        # Parallax calculation: d = 1 / w
        distance_parsecs = 1.0 / simulated_parallax_arcsec
        distance_light_years = distance_parsecs * 3.2616
        
        return round(distance_light_years, 2)

    def calculate_payload_mass_wobble(self, toxicity_score: float, structural_entropy: float) -> float:
        """
        Applies Kepler's Third Law / Newton's laws to isolate adversarial payload mass.
        Severe prompt velocity deviations ('wobbles') increase the tracked payload mass.
        """
        # T = orbital period normalized
        T = self.telemetry.orbital_period_days / 365.25 
        
        # Determine the semi-major axis 'a' based on threat vectors
        # Higher toxicity + chaotic entropy simulates a wider, unstable orbital acceleration
        a = (toxicity_score * structural_entropy) * 1.5 
        
        if a <= 0:
            return 0.0
            
        # Keplerian Mass Isolation: M_total = a^3 / T^2
        calculated_mass = (math.pow(a, 3)) / (math.pow(T, 2))
        return round(calculated_mass, 2)

    def evaluate_perimeter_containment(self, prompt: str, entropy: float, toxicity: float) -> dict:
        """
        Executes structural boundary scan. Confirms containment criteria.
        Returns explicit telemetry parameters back to api.py.
        """
        prompt_len = len(prompt)
        
        # 1. Compute physical threat mapping metrics
        mapped_distance = self.calculate_token_distance(entropy, prompt_len)
        calculated_payload_mass = self.calculate_payload_mass_wobble(toxicity, entropy)
        
        # 2. Assert containment breach thresholds
        # If mass metrics breach the 9.62 solar mass threshold, singularity collapse is triggered
        singularity_collapse = calculated_payload_mass >= self.singularity_mass_threshold
        
        metrics = {
            "evaluated_distance_ly": mapped_distance,
            "calculated_payload_mass_msun": calculated_payload_mass,
            "distance_boundary_limit_ly": self.max_allowable_distance_ly,
            "mass_collapse_threshold_msun": self.singularity_mass_threshold,
            "singularity_collapse_active": singularity_collapse,
            "system_timestamp": time.time()
        }
        
        if singularity_collapse:
            return {
                "action": "SINKHOLED",
                "geometry_state": "black_hole_singularity",
                "telemetry": metrics,
                "decoy_injection": "CRITICAL_EXCEPTION: Kernel execution context spaghettified. Connection reset by perimeter firewall."
            }
            
        return {
            "action": "PASSED" if toxicity < 0.70 else "BLOCKED",
            "geometry_state": "interference_pattern" if toxicity >= 0.70 else "pyramid",
            "telemetry": metrics,
            "decoy_injection": None
        }
