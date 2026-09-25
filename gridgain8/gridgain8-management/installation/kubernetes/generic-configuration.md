---
description: >-
  A generic, step-by-step guide to deploying and managing GridGain server nodes
  on Kubernetes using a StatefulSet, covering configuration, licensing, probes,
  activation, scaling, and connectivity.
---

# Generic Kubernetes Instruction

{% hint style="warning" %}
This guide was written using `kubectl` version 1.17.
{% endhint %}

## Introduction

In this tutorial, we will use StatefulSet to manage GridGain cluster in Kubernetes. We will create both in-memory and persistent clusters.

{% hint style="warning" %}
This guide focuses on Kubernetes server nodes. If you want to run client nodes on Kubernetes while your cluster is deployed elsewhere, you need to enable the communication mode designed for client nodes running behind a NAT. Refer to [this section](../../../gridgain8-usage/clustering/running-client-nodes-behind-nat.md).
{% endhint %}

## Kubernetes Configuration

Kubernetes configuration involves creating the following resources:

- A namespace
- A cluster role
- A ConfigMap for the node configuration file
- A ConfigMap for the license file if you use Enterprise or Ultimate Edition
- A service to be used for discovery and load balancing when external apps connect to the cluster
- A configuration for pods running GridGain nodes

{% hint style="info" %}
It is also required to provide a license by using one of the methods described below.
{% endhint %}

### Creating Namespace

Create a unique namespace for your deployment.
In our case, the namespace is called "gridgain".

Create the namespace using the following command:

```shell
kubectl create namespace gridgain
```

### Creating Service

The Kubernetes service is used for auto-discovery and as a load-balancer for external applications that connect to your cluster.

Every time a new node is started (in a separate pod), the IP finder connects to the service via the Kubernetes API to obtain the list of the existing pods' addresses.
The new node uses this addresses to discover all cluster nodes.

{% code title="service.yaml" %}
```yaml
apiVersion: v1
kind: Service
metadata: 
  # The name must be equal to TcpDiscoveryKubernetesIpFinder.serviceName
  name: gridgain-service
  # The name must be equal to TcpDiscoveryKubernetesIpFinder.namespace
  namespace: gridgain
  labels:
    app: gridgain
spec:
  type: LoadBalancer
  ports:
    - name: rest
      port: 8080
      targetPort: 8080
    - name: thinclients
      port: 10800
      targetPort: 10800
  # Optional - remove 'sessionAffinity' property if the cluster
  # and applications are deployed within Kubernetes
  #  sessionAffinity: ClientIP   
  selector:
    # Must be equal to the label set for pods.
    app: gridgain
status:
  loadBalancer: {}
```
{% endcode %}

Create the service:

```shell
kubectl create -f service.yaml
```

### Creating Cluster Role and Service Account

Create a service account:

```shell
kubectl create sa gridgain -n gridgain
```

A cluster role is used to grant access to pods. The following file is an example of a cluster role:

{% code title="cluster-role.yaml" %}
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: gridgain
  namespace: gridgain
rules:
- apiGroups:
  - ""
  resources: # Here are the resources you can access
  - pods
  - endpoints
  verbs: # That is what you can do with them
  - get
  - list
  - watch
---
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: gridgain
roleRef:
  kind: ClusterRole
  name: gridgain
  apiGroup: rbac.authorization.k8s.io
subjects:
- kind: ServiceAccount
  name: gridgain
  namespace: gridgain
```
{% endcode %}

Run the following command to create the role and a role binding:

```shell
kubectl create -f cluster-role.yaml
```

### Creating ConfigMap for Node Configuration File

We create a ConfigMap that keeps the node configuration file so that every node can use it.
This allows you to keep a single instance of the configuration file for all nodes.

Let's create a configuration file first.
Choose one of the tabs below, depending on whether you use persistence or not.

{% tabs %}
{% tab title="Configuration without persistence" %}
We must use the `TcpDiscoveryKubernetesIpFinder` IP finder for node discovery.
This IP finder connects to the service via the Kubernetes API and obtains the list of the existing pods' addresses. The new node uses these addresses to discover all other cluster nodes.

The file looks like this:

{% code title="node-configuration.xml" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
        http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean class="org.apache.ignite.configuration.IgniteConfiguration">

        <property name="discoverySpi">
            <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
                <property name="ipFinder">
                    <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.kubernetes.TcpDiscoveryKubernetesIpFinder">
                        <property name="namespace" value="gridgain"/>
                        <property name="serviceName" value="gridgain-service"/>
                    </bean>
                </property>
            </bean>
        </property>
    </bean>
</beans>
```
{% endcode %}
{% endtab %}

