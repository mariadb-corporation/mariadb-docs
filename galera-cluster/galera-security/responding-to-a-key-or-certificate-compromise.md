---
description: >-
  Respond to a compromised MariaDB Galera Cluster node key or certificate by
  revoking via CRL or reissuing from a new CA, applied online with hot reload.
icon: triangle-exclamation
---

# Responding to a Key or Certificate Compromise

If a node's private key or certificate is compromised, the goal is to stop trusting it across the cluster as quickly as possible. There are two approaches, which can be combined.

## Revoke via a Certificate Revocation List (CRL)

In the `SERVER` and `SERVER_X509` TLS modes, inter-node TLS uses the server's TLS configuration, which supports a CRL through the `ssl_crl` (file) and `ssl_crlpath` (directory) system variables.

1. Add the compromised certificate to the CRL and distribute the updated CRL to every node.
2. Run `FLUSH SSL;` on each node so the new CRL takes effect.

{% hint style="info" %}
CRL checking applies to inter-node traffic only in the server-based TLS modes (`SERVER`, `SERVER_X509`).
{% endhint %}

## Reissue from a New CA

For a CA-key compromise, or to invalidate a certificate without relying on CRL distribution, rotate the cluster CA and reissue all node certificates. See [Cluster CA Rotation](cluster-ca-rotation.md).

## See Also

* [Cluster CA Rotation](cluster-ca-rotation.md)
* [Reloading TLS Certificates Without Downtime](reloading-tls-certificates-without-downtime.md)
* [wsrep\_ssl\_mode](../reference/wsrep-variable-details/wsrep_ssl_mode.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
