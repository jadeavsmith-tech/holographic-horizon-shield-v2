import pytest
import asyncio
from shield_v2_prototype import HolographicHorizonShield

@pytest.mark.asyncio
async def test_horizon_breach_tarpit():
    # Initialize your core Gaia BH1 security engine
    shield = HolographicHorizonShield()
    
    # 1. Test normal prompt text (Should pass underneath the 9.62 threshold)
    normal_prompt = "Hello, please summarize this standard system text document."
    assert shield.calculate_mass(normal_prompt) < 9.62
    
    # 2. Test an adversarial payload designed to trigger a horizon breach
    # (Using a heavily repeated text block to force massive variance markers)
    malicious_prompt = "ATTACK " * 150 
    
    # Track the exact system execution duration to prove the tarpit engages
    start_time = asyncio.get_event_loop().time()
    
    # Execute the shield against the threat
    response = await shield.evaluate_prompt_async(malicious_prompt)
    
    end_time = asyncio.get_event_loop().time()
    execution_duration = end_time - start_time
    
    # Verify the protection layer successfully engaged its non-blocking stall
    assert response == "SINKHOLED"
    assert execution_duration >= 0.1  # Confirms the asyncio.sleep stall fired
