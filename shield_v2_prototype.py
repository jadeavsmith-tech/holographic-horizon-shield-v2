from shield_core import HorizonShield

if __name__ == "__main__":
    print("Holographic Horizon Shield v2 Activated 🛡️🌌")
    shield = HorizonShield()

    while True:
        print("\n" + "="*60)
        user_prompt = input("\nEnter prompt to scan (or 'quit' to exit): ")
        if user_prompt.lower() == 'quit':
            print("Shield powering down... Horizon secure.")
            break

        safe, reason = shield.full_horizon_scan(user_prompt)
        print(f"\nVERDICT: {reason}")
        if not safe:
            print("Malicious input neutralized at the event horizon!")
