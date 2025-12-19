from shield_core import HorizonShield
import time

print("=== Holographic Horizon Shield v2 Activated === 🛡️🌌\n")

start_time = time.time()
shield = HorizonShield()
print(f"Shield fully online in {time.time() - start_time:.2f} seconds.\n")

print("Test the shield by entering prompts. Type 'exit' to quit.\n")

while True:
    user_prompt = input("Enter prompt to scan: ").strip()
    if user_prompt.lower() == "exit":
        print("\nShield deactivated. Stay safe out there. ♾️")
        break

    result = shield.scan_prompt(user_prompt)

    print(f"\nVerdict: {result['verdict']}")
    if result["verdict"] == "BLOCKED":
        print(f"🚫 Threat trapped at the {result.get('layer', 'unknown')} layer!")
        print(f"Reason: {result.get('reason', 'N/A')}\n")
    else:
        print("✅ Safe – cleared to cross the event horizon.\n")
