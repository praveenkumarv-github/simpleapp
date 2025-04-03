# Password Generator Helm Chart

This Helm chart deploys the Password Generator application on a Kubernetes cluster. It includes the necessary Kubernetes resources such as Deployment, Service, and Ingress.

## Prerequisites

- Kubernetes 1.12+
- Helm 3.x

## Installation

To install the chart, use the following command:

```bash
helm install <release-name> ./password-generator
```

Replace `<release-name>` with your desired name for the release.

## Configuration

The following table lists the configurable parameters of the Password Generator chart and their default values:

| Parameter                | Description                          | Default                     |
|--------------------------|--------------------------------------|-----------------------------|
| `replicaCount`           | Number of replicas                   | `1`                         |
| `image.repository`       | Image repository                     | `praveenkumar081097/password-generator` |
| `image.tag`              | Image tag                           | `latest`                    |
| `service.type`           | Service type                         | `ClusterIP`                 |
| `service.port`           | Service port                         | `80`                        |
| `ingress.enabled`        | Enable ingress                       | `false`                     |
| `ingress.hosts[0].host`  | Host for the ingress                 | `pg.cluster.lab.net`       |
| `ingress.hosts[0].paths` | Path for the ingress                 | `/`                         |

## Usage

1. **Customize the values** in `values.yaml` as needed.
2. **Install the chart** using the Helm command provided above.
3. **Access the application** via the specified ingress host or service.

## Uninstalling the Chart

To uninstall the chart, use the following command:

```bash
helm uninstall <release-name>
```

Replace `<release-name>` with the name of your release.

## License

This project is licensed under the MIT License. See the LICENSE file for details.