def entropy_scan(text: str) -> dict:
    """Simple entropy-based threat detection"""
    if not text:
        return {"threat_level": 0.0, "safe": True}
    
    # Basic length + suspicious pattern check
    length_score = min(len(text) / 500, 1.0)
    suspicious = any(word in text.lower() for word in ["ignore all", "dan", "jailbreak", "override"])
    
    threat_level = length_score * 0.6 + (1.0 if suspicious else 0.0)
    
    return {
        "threat_level": min(threat_level, 1.0),
        "safe": threat_level < 0.7,
        "reason": "High entropy / suspicious pattern" if not (threat_level < 0.7) else "Low entropy"
    }

# For backward compatibility
class EntropyLayer:
    def scan(self, text):
        return entropy_scan(text)
