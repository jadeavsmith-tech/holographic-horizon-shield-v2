import json
import re

class HorizonShieldGuardrails:
def __init__(self, config_path="config.json"):
with open(config_path, "r") as f:
self.config = json.load(f)
            
def verify_input(self, user_input: str) -> dict:
# Check token/length limits
if len(user_input.split()) > self.config["shield_settings"]["max_input_tokens"]:
return {"safe": False, "reason": "Input length limit exceeded."}
            
# Scan for blacklisted adversarial patterns
for keyword in self.config["blocked_keywords"]:
if re.search(r'\b' + re.escape(keyword) + r'\b', user_input, re.IGNORECASE):
return {"safe": False, "reason": f"Heuristic match: Found blocked pattern '{keyword}'"}
                
return {"safe": True, "reason": "Passed pre-processing guardrails."}
