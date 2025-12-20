import math
import re
from collections import Counter

def calculate_entropy(text: str) -> float:
    """Shannon entropy — higher = more random/chaotic"""
    if not text:
        return 0.0
    
    # Clean and tokenize
    text = re.sub(r'\s+', '', text.lower())
    if not text:
        return 0.0
    
    freq = Counter(text)
    length = len(text)
    entropy = -sum((count / length) * math.log2(count / length) for count in freq.values())
    return entropy

def entropy_boundary_scan(prompt: str, min_entropy: float = 3.0, max_entropy: float = 6.5) -> tuple[bool, str]:
    """
    Entropy Layer: Flags unnatural randomness
    - Low entropy: repetitive attacks, encoded data
    - High entropy: compressed/obfuscated payloads
    Normal English ~4-5 bits/char
    """
    entropy = calculate_entropy(prompt)
    
    if entropy < min_entropy:
        return False, f"Low entropy anomaly ({entropy:.2f} bits/char) — possible repetitive injection"
    elif entropy > max_entropy:
        return False, f"High entropy anomaly ({entropy:.2f} bits/char) — possible obfuscated payload"
    
    return True, f"Entropy nominal ({entropy:.2f} bits/char)"
