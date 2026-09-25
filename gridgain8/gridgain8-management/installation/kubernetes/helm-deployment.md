---
description: >-
  How to deploy a GridGain cluster on Kubernetes using the GridGain Helm chart,
  including custom configuration, license, authentication, and volumes.
---

# Installing GridGain on Kubernetes using Helm Chart

Following is a step-by-step guide for deploying a GridGain cluster on Kubernetes using [Kubernetes Helm Chart](https://helm.sh/).

## Prerequisites

- Kubernetes cluster version 1.26 or more recent
- Helm version 3 or more recent
- PersistentVolume provisioner support in the persistence configuration

{% hint style="info" %}
Older versions of Kubernetes and Helm have not been tested; use at your own risk.
{% endhint %}

## Step 1: Add the Helm Repository

To add the Helm chart repository, run the following commands:

```bash
helm repo add gridgain https://gridgain.github.io/helm-charts/
helm repo update
```

## Step 2: Install the Helm Chart

To install the chart with the default configuration, use the following command:

```bash
helm install my-release gridgain/gridgain
```

This installs GridGain on your Kubernetes cluster.

## Step 3 (Optional): Customize Your Installation

You can customize the installation by providing a custom `values.yaml` file or using the `--set` options. Here is an example of providing custom values:

```bash
helm install my-release gridgain/gridgain -f values.yaml
```

Following are two common customizations.

### 3.1. Custom Configuration for GridGain

You can provide custom configuration for GridGain by passing configuration parameters in the `values.yaml` file.

{% code title="values.yaml" %}
```yaml
# Make default config from file null to provide custom config in plain text.
configMapsFromFile:
  default-config: null

configMaps:
  default-config:
    name: default-config.xml
    path: /opt/gridgain/config/default-config.xml
    subpath: default-config.xml
# Provide a custom GridGain config.
    content: |
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
                              <property name="namespace" value="{{ .Release.Namespace }}"/>
                              <property name="serviceName" value="{{ include "gridgain.fullname" . }}-headless"/>
                          </bean>
                      </property>
                  </bean>
              </property>
              <property name="dataStorageConfiguration">
                  <bean class="org.apache.ignite.configuration.DataStorageConfiguration">
                      <property name="defaultDataRegionConfiguration">
                          <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                              <property name="persistenceEnabled" value="true"/>
                          </bean>
                      </property>
                  </bean>
              </property>
          </bean>
      </beans>
```
{% endcode %}

### 3.2. Custom License

To install GridGain with a custom license, you can use the `license` key.

{% code title="values.yaml" %}
```yaml
license:
  mountPath: /opt/gridgain/gridgain-license.xml
  createSecret: 
    mountPath: /opt/gridgain/gridgain-license.xml
    # Paste your license content below
    content: |
      <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
      </gridgain-license>
```
{% endcode %}

### 3.3. Authentication Configuration

To configure authentication for GridGain, specify the `auth` section in the `values.yaml` file. Authentication may include usernames, passwords, and permissions.

{% code title="values.yaml" %}
```yaml
auth: 
  enabled: true
  users: 
    server: 
      name: server1
      password: password1
      permissions: "{defaultAllow:true}"
    client: 
      name: client2
      password: password2
      permissions: "{defaultAllow:false, {cache:'*',permissions:['CACHE_READ']}}"
    user: 
      name: user3
      password: password3
      permissions: "{defaultAllow:true}"
```
{% endcode %}

### 3.4. Volume Configuration

To configure persistent storage or attach custom volumes to GridGain, define the volume mounts and persistence settings in `values.yaml`.

{% hint style="warning" %}
Do not store the work directory, WAL, or WAL archive on NFS volumes. GridGain uses an OS-level advisory lock (`fcntl`) to prevent two nodes from sharing a persistence directory. On NFS volumes the lock is held by the server and survives the client for up to 30-90 seconds. Because Kubernetes restarts crashed pods inside that window, the restarting node cannot reacquire its own lock and the pod is stuck in `CrashLoopBackOff` until the server times out.
{% endhint %}

{% code title="values.yaml" %}
```yaml
persistence:
  volumes:
    wal:
      enabled: true
      mountPath: /wal
      size: 8Gi
      accessModes:
        - ReadWriteOnce
    persistence:
      enabled: true
      mountPath: /persistence
      size: 8Gi
      accessModes:
        - ReadWriteOnce
    snapshot:
      enabled: true
      mountPath: /snapshots
      size: 8Gi
      accessModes:
        - ReadWriteOnce

# Make default config from file null to provide custom config in plain text.
configMapsFromFile:
  default-config: null

configMaps:
  default-config:
    name: default-config.xml
    path: /opt/gridgain/config/default-config.xml
    subpath: default-config.xml
# Configure snapshots and wal.
    content: |
      <?xml version="1.0" encoding="UTF-8"?>

      <!--
          Copyright (C) GridGain Systems. All Rights Reserved.
          _________        _____ __________________        _____
          __  ____/___________(_)______  /__  ____/______ ____(_)_______
          _  / __  __  ___/__  / _  __  / _  / __  _  __ `/__  / __  __ \
          / /_/ /  _  /    _  /  / /_/ /  / /_/ /  / /_/ / _  /  _  / / /
          \____/   /_/     /_/   \_,__/   \____/   \__,_/  /_/   /_/ /_/
      -->

      <beans xmlns="http://www.springframework.org/schema/beans"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xmlns:util="http://www.springframework.org/schema/util"
              xsi:schemaLocation="
              http://www.springframework.org/schema/beans
              http://www.springframework.org/schema/beans/spring-beans.xsd
              http://www.springframework.org/schema/util
              http://www.springframework.org/schema/util/spring-util.xsd">
          <bean class="org.apache.ignite.configuration.IgniteConfiguration">
              <property name="authenticationEnabled" value="false"/>
              <property name="failureDetectionTimeout" value="10000"/>
              <property name="clientFailureDetectionTimeout" value="10000"/>
              <property name="networkTimeout" value="10000"/>

              <property name="gridLogger">
                  <bean class="org.apache.ignite.logger.log4j2.Log4J2Logger">
                      <constructor-arg type="java.lang.String" value="/opt/gridgain/config/ignite-log4j2.xml"/>
                  </bean>
              </property>
              <property name="communicationSpi">
                  <bean class="org.apache.ignite.spi.communication.tcp.TcpCommunicationSpi">
                      <!-- Sets socket write timeout for TCP connection. -->
                      <property name="socketWriteTimeout" value="10000"/>
                      <property name="messageQueueLimit"  value="1024"/>
                  </bean>
              </property>

              <property name="discoverySpi">
                  <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
                      <property name="ipFinder">
                          <!--
                              Enables Kubernetes IP finder and setting custom namespace and service names.
                          -->
                          <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.kubernetes.TcpDiscoveryKubernetesIpFinder">
                              <property name="namespace" value="{{ .Release.Namespace }}"/>
                              <property name="serviceName" value="{{ include "gridgain.fullname" . }}-headless"/>
                          </bean>
                      </property>
                  </bean>
              </property>

              <property name="transactionConfiguration">
                  <bean class="org.apache.ignite.configuration.TransactionConfiguration">
                      <property name="txTimeoutOnPartitionMapExchange" value="#{60L * 1000L}"/>
                      <property name="DefaultTxTimeout" value="20000"/>
                  </bean>
              </property>

              <property name="dataStorageConfiguration">
                  <bean class="org.apache.ignite.configuration.DataStorageConfiguration">
                      <property name="metricsEnabled" value="true"/>

                      <property name="storagePath" value="/persistence/db"/>

                      <!--property name="walMode" value="${wal_mode}"/-->
                      <property name="walPath" value="/wal"/>
                      <property name="walArchivePath" value="/wal"/>
                      <property name="walSegmentSize" value="#{512L * 1024 * 1024}"/>
                      <property name="maxWalArchiveSize" value="#{5L * 1024 * 1024 * 1024}"/>
                      <!-- Enable write throttling. -->
                      <property name="writeThrottlingEnabled" value="true"/>

                      <property name="defaultDataRegionConfiguration">
                          <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                              <property name="initialSize" value="#{1024L * 1024L * 1024L}"/>
                              <property name="maxSize" value="#{1600L * 1024L * 1024L}"/>
                              <property name="metricsEnabled" value="true"/>
                              <property name="persistenceEnabled" value="true"/>
                          </bean>
                      </property>
                      <property name="dataRegionConfigurations">
                      <list>
                          <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                              <property name="name" value="in-memory"/>
                              <property name="initialSize" value="#{10L * 1024 * 1024}"/>
                              <property name="maxSize" value="#{1024L * 1024L * 1024L}"/>
                              <property name="metricsEnabled" value="true"/>
                          </bean>
                      </list>
                      </property>
                  </bean>
              </property>

              <property name="pluginConfigurations">
                  <bean class="org.gridgain.grid.configuration.GridGainConfiguration">
                    <property name="rollingUpdatesEnabled" value="true"/>
                    <property name="snapshotConfiguration">
                      <bean class="org.gridgain.grid.configuration.SnapshotConfiguration">
                          <property name="snapshotsPath" value="/snapshots"/>
                      </bean>
                    </property>
                  </bean>
              </property>

              <property name="eventStorageSpi">
                  <bean class="org.apache.ignite.spi.eventstorage.memory.MemoryEventStorageSpi">
                  </bean>
              </property>

              <property name="workDirectory" value="/persistence/work"/>

              <property name="userAttributes">
                  <map>
                      <entry key="IGNITE_CLUSTER_NAME" value="{{ include "gridgain.fullname" . }}.{{ .Release.Namespace }}"/>
                  </map>
              </property>
          </bean>
      </beans>
```
{% endcode %}

## Updating Your Installation

To update GridGain with new values, run the following command:

```bash
helm upgrade my-release gridgain/gridgain -f values.yaml
```

## Uninstalling GridGain

To remove the installation from your Kubernetes cluster, use the following command:

```bash
helm uninstall my-release
```

## Getting Help

For more information about available options and values, refer to the [Helm chart documentation on Artifact Hub](https://artifacthub.io/packages/helm/gridgain/gridgain).

If you have questions or concerns, [open an issue](https://github.com/gridgain/helm-charts/issues) in our GitHub repository.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
