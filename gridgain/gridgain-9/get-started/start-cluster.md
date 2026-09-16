---
description: >-
  Set up and run a three-node GridGain 9 cluster using Docker containers, then
  initialize and verify it.
---

# How to Start a GridGain 9 Cluster in Docker

This guide walks you through the process of setting up and running a GridGain 9 cluster using Docker containers. Follow these steps to get a three-node cluster up and running quickly.

## Prerequisites

- Up-to-date Docker and Docker Compose installed on your system
- Basic familiarity with command-line operations
- The code editor of your choice (VS Code, IntelliJ IDEA, etc.)

## Step 1: Create a Docker-Compose Configuration

1. Download [`docker-compose.yml`](../../.gitbook/assets/gg9-quick-start-docker-compose.yml) file or create a file in your project directory:

```yaml
#  Copyright (C) GridGain Systems. All Rights Reserved.
#  _________        _____ __________________        _____
#  __  ____/___________(_)______  /__  ____/______ ____(_)_______
#  _  / __  __  ___/__  / _  __  / _  / __  _  __ `/__  / __  __ \
#  / /_/ /  _  /    _  /  / /_/ /  / /_/ /  / /_/ / _  /  _  / / /
#  \____/   /_/     /_/   \_,__/   \____/   \__,_/  /_/   /_/ /_/

name: gridgain9

x-gridgain-def: &gridgain-def
  image: gridgain/gridgain9:9.1
  environment:
    JVM_MAX_MEM: "4g"
    JVM_MIN_MEM: "4g"
    BOOTSTRAP_NODE_CONFIG: /opt/gridgain/etc/gridgain-config.conf
  configs:
    - source: node_config
      target: /opt/gridgain/etc/gridgain-config.conf
      mode: 0644

services:
  node1:
    <<: *gridgain-def
    command: --node-name node1
    ports:
      - "10300:10300"
      - "10800:10800"
  node2:
    <<: *gridgain-def
    command: --node-name node2
    ports:
      - "10301:10300"
      - "10801:10800"
  node3:
    <<: *gridgain-def
    command: --node-name node3
    ports:
      - "10302:10300"
      - "10802:10800"

configs:
  node_config:
    content: |
      ignite {
        network {
          port: 3344
          nodeFinder.netClusterNodes = ["node1:3344", "node2:3344", "node3:3344"]
        }
      }
```

{% hint style="info" %}
This `docker-compose` file will always launch the latest version of GridGain 9. Do you want to run a specific version of GridGain from [Docker Hub](https://hub.docker.com/r/gridgain/gridgain9/tags)?

GridGain 9 images are available for multiple JDK versions. The default tag uses **JDK 25**. To use a different JDK, append the variant suffix: `9.1-openjdk21` for JDK 21, `9.1-openjdk17` for JDK 17, or `9.1-openjdk26` for JDK 26 (STS, supported until the next STS release).

Set the `GRIDGAIN9_VERSION` variable in your environment to a specific version tag.

```bash
export GRIDGAIN9_VERSION=9.1
```

Alternatively, you can set the version tag using a `.env` file located in the same directory as the `docker-compose.yml` file.

```bash
echo GRIDGAIN9_VERSION=9.1 > .env
```
{% endhint %}

Then download the Docker image:

```bash
docker pull gridgain/gridgain9:9.1
```

## Step 2: Start the Ignite Cluster

1. Open a terminal in the directory containing your `docker-compose.yml` file
2. Run the following command to start the cluster:

```bash
docker compose up -d
```

3. Verify that all containers are running:

```bash
docker compose ps
```

Here is how the command output may look:

```
NAME                IMAGE                       COMMAND                  SERVICE   CREATED          STATUS         PORTS
gridgain9-node1-1   gridgain/gridgain9:9.1   "docker-entrypoint.s…"   node1     13 seconds ago   Up 9 seconds   0.0.0.0:10300->10300/tcp, 3344/tcp, 0.0.0.0:10800->10800/tcp
gridgain9-node2-1   gridgain/gridgain9:9.1   "docker-entrypoint.s…"   node2     13 seconds ago   Up 9 seconds   3344/tcp, 0.0.0.0:10301->10300/tcp, 0.0.0.0:10801->10800/tcp
gridgain9-node3-1   gridgain/gridgain9:9.1   "docker-entrypoint.s…"   node3     13 seconds ago   Up 9 seconds   3344/tcp, 0.0.0.0:10302->10300/tcp, 0.0.0.0:10802->10800/tcp
```

Your nodes are now running, but the cluster is not initialized.

## Step 3: Initialize the Cluster

{% hint style="info" %}
You need an active GridGain license to complete this step. Get a free trial license for Enterprise edition from the [GridGain website](https://www.gridgain.com/tryfree).
{% endhint %}

1. Copy your license file into your project directory.
2. Start the Ignite CLI in Docker:

```
docker run --rm -it --network=host -v /opt/etc/license.json:/opt/gridgain/etc/license.json gridgain/gridgain9:9.1 cli
```

{% hint style="info" %}
Update the `docker` command above to match the full path to the license file you received but leave the mounted name set to `license.json`.
{% endhint %}

3. Inside the CLI, connect to one of the nodes:

```bash
connect http://localhost:10300
```

4. Confirm the connection to the default node in the CLI tool.
5. Initialize the cluster with a name and license:

```bash
cluster init --name=GridGain --license=/opt/gridgain/etc/license.json
```

{% hint style="info" %}
The cluster name can be changed after initialization by using the [`cluster rename`](../ignite-cli-tool.md#cluster-rename) CLI command or the [`cluster/rename`](../developers-guide/rest/rest-api.md#using-http-tools) REST endpoint.
{% endhint %}

The output from this step should be similar to this:

```
  _________        _____ __________________        _____
  __  ____/___________(_)______  /__  ____/______ ____(_)_______
  _  / __  __  ___/__  / _  __  / _  / __  _  __ `/__  / __  __ \
  / /_/ /  _  /    _  /  / /_/ /  / /_/ /  / /_/ / _  /  _  / / /
  \____/   /_/     /_/   \_,__/   \____/   \__,_/  /_/   /_/ /_/
                      GridGain CLI version 9.1


You appear to have not connected to any node yet. Do you want to connect to the default node http://localhost:10300? [Y/n] 
Connected to http://localhost:10300
The cluster is not initialized. Run cluster init command to initialize it.
[node1]> cluster init --name=GridGain --license=/opt/gridgain/etc/license.json
Cluster was initialized successfully
[node1]> 
```

