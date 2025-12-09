# MaxScale ExasolRouter

{% hint style="info" %}
This functionality is available from MaxScale 25.10.1.
{% endhint %}

## Overview

_ExasolRouter_ is a router that in itself is capable of using an Exasol
cluster. It is primarily intended to be used together with
[SmartRouter](maxscale-smartrouter.md), with _writes_ being directed
to a regular MariaDB cluster and _reads_ to Exasol.

Unlike the other routers of MaxScale, the targets _ExasolRouter_ routes to
are not specified using `servers`, `targets`, or `cluster` entries in
the configuration file. Instead, Exasol database nodes are specified using
the [connection\_string](#connection_string) setting.

If _ExasolRouter_ is used standalone, a MariaDB server or a service should
be specified using `targets`. _ExasolRouter_ will not route to it, but it
will use it for authenticating clients. However, Exasol will be accessed
on behalf of all clients using the credentials specified in the
[connection\_string](#connection_string).

## Users

A `user` and `password` must _always_ be specified, but will only be used
if a MariaDB server/service has been specified as a target, and only for
authenticating a client.

The user and password to be used when accessing Exasol must be specified
using `UID` and `PWD` in the [connection\_string](#connection_string).

## Settings

### `connection_string`

* Type: string
* Mandatory: Yes
* Dynamic: No

Specifies the Exasol connection string.

For example:
```
connection_string=DSN=ExasolDSN;UID=sys;PWD=exasol;FINGERPRINT=NOCERTCHECK
```
Here it is assumed there is an `odbc.ini` ODBC configuration file containing
an `ExasolDSN` entry.

### `appearance`

* Type: [enum](../../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `read_only`, `read_write`
* Default: `read_only`

Specifies how the Exasol router appears to other components of MaxScale.

**Note** Irrespective of the value, the router does not in any way restrict
what kind of queries can be run through the router.

### `install_preprocessor_script`

* Type: [boolean](../../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default `true`

Specifies whether the MariaDB preprocessor script should be installed.
With the script installed, some MariaDB SQL constructs will be transparently
translated to equivalent Exasol SQL.

At the time of this writing, the script looks like
```
CREATE OR REPLACE PYTHON3 SCALAR SCRIPT UTIL.maria_preprocessor(request VARCHAR(2000000))
EMITS (translated_sql VARCHAR(2000000)) AS
def adapter_call(request):
    import sqlglot
    try:
        result = sqlglot.transpile(
            request,
            read='mysql',
            write='exasol',
            identify=True,
            unsupported='ignore'
        )
        return str(result[0])
    except Exception:
        return request
/
```

See [preprocessor\_script](#preprocessor_script)

### `preprocessor_script`

* Type: Path
* Mandatory: No
* Dynamic: No
* Default: ""

Specifies the location of a file from which the preprocessor script should
be read. With this setting, the built-in default script can be overridden.

If the path is not _absolute_ it will be interpreted relative to the MaxScale
data directory.

### `use_preprocessor_script`

* Type: [boolean](../../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`

Specifies whether the preprocessor script should be used. If `true`, the
session creation will fail unless the script is present.

## Transformations

The Exasol Router transparently translates some MariaDB constructs to
equivalent Exasol constructs.

### `COM_INIT_DB`

The MariaDB COM_INIT_DB packet, using which the default database is changed,
is transformed into the statement `OPEN SCHEMA <db>`.

### SQL

Currently a transformation will be made _only_ if there is an **exact**
match (apart from case and differences in whitespace) with the MariaDb SQL.

| MariaDb | Exasol  |
| ------- | ------- |
| SELECT @@VERSION_COMMENT LIMIT 1 | SELECT 'Exasol' AS '@@version_comment' LIMIT 1 |
| SELECT DATABASE() | SELECT TABLE_NAME AS 'Database()' FROM EXA_ALL_TABLES WHERE TABLE_SCHEMA = CURRENT_SCHEMA |
| SHOW DATABASES | SELECT SCHEMA_NAME AS 'Database' FROM EXA_SCHEMAS ORDER BY SCHEMA_NAME |
| SHOW TABLES | SELECT TABLE_NAME AS 'Tables' FROM SYS.EXA_ALL_TABLES WHERE TABLE_SCHEMA = CURRENT_SCHEMA ORDER BY TABLE_NAME |

## SmartRouter

The primary purpose of the Exasol router is to be used together with
[SmartRouter](maxscale-smartrouter.md). A minimal configuration looks
as follows:
```
[Server1]
type=server
address=127.0.0.1
port=3306
protocol=mariadbbackend

[ExasolService]
type=service
router=exasolrouter
connection_string=DSN=ExasolDSN;UID=sys;PWD=exasol
user=
password=

[SmartService]
type=service
router=smartrouter
user=MyServiceUser
password=MyServicePassword
targets=Server1, ExasolService
master=Server1

[SmartListener]
type=listener
service=SmartService
port=4007

```
Here it is assumed there is an `odbc.ini` ODBC configuration file containing
and `ExasolDSN` entry.

Note that `user` and `password` must be specified, even if they in this
context are not used.

With this setup, all writes will always be sent to `Server1`. Reads will initially
be sent to both `Server1` and `ExasolService` and once SmartRouter has learnt what
kind of reads are best sent to which target, it will exclusively send reads to
either `Server1` or `ExasolService` depending on which one is likely to provide
the response faster.

Here, a single server was used as `master`. It could just as well be a
[ReadWriteSplit](maxscale-readwritesplit.md) service in front of a MariaDB
cluster, which would provide HA.

## Stand-Alone
A minimal stand-alone configuration looks as follows.

```
[Server1]
type=server
address=127.0.0.1
port=3306
protocol=mariadbbackend

[ExasolService]
type=service
router=exasolrouter
connection_string=DSN=ExasolDSN;UID=sys;PWD=exasol;FINGERPRINT=NOCERTCHECK
targets=Server1
user=MyServiceUser
password=MyServicePassword

[ExasolListener]
type=listener
service=ExasolService
port=4008
```

With this setup, it is possible to connect using the regular `mariadb`
command line utility to the port 4008 and all queries will be sent to
Exasol.
