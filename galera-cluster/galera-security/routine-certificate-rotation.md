---
description: >-
  Rotate MariaDB Galera Cluster node certificates before expiry with no downtime,
  using hot reload and a validity-overlap window.
icon: clock-rotate-left
---

# Routine Certificate Rotation

Node certificates should be replaced before they expire. Because certificates can be reloaded without a restart (see [Reloading TLS Certificates Without Downtime](reloading-tls-certificates-without-downtime.md)), routine rotation needs no coordinated downtime.

## Procedure

1. Issue a new certificate for each node from the **same cluster CA**, with a validity period that overlaps the current certificate (the new certificate should be valid before the old one expires).
2. Distribute each node's new certificate and key to that node.
3. On one node at a time, replace the files at their configured paths and run `FLUSH SSL;`.
4. Confirm the node is serving the new certificate and remains `Synced`.
5. Repeat for each node.

{% hint style="info" %}
Keeping certificate lifetimes short is practical precisely because rotation is online. See [Choosing a Certificate Authority for Galera Cluster](choosing-a-certificate-authority-for-galera-cluster.md).
{% endhint %}

## See Also

* [Reloading TLS Certificates Without Downtime](reloading-tls-certificates-without-downtime.md)
* [Cluster CA Rotation](cluster-ca-rotation.md)
* [Responding to a Key or Certificate Compromise](responding-to-a-key-or-certificate-compromise.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
