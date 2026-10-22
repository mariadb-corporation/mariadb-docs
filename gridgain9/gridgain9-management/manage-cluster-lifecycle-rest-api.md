---
description: >-
  Monitor node startup, initialize a cluster, and verify health using REST endpoints on GridGain 9.
---

# How to Manage Cluster Lifecycle With the REST API

## Prerequisites

- A running 3-node cluster from [How to Start a Cluster with Docker Compose](installation/start-cluster-docker-compose.md)
- **curl** and [**jq**](https://jqlang.github.io/jq/download/) for JSON parsing
- **Ports 10300-10302** accessible on your machine

## Overview

Every GridGain 9 node exposes a REST management API on port 10300. The API is available as soon as the node's HTTP server starts, before the cluster is initialized. This guide walks through each REST endpoint in the order you use them during startup: check node state, verify discovery, initialize the cluster, and confirm health. Both products share the same REST API paths and response formats. The differences are the license field in the GridGain 9 initialization request and the product name and version number in the version response.

Use this guide when you need scriptable cluster management, want to diagnose startup issues, or are building automation around cluster lifecycle.

{% hint style="info" %}
If you completed [How to Start a Cluster with Docker Compose](installation/start-cluster-docker-compose.md) and your cluster is already running, every step in this guide still works. You will see `"state": "STARTED"` instead of `"STARTING"` in Steps 1-3, and the initialization request in Step 4 returns 200 OK as a safe no-op. No need to tear down and rebuild. Follow along as-is to learn the REST endpoints.
{% endhint %}

## Check Node State

Query the node state endpoint to confirm the REST API is reachable. This is the most reliable boot indicator across all product versions.

```bash
curl -s http://localhost:10300/management/v1/node/state | jq .
```

Expected response (before initialization):

```json
{
  "name": "node1",
  "state": "STARTING"
}
```

A node reports one of three states:

| State | Meaning |
|-------|---------|
| `STARTING` | The node process is running but has not joined a cluster |
| `STARTED` | The node has joined a cluster and is fully operational |
| `STOPPING` | The node is shutting down |

The REST server starts partway through the boot sequence, before all components are ready. If the connection is refused, the HTTP server has not started yet. Retry after a few seconds.

`STARTING` is expected at this point. It confirms the node is running and ready for further interaction.

{% hint style="success" %}
**Checkpoint:** The endpoint returns `200 OK` with `"state": "STARTING"`. If the connection is refused, the node is still booting. Retry after 3-5 seconds.
{% endhint %}

## Verify Node Identity and Version

Confirm you are talking to the expected node and check the product version.

```bash
curl -s http://localhost:10300/management/v1/node/info | jq .
```

Expected response:

```json
{
  "name": "node1",
  "jdbcPort": 10800
}
```

Check the product version:

```bash
curl -s http://localhost:10300/management/v1/node/version | jq .
```

```json
{
  "version": "<latest GridGain 9 version>",
  "product": "GridGain",
  "revision": "<revision>"
}
```

## Confirm Node Discovery

Before initializing, verify that all nodes have discovered each other through the internal cluster network.

```bash
curl -s http://localhost:10300/management/v1/cluster/topology/physical | jq .
```

Expected response (abbreviated):

```json
[
  {
    "name": "node1",
    "address": {
      "host": "172.18.0.2",
      "port": 3344
    },
    "metadata": {
      "restHost": "172.18.0.2",
      "httpPort": 10300,
      "httpsPort": -1
    }
  },
  {
    "name": "node2",
    "address": {
      "host": "172.18.0.3",
      "port": 3344
    },
    "metadata": {
      "restHost": "172.18.0.3",
      "httpPort": 10300,
      "httpsPort": -1
    }
  },
  {
    "name": "node3",
    "address": {
      "host": "172.18.0.4",
      "port": 3344
    },
    "metadata": {
      "restHost": "172.18.0.4",
      "httpPort": 10300,
      "httpsPort": -1
    }
  }
]
```

The physical topology lists every node that has announced itself over port 3344, regardless of whether a cluster has been initialized. Each entry includes the node's `name` (persistent across restarts), internal communication `address`, and REST API metadata. The `id` field (UUID) changes on every restart and is omitted above for brevity.

Wait until all expected nodes appear before proceeding. Node names are case-sensitive and must match exactly when referenced in the initialization request. Nodes that have not discovered each other cannot participate in cluster formation.

{% hint style="success" %}
**Checkpoint:** The response lists all three nodes (`node1`, `node2`, `node3`). If a node is missing, check that its container is running with `docker compose ps` and wait for discovery to complete (typically 10-30 seconds after container start).
{% endhint %}

## Initialize the Cluster

Cluster initialization is a one-time operation that creates the Cluster Management Group (CMG) and MetaStorage RAFT groups, assigns a cluster name, and opens the cluster for client connections. Send the request to any single node. It propagates to all discovered nodes.

GridGain 9 requires a license in the initialization request. The `license` field is a JSON string, so encode the license file with `jq -Rs`, which escapes the quotes and line breaks in the file. Pasting the raw file content into the request fails with `400 Invalid JSON`:

```bash
LICENSE=$(jq -Rs . gridgain-license.json)

curl -X POST http://localhost:10300/management/v1/cluster/init \
  -H "Content-Type: application/json" \
  -d '{
    "metaStorageNodes": ["node1", "node2", "node3"],
    "cmgNodes": ["node1", "node2", "node3"],
    "clusterName": "my-cluster",
    "license": '"$LICENSE"'
  }'
```

A successful initialization returns **HTTP 200 with an empty response body**. The endpoint blocks until the receiving node has fully joined the cluster, so the response itself confirms that at least one node has transitioned to `STARTED`.

The request fields:

| Field | Required | Description |
|-------|----------|-------------|
| `metaStorageNodes` | No | Nodes hosting the MetaStorage RAFT group. Use an odd number (1, 3, or 5) for quorum. |
| `cmgNodes` | No | Nodes hosting the CMG RAFT group. Defaults to `metaStorageNodes` if omitted. |
| `clusterName` | Yes | Human-readable cluster name. Must not be blank. |
| `clusterConfiguration` | No | Initial cluster configuration in HOCON format. |
| `license` | Yes | License key content. |

If you omit both `metaStorageNodes` and `cmgNodes`, the cluster auto-selects nodes: all nodes for clusters of 1-3, three nodes for clusters of 4, and five nodes for clusters of 5 or more. Nodes are selected alphabetically by name.

{% hint style="info" %}
Initialization is idempotent for identical parameters. Calling the endpoint again on an already-initialized cluster with the same node lists and cluster name returns 200 OK, and the CMG RAFT group keeps the first initialization. A call with a different cluster name or different node lists is rejected (for example, `Init CMG request denied, reason: Cluster names do not match`).
{% endhint %}

{% hint style="success" %}
**Checkpoint:** The curl command returns with no output and exit code 0 (HTTP 200). If it hangs, verify that all three nodes appear in the physical topology (previous step).
{% endhint %}

## Verify Cluster Health

After initialization completes, verify that the cluster is operational and all nodes have joined.

Query the cluster state:

```bash
curl -s http://localhost:10300/management/v1/cluster/state | jq .
```

Expected response:

```json
{
  "cmgNodes": [
    "node1",
    "node2",
    "node3"
  ],
  "msNodes": [
    "node1",
    "node2",
    "node3"
  ],
  "igniteVersion": "<latest GridGain 9 version>",
  "clusterTag": {
    "clusterName": "my-cluster",
    "clusterId": "..."
  }
}
```

The `cmgNodes` field lists nodes hosting the Cluster Management Group and `msNodes` lists nodes hosting MetaStorage. Both should contain all three nodes for a standard 3-node development cluster. The `igniteVersion` field reflects the product version.

Verify that each node has transitioned to `STARTED`:

```bash
for port in 10300 10301 10302; do
  echo "Port $port: $(curl -s http://localhost:$port/management/v1/node/state | jq -r .state)"
done
```

Expected output:

```text
Port 10300: STARTED
Port 10301: STARTED
Port 10302: STARTED
```

{% hint style="info" %}
On the latest GridGain 9 version, health probe endpoints provide an additional readiness signal. Query `/health/readiness` for a 200 `UP` response after initialization, or 503 `DOWN` before. On older versions, these endpoints return 404. The node state endpoint is the reliable cross-version indicator.
{% endhint %}

{% hint style="success" %}
**Checkpoint:** The cluster state response lists all three nodes in both `cmgNodes` and `msNodes`, and every node reports `STARTED`. The cluster is fully operational and accepting client connections on ports 10800-10802.
{% endhint %}

## Explore Post-initialization Endpoints

Before initialization, most REST endpoints return `409 CONFLICT`. After initialization, the full API becomes available. Query the logical topology to see nodes that are participating in distributed operations:

```bash
curl -s http://localhost:10300/management/v1/cluster/topology/logical | jq .
```

This returns the same node list as the physical topology, but only includes nodes that have successfully joined the cluster. Other endpoints now available include:

- `/management/v1/cluster/state` - Cluster metadata (CMG nodes, MetaStorage nodes, version)
- `/management/v1/configuration/cluster` - Read and update cluster-wide configuration (HOCON)
- `/management/v1/cluster/topology/logical` - Nodes participating in distributed operations

{% hint style="success" %}
**Checkpoint:** The logical topology returns the same three nodes as the physical topology. All post-initialization endpoints return `200 OK` instead of `409 CONFLICT`.
{% endhint %}

## Troubleshooting

<details>
<summary>Connection refused on port 10300</summary>

The REST server has not started yet. The HTTP server starts partway through the node boot sequence. Wait 5-10 seconds after container start and retry. Verify the container is running with `docker compose ps`.

</details>

<details>
<summary>Node state stuck on STARTING</summary>

`STARTING` is the expected state before cluster initialization. The node is waiting for an init command. If you have already initialized, the node may not have discovered the existing cluster. Check the physical topology endpoint to verify that the node can see the other cluster members. If the node is isolated, check Docker network connectivity.

</details>

<details>
<summary>409 CONFLICT on cluster state or configuration endpoints</summary>

The cluster has not been initialized. Before initialization, only a subset of endpoints are available (node state, node info, node version, physical topology, node configuration, cluster recovery, health probes, and cluster init). All other endpoints return `409 CONFLICT` with the message "Cluster is not initialized." Complete the initialization step first.

</details>

<details>
<summary>400 Bad Request: "Cluster name must not be empty"</summary>

The `clusterName` field in the init request is blank or missing. Provide a non-empty cluster name in the JSON body.

</details>

<details>
<summary>500 Internal Server Error: "Node is not present in the physical topology"</summary>

A node name in `metaStorageNodes` or `cmgNodes` does not match any node in the physical topology. Node names are case-sensitive and must match exactly. Query the physical topology endpoint to verify the correct node names before retrying.

</details>

<details>
<summary>409 CONFLICT: "REST temporarily unavailable" after initialization</summary>

The node is briefly transitioning through its post-initialization startup phase. During this window (typically a few seconds), most endpoints are temporarily restricted. Retry after 3-5 seconds. If it persists beyond 30 seconds, check the node logs with `docker compose logs node1`.

</details>

<details>
<summary>Init request hangs without returning</summary>

The init endpoint blocks until the receiving node joins the cluster. If it hangs, one or more nodes referenced in `metaStorageNodes` may not be reachable. Verify all nodes appear in the physical topology from the node receiving the request. Check Docker network connectivity and ensure no firewall rules block port 3344 between containers.

</details>

<details>
<summary>GridGain 9: License error during initialization</summary>

The `jq -Rs . gridgain-license.json` command reads the file relative to your current working directory. Verify that `gridgain-license.json` exists in the directory where you are running curl (the same directory as `docker-compose.yml`). A `400 Invalid JSON` response means the license content was not encoded as a JSON string; encode it with `jq -Rs` as shown in the init step. Check the file content with `cat gridgain-license.json` to confirm it contains valid JSON. Licenses expire; request a new one if yours has lapsed.

</details>

These endpoints form the foundation for scripted cluster management. You can extend them into health-check scripts, CI/CD pipeline steps, or monitoring integrations that poll node state and cluster topology.

## Related

- [How to Start a Cluster with Docker Compose](installation/start-cluster-docker-compose.md) - Set up the 3-node development cluster this guide manages.

- [Start Your Local GridGain 9 Development Cluster](../gridgain9-tutorials/distributed-sql-foundations/start-local-cluster.md) - Tutorial that walks through cluster setup with deeper context and loads the Music Store dataset.
