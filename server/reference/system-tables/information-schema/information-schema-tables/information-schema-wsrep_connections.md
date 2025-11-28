---
description: >-
  The Information Schema WSREP_CONNECTIONS table shows active connections to the
  Galera Cluster, primarily used for debugging cluster membership.
---

# Information Schema WSREP\_CONNECTIONS

{% hint style="info" %}
This table is used in [MariaDB Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/).
{% endhint %}

{% hint style="info" %}
This table is available as of MariaDB Enterprise Server 11.8.
{% endhint %}

This table contains active Galera connections on queried nodes in the cluster. Example output:

```sql
MariaDB [(none)]> SELECT * FROM information_schema.wsrep_connections;
+-----------------+-------------------+-----------------+-----------------+------------------------+---------------------------------------------------+------------------------------------------------------+---------------------+
| connection_id   | connection_scheme | local_address   | remote_address  | cipher                 | certificate_subject                               | certificate_issuer                                   | certificate_version |
+-----------------+-------------------+-----------------+-----------------+------------------------+---------------------------------------------------+------------------------------------------------------+---------------------+
| 136018124822096 | ssl               | 127.0.0.1:19033 | 127.0.0.1:59010 | TLS_AES_256_GCM_SHA384 | /C=FI/ST=Helsinki/L=Helsinki/O=Galera/CN=galera.1 | /C=FI/ST=Helsinki/L=Helsinki/O=Galera/CN=galera.root | TLSv1.3             |
| 136018124966656 | ssl               | 127.0.0.1:49650 | 127.0.0.1:19039 | TLS_AES_256_GCM_SHA384 | /C=FI/ST=Helsinki/L=Helsinki/O=Galera/CN=galera.1 | /C=FI/ST=Helsinki/L=Helsinki/O=Galera/CN=galera.root | TLSv1.3             |
+-----------------+-------------------+-----------------+-----------------+------------------------+---------------------------------------------------+------------------------------------------------------+---------------------+
2 rows in set (0.004 sec)
```
