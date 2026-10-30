---
description: >-
  Set up a single-node GridGain 8 cluster with Docker Compose for cache-centric development and testing.
---

# Start a Local Cache Development Cluster

<!-- TODO (release): the Docker Hub tag with the plain version 8.10.0 does not exist yet (no 8.10.0 image is published yet); this page uses the placeholder tag 8.10.0; the version strings in the sample output and the download file name are placeholders; re-capture them from the released build. After the 8.10.0 release, check that each of these resolves, update this page if the final names differ, and delete this comment. -->

<!-- TODO (release): no official 8.10.0 image is published yet, so whether the `platform: linux/amd64` pin is still needed was not tested. This page keeps the amd64 wording and the pin as originally written. After the 8.10.0 release, check the architectures of the final tag and decide whether to drop the pin and the emulation notes here and in the other tutorials that use `platform: linux/amd64`. -->

## Introduction

Your application needs a fast caching layer. In this tutorial, you start a single-node cluster with Docker Compose and verify it is running. Every subsequent tutorial in the cache-centric Foundations path builds on this environment.

The cache-centric architecture is used by GridGain 8. It organizes server nodes in a ring topology with no minimum node count.

A single server node is all you need to start developing. Later tutorials add nodes when you explore partition distribution and resilience.

## Prerequisites

- **Docker** 20.10 or later
- **Docker Compose** 2.23.1 or later (ships with Docker Desktop)
- **Port 47500** available on your machine (cluster discovery)
- **Port 10800** available on your machine (client connections)
- **2 GB of available RAM** for the server node

GridGain 8 Enterprise requires a trial license:

