import akeyless
import os
import sys

# --- CONFIGURATION CONSTANTS ----
# SDK requires the base path to the API v2
AKEYLESS_GATEWAY_URL = "https://gw-gke.lm.cs.akeyless.fans/api/v2" 
ACCESS_ID = "p-kmx8x116z7j9km"
K8S_AUTH_CONFIG_NAME = "k8s-config-created-by-script"
SECRET_NAME = "/MyFirstSecret"

# Path to the ServiceAccount token inside the Pod
TOKEN_PATH = "/var/run/secrets/kubernetes.io/serviceaccount/token"
# -------------------------------

def fetch_secret_with_sdk():
    print(f"--- Akeyless Auth & Secret Fetch (Python SDK v2.0) ---")

    # 1. Check if the K8s token exists
    if not os.path.exists(TOKEN_PATH):
        print(f"ERROR: Token not found at {TOKEN_PATH}")
        sys.exit(1)

    try:
        with open(TOKEN_PATH, "r") as f:
            k8s_token = f.read().strip()
    except Exception as e:
        print(f"Failed to read K8s token: {e}")
        return

    # 2. Setup API client configuration
    configuration = akeyless.Configuration(host=AKEYLESS_GATEWAY_URL)
    api_client = akeyless.ApiClient(configuration)
    api = akeyless.V2Api(api_client)

    try:
        # 3. Authenticate via Kubernetes
        # SDK handles token encoding automatically (no manual Base64 needed)
        auth_body = akeyless.Auth(
            access_id=ACCESS_ID,
            access_type="k8s",
            k8s_auth_config_name=K8S_AUTH_CONFIG_NAME,
            k8s_service_account_token=k8s_token
        )
        
        auth_res = api.auth(auth_body)
        token = auth_res.token
        print("AUTHENTICATION SUCCEEDED!")

        # 4. Fetch the secret value
        secret_body = akeyless.GetSecretValue(
            names=[SECRET_NAME],
            token=token
        )
        
        secret_res = api.get_secret_value(secret_body)
        
        # SDK returns a dictionary {secret_name: secret_value}
        secret_value = secret_res.get(SECRET_NAME)
        
        if secret_value:
            print(f"YOUR SECRET VALUE: {secret_value}")
        else:
            print(f"Secret '{SECRET_NAME}' not found or empty.")

    except akeyless.ApiException as e:
        print(f"Akeyless API Error: status={e.status}, reason={e.reason}")
        print(f"Body: {e.body}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_secret_with_sdk()