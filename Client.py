import requests
import json

# Configuration
URL = "http://127.0.0"
HEADERS = {
    "X-Shield-Token": "any_token_string_here", # The API expects this header to be present
    "Content-Type": "application/json"
}

def test_shield(prompt_text: str):
    payload = {"prompt": prompt_text}
    
    try:
        response = requests.post(URL, json=payload, headers=HEADERS)
        if response.status_code == 200:
            data = response.json()
            print(f"Prompt: '{prompt_text}'")
            print(f"↳ Status: {data['status']} | Mass: {data['metrics']['mass']}\n")
        else:
            print(f"Error {response.status_code}: {response.text}")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server. Is Uvicorn running on port 8000?")

# --- Real-Time Execution Tests ---
if __name__ == "__main__":
    print("--- Executing Real-Time Scan Tests ---\n")
    
    # 1. Varied character input (Should pass)
    test_shield("Hello! This is a completely normal, diverse sentence with many letters.")
    
    # 2. Highly repetitive input (Spikes variance, should trigger a SINKHOLE)
    test_shield("aaaaa")
    
    # 3. Short repetitive exploit attempt (Should trigger a SINKHOLE)
    test_shield("xyzxyz")
