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
| `image.repository`            | Container image repository                       | `praveenkumar081097/simpleapp` |
| `image.tag`                   | Container image tag                             | `latest`                 |
| `image.pullPolicy`            | Container image pull policy                     | `Always`                 |
| `service.type`                | Service type                                    | `ClusterIP`              |
| `service.port`                | Service port                                    | `80`                     |
| `ingress.enabled`             | Enable ingress resource                         | `true`                   |
| `ingress.hosts[0].host`      | Hostname for the ingress resource               | `app.cluster.lab.net`    |
| `ingress.hosts[0].paths`      | Path for the ingress resource                   | `/`                      |

## Usage

To customize the deployment, create a `values.yaml` file and override the default values. For example:

```yaml
replicaCount: 2
image:
  tag: "1.0.0"
service:
  type: NodePort
```

Then install the chart with your custom values:

```bash
helm install simpleapp ./simpleapp -f values.yaml
```

## Uninstalling the Chart

To uninstall the `simpleapp` release, run:

```bash
helm uninstall simpleapp
```

## Contributing

Feel free to submit issues and pull requests for improvements or bug fixes.