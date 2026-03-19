# Akeyless Kubernetes Authentication Demo

### 🎯 Project Goal
**The goal of this project is to demonstrate how the **keyless** Akeyless Kubernetes Authentication method works using a Python application as an example. It covers everything from namespace creation to secret retrieval.**

### 🧩 Process Decomposition
The authentication flow follows these logical steps:
1. **Identity**: The Pod identifies itself using a Kubernetes ServiceAccount token.
2. **Handshake**: The Python app sends this token to the Akeyless Gateway.
3. **Validation**: The Gateway verifies the token with the Kubernetes API server.
4. **Access**: Upon successful verification, Akeyless provides a temporary access token to fetch secrets.

## 🛠️ Prerequisites
Before starting this demo, you must have a functional **Akeyless Kubernetes Auth Method** configured in your Gateway. If you haven't set this up yet, you can use this automation tool:
- **K8s Auth Setup Tool**: [Kubernetes-Authentication](https://github.com/leon-maister/Kubernetes-Authentication)

## 📂 File Descriptions
| File | Function |
| :--- | :--- |
| get_akeyless_secret.py | Python logic with Base64 encoding for K8s tokens. |
| serviceaccount.yaml | Identity for the Pod (ServiceAccount). |
| deployment.yaml | Deployment manifest for the application pod. |
| dockerfile | Builds the application container. |

## ⚠️ Configuration
Before building the image, open `get_akeyless_secret.py` and set your specific constants:
- `AKEYLESS_GATEWAY_URL`: Your Gateway address.
- `ACCESS_ID`: Your Akeyless **Kubernetes Auth Method** Access ID.
- `K8S_AUTH_CONFIG_NAME`: The name of your K8s Auth configuration.
- `SECRET_NAME`: The path to the secret you want to fetch.

## 👩‍💻 For Developer
### Build and Push the Image
```bash
docker build -t leon-maister/akeyless-k8s-demo:5.0 .
docker push leon-maister/akeyless-k8s-demo:5.0
```

## 🚀 Quick Start Guide

### 1. Environment Setup
Run these commands to prepare your cluster:
```bash
# Create namespace if it doesn't exist
kubectl create namespace akeyless-kubernetes-authentication-demo --dry-run=client -o yaml | kubectl apply -f -

# Apply ServiceAccount
kubectl apply -f serviceaccount.yaml
```

### 2. Deploy and Verify
Run these commands to launch and check:
```bash
# Launch the application
kubectl apply -f deployment.yaml

# Check the results in logs
kubectl logs -f deployment/akeyless-kubernetes-authentication-app -n akeyless-kubernetes-authentication-demo
```

## ⚙️ Akeyless Configuration
For a successful handshake, ensure your Akeyless K8s Auth Method is configured to trust (at least ensuring it does not restrict access to these Namespaces):
- **Namespace**: `akeyless-kubernetes-authentication-demo`
- **ServiceAccount**: `akeyless-kubernetes-authentication-sa`

---
**Maintained by**: [leon-maister](https://github.com/leon-maister)

<small><sub>/home/keyless/k8s/test_k8s_auth</sub></small>
