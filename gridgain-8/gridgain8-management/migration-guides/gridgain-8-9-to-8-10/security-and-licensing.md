---
description: >-
  Security, permission, and license changes when upgrading from GridGain 8.9 to 8.10: server-side SQL COPY, REST scan queries, thin client checks, and per-feature license checks.
---

# Security, Permission, and Licensing Changes

Several features that were open in 8.9 are closed by default in 8.10, and the license is checked for every feature that your configuration uses.

## Server-Side SQL COPY

Server-side SQL `COPY` against a file or an object store is closed by default. In 8.9.x the statement read any file that the node process could read, and 8.10 rejects it with `Server-side file/object-store COPY is disabled on this node` until you configure it. To use it after the upgrade:

1. Set `fileAccessEnabled` to `true` on the `ImportExportConfiguration` block of the GridGain plugin configuration (default `false`).
2. Fill the allow-lists on that block: `importRoots` for local directories, `allowedS3Buckets` and `allowedS3Endpoints` for S3, and `allowedCatalogUris` for Iceberg catalogs. An empty list forbids the access.
3. Grant the new `COPY_FROM_FILE` and `COPY_TO_FILE` [permissions](../../../security/authentication-and-authorization/authorization-permissions.md) to the roles that run server-side `COPY`. They are system permissions, for example `{system:['COPY_FROM_FILE']}` in the permission string. In 8.9.x the statement needed no permission beyond the cache permissions. In 8.10 a role without `COPY_FROM_FILE` fails with `Authorization failed [perm=COPY_FROM_FILE, name=null, ...]`.

`ImportExportConfiguration` is node-local, so configure it identically on every node. Do not point `importRoots` at the node work directory. `COPY_TO_FILE` overwrites files in a root, so use dedicated directories. Client-side `COPY` is not affected.

`COPY ... FORMAT JDBC` also validates the JDBC URL. Only the `jdbc:mariadb:`, `jdbc:mysql:`, and `jdbc:postgresql:` schemes are accepted by default (`GRIDGAIN_BULKLOAD_JDBC_ALLOWED_URL_SCHEMES`), and `${VAR}` placeholders are no longer expanded unless the variables are listed in `GRIDGAIN_BULKLOAD_JDBC_ENV_ALLOWLIST`.

## REST Scan Queries With a Filter Class

This section applies if you send the `EXECUTE_SCAN_QUERY` REST command with a `className`, or if a client parses REST error responses.

The `EXECUTE_SCAN_QUERY` REST command instantiates a filter class only if the class is listed in the `IGNITE_REST_SCAN_QUERY_FILTER_CLASSES` system property. In 8.9.x the node instantiated any class that the request named. The list is empty by default, so a scan query that passes `className` is rejected until you allow the class. Set the property to a comma-separated list of fully qualified class names (exact match) on every node that has the REST connector enabled.

REST error responses no longer include the server stack trace. In 8.9.x the `error` field ended with `trace=` followed by the Java stack trace. In 8.10 it contains only the message, for example `Failed to handle request: [req=CACHE_GET, err=Failed to find cache for given cache name: nonexistent]`. Clients that parsed the trace must use the message instead.

## Thin Client Permission and Filter Checks

This section applies if thin clients call Java services or register continuous query remote filters.

Thin client requests are checked more strictly:

- *Service calls.* `SERVICE_INVOKE` is checked for thin client calls to Java services, including services that run on a node other than the one the client is connected to. A role without it fails with `Authorization failed [perm=SERVICE_INVOKE, name=<service_name>]`. Grant `SERVICE_INVOKE` to the roles whose thin clients call services. This check was added in GridGain 8.9.39, so a cluster on 8.9.39 already behaves this way.
- *Continuous query remote filters.* Filters that a thin client sends as a class name go through the marshaller class filter (`IGNITE_MARSHALLER_WHITELIST` and `IGNITE_MARSHALLER_BLACKLIST`). A filter class that the lists do not allow starts failing. This check was added in GridGain 8.9.40, so a cluster on 8.9.40 already behaves this way.

## Per-Feature License Checks

Compare your license with your configuration before you upgrade.

{% hint style="warning" %}
Upgrade to GridGain 8.10.1 or later. GridGain 8.10.0 checked more features against XML license files than GridGain 8.9 did, so a node with a license issued before GridGain 8.10 could fail to start, for example with `Security feature is not allowed by the licence.` GridGain 8.10.1 fixes this. This section describes GridGain 8.10.1 and later.
{% endhint %}

GridGain 8.10 checks the license for every feature that the node configuration uses. GridGain 8.9 checked only snapshots, compression, vector search, and z/OS. When the check fails depends on the feature:

- *At node start.* Authentication or authorization, data center replication, rolling upgrades, and snapshots (including point-in-time recovery) fail the node start, with a message such as `Data center replication feature is not allowed by the licence.`
- *When a cache starts.* Rack awareness, cache encryption, and vector indexes are checked for each cache configuration. The cache fails to start, and a cache from the node configuration also stops the node from starting, with `Rack awareness is not allowed by the licence [cacheName=...]`, `Encryption is not allowed by the licence [cacheName=...]`, or `Vector search is not allowed by the licence [cacheName=...]`.

What a license allows depends on its format: an XML license file, or a MariaDB license key. An XML license file lists its features as `<enabled-feature name="..."/>` entries. Feature names are matched exactly, and most of them use underscores, not hyphens. The license type, such as `ENT`, is not checked.

| Your configuration uses | XML license file | MariaDB license key | 8.9.x |
| --- | --- | --- | --- |
| Authentication or authorization (`authenticator` or `authenticationEnabled`) | Any license | Any license | Not checked |
| Rolling upgrades (`rollingUpdatesEnabled=true`) | Any license | Any license | Not checked |
| Cache encryption | Any license | Any license | Not checked |
| Data center replication (a data center ID) | Any license | `data_center_replication` or `ultimate` | Not checked |
| Rack awareness (any affinity backup filter) | Any license | `rack_awareness` or `ultimate` | Not checked |
| Vector search index | `vector-search` | Any license | `vector-search` |
| Local snapshots (a `snapshotConfiguration`) | `local_snapshots` or `ultimate` | `local_snapshots` or `ultimate` | `ultimate` |
| Remote (SFTP) snapshots | `remote_snapshots` or `ultimate` | `remote_snapshots` or `ultimate` | `ultimate` |
| Point-in-time recovery | `point_in_time_recovery` or `ultimate` | `point_in_time_recovery` or `ultimate` | `ultimate` |
| Entry compression | `compression` or `ultimate` | `compression` or `ultimate` | `compression` or `ultimate` |

With an XML license file, the `ultimate` feature does not enable vector search. The license must list `vector-search`, as in GridGain 8.9.

An XML license file that works with your configuration on GridGain 8.9 also works with it on GridGain 8.10.1. If you switch to a MariaDB license key, compare its features with your configuration, and contact MariaDB [support](https://mariadb.com/support/) if a feature is missing.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
