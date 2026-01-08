---
description: >-
  Route analytical queries to an Exasol cluster. This router integrates Exasol
  with MaxScale often used alongside SmartRouter for hybrid
  transactional/analytical workloads.
---

# MaxScale Exasolrouter

{% hint style="info" %}
This functionality is available from MaxScale 25.10.1.
{% endhint %}

## Overview

_ExasolRouter_ is a router that in itself is capable of using an
[Exasol Analytics Engine](https://www.exasol.com).
It is primarily intended to be used together with
[SmartRouter](maxscale-smartrouter.md), with _writes_ being directed
to a regular MariaDB cluster and _reads_ to either MariaDB or Exasol,
depending on which one can provide the response faster.

Unlike the other routers of MaxScale, the targets _ExasolRouter_ routes to
are not specified using `servers`, `targets`, or `cluster` settings in
the configuration file. Instead, Exasol is specified using the
[connection\_string](#connection_string) setting.

However, if _ExasolRouter_ is used standalone, a MariaDB server or a service
should be specified using `targets`. _ExasolRouter_ will not route to it,
but it will use it for authenticating clients. Exasol will still be accessed
on behalf of all clients using the credentials specified in the
[connection\_string](#connection_string).

## Users

A `user` and `password` must _always_ be specified, but will only be used
if a MariaDB server/service has been specified as a target, and only for
authenticating a client. If that functionality is not needed, e.g. when
_ExasolRouter_ is used with _SmartRouter_, they can be left empty, but
must still be present.
```
user=
password=
```

The user and password to be used when accessing Exasol must be specified using `UID` and `PWD` in the [connection\_string](maxscale-exasolrouter.md#connection_string).

## Preprocessor Script

The SQL supported by Exasol is not identical with the SQL supported by
MariaDB. To alleviate that, the Exasol router can install a preprocessor
script that is capable of converting to some extent MariaDB SQL constructs
to the Exasol equivalents. Currently, the script looks like:
```
CREATE OR REPLACE PYTHON3 PREPROCESSOR SCRIPT UTIL.maria_preprocessor AS
import sqlglot
def adapter_call(request):
    result = sqlglot.transpile(
        request,
        read='mysql',
        write='exasol',
        identify=True
    )
    return str(result[0])
```
By default, the Exasol router installs it every time it starts. The default
behaviour can be alterered using the [preprocessor](#preprocessor)
setting.

If the default script is used, the Exasol router will also ensure that the
schema `UTIL` exists. If the default script is not used, the Exasol router
assumes that a used schema exists.

## Settings

### `connection_string`

* Type: string
* Mandatory: Yes
* Dynamic: No

Specifies the Exasol connection string. The exact content depends on the
contents of `odbc.ini` and `odbcinst.ini`.

For example:
```
connection_string=DSN=ExasolDSN;UID=sys;PWD=exasol;FINGERPRINT=NOCERTCHECK
```
Here it is assumed the `odbc.ini` ODBC configuration file containing
an `ExasolDSN` entry.

### `appearance`

* Type: [enum](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `read_only`, `read_write`
* Default: `read_only`

Specifies how the Exasol router appears to other components of MaxScale.
This is of relevance only if another service uses an Exasol router service
as target.

**Note** Irrespective of the value, the router does not in any way restrict
what kind of queries can be run through the router.

### `preprocessor`

* Type: String
* Mandatory: No
* Dynamic: No
* Values: `auto`, `activate-only`, `custom:<path>`, `disabled`
* Default: `auto`

The values mean:

* `auto`: The built-in preprocessor script is installed at service
  startup and is taken into use in each session.
* `activate-only`: The preprocessor script is assumed to exist in Exasol
  and is taken into use in each session.
* `custom:<path>`: The path is assumed to point to a file containing the
  preprocessor script to be installed at service startup. If the path is
  _not_ absolute, it is interpreted relative to the MaxScale data directory.
  The script is subsequently taken into use in each session.
  See also [preprocessor_script](#preprocessor_script).
* `disabled`: The preprocessor is neither installed at service startup,
  nor taken into use in sessions.

### `preprocessor_script`

* Type: String
* Mandatory: No
* Dynamic: No
* Default: "UTIL.maria_preprocessor"

If the name of a custom preprocessor script, specified using
`preprocessor=custom:/path`, is not `UTIL.maria_preprocessor`, the
name should be provided using this setting.

## Transformations

The Exasol Router transparently translates some MariaDB constructs to equivalent Exasol constructs.

### `COM_INIT_DB`

The MariaDB COM\_INIT\_DB packet, using which the default database is changed, is transformed into the statement `OPEN SCHEMA <db>`.

### SQL

Currently a transformation will be made _only_ if there is an **exact** match (apart from case and differences in whitespace) with the MariaDb SQL.

| MariaDb                           | Exasol                                                                                                              |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| SELECT @@VERSION\_COMMENT LIMIT 1 | SELECT 'Exasol' AS '@@version\_comment' LIMIT 1                                                                     |
| SELECT DATABASE()                 | SELECT TABLE\_NAME AS 'Database()' FROM EXA\_ALL\_TABLES WHERE TABLE\_SCHEMA = CURRENT\_SCHEMA                      |
| SHOW DATABASES                    | SELECT SCHEMA\_NAME AS 'Database' FROM EXA\_SCHEMAS ORDER BY SCHEMA\_NAME                                           |
| SHOW TABLES                       | SELECT TABLE\_NAME AS 'Tables' FROM SYS.EXA\_ALL\_TABLES WHERE TABLE\_SCHEMA = CURRENT\_SCHEMA ORDER BY TABLE\_NAME |

## ODBC

The Exasol router communicates with Exasol using ODBC. In practice that
means that the way ODBC has been configured affects what actually must
be specified in [connections_string](#connection_string). It is possible
to provide all needed information in the connection string, but it is
advisable to at least have a `/etc/odbcinst.ini` or `~/.odbcinst.ini`
where the location of the ODBC driver is specified.
```
[EXAODBC]
Description = Exasol ODBC Driver
Driver = /path/to/libexaodbc.so
Threading = 2
FileUsage = 1
```
With that file present, the connection string could be like:
```
connection_string=DRIVER=EXAODBC;EXAHOST=127.0.0.1:8563;UID=sys;PWD=exasol;FINGERPRINT=NOCERTCHECK
```
By creating an `/etc/odbc.ini` or `~/.odbc.ini`, the information that must
be provided in the connection string can further be reduced. For instance,
with the following,
```
[ExasolDSN]
Driver = EXAODBC
EXAHOST = 127.0.0.1:8563
UID = sys
PWD = exasol
FINGERPRINT=NOCERTCHECK
```
the connection string can be reduced to
```
connection_string=DSN=ExasolDSN
```

## Examples

### SmartRouter

The primary purpose of the Exasol router is to be used together with
[SmartRouter](maxscale-smartrouter.md). A minimal configuration looks as follows:

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
It is assumed there is an `odbc.ini` ODBC configuration file containing
an `ExasolDSN` entry.

Here it is assumed there is an `odbc.ini` ODBC configuration file containing and `ExasolDSN` entry.

With this setup, all writes will always be sent to `Server1`. Reads will initially
be sent to both `Server1` and `ExasolService` and once SmartRouter has learnt what
kind of reads are best sent to which target, it will exclusively send reads to
either `Server1` or `ExasolService`, depending on which one is likely to provide
the response faster.

With this setup, all writes will always be sent to `Server1`. Reads will initially
be sent to both `Server1` and `ExasolService` and once SmartRouter has learnt what
kind of reads are best sent to which target, it will exclusively send reads to either
`Server1` or `ExasolService` depending on which one is likely to provide the response
faster.

Here, a single server was used as `master`. It could just as well be a
[ReadWriteSplit](maxscale-readwritesplit.md) service in front of a MariaDB cluster,
which would provide HA.

### Stand-Alone

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

With this setup, it is possible to connect using the regular `mariadb` command line
utility to the port 4008 and all queries will be sent to Exasol.
