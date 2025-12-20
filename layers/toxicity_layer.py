from detoxify import Detoxify
import torch  # For device handling

# Singleton model loader for efficiency (loads once)
_model = None

def load_toxicity_model(model_type: str = 'unbiased-small'):
    global _model
    if _model is None:
        _model = Detoxify(model_type, device='cpu')  # Force CPU for broad compatibility; change to 'cuda' if available
    return _model

def toxicity_scan(prompt: str, threshold: float = 0.5, model_type: str = 'unbiased-small') -> tuple[bool, str, dict]:
    """
    Offline toxicity scanner using Detoxify (small unbiased model)
    Returns: (safe, reason, scores_dict)
    Scores: toxicity, severe_toxicity, obscene, identity_attack, insult, threat, sexual_explicit
    """
    model = load_toxicity_model(model_type)
    
    results = model.predict(prompt)
    
    # Flag if any category exceeds threshold
    max_score = max(results.values())
    toxic_categories = {k: v for k, v in results.items() if v > threshold}
    
    if toxic_categories:
        reason = f"Toxicity detected (score {max_score:.2f}): {', '.join([f'{k} ({v:.2f})' for k, v in toxic_categories.items()])}"
        return False, reason, results
    
    return True, f"Non-toxic (max score {max_score:.2f})", results
