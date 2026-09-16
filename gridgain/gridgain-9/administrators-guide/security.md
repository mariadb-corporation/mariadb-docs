---
description: >-
  Overview of GridGain 9 cluster security, covering user authorization and the
  encryption of node-to-node and node-to-client communication.
---

# Cluster Security

## User Security

By default, all users can perform any updates on the cluster, or [upload arbitrary code to the cluster](../developers-guide/code-deployment/code-deployment.md) and perform remote code execution with [distributed computing](../developers-guide/compute/compute.md). To improve security, we recommend configuring [user roles](security/permissions.md) and [enabling authorization](security/authentication.md#basic-authentication) on the cluster.

## Communication

By default, nodes use plain-text communication that is vulnerable to malicious actions. GridGain separates communications between cluster nodes and communication with clients.

## Node to Node Communication

Communication between nodes usually happens within the same data center. We recommend the following to improve the security of your cluster:

- Enable SSL for cluster communication with the `ignite.network.ssl` [node configuration](config/node-config.md#network-configuration).
- Run the cluster in a trusted and isolated network.

## Node to Client Communication

Communication to clients is exposed to the internet. Only the client port (10800 by default) is exposed. To secure interaction with your clients:

- Enable SSL for client communication with the `ignite.clientConnector.ssl` node configuration.
- Enable [authentication](security/authentication.md) on the cluster.
