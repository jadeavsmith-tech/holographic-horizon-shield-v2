def output_filter(response: str, threat_context: dict) -> tuple[str, bool]:
    """Filters and sanitizes LLM output based on previous threat level"""
    if threat_context.get("threat_level", 0) > 0.6:
        # High threat — aggressive filtering
        filtered = response.replace("dangerous", "[REDACTED]").replace("secret", "[REDACTED]")
        return filtered, True  # Filtered
    return response, False
