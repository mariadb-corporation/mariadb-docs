---
description: >-
  The Rust connector for MariaDB provides two community-maintained crates for
  building native Rust applications that connect to MariaDB databases, with
  MariaDB-specific features contributed directly by MariaDB.
icon: link
---

# Rust Connector for MariaDB

## Overview

Rust applications can connect to MariaDB using the community-maintained drivers from the [blackbeam](https://github.com/blackbeam) project. These are not official MariaDB connectors, but MariaDB has contributed MariaDB-specific features to them, and they are the recommended way to connect to MariaDB from Rust.

The Rust ecosystem has two widely used community-maintained MySQL/MariaDB client crates:

- **[`mysql`](https://crates.io/crates/mysql)** (`rust-mysql-simple`) — a synchronous Rust driver
- **[`mysql_async`](https://crates.io/crates/mysql_async)** — an asynchronous Rust driver built on Tokio

Both crates share a common protocol implementation library, **[`rust_mysql_common`](https://crates.io/crates/mysql_common)**, which handles low-level MySQL/MariaDB protocol primitives, value conversion, and authentication primitives used by both drivers.

MariaDB recommends these Rust crates, which provide robust MySQL‑protocol compatibility and include MariaDB‑specific enhancements for first‑class client support.

Select the driver based on your application’s architecture: use `mysql` for blocking/synchronous I/O, or `mysql_async` for non‑blocking I/O with Tokio. Both drivers have received the same MariaDB-specific contributions for the features described below.

## MariaDB-Specific Contributions

MariaDB has contributed MariaDB‑specific features directly to these crates. The following features have been implemented and incorporated into the official releases (mysql_async v0.37.0 and the corresponding rust‑mysql‑simple version):

### 1. PARSEC Authentication Plugin Support

PARSEC (Password Authentication using Response Signed with Elliptic Curve) is a modern authentication plugin introduced in MariaDB 11.6. It uses salted passwords, PBKDF2 key derivation, and ed25519 elliptic-curve signatures to prevent replay attacks and protect credentials.

Both `mysql_async` and `mysql` (sync) now support PARSEC authentication natively. When connecting to a MariaDB 11.6+ server configured to use the `parsec` authentication plugin, the driver will automatically handle the PARSEC handshake without any special configuration from the application developer.

### 2. Bulk Execution (`COM_STMT_BULK_EXECUTE`)

MariaDB supports a protocol extension called `COM_STMT_BULK_EXECUTE`, enabled via the `MARIADB_CLIENT_STMT_BULK_OPERATIONS` capability flag. This allows a client to execute a previously prepared statement with multiple rows of parameters in a single network round-trip, rather than sending one execution packet per row.

This feature is specific to MariaDB. When the driver connects to a MariaDB server that indicates support for the `MARIADB_CLIENT_STMT_BULK_OPERATIONS` capability, bulk execution is automatically negotiated and used for batch inserts or updates.

The benefit is significant performance improvement for write-heavy workloads, reducing network overhead and server round-trips.

### 3. Metadata Skipping (`MARIADB_CLIENT_CACHE_METADATA`)

Since MariaDB 10.6, the server supports a binary protocol optimization where result-set column metadata is not re-sent if it has not changed between executions of a prepared statement. This is negotiated via the `MARIADB_CLIENT_CACHE_METADATA` capability.

Both drivers now support this optimization. When connected to MariaDB 10.6+, the driver caches the column metadata on the first execution of a prepared statement and skips receiving it on subsequent executions — reducing network payload and parsing overhead on every repeated query.

## Crate Reference Summary

| Crate | Type | Description | MariaDB Features |
|---|---|---|---|
| [`mysql`](https://crates.io/crates/mysql) | Sync | `rust-mysql-simple`; blocking I/O | PARSEC auth, bulk execute, metadata skip |
| [`mysql_async`](https://crates.io/crates/mysql_async) | Async | Tokio-based async driver | PARSEC auth, bulk execute, metadata skip |
| [`mysql_common`](https://crates.io/crates/mysql_common) | Shared | Protocol primitives, value types, auth | Used internally by both drivers |

> **Note:** `rust_mysql_common` is a shared dependency and does not need to be added to your `Cargo.toml` directly. It is pulled in automatically by either `mysql` or `mysql_async`.

## Installation

**Sync driver:**
```toml
[dependencies]
mysql = "*"
```

## MariaDB Server Version Requirements

| Feature | Minimum MariaDB Version |
|---|---|
| Metadata skipping | 10.6 |
| PARSEC authentication | 11.6 |
| Bulk execution (`COM_STMT_BULK_EXECUTE`) | - |

All features are automatically negotiated during the connection handshake based on what the server announces; no application‑side configuration is needed."

## See Also

- [`mysql_async` on crates.io](https://crates.io/crates/mysql_async)
- [`mysql` (sync) on crates.io](https://crates.io/crates/mysql)
- [`mysql_async`](https://github.com/blackbeam/mysql_async)
- [`rust-mysql-simple`](https://github.com/blackbeam/rust-mysql-simple)
- [MariaDB PARSEC Authentication Plugin documentation](https://mariadb.com/docs/server/reference/plugins/authentication-plugins/authentication-plugin-parsec)
- [MDEV-19237 — Metadata skip server-side implementation](https://jira.mariadb.org/browse/MDEV-19237)