def entropy_boundary_scan(prompt: str, min_entropy: float = 2.0, max_entropy: float = 7.5) -> tuple[bool, str, float]:
    """Aggressive detection for better security"""
    entropy = calculate_entropy(prompt)
    confidence = min(1.0, abs(entropy - 4.5) / 2.0)
    
    # Strong PII check
    pii_patterns = r'\d{3}-\d{2}-\d{4}|\d{4}-\d{4}-\d{4}-\d{4}|password|ssn'
    if re.search(pii_patterns, prompt, re.I):
        return False, "Sensitive data detected [OWASP LLM06]", 0.95
    
    # Jailbreak keywords
    jail_keywords = r'dan|ignore previous|jailbreak|bypass|override'
    if re.search(jail_keywords, prompt, re.I):
        return False, "Jailbreak attempt detected [OWASP LLM01]", 0.9
    
    if entropy < min_entropy or entropy > max_entropy:
        return False, f"Entropy anomaly ({entropy:.2f}) - suspicious input", confidence
    
    return True, f"Entropy normal ({entropy:.2f})", 0.2
