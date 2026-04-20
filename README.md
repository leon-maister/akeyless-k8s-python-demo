# Akeyless Kubernetes Authentication & Secret Retrieval (Python SDK)

### 🎯 Project Goal
**The goal of this project is to demonstrate how the **keyless** Akeyless Kubernetes Authentication method works using the official Python SDK. It covers everything from namespace creation to detailed Identity Sub-Claims verification.**

### 🧩 Process Decomposition

#### Phase 1: Deployment & Infrastructure
1. **Namespace & Identity**: A dedicated namespace and ServiceAccount are created to provide a secure boundary.
2. **Image Pull**: Kubernetes pulls the Python-based Docker image (SDK v2.4+) from the registry.
3. **Pod Initialization**: A Kubernetes Job orchestrates the Pod, mounting the ServiceAccount token automatically.
4. **Security Context**: Kyverno or native K8s policies ensure the Pod meets resource limits and security standards.

#### Phase 2: Application Logic (SDK Flow)
1. **Token Retrieval**: The script reads the JWT token from `/var/run/secrets/kubernetes.io/serviceaccount/token`.
2. **SDK Handshake**: The app uses `akeyless.V2Api` and Base64-encoded K8s token for authentication.
3. **Identity Verification**: The script calls `describe_sub_claims()` to inspect the JWT claims validated by the Gateway.
4. **Secret Access**: Upon successful auth, the SDK fetches the secret value directly into the app memory.

## 🛠️ Prerequisites
Before starting this demo, you must have a functional **Akeyless Kubernetes Auth Method** configured.
- **K8s Auth Setup Tool**: [Kubernetes-Authentication](https://github.com/leon-maister/Kubernetes-Authentication)

## 📂 File Descriptions
| File | Function |
| :--- | :--- |
| get_akeyless_secret_SDK.py | Logic using Akeyless Python SDK v2.3+. |
| serviceaccount.yaml | Identity for the Pod (ServiceAccount). |
| job.yaml | Kubernetes Job manifest with resource limits. |
| dockerfile | Builds the container (Recommended: use -u flag for unbuffered logs). |

## 👩‍💻 For Developer
### Build and Push the Image
```bash
docker build -t leonmaister/akeyless-k8s-python-demo:2.4-sdk .
docker push leonmaister/akeyless-k8s-python-demo:2.4-sdk
```

## 🚀 Quick Start Guide

### 1. Environment Setup
```bash
# Create namespace
kubectl create namespace akeyless-k8s-python-demo --dry-run=client -o yaml | kubectl apply -f -

# Apply ServiceAccount
kubectl apply -f serviceaccount.yaml
```

### 2. Run Job and Verify (The Professional Way)
```bash
# Launch the application as a Job
kubectl apply -f job.yaml

# IMPORTANT: Use this command to see full logs including headers and Sub-Claims
kubectl logs $(kubectl get pods -n akeyless-k8s-python-demo -l job-name=akeyless-retrieval-job --sort-by=.metadata.creationTimestamp -o jsonpath='{.items[-1].metadata.name}') -n akeyless-k8s-python-demo
```

### 🔄 Rerunning the Job
To run the secret retrieval again, you must delete the previous Job:
```bash
kubectl delete job akeyless-retrieval-job -n akeyless-k8s-python-demo
kubectl apply -f job.yaml
```

## ⚙️ Akeyless Configuration
Ensure your Akeyless K8s Auth Method trusts:
- **Namespace**: `akeyless-k8s-python-demo`
- **ServiceAccount**: `akeyless-python-sa`

---
**Maintained by**: [leon-maister](https://github.com/leon-maister)

<sub style="color: gray;">/home/keyless/k8s/akeyless-k8s-python-demo | vcluster_my-vcluster_leon_gke_customer-success-391112_us-central1_customer-success-391112-gke-sandbox</sub>
