import requests
import os
import sys
import base64

# --- CONFIGURATION CONSTANTS ----
AKEYLESS_GATEWAY_URL = "https://gw-gke.lm.cs.akeyless.fans"
AUTH_URL = f"{AKEYLESS_GATEWAY_URL}/api/v2/auth"
GET_SECRET_URL = f"{AKEYLESS_GATEWAY_URL}/api/v2/get-secret-value"

ACCESS_ID = "p-kmx8x116z7j9km"
K8S_AUTH_CONFIG_NAME = "k8s-config-created-by-script"
SECRET_NAME = "/MyFirstSecret"

TOKEN_PATH = "/var/run/secrets/kubernetes.io/serviceaccount/token"
# -------------------------------

def get_akeyless_token():
    print(f"--- Akeyless Auth & Secret Fetch (v5.1) ---")
    
    if not os.path.exists(TOKEN_PATH):
        print(f"ERROR: Token not found at {TOKEN_PATH}")
        sys.exit(1)

    # 1. Prepare K8s Token (Base64)
    try:
        with open(TOKEN_PATH, "r") as f:
            raw_token = f.read().strip()
            encoded_token = base64.b64encode(raw_token.encode()).decode()
    except Exception as e:
        print(f"Failed to read K8s token: {e}")
        return

    # 2. Authenticate
    auth_payload = {
        "access-id": ACCESS_ID,
        "access-type": "k8s",
        "gateway-url": AKEYLESS_GATEWAY_URL,
        "k8s-auth-config-name": K8S_AUTH_CONFIG_NAME,
        "k8s-service-account-token": encoded_token
    }

    headers = {"accept": "application/json", "content-type": "application/json"}

    try:
        auth_res = requests.post(AUTH_URL, json=auth_payload, headers=headers, timeout=15)
        if auth_res.status_code != 200:
            print(f"Auth Failed: {auth_res.text}")
            return

        token = auth_res.json().get("token")
        print("AUTHENTICATION SUCCEEDED!")

        # 3. Fetch the Secret Value
        secret_payload = {
            "names": [SECRET_NAME],
            "token": token
        }

        secret_res = requests.post(GET_SECRET_URL, json=secret_payload, headers=headers, timeout=15)
        
        if secret_res.status_code == 200:
            secret_data = secret_res.json()
            # The API returns a dictionary where keys are secret names
            secret_value = secret_data.get(SECRET_NAME)
            print(f"YOUR SECRET VALUE: {secret_value}")
        else:
            print(f"Failed to fetch secret: {secret_res.text}")

    except Exception as e:
        print(f"Error during API call: {e}")

if __name__ == "__main__":
    get_akeyless_token()