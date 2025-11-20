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

Internally, the router communicates with Exasol using ODBC, which is visible
in the configuration of the router.

## Users

Currently, the Exasol router uses one set of credentials when connecting
to Exasol. That is, it uses the same credentials _regardless_ of the identity
of the client accessing MaxScale.

## Settings

### `connection_string`

* Type: string
* Mandatory: Yes
* Dynamic: No

Specifies the Exasol connection string. This setting is passed directly
to the ODBC driver and the required content depends on how ODBC has
been configured.

#### Without `odbc.ini` and `odbcinst.ini`

In this case, the following keys must be provided in the connection
string:
* `DRIVER`: The path to the Exasol ODBC driver.
* `EXAHOST`: The Exasol host string.

In addition, any of the keys specified
[here](https://docs.exasol.com/db/latest/connect_exasol/drivers/odbc/using_odbc.htm)
can be provided and may have to be provided (e.g. `FINGERPRINT`).

**NOTE** If `EXAUSER` (or `UID`) is **not** provided in the connection string, the
service
[user](../../maxscale-management/deployment/maxscale-configuration-guide.md#user) and
[password](../../maxscale-management/deployment/maxscale-configuration-guide.md#password)
will automatically be appended to the string as `;UID=...;PWD=...`.

Example:
```
connection_string=Driver=/path/to/libexaodbc.so;EXAHOST=127.0.0.1:8563;FINGERPRINT=NOCERTCHECK
```

`libexaodbc.so` is the Exasol ODBC driver; not the MaxScale Exasol router module.

#### With `/etc/odbcinst.ini`

The `odbcinst.ini` file should contain an entry like
```
[Exasol-Driver]
Description=Exasol ODBC Connector
Driver=/path/to/libexaodbc.so
```
With that entry, the `DRIVER` can be specified using the section name.

Example:
```
connection_string=Driver=Exasol-Driver;EXAHOST=127.0.0.1:8563;FINGERPRINT=NOCERTCHECK
```

#### With `/etc/odbc.ini` or `~/.odbc.ini`

The latter file must reside in the home-directory of the user used
for running MaxScale.

The `odbc.ini` file should contain an entry like
```
[Exasol]
DRIVER = Exasol-Driver
EXAHOST = 127.0.0.1:8563
FINGERPRINT = NOCERTCHECK
UID = MyUser
PWD = MyPwd
```

That assumes a `Exasol-Driver` entry in `/etc/odbcinst.ini`. The `DRIVER`
can also be provided as a path:
```
DRIVER = /path/to/libexaodbc.so
```

With that entry, the following is sufficient:
```
connection_string=DSN=Exasol
```

In this case, the `UID/PWD` specified in the file, will be used
instead of the `user` and `password` settings of the service.

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

