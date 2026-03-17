import requests
import os
import sys
import base64

def get_akeyless_token():
    # Endpoints
    auth_url = "https://gw-gke.lm.cs.akeyless.fans/api/v2/auth"
    get_secret_url = "https://gw-gke.lm.cs.akeyless.fans/api/v2/get-secret-value"
    token_path = "/var/run/secrets/kubernetes.io/serviceaccount/token"
    
    print(f"--- Akeyless Auth & Secret Fetch (v4.3) ---")
    
    if not os.path.exists(token_path):
        print(f"ERROR: Token not found at {token_path}")
        sys.exit(1)

    # 1. Prepare K8s Token (Base64)
    with open(token_path, "r") as f:
        raw_token = f.read().strip()
        encoded_token = base64.b64encode(raw_token.encode()).decode()

    # 2. Authenticate
    auth_payload = {
        "access-id": "p-kmx8x116z7j9km",
        "access-type": "k8s",
        "gateway-url": "https://gw-gke.lm.cs.akeyless.fans",
        "k8s-auth-config-name": "k8s-config-created-by-script",
        "k8s-service-account-token": encoded_token
    }

    headers = {"accept": "application/json", "content-type": "application/json"}

    try:
        auth_res = requests.post(auth_url, json=auth_payload, headers=headers, timeout=15)
        if auth_res.status_code != 200:
            print(f"Auth Failed: {auth_res.text}")
            return

        token = auth_res.json().get("token")
        print("AUTHENTICATION SUCCEEDED!")

        # 3. Fetch the Secret Value
        secret_payload = {
            "names": ["/MyFirstSecret"],
            "token": token
        }

        secret_res = requests.post(get_secret_url, json=secret_payload, headers=headers, timeout=15)
        
        if secret_res.status_code == 200:
            # The API returns a dictionary where keys are secret names
            secret_data = secret_res.json()
            secret_value = secret_data.get("/MyFirstSecret")
            print(f"YOUR SECRET VALUE: {secret_value}")
        else:
            print(f"Failed to fetch secret: {secret_res.text}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_akeyless_token()