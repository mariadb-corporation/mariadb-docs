---
description: >-
  How GridGain MCP Server protects your data: a dedicated read-only cluster account, the statement check, TLS, and what the account permissions do not cover.
---

# Security

GridGain MCP Server lets an AI assistant run queries on your cluster.
The server and the cluster protect your data in several ways, but some of the protection depends on how you set up the cluster.

## Protection Layers

Each layer covers a different risk. The cluster account is the main protection, and the other layers add to it.

| Layer | What it does |
| ----- | ------------ |
| Dedicated account | The cluster decides what the server can read. See [Preparing a Cluster Account](#preparing-a-cluster-account). |
| Statement check | The server refuses everything except one `SELECT` query before it sends anything to the cluster. This protects against the assistant's mistakes, but it is not a security boundary. |
| Credentials stay outside the assistant | You set the user name and password in the server's environment. No tool takes credentials as an argument or returns the password. |
| Encrypted connection | The server can connect to the cluster over TLS, with a client certificate if the cluster requires it. See [TLS and Mutual TLS](#tls-and-mutual-tls). |
| Rate limit and audit log | The server limits how often the assistant can call a tool, and it records tool calls in an audit log. See [Operating MCP Server](operations.md) for what the log records and what it leaves out. |

## Preparing a Cluster Account

The account that the server uses decides what the assistant can read.
Do not run the server with an administrator account or with your own account.
Create a dedicated account for the server, and give it only the permission to read the caches that the assistant may query.

The account needs `CACHE_READ` for those caches and no other permissions.
Set `defaultAllow` to `false`, so that the account gets no permissions that you do not list.
The following permissions let the account read only the cache of the `PERSON` table:

```json
{
    defaultAllow: false,
    {
        cache: "SQL_PUBLIC_PERSON",
        permissions: [CACHE_READ]
    }
}
```

With this account, the cluster refuses `INSERT`, `UPDATE`, `DELETE`, `MERGE`, `CREATE TABLE`, and `DROP TABLE`, even if a statement passes the server's statement check.

{% hint style="info" %}
Permissions apply only when authentication is enabled on the cluster.
See [Authentication](../../../security/authentication.md) and [Authorization and Permissions](../../../security/authorization-permissions.md).
On a cluster without authorization, the account cannot limit the server, and only the statement check protects your data.
{% endhint %}

## Limits of Account Permissions

The account's permissions do not cover everything that a query can do.
In the following cases, only the server's statement check or the cluster configuration protects your data.

### Schema Changes

Among the schema changes, the cluster checks permissions only for `CREATE TABLE` and `DROP TABLE`.
Any account can run the following statements:

- `CREATE INDEX` and `DROP INDEX`
- `ALTER TABLE` with `ADD COLUMN`, `DROP COLUMN`, `LOGGING`, or `NOLOGGING`

Only the server's statement check stops these statements.

### User-Defined Functions

A user-defined function runs with all its effects.
A query that does not use a cache is not checked against cache permissions, so `SELECT my_function()` runs for any account.

Do not install user-defined functions with side effects on a cluster that the server connects to.

### System Views

Any account can read most `SYS` views.
Only `SQL_QUERIES`, `SQL_QUERIES_HISTORY`, and `SQL_PLANS_HISTORY` require the `GET_QUERY_VIEWS` permission.

`SYS.NODE_ATTRIBUTES` holds the environment variables and system properties of every node, unless you limit them with `IgniteConfiguration.setIncludeProperties`.
The server's statement check allows only eight system views, and `NODE_ATTRIBUTES` is not one of them.
Other clients of the cluster can still read the view. To protect the properties from all clients, limit them on the nodes.

## TLS and Mutual TLS

TLS encrypts the connection between the server and the cluster.
The cluster must accept TLS connections from thin clients. See [SSL/TLS](../../../security/ssl-tls.md).

To encrypt the connection, set the following variables:

```shell
GRIDGAIN_SSL_MODE=REQUIRED
GRIDGAIN_SSL_TRUSTSTORE_PATH=/path/to/truststore.jks
GRIDGAIN_SSL_TRUSTSTORE_PASSWORD=...
```

If the cluster requires a client certificate (mutual TLS), also set the key store:

```shell
GRIDGAIN_SSL_KEYSTORE_PATH=/path/to/keystore.jks
GRIDGAIN_SSL_KEYSTORE_PASSWORD=...
```

The server checks the stores when it starts. It does not start if a store is missing, of a wrong type, or protected by a different password.
For all TLS settings and checks, see [TLS](configuration.md#tls).

{% hint style="info" %}
If `GRIDGAIN_SSL_MODE` does not match the cluster, the connection fails, and the failure can look like an unreachable cluster.
Check that `GRIDGAIN_SSL_MODE` matches the cluster.
{% endhint %}

### Protecting the Stores

The key store holds the private key of the client certificate.
Keep the store files and their passwords private:

- Set the passwords through environment variables, not flags.
- Make the store files readable only by the user who runs the server.
- With the container image, mount the stores as read-only. See [Using Certificates](installation.md#using-certificates).

## Checklist

Before you let an assistant use the server, check the following:

- Create a dedicated account with `CACHE_READ` on the needed caches only.
- Set the user name and password through the environment, not in command-line arguments or files that you share.
- Use TLS to connect to the cluster.
- Remove user-defined functions with side effects from the cluster.
- Limit the properties that the nodes publish in `SYS.NODE_ATTRIBUTES`.
- Keep the audit log, and keep the audit folder private.
