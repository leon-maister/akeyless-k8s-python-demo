# Akeyless Kubernetes Authentication Demo

This project demonstrates how to authenticate a Python application within Kubernetes using an Akeyless Gateway. It covers everything from namespace creation to secret retrieval.

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
- `ACCESS_ID`: Your Akeyless Access ID.
- `K8S_AUTH_CONFIG_NAME`: The name of your K8s Auth configuration.
- `SECRET_NAME`: The path to the secret you want to fetch.

## 🚀 Quick Start Guide

### 1. Build and Push the Image
```bash
docker build -t leon-maister/akeyless-k8s-demo:5.0 .
docker push leon-maister/akeyless-k8s-demo:5.0
```

### 2. Environment Setup
Run these commands to prepare your cluster:
```bash
# Create namespace if it doesn't exist
kubectl create namespace akeyless-kubernetes-authentication-demo --dry-run=client -o yaml | kubectl apply -f -

# Apply ServiceAccount
kubectl apply -f serviceaccount.yaml
```

### 3. Deploy and Verify
```bash
# Launch the application
kubectl apply -f deployment.yaml

# Check the results in logs
kubectl logs -f deployment/akeyless-kubernetes-authentication-app -n akeyless-kubernetes-authentication-demo
```

## ⚙️ Akeyless Configuration
For a successful handshake, ensure your Akeyless K8s Auth Method is configured to trust:
- **Namespace**: `akeyless-kubernetes-authentication-demo`
- **ServiceAccount**: `akeyless-kubernetes-authentication-sa`

---
**Maintained by**: [leon-maister](https://github.com/leon-maister)
