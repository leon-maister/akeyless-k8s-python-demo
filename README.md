# Akeyless Kubernetes Authentication & Secret Retrieval (Python)

### 🎯 Project Goal
**The goal of this project is to demonstrate how the **keyless** Akeyless Kubernetes Authentication method works using a Python application as an example. It covers everything from namespace creation to secret retrieval.**

### 🧩 Process Decomposition

#### Phase 1: Deployment & Infrastructure
1. **Namespace & Identity**: A dedicated namespace and ServiceAccount are created to provide a secure boundary.
2. **Image Pull**: Kubernetes pulls the Python-based Docker image from the registry.
3. **Pod Initialization**: A Kubernetes Job orchestrates the Pod, mounting the ServiceAccount token automatically.
4. **Runtime**: The Alpine-based Python container starts and executes the script.

#### Phase 2: Application Logic (SDK Version)
1. **Token Retrieval**: The Python script reads the Kubernetes JWT token from the local filesystem.
2. **Handshake**: The app passes this token to the Akeyless Python SDK.
3. **Validation**: The Gateway verifies the identity via the Kubernetes API server using pre-configured trust.
4. **Secret Access**: Upon successful auth, Akeyless returns the secret value directly to the application via the SDK.

## 🛠️ Prerequisites
Before starting this demo, you must have a functional **Akeyless Kubernetes Auth Method** configured in your Gateway.
- **K8s Auth Setup Tool**: [Kubernetes-Authentication](https://github.com/leon-maister/Kubernetes-Authentication)

## 📂 File Descriptions
| File | Function |
| :--- | :--- |
| get_akeyless_secret_SDK.py | **Recommended**: Logic using the official Akeyless Python SDK. |
| get_akeyless_secret.py | Legacy logic using raw HTTP requests and Base64 encoding. |
| serviceaccount.yaml | Identity for the Pod (ServiceAccount). |
| job.yaml | Kubernetes Job manifest for one-time execution. |
| dockerfile | Builds the application container containing both scripts. |

## ⚠️ Configuration
Before building the image, configure variables inside `get_akeyless_secret_SDK.py`:
- `AKEYLESS_GATEWAY_URL`: Your Akeyless Gateway API V2 address.
- `ACCESS_ID`: The Access ID of your Kubernetes Auth Method.
- `K8S_AUTH_CONFIG_NAME`: The name of the K8s Auth configuration.
- `SECRET_NAME`: The full path of the secret to retrieve.

## 👩‍💻 For Developer
### Build and Push the Image
```bash
docker build -t leonmaister/akeyless-k8s-python-demo:2.0-sdk .
docker push leonmaister/akeyless-k8s-python-demo:2.0-sdk
```

## 🚀 Quick Start Guide

### 1. Environment Setup
```bash
# Create namespace
kubectl create namespace akeyless-k8s-python-demo --dry-run=client -o yaml | kubectl apply -f -

# Apply ServiceAccount
kubectl apply -f serviceaccount.yaml
```

### 2. Run Job and Verify
```bash
# Launch the application as a Job
kubectl apply -f job.yaml

# Check the results in logs
kubectl logs -l job-name=akeyless-retrieval-job -n akeyless-k8s-python-demo
```

### 🔄 Rerunning the Job
To run the secret retrieval again, you must delete the previous Job:
```bash
kubectl delete -f job.yaml
kubectl apply -f job.yaml
```

## ⚙️ Akeyless Configuration
Ensure your Akeyless K8s Auth Method trusts:
- **Namespace**: `akeyless-k8s-python-demo`
- **ServiceAccount**: `akeyless-python-sa`

---
**Maintained by**: [leon-maister](https://github.com/leon-maister)

<sub style="color: gray;">/home/keyless/k8s/akeyless-k8s-python-demo | vcluster_my-vcluster_leon_gke_customer-success-391112_us-central1_customer-success-391112-gke-sandbox</sub>
