---
description: >-
  Guidance for selecting a Certificate Authority for MariaDB Galera Cluster
  inter-node TLS: dedicate a CA, keep certificates short-lived, issue both
  serverAuth and clientAuth EKUs, and keep the CA key offline.
icon: certificate
---

# Choosing a Certificate Authority for Galera Cluster

Inter-node TLS needs a certificate, private key, and CA chain on every node. How you source those certificates has security and operational consequences.

## Recommendations

### Dedicate a CA to Inter-Node Traffic

Inter-node TLS and customer-facing (client) TLS serve different threat models and should use separate trust anchors. If one CA signs both, every external client must then present a certificate signed by that same CA — usually not intended. Use a dedicated cluster CA for inter-node certificates.

### Keep Certificates Short-Lived

Issue node certificates with short validity (months to one or two years). Because certificates can be [reloaded without downtime](reloading-tls-certificates-without-downtime.md), short lifetimes are practical and reduce exposure if a key is compromised.

### Issue Certificates with Both serverAuth and clientAuth EKUs

During a state transfer the donor connects out to the joiner, so each node acts as both a TLS client and a TLS server at different times. Every node certificate must include **both** `serverAuth` and `clientAuth` in its Extended Key Usage (EKU) extension.

{% hint style="warning" %}
Web-server certificate templates restrict EKU to `serverAuth` only. A node certificate from such a template causes the donor's TLS handshake to abort during state transfer with an unsupported certificate-purpose error — even though replication itself works.
{% endhint %}

### Keep the CA Private Key Offline

The cluster does not need the CA private key at runtime — only the CA's self-signed certificate to verify peers. Keep the CA key offline or in an HSM.

## Extended Key Usage Requirement

During Incremental State Transfer (IST) and State Snapshot Transfer (SST) the donor connects *to* the joiner, so the joiner's certificate must work as a TLS **server** certificate and the donor's as a TLS **client** certificate. Because any node may take either role, every node certificate must include both `serverAuth` and `clientAuth` EKUs. Certificates restricted to `serverAuth` only break on the first state transfer to a newly added node.

## See Also

* [Securing Communications in Galera Cluster](securing-communications-in-galera-cluster.md)
* [Encryption vs Authentication in Galera Cluster](encryption-vs-authentication-in-galera-cluster.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
