# K3S Cluster Setup with App

## Cluster Setup

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
