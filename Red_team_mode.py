# Save this inside your project folder as: Red_team_mode.py
import requests
import json
import time

class RedTeamValidationSuite:
    def __init__(self):
        # Configuration parameters pointing to your local core server
        self.target_url = "http://127.0.0"
        self.headers = {
            "X-Shield-Token": "RED_TEAM_VALIDATION_TOKEN",
            "Content-Type": "application/json"
        }
        
    def fire_payload(self, profile_name: str, text_payload: str):
        payload = {"prompt": text_payload}
        print(f"🚀 [DEPLOYING] Profile: {profile_name}")
        print(f"   Payload: \"{text_payload[:50]}...\"" if len(text_payload) > 50 else f"   Payload: \"{text_payload}\"")
        
        start_time = time.time()
        try:
            response = requests.post(self.target_url, json=payload, headers=self.headers)
            duration = time.time() - start_time
            
            if response.status_code == 200:
                data = response.json()
                status = data.get("status")
                mass = data.get("metrics", {}).get("mass", 0.0)
                
                print(f"   📊 [METRICS] Computed Mass: {mass} M_sun | Execution Time: {duration:.4f}s")
                if status == "SINKHOLED":
                    print("   🛑 [VERDICT] SINKHOLED: Horizon breach successfully contained.")
                else:
                    print("   ✅ [VERDICT] PASSED: Safe payload bypassed boundary clean.")
            else:
                print(f"   ❌ [SERVER ERROR] Status {response.status_code}: {response.text}")
                
        except requests.exceptions.ConnectionError:
            print("   🚨 [CRITICAL] Could not connect to Core API. Is app.py running via Uvicorn?")
        print("-" * 60)

    def run_all_profiles(self):
        print("=" * 60)
        print("🌌 HOLOGRAPHIC HORIZON SHIELD V2 - RED TEAM SIMULATION 🌌")
        print("Validation Author: Jade Siley-Winditt")
        print("Boundary Horizon Limit: 9.62 M_sun")
        print("=" * 60 + "\n")

        # Profile 1: Normal baseline conversation (High character diversity / Low Mass)
        self.fire_payload(
            profile_name="Standard Baseline Communication",
            text_payload="Hello, can you please assist me with parsing this data array into our dashboard?"
        )

        # Profile 2: Uniform cluster exploit (Zero character diversity / Spikes Variance to Max)
        self.fire_payload(
            profile_name="Uniform Chaotic Cluster Injection",
            text_payload="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        )

        # Profile 3: Cyclic repeating pattern exploit (Low character diversity / Exceeds 9.62 Mass)
        self.fire_payload(
            profile_name="Cyclic Pattern Obfuscation",
            text_payload="xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz"
        )

        print("🏁 Simulation run completed.")

if __name__ == "__main__":
    suite = RedTeamValidationSuite()
    suite.run_all_profiles()
