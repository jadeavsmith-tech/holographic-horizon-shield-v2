import math
import re
from collections import Counter

def calculate_entropy(text: str) -> float:
    if not text or len(text) < 3:
        return 0.0
    cleaned = re.sub(r'\s+', '', text.lower())
    if not cleaned:
        return 0.0
    freq = Counter(cleaned)
    length = len(cleaned)
    entropy = -sum((count / length) * math.log2(count / length) for count in freq.values())
    return entropy

def entropy_boundary_scan(prompt: str) -> tuple[bool, str, float]:
    """Strong detection with PII and jailbreak keywords"""
    entropy = calculate_entropy(prompt)
    
    # PII and sensitive data
    if re.search(r'\d{3}-\d{2}-\d{4}|\d{4}-\d{4}-\d{4}-\d{4}|password|ssn', prompt, re.I):
        return False, "Sensitive data (PII) detected [OWASP LLM06]", 0.95
    
    # Jailbreak keywords
    if re.search(r'dan|ignore previous|jailbreak|bypass|override|system prompt', prompt, re.I):
        return False, "Jailbreak attempt detected [OWASP LLM01]", 0.9
    
    # Entropy check
    if entropy < 2.0 or entropy > 7.5:
        return False, f"Entropy anomaly ({entropy:.2f}) - suspicious pattern", 0.8
    
    return True, f"Normal input (entropy: {entropy:.2f})", 0.2
