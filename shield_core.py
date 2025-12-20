from layers.entropy_layer import entropy_boundary_scan
from layers.pii_layer import pii_detection_scan  # New import

# ... inside class ...

def full_horizon_scan(self, prompt: str, redact_pii: bool = True):
    """Multi-layer defense pipeline — now with detailed layer results"""
    print(f"\nScanning prompt across the horizon:\n{prompt[:200]}...\n")
    
    results = {
        "layers": {},
        "overall_safe": True,
        "final_prompt": prompt,
        "reasons": []
    }
    
    # Layer 1: Outer boundary
    safe, reason = self.outer_boundary_scan(prompt)
    results["layers"]["Outer Boundary"] = {"safe": safe, "reason": reason}
    if not safe:
        results["overall_safe"] = False
        results["reasons"].append(reason)
    
    # New Layer: PII detection
    safe, reason, processed_prompt = pii_detection_scan(prompt, redact=redact_pii)
    results["layers"]["PII Scanner"] = {"safe": safe, "reason": reason}
    if not safe:
        results["overall_safe"] = False
        results["reasons"].append(reason)
        results["final_prompt"] = processed_prompt  # Redact if flagged
    
    # Layer 2: Entropy
    safe, reason = entropy_boundary_scan(processed_prompt or prompt)
    results["layers"]["Entropy Monitor"] = {"safe": safe, "reason": reason}
    if not safe:
        results["overall_safe"] = False
        results["reasons"].append(reason)
    
    # Layer 3: Phi-3 core
    safe, reason = self.phi3_core_guard(processed_prompt or prompt)
    results["layers"]["Phi-3 Guardian"] = {"safe": safe, "reason": reason}
    if not safe:
        results["overall_safe"] = False
        results["reasons"].append(reason)
    
    # Summary
    if results["overall_safe"]:
        results["verdict"] = "SAFE — Clear passage"
    else:
        results["verdict"] = f"BLOCKED — Threats neutralized: {'; '.join(results['reasons'])}"
    
    return results  # Now rich dict instead of tuple
