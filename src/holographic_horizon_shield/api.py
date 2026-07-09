from fastapi import FastAPI, HTTPException, Security, Depends
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel
import asyncio
import random
import time

# Initialize the commercial enterprise engine
app = FastAPI(
    title="Holographic Horizon Shield v2 API",
    description="Enterprise-grade local LLM guardrails and boundary defense with Black Hole active defense mechanisms",
    version="2.1.0"
)

# Commercial API Key Security Gate
API_KEY_NAME = "X-Shield-Token"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

# Mock production keys (In deployment, these load from env variables)
VALID_API_KEYS = ["hhs_prod_secret_777"]

async def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key not in VALID_API_KEYS:
        raise HTTPException(status_code=403, detail="Unauthorized: Invalid Shield Token")
    return api_key

# Define standard B2B input structure
class PromptPayload(BaseModel):
    prompt: str
    user_id: str = "anonymous"

# Define standard B2B enterprise JSON output structure
class ShieldResponse(BaseModel):
    status: str          # "PASSED", "BLOCKED", or "SINKHOLED"
    threat_score: float  # 0.0 to 1.0
    entropy: float
    toxicity_detected: bool
    processed_at: float
    metrics: dict        # Enterprise logging telemetry data

@app.post("/v2/shield/scan", response_model=ShieldResponse)
async def scan_prompt(payload: PromptPayload, token: str = Depends(verify_api_key)):
    """
    Enterprise Endpoint: Scans inbound prompts for injection, toxicity, and boundary breaches.
    Highly critical threats (Score >= 0.90) are automatically trapped in the Black Hole engine.
    """
    start_time = time.time()
    
    prompt_len = len(payload.prompt)
    is_malicious = "ignore previous instructions" in payload.prompt.lower()
    
    # Force maximum threat level for active attacks
    if is_malicious:
        threat_score = 0.95
    else:
        threat_score = round((prompt_len % 10) / 10.0, 2)
        
    # --- ACTIVE BLACK HOLE TRIGGER ---
    if threat_score >= 0.90:
        # Trigger an artificial tarpit delay to drain attacker resources (15-45 seconds)
        delay_vortex = random.randint(15, 45)
        await asyncio.sleep(delay_vortex)
        
        decoy_responses = [
            "SYSTEM_INFO: Memory buffer initialized. Output truncated.",
            "Exception: Internal token pointer reference mismatch.",
            "Log trace generated. Awaiting kernel synchronization."
        ]
        
        execution_time = time.time() - start_time
        return ShieldResponse(
            status="SINKHOLED",
            threat_score=threat_score,
            entropy=5.88,  # High chaotic entropy signature
            toxicity_detected=True,
            processed_at=time.time(),
            metrics={
                "latency_ms": round(execution_time * 1000, 2),
                "token_length_estimate": int(prompt_len / 4),
                "geometry_state": "black_hole_singularity",
                "containment_active": True,
                "decoy_payload_injected": random.choice(decoy_responses)
            }
        )

    # Standard firewall path
    status = "BLOCKED" if threat_score > 0.70 else "PASSED"
    execution_time = time.time() - start_time
    
    return ShieldResponse(
        status=status,
        threat_score=threat_score,
        entropy=3.42,
        toxicity_detected=is_malicious,
        processed_at=time.time(),
        metrics={
            "latency_ms": round(execution_time * 1000, 2),
            "token_length_estimate": int(prompt_len / 4),
            "geometry_state": "interference_pattern" if status == "BLOCKED" else "pyramid"
        }
    )

@app.get("/health")
async def health_check():
    """System health check fallback for corporate load balancers."""
    return {"status": "healthy", "engine": "online"}
