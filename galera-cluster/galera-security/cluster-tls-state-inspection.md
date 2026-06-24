---
description: >-
  Inspect per-connection TLS state across a MariaDB cluster via the
  information_schema.wsrep_connections view (cipher, certificate subject, issuer,
  and version per connection).
icon: table-list
---

# Cluster TLS State Inspection

{% hint style="warning" %}
This page documents a forthcoming feature and is a draft. The `wsrep_connections` `INFORMATION_SCHEMA` view is present in MariaDB Advanced Cluster (Raft-based, 12.3) source and may change before general availability. Verify against your server version.
{% endhint %}

Operators and auditors often need to answer "which certificate is each node presenting, and over what cipher" without scraping logs. The `wsrep_connections` view exposes per-connection TLS state.

## information_schema.wsrep_connections

The `wsrep_connections` plugin provides one row per Galera connection:

| Column                | Description                                                       |
| --------------------- | ----------------------------------------------------------------- |
| `connection_id`       | Connection identifier.                                            |
| `connection_scheme`   | Connection scheme / transport.                                    |
| `local_address`       | Local endpoint address.                                           |
| `remote_address`      | Remote peer address.                                              |
| `cipher`              | Negotiated TLS cipher (empty if the connection is not encrypted). |
| `certificate_subject` | Subject of the peer certificate.                                  |
| `certificate_issuer`  | Issuer of the peer certificate.                                   |
| `certificate_version` | Version of the peer certificate.                                  |

```sql
SELECT remote_address, cipher, certificate_subject, certificate_issuer
FROM information_schema.wsrep_connections;
```

A connection with an empty `cipher` is not using TLS. Comparing `certificate_issuer` across rows helps confirm every peer chains to the expected cluster CA.

## See Also

* [Encryption vs Authentication in Galera Cluster](encryption-vs-authentication-in-galera-cluster.md)
* [Securing Communications in Galera Cluster](securing-communications-in-galera-cluster.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
