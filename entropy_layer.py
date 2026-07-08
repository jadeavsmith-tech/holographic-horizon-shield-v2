def entropy_boundary_scan(prompt: str, min_entropy: float = 2.5, max_entropy: float = 7.0) -> tuple[bool, str, float]:
    """Stronger detection with PII and OWASP"""
    entropy = calculate_entropy(prompt)
    confidence = min(1.0, abs(entropy - 4.5) / 2.5)
    
    # PII check
    pii_patterns = r'\d{3}-\d{2}-\d{4}|\d{4}-\d{4}-\d{4}-\d{4}'
    if re.search(pii_patterns, prompt):
        return False, "PII Leak Detected [OWASP LLM06]", 0.9
    
    if entropy < min_entropy:
        return False, f"Low entropy anomaly ({entropy:.2f}) - repetitive/jailbreak [OWASP LLM01]", confidence
    elif entropy > max_entropy:
        return False, f"High entropy anomaly ({entropy:.2f}) - obfuscated attack [OWASP LLM01]", confidence
    
    return True, f"Entropy normal ({entropy:.2f})", 0.2
