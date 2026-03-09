---
description: >-
  Explore connection redirection. This section details how the client/server
  protocol handles redirection for high availability and load balancing,
  ensuring seamless database access and failover.
---

# Connection Redirection Mechanism in the MariaDB Client/Server Protocol

{% hint style="info" %}
This functionality is available from MariaDB 11.3.
{% endhint %}

A connection redirection mechanism was added via [MDEV-15935](https://jira.mariadb.org/browse/MDEV-15935).

Redirection mechanisms are widely used in proxy-based scenarios.

Previously, when multiple servers shared one proxy, the proxy forwarded all packets between servers and clients. Thus, the proxy added latency, consuming computing resources and impacting overall performance. For scenarios with many short connections, such as WordPress, latency can be a critical issue.

With a redirection mechanism, much like HTTP redirects or Oracle redirected connections, clients get the servers’ address from proxies and connect to servers transparently, without latency and without wasting resources.

## Usage

Redirection is handled through a new system variable, [redirect\_url](optimization-and-tuning/system-variables/server-system-variables.md#redirect_url). The value defaults to an empty string, but can also contain a connection string in the conventional format (in the style of a Connector/C etc. connection url), like this:

```
{mysql,mariadb}://host[:port]
```

Here, _`host`_ is an arbitrary string not containing colons, and _`port`_ is a number between `0` and `65535` inclusive.

This variable is appended to the default value of the [session\_track\_system\_variables](optimization-and-tuning/system-variables/server-system-variables.md#session_track_system_variables) system variable. Unless empty, clients are redirected to the specified server.

## Use Cases

* Always redirect all clients to a new location:
  * Set `@@global.redirect_url`, or start the server with `--redirect-url=`_`url`_, or add that setting to the [server configuration file](../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md).
* Redirect to a group of servers randomly:
  * Create a table with connection URLs, one per row.
  * Use an SQL script that selects a random row from that table, and sets `@@redirect_url` to this value.
  * Specify this script in the [`--init-connect`](optimization-and-tuning/system-variables/server-system-variables.md#init_connect) server parameter.
* Dynamically redirect from the primary server to one of the replicas:
  * Same as before, but use [INFORMATION\_SCHEMA.PROCESSLIST](../reference/system-tables/information-schema/information-schema-tables/information-schema-processlist-table.md) to get the list of active replicas.

## Example

```sql
SET GLOBAL redirect_url="mysql://mariadb.org:12345";
```

Invalid formats are not permitted:

```sql
SET GLOBAL redirect_url="mysql://mariadb.org:"; 
ERROR 1231 (42000): Variable 'redirect_url' can't be set to the value of 'mysql://mariadb.org:'
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
