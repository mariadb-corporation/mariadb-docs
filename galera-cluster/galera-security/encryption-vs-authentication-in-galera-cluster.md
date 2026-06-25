---
description: >-
  How encryption and peer authentication differ in MariaDB Galera Cluster, what
  each wsrep_ssl_mode value guarantees, and why the default SERVER mode is
  insufficient for compliance regimes that require peer authentication.
icon: shield-halved
---

# Encryption vs Authentication in Galera Cluster

TLS provides two related but distinct guarantees:

* **Encryption** protects data in transit from eavesdropping.
* **Peer authentication** ensures the entity at the other end of the connection is the one you expect.

They are configured independently, and Galera Cluster's default configuration provides only the first.

## What Each WSREP TLS Mode Guarantees

The [wsrep\_ssl\_mode](../reference/wsrep-variable-details/wsrep_ssl_mode.md) system variable determines which guarantees apply to Enterprise Cluster replication traffic:

| Goal                             | Configuration                                                         |
| -------------------------------- | --------------------------------------------------------------------- |
| Encryption only                  | `wsrep_ssl_mode=SERVER` (default), plus `ssl_cert`/`ssl_key`/`ssl_ca` |
| Encryption + peer authentication | `wsrep_ssl_mode=SERVER_X509`                                          |

In `SERVER` mode a node encrypts replication traffic but accepts any peer that completes the TLS handshake — it does not verify the peer's X.509 certificate. In `SERVER_X509` mode every inter-node connection additionally requires a valid, CA-verifiable certificate.

{% hint style="warning" %}
If compliance requires mutual authentication of endpoints — as PCI DSS, SOC 2, ISO 27001, and most internal audit programs interpret "strong cryptography" — the default `SERVER` mode is insufficient. Use `SERVER_X509`.
{% endhint %}

{% hint style="info" %}
A future per-peer identity scheme (`[cluster_tls] verify=identity`, based on URI-SAN matching) is **planned** to provide encryption with per-peer identity verification. It is not yet available.
{% endhint %}

## Why the Distinction Matters

Encryption alone defends against a passive eavesdropper, but not against an active attacker who can place a rogue server at a cluster member's address. Without peer authentication a node cannot tell a legitimate member from an impostor presenting an arbitrary certificate. Peer authentication closes that gap by requiring each node to present a certificate that chains to the cluster's trusted CA.

## See Also

* [wsrep\_ssl\_mode](../reference/wsrep-variable-details/wsrep_ssl_mode.md)
* [Securing Communications in Galera Cluster](securing-communications-in-galera-cluster.md)
* [Migrating to Verified TLS in Galera Cluster](migrating-to-verified-tls-in-galera-cluster.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
