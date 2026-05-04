---
description: >-
  socket.ssl_cert sets the path to the node's SSL certificate used by the wsrep
  provider to encrypt Galera replication traffic; it must be in PEM format and
  is non-dynamic.
---

# socket.ssl\_cert

## Overview <a href="#overview_h2" id="overview_h2"></a>

Defines the path to the SSL certificate.

The `wsrep_provider_options` system variable applies to MariaDB Enterprise Cluster, powered by Galera and to Galera Cluster available with MariaDB Community Server. This page relates specifically to the socket.ssl\_cert `wsrep_provider_options`.

## Details

The node uses the certificate as a self-signed public key in encrypting replication traffic over SSL. You can use either an absolute path or one relative to the working directory. The file must use PEM format.

| Option Name   | socket.ssl\_cert       |
| ------------- | ---------------------- |
| Default Value | "" _(an empty string)_ |
| Dynamic       | NO                     |
| Debug         | `NO`                   |

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
wsrep_provider_options='socket.ssl_cert=/path/to/server-cert.pem;gcache.debug=YES;gcs.fc_limit=NO;socket.send_buf_size=NO;evs.keepalive_period=PT3S'
```

### Set Dynamically

The socket.ssl\_cert option cannot be set dynamically. It can only be set in the configuration file.

Trying to change a non-dynamic option with `SET` results in an error:

```sql
ERROR 1210 (HY000): Incorrect arguments to SET
```
