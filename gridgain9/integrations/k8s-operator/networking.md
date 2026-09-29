---
description: >-
  Configure the default headless service and custom ClusterIP, NodePort, and
  LoadBalancer services for GridGain 9 clusters managed by the Kubernetes
  Operator.
---

# Services and Networking

{% hint style="warning" %}
Kubernetes operator is an experimental feature. The configuration may change in a subsequent release.
{% endhint %}

The operator automatically creates a headless service for internal cluster communication. Additionally, you can define any number of additional services to expose the cluster to applications inside or outside the Kubernetes cluster.

## Default Headless Service

The operator creates a headless service named `<cluster-name>-headless` for each `GridGain9Cluster`. This service provides stable DNS names for each pod in the StatefulSet, which GridGain nodes use to discover each other. The node finder configuration in `gridgainConfig` typically references this service:

```yaml
spec:
  gridgainConfig:
    content: |
      ignite {
        network {
          nodeFinder {
            netClusterNodes=[
              "my-cluster-headless:27100"
            ]
            type=STATIC
          }
          port=27100
        }
      }
```

You do not need to create this service yourself. The operator creates it automatically.

## Custom Services

You can define additional services under `spec.services`. Each entry requires a `name`, a `type`, and at least one port. The operator creates a Kubernetes Service named `<cluster-name>-<service-name>` for each entry.

The supported service types are `ClusterIP`, `NodePort`, `LoadBalancer`, and `Headless`.

### ClusterIP

A ClusterIP service makes the cluster reachable from within the Kubernetes cluster. This is the default service type and is suitable for applications running alongside GridGain:

```yaml
spec:
  services:
    - name: internal
      type: ClusterIP
      ports:
        - name: rest
          port: 10300
        - name: client
          port: 10800
```

### NodePort

A NodePort service exposes the cluster on a static port on every Kubernetes node. Node ports must be in the range 30000-32767:

```yaml
spec:
  services:
    - name: external
      type: NodePort
      ports:
        - name: rest
          port: 10300
          nodePort: 30300
        - name: client
          port: 10800
          nodePort: 30800
```

### LoadBalancer

A LoadBalancer service provisions a cloud load balancer that routes external traffic to the cluster. This is the recommended approach for production deployments in cloud environments:

```yaml
spec:
  services:
    - name: rest-external
      type: LoadBalancer
      externalTrafficPolicy: Local
      ports:
        - name: rest
          port: 10300
```

Setting `externalTrafficPolicy` to `Local` preserves client source IP addresses but requires that the load balancer only sends traffic to nodes that have a GridGain pod running. The default policy is `Cluster`, which distributes traffic across all nodes at the cost of an extra hop.

## Service Annotations

Cloud providers often use annotations to configure load balancer behavior. Pass them through the `annotations` field on the service definition:

```yaml
spec:
  services:
    - name: rest-external
      type: LoadBalancer
      ports:
        - name: rest
          port: 10300
      annotations:
        service.beta.kubernetes.io/aws-load-balancer-type: "nlb"
        service.beta.kubernetes.io/aws-load-balancer-cross-zone-load-balancing-enabled: "true"
```

## Session Affinity

For services that benefit from sticky sessions, set `sessionAffinity` to `ClientIP`. The default is `None`:

```yaml
spec:
  services:
    - name: management
      type: ClusterIP
      sessionAffinity: ClientIP
      ports:
        - name: rest
          port: 10300
```

## Multiple Services

You can define multiple services on a single cluster to serve different access patterns. For example, an internal ClusterIP for pod-to-pod communication, a LoadBalancer for external REST API access, and a NodePort for client driver connections:

```yaml
spec:
  services:
    - name: internal
      type: ClusterIP
      ports:
        - name: rest
          port: 10300
        - name: client
          port: 10800
    - name: rest-external
      type: LoadBalancer
      ports:
        - name: rest
          port: 10300
    - name: client-external
      type: NodePort
      ports:
        - name: client
          port: 10800
          nodePort: 30800
```

Each service is independent and can have its own type, ports, annotations, and traffic policies.
