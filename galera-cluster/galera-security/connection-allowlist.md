---
description: >-
  Restrict which IP addresses may join a MariaDB Galera Cluster using the
  wsrep_allowlist system variable or the mysql.wsrep_allowlist table.
icon: list-check
---

# Connection Allowlist

{% hint style="info" %}
The `wsrep_allowlist` system variable is available from MariaDB Enterprise Server 11.4.
{% endhint %}

MariaDB Enterprise Cluster can restrict which IP addresses are allowed to establish cluster connections. Incoming connections are checked by IP address against an allowlist. When no allowlist is configured, all addresses are allowed.

## Configuring the Allowlist

Allowed addresses can be specified in two ways:

* **`wsrep_allowlist` system variable** — a comma-separated list of allowed IP addresses, set at server startup. The variable is read-only and global, and defaults to empty.
* **`mysql.wsrep_allowlist` table** — a persistent allowlist stored in the system schema, consulted once the storage engines are initialized.

When an allowlist is configured, only the listed addresses may join the cluster; all other connection attempts are rejected.

```ini
[mariadb]
...
wsrep_allowlist = "10.0.0.11,10.0.0.12"
```

## How It Works

The allowlist is enforced through the wsrep allowlist service, which the Galera library calls to authorize each incoming connection by its IP address.

## See Also

* [Securing Communications in Galera Cluster](securing-communications-in-galera-cluster.md)
* [MariaDB Enterprise Cluster Security](mariadb-enterprise-cluster-security.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