{% tab title="Configuration with persistence" %}
In the configuration file, we:

- Enable [native persistence](../../../architecture/storage/native-persistence.md) and specify the `workDirectory`, `walPath`, and `walArchivePath`. These directories are mounted in each pod that runs a GridGain node. Volume configuration is part of the [pod configuration](#creating-pod-configuration).
- Use the `TcpDiscoveryKubernetesIpFinder` IP finder. This IP finder connects to the service via the Kubernetes API and obtains the list of the existing pods' addresses. The new node uses these addresses to discover all other cluster nodes.

The file looks like this:

{% code title="node-configuration.xml" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
    http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean class="org.apache.ignite.configuration.IgniteConfiguration">

        <property name="workDirectory" value="/opt/gridgain/work"/>

        <property name="dataStorageConfiguration">
            <bean class="org.apache.ignite.configuration.DataStorageConfiguration">
                <property name="defaultDataRegionConfiguration">
                    <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                        <property name="persistenceEnabled" value="true"/>
                    </bean>
                </property>

                <property name="walPath" value="/opt/gridgain/wal"/>
                <property name="walArchivePath" value="/opt/gridgain/walarchive"/>
            </bean>

        </property>

        <property name="discoverySpi">
            <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
                <property name="ipFinder">
                    <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.kubernetes.TcpDiscoveryKubernetesIpFinder">
                        <property name="namespace" value="gridgain"/>
                        <property name="serviceName" value="gridgain-service"/>
                    </bean>
                </property>
            </bean>
        </property>

    </bean>
</beans>
```
{% endcode %}
{% endtab %}
{% endtabs %}

The `namespace` and `serviceName` properties of the IP finder must be the same as specified in the [service configuration](#creating-service).
Add other properties as required for your use case.

To create the ConfigMap, run the following command in the directory with the `node-configuration.xml` file.

```shell
kubectl create configmap gridgain-config -n gridgain --from-file=node-configuration.xml
```

### Providing License File

If you use GridGain Enterprise or Ultimate Edition, you must provide the license file.
You can provide the license file as a link to a remote resource, or you can mount the file to each pod.

#### License via URL

Use the `LICENSE_URI` variable as described in the [Docker documentation](../installing-using-docker.md#providing-license-file) in the pod specification file.
See the example in the [Creating Pod Configuration](#creating-pod-configuration) section.

#### License via ConfigMap

Create a ConfigMap from the license file by running the following command. The `--from-file` option must point to an existing license file.

```shell
kubectl create configmap gridgain-license -n gridgain --from-file=gridgain-license.xml
```

Use this config map ('gridgain-license') to mount the license in the pod configuration. The file must be mounted under the path of the default license file available in the `GRIDGAIN-HOME` directory.
See the example in the [Creating Pod Configuration](#creating-pod-configuration) section below.

### Creating Pod Configuration

Now we create a configuration for pods that use a [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/).

Our configuration deploys 2 pods running GridGain Enterprise Edition 8.10.
If you want to use Ultimate Edition, change the `spec.template.spec.containers.image` property in the configuration file.

In the container's configuration we:

- Enable the "ignite-kubernetes" and "ignite-rest-http" [modules](../installing-using-docker.md#enabling-modules).
- Use the configuration file from the ConfigMap we created earlier.
- Mount volumes for the work directory (where application data is stored), WAL files, and WAL archive.
- Open a number of ports:
  - 47100 — the communication port
  - 47500 ­—­ the discovery port
  - 49112 — the default JMX port
  - 10800 — thin client/JDBC/ODBC port
  - 8080 — REST API port

The StatefulSet configuration file might look like as follows:

{% code title="statefulset.yaml" %}
```yaml
# An example of a Kubernetes configuration for pod deployment.
apiVersion: apps/v1 
kind: StatefulSet 
metadata:
  # Cluster name.
  name: gridgain-cluster
  namespace: gridgain
spec:
  # The initial number of pods to be started by Kubernetes.
  replicas: 2
  serviceName: gridgain
  selector:
    matchLabels:
      app: gridgain
  template:
    metadata:
      labels:
        app: gridgain 
    spec:
      serviceAccountName: gridgain 
      terminationGracePeriodSeconds: 60000 
      containers:
        # Custom pod name.
      - name: gridgain-node
        image: gridgain/enterprise:8.10
        env:
        - name: OPTION_LIBS
          value: ignite-kubernetes,ignite-rest-http
        - name: CONFIG_URI
          value: file:///opt/gridgain/config/node-configuration.xml
        - name: JVM_OPTS
          value: "-DIGNITE_WAL_MMAP=false -DIGNITE_WAIT_FOR_BACKUPS_ON_SHUTDOWN=true"
         # if you want to provide the license file via URI, uncomment the following 2 lines
#        - name: LICENSE_URI
#          value: http://url_to_license_file 
        ports:
        # Ports to open.
        - containerPort: 47100 # communication SPI port
        - containerPort: 47500 # discovery SPI port
        - containerPort: 49112 # JMX port
        - containerPort: 10800 # thin clients/JDBC driver port
        - containerPort: 8080 # REST API
        volumeMounts:
        - mountPath: /opt/gridgain/config
          name: config-vol
        - mountPath: /opt/gridgain/work
          name: work-vol
        - mountPath: /opt/gridgain/wal
          name: wal-vol
        - mountPath: /opt/gridgain/walarchive
          name: walarchive-vol
        readinessProbe:
          httpGet:
           path: "/ignite?cmd=probe&kind=readiness"
           port: 8080
          initialDelaySeconds: 5
          failureThreshold: 3
          periodSeconds: 10
          timeoutSeconds: 10
        livenessProbe:
          httpGet:
           path: "/ignite?cmd=probe&kind=liveness"
           port: 8080
          initialDelaySeconds: 5
          failureThreshold: 3
          periodSeconds: 10
          timeoutSeconds: 10
        startupProbe:
          httpGet:
           path: "/ignite?cmd=probe&kind=readiness"
           port: 8080
          failureThreshold: 30
          periodSeconds: 10
# uncomment the following mount path if you want to provide a license
# the license must be mounted under this exact path
#        - mountPath: /opt/gridgain/gridgain-license.xml
#          subPath: gridgain-license.xml
#          name: license-vol          
      securityContext:
        fsGroup: 2000 # try removing this if you have permission issues
      volumes:
      - name: config-vol
        configMap:
          name: gridgain-config
      # uncomment the following volume if you want to provide a license
#      - name: license-vol
#        configMap:
#          name: gridgain-license          
  volumeClaimTemplates:
  - metadata:
      name: work-vol
    spec:
      accessModes: [ "ReadWriteOnce" ]
#      storageClassName: "gridgain-persistence-storage-class"
      resources:
        requests:
          storage: "1Gi" # make sure to provide enough space for your application data
  - metadata:
      name: wal-vol
    spec:
      accessModes: [ "ReadWriteOnce" ]
#      storageClassName: "gridgain-wal-storage-class"
      resources:
        requests:
          storage: "1Gi" 
  - metadata:
      name: walarchive-vol
    spec:
      accessModes: [ "ReadWriteOnce" ]
#      storageClassName: "gridgain-wal-storage-class"
      resources:
        requests:
          storage: "1Gi"

```
{% endcode %}

Note the `spec.volumeClaimTemplates` section, which defines persistent volumes provisioned by a persistent volume provisioner.
The volume type depends on the cloud provider.
You can have more control over the volume type by defining [storage classes](https://kubernetes.io/docs/concepts/storage/storage-classes/).

{% hint style="warning" %}
Do not store the work directory, WAL, or WAL archive on NFS volumes. GridGain uses an OS-level advisory lock (`fcntl`) to prevent two nodes from sharing a persistence directory. On NFS volumes the lock is held by the server and survives the client for up to 30-90 seconds. Because Kubernetes restarts crashed pods inside that window, the restarting node cannot reacquire its own lock and the pod is stuck in `CrashLoopBackOff` until the server times out.
{% endhint %}

Create the StatefulSet by running the following command:

```shell
kubectl create -f statefulset.yaml
```

Check if the pods were created correctly:

```bash
$ kubectl get pods -n gridgain
NAME                                READY   STATUS    RESTARTS   AGE
gridgain-cluster-5b69557db6-lcglw   1/1     Running   0          44m
gridgain-cluster-5b69557db6-xpw5d   1/1     Running   0          44m
```

Check the logs of the nodes:

```
$ kubectl logs gridgain-cluster-5b69557db6-lcglw -n gridgain
[14:33:50]    __________  ________________
[14:33:50]   /  _/ ___/ |/ /  _/_  __/ __/
[14:33:50]  _/ // (7 7    // /  / / / _/
[14:33:50] /___/\___/_/|_/___/ /_/ /___/
[14:33:50]
[14:33:50] ver. 8.7.8#20191129-sha1:6b3cc030
[14:33:50] 2019 Copyright(C) GridGain Systems, Inc. and Contributors
[14:33:50]
[14:33:50] Ignite documentation: http://gridgain.com
[14:33:50]
[14:33:50] Quiet mode.
[14:33:50]   ^-- Logging to file '/opt/gridgain/work/log/ignite-b8622b65.0.log'
[14:33:50]   ^-- Logging by 'JavaLogger [quiet=true, config=null]'
[14:33:50]   ^-- To see **FULL** console log here add -DIGNITE_QUIET=false or "-v" to ignite.{sh|bat}
[14:33:50]
[14:33:50] OS: Linux 4.19.81 amd64
[14:33:50] VM information: OpenJDK Runtime Environment 1.8.0_212-b04 IcedTea OpenJDK 64-Bit Server VM 25.212-b04
[14:33:50] Please set system property '-Djava.net.preferIPv4Stack=true' to avoid possible problems in mixed environments.
[14:33:50] Initial heap size is 30MB (should be no less than 512MB, use -Xms512m -Xmx512m).
[14:33:50] Configured plugins:
[14:33:50]   ^-- None
[14:33:50]
[14:33:50] Configured failure handler: [hnd=StopNodeOrHaltFailureHandler [tryStop=false, timeout=0, super=AbstractFailureHandler [ignoredFailureTypes=UnmodifiableSet [SYSTEM_WORKER_BLOCKED, SYSTEM_CRITICAL_OPERATION_TIMEOUT]]]]
[14:33:50] Message queue limit is set to 0 which may lead to potential OOMEs when running cache operations in FULL_ASYNC or PRIMARY_SYNC modes due to message queues growth on sender and receiver sides.
[14:33:50] Security status [authentication=off, tls/ssl=off]
[14:34:00] Nodes started on local machine require more than 80% of physical RAM what can lead to significant slowdown due to swapping (please decrease JVM heap size, data region size or checkpoint buffer size) [required=918MB, available=1849MB]
[14:34:01] Performance suggestions for grid  (fix if possible)
[14:34:01] To disable, set -DIGNITE_PERFORMANCE_SUGGESTIONS_DISABLED=true
[14:34:01]   ^-- Enable G1 Garbage Collector (add '-XX:+UseG1GC' to JVM options)
[14:34:01]   ^-- Specify JVM heap max size (add '-Xmx<size>[g|G|m|M|k|K]' to JVM options)
[14:34:01]   ^-- Set max direct memory size if getting 'OOME: Direct buffer memory' (add '-XX:MaxDirectMemorySize=<size>[g|G|m|M|k|K]' to JVM options)
[14:34:01] Refer to this page for more performance suggestions: https://apacheignite.readme.io/docs/jvm-and-system-tuning
[14:34:01]
[14:34:01] Data Regions Configured:
[14:34:01]   ^-- default [initSize=256.0 MiB, maxSize=370.0 MiB, persistence=false, lazyMemoryAllocation=true]
[14:34:01]
[14:34:01] Ignite node started OK (id=b8622b65)
[14:34:01] Topology snapshot [ver=2, locNode=b8622b65, servers=2, clients=0, state=ACTIVE, CPUs=2, offheap=0.72GB, heap=0.88GB]
```

The string `servers=2` in the last line indicates that the two nodes joined into a single cluster.

### Readiness Probe

The readiness probe controls when a pod starts receiving traffic from the Kubernetes Service. It uses the [PROBE](../../../reference/rest-api/README.md#probe) REST command with `kind=readiness` argument, which reports the node as ready only after it has finished pulling its partitions. This keeps Kubernetes from routing traffic to a node that is still rebalancing.

### Liveness Probe

The liveness probe controls when Kubernetes restarts an unhealthy pod. It uses the [PROBE](../../../reference/rest-api/README.md#probe) REST command with `kind=liveness` argument, which checks only that the Ignite kernel has started; a node that is rebalancing or in maintenance mode is still considered alive and is not restarted.

### Startup Probe

The startup probe gives a (re)joining node time to complete its initial rebalance before the liveness probe takes over. It uses the same `kind=readiness` check as the readiness probe.

### Draining a Node

{% hint style="warning" %}
In GridGain 8.10, the DRAIN command does not set the node's drain flag correctly, preventing Kubernetes from draining the node.
{% endhint %}

To take a pod out of rotation before a rolling restart, send the [DRAIN](../../../reference/rest-api/README.md#drain) REST command with `action=start` argument. This sets the node's drain flag, which makes the readiness probe report 503 so that Kubernetes stops routing new traffic to the pod before it is terminated. Send DRAIN command with `action=stop` argument to clear the flag and return the node to normal readiness behavior. The flag is held in node memory and is cleared automatically when the pod restarts.

## Activating the Cluster

If you use a stateless cluster, skip this step: a cluster without persistence does not require activation.

If you are using persistence, you must activate the cluster after it is started. To do that, connect to one of the pods:

```shell
kubectl exec -it <pod_name> -n gridgain -- /bin/bash
```

Execute the following command:

```shell
/opt/gridgain/bin/control.sh --activate
```

You can also activate the cluster using the [REST API](../../../reference/rest-api/README.md#activate). Refer to the [Connecting to the Cluster](#connecting-to-the-cluster) section for details about connection to the cluster's REST API.

## Scaling the Cluster

You can add more nodes to the cluster by using the `kubectl scale` command.

{% hint style="warning" %}
Make sure your cluster has enough resources to add new pods.
{% endhint %}

In the following example, we bring up one more node (we had two).

{% tabs %}
{% tab title="Configuration without persistence" %}
To scale your StatefulSet, run the following command:

```shell
kubectl scale sts  gridgain-cluster --replicas=3 -n gridgain
```
{% endtab %}

{% tab title="Configuration with persistence" %}
To scale your StatefulSet, run the following command:

```shell
kubectl scale sts gridgain-cluster --replicas=3 -n gridgain
```

After scaling the cluster, [change the baseline topology](../../../reference/cli-tool/README.md#activation-deactivation-and-topology-management) accordingly.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
If you reduce the number of nodes by more than the [number of partition backups](../../../gridgain8-usage/configuring-caches/configuring-backups.md), you may lose data. The proper way to scale down is to redistribute the data after removing a node by changing the [baseline topology](../../../reference/cli-tool/README.md).
{% endhint %}

## Connecting to the Cluster

If your application is also running in Kubernetes, you can use either thin clients or client nodes to connect to the cluster.

Get the public IP of the service:

```shell
$ kubectl describe svc gridgain-service -n gridgain
Name:                     gridgain-service
Namespace:                gridgain
Labels:                   app=gridgain
Annotations:              <none>
Selector:                 app=gridgain
Type:                     LoadBalancer
IP:                       10.0.144.19
LoadBalancer Ingress:     13.86.186.145
Port:                     rest  8080/TCP
TargetPort:               8080/TCP
NodePort:                 rest  31912/TCP
Endpoints:                10.244.1.5:8080
Port:                     thinclients  10800/TCP
TargetPort:               10800/TCP
NodePort:                 thinclients  31345/TCP
Endpoints:                10.244.1.5:10800
Session Affinity:         None
External Traffic Policy:  Cluster
```

You can use the `LoadBalancer Ingress` address to connect to one of the open ports.
The ports are also listed in the output of the command.

### Connecting Client Nodes

A client node requires connection to every node in the cluster. The only way to achieve this is to start a client node within Kubernetes.
You need to configure the discovery mechanism to use `TcpDiscoveryKubernetesIpFinder`, as described in the [Creating ConfigMap for Node Configuration File](#creating-configmap-for-node-configuration-file) section.

### Connecting with Thin Clients

The following code snippet illustrates how to connect to your cluster using the [java thin client]({connectors}/thin-clients/java-thin-client). You can use other thin clients in the same way.
Note that we use the external IP address (LoadBalancer Ingress) of the service.

```java
ClientConfiguration cfg = new ClientConfiguration().setAddresses("13.86.186.145:10800");
IgniteClient client = Ignition.startClient(cfg);

ClientCache<Integer, String> cache = client.getOrCreateCache("test_cache");

cache.put(1, "first test value");

System.out.println(cache.get(1));

client.close();
```

### Connecting to REST API

Connect to the cluster's REST API as follows:

```shell
$ curl http://13.86.186.145:8080/ignite?cmd=version
{"successStatus":0,"error":null,"response":"8.10","sessionToken":null}
```

{% hint style="info" %}
[Instructor-led Developer Training - Apache Ignite and Kubernetes: Deployment and Orchestration Strategies](https://www.gridgain.com/products/services/training/apache-ignite-and-kubernetes-deployment-and-orchestration-strategies)

Join our free instructor-led training sessions to explore the best practices of using Kubernetes and Apache Ignite.
{% endhint %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
