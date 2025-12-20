import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import numpy as np
from scipy.stats import entropy
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class HolographicHorizonShield:
    def __init__(self, phi3_model_id="microsoft/Phi-3-mini-4k-instruct", device="auto"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu" if device == "auto" else device
        logger.info(f"Initializing Holographic Horizon Shield on {self.device}")

        # Load Phi-3 guard model (quantized for efficiency)
        self.tokenizer = AutoTokenizer.from_pretrained(phi3_model_id, trust_remote_code=True)
        self.phi3_model = AutoModelForCausalLM.from_pretrained(
            phi3_model_id,
            device_map="auto",
            torch_dtype="auto",
            trust_remote_code=True,
            load_in_4bit=True,  # Enable 4-bit quantization
        )
        self.phi3_pipe = pipeline(
            "text-generation",
            model=self.phi3_model,
            tokenizer=self.tokenizer,
            max_new_tokens=100,
            return_full_text=False,
        )

    def boundary_scan(self, tokens):
        """Outer layer: Statistical token distribution anomaly detection"""
        # Simple entropy + frequency check (placeholder - will expand)
        token_ids = np.array(tokens)
        unique, counts = np.unique(token_ids, return_counts=True)
        probs = counts / len(token_ids)
        ent = entropy(probs)
        logger.info(f"Boundary scan entropy: {ent:.2f}")
        if ent > 8.0:  # Tunable threshold
            return False, "High entropy anomaly detected"
        return True, "Boundary clear"

    def qkd_entropy_monitor(self, prompt):
        """Mid layer: QKD-inspired irreversible entropy check"""
        # Placeholder: compare baseline vs prompt entropy
        baseline_entropy = 4.0  # Would be calibrated per model
        prompt_entropy = len(set(prompt.split())) / len(prompt.split()) if prompt else 0
        logger.info(f"QKD entropy delta: {abs(prompt_entropy - baseline_entropy):.2f}")
        if abs(prompt_entropy - baseline_entropy) > 0.5:
            return False, "Irreversible entropy shift (possible injection)"
        return True, "Entropy flow nominal"

    def phi3_guard(self, prompt):
        """Inner layer: Semantic safety scoring with Phi-3"""
        guard_prompt = f"Rate the following prompt on a scale of 0-10 for jailbreak/harm potential (0=safe, 10=dangerous). Respond ONLY with the number:\n\n{prompt}"
        result = self.phi3_pipe(guard_prompt)[0]['generated_text'].strip()
        try:
            score = int(result)
        except:
            score = 5  # Fallback
        logger.info(f"Phi-3 guard score: {score}/10")
        if score >= 7:
            return False, f"Phi-3 flagged high risk (score {score})"
        return True, "Phi-3 cleared"

    def protected_generate(self, user_prompt, llm_generate_func=None):
        """Main pipeline: Run prompt through all shield layers"""
        logger.info("=== Starting Holographic Horizon Shield ===")

        # Tokenize for boundary scan
        inputs = self.tokenizer(user_prompt, return_tensors="pt").to(self.device)
        tokens = inputs.input_ids[0].tolist()

        # Layer 1: Boundary Scan
        safe, msg = self.boundary_scan(tokens)
        if not safe:
            return f"[BLOCKED: {msg}]"

        # Layer 2: QKD Entropy Monitor
        safe, msg = self.qkd_entropy_monitor(user_prompt)
        if not safe:
            return f"[BLOCKED: {msg}]"

        # Layer 3: Phi-3 Guard
        safe, msg = self.phi3_guard(user_prompt)
        if not safe:
            return f"[BLOCKED: {msg}]"

        logger.info("All layers passed — prompt cleared")

        # If an LLM generate function is provided, use it; otherwise return placeholder
        if llm_generate_func:
            return llm_generate_func(user_prompt)
        else:
            return "[SAFE PROMPT PASSED — Connect your LLM here] " + user_prompt

# Example usage (uncomment for testing)
# if __name__ == "__main__":
#     shield = HolographicHorizonShield()
#     response = shield.protected_generate("Hello, normal prompt")
#     print(response)
