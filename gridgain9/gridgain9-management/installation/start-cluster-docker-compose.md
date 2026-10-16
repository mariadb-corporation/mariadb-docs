---
description: >-
  Start a 3-node Apache Ignite 3 or GridGain 9 cluster for development using Docker Compose.
---

# How to Start a Cluster With Docker Compose

## Prerequisites

- **Docker** 20.10 or later
- **Docker Compose** 2.23.1 or later (ships with Docker Desktop)
- **curl** and [**jq**](https://jqlang.github.io/jq/download/) for verifying cluster health
- **Ports 10300-10302 and 10800-10802** available on your machine
- **12 GB of available RAM** for three cluster nodes (4 GB minimum; see the memory note in Step 1)
- **GridGain 9 only:** A GridGain 9 license file. If you are interested in trying out GridGain 9, contact our support. Save the license file as `gridgain-license.json` in your project directory alongside `docker-compose.yml`.

## Overview

This guide walks you through starting a 3-node development cluster on your local machine with Docker Compose. By the end, you will have a running cluster that accepts client connections on ports 10800-10802 and exposes a REST management API on ports 10300-10302.

Both Apache Ignite 3 and GridGain 9 share the same distributed architecture and management interfaces. The Docker images, configuration paths, and license requirements differ between the two products, but the cluster lifecycle is the same: start nodes, initialize them into a cluster, then connect.

You have two tools for managing the cluster once the containers are running:

- **REST API** (port 10300) accepts HTTP requests for cluster initialization, health checks, and configuration. It is available as soon as a node starts, even before the cluster is initialized. Use this when you want scriptable, automatable management.
- **CLI tool** is an interactive command-line shell that communicates with the cluster through the REST API. It is bundled inside the server image, so you access it via `docker exec` on any running node. Use it for interactive sessions, SQL queries, or one-off administration. For a deeper walkthrough, see [How to Work with the Ignite CLI](../cli-tool-step-by-step.md).

Select your product version in the tabs below. Each step shows both management approaches where they differ.

## Create a Docker Compose File

Create a directory for your project and add a file named `docker-compose.yml` with the following content.

{% tabs %}
{% tab title="Apache Ignite 3" %}

{% code title="docker-compose.yml" %}
```yaml
name: ignite3

x-ignite-def: &ignite-def
  image: apacheignite/ignite:3.1.0
  environment:
    JVM_MAX_MEM: "4g"
    JVM_MIN_MEM: "4g"
  configs:
    - source: node_config
      target: /opt/ignite/etc/ignite-config.conf

services:
  node1:
    <<: *ignite-def
    container_name: ignite3-node1
    command: --node-name node1
    ports:
      - "10300:10300"
      - "10800:10800"

  node2:
    <<: *ignite-def
    container_name: ignite3-node2
    command: --node-name node2
    ports:
      - "10301:10300"
      - "10801:10800"
    depends_on:
      - node1

  node3:
    <<: *ignite-def
    container_name: ignite3-node3
    command: --node-name node3
    ports:
      - "10302:10300"
      - "10802:10800"
    depends_on:
      - node1
      - node2

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
{% endcode %}

The YAML anchor (`x-ignite-def`) keeps the node definitions consistent. Each node exposes two ports: **10300** for the REST management API and **10800** for client connections (JDBC, ODBC, and thin client drivers). The Ignite CLI is bundled inside the server image, so you access it via `docker exec` on any running node.

Port 3344 handles internal cluster communication between nodes. Docker's internal network routes this traffic, so you don't need to expose it to the host.

{% endtab %}

{% tab title="GridGain 9" %}

Ensure your `gridgain-license.json` file (from the prerequisites) is in the same directory where you create `docker-compose.yml`.

{% code title="docker-compose.yml" %}
```yaml
name: gridgain9

x-gridgain-def: &gridgain-def
  image: gridgain/gridgain9:latest
  environment:
    JVM_MAX_MEM: "4g"
    JVM_MIN_MEM: "4g"
  configs:
    - source: node_config
      target: /opt/gridgain/etc/gridgain-config.conf

services:
  node1:
    <<: *gridgain-def
    container_name: gridgain9-node1
    command: --node-name node1
    ports:
      - "10300:10300"
      - "10800:10800"

  node2:
    <<: *gridgain-def
    container_name: gridgain9-node2
    command: --node-name node2
    ports:
      - "10301:10300"
      - "10801:10800"
    depends_on:
      - node1

  node3:
    <<: *gridgain-def
    container_name: gridgain9-node3
    command: --node-name node3
    ports:
      - "10302:10300"
      - "10802:10800"
    depends_on:
      - node1
      - node2

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
{% endcode %}

The structure mirrors the Apache Ignite 3 compose file with two key differences: the image names use `gridgain/gridgain9`, and the node configuration mounts to `/opt/gridgain/etc/` instead of `/opt/ignite/etc/`. The GridGain CLI is bundled inside the server image at `/opt/gridgain9cli/bin/gridgain9`.

Port 3344 handles internal cluster communication between nodes. Docker's internal network routes this traffic, so you don't need to expose it to the host.

{% endtab %}

{% endtabs %}

{% hint style="info" %}
Reduce `JVM_MAX_MEM` and `JVM_MIN_MEM` to `1g` if your machine has less than 16 GB of RAM. Each node will use approximately 1 GB instead of 4 GB. Performance will be adequate for development and tutorial workloads.
{% endhint %}

## Start the Cluster

This command works for both Apache Ignite 3 and GridGain 9:

```bash
docker compose up -d
```

{% tabs %}
{% tab title="Apache Ignite 3" %}

Expected output:

```text
[+] Running 4/4
 ✔ Network ignite3_default  Created
 ✔ Container ignite3-node1  Started
 ✔ Container ignite3-node2  Started
 ✔ Container ignite3-node3  Started
```

{% endtab %}

{% tab title="GridGain 9" %}

Expected output:

```text
[+] Running 4/4
 ✔ Network gridgain9_default  Created
 ✔ Container gridgain9-node1  Started
 ✔ Container gridgain9-node2  Started
 ✔ Container gridgain9-node3  Started
```

{% endtab %}

{% endtabs %}

The nodes need a few seconds to discover each other over port 3344 and form a physical topology. Verify all three containers are running:

```bash
docker compose ps --format "table {{.Name}}\t{{.Image}}\t{{.Status}}"
```

{% tabs %}
{% tab title="Apache Ignite 3" %}

Expected output:

```text
NAME            IMAGE                          STATUS
ignite3-node1   apacheignite/ignite:3.1.0      Up 30 seconds
ignite3-node2   apacheignite/ignite:3.1.0      Up 29 seconds
ignite3-node3   apacheignite/ignite:3.1.0      Up 28 seconds
```

{% endtab %}

{% tab title="GridGain 9" %}

Expected output:

```text
NAME              IMAGE                        STATUS
gridgain9-node1   gridgain/gridgain9:latest     Up 30 seconds
gridgain9-node2   gridgain/gridgain9:latest     Up 29 seconds
gridgain9-node3   gridgain/gridgain9:latest     Up 28 seconds
```

{% endtab %}

{% endtabs %}

{% hint style="success" %}
**Checkpoint:** All three containers show `Up` status. If any container shows `Restarting` or `Exited`, see [Troubleshooting](#troubleshooting).
{% endhint %}

## Initialize the Cluster

At this point, the nodes are running and can see each other, but they are not yet a cluster. Initialization is a one-time step that elects a leader, designates which nodes store cluster metadata, and opens client connection ports (10800). Until you initialize, the REST API on port 10300 is the only way to interact with the nodes.

Choose your preferred management tool below. Both accomplish the same result.

{% tabs %}
{% tab title="REST API: Apache Ignite 3" %}

Send the initialization request to any node's REST endpoint. The REST API is available on all three nodes (ports 10300, 10301, 10302), but you only need to send the init request once.

```bash
curl -X POST http://localhost:10300/management/v1/cluster/init \
  -H "Content-Type: application/json" \
  -d '{
    "metaStorageNodes": ["node1", "node2", "node3"],
    "cmgNodes": ["node1", "node2", "node3"],
    "clusterName": "my-cluster"
  }'
```

A successful initialization returns HTTP 200 with an empty response body.

{% endtab %}

{% tab title="REST API: GridGain 9" %}

Send the initialization request to any node's REST endpoint. The REST API is available on all three nodes (ports 10300, 10301, 10302), but you only need to send the init request once.

GridGain 9 requires the license content in the init request. Load the license file into a shell variable first. `jq -Rs` reads the file and encodes it as a JSON string with proper escaping:

```bash
LICENSE=$(jq -Rs . gridgain-license.json)
```

Initialize the cluster with the license:

```bash
curl -X POST http://localhost:10300/management/v1/cluster/init \
  -H "Content-Type: application/json" \
  -d '{"metaStorageNodes":["node1","node2","node3"],"cmgNodes":["node1","node2","node3"],"clusterName":"my-cluster","license":'"$LICENSE"'}'
```

A successful initialization returns HTTP 200 with an empty response body.

{% endtab %}

{% tab title="CLI: Apache Ignite 3" %}

Open the CLI inside a running node with `docker exec`. The CLI is bundled in the server image.

```bash
docker exec -it ignite3-node1 /opt/ignite3cli/bin/ignite3
```

At the CLI prompt, connect to the local node and initialize:

```text
connect http://localhost:10300
cluster init --name=my-cluster --metastorage-group=node1,node2,node3
```

Expected output:

```text
Connected to http://localhost:10300
Cluster was initialized successfully
```

Type `exit;` to leave the CLI.

{% endtab %}

{% tab title="CLI: GridGain 9" %}

Open the CLI inside a running node with `docker exec`. The CLI is bundled in the server image.

First, copy the license file into the container:

```bash
docker cp gridgain-license.json gridgain9-node1:/opt/gridgain9cli/license.json
```

Then open the CLI:

```bash
docker exec -it gridgain9-node1 /opt/gridgain9cli/bin/gridgain9
```

At the CLI prompt, connect to the local node and initialize with the license file:

```text
connect http://localhost:10300
cluster init --name=my-cluster --metastorage-group=node1,node2,node3 --license=/opt/gridgain9cli/license.json
```

Expected output:

```text
Connected to http://localhost:10300
Cluster was initialized successfully
```

Type `exit;` to leave the CLI.

{% endtab %}

{% endtabs %}

Allow a few seconds for the nodes to elect a leader and synchronize metadata before verifying.

{% hint style="success" %}
**Checkpoint:** Initialization completes without errors. If the command hangs or returns a connection error, wait 30-60 seconds for the nodes to finish starting, then retry.
{% endhint %}

## Verify Cluster Health

Once the cluster is initialized, confirm that all three nodes joined successfully. This verification works the same way for both Apache Ignite 3 and GridGain 9.

{% tabs %}
{% tab title="REST API: Apache Ignite 3" %}

```bash
curl -s http://localhost:10300/management/v1/cluster/state | jq .
```

Expected output:

```json
{
  "cmgNodes": ["node1", "node2", "node3"],
  "msNodes": ["node1", "node2", "node3"],
  "igniteVersion": "3.1.0",
  "clusterTag": {
    "clusterName": "my-cluster",
    "clusterId": "..."
  }
}
```

Both `cmgNodes` (cluster management group) and `msNodes` (metastorage nodes) should list all three nodes. The `igniteVersion` field reflects the product version.

{% hint style="success" %}
**Checkpoint:** Both `cmgNodes` and `msNodes` list all three nodes, confirming the cluster is healthy and accepting client connections on port 10800.
{% endhint %}

{% endtab %}

{% tab title="REST API: GridGain 9" %}

```bash
curl -s http://localhost:10300/management/v1/cluster/state | jq .
```

Expected output:

```json
{
  "cmgNodes": ["node1", "node2", "node3"],
  "msNodes": ["node1", "node2", "node3"],
  "igniteVersion": "latest GridGain 9 version",
  "clusterTag": {
    "clusterName": "my-cluster",
    "clusterId": "..."
  }
}
```

Both `cmgNodes` (cluster management group) and `msNodes` (metastorage nodes) should list all three nodes. The `igniteVersion` field reflects the product version.

{% hint style="success" %}
**Checkpoint:** Both `cmgNodes` and `msNodes` list all three nodes, confirming the cluster is healthy and accepting client connections on port 10800.
{% endhint %}

{% endtab %}

{% tab title="CLI: Apache Ignite 3" %}

```bash
docker exec -it ignite3-node1 /opt/ignite3cli/bin/ignite3
```

At the CLI prompt:

```text
connect http://localhost:10300
cluster status
```

Expected output:

```text
Connected to http://localhost:10300
[name: my-cluster, nodes: 3, status: active, cmgNodes: [node1, node2, node3], msNodes: [node1, node2, node3]]
```

For a detailed node list, use:

```text
cluster topology physical
```

This lists all nodes with their names, addresses, and IDs.

Type `exit;` to leave the CLI.

{% hint style="success" %}
**Checkpoint:** The `cluster status` command shows 3 nodes in active status. All nodes are in the CMG and MetaStorage groups.
{% endhint %}

{% endtab %}

{% tab title="CLI: GridGain 9" %}

```bash
docker exec -it gridgain9-node1 /opt/gridgain9cli/bin/gridgain9
```

At the CLI prompt:

```text
connect http://localhost:10300
cluster status
```

Expected output:

```text
Connected to http://localhost:10300
[name: my-cluster, nodes: 3, status: active, cmgNodes: [node1, node2, node3], msNodes: [node1, node2, node3]]
```

For a detailed node list, use:

```text
cluster topology physical
```

This lists all nodes with their names, addresses, and IDs.

Type `exit;` to leave the CLI.

{% hint style="success" %}
**Checkpoint:** The `cluster status` command shows 3 nodes in active status. All nodes are in the CMG and MetaStorage groups.
{% endhint %}

{% endtab %}

{% endtabs %}

## Stopping and Restarting

All Docker Compose lifecycle commands work identically for both Apache Ignite 3 and GridGain 9.

**Stop the cluster (preserves data):**

```bash
docker compose stop
```

This stops the containers without removing them. Data, cluster state, and initialization all persist.

**Restart a stopped cluster:**

```bash
docker compose up -d
```

The nodes rejoin the existing cluster automatically. You do not need to re-initialize. Client connections on port 10800 become available once the nodes finish starting (typically 15-30 seconds). This same command also works after `docker compose down` to create a fresh cluster (which will require re-initialization).

**Remove the cluster (destroys data):**

```bash
docker compose down
```

This removes all containers and the default network, destroying all data. The next `docker compose up -d` starts a fresh cluster that requires re-initialization.

**Remove the cluster and all volumes:**

```bash
docker compose down -v
```

This also removes named volumes for a completely clean state.

## Troubleshooting

These issues apply to both Apache Ignite 3 and GridGain 9 unless noted otherwise.

<details>

<summary>Port conflict on startup</summary>

`docker compose up -d` fails with `Bind for 0.0.0.0:10300 failed: port is already allocated`.

Another process is using one of the required ports. Identify it:

```bash
lsof -i :10300
```

Stop the conflicting process, or change the host port mapping in `docker-compose.yml`. For example, map to port 10400 instead:

```yaml
ports:
  - "10400:10300"
```

Adjust all subsequent commands to use the new port number.

</details>

<details>

<summary>Initialization timeout</summary>

The `curl` command to `/management/v1/cluster/init` hangs or returns `connection refused`.

The nodes are not ready yet. Check that all containers are running:

```bash
docker compose ps
```

If a container shows `Restarting` or `Exited`, check its logs:

```bash
docker compose logs node1
```

Wait for the REST API to become available (30-60 seconds after startup):

```bash
curl -sf http://localhost:10300/management/v1/node/state
```

When this returns a JSON response, the node is ready for initialization.

</details>

<details>

<summary>Fewer than 3 nodes in cluster state</summary>

`/management/v1/cluster/state` shows fewer than 3 nodes in `cmgNodes` or `msNodes`.

The cluster was initialized before all nodes discovered each other. In a development environment, the safest fix is to start over:

```bash
docker compose down
docker compose up -d
```

Wait 30-60 seconds for all nodes to discover each other, then re-initialize.

</details>

<details>

<summary>Client connection refused on port 10800</summary>

An application connecting to `localhost:10800` gets `Connection refused` after the containers are running.

Client ports open only after cluster initialization. Verify the cluster is initialized:

```bash
curl -s http://localhost:10300/management/v1/cluster/state | jq .clusterTag.clusterName
```

If this returns `null` or an error, the cluster has not been initialized. Complete the Initialize the Cluster step above.

</details>

<details>

<summary>GridGain 9: License error during REST API initialization</summary>

**GridGain 9 only.** The REST API returns HTTP 400 with a message about a missing or invalid license.

Verify that `gridgain-license.json` exists in the same directory as `docker-compose.yml`:

```bash
ls -la gridgain-license.json
```

Verify the file contains valid JSON:

```bash
cat gridgain-license.json | jq .
```

The `license` field in the curl command must be a JSON-encoded string of the file contents, not the filename. Use `LICENSE=$(jq -Rs . gridgain-license.json)` to load the license into a variable as shown in the initialization step.

</details>

<details>

<summary>GridGain 9: License error during CLI initialization</summary>

**GridGain 9 only.** The CLI returns an error about a missing license when running `cluster init`.

Verify the license file was copied into the container:

```bash
docker exec gridgain9-node1 cat /opt/gridgain9cli/license.json | head -1
```

If the file is missing, copy it again:

```bash
docker cp gridgain-license.json gridgain9-node1:/opt/gridgain9cli/license.json
```

Use the `--license=/opt/gridgain9cli/license.json` flag with the `cluster init` command.

</details>

Your cluster is now accepting client connections on ports 10800-10802. You can connect with any Ignite thin client driver, JDBC (`jdbc:ignite:thin://localhost:10800`), or ODBC.

## Related

- [How to Manage Cluster Lifecycle with the REST API](../manage-cluster-lifecycle-rest-api.md) - Monitor startup, initialize, and verify cluster health using REST endpoints.

- [Start Your Local Ignite 3 Development Cluster](../../gridgain9-tutorials/distributed-sql-foundations/start-local-cluster.md) - Tutorial that walks through this setup with deeper context, loads the Music Store dataset, and introduces cluster concepts.
- [How to Work with the Ignite CLI](../cli-tool-step-by-step.md) - Interactive SQL, cluster inspection, output formatting, and profiles.
