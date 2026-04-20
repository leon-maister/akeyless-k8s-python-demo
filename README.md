# Akeyless Kubernetes Authentication & Secret Retrieval (Python)

### 🎯 Project Goal
**The goal of this project is to demonstrate how the Akeyless Kubernetes Authentication method works using a Python application (both with Requests and official SDK).**

## 📂 File Descriptions
| File | Function |
| :--- | :--- |
| get_akeyless_secret_SDK.py | **Recommended**: Logic using official Akeyless Python SDK. |
| get_akeyless_secret.py | Legacy logic using raw HTTP requests. |
| serviceaccount.yaml | Identity for the Pod (ServiceAccount). |
| job.yaml | Kubernetes Job manifest for execution. |

## 👩‍💻 Build and Push (SDK Version)
```bash
docker build -t leonmaister/akeyless-k8s-python-demo:2.0-sdk .
docker push leonmaister/akeyless-k8s-python-demo:2.0-sdk
```

## 🚀 Quick Start
1. Apply ServiceAccount:
```bash
kubectl apply -f serviceaccount.yaml
```
2. Run Job:
```bash
# Update image tag to 2.0-sdk in job.yaml before applying
kubectl apply -f job.yaml
```

---
**Maintained by**: [leon-maister](https://github.com/leon-maister)
