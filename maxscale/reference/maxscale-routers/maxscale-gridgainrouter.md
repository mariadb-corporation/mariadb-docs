---
description: >-
  Run queries on a GridGain cluster using ODBC. The router sends the
  statements to GridGain as they are.
---

# MaxScale GridGainrouter

{% hint style="info" %}
This functionality is available from MaxScale 26.10.
{% endhint %}

## Overview

_GridGainRouter_ is a router that runs the queries it receives on a GridGain
cluster, using ODBC.

Unlike most other routers, the targets _GridGainRouter_ routes to are not
specified using `servers`, `targets`, or `cluster` settings in the
configuration file. Instead, GridGain is specified using the
[odbc\_connection\_string](#odbc_connection_string) setting.

However, if _GridGainRouter_ is used standalone, a MariaDB server or a service
should be specified using `targets`. _GridGainRouter_ will not route to it,
but it will use it for authenticating clients. GridGain will still be
accessed on behalf of all clients using the credentials specified in the
[odbc\_connection\_string](#odbc_connection_string).

The statements are sent to GridGain as they are. MariaDB specific syntax is
not translated, so the statements must be valid in the SQL of GridGain.

## Users

A `user` and `password` must _always_ be specified, but will only be used
if a MariaDB server/service has been specified as a target, and only for
authenticating a client. If that functionality is not needed, they can be
left empty, but must still be present.
```
user=
password=
```

The user and password to be used when accessing GridGain, if any, must be
specified in the [odbc\_connection\_string](#odbc_connection_string), using
the keys of the ODBC driver.

## Settings

### `odbc_connection_string`

* Type: string
* Mandatory: Yes
* Dynamic: No
* Description: Specifies the ODBC connection string used to connect to GridGain.

Specifies the GridGain connection string. The exact content depends on the
ODBC driver and on the contents of `odbc.ini` and `odbcinst.ini`.

For example:
```
odbc_connection_string=DRIVER={Apache Ignite};ADDRESS=127.0.0.1:10800
```

A `SCHEMA` need not be specified, as MaxScale appends the default schema
that the client specified when it connected, see [Schemas](#schemas).

The values of the credential keys `UID`, `USER`, `USERNAME`, `PWD`,
`PASSWORD` and `PASSWD` are shown as `*****` where MaxScale displays the
setting, for instance in the output of `maxctrl show service`.

### `odbc_login_timeout`

* Type: [duration](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 30s
* Description: Sets the login timeout for a connection.

Defines the login timeout in seconds for a connection. If the value is set
to 0, the timeout is not set explicitly, which means that the default of the
ODBC driver applies.

A change at runtime only affects sessions that are created after the
change.

### `odbc_query_timeout`

* Type: [duration](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 30s
* Description: Sets the query timeout for a connection.

Defines the query timeout in seconds for a connection. If the value is set
to 0, the timeout is not set explicitly, which means that the default of the
ODBC driver applies.

A change at runtime only affects sessions that are created after the
change.

### `appearance`

* Type: [enum](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `read_only`, `read_write`
* Default: `read_only`
* Description: Determines whether the router appears as read-only or read-write to other MaxScale components.

Specifies how _GridGainRouter_ appears to other components of MaxScale.
This is of relevance only if another service uses a GridGain router service
as target.

**Note** Irrespective of the value, the router does not in any way restrict
what kind of queries can be run through the router.

### `kill_connection_timeout`

* Type: [duration](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: 10s
* Description: Sets how long an unused kill connection is kept alive after the last `KILL` command; `0` closes it immediately after each use.

The duration that an unused kill connection is kept alive after the
last KILL command before it is automatically closed; a value of 0
closes it immediately after each use.

## Schemas

A client must specify a default schema when it connects, for instance
using `--database` with the `mariadb` command line client. If it does
not, the session is refused with the error 1815 (`Session creation failed`)
and an error is logged.

If a MariaDB server or service is specified using `targets`, the client is
authenticated using it. The default schema must then also exist as a
database on that server, as the client is otherwise refused with the error
1049 (`Unknown database`) before GridGain is involved.

The default schema of the client is used as the `SCHEMA` of the ODBC
connection to GridGain. GridGain may silently fall back to the schema
`PUBLIC` if the schema does not exist, so MaxScale verifies that the
schema in use is the requested one. If it is not, the session is refused
with the error 1927 (`Could not verify the current schema`).

The schema is fixed for the lifetime of the session. A `USE` statement
(`COM_INIT_DB`) that names the schema the client connected with is
accepted and does nothing. A `USE` statement that names another schema
fails with the error 1235

> Changing the database is not supported by the router of this service;
> reconnect with the desired database instead.

## Queries

The statements are sent to GridGain as they are, so syntax that is specific
to MariaDB, such as `SELECT @@version`, is rejected by GridGain and the
error of GridGain is returned to the client.

The only change is that a comment of the form `/* MXS_<process-id>_<n> */`
is added in front of each statement, except in front of a `KILL` statement.
With the comment the running query can be identified, and thus killed, on
GridGain.

### Killing a Query

A query running on GridGain is killed using the `KILL QUERY` statement of
GridGain, and not using a MariaDB `KILL` statement. The identifier of the
query is found in the table `SYS.SQL_QUERIES`, and must be quoted.
```
SELECT QUERY_ID, SQL FROM SYS.SQL_QUERIES;
KILL QUERY '<query-id>';
```

A MariaDB `KILL` statement, such as `KILL QUERY 123`, is handled by MaxScale
and does not reach GridGain. The number is the connection id that MaxScale
has given the client, which GridGain does not know. MaxScale carries out such
a statement by sending a kill to the connections it has to MariaDB servers,
and as _GridGainRouter_ has no such connections, nothing is killed.

[SmartRouter](maxscale-smartrouter.md) kills the query on GridGain when it
has received the response from another target and no longer needs the
response from GridGain. The kill is made using a separate connection, which
is kept alive for [kill\_connection\_timeout](#kill_connection_timeout) after
the last use.

## Result Sets

The type of each column is derived from the metadata of the result that the
ODBC driver provides. Character data is returned to the client as UTF-8
(`utf8mb4`).

## ODBC

_GridGainRouter_ communicates with GridGain using ODBC, so an ODBC driver
for GridGain is needed. The router has been verified using the Apache Ignite
ODBC driver.

## Examples

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

[GridGainService]
type=service
router=gridgainrouter
odbc_connection_string=DRIVER={Apache Ignite};ADDRESS=127.0.0.1:10800
targets=Server1
user=MyServiceUser
password=MyServicePassword

[GridGainListener]
type=listener
service=GridGainService
port=4008
```

With this setup, it is possible to connect using the regular `mariadb`
command line utility to the port 4008, specifying a default schema, and all
queries will be sent to GridGain.
```
mariadb --port=4008 --database=PUBLIC
```

## Limitations

* The schema cannot be changed after the connection has been made, see
  [Schemas](#schemas).
* Changing the user of a session using `COM_CHANGE_USER` is not supported.
  The session is closed with an error message and the client must reconnect
  as the desired user.
* A `KILL` statement with a MaxScale connection id does not kill a running
  query on GridGain, see [Killing a Query](#killing-a-query).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
