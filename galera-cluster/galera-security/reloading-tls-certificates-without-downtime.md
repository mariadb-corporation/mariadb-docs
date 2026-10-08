---
description: >-
  Reload MariaDB Galera Cluster TLS certificates without restarting a node using
  FLUSH SSL or socket.ssl_reload, including the atomic file-replacement procedure.
icon: rotate
---

# Reloading TLS Certificates Without Downtime

Galera Cluster nodes can pick up new TLS certificates without a restart. Two operator commands trigger a reload:

| Command                                                    | Effect                                                                                         |
| ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `FLUSH SSL;`                                               | Reloads the MariaDB server's TLS context and, when WSREP is active, the Galera provider's too. |
| `SET GLOBAL wsrep_provider_options='socket.ssl_reload=1';` | Reloads only the Galera provider's TLS context.                                                |

{% hint style="info" %}
The certificate and key file *paths* cannot be changed dynamically. Place the updated files at the same paths configured by `ssl_cert`, `ssl_key`, and `ssl_ca` (or the `socket.ssl_*` provider options).
{% endhint %}

## Procedure for Replacing a Node's Certificate

1. Write the new certificate and key to disk alongside the existing files.
2. Atomically replace the files at the configured paths (for example with `mv`, which is atomic on POSIX — readers see either the old or the new pair, never a torn state).
3. Run `FLUSH SSL;` on the node.
4. Confirm the node is serving the new certificate.
5. Repeat on each node. No coordinated downtime is required.

## See Also

* [Securing Communications in Galera Cluster](securing-communications-in-galera-cluster.md)
* [MariaDB Enterprise Cluster Security](mariadb-enterprise-cluster-security.md) (Enable TLS without Downtime)
* [Routine Certificate Rotation](routine-certificate-rotation.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
