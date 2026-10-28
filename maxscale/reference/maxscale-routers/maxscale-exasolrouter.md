---
description: >-
  Route analytical queries to an Exasol cluster. This router integrates Exasol
  with MaxScale and is often used with SmartRouter for hybrid
  transactional/analytical workloads.
---

# MaxScale Exasolrouter

{% hint style="info" %}
This functionality is available from MaxScale 25.10.1.

The router is provided in the `maxscale-exasol` package, which must be
installed separately.
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
[odbc\_connection\_string](#odbc_connection_string) setting.

However, if _ExasolRouter_ is used standalone, a MariaDB server or a service
should be specified using `targets`. _ExasolRouter_ will not route to it,
but it will use it for authenticating clients. Exasol will still be accessed
on behalf of all clients using the credentials specified in the
[odbc\_connection\_string](#odbc_connection_string).

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
using `UID` and `PWD` in the [odbc\_connection\_string](maxscale-exasolrouter.md#odbc_connection_string).

## Preprocessing

The SQL supported by Exasol is not identical with the SQL supported by
MariaDB. To alleviate that, _ExasolRouter_ can either preprocess the
SQL internally or configure Exasol to do that. The approach is
selected using the setting [preprocessor](#preprocessor).

## Settings

### `odbc_connection_string`

* Type: string
* Mandatory: Yes
* Dynamic: No
* Description: Specifies the Exasol ODBC connection string used to connect to the database.

Specifies the Exasol connection string. The exact content depends on the
contents of `odbc.ini` and `odbcinst.ini`.

For example:
```
odbc_connection_string=DSN=ExasolDSN;UID=sys;PWD=exasol;FINGERPRINT=NOCERTCHECK
```
Here it is assumed there is an `odbc.ini` ODBC configuration file containing
an `ExasolDSN` entry.

**From MaxScale 26.10,** the values of the credential keys `UID`, `USER`,
`USERNAME`, `PWD`, `PASSWORD` and `PASSWD` are shown as `*****` where
MaxScale displays the setting, for instance in the output of
`maxctrl show service`.

**From MaxScale 26.10,** unless the connection string contains
`ANSIDATAENCODING`, MaxScale adds `ANSIDATAENCODING=UTF-8` to it. Without
it the Exasol ODBC driver would encode character data using the locale
of the MaxScale process and characters outside ASCII would be lost. If
the connection string already contains `ANSIDATAENCODING`, it is left as
it is and a warning is logged, as _ExasolRouter_ will not function
properly unless the value is equivalent to UTF-8.

### `odbc_login_timeout`

* Type: [duration](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 30s
* Description: Sets the login timeout for a connection, overriding `LOGINTIMEOUT` in the connection string. A value of `0` leaves the connection string value in effect.

Defines the login timeout in seconds for a connection. Corresponds to the
Exasol connection string key `LOGINTIMEOUT`. If the value is set to 0, the timeout
will not explicitly be set, which means that a `LOGINTIMEOUT` in the connection string
will be honored. Otherwise this value will override.

**From MaxScale 26.10,** the setting can be modified at runtime. A change
only affects sessions that are created after the change.

### `odbc_query_timeout`

* Type: [duration](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 30s
* Description: Sets the query timeout for a connection, overriding `QUERYTIMEOUT` in the connection string. A value of `0` leaves the connection string value in effect.

Defines the query timeout in seconds for a connection. Corresponds to the
Exasol connection string key `QUERYTIMEOUT`. If the value is set to 0, the timeout
will not explicitly be set, which means that a `QUERYTIMEOUT` in the connection string
will be honored. Otherwise this value will override.

**From MaxScale 26.10,** the setting can be modified at runtime. A change
only affects sessions that are created after the change.

### `preprocessor`

* Type: string
* Mandatory: No
* Dynamic: No
* Values: `disabled`, `external[:preprocessor-script-name]`, `internal[:preprocessor-script-path]`
* Default: `internal`, if the distribution provides a new enough Python implementation, `disabled` if not.
* Description: Determines how MariaDB SQL is transpiled for Exasol: internally with a Python script, externally by a preprocessor script in Exasol, or not at all.

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

The bundled `maria_preprocessor.py` is installed by the `maxscale-exasol`
package. The latest version of the script is available from the
[exasol-mariadb-compat](https://github.com/mariadb-corporation/exasol-mariadb-compat/blob/main/preprocessor/maria_preprocessor.py)
repository and can be used with `internal` as it is. For example:
```
preprocessor=internal:/path/to/maria_preprocessor.py
```

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
* Description: Specifies the directory that SQLGlot is loaded from when `preprocessor` is `internal`.

The library from which [SQLGlot](https://sqlglot.com/sqlglot.html) is loaded,
if the value of `preprocessor` is `internal`.

### `appearance`

* Type: [enum](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `read_only`, `read_write`
* Default: `read_only`
* Description: Determines whether the Exasolrouter appears as read-only or read-write to other MaxScale components.

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
* Description: Sets how long an unused kill connection is kept alive after the last KILL command. A value of `0` closes it immediately after each use.

The duration that an unused kill connection is kept alive after the
last KILL command before it is automatically closed; a value of 0
closes it immediately after each use.

### `quote_identifiers`

* Type: [boolean](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: true
* Description: Determines whether the router quotes identifiers when converting a `COM_INIT_DB` packet to `OPEN SCHEMA`, and when transpiling internally with `preprocessor` set to `disabled`.

Whether _ExasolRouter_ should quote identifiers. This applies always
when a `COM_INIT_DB` packet is converted to an `OPEN SCHEMA ...`
statement and when the value of `preprocessor` is `disabled`.

In the latter case, it only affects whether 'USE db' becomes
'OPEN SCHEMA db' or 'OPEN SCHEMA \"db\"'.

### `impersonate`

{% hint style="info" %}
This setting is available from MaxScale 26.10.
{% endhint %}

* Type: [boolean](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: false
* Description: Determines whether the Exasol session of a client assumes the identity of the authenticated MariaDB user by using `IMPERSONATE`.

Whether the Exasol session of a client should assume the identity of the
client.

By default all clients access Exasol using the account specified in
[odbc\_connection\_string](#odbc_connection_string). If `impersonate` is
enabled, MaxScale issues `IMPERSONATE` on the Exasol connection using the
name of the authenticated MariaDB user, so that the privileges of the
client's own Exasol user are applied.

* The account in `odbc_connection_string` must have the Exasol system
  privilege `IMPERSONATE ANY USER`.
* The client must have an Exasol user with the name of the MariaDB user.
  A client that has none will not get a usable session.
* Exasol user names are always upper case, so the MariaDB users `bob` and
  `BOB` both map to the Exasol user `BOB`.
* The users to be impersonated need not have the privilege `CREATE SESSION`,
  as the session is opened by the account in `odbc_connection_string`.

An Exasol `IMPERSONATE` cannot be undone, so changing the user of a
session is not supported, see [Limitations](#limitations).

### `gtid_polling`

{% hint style="info" %}
This setting is available from MaxScale 26.10.
{% endhint %}

* Type: [boolean](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true
* Description: Determines whether MaxScale polls the GTID position that `exasol_cdc` writes into Exasol, for use in SmartRouter causal reads.

Whether MaxScale should poll the GTID position that `exasol_cdc` writes into
the Exasol table `maxscale_cdc.gtid_current_pos`.

The position is used for causal reads when the service is a target of
[SmartRouter](maxscale-smartrouter.md). A read that SmartRouter would send to
Exasol is then held until the position shows that Exasol has applied the last
write of the session, see
[causal\_reads](maxscale-smartrouter.md#causal_reads).

The setting should be disabled if `exasol_cdc` is not used.

### `gtid_poll_interval`

{% hint style="info" %}
This setting is available from MaxScale 26.10.
{% endhint %}

* Type: [duration](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 1s
* Description: Sets how often the GTID position is polled when `gtid_polling` is enabled.

How often the GTID position is polled, see [gtid\_polling](#gtid_polling).
The minimum is 100ms.

A causal read may have to wait up to this long, in addition to the time it
takes `exasol_cdc` to apply a change.

## Transformations

### `COM_INIT_DB`

The MariaDB `COM_INIT_DB` protocol packet, using which the default database
is changed, is transformed into the statement `OPEN SCHEMA <db>`.

### SQL

If the value of `preprocessor` is `disabled`, _ExasolRouter_ itself
translates some MariaDB constructs to equivalent Exasol constructs.

A transformation will be made _only_ if there is an **exact** match
(apart from case and differences in whitespace) with the MariaDb SQL.

| MariaDb                           | Exasol                                                                                                              |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `SELECT @@VERSION_COMMENT LIMIT 1` | `SELECT 'Exasol' AS '@@version_comment' LIMIT 1`                                                                     |
| `SELECT DATABASE()`                 | `SELECT TABLE_NAME AS 'Database()' FROM EXA_ALL_TABLES WHERE TABLE_SCHEMA = CURRENT_SCHEMA`                      |
| `SHOW DATABASES`                    | `SELECT SCHEMA_NAME AS 'Database' FROM EXA_SCHEMAS ORDER BY SCHEMA_NAME`                                           |
| `SHOW TABLES`                       | `SELECT TABLE_NAME AS 'Tables' FROM SYS.EXA_ALL_TABLES WHERE TABLE_SCHEMA = CURRENT_SCHEMA ORDER BY TABLE_NAME` |

## ODBC

_ExasolRouter_ communicates with Exasol using ODBC. The necessary
ODBC driver is included in the `maxscale-exasol` package and the
files are copied to
```
<maxscale-libdir>/exasol/M.N.O/lib/libexaodbc.so
<maxscale-libdir>/exasol/M.N.O/lib/libexacli.so
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

In [odbc_connection_string](#odbc_connection_string), the driver can be referred
to directly as in
```
odbc_connection_string=DRIVER=/path/to/exasol/current/lib/libexaodbc.so;EXAHOST=127.0.0.1:8563;UID=sys;PWD=exasol;FINGERPRINT=NOCERTCHECK
```

Alternatively, the driver location can be specified in `/etc/odbcinst.ini`
or `~/.odbcinst.ini`, in which case it need not be specified in
`odbc_connection_string`.
```
[EXAODBC]
Description = Exasol ODBC Driver
Driver = /path/to/exasol/current/lib/libexaodbc.so
Threading = 2
FileUsage = 1
```
With that file present, the connection string could be like:
```
odbc_connection_string=DRIVER=EXAODBC;EXAHOST=127.0.0.1:8563;UID=sys;PWD=exasol;FINGERPRINT=NOCERTCHECK
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
odbc_connection_string=DSN=ExasolDSN
```

## Result Sets

{% hint style="info" %}
This functionality is available from MaxScale 26.10.
{% endhint %}

The type of each column is derived from the metadata of the result that the
Exasol ODBC driver provides.

## Killing a Query

A statement running on Exasol is killed using the `KILL STATEMENT` statement
of Exasol, and not using a MariaDB `KILL` statement. The session in which the
statement runs is found in the table `EXA_DBA_SESSIONS`.
```
SELECT SESSION_ID, SQL_TEXT FROM EXA_DBA_SESSIONS WHERE STATUS = 'EXECUTE SQL';
KILL STATEMENT IN SESSION <session-id>;
```
The statement is sent to Exasol as is, irrespective of the value of
[preprocessor](#preprocessor).

A MariaDB `KILL` statement, such as `KILL QUERY 123`, is handled by MaxScale
and does not reach Exasol. The number is the connection id that MaxScale has
given the client, which Exasol does not know. MaxScale carries out such a
statement by sending a kill to the connections it has to MariaDB servers, and
as _ExasolRouter_ has no such connections, nothing is killed in Exasol.

[SmartRouter](maxscale-smartrouter.md) kills the query on Exasol when it has
received the response from another target and no longer needs the response
from Exasol. The kill is made using a separate connection, which is kept alive
for [kill\_connection\_timeout](#kill_connection_timeout) after the last use.

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

[Monitor]
type=monitor
module=mariadbmon
user=MyMonitorUser
password=MyMonitorPassword
servers=Server1

[ExasolService]
type=service
router=exasolrouter
odbc_connection_string=DSN=ExasolDSN;UID=sys;PWD=exasol
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

[Monitor]
type=monitor
module=mariadbmon
user=MyMonitorUser
password=MyMonitorPassword
servers=Server1

[ExasolService]
type=service
router=exasolrouter
odbc_connection_string=DSN=ExasolDSN;UID=sys;PWD=exasol;FINGERPRINT=NOCERTCHECK
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

## Router Diagnostics

{% hint style="info" %}
This functionality is available from MaxScale 26.10.
{% endhint %}

The `router_diagnostics` output of _ExasolRouter_, for instance in the output
of `maxctrl show service`, has the following field.

* `gtid_polling`: The state of the polling of the GTID position, see
  [gtid\_polling](#gtid_polling). If polling is disabled, the object only
  has the field `state`, with the value `disabled`. Otherwise it has the
  following fields.
  * `state`: `starting` before the first poll has completed, `ok` if the
    last poll succeeded and `failing` if it did not.
  * `interval`: The polling interval, e.g. `1000ms`.
  * `gtid`: The GTID position most recently read from Exasol, or `null` if
    none has been read.
  * `last_success`: The time of the last successful poll, or `null`.
  * `last_failure`: The time of the last failed poll, or `null`.
  * `last_error`: The error of the last failed poll, or `null`.
  * `consecutive_failures`: The number of failed polls since the last
    successful one.

## Limitations

* Changing the user of a session using `COM_CHANGE_USER` is not supported.
  The session is closed with an error message and the client must reconnect
  as the desired user.
* A MariaDB `KILL` statement does not kill a running statement on Exasol, see
  [Killing a Query](#killing-a-query).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
