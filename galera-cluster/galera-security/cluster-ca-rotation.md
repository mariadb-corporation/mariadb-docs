---
description: >-
  Migrate a MariaDB Galera Cluster to a new Certificate Authority without downtime
  using a dual-trust bundle, then retire the old CA.
icon: right-left
---

# Cluster CA Rotation

Migrating to a new Certificate Authority without downtime relies on a **dual-trust** window, during which nodes trust both the old and the new CA.

## Procedure

1. **Trust both CAs.** Add the new CA to each node's trust store alongside the old one — either by pointing `ssl_capath` at a directory containing both CA certificates (processed with `openssl rehash`), or by using a CA bundle file that contains both. Apply with `FLUSH SSL;` on each node so both CAs are trusted before any new certificate is issued.
2. **Reissue node certificates from the new CA**, one node at a time, replacing the files at their configured paths and running `FLUSH SSL;`. Because every node still trusts the old CA, nodes with old and new certificates interoperate throughout.
3. **Retire the old CA.** Once every node presents a certificate signed by the new CA, remove the old CA from the trust store and run `FLUSH SSL;` on each node.

{% hint style="warning" %}
Do not remove the old CA from trust until every node has been reissued from the new CA. Removing it early will reject nodes still presenting old-CA certificates.
{% endhint %}

## See Also

* [Reloading TLS Certificates Without Downtime](reloading-tls-certificates-without-downtime.md)
* [Routine Certificate Rotation](routine-certificate-rotation.md)
* [Choosing a Certificate Authority for Galera Cluster](choosing-a-certificate-authority-for-galera-cluster.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
