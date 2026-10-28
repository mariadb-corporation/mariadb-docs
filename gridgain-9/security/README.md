---
description: >-
  Secure a GridGain 9 cluster with SSL/TLS encryption, user authentication,
  role-based authorization, row-level security, and data encryption at rest.
icon: shield-halved
---

# Security and Authentication

This section describes how to secure a GridGain 9 cluster. It covers encrypting communication with SSL/TLS, authenticating users, controlling access with role-based authorization and row-level security, issuing JWT tokens, the full list of user permissions and roles, and encrypting data at rest with transparent data encryption.

## User Security

By default, all users can perform any updates on the cluster, or [upload arbitrary code to the cluster](../gridgain9-development/code-deployment.md) and perform remote code execution with [distributed computing](../gridgain9-development/distributed-computing/about-distributed-computing.md). To improve security, we recommend configuring [user roles](user-permissions-and-roles.md) and [enabling authorization](authentication.md#basic-authentication) on the cluster.

## Communication

By default, nodes use plain-text communication that is vulnerable to malicious actions. GridGain separates communications between cluster nodes and communication with clients.

### Node to Node Communication

Communication between nodes usually happens within the same data center. We recommend the following to improve the security of your cluster:

- Enable SSL for cluster communication with the `ignite.network.ssl` [node configuration](../reference/configuration/node-configuration-parameters.md#network-configuration).
- Run the cluster in a trusted and isolated network.

### Node to Client Communication

Communication to clients is exposed to the internet. Only the client port (10800 by default) is exposed. To secure interaction with your clients:

- Enable SSL for client communication with the `ignite.clientConnector.ssl` [node configuration](../reference/configuration/node-configuration-parameters.md#client-connector-configuration).
- Enable [authentication](authentication.md) on the cluster.

## In This Section

{% columns %}
{% column %}
{% content-ref url="authentication-and-authorization/" %}
[Authentication and Authorization](authentication-and-authorization/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Control who can connect to a GridGain 9 cluster and what they may do — authentication, JWT tokens, role-based authorization, permissions and roles, and row-level security.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="encryption-and-transport/" %}
[Encryption and Transport Security](encryption-and-transport/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Protect GridGain 9 data in transit and at rest — SSL/TLS for nodes and clients, and transparent data encryption.
{% endcolumn %}
{% endcolumns %}
