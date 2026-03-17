# Akeyless Kubernetes Authentication Demo

This project provides a complete example of how to authenticate a Python application within a Kubernetes cluster using an Akeyless Gateway. It specifically addresses common hurdles like **Base64 token encoding** and **Akeyless API v2** requirements.

## 📂 File Descriptions

| File | Function |
| :--- | :--- |
| \`get_akeyless_secret.py\` | Core Python logic that reads the K8s token, encodes it, authenticates with Akeyless, and retrieves a secret. |
| \`serviceaccount.yaml\` | Creates the **ServiceAccount** (Identity) in the cluster used for authentication. |
| \`deployment.yaml\` | Manages the application pod, links it to the ServiceAccount, and pulls the container image. |
| \`dockerfile\` | Containerizes the Python application. |
| \`requirements.txt\` | Defines the \`requests\` library dependency. |

## 🔧 Prerequisites
- **Akeyless Gateway** accessible from the cluster.
- A **K8s Auth Method** configured in your Akeyless console.
- **Docker** and **Kubectl** installed locally.

## 🚀 Quick Start Guide

### 1. Build and Push the Image
\`\`\`bash
# Build the image
docker build -t leon-maister/akeyless-k8s-demo:4.3 .

# Push to your registry
docker push leon-maister/akeyless-k8s-demo:4.3
\`\`\`

### 2. Prepare the Environment
Ensure the namespace exists and create the ServiceAccount:
\`\`\`bash
# Create the ServiceAccount
kubectl apply -f serviceaccount.yaml
\`\`\`

### 3. Deploy the Application
\`\`\`bash
# Deploy the application pod
kubectl apply -f deployment.yaml
\`\`\`

### 4. Verify Results
Watch the logs to confirm the authentication and secret retrieval were successful:
\`\`\`bash
# Follow logs
kubectl logs -f deployment/akeyless-kubernetes-authentication-app -n akeyless-kubernetes-authentication-demo
\`\`\`

## 💡 Troubleshooting
If you see an authentication error:
1. Ensure the \`access-id\` in \`get_akeyless_secret.py\` matches your Akeyless Auth Method.
2. Check if the \`k8s-auth-config-name\` matches the configuration name on your Gateway.
3. Verify that your Akeyless RBAC allows this Auth Method to read the specific secret path.

---
**Maintained by**: [leon-maister](https://github.com/leon-maister)
