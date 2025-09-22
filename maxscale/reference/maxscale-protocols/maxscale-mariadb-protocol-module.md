# MaxScale MariaDB Protocol Module

## Overview

The `mariadbprotocol` module implements the MariaDB client-server protocol.

The legacy protocol names `mysqlclient`, `mariadb` and `mariadbclient` are all
aliases to `mariadbprotocol`.

## Connection Redirection

The [Connection Redirection](https://mariadb.com/docs/server/ha-and-performance/connection-redirection-mechanism-in-the-mariadb-clientserver-protocol)
introduced in MariaDB 11.4 allows client connections to be redirected to another
server if the server in question is going into maintenance. As MaxScale is
intended to be the gateway through which clients connect to the database
cluster, the use of `redirect_url` directly on the backend database servers
poses some challenges when used with MaxScale.

To prevent the accidental redirection of clients away from MaxScale, the
notification about the change of the system variable `redirect_url` is
intercepted by MaxScale and renamed into `mxs_rdir_url`. This prevents any
automated redirects from taking place while still allowing clients to see the
information if they need it.

To redirect clients away from MaxScale, use the
[redirect_url](../Getting-Started/Configuration-Guide.md#redirect_url)
parameter.

## Configuration

Protocol level parameters are defined in the listeners. They must be defined
using the scoped parameter syntax where the protocol name is used as the prefix.

```
[MyListener]
type=listener
service=MyService
protocol=mariadbprotocol
mariadbprotocol.allow_replication=false
port=3306
```

For the MariaDB protocol module, the prefix is always `mariadbprotocol`.

## Settings

### `allow_replication`

* Type: [boolean](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true

Whether the use of the replication protocol is allowed through this listener. If
disabled with `mariadbprotocol.allow_replication=false`, all attempts to start
replication will be rejected with a ER\_FEATURE\_DISABLED error (error number
1289).

### `compression`

- **Type**: [enum_mask](../Getting-Started/Configuration-Guide.md#enumerations)
- **Mandatory**: No
- **Dynamic**: Yes
- **Values**: `none`, `zlib`, `zstd`
- **Default**: `zlib`, `zstd`

The set of enabled compression protocols. The `zlib` compression protocol is the
traditional MySQL/MariaDB zlib based compression algorithm that uses a fixed
compression level. The `zstd` is the newer compression protocol that allows the
compression level to be configured by the client.

To disable protocol level compression, set `mariadbprotocol.compression=none`.

### `compression_threshold`

- **Type**: [size](../Getting-Started/Configuration-Guide.md#sizes)
- **Mandatory**: No
- **Dynamic**: Yes
- **Default**: 50

The upper limit for uncompressed payloads.

In MariaDB and MySQL, the upper limit for uncompressed payloads is always 50
bytes. If the response is smaller than that, the result is sent uncompressed and
if it's larger than that, it is sent compressed. MaxScale allows this limit to
be configured so that larger results can be sent uncompressed.

For example, with `mariadbprotocol.compression_threshold=256Ki`, only events
that are larger than 256 kibibytes get compressed. Most small resultsets thus
will be sent uncompressed but larger ones will be compressed before being
sent. This makes it possible to customize the bandwidth usage of MaxScale when
protocol level compression is used.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
