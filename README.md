# K3S Cluster Setup with App

## Cluster architecture

![image](https://github.com/user-attachments/assets/7197c530-7226-4647-9927-eb790f39b9aa)

### Setting Up a Local K3s Cluster: Learn Kubernetes the Hands-On Way

This guide walks you through creating a lightweight Kubernetes (K8s) cluster using **K3s** on your local laptop or workstation. Perfect for development, testing, or learning, this setup allows you to host applications within your internal network without relying on cloud-managed services like EKS, AKS, or GKE.

Building a local cluster from scratch is a cost-effective and insightful way to understand Kubernetes fundamentals while efficiently managing limited resources. By setting up a minimal yet functional cluster, you'll gain valuable experience in managing K8s in a resource-constrained environment.

Whether you’re a beginner or looking to sharpen your skills, this guide is the perfect starting point. Let’s dive in!

### Understanding the Initial Setup for Hosting a Cloud-Managed Style Kubernetes Cluster

To set up a Kubernetes cluster locally for learning or testing, you will need the following:
#### **Host System Requirements**

- **Operating System**: Windows, Linux, or Mac (laptop/workstation)
- **Internet Connection**: Required for downloading dependencies and cluster setup
- **Virtualization Software**: Oracle VirtualBox installed

| **VM Name** | **Role**    | **Description**                           | **Preferred Operating System** | **Networking**  | Private IP Address |
| ----------- | ----------- | ----------------------------------------- | ------------------------------ | --------------- | ------------------ |
| VM1         | Master Node | Acts as the control plane for the cluster | Linux (Centos9)                | Bridged Network | 192.168.29.91      |
| VM2         | Worker Node | Runs application workloads                | Linux (Centos9)                | Bridged Network | 192.168.29.92      |
| VM3         | Worker Node | Runs application workloads                | Linux (Centos9)                | Bridged Network | 192.168.29.93      |
| VM4         | Client      | Internal client for accessing and testing | Linux (Centos9)                | Bridged Network | 192.168.29.94      |

Set all VMs to Bridged Network mode. This ensures that all VMs can communicate within the same local network.

## Cluster Setup

### Install - Docker
```bash
curl https://releases.rancher.com/install-docker/20.10.sh | sh
```

### K3S - Kubernetes Cluster
#### Server:
```bash
curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="--disable traefik --docker --disable=servicelb" sh
token:  /var/lib/rancher/k3s/server/node-token
```

#### Worker:
```bash
curl -sfL https://get.k3s.io | K3S_URL=https://SERVERIP:6443 K3S_TOKEN=XXYXX INSTALL_K3S_EXEC="--docker" sh -
```

#### Common for Server & Worker
```bash
systemctl disable firewalld --now
firewall-cmd --reload
```

#### Post K3s Setup
```bash
kubectl label node workerX.com node-role.kubernetes.io/worker=worker
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
```

### MetalLB - Classic/On-prem Load Balancer
```bash
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.14.9/config/manifests/metallb-native.yaml
kubectl apply -f simpleapp/k8s/ingress-controller/metallb/helm-metallb.yaml
```

### NGINX - Ingress Controller
```bash
kubectl create namespace ingress-nginx
helm install ingress-nginx ingress-nginx/ingress-nginx -n ingress-nginx
helm uninstall -n ingress-nginx ingress-nginx
```

### Prometheus-Stack - Cluster Monitoring
```bash
helm install monitoring prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace
```

## SimpleApp Setup
This is a simple app that can be run locally.

### Setup - Locally
```bash
git config --global user.name praveenkumarv-github
git config --global user.email praveenkumar081097@gmail.com
ssh-keygen -t ed25519 -C "praveenkumar081097@gmail.com"
# For more: Added a new SSH key to your GitHub account - https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection
git remote set-url --push origin 'git@github.com:praveenkumarv-github/simpleapp.git'
```

### Docker Hub Link
```bash
https://hub.docker.com/r/praveenkumar081097/simpleapp
```

### Testing - Locally
To run this app locally, you need to install the httpserver package using pip: For running it locally

```bash
pip install httpserver
python /simpleapp/main.py
```

### Setting Up - Locally Docker

```bash
docker pull praveenkumar081097/simpleapp:latest
docker run -it --rm -d -p 80:80 --name web praveenkumar081097/simpleapp:latest
curl 192.168.29.173:80
curl 192.168.29.173/hit-server-endpoint
```

### Deploying the App
```bash
kubectl apply -f simpleapp/k8s/sampleapp/.
```

## Troubleshooting

### Common Errors and Fixes

1. **Ingress-Nginx Admission Issue**  
   - Error: Webhook "validate.nginx.ingress.kubernetes.io" times out.  
   - **Solution**: Delete the ingress-nginx webhook configuration:  
     ```shell
     kubectl delete -A ValidatingWebhookConfiguration ingress-nginx-admission
     ```

2. **MetalLB Webhook Timeout**  
   - Error: Timeout while calling MetalLB webhooks for IPAddressPool or L2Advertisement validation.  
   - **Solution**: Check if the MetalLB webhook service is running and reachable.

3. **Ingress Validation Timeout**  
   - Error: Ingress creation fails due to validation webhook timeout.  
   - **Solution**: Ensure the ingress-nginx controller is deployed correctly and verify network connectivity.
