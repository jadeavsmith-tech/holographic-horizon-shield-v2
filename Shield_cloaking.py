import re
from typing import Dict, Tuple

class PIICloakingDevice:
    def __init__(self):
        # Sci-fi themed replacement tokens
        self.registry: Dict[str, str] = {}
        self.reverse_registry: Dict[str, str] = {}
        self.counter = 0

        # High-accuracy regex patterns for real-world PII
        self.patterns = {
            "EMAIL": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
            "PHONE": r"\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}",
            "API_KEY": r"(sk|pk|key|secret|token)-[a-zA-Z0-9]{32,}"
        }

    def _generate_token(self, pii_type: str) -> str:
        self.counter += 1
        return f"🛸_SECTOR_DATA_{pii_type}_{self.counter:04d}_🛸"

    def cloak(self, prompt: str) -> str:
        """Scrubs real PII and replaces it with secure sci-fi tokens."""
        cloaked_prompt = prompt
        
        for pii_type, pattern in self.patterns.items():
            matches = re.findall(pattern, cloaked_prompt)
            for match in set(matches):
                if match not in self.registry:
                    token = self._generate_token(pii_type)
                    self.registry[match] = token
                    self.reverse_registry[token] = match
                
                cloaked_prompt = cloaked_prompt.replace(match, self.registry[match])
                
        return cloaked_prompt

    def decloak(self, model_response: str) -> str:
        """Restores the original PII tokens into the final generated output."""
        decloaked_response = model_response
        
        for token, original_value in self.reverse_registry.items():
            if token in decloaked_response:
                decloaked_response = decloaked_response.replace(token, original_value)
                
        return decloaked_response

# Quick integration verification
if __name__ == "__main__":
    device = PIICloakingDevice()
    
    # Simulate a user trying to feed credentials/PII to the model
    raw_input = "Transmit coordinates to test@galaxy-net.org using subspace key sk-xyz1234567890abcdef1234567890abcdef."
    print(f"📥 Raw Input:   {raw_input}")
    
    cloaked = device.cloak(raw_input)
    print(f"🛡️ Cloaked:     {cloaked}")
    
    # Simulate a safe response coming back from Phi-3 containing our token
    simulated_output = f"Acknowledged. Connection established with {device.registry.get('test@galaxy-net.org')} via secured relay channels."
    print(f"🤖 AI Response: {simulated_output}")
    
    restored = device.decloak(simulated_output)
    print(f"📤 Restored:    {restored}")
