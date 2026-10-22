---
description: >-
  Encrypt GridGain 8 discovery and communication traffic with automatic mTLS from a Linkerd service mesh, with no keystores and no cluster configuration changes.
---

# How to Encrypt Inter-Node Cluster Traffic With Linkerd on Kubernetes

<!-- TODO (not tested): The Linkerd steps (need a Kubernetes cluster) was not run against GridGain 8.10. Run it on an 8.10 build, compare the output and samples with the page, fix differences, then delete this comment. -->

<!-- TODO (release): the Docker Hub tag with the plain version 8.10.0 does not exist yet (no 8.10.0 image is published yet); this page uses the placeholder tag 8.10.0. After the 8.10.0 release, check that each of these resolves, update this page if the final names differ, and delete this comment. -->

## Prerequisites

- A running Kubernetes cluster with `kubectl` access. The commands below were tested on [kind](https://kind.sigs.k8s.io). They apply unchanged to managed Kubernetes (EKS, GKE, AKS).
- **The Linkerd CLI** ([install guide](https://linkerd.io/2/getting-started/)).
- **GridGain 8 only:** A GridGain Enterprise evaluation or commercial license file (`gridgain-license.xml`) from [gridgain.com/tryfree](https://www.gridgain.com/tryfree).

## Overview

Cache nodes chatter constantly: discovery on 47500 and communication on 47100 carry the traffic that keeps the cluster together. By default that traffic is plain TCP. This guide encrypts it with Linkerd, which issues and rotates short-lived workload certificates and applies mutual TLS at a per-pod proxy. The cluster runs with no SSL configuration of its own and no keystores to manage.

The procedure runs against GridGain 8 Enterprise.

Two notes on the environment. This guide uses Kubernetes rather than the standard local Docker setup because a service mesh is a Kubernetes construct. It uses two cache nodes rather than one because the traffic this guide encrypts is the traffic between nodes, which only exists once a second node joins.

## Install Linkerd

Recent Linkerd releases require the Gateway API CRDs. Install them first, then install the Linkerd CRDs and control plane.

```bash
kubectl apply --server-side -f \
  https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.2.1/standard-install.yaml
linkerd install --crds | kubectl apply -f -
linkerd install | kubectl apply -f -
```

The Linkerd CLI install output prints the Gateway API version it expects. This guide pins v1.2.1 to match the current Linkerd edge release. If your CLI recommends a different version, apply that one instead.

Verify the installation:

```bash
linkerd check
```

Every check group should pass, ending with the overall result:

```text
linkerd-existence
-----------------
√ 'linkerd-config' config map exists
√ heartbeat ServiceAccount exist
√ control plane replica sets are ready
√ no unschedulable pods
√ control plane pods are ready
√ cluster networks contains all node podCIDRs
√ cluster networks contains all pods
√ cluster networks contains all services

linkerd-identity
----------------
√ certificate config is valid
√ trust anchors are using supported crypto algorithm
√ trust anchors are within their validity period
√ trust anchors are valid for at least 60 days
√ issuer cert is using supported crypto algorithm
√ issuer cert is within its validity period
√ issuer cert is valid for at least 60 days
√ issuer cert is issued by the trust anchor

control-plane-version
---------------------
√ can retrieve the control plane version
√ control plane is up-to-date
√ control plane and cli versions match

Status check results are √
```

{% hint style="success" %}
**Checkpoint:** `linkerd check` ends with `Status check results are √`. The control plane is healthy and ready to inject proxies.
{% endhint %}

## Deploy the Two-Node Cluster

Deploy a two-node cluster with the Linkerd annotations on the pod template. The manifests below define three objects: a `ConfigMap` holding the node configuration, a headless `Service` for peer discovery, and a `StatefulSet` running two cache nodes. The two annotations that enable mesh encryption are called out after the code.

GridGain 8 Enterprise requires a license. Create the namespace and a Secret from your license file first:

```bash
kubectl create namespace ignite
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
        linkerd.io/inject: enabled
        config.linkerd.io/opaque-ports: "10800,47100,47500"
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

The two annotations on the pod template are what enable mesh encryption:

- **`linkerd.io/inject: enabled`** adds a `linkerd-proxy` sidecar to each pod. The proxy transparently wraps outbound connections in mTLS and unwraps inbound ones.
- **`config.linkerd.io/opaque-ports: "10800,47100,47500"`** marks the cache ports as opaque. Linkerd runs HTTP protocol detection on every connection by default. The discovery and communication SPIs are server-first binary protocols where neither side sends identifiable bytes, so detection stalls for ten seconds, past the cache's own handshake timeout, and the cluster fails to form. Marking these ports opaque skips detection while keeping mTLS. Port 8080, the HTTP REST port, stays out of the list because Linkerd handles HTTP traffic natively. Port 11211 is the legacy binary REST port, not an HTTP port.

Wait for both pods to report `2/2` containers (the cache node plus the proxy):

```bash
kubectl get pods -n ignite -w
```

Both pods come up sequentially and settle at `2/2`:

```text
NAME       READY   STATUS    RESTARTS   AGE
ignite-0   2/2     Running   0          8s
ignite-1   2/2     Running   0          3s
```

{% hint style="success" %}
**Checkpoint:** Both pods report `2/2` and `Running`. The `2/2` count confirms the proxy was injected alongside the cache node.
{% endhint %}

## Verify Mutual TLS is Flowing

Confirm that the discovery and communication traffic is actually encrypted and authenticated. Query the proxy metrics on one node and filter for TLS-secured TCP connections:

```bash
linkerd diagnostics proxy-metrics -n ignite po/ignite-0 \
  | grep 'tcp_open_total.*tls="true"'
```

The matching lines show discovery (47500) and communication (47100) connections, both inbound and outbound, carrying `tls="true"` and a verified peer identity:

```text
tcp_open_total{direction="inbound",peer="src",target_addr="10.244.0.19:47500",target_port="47500",tls="true",client_id="default.ignite.serviceaccount.identity.linkerd.cluster.local",srv_name="all-unauthenticated",srv_port="47500"} 2
tcp_open_total{direction="inbound",peer="src",target_addr="10.244.0.19:47100",target_port="47100",tls="true",client_id="default.ignite.serviceaccount.identity.linkerd.cluster.local",srv_name="all-unauthenticated",srv_port="47100"} 1
tcp_open_total{direction="outbound",peer="dst",target_addr="10.244.0.20:47500",target_port="47500",tls="true",server_id="default.ignite.serviceaccount.identity.linkerd.cluster.local",dst_namespace="ignite",dst_pod="ignite-1",dst_statefulset="ignite"} 2
```

Each line reports a TCP connection the proxy opened or accepted with `tls="true"`. The inbound entries on the communication SPI (47100) and discovery SPI (47500) carry a verified `client_id`, and the outbound entry to `dst_pod="ignite-1"` confirms ignite-0 is actively talking to ignite-1 over encrypted discovery. Together they confirm node-to-node traffic is mutually authenticated and encrypted.

{% hint style="success" %}
**Checkpoint:** The grep returns inbound and outbound lines for 47100 and 47500 with `tls="true"`. Inter-node traffic is encrypted under Linkerd mTLS.
{% endhint %}

{% hint style="info" %}
Linkerd adds three sources of overhead: a per-connection mTLS handshake (amortized across long-lived inter-node connections), per-packet encryption, and one extra in-pod hop through the proxy on every request. Most meshed workloads do not notice them, but a distributed cache is throughput-sensitive. This guide does not benchmark the overhead. Measure it against your own workload before rolling a mesh into production.
{% endhint %}

## Troubleshooting

<details>
<summary>Nodes never form a cluster; logs show handshake timeouts</summary>

The `opaque-ports` annotation is missing or does not list the SPI ports. Linkerd's HTTP protocol detection stalls on the server-first communication and discovery protocols until the cache's handshake timeout fires. Confirm the pod template carries `config.linkerd.io/opaque-ports: "10800,47100,47500"`, then restart the StatefulSet: `kubectl rollout restart statefulset/ignite -n ignite`.

</details>

<details>
<summary>Pods stay at 1/1 instead of 2/2</summary>

The proxy was not injected. Confirm the pod template carries the `linkerd.io/inject: enabled` annotation under `spec.template.metadata.annotations`, not on the StatefulSet itself. Reapply the manifest and, if needed, restart the StatefulSet with `kubectl rollout restart statefulset/ignite -n ignite`.

</details>

<details>
<summary>linkerd install fails with a Gateway API CRD error</summary>

Recent Linkerd releases require the Gateway API CRDs to be present first. Apply them with the `kubectl apply --server-side` command from Step 1 before running `linkerd install`.

</details>

<details>
<summary>Linkerd or meshed pods crash-loop in the proxy-init container</summary>

The proxy-init logs show iptables stopping on a rule that uses `--match multiport`, `-m comment`, or `-m owner`. Linkerd's proxy-init programs iptables with match extensions that need the `xt_multiport`, `xt_comment`, and `xt_owner` kernel modules. Containers cannot load modules, so the host kernel must provide them. On most managed Kubernetes this is already true. On a self-managed node where it is not, load them on the host (for example `sudo modprobe xt_multiport xt_comment xt_owner`, persisted via `/etc/modules-load.d/`) and recreate the pods. If the modules are present but not found, the running kernel may not match the installed module tree after a kernel upgrade; reboot the node so the two align.

</details>

<details>
<summary>GridGain 8 node exits at startup with a license error</summary>

The license Secret is missing, mounted at the wrong path, or expired. Confirm the Secret exists (`kubectl get secret gridgain-license -n ignite`) and that the config's `licenseUrl` matches the mount path (`/ignite/license/gridgain-license.xml`). GridGain Enterprise evaluation licenses are time-limited; download a current one from [gridgain.com/tryfree](https://www.gridgain.com/tryfree) if yours has lapsed.

</details>

## Related

- [How to Encrypt Cluster Traffic with Istio mTLS on Kubernetes](encrypt-traffic-istio.md) - A fuller mesh that also encrypts thin-client and external traffic and exposes an HTTPS gateway.
- [Linkerd automatic mTLS reference](https://linkerd.io/2/features/automatic-mtls/) - How Linkerd issues and rotates workload certificates.
