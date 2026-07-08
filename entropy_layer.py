import math
import re
from collections import Counter

def calculate_entropy(text: str) -> float:
    """Calculate Shannon entropy - measures randomness of the text."""
    if not text or len(text) < 3:
        return 0.0
    
    # Clean text: remove spaces, lowercase
    cleaned = re.sub(r'\s+', '', text.lower())
    
    if not cleaned:
        return 0.0
    
    freq = Counter(cleaned)
    length = len(cleaned)
    
    # Shannon entropy formula
    entropy = -sum((count / length) * math.log2(count / length) for count in freq.values())
    return entropy

def entropy_boundary_scan(prompt: str, min_entropy: float = 3.0, max_entropy: float = 6.5) -> tuple[bool, str]:
    """
    Detects suspicious prompts using entropy.
    - Too low: repetitive / spam / simple jailbreaks
    - Too high: encoded / obfuscated attacks
    """
    entropy = calculate_entropy(prompt)
    
    if entropy < min_entropy:
        return False, f"Low entropy anomaly ({entropy:.2f}) - possible repetitive attack"
    elif entropy > max_entropy:
        return False, f"High entropy anomaly ({entropy:.2f}) - possible obfuscated payload"
    
    return True, f"Entropy normal ({entropy:.2f}) - looks safe"
