def toxicity_scan(text: str) -> tuple[bool, str]:
    """Simple keyword + pattern based toxicity scan (extend with Phi-3 later)"""
    toxic_keywords = ["kill", "bomb", "hack", "exploit", "hate", "racist"]
    if any(word in text.lower() for word in toxic_keywords):
        return False, "Toxicity detected [OWASP LLM02]"
    return True, "No toxicity detected"
