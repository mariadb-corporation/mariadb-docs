---
description: >-
  The socket.ssl wsrep_provider_options entry enables TLS encryption for
  Galera Cluster replication traffic; it defaults to NO and cannot be changed
  dynamically.
---

# socket.ssl

## Overview <a href="#overview_h2" id="overview_h2"></a>

Explicitly enables TLS usage by the wsrep provider.

The `wsrep_provider_options` system variable applies to MariaDB Enterprise Cluster, powered by Galera and to Galera Cluster available with MariaDB Community Server. This page relates specifically to the socket.ssl `wsrep_provider_options`.

## Details

The `socket.ssl` option is used to specify if SSL encryption should be used.

| Option Name   | socket.ssl |
| ------------- | ---------- |
| Default Value | NO         |
| Dynamic       | NO         |
| Debug         | `NO`       |

## Examples

### Display Current Value

`wsrep_provider_options` define optional settings the node passes to the wsrep provider.

To display current `wsrep_provider_options` values:

```sql
SHOW GLOBAL VARIABLES LIKE 'wsrep_provider_options';
```

The expected output will display the option and the value. Options with no default value, for example SSL options, will not be displayed in the output.

### Set in Configuration File

**When changing a setting for a wsrep\_provider\_options in the config file, you must list EVERY option that is to have a value other than the default value**. Options that are not explicitly listed are reset to the default value.

Options are set in the `my.cnf` configuration file. Use the `;` delimiter to set multiple options.

The configuration file must be updated on each node. A restart to each node is needed for changes to take effect.

Use a quoted string that includes **every option** where you want to override the default value. Options that are not in the list will reset to their default value.

To set the option in the configuration file:

```
wsrep_provider_options='socket.ssl=YES;gcache.debug=YES;gcs.fc_limit=NO;socket.send_buf_size=NO;evs.keepalive_period=PT3S'
```

### Set Dynamically

The socket.ssl option cannot be set dynamically. It can only be set in the configuration file.

Trying to change a non-dynamic option with `SET` results in an error:

```sql
ERROR 1210 (HY000): Incorrect arguments to SET
```