1. Go to [gridgain.com/tryfree](https://www.gridgain.com/tryfree) and request an Enterprise trial download
2. Check your email for a download link to `gridgain-enterprise-8.10.0.zip`
3. Download and extract the zip file
4. Copy `gridgain-license.xml` from the top level of the extracted directory into your project directory (you create this directory in Step 1)

The trial license is valid for 30 days. The 1.1 GB zip contains the full binary distribution, but only the license file is needed for Docker.

{% hint style="info" %}
The GridGain 8 Docker images are **amd64 only**. Docker Desktop runs them under Rosetta 2 emulation. Startup takes longer than native images, and JVM performance is reduced. This is an emulation artifact, not a product limitation.
{% endhint %}

## What You Will Learn

A running single-node cluster verified through its startup log and a cluster state check. You will:

- Start a cache-centric cluster node with Docker Compose
- Read the topology snapshot log to confirm the node is active
- Run a cluster state check to verify connectivity

## Create the Docker Compose Environment

Create a project directory and the configuration files. The cluster needs a `docker-compose.yml` for the server container and an XML configuration for node discovery.

```bash
mkdir cache-cluster
```

Create the XML configuration file that configures static IP discovery. Save this as `cache-cluster/ignite-config.xml`:

{% code title="ignite-config.xml" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
       http://www.springframework.org/schema/beans
       http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean class="org.apache.ignite.configuration.IgniteConfiguration">

        <!-- Static IP discovery (no multicast) -->
        <property name="discoverySpi">
            <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
                <property name="ipFinder">
                    <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                        <property name="addresses">
                            <list>
                                <value>node1:47500</value>
                            </list>
                        </property>
                    </bean>
                </property>
            </bean>
        </property>

        <!-- Inter-node communication port -->
        <property name="communicationSpi">
            <bean class="org.apache.ignite.spi.communication.tcp.TcpCommunicationSpi">
                <property name="localPort" value="47100"/>
            </bean>
        </property>

        <!-- Allow the server to load classes defined on the client -->
        <property name="peerClassLoadingEnabled" value="true"/>

    </bean>

</beans>
```
{% endcode %}

The `TcpDiscoveryVmIpFinder` configures static IP discovery. In a Docker network, `node1` resolves to the container's IP address.

The `peerClassLoadingEnabled` flag has to match on every node in the cluster, server and client. Later tutorials in this path ship user-defined classes (cache configurations, compute tasks) from the client to the server, which requires the flag set to `true`. Setting it now avoids restarting the cluster with a new config when you reach those tutorials. A client that connects with a different value fails immediately with `Remote node has peer class loading enabled flag different from local`.

Now create the Docker Compose file. Save this as `cache-cluster/docker-compose.yml`:

{% code title="docker-compose.yml" %}
```yaml
name: gridgain8

services:
  node1:
    image: gridgain/enterprise:8.10.0
    platform: linux/amd64
    container_name: gridgain8-node1
    environment:
      CONFIG_URI: /config/ignite-config.xml
      JVM_OPTS: "-Xms1g -Xmx1g"
    volumes:
      - ./ignite-config.xml:/config/ignite-config.xml:ro
      - ./gridgain-license.xml:/opt/gridgain/gridgain-license.xml:ro
    ports:
      - "47500:47500"
      - "10800:10800"
```
{% endcode %}

The additional volume mount maps your trial license into the container at the path GridGain expects. Verify the license file is in your project directory before starting:

```bash
ls cache-cluster/gridgain-license.xml
```

Your project directory should now contain:

```text
cache-cluster/
  docker-compose.yml
  ignite-config.xml
  gridgain-license.xml
```

{% hint style="success" %}
**Checkpoint:** Your project directory contains the Docker Compose file and the XML configuration (plus the license file for GridGain 8).
{% endhint %}

## Start the Cluster

Start the server node in detached mode and follow the logs:

```bash
docker compose -f cache-cluster/docker-compose.yml up -d
docker compose -f cache-cluster/docker-compose.yml logs -f
```

The node takes 10-30 seconds to start (longer on Apple Silicon due to emulation). Watch for the banner and the topology snapshot:

```text
>>>    __________  ________________
>>>   /  _/ ___/ |/ /  _/_  __/ __/
>>>  _/ // (7 7    // /  / / / _/
>>> /___/\___/_/|_/___/ /_/ /___/
>>>
>>> ver. 8.10.0#...
>>> 2026 Copyright(C) GridGain Systems, Inc. and Contributors
...
[2026-10-22T13:37:02.862][INFO][main][GridEntLicenseProcessor] License successfully loaded from file: file:/opt/gridgain/gridgain-license.xml
[2026-10-22T13:37:02.862][INFO][main][GridEntLicenseProcessor] License [ID=..., type=ENT]
...
[2026-10-22T13:37:03.375][INFO][main][GridDiscoveryManager] Topology snapshot [ver=1, locNode=38d4ef2b, servers=1, clients=0, state=ACTIVE, CPUs=10, offheap=1.5GB, heap=1.0GB, ...]
```

The key line is the **topology snapshot**. It confirms:

- `servers=1` means one server node is active
- `clients=0` means no client applications have connected yet (you add one in a later tutorial)
- `state=ACTIVE` means the cluster is ready to accept operations

Press `Ctrl+C` to stop following the logs. The container continues running in the background.

{% hint style="success" %}
**Checkpoint:** The topology snapshot shows servers=1, clients=0, state=ACTIVE.
{% endhint %}

## Verify the Cluster is Active

Run a cluster state check to confirm the node is accepting connections:

```bash
docker exec gridgain8-node1 /opt/gridgain/bin/control.sh --state
```

```text
Control utility [ver. 8.10.0#...]
2026 Copyright(C) GridGain Systems, Inc. and Contributors
User: gridgain
Time: 2026-10-22T13:38:06.958
Command [STATE] started
Arguments: --state
--------------------------------------------------------------------------------
Cluster  ID: aedbd25b-247d-43f9-b585-c08c519dd53b
Cluster tag: strange_kepler
--------------------------------------------------------------------------------
Cluster is active
Command [STATE] finished with code: 0
Control utility has completed execution at: 2026-10-22T13:38:07.051
Execution time: 92 ms
```

The output confirms `Cluster is active`. The cluster ID and tag are auto-generated and will differ on your machine.

{% hint style="info" %}
You may see a line that reads `JVM_OPTS environment variable is set, but will not be used. To pass JVM options use CONTROL_JVM_OPTS`. This is cosmetic. The `control.sh` utility runs its own JVM separate from the server. The warning is safe to ignore.
{% endhint %}

{% hint style="success" %}
**Checkpoint:** The control utility reports "Cluster is active" with exit code 0.
{% endhint %}

## Why One Node?

Starting with one node gives you the fastest possible setup. Later tutorials add server nodes when you explore partition distribution and what happens when a node leaves the cluster.

## Managing the Cluster

To stop the cluster and preserve its state for next time:

```bash
docker compose -f cache-cluster/docker-compose.yml stop
```

To restart:

```bash
docker compose -f cache-cluster/docker-compose.yml start
```

To destroy the cluster and remove all data:

```bash
docker compose -f cache-cluster/docker-compose.yml down
```

{% hint style="info" %}
The cluster runs in-memory with no persistence configured. Stopping the container preserves the JVM state, but destroying the container (`down`) removes all cached data. Persistence configuration is covered in a later tutorial.
{% endhint %}

## Summary

You started a single-node cache-centric cluster with Docker Compose and verified it is active. The server node is listening on port 47500 (discovery) and port 10800 (client connections).

## Next Step

In **Cache Data and Experience the Speed**, you connect a Java application as a thick client, create caches, and store your first data. The thick client joins the cluster ring and enables features like near-cache that are unique to the cache-centric architecture.
