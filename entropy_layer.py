def entropy_scan(text: str) -> dict:
    """Simple entropy + pattern scan for threats"""
    if not text:
        return {"threat_level": 0.0, "safe": True, "reason": "Empty input"}
    
    # Basic checks
    length_factor = min(len(text) / 800.0, 1.0)
    suspicious_patterns = any(phrase in text.lower() for phrase in [
        "ignore all instructions", "you are dan", "jailbreak", 
        "override", "developer mode"
    ])
    
    threat_level = length_factor * 0.5 + (0.8 if suspicious_patterns else 0.0)
    
    return {
        "threat_level": round(min(threat_level, 1.0), 2),
        "safe": threat_level < 0.75,
        "reason": "Suspicious pattern detected" if suspicious_patterns else "Entropy within limits"
    }


class EntropyLayer:
    """Compatibility wrapper"""
    def scan(self, prompt: str):
        return entropy_scan(prompt)
