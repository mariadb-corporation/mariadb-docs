---
description: >-
  Deploy a GridGain 9 cluster on Kubernetes with ConfigMaps, a StatefulSet, and
  an initialization job, and configure logging, probes, and autoscaling.
---

# Installing on Kubernetes

You can install GridGain 9 and run a GridGain cluster on Kubernetes cluster. This section describes all the necessary steps, as well as provides the configurations and manifests that you can copy and paste into your environment.

{% hint style="info" %}
Using [Helm chart](installing-with-helm.md) is recommended, however, if you choose not to use Helm, this guide will walk you through installing GridGain on Kubernetes.
{% endhint %}

## Prerequisites

### Recommended Kubernetes Version

GridGain is tested on Kubernetes version 1.26.

## Version Lifecycle

The information about versioning and lifecycle of GridGain 9 is available on the [Versioning page](https://www.gridgain.com/versioning-and-support-lifecycle).

## Installation Steps

### Create ConfigMaps

1. Create the GridGain configuration file and get a [license](https://www.gridgain.com/tryfree). The minimum node configuration is as follows:

   {% code title="gridgain-config.conf" %}
   ```javascript
   ignite: {
     network: {
       # GridGain 9 node port
       port = 3344
       nodeFinder = {
         netClusterNodes = [
           # Kubernetes service to access the GridGain 9 cluster on the Kubernetes network
           "gridgain-svc-headless:3344"
         ]
       }
     }

     storage: {
       profiles = [
         {
           engine = "aipersist"
           name = "default"
           replacementMode = "CLOCK"
           # Explicit storage size configuration
           sizeBytes = 2147483648
         }
       ]
     }
   }
   ```
   {% endcode %}
2. Place your license content in the `license.conf` file.
3. Create the ConfigMap object for GridGain configuration:

   ```bash
   kubectl create configmap gridgain-config -n <namespace> --from-file=gridgain-config.conf
   ```
4. Create the ConfigMap object for the GridGain license:

   ```bash
   kubectl create configmap gridgain-license -n <namespace> --from-file=license.conf
   ```

Replace `<namespace>` with the name of the namespace where you want to deploy GridGain.

{% hint style="info" %}
In Kubernetes deployments, the `gridgain-config.conf` file is mounted as a read-only ConfigMap, so any attempt to update it with the `node config update` command will fail.
{% endhint %}

To update GridGain node configuration, modify the existing ConfigMap and restart all GridGain pods.

- Modify previously configured ConfigMap object:

  ```bash
  kubectl edit configmap gridgain-config -n <namespace>
  ```
- Restart GridGain pod, repeat for every pod:

  ```bash
  kubectl delete pod <GridGain pode name> -n <namespace>
  ```

### Configure Environment Variables and Logging

In Kubernetes deployments all environment variables must be defined directly in the container specification, either in the `StatefulSet` manifests or in the Helm chart [configuration](installing-with-helm.md).

#### JVM and Memory Configuration

To configure JVM options (such as heap size, Metaspace, and Java agent), define the `GRIDGAIN9_EXTRA_JVM_ARGS` environment variable in your manifests.

{% hint style="info" %}
If `-XX:MaxDirectMemorySize=<size>` is not set, it can grow as high as configured max heap.
{% endhint %}

For example, in a `StatefulSet`:

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: gridgain-cluster
  namespace: <namespace>
spec:
  ...
  template:
    spec:
      terminationGracePeriodSeconds: 60000
      containers:
        - name: gridgain-node
          env:
            # Must be specified to ensure that GridGain 9 cluster replicas are visible to each other.
            - name: GRIDGAIN9_EXTRA_JVM_ARGS
              value: "-javaagent:/agent/jmx.jar=9404:/opt/jmx/jmx.yaml -Xms1g -Xmx3g -XX:MaxMetaspaceSize=256m -XX:MaxDirectMemorySize=4g"
```

When using the [Helm chart](installing-with-helm.md), define the same variable through the `extraEnvVars` field:

```yaml
extraEnvVars:
  - name: GRIDGAIN9_EXTRA_JVM_ARGS
    value: "-javaagent:/agent/jmx.jar=9404:/opt/jmx/jmx.yaml -Xms1g -Xmx3g -XX:MaxMetaspaceSize=256m -XX:MaxDirectMemorySize=4g"
```

{% hint style="info" %}
Make sure that the combined memory usage including heap, direct buffers, metaspace, native overhead and storage, remains within the pod's memory limit specified in the `StatefulSet`.
{% endhint %}

To generate JVM diagnostic files inside Kubernetes/Docker, pass the relevant JVM options through `GRIDGAIN9_EXTRA_JVM_ARGS`:

```yaml
env:
  - name: GRIDGAIN9_EXTRA_JVM_ARGS
    value: "-XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/opt/gridgain/work/diagnostics -XX:ErrorFile=/opt/gridgain/work/diagnostics/hs_err_pid%p.log -Xlog:gc*:file=/opt/gridgain/work/log/gc.log:time,level,tags"
```

Ensure that the output directories exist and are writable inside the pod. Declare persistent volumes for diagnostic outputs and mount them into the container:

```yaml
volumeMounts:
  - name: diagnostics
    mountPath: /opt/gridgain/work/diagnostics
  - name: logs
    mountPath: /opt/gridgain/work/log

volumes:
  - name: diagnostics
    persistentVolumeClaim:
      claimName: gg9-diagnostics-pvc
  - name: logs
    persistentVolumeClaim:
      claimName: gg9-logs-pvc
```

#### Logging Configuration

By default, the Docker image ships with a `gridgain.java.util.logging.properties` configuration that enables only console logging.

To modify the default logging behavior (e.g., enabling file-based logging or using `log4j2`), create a ConfigMap with a custom `gridgain.java.util.logging.properties` file and mount it into each pod.

- Create the ConfigMap:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: gg9-gridgain9-logging
  namespace: "yournamespace"
data:
  gridgain.java.util.logging.properties: |-
    handlers=java.util.logging.FileHandler
    java.util.logging.SimpleFormatter.format = [%1$tF %1$tT] [%4$s] %5$s%6$s%n
    java.util.logging.FileHandler.pattern = /opt/gridgain/etc/gridgain9-%u-%g.log
    java.util.logging.FileHandler.formatter = org.apache.ignite.internal.lang.JavaLoggerFormatter
    java.util.logging.FileHandler.level = WARNING
    java.util.logging.FileHandler.encoding = UTF-8
```

- Mount it in the `StatefulSet`:

```yaml
volumeMounts:
  - name: logging
    mountPath: /opt/gridgain/etc/gridgain.java.util.logging.properties
    subPath: gridgain.java.util.logging.properties
...
volumes:
  - name: logging
    configMap:
      defaultMode: 420
      name: gg9-gridgain9-logging
```

If you use Helm, the same can be defined via `configMaps` in `values.yaml`:

```yaml
configMaps:
  logging:
    name: gridgain.java.util.logging.properties
    path: /opt/gridgain/etc/gridgain.java.util.logging.properties
    subpath: gridgain.java.util.logging.properties
    content: |
      handlers=java.util.logging.FileHandler
      java.util.logging.SimpleFormatter.format = [%1$tF %1$tT] [%4$s] %5$s%6$s%n
      java.util.logging.FileHandler.pattern = /opt/gridgain/etc/gridgain9-%u-%g.log
      java.util.logging.FileHandler.formatter = org.apache.ignite.internal.lang.JavaLoggerFormatter
      java.util.logging.FileHandler.level = WARNING
      java.util.logging.FileHandler.encoding = UTF-8
```

Once both are configured, directory—file logging becomes active on startup.

#### Default Storage Configuration

In Kubernetes deployments, the default storage profile is defined in the ConfigMap created during installation.

- You can use this configuration:

  ```javascript
  storage: {
    profiles = [
      {
        engine = "aipersist"
        name = "default"
        replacementMode = "CLOCK"
        sizeBytes = 2147483648
      }
    ]
  }
  ```

- Or see the [example](https://github.com/gridgain/helm-charts/blob/e97576fb05101fa4ddd6959d268a17f150910059/charts/gridgain9/examples/custom_config/values.yaml) on how to redefine it for the Helm chart.

### Create and Deploy the Service

Depending on your requirements, define and deploy a Kubernetes service. Gridgain 9 use two types of services: one for internal cluster discovery, and the other -- for external client access.

1. First, choose a type of service you need and prepare the `service.yaml` file.

- For communication inside the Kubernetes cluster, Use a headless service by setting the `clusterIP` parameter to `None`. This will expose each pod's IP, enabling GridGain to be partition‑aware: clients discover every node's address, determine which partition resides on which node, and send requests directly where the data is located.

{% code title="service.yaml" %}
```yaml
apiVersion: v1
kind: Service
metadata:
  # The name must be equal to netClusterNodes.
  name: gridgain-svc-headless
  # Place your namespace name here.
  namespace: <namespace>
spec:
  clusterIP: None
  internalTrafficPolicy: Cluster
  ipFamilies:
  - IPv4
  ipFamilyPolicy: SingleStack
  ports:
  - name: management
    port: 10300
    protocol: TCP
    targetPort: 10300
  - name: rest
    port: 10800
    protocol: TCP
    targetPort: 10800
  - name: cluster
    port: 3344
    protocol: TCP
    targetPort: 3344
  selector:
    # Must be equal to the label set for pods.
    app: gridgain 
  # Include not-yet-ready nodes.
  publishNotReadyAddresses: True
  sessionAffinity: None
  type: ClusterIP
```
{% endcode %}

{% hint style="warning" %}
The `publishNotReadyAddresses: true` setting is required for GridGain 9 cluster initialization. It ensures that DNS records for pods are published even before the pods become ready, allowing the cluster nodes to discover each other during startup. Without this setting, nodes cannot resolve each other's addresses until they pass readiness probes, creating a circular dependency.
{% endhint %}

- Use a `LoadBalancer` service to allow external clients to connect. Keep in mind, that with this option you giving up partition awareness.

  If your environments does not support `LoadBalancer`, you can use `type: NodePort` instead. Refer to the Kubernetes [documentation](https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/) for details.

  ```yaml
  apiVersion: v1
  kind: Service
  metadata:
    name: gridgain-loadbalancer
    labels:
      app: gridgain
  spec:
    type: LoadBalancer
    selector:
      app: gridgain
    # Set to true so that the StatefulSet's Headless Service propagates SRV DNS records for its Pods for node discovery
    publishNotReadyAddresses: true
    ports:
      - name: rest
        protocol: TCP
        port: 10800
        targetPort: 10800
      - name: client
        port: 10300
        protocol: TCP
        targetPort: 10300
  ```

2. Then apply the `service.yaml` file to set up this service:

```bash
kubectl apply -f service.yaml
```

### Deploy the StatefulSet

1. Prepare the `statefulset.yaml` file for StatefulSet deployment:

   {% code title="statefulset.yaml" %}
   ```yaml
   apiVersion: apps/v1 
   kind: StatefulSet 
   metadata:
     # The cluster name.
     name: gridgain-cluster
     # Place your namespace name.
     namespace: <namespace>
   spec:
     # Default value is Parallel so the StatefulSet controller doesn't wait the pod to become ready in order to start new one.
     podManagementPolicy: Parallel
     # The initial number of pods to be started by Kubernetes.
     replicas: 2
     # Kubernetes service to access the GridGain 9 cluster on the Kubernetes network.
     serviceName: gridgain-svc-headless
     selector:
       matchLabels:
         app: gridgain
     template:
       metadata:
         labels:
           app: gridgain 
       spec:
         terminationGracePeriodSeconds: 60000
         containers:
           # Custom pod name.
         - name: gridgain-node
           # Limits and requests for the GridGain container.
           resources:
             limits:
               cpu: "4"
               memory: 4Gi
             requests:
               cpu: "4"
               memory: 4Gi
           env:
             # Must be specified to ensure that GridGain 9 cluster replicas are visible to each other. 
             - name: GRIDGAIN_NODE_NAME
               valueFrom:
                 fieldRef: 
                   fieldPath: metadata.name
             # GridGain 9 working directory.
             - name: GRIDGAIN_WORK_DIR
               value: /gg9-work
           # GridGains Docker image and it's version.
           image: gridgain/gridgain9:9.1
           ports:
           - containerPort: 10300
           - containerPort: 10800
           - containerPort: 3344
           readinessProbe:
             failureThreshold: 3
             httpGet:
               path: /health/readiness
               port: 10300
               scheme: HTTP
             initialDelaySeconds: 30
             periodSeconds: 10
             successThreshold: 1
             timeoutSeconds: 10
           livenessProbe:
             failureThreshold: 3
             httpGet:
               path: /health/liveness
               port: 10300
               scheme: HTTP
             initialDelaySeconds: 5
             periodSeconds: 30
             successThreshold: 1
             timeoutSeconds: 10
           volumeMounts:
           # The config will be placed at this path in the container.
           - mountPath: /opt/gridgain/etc/gridgain-config.conf
             name: config-vol
             subPath: gridgain-config.conf
           # The license will be placed at this path in the container.
           - mountPath: /opt/gridgain/etc/license.conf
             name: license-vol
             subPath: license.conf
           # GridGain 9 working directory.
           - mountPath: /gg9-work
             name: persistence
         volumes:
         - name: config-vol
           configMap:
             name: gridgain-config
         - name: license-vol
           configMap:
             name: gridgain-license
     volumeClaimTemplates:
     - apiVersion: v1
       kind: PersistentVolumeClaim
       metadata:
         name: persistence
       spec:
         accessModes:
         - ReadWriteOnce
         resources:
           requests:
             storage: 10Gi # Provide enough space for your application data.
         volumeMode: Filesystem
   ```
   {% endcode %}
2. Apply the `statefulset.yaml` file to deploy the main components of GridGain 9:

   ```bash
   kubectl apply -f statefulset.yaml
   ```

### Wait for Pods to Start

1. Monitor the status of the pods:

   ```bash
   kubectl get pods -n <namespace> -w
   ```
2. Ensure that all pods' `STATUS` is `Running` before proceeding.

### Deploy the Job

1. Prepare the `job.yaml` file for deploying the job:

   {% code title="job.yaml" %}
   ```yaml
   apiVersion: batch/v1
   kind: Job
   metadata:
     name: cluster-init
     # Place your namespace name here.
     namespace: <namespace>
   spec:
     template:
       spec:
         containers:
         # Command to init the cluster. URL and host must be the name of the service you created before. Port is 10300 as the management port.
         - args:
           - -ec
           - |
             apt update && apt-get install -y bind9-host
             GG_NODES=$(host -tsrv _cluster._tcp.gridgain-svc-headless | grep 'SRV record' | awk '{print $8}' | awk -F. '{print $1}' | paste -sd ',')
             /opt/gridgain9cli/bin/gridgain9 cluster init --name=gridgain --url=http://gridgain-svc-headless:10300 --license=/opt/gridgain/etc/license.conf
           command:
           - /bin/sh
           # Specify the Docker image with the GridGain 9 CLI and its version.
           image: gridgain/gridgain9:9.1
           imagePullPolicy: IfNotPresent
           name: cluster-init
           resources: {}
           volumeMounts:
           # The license required to be mounted to cluster-init job.
           - mountPath: /opt/gridgain/etc/license.conf
             name: license-vol
             subPath: license.conf
         restartPolicy: Never
         terminationGracePeriodSeconds: 120
         volumes:
         - name: license-vol
           configMap:
             name: gridgain-license
   ```
   {% endcode %}
2. Apply the `job.yaml` file to complete installation.

   ```bash
   kubectl apply -f job.yaml
   ```

## Installation Verification

1. Check the status of all resources in your namespace:

   ```bash
   kubectl get all -n <namespace>
   ```
2. Ensure that all components are running as expected, without errors, and that the initialization job is in the `Completed` status.
3. Verify that your cluster is initialized and running.

   ```bash
   kubectl exec -it gridgain-cluster-0 bash -n <namespace>
   /opt/gridgain9cli/bin/gridgain9 cluster status
   ```

The command output must include the name of your cluster and the number of nodes. The status must be `ACTIVE`.

## Optional: Liveness and Readiness Probes

You can set up configuration for readiness and liveness probes.

- Liveness probe checks if the GridGain node has started in the pod, and responds to REST requests on the liveness endpoint.
- Readiness probe checks if the GridGain node has joined the cluster and is ready to receive data.

{% hint style="warning" %}
When using readiness probes, you must configure both `publishNotReadyAddresses: true` and `podManagementPolicy: Parallel` properties. Without these settings, pods will not be able to discover each other during initialization.
{% endhint %}

The example below shows how to set up liveness and readiness probes with recommended defaults:

```yaml
livenessProbe:
  failureThreshold: 3
  httpGet:
    path: /health/liveness
    port: 10300
    scheme: HTTP
  initialDelaySeconds: 5
  periodSeconds: 30
  successThreshold: 1
  timeoutSeconds: 10
readinessProbe:
  failureThreshold: 3
  httpGet:
    path: /health/readiness
    port: 10300
    scheme: HTTP
  initialDelaySeconds: 30
  periodSeconds: 10
  successThreshold: 1
  timeoutSeconds: 10
```

{% hint style="info" %}
Since readiness and liveness probes are highly recommended for kubernetes deployments, the `statefulset.yaml` provided above includes this configuration.
{% endhint %}

For more information about the REST endpoints, see the [OpenAPI specification](https://www.gridgain.com/sdk/gridgain9/latest/openapi.html).

## Optional: KEDA Configuration

You can configure KEDA to automatically scale the cluster based on your needs, ensuring optimal resource optimization and performance. This implementation uses Prometheus to monitor cluster load.

{% hint style="warning" %}
Before configuring KEDA autoscaling based on JVM metrics, you must define the maximum heap and non-heap (Metaspace) memory for the GridGain Java process. If these are not set, threshold values will be calculated incorrectly.

You can set these limits by modifying the `statefulset` to define the `GRIDGAIN9_EXTRA_JVM_ARGS` environment variable and define `-Xmx` (max heap size) and `-XX:MaxMetaspaceSize` (max non-heap/metaspace size) flags.

The total memory for these flags should be less than the container's memory limit (e.g., memory: 4Gi in the limits).
{% endhint %}

To enable KEDA scaling for your cluster:

- Add the necessary Helm repositories, install KEDA and Prometheus:

  ```bash
  helm install keda kedacore/keda --namespace keda --create-namespace
  helm install prometheus prometheus-community/prometheus --namespace keda -f prometheus-values.yaml
  ```
- Deploy the KEDA configurations:
  - The `keda-scaled-object.yaml` configuration defines the scaling rules for the GridGain cluster:

    {% code title="keda-scaled-object.yaml" %}
    ```yaml
    apiVersion: keda.sh/v1alpha1
    kind: ScaledObject
    metadata:
      name: gridgain-autoscale
      namespace: gridgain
    spec:
      scaleTargetRef:
        kind: StatefulSet
        name: gridgain-cluster

      pollingInterval: 30
      cooldownPeriod: 120

      minReplicaCount: 2  # Set initial number of replics
      maxReplicaCount: 5

      advanced:
        horizontalPodAutoscalerConfig:
          behavior:
            scaleDown:
              selectPolicy: Disabled
            scaleUp:
              stabilizationWindowSeconds: 60  # Increase if needed
              selectPolicy: Max
              policies:
                - type: Pods
                  value: 1
                  periodSeconds: 120

      triggers:
        # Uncomment and modify the following section to enable CPU usage based autoscaling
        # - type: prometheus
        #   metadata:
        #     name: cpu-usage
        #     serverAddress: http://prometheus-server.keda.svc.cluster.local:80
        #     query: sum(os_system_load_average{job="gridgain"})
        #     threshold: "0.8"
        #     activationThreshold: "0.6"
        - type: prometheus
          name: heap-memory-usage
          metadata:
            serverAddress: http://prometheus-server.keda.svc.cluster.local:80
            query: |
              sum(jvm_memory_committed_bytes{area="heap", job="gridgain"} / jvm_memory_max_bytes{area="heap", job="gridgain"})
            threshold: "0.7"
        - type: prometheus
          name: nonheap-memory-usage
          metadata:
            serverAddress: http://prometheus-server.keda.svc.cluster.local:80
            query: |
              sum(jvm_memory_committed_bytes{area="nonheap", job="gridgain"} / jvm_memory_max_bytes{area="nonheap", job="gridgain"})
            threshold: "0.7"
    ```
    {% endcode %}
  - The `keda-recovery-scaled-job.yaml` configuration handles rebuilding [CMG nodes](../../architecture/cluster-lifecycle.md#cluster-management-group) in the GridGain cluster.

    {% code title="keda-scaled-object.yaml" %}
    ```yaml
    apiVersion: keda.sh/v1alpha1
    kind: ScaledJob
    metadata:
      name: gridgain-recovery
      namespace: gridgain
    spec:
      jobTargetRef:
        template:
          spec:
            # securityContext:
            #   runAsUser: 0
            #   runAsGroup: 0
            #   fsGroup: 0
            containers:
              - name: recovery
                image: gridgain/gridgain9:9.1.21
                command: ["/bin/bash", "/scripts/recovery.sh"]
                volumeMounts:
                - name: script-vol
                  mountPath: /scripts
            restartPolicy: Never
            volumes:
            - name: script-vol
              configMap:
                name: gridgain-recovery-script
                defaultMode: 0777
        backoffLimit: 1
      pollingInterval: 30
      successfulJobsHistoryLimit: 2
      failedJobsHistoryLimit: 3
      maxReplicaCount: 1
      triggers:
        # - type: prometheus
        #   metadata:
        #     serverAddress: http://prometheus-server.keda.svc.cluster.local:80
        #     query: avg(os_system_load_average{job="gridgain"})
        #     threshold: "0.8"
        #     activationThreshold: "0.6"
        - type: prometheus
          name: heap-memory-usage
          metadata:
            serverAddress: http://prometheus-server.keda.svc.cluster.local:80
            query: |
              avg(jvm_memory_committed_bytes{area="heap", job="gridgain"} / jvm_memory_max_bytes{area="heap", job="gridgain"})
            threshold: "0.7"
        - type: prometheus
          name: nonheap-memory-usage
          metadata:
            serverAddress: http://prometheus-server.keda.svc.cluster.local:80
            query: |
              avg(jvm_memory_committed_bytes{area="nonheap", job="gridgain"} / jvm_memory_max_bytes{area="nonheap", job="gridgain"})
            threshold: "0.7"
    ```
    {% endcode %}
- You can deploy the above configurations with the following commands:

  ```bash
  kubectl apply -n gridgain -f keda-scaled-object.yaml
  kubectl apply -n gridgain -f keda-recovery-scaled-job.yaml
  ```

## Installation Troubleshooting

If any issues occur during the installation:

- Check the logs of specific pods:

  ```bash
  kubectl logs <pod-name> -n <namespace>
  ```
- Review events in the namespace:

  ```bash
  kubectl get events -n <namespace>
  ```

## Troubleshooting via REST

This approach is intended for short-lived debugging and testing sessions, not for long-term or external access.

{% hint style="warning" %}
`kubectl port-forward` opens a local tunnel from your machine to a pod through the Kubernetes API server. Do not expose REST this way permanently.
{% endhint %}

1. Forward the REST port to a specific GridGain 9 replica:

   ```bash
   kubectl port-forward <pod-name> 10300:10300 -n <namespace>
   ```

   Example:

   ```bash
   kubectl port-forward gridgain-cluster-0 10300:10300 -n gridgain
   ```
2. Open a new terminal and run REST requests to the `http://localhost:10300`, for example:

   ```bash
   curl 'http://localhost:10300/management/v1/cluster/state'

   {"title":"Cluster is not initialized","status":409,"detail":"Cluster is not initialized. Call /management/v1/cluster/init in order to initialize cluster."}
   ```

   ```bash
   curl 'http://localhost:10300/management/v1/node/info'
   {"name":"gridgain-cluster-0","jdbcPort":10800}
   ```

For more information refer to the documentation:

- Kubernetes: [Use Port Forwarding to Access Applications in a Cluster](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/)
- `kubectl` command reference: [kubectl port-forward](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_port-forward/)
- GridGain 9 REST API docs: [REST API](../../reference/rest-api/overview.md)

## Limitations and Considerations

When running GridGain 9 in a Kubernetes environment, the node configuration becomes **read-only** and cannot be modified by using the `gridgain9 node config update` CLI command. This is by design, as node configuration is managed via Kubernetes resources. To change your configuration:

1. Manually update the corresponding ConfigMap;
2. Restart all cluster pods by executing `kubectl delete pod` for each replica.

The updated configuration will take effect after the pods are recreated by the Kubernetes controller.

{% hint style="warning" %}
While it is technically possible to make the node configuration writable by using an init container that copies the mounted configuration from one location to another (and pointing GridGain 9 to this new location), we **strongly discourage** this approach. It is not native to the Kubernetes model, and any changes made to the configuration will be lost during pod restarts or re-deployments.
{% endhint %}
