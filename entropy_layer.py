import math
import re
from collections import Counter

def calculate_entropy(text: str) -> float:
    """Calculate Shannon entropy - measures randomness of the text."""
    if not text or len(text) < 3:
        return 0.0
    cleaned = re.sub(r'\s+', '', text.lower())
    if not cleaned:
        return 0.0
    freq = Counter(cleaned)
    length = len(cleaned)
    entropy = -sum((count / length) * math.log2(count / length) for count in freq.values())
    return entropy

def entropy_boundary_scan(prompt: str, min_entropy: float = 3.0, max_entropy: float = 6.5) -> tuple[bool, str, float]:
    """Returns (safe, reason with OWASP tag, confidence 0-1)"""
    entropy = calculate_entropy(prompt)
    deviation = abs(entropy - 4.5)
    confidence = min(1.0, deviation / 3.0)
    
    if entropy < min_entropy:
        return False, f"Low entropy anomaly ({entropy:.2f}) - possible repetitive attack [OWASP LLM01]", confidence
    elif entropy > max_entropy:
        return False, f"High entropy anomaly ({entropy:.2f}) - possible obfuscated payload [OWASP LLM01]", confidence
    
    return True, f"Entropy normal ({entropy:.2f}) - looks safe", 0.1
