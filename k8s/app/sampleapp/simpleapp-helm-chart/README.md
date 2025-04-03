# Simple Application Helm Chart

This Helm chart deploys a simple application with a frontend service, ingress, and deployment configuration.

## Prerequisites

- Kubernetes 1.12+
- Helm 3.x

## Installation

To install the chart with the release name `simpleapp`, run the following command:

```bash
helm install simpleapp ./simpleapp-helm-chart
```

## Configuration

The following table lists the configurable parameters of the simpleapp chart and their default values.

| Parameter                     | Description                                     | Default                  |
|-------------------------------|-------------------------------------------------|--------------------------|
| `replicaCount`                | Number of replicas for the frontend deployment  | `1`                      |
| `image.repository`            | Container image repository                      | `praveenkumar081097/simpleapp` |
| `image.tag`                   | Container image tag                             | `latest`                 |
| `image.pullPolicy`            | Container image pull policy                     | `Always`                 |
| `service.type`                | Service type                                    | `ClusterIP`              |
| `service.port`                | Service port                                    | `80`                     |
| `service.targetPort`          | Target port for the service                     | `80`                     |
| `ingress.enabled`             | Enable ingress resource                         | `true`                   |
| `ingress.className`           | Ingress class name                              | `nginx`                  |
| `ingress.hosts[0].host`       | Hostname for the ingress resource               | `app.cluster.lab.net`    |
| `ingress.hosts[0].paths`      | Path for the ingress resource                   | `/`                      |
| `ingress.annotations`         | Annotations for the ingress resource            | `{}`                     |

## Usage

To customize the deployment, create a `values.yaml` file and override the default values. For example:

```yaml
replicaCount: 2
image:
  repository: "myrepo/simpleapp"
  tag: "1.0.0"
  pullPolicy: IfNotPresent
service:
  type: NodePort
  port: 30000
  targetPort: 8080
ingress:
  enabled: true
  className: nginx
  hosts:
    - host: myapp.example.com
      paths:
        - path: /
          pathType: ImplementationSpecific
```

Then install the chart with your custom values:

```bash
helm install simpleapp ./simpleapp-helm-chart -f values.yaml
```

## Uninstalling the Chart

To uninstall the `simpleapp` release, run:

```bash
helm uninstall simpleapp
```

This removes all the Kubernetes resources associated with the chart.

## Contributing

Feel free to submit issues and pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.