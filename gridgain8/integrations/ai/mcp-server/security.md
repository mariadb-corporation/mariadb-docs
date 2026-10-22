---
description: >-
  How GridGain MCP Server protects your data: a dedicated read-only cluster account, the statement check, TLS, and what the account permissions do not cover.
---

# Security

GridGain MCP Server lets an AI assistant run queries on your cluster.
This page explains what protects your data and what you must do yourself.

## Protection Layers

| Layer | What it does |
| ----- | ------------ |
| Dedicated account | The cluster decides what the server can read. This is the main protection. See [Preparing a Cluster Account](#preparing-a-cluster-account). |
| Statement check | The server refuses everything except one `SELECT` query before it sends anything to the cluster. This protects against mistakes of the assistant, but it is not a security boundary. |
| Credentials stay outside the assistant | You set the user name and password in the environment of the server. No tool takes them as an argument or returns them, so the assistant never sees them. |
| Encrypted connection | The server can connect to the cluster over TLS, with a client certificate if the cluster requires it. See [TLS and Mutual TLS](#tls-and-mutual-tls). |
| Rate limit and audit log | The server limits how often the assistant can call a tool, and it records every call. See [Operating MCP Server](operations.md). |

## Preparing a Cluster Account

Do not run the server with an administrator account or with your own account.
Create a dedicated account for it and give the account only the permission to read the caches that the assistant may query.

The account needs `CACHE_READ` for those caches and no other permissions.
With this account, the cluster refuses `INSERT`, `UPDATE`, `DELETE`, `MERGE`, `CREATE TABLE`, and `DROP TABLE`, even if a statement passes the check of the server.

{% hint style="info" %}
Permissions are available only with GridGain Enterprise or Ultimate Edition and with authentication enabled on the cluster.
See [Authentication](../../../security/authentication.md) and [Authorization and Permissions](../../../security/authorization-permissions.md).
On a cluster without authorization, the account cannot limit the server, and only the statement check protects your data.
{% endhint %}

## Limits of Account Permissions

Three things are not stopped by the permissions of the account:

- The cluster does not check permissions for `CREATE INDEX` and `ALTER TABLE ... ADD COLUMN` on a table that the account can read. Only the statement check of the server stops these statements.
- A user-defined function runs with all its effects. A query that does not use a cache is not checked against cache permissions, so `SELECT my_function()` runs for any account. Do not install user-defined functions with side effects on a cluster that the server connects to. The execution plan of a query does not call the function.
- Any account can read the `SYS` views, including `SYS.NODE_ATTRIBUTES`. This view holds the environment variables and system properties of every node, unless you limit them with `IgniteConfiguration.setIncludeProperties`. The statement check of the server allows only eight system views, and `NODE_ATTRIBUTES` is not one of them. To protect the properties from all other clients, limit them on the nodes.

Because all tools are marked as read-only, a host can run them without asking you.
Before you allow this, make sure that the cluster has no user-defined functions with side effects.

## TLS and Mutual TLS

To encrypt the connection, set the following variables.
The cluster must accept TLS connections from thin clients.
See [SSL/TLS](../../../security/ssl-tls.md).

```shell
GRIDGAIN_SSL_MODE=REQUIRED
GRIDGAIN_SSL_TRUSTSTORE_PATH=/path/to/truststore.jks
GRIDGAIN_SSL_TRUSTSTORE_PASSWORD=...
```

If the cluster requires a client certificate (mutual TLS), add the key store:

```shell
GRIDGAIN_SSL_KEYSTORE_PATH=/path/to/keystore.jks
GRIDGAIN_SSL_KEYSTORE_PASSWORD=...
```

The server checks the stores when it starts and refuses to start if a store is missing, of a wrong type, or protected by a different password.
For all TLS settings and checks, see [TLS](configuration.md#tls).

Keep the store files and their passwords private:

- Set the passwords through environment variables, not flags.
- Give the store files to the user who runs the server only.
- With the container image, mount the stores as read-only. See [Using Certificates](installation.md#using-certificates).

{% hint style="info" %}
If you point a TLS client to a node that has no TLS, the connection can wait until the connection timeout and then be repeated.
This looks like an unreachable cluster. Check that `GRIDGAIN_SSL_MODE` matches the cluster.
{% endhint %}

## Checklist

- Create a dedicated account with `CACHE_READ` on the needed caches only.
- Set the user name and password through the environment, not in command-line arguments or files that you share.
- Use TLS to connect to the cluster.
- Remove user-defined functions with side effects from the cluster.
- Limit the properties that the nodes publish in `SYS.NODE_ATTRIBUTES`.
- Keep the audit log, and keep the audit folder private.
