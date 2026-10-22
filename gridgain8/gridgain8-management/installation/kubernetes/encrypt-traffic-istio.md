---
description: >-
  Enforce mutual TLS across GridGain 8 cluster, thin-client, and external traffic with an Istio service mesh, without changing the cluster's own configuration.
---

# How to Encrypt Cluster Traffic With Istio mTLS on Kubernetes

<!-- TODO (not tested): The Istio steps (need a Kubernetes cluster) was not run against GridGain 8.10. Run it on an 8.10 build, compare the output and samples with the page, fix differences, then delete this comment. -->

<!-- TODO (release): the Docker Hub tag with the plain version 8.10.0 does not exist yet (only 8.10.0-b1 and 8.10.0-b2, in the form 8.10.0-b2-openjdk17, are published); this page uses the placeholder tag 8.10.0. After the 8.10.0 release, check that each of these resolves, update this page if the final names differ, and delete this comment. -->

## Prerequisites

- A running Kubernetes cluster with `kubectl` access. The commands below were tested on [kind](https://kind.sigs.k8s.io). They apply unchanged to managed Kubernetes (EKS, GKE, AKS); only the external load balancer in the optional gateway step differs by platform.
- **istioctl** 1.20 or later ([install guide](https://istio.io/latest/docs/setup/getting-started/#download)).
- **GridGain 8 only:** A GridGain Enterprise evaluation or commercial license file (`gridgain-license.xml`) from [gridgain.com/tryfree](https://www.gridgain.com/tryfree).

## Overview

This guide encrypts every transport into and across a two-node cache cluster using an Istio service mesh: discovery and communication between nodes, thin-client connections, and external HTTP traffic. Istio wraps each connection in mutual TLS at the sidecar, so the cluster runs with no SSL configuration of its own and no keystores to manage.

The procedure runs against GridGain 8 Enterprise.

Two notes on the environment. This guide uses Kubernetes rather than the standard local Docker setup because a service mesh is a Kubernetes construct. It uses two cache nodes rather than one because the value of the mesh is encrypting the traffic between nodes, which only exists once a second node joins.

## Install Istio

Install Istio with the default profile, which includes the ingress gateway used in the optional external-access step later.

```bash
istioctl install -y
```

Confirm the control plane is running:

```bash
kubectl get pods -n istio-system
```

Expected output:

```text
NAME                                    READY   STATUS    RESTARTS   AGE
istio-ingressgateway-5dcc6ff9cb-nspc9   1/1     Running   0          12m
istiod-54b5f6856c-fzkx6                 1/1     Running   0          12m
```

{% hint style="success" %}
**Checkpoint:** The `istiod` pod reports `Running` and `1/1`. The control plane is ready to inject sidecars.
{% endhint %}

## Create the Namespace With Sidecar Injection

Istio injects an Envoy sidecar into every pod in a labeled namespace. Create the namespace and apply the label before deploying the cluster, so the cache pods start with their proxies already in place.

```bash
kubectl create namespace ignite
kubectl label namespace ignite istio-injection=enabled
```

Verify the label:

```bash
kubectl get namespace ignite --show-labels
```

Expected output:

```text
NAME     STATUS   AGE   LABELS
ignite   Active   0s    istio-injection=enabled,kubernetes.io/metadata.name=ignite
```

{% hint style="success" %}
**Checkpoint:** The namespace labels include `istio-injection=enabled`. Pods created in this namespace will receive a sidecar.
{% endhint %}

## Deploy the Two-Node Cluster

Deploy a two-node cluster configured for Istio. The manifests below define three objects: a `ConfigMap` holding the node configuration, a headless `Service` for peer discovery, and a `StatefulSet` running two cache nodes. Two details in these manifests are what make Istio work with a stateful cache cluster, and both are called out after the code.

GridGain 8 Enterprise requires a license. Create a Secret from your license file first:

```bash
kubectl create secret generic gridgain-license \
  --namespace ignite \
  --from-file=gridgain-license.xml=./gridgain-license.xml
```

Save the following as `ignite-cluster.yaml`. The node configuration adds the GridGain plugin pointing at the mounted license:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: ignite-config
  namespace: ignite
data:
  ignite-config.xml: |
    <?xml version="1.0" encoding="UTF-8"?>
    <beans xmlns="http://www.springframework.org/schema/beans"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="
           http://www.springframework.org/schema/beans
           http://www.springframework.org/schema/beans/spring-beans.xsd">
      <bean id="ignite.cfg" class="org.apache.ignite.configuration.IgniteConfiguration">
        <property name="workDirectory" value="/ignite/work"/>
        <property name="cacheConfiguration">
          <list>
            <bean class="org.apache.ignite.configuration.CacheConfiguration">
              <property name="name" value="PERSON"/>
              <property name="cacheMode" value="PARTITIONED"/>
              <property name="backups" value="1"/>
            </bean>
          </list>
        </property>
        <property name="pluginConfigurations">
          <list>
            <bean class="org.gridgain.grid.configuration.GridGainConfiguration">
              <property name="rollingUpdatesEnabled" value="true"/>
              <property name="licenseUrl" value="/ignite/license/gridgain-license.xml"/>
            </bean>
          </list>
        </property>
        <property name="discoverySpi">
          <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <property name="ipFinder">
              <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                <property name="addresses">
                  <list>
                    <value>ignite-headless.ignite.svc.cluster.local</value>
                  </list>
                </property>
              </bean>
            </property>
          </bean>
        </property>
      </bean>
    </beans>
---
apiVersion: v1
kind: Service
metadata:
  name: ignite-headless
  namespace: ignite
spec:
  clusterIP: None
  publishNotReadyAddresses: true
  ports:
    - port: 10800
      name: tcp-thinclient
    - port: 47100
      name: tcp-communication
    - port: 47500
      name: tcp-discovery
  selector:
    app: ignite
    type: server
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: ignite
  namespace: ignite
spec:
  replicas: 2
  serviceName: ignite-headless
  selector:
    matchLabels:
      app: ignite
      type: server
  template:
    metadata:
      labels:
        app: ignite
        type: server
      annotations:
        proxy.istio.io/config: |
          holdApplicationUntilProxyStarts: true
    spec:
      terminationGracePeriodSeconds: 60
      volumes:
        - name: ignite-config
          configMap:
            name: ignite-config
        - name: ignite-license
          secret:
            secretName: gridgain-license
        - name: ignite-work
          emptyDir: {}
      containers:
        - name: ignite-node
          image: gridgain/enterprise:8.10.0-openjdk17-slim
          resources:
            limits:
              memory: 1536Mi
              cpu: 1
          env:
            - name: IGNITE_QUIET
              value: "false"
            - name: OPTION_LIBS
              value: ignite-rest-http
            - name: CONFIG_URI
              value: file:///ignite/config/ignite-config.xml
            - name: JVM_OPTS
              value: -Djava.net.preferIPv4Stack=true
          ports:
            - containerPort: 10800
            - containerPort: 11211
            - containerPort: 47100
            - containerPort: 47500
            - containerPort: 8080
          volumeMounts:
            - mountPath: /ignite/config
              name: ignite-config
            - mountPath: /ignite/license
              name: ignite-license
            - mountPath: /ignite/work
              name: ignite-work
```

Apply the manifests:

```bash
kubectl apply -f ignite-cluster.yaml
```

Two lines in these manifests are specific to running under Istio:

- **`name: tcp-communication` (and the other `tcp-` port names) on the headless Service.** Istio creates an outbound listener only for declared, named ports. Cache nodes discover each other by connecting directly to pod IPs through the headless Service, so without these named ports Istio has no listener for that traffic, it falls through to the PassthroughCluster as plaintext, and STRICT mTLS rejects it. The `tcp-` prefix tells Istio to treat the port as opaque TCP rather than attempting HTTP parsing.
- **`holdApplicationUntilProxyStarts: true` in the pod annotation.** This delays the cache node until the Envoy proxy and its iptables rules are ready. Without it the JVM starts first, the first inter-node handshake fires before the proxy can route it, and the cluster stalls on partition-map-exchange warnings.

Wait for both pods to report `2/2` containers (the cache node plus the sidecar):

```bash
kubectl get pods -n ignite -w
```

Both pods come up sequentially and settle at `2/2`:

```text
NAME       READY   STATUS    RESTARTS   AGE   IP            NODE
ignite-0   2/2     Running   0          5s    10.244.0.15   mesh-control-plane
ignite-1   2/2     Running   0          2s    10.244.0.16   mesh-control-plane
```

{% hint style="success" %}
**Checkpoint:** Both pods report `2/2` and `Running`. The `2/2` count confirms the sidecar was injected alongside the cache node.
{% endhint %}

## Enforce STRICT Mutual TLS

Sidecar injection alone permits mTLS but does not require it; nodes can still accept plaintext. A `PeerAuthentication` policy in STRICT mode closes that gap by rejecting any non-mTLS connection in the namespace.

Save the following as `peer-authentication.yaml`:

```yaml
apiVersion: security.istio.io/v1
kind: PeerAuthentication
metadata:
  name: default
  namespace: ignite
spec:
  mtls:
    mode: STRICT
```

Apply it:

```bash
kubectl apply -f peer-authentication.yaml
```

Scoping the policy to the `ignite` namespace keeps the rule contained. From this point, every connection between pods in the namespace must present a valid mesh-issued certificate.

{% hint style="success" %}
**Checkpoint:** `kubectl get peerauthentication -n ignite` lists the `default` policy. The cluster pods remain `Running` and `2/2`, confirming inter-node traffic still flows under STRICT enforcement.
{% endhint %}

## Expose the External Client Over HTTPS (Optional)

Skip this step if you only need encryption inside the cluster. Complete it to terminate HTTPS for an external application, such as the Spring Boot thin client in the [reference repository](https://github.com/sdarlington/ignite-minikube). The gateway terminates TLS at the mesh edge and re-wraps the in-cluster hop as mTLS, so the application needs no changes.

Generate a self-signed certificate and load it as a TLS secret in the gateway's namespace:

```bash
openssl req -x509 -newkey rsa:2048 -nodes -days 365 \
  -keyout key.pem -out cert.pem -subj "/CN=ignite-client"
kubectl create -n istio-system secret tls ignite-client-tls \
  --cert=cert.pem --key=key.pem
```

Save the following as `ignite-client-gateway.yaml`. It expects a `Service` named `ignite-client` on port 80 in the `ignite` namespace (deployed with the application):

```yaml
apiVersion: networking.istio.io/v1
kind: Gateway
metadata:
  name: ignite-client-gateway
  namespace: ignite
spec:
  selector:
    istio: ingressgateway
  servers:
    - port:
        number: 443
        name: https
        protocol: HTTPS
      tls:
        mode: SIMPLE
        credentialName: ignite-client-tls
      hosts:
        - "*"
---
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: ignite-client
  namespace: ignite
spec:
  hosts:
    - "*"
  gateways:
    - ignite-client-gateway
  http:
    - route:
        - destination:
            host: ignite-client.ignite.svc.cluster.local
            port:
              number: 80
```

Apply it:

```bash
kubectl apply -f ignite-client-gateway.yaml
```

Forward the ingress gateway's HTTPS port and call the application:

```bash
kubectl -n istio-system port-forward svc/istio-ingressgateway 8443:443
```

In a second terminal:

```bash
curl -ki https://localhost:8443/person/
```

Expected output (the response shape depends on your application; the headers are what matter):

```text
HTTP/1.1 200 OK
content-type: application/json
server: istio-envoy
x-envoy-upstream-service-time: 124

{"count":1}
```

{% hint style="success" %}
**Checkpoint:** The HTTPS request returns `200` with the `server: istio-envoy` header. Traffic reached the application over TLS terminated at the gateway. The self-signed certificate is why `-k` is required.
{% endhint %}

{% hint style="info" %}
This optional step requires the Spring Boot client deployed in the namespace. The inter-node and thin-client encryption verified in the rest of this guide does not depend on it.
{% endhint %}

## Verify Mutual TLS is Enforced

Confirm that inter-node traffic is actually mutually authenticated, not merely permitted. Each sidecar exposes Envoy statistics on port 15000. Query the cache node's sidecar for connections labeled with the mutual-TLS security policy:

```bash
kubectl exec ignite-0 -n ignite -c istio-proxy -- \
  curl -s localhost:15000/stats/prometheus \
  | grep 'connection_security_policy="mutual_tls"'
```

Expected output:

```text
istio_tcp_connections_opened_total{reporter="destination",source_workload="ignite",source_workload_namespace="ignite",source_principal="spiffe://cluster.local/ns/ignite/sa/default",destination_workload="ignite",destination_workload_namespace="ignite",destination_principal="spiffe://cluster.local/ns/ignite/sa/default",destination_service="ignite-headless.ignite.svc.cluster.local",request_protocol="tcp",connection_security_policy="mutual_tls"} 3
```

The same `connection_security_policy="mutual_tls"` label also appears on the `istio_tcp_connections_closed_total`, `istio_tcp_received_bytes_total`, and `istio_tcp_sent_bytes_total` metrics. The presence of `istio_tcp_connections_opened_total` entries with `connection_security_policy="mutual_tls"` is the proof: the sidecar opened TCP connections for the cache ports and secured them with mutual TLS. A non-zero counter on the discovery and communication ports means node-to-node traffic is encrypted and authenticated.

{% hint style="success" %}
**Checkpoint:** The grep returns one or more lines with `connection_security_policy="mutual_tls"` and a non-zero count. Inter-node traffic is encrypted under STRICT mTLS.
{% endhint %}

{% hint style="info" %}
Istio adds a userspace hop on every connection and a small first-connection latency cost from configuration push. For long-lived inter-node traffic the per-byte overhead is modest; for very chatty short-lived calls it is more noticeable. The sidecar also adds memory and CPU per pod. This guide does not benchmark the overhead. Measure it against your own workload before rolling a mesh into production.
{% endhint %}

## Troubleshooting

<details>
<summary>Cluster stalls on "Still waiting for initial partition map exchange"</summary>

The cache node started before its sidecar was ready, so the first inter-node handshake had no route. Confirm the `holdApplicationUntilProxyStarts: true` annotation is present on the pod template, then delete the pods so they restart with correct ordering: `kubectl delete pod ignite-0 ignite-1 -n ignite`.

</details>

<details>
<summary>Nodes never form a cluster after applying STRICT mTLS</summary>

Discovery or communication traffic is falling through to the PassthroughCluster as plaintext and being rejected. Verify the headless Service declares the cache ports with named, `tcp-` prefixed entries (`tcp-discovery`, `tcp-communication`, `tcp-thinclient`). Headless Services work without named ports for normal Kubernetes routing, but Istio needs them to create the outbound TCP listener.

</details>

<details>
<summary>Pods stay at 1/1 instead of 2/2</summary>

The sidecar was not injected. Confirm the namespace carries the `istio-injection=enabled` label with `kubectl get namespace ignite --show-labels`. If you labeled the namespace after deploying, restart the StatefulSet so the pods are recreated with sidecars: `kubectl rollout restart statefulset/ignite -n ignite`.

</details>

<details>
<summary>GridGain 8 node exits at startup with a license error</summary>

The license Secret is missing, mounted at the wrong path, or expired. Confirm the Secret exists (`kubectl get secret gridgain-license -n ignite`) and that the config's `licenseUrl` matches the mount path (`/ignite/license/gridgain-license.xml`). GridGain Enterprise evaluation licenses are time-limited; download a current one from [gridgain.com/tryfree](https://www.gridgain.com/tryfree) if yours has lapsed.

</details>

<details>
<summary>istio-ingressgateway port-forward returns connection refused</summary>

The ingress gateway is not running. The default Istio profile installs it; the minimal and demo-minimal profiles do not. Confirm with `kubectl get pods -n istio-system` and reinstall with `istioctl install -y` if the gateway pod is absent.

</details>

## Related

- [How to Encrypt Inter-Node Cluster Traffic with Linkerd on Kubernetes](encrypt-traffic-linkerd.md) - The same goal with a lighter-weight mesh, focused on inter-node traffic.
- [Istio PeerAuthentication reference](https://istio.io/latest/docs/reference/config/security/peer_authentication/) - All mTLS modes and scoping options.