## Step 4: Verify Your Cluster

1. Use the `cluster status` CLI command to verify your cluster is running correctly.

```bash
cluster status
```

The output should look similar to this:

```
[name: GridGain, nodes: 3, status: active, cmgNodes: [node1, node2, node3], msNodes: [node1, node2, node3]]
```

This means that all 3 nodes found each other and formed an active cluster.

2. Exit the CLI by typing `exit` or pressing Ctrl+D. This will also stop the CLI container.

Congratulations! You have a local GridGain 9 cluster running that you can use for development.

## Understanding Port Configuration

The `docker-compose` file exposes two types of ports for each node:

- **10300-10302**: REST API ports for administrative operations;
- **10800-10802**: Client connection ports for your applications.

## Configuring Logs

### Default Setup

By default, GridGain logs are written to the Docker container's runtime output, meaning they are tied to the container's lifecycle. These logs are *not persistent* as they are managed by the Docker and will be lost if the container is removed.

Use the `docker logs` command to access the logs:

```bash
docker logs <container-id>
```

### Custom Setup

To make logs *persistent* and redirect them to a file on the host system, follow these steps:

1. Use the [preconfigured file](../../.gitbook/assets/gg9-get-started-gridgain.java.util.logging.properties) or create a new one and place it on the host system. Set a file path for the log output inside the container:

```bash
handlers=java.util.logging.FileHandler
java.util.logging.FileHandler.pattern=/gridgain/log/gridgain.log
java.util.logging.FileHandler.append=true
java.util.logging.FileHandler.limit=10000000
java.util.logging.FileHandler.count=5
```

Make sure that `java.util.logging.FileHandler.pattern` specifies the full file path for the log file inside the container. It should match the mounted volume path (`/gridgain/log`) defined in *step 2*.

2. Run the container with volume mounts to bind the log output directory and the config file to the host system:

```bash
docker run \
  -v /host/logs:/gridgain/log \
  -v /host/logging.properties:/gridgain/config/logging.properties \
  -e GRIDGAIN9_EXTRA_JVM_ARGS="-Djava.util.logging.config.file=/gridgain/config/logging.properties" \
  gridgain/gridgain9:9.1
```

3. After the container starts, verify that the log file is created on the host:

```bash
/host/logs/gridgain.log
```

## Stopping the Cluster

If you want to pause your cluster:

```bash
docker compose stop

[+] Stopping 3/3
 ✔ Container gridgain9-node1-1  Stopped
 ✔ Container gridgain9-node3-1  Stopped
 ✔ Container gridgain9-node2-1  Stopped
```

This will stop the containers and retain your data.

## Removing the Cluster

When you are done working with the cluster, you can remove it using:

```bash
docker compose down

[+] Running 4/4
 ✔ Container gridgain9-node3-1  Removed
 ✔ Container gridgain9-node1-1  Removed
 ✔ Container gridgain9-node2-1  Removed
 ✔ Network gridgain9_default    Removed
```

This will stop and remove all the containers. Your data will be lost unless you have configured persistent storage.
