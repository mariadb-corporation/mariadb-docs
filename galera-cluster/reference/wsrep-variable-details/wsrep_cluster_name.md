---
description: >-
  wsrep_cluster_name is the dynamic global system variable that sets the
  logical cluster name; all Galera Cluster nodes must share the same value to
  form a Primary Component.
---

# wsrep\_cluster\_name

## Overview <a href="#overview_h2" id="overview_h2"></a>

Name for the cluster.

## Details

This system variable specifies the logical name of the cluster. Every Cluster Node that connects to each other **must** have the same logical name in order to form a component or join the Primary Component.

### Parameters

| Command-line          | --wsrep\_cluster\_name=arg |
| --------------------- | -------------------------- |
| Configuration file    | Supported                  |
| Dynamic               | Yes                        |
| Scope                 | Global                     |
| Data Type             | VARCHAR                    |
| Product Default Value | my\_wsrep\_cluster         |

## Examples

### Configuration

Set the cluster name using an options file:

```ini
[mariadb]
wsrep_provider        = /usr/lib/galera/libgalera_smm.so
wsrep_cluster_name    = example_cluster
wsrep_cluster_address = gcomm://192.0.2.1,192.0.2.2,192.0.2.3
```

### Show Configuration

To view the current cluster name, use the [SHOW VARIABLES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-variables) statement:

```sql
SHOW VARIABLES LIKE "wsrep_cluster_name";
```

```
+--------------------+-----------------+
| Variable_name      | Value           |
+--------------------+-----------------+
| wsrep_cluster_name | example_cluster |
+--------------------+-----------------+
```
