---
description: >-
  Reference for the GridGain Operator custom resources: the Ignite resource and
  the IgniteConfig resource, their configuration options, and cluster termination.
---

# Custom Resource Configuration

To define a cluster, adjust the following resources:

`ignite.yaml` contains a set of high-level cluster settings, please check the [Ignite Resource](#ignite-resource) section for more details. 

`ignite_config.yaml` contains a set of internal cluster settings, please check the [IgniteConfig Resource](#igniteconfig-resource) section for more details. 

To apply changes, save the files and run the following commands:

```shell
kubectl apply -f crds/ignite.yaml -n apache-ignite-operator
kubectl apply -f crds/ignite_config.yaml -n apache-ignite-operator
```

## Ignite Resource

Ignite resource is represented by the `ignite.yaml` file and contains high-level configuration details such as k8s namespace, cluster name, and number of nodes.

To create a resource, use the following command:

```shell
kubectl apply -f ignite.yaml
```

### Namespace

A namespace at which to deploy a cluster. The default value is `apache-ignite`

### cluster_name

The name of the cluster. The default value is `apache-ignite-cluster`. Cluster name is used by Kubernetes to create different objects, like pods.

### cluster_type `[persistence|inmemory]`

Defines whether the cluster should use pure in-memory data access or use a [persistence storage model](../../../architecture/storage/native-persistence.md).

The default value is `persistence`. After cluster initialization, the value cannot be changed.

When the value is set to persistence, it is mandatory to configure the `StorageClass` value that the operator uses to provide the required data stores.

### storage_class_name

For `cluster_type: "persistence"` it is mandatory to have at least one storage class configured for the Kubernetes cluster. By default, if `storage_class_name` is not configured explicitly, the operator tries to use the attribute `is-default-class=True` to find the default storage class.
If the operator fails to locate the storage class, then the following error is reported:

```
The system is unable to locate StorageClass
```

This process is suitable for local development, but for production usage we suggest that you create StorageClass manually. Please check your environment for more details: https://kubernetes.io/docs/concepts/storage/storage-classes/

{% hint style="warning" %}
Do not store the work directory, WAL, or WAL archive on NFS volumes. GridGain uses an OS-level advisory lock (`fcntl`) to prevent two nodes from sharing a persistence directory. On NFS volumes the lock is held by the server and survives the client for up to 30-90 seconds. Because Kubernetes restarts crashed pods inside that window, the restarting node cannot reacquire its own lock and the pod is stuck in `CrashLoopBackOff` until the server times out.
{% endhint %}

You can check the available storage classes by using kubectl get sc and then set the appropriate storage class inside `ignite.yaml using`:

```yaml
 ...
  storage_class_name: "standard"
 ...
```

And then apply the changes:

```shell
kubectl apply -f ignite_config.yaml -n <operator-namespace>
```

### cluster_image

The default cluster image is `"gridgain/enterprise:latest"`. For GridGain images, changing the value triggers a rolling upgrade procedure. For Apache Ignite, the pods are deleted and re-created.

### number_of_nodes

The number of pods in the cluster, the default value is `2`.

### option_libs

Defines which modules should be included in the classpath at startup. 

Default value: `"ignite-kubernetes,ignite-rest-http,ignite-opencensus,control-center-agent"`

Please refer to [Enabling Modules](../installing-using-docker.md#enabling-modules) section for the details.

### jvm_opts

JVM arguments passed to the GridGain instance, with a default value of  `"-DIGNITE_WAL_MMAP=false -DIGNITE_WAIT_FOR_BACKUPS_ON_SHUTDOWN=true"`

Please refer to [Environment Variables](../installing-using-docker.md#environment-variables) section for the details.

### Storage Configuration

If `persistent` mode is in use, the following values are required. This requirement is ignored for in-memory cluster configuration. All values are in gigabytes:

- `work_volume_size`: 1, size of the work directory
- `pds_volume_size`: 1, size of the pds volume 
- `wal_volume_size`: 1, size of the WAL volume
- `wal_archive_volume_size`: 1, size of the WAL archive

Please refer to the [Configuration Properties](../../../architecture/storage/native-persistence.md#configuration-properties) section for details.

## IgniteConfig Resource

This custom resource is responsible for managing internal cluster configuration through the embedded XML configuration file. Please refer to [GridGain configuration docs](../../../gridgain8-usage/understanding-configuration.md) for details.

{% hint style="warning" %}
Changes in the custom resource trigger the operator reconciliation loop, and, as a result, the pods are re-created.
{% endhint %}

To create a resource, use the following command:

```shell
kubectl apply -f ignite_config.yaml
```

### Cluster Configuration

You can modify GridGain or Apache Ignite configuration by changing yaml's `gridgian_conf` section:

```yaml
apiVersion: gridgain.com/v1
kind: IgniteConfig
metadata:
  name: ignite-custom-config
spec:
  gridgian_conf: |-
          <?xml version="1.0" encoding="UTF-8"?>
          <beans xmlns="http://www.springframework.org/schema/beans"
                 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                 xsi:schemaLocation="
                  http://www.springframework.org/schema/beans
                  http://www.springframework.org/schema/beans/spring-beans.xsd">

              <bean class="org.apache.ignite.configuration.IgniteConfiguration">

                  <property name="workDirectory" value="/ignite/work"/>

                  <property name="dataStorageConfiguration">
                      <bean class="org.apache.ignite.configuration.DataStorageConfiguration">
                          <property name="defaultDataRegionConfiguration">
                              <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                                  <property name="persistenceEnabled" value="true"/>
                              </bean>
                          </property>
                          <property name="storagePath" value="/ignite/pds"/>
                          <property name="walPath" value="/ignite/wal"/>
                          <property name="walArchivePath" value="/ignite/walarchive"/>
                      </bean>

                  </property>

                  <property name="discoverySpi">
                      <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
                          <property name="ipFinder">
                              <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.kubernetes.TcpDiscoveryKubernetesIpFinder">
                                  <property name="namespace" value="<namespace>"/>
                                  <property name="serviceName" value="<cluster_name>-service"/>
                              </bean>
                          </property>
                      </bean>
                  </property>
              </bean>
          </beans>
```

The configuration above contains two placeholders — `<namespace>` and `<cluster_name>` — for k8s IP finder.  These placeholders are replaced with the `namespace` and `cluster_name` values of Ignite Custom Resource. See Custom Resources Configuration. for details.

### Licensing

If you use GridGain Enterprise or Ultimate edition, you can provide a license file with `license` parameter:

```
apiVersion: gridgain.com/v1
kind: IgniteConfig
metadata:
  name: ignite-custom-config
spec:
  gridgian_conf: |- <XML_CONFIG>

...

license: |-
            <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
              <gridgain-license version="2.1">
                  <id>a1aef789-9edc-41a6-b00d-e000a000e0a1</id>
                  <maintenance-time>0</maintenance-time>
                  <expire-date>01/01/2022</expire-date>
                  <max-nodes>10</max-nodes>
                  <max-cpus>80</max-cpus>
                  <max-computers>0</max-computers>
                  <grace-period>0</grace-period>
                  <max-uptime>0</max-uptime>
                  <signature>SIGN</signature>
                  <enabled-feature name="ultimate"/>
              </gridgain-license>
```

When applied, Gridgain Operator creates a `/opt/gridgain/gridgain-license.xml` file.

To provide a new license, replace the current license with the new one. Operator restarts your pods automatically.

### Init Container

To use an init container, add the appropriate definitions.

For example:

```
...
init_container_image: busybox
init_container_command: "'sh', '-c', echo \"hello there\""
...
```

The operator adjusts the K8 yaml config to include an init container when the init container image is in the custom resource.

{% hint style="info" %}
The init container command is optional.
{% endhint %}

## Cluster Termination

To remove the previously deployed cluster and clean resources, remove `Ignite` custom resource:

```shell
kubectl delete -f ignite.yaml -n <operator-namespace>
```

{% hint style="warning" %}
This action removes the entire [cluster namespace](#namespace) that might contain custom objects.
{% endhint %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
