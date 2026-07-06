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

_ExasolRouter_ is a router that in itself is capable of using the
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

_ExasolRouter_ is intended to be used with the value of the Exasol
setting `SQL_IDENTIFIER_COMPARISON` being `IGNORE CASE`. The value
will be checked and a warning issued if the value is something else.

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

The user and password to be used when accessing Exasol must be specified
using `UID` and `PWD` in the [connection\_string](maxscale-exasolrouter.md#connection_string).

## Preprocessing

The SQL supported by Exasol is not identical with the SQL supported by
MariaDB. To alleviate that, _ExasolRouter_ can either preprocess the
SQL internally or configure Exasol to do that. The approach is
selected using the setting [preprocessor](#preprocessor).

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
Here it is assumed there is an `odbc.ini` ODBC configuration file containing
an `ExasolDSN` entry.

### `login_timeout`

* Type: [duration](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: 30s

Defines the login timeout in seconds for a connection. Corresponds to the
Exasol connection string key `LOGINTIMEOUT`. If the value is set to 0, the timeout
will not explicitly be set, which means that a `LOGINTIMEOUT` in the connection string
will be honored. Otherwise this value will override.

### `query_timeout`

* Type: [duration](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: 30s

Defines the query timeout in seconds for a connection. Corresponds to the
Exasol connection string key `QUERYTIMEOUT`. If the value is set to 0, the timeout
will not explicitly be set, which means that a `QUERYTIMEOUT` in the connection string
will be honored. Otherwise this value will override.

### `preprocessor`

* Type: string
* Mandatory: No
* Dynamic: No
* Values: `disabled`, `external[:preprocessor-script-name]`, `internal[:preprocessor-script-path]`
* Default: `internal`, if the distribution provides a new enough Python implementation, `disabled` if not.

The values mean:

* `disabled`: The SQL is not transpiled internally and the external
  transpiler is not enabled. _ExasolRouter_ itself performs some
  essential transpiling, to make it possible to use the
  `mariadb` command line tool against Exasol.
* `external`: The preprocessor script is assumed to exist in Exasol
  and is taken into use in each session. By default, the preprocessor
  script is assumed to be `UTIL.maria_preprocessor`, but that can be
  changed by giving the name as an argument. If `external` is specified,
  the following statement will be executed for each session:
  `ALTER SESSION SET sql_preprocessor_script=<preprocessor-script-name>`,
  with `<preprocessor-script-name>` being by default `UTIL.maria_preprocessor`
  or what was explicitly specified.
* `internal`: Transpiling is performed internally using a Python script
  that utilizes the library
  [SQLGlot](https://sqlglot.com/sqlglot.html).
  By default, the script is assumed to be `maria_preprocessor.py` located
  in the _share_ directory of MaxScale. A different script can be used by
  providing it as an argument. Unless an absolute path is used, it is
  interpreted relative to the _share_ directory.

_Internal_ transpilation is performed using Python, but it is supported only
if the Linux distribution supports a sufficiently new version of Python.
On Ubuntu 24.04, Python 3.12 is sufficient, but on all other distributions
the version must be at least Python 3.13. In practice this means that
internal transpilation is available on the following distributions:

* Ubuntu 24.04
* Ubuntu 26.04
* Redhat 9
* Redhat 10
* Debian 13

On all other platforms, specifying `internal` will cause a startup error.

### `python_libdir`

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `<maxscale-libdir>/python3/site-packages`

The library from which [SQLGlot](https://sqlglot.com/sqlglot.html) is loaded,
if the value of `preprocessor` is `internal`.

### `appearance`

* Type: [enum](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `read_only`, `read_write`
* Default: `read_only`

Specifies how _ExasolRouter_ appears to other components of MaxScale.
This is of relevance only if another service uses an Exasol router service
as target.

**Note** Irrespective of the value, the router does not in any way restrict
what kind of queries can be run through the router.

### `kill_connection_timeout`

* Type: [duration](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: 10s

The duration that an unused kill connection is kept alive after the
last KILL command before it is automatically closed; a value of 0
closes it immediately after each use.

### `quote_identifiers`

* Type: [boolean](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: true

Whether _ExasolRouter_ should quote identifiers. This applies always
when a `COM_INIT_DB` packet is converted to an `OPEN SCHEMA ...`
statement and when the value of `preprocessor` is `disabled`.

In the latter case, currently it only affects whether 'USE db' becomes
'OPEN SCHEMA db' or 'OPEN SCHEMA \"db\"'.

## Transformations

### `COM_INIT_DB`

The MariaDB `COM\_INIT\_DB` protocol packet, using which the default database
is changed, is transformed into the statement `OPEN SCHEMA <db>`.

### SQL

If the value of `preprocessor` is `disabled`, _ExasolRouter_ itself
translates some MariaDB constructs to equivalent Exasol constructs.

Currently a transformation will be made _only_ if there is an **exact** match
(apart from case and differences in whitespace) with the MariaDb SQL.

| MariaDb                           | Exasol                                                                                                              |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `SELECT @@VERSION\_COMMENT LIMIT 1` | `SELECT 'Exasol' AS '@@version\_comment' LIMIT 1`                                                                     |
| `SELECT DATABASE()`                 | `SELECT TABLE\_NAME AS 'Database()' FROM EXA\_ALL\_TABLES WHERE TABLE\_SCHEMA = CURRENT\_SCHEMA`                      |
| `SHOW DATABASES`                    | `SELECT SCHEMA\_NAME AS 'Database' FROM EXA\_SCHEMAS ORDER BY SCHEMA\_NAME`                                           |
| `SHOW TABLES`                       | `SELECT TABLE\_NAME AS 'Tables' FROM SYS.EXA\_ALL\_TABLES WHERE TABLE\_SCHEMA = CURRENT\_SCHEMA ORDER BY TABLE\_NAME` |

## ODBC

_ExasolRouter_ communicates with Exasol using ODBC. The necessary
ODBC driver is included in the `maxscale-exasol` package and the
files are copied to
```
<maxscale-libdir>/exasol/M.N.O/libexaodbc.so
<maxscale-libdir>/exasol/M.N.O/libexacli.so
```
where `M.N.O` is the version of the ODBC library, e.g. `26.2.6`.
`libexaodbc.so` is the actual ODBC driver and `libexacli.so` the
lower level library using which the ODBC driver is implemented.

In the `exasol` directory there is a symbolic link `current` pointing
to the `M.N.O` directory. E.g.
```
<maxscale-libdir>/exasol/current -> 26.2.6
```

The included driver version may change in each release of MaxScale.
Hence, by referring to `current`, a MaxScale configuration will continue
to work even if the included Exasol ODBC driver version would change.
If it is important to become aware of a changed driver version, the
driver can be referred to using the directory and not the symbolic link,
as that will no longer work, if the included Exasol driver is updated
in a MaxScale patch release.

In [connection_string](#connection_string), the driver can be referred
to directly as in
```
connection_string=DRIVER=/path/to/exasol/current/libexaodbc.so;EXAHOST=127.0.0.1:8563;UID=sys;PWD=exasol;FINGERPRINT=NOCERTCHECK
```

Alternatively, the driver location can be specified in `/etc/odbcinst.ini`
or `~/.odbcinst.ini`, in which case it need not be specified in
`connection_string`.
```
[EXAODBC]
Description = Exasol ODBC Driver
Driver = /path/to/exasol/current/libexaodbc.so
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

The primary purpose of _ExasolRouter_ is to be used together with
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

With this setup, all writes will always be sent to `Server1`. Reads will initially
be sent to both `Server1` and `ExasolService` and once SmartRouter has learnt what
kind of reads are best sent to which target, it will exclusively send reads to
either `Server1` or `ExasolService`, depending on which one is likely to provide
the response faster.

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
