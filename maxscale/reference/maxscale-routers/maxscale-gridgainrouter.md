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

**From MaxScale 26.10.1,** the password in the connection string may be
either a plain text password or an [encrypted password](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#encrypting-passwords).
An encrypted password is created using `maxpasswd` and is given as the
value of `PWD`, `PASSWORD` or `PASSWD`, whichever the connection string
uses.
```
odbc_connection_string=DRIVER={Apache Ignite};ADDRESS=127.0.0.1:10800;USER=ignite;PASSWORD=61DD955512C39A4A8BC4BB1E5F116705
```
MaxScale decrypts the password before the connection string is given to
the ODBC driver. Only the password can be encrypted.

### `odbc_login_timeout`

* Type: [duration](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#durations)
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

* Type: [duration](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#durations)
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

* Type: [enum](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#enumerations)
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

* Type: [duration](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#durations)
* Mandatory: No
* Dynamic: No
* Default: 10s
* Description: Sets how long an unused kill connection is kept alive after the last `KILL` command; `0` closes it immediately after each use.

The duration that an unused kill connection is kept alive after the
last KILL command before it is automatically closed; a value of 0
closes it immediately after each use.

### `poll_interval`

{% hint style="info" %}
This setting is available from MaxScale 26.10.1.
{% endhint %}

* Type: [duration](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 1s
* Description: Sets how often GridGain is polled for whether it can be reached.

How often _GridGainRouter_ polls GridGain. A poll finds out whether
GridGain can be reached, see
[Availability of GridGain](#availability-of-gridgain).
The minimum is 100ms.

The interval affects how soon it is noticed that GridGain cannot be reached,
and that it can be reached again.

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

The schema is fixed when the connection to GridGain is made. A `USE`
statement (`COM_INIT_DB`) that names the schema in use is accepted and
does nothing. A `USE` statement that names another schema fails with the
error 1235

> Changing the database is not supported by the router of this service;
> reconnect with the desired database instead.

The schema can also be changed by changing the user, as a new connection
to GridGain is then made, see
[Changing the User and Resetting the Connection](#changing-the-user-and-resetting-the-connection).

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

## Loss of the Connection

{% hint style="info" %}
This functionality is available from MaxScale 26.10.1.
{% endhint %}

If the connection to GridGain is lost, for instance because GridGain is
restarted, the session is closed. The client first gets the error of the
statement that failed. If the connection is lost while a large result set
is being sent, the client may instead only notice that the connection is
closed. That is, the session behaves as a connection to a MariaDB server
that goes away.

A `COM_PING` is sent to GridGain as the statement `SELECT 1`. If that
fails, the session is closed without a response, as a server that cannot
be reached does not answer a ping either.

If _GridGainRouter_ is used via [SmartRouter](maxscale-smartrouter.md) and
GridGain is not the primary, a lost connection to GridGain does not close
the session of SmartRouter. It continues using its other targets, and
reconnects to GridGain the next time a query is to be sent to it. If it is
known by then that GridGain cannot be reached, see
[Availability of GridGain](#availability-of-gridgain), the query is handled
according to
[on\_unavailable\_target](maxscale-smartrouter.md#on_unavailable_target).
If it is not yet known, the session may be closed. If GridGain is the
primary, the session is closed.

## Availability of GridGain

{% hint style="info" %}
This functionality is available from MaxScale 26.10.1.
{% endhint %}

_GridGainRouter_ polls GridGain at the interval specified with
[poll\_interval](#poll_interval), using a connection of its own that is
made with [odbc\_connection\_string](#odbc_connection_string).
The poll consists of the statement `SELECT 1`.

When a poll shows that GridGain cannot be reached, a warning is logged and
the service is marked as being down. When a later poll succeeds, a notice
is logged and the service is marked as running again. The current state is
shown in the [Router Diagnostics](#router-diagnostics).

The state of the service matters when the service is a target of
[SmartRouter](maxscale-smartrouter.md). SmartRouter does not connect to a
service that is down, so its sessions do not have to wait for a connection
attempt to GridGain to fail. Once the service is running again, SmartRouter
connects to GridGain the next time a query is to be sent to it. That applies
also to sessions that were created while GridGain could not be reached.

If GridGain accepts connections but does not respond, for instance because
it is hung, that is not necessarily noticed, in which case the service
remains marked as running.

## Changing the User and Resetting the Connection

{% hint style="info" %}
This functionality is available from MaxScale 26.10.1.
{% endhint %}

When a client changes the user (`COM_CHANGE_USER`) or resets the
connection (`COM_RESET_CONNECTION`), _GridGainRouter_ makes a new
connection to GridGain and uses it instead of the current one. The client
thus gets a new GridGain session, with nothing left of the state of the
previous one.

When the user is changed, the default database specified with the change
is used as the schema of the new connection, see [Schemas](#schemas). If
none is specified, the change fails with the error 1046

> A database must be specified with the router of this service.

If the connection cannot be made, the client gets an error. In both
cases the session continues as it was.

When the connection is reset, the schema is kept. If the new connection
cannot be made, the session is closed.

If _GridGainRouter_ is used via [SmartRouter](maxscale-smartrouter.md), a
change of user must succeed on all targets of SmartRouter, see
[Changing the User](maxscale-smartrouter.md#changing-the-user).

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

## Router Diagnostics

{% hint style="info" %}
This functionality is available from MaxScale 26.10.1.
{% endhint %}

The `router_diagnostics` output of _GridGainRouter_, for instance in the
output of `maxctrl show service`, has the following field.

* `backend`: Whether GridGain can be reached, see
  [Availability of GridGain](#availability-of-gridgain).
  * `state`: `starting` before the first poll has completed, `reachable` if
    the last poll showed that GridGain can be reached and `unreachable` if it
    showed that it cannot.
  * `last_success`: The time of the last poll that showed that GridGain can
    be reached, or `null`.
  * `last_failure`: The time of the last poll that showed that GridGain
    cannot be reached, or `null`.
  * `last_error`: The error of that poll, or `null`.

## Limitations

* The schema cannot be changed with a `USE` statement, see
  [Schemas](#schemas).
* A `KILL` statement with a MaxScale connection id does not kill a running
  query on GridGain, see [Killing a Query](#killing-a-query).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
