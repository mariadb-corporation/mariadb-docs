# MaxScale ExasolRouter

## Overview

The _Exasol Router_ is a router that in itself is capable of using an Exasol
cluster. It is primarily intended to be used together with
[SmartRouter](maxscale-maxscale-smartrouter.md), with _writes_ being directed
to a regular MariaDB cluster and _reads_ to Exasol.

Unlike the other routers or MaxScale, the Exasol router does not use `servers`,
`targets`, or `cluster` entries in the configuration file to define servers.
Instead, Exasol database nodes are specified directly via the `connection_string`
setting.

## Users

Currently, the Exasol router _always_ uses the service `user` and `password`
settings when accessing Exasol. That is, it uses those settings _regardless_
of the identity of the client accessing MaxScale.

## Settings

### `connection_string`

* Type: string
* Mandatory: Yes
* Dynamic: No

Specifies the Exasol connection string.

For example:
```
connection_string=127.0.0.1:8563

connection_string=127.0.0.1/340F511A5A5179FF44A6828CC140FAEBAF1F2E2ECD73FBCD7EDD54C8B96A5886:8563
```
The latter alternative illustrates the case when the Exasol server uses a
self-signed certificate.

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

See [preprocessor_script](#preprocessor_script)

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

Currently a transformation will be made **only** if there is an **exact**
match (apart from case) with the MariaDb SQL. At this point the goal is
to match what the MariaDB command line client sends.

| MariaDb | Exasol  |
| ------- | ------- |
| SELECT @@VERSION_COMMENT LIMIT 1 | SELECT 'Exasol' AS '@@version_comment' LIMIT 1 |
| SELECT DATABASE() | SELECT TABLE_NAME AS 'Database()' FROM EXA_ALL_TABLES WHERE TABLE_SCHEMA = CURRENT_SCHEMA |
| SHOW DATABASES | SELECT SCHEMA_NAME AS 'Database' FROM EXA_SCHEMAS ORDER BY SCHEMA_NAME |
| SHOW TABLES | SELECT TABLE_NAME AS 'Tables' FROM SYS.EXA_ALL_TABLES WHERE TABLE_SCHEMA = CURRENT_SCHEMA ORDER BY TABLE_NAME |

## Limitations

The following is assumed regarding the data returned by Exasol:
* The value in a column of a row is assumed to be no more than 1024 bytes, and
* the complete returned result set will fit in a 16MB MariaDB protocol packet.

If these limitations are exceeded, the router may malfunction or crash.

These limitations are temporary and will be removed before Dec 8.

## SmartRouter

The primary purpose of the Exasol router is to be used together with
[SmartRouter](maxscale-smartrouter.md). A minimal configuration looks
as follows:
```
[ExasolService]
type=service
router=exasolrouter
user=sys
password=exasol
connection_string=127.0.0.1/340F511A5A5179FF44A6828CC140FAEBAF1F2E2ECD73FBCD7EDD54C8B96A5886:8563

[Server1]
type=server
address=127.0.0.1
port=3306
protocol=mariadbbackend

[SmartService]
type=service
router=smartrouter
user=MyUser
password=MyPassword
targets=Server1, ExasolService
master=Server1
```
With this setup, all writes will always be sent to `Server1`. Reads will initially
be sent to both `Server1` and `ExasolService` and once SmartRouter has learnt what
kind of reads are best sent to which target, it will exclusively send reads to
either `Server1` or `ExasolService` depending on which one is likely to provide
the response faster.

Here, a single server was used as `master`. It could just as well be a
[ReadWriteSplit](maxscale-readwritesplit.md) service, in front of a MariaDB
cluster, which would provide HA.

