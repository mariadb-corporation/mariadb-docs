---
hidden: true
---

# MySQL to MariaDB Compatibility Matrix

## Introduction & Executive Summary

MariaDB Server was originally designed as a drop-in replacement for MySQL, maintaining high compatibility across library binary protocols, file structures, and APIs. For most applications, moving from MySQL to MariaDB is a straightforward process that requires minimal changes to your code or configuration.

However, as both projects have evolved—particularly with the release of MySQL 8.0, the latest MySQL 8.4 LTS, and MariaDB 10.11/11.4 LTS—they have introduced unique features and default behaviors. While MariaDB often maintains support for "legacy" MySQL behaviors for compatibility, MySQL 8.4 has moved to aggressively remove them. This guide highlights the essential differences you must understand to ensure a seamless transition.

### The TL;DR of MySQL to MariaDB Migration

If you are migrating from MySQL 8.0 or 8.4 LTS to a modern version of MariaDB, these are the four "deal-breaker" areas where you are most likely to encounter friction:

#### **Authentication & Security**

MySQL 8.4 has accelerated the push toward `caching_sha2_password`. Notably, the older `mysql_native_password` plugin is now disabled by default in MySQL 8.4 and requires explicit configuration to enable. MariaDB continues to support and often default to `mysql_native_password` or `unix_socket`.

* Action: Check your client connector versions. When moving from 8.4 to MariaDB, you may need to re-enable or transition user accounts back to `mysql_native_password` or `ed25519`.

#### **Feature & Variable Removals**

A key difference in MySQL 8.4 is the removal of many system variables and syntax options that were deprecated in 8.0. MariaDB often retains these for backward compatibility.

* Action: If you have optimized your configuration specifically for 8.4 by removing "removed" variables, MariaDB will likely accept them, but it may also still support the older variants you previously used in MySQL 5.7 or 8.0.

#### **Global Transaction IDs**

MariaDB and MySQL use entirely different formats for GTIDs. In MySQL 8.4, replication syntax has been further modernized (e.g., removal of `MASTER` in favor of `SOURCE` keywords). MariaDB supports both sets of keywords but maintains its own unique GTID structure (`DomainID:ServerID:Sequence`).

* Action: You cannot "mix and match" GTID replication directly. Plan to use position-based replication if running a hybrid environment during your migration.

#### **Data Types & JSON Evolution**

Both systems have diverged in how they handle complex data. MySQL 8.0 and 8.4 use a native binary format for JSON, optimized for their internal engine. MariaDB treats JSON as an alias for `LONGTEXT` with `CHECK` constraints.

* Action: While SQL-level JSON functions are highly compatible, performance and storage characteristics differ. Test any application logic that relies on high-speed JSON attribute extraction.

## How to use this Matrix

The table below provides a granular breakdown of these differences. We recommend focusing on the "High Impact" items first, as these are the most likely to affect your application's ability to connect or execute queries immediately after the migration.

> Target Version Tip: If you are migrating from MySQL 8.4 LTS, the most logical targets are MariaDB 10.11 LTS or MariaDB 11.4 LTS to ensure you are moving from one stable long-term environment to another.

{% hint style="info" %}
#### Key changes from the 8.4 Nutshell you should keep in mind

* Authentication: The fact that `mysql_native_password` is now "off" by default in 8.4 is a huge point of divergence. Most MariaDB installs still rely on it.
* Syntax: 8.4 officially removed `SET OPTION`, the `LOW_PRIORITY` prefix for some statements, and various SSL variables. If a user's app was updated to work with 8.4, it's "cleaner" but might be using syntax that MariaDB handles differently.
* Default Changes: Some InnoDB defaults changed in 8.4 that might not match MariaDB’s defaults.
{% endhint %}

### Authentication & Security

| Component                     | MySQL 8.0 / 8.4 Behavior                                                                       | MariaDB Behavior                                              | Migration Impact                                                                                     |
| ----------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Default Authentication Plugin | `caching_sha2_password` (MySQL 8.4 requires explicit config to even _enable_ native password). | `mysql_native_password` or `unix_socket`.                     | High. New MySQL users cannot connect to MariaDB without altering the account or updating the client. |
| Connection Security           | `REQUIRE SSL` is common.                                                                       | Supports SSL/TLS but syntax for specific ciphers can vary.    | Medium. Review `GRANT` statements for SSL requirements.                                              |
| Password Complexity           | `validate_password` component.                                                                 | `simple_password_check` or `cracklib_password_check` plugins. | Low. Logic is similar, but plugin names and variables differ.                                        |
| User Locking                  | Supports `ACCOUNT LOCK` / `UNLOCK`.                                                            | Supports `ACCOUNT LOCK` / `UNLOCK` (10.4.2+).                 | None. Highly compatible syntax.                                                                      |

### SQL Syntax & Data Types

| Component               | MySQL 8.0 / 8.4 Behavior                                            | MariaDB Behavior                                                            | Migration Impact                                                                                   |
| ----------------------- | ------------------------------------------------------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| JSON Support            | Native binary format (`JSON` type).                                 | Alias for `LONGTEXT` with `CHECK` constraints.                              | Medium. SQL syntax is compatible, but binary-level storage and some indexing optimizations differ. |
| Reserved Words          | Frequent additions (e.g., `WINDOW`, `EXCEPT`, `INTERSECT` in 8.0+). | Also uses these reserved words, but some unique MariaDB keywords may exist. | Low. Most modern reserved words are now synchronized between both.                                 |
| Invisible Columns       | Supported since 8.0.23.                                             | Supported since 10.3.3.                                                     | None. Highly compatible syntax.                                                                    |
| Common Table Expr (CTE) | Non-recursive and Recursive support.                                | Non-recursive and Recursive support.                                        | None. Functionally identical for standard use cases.                                               |
| Window Functions        | Standard support since 8.0.                                         | Standard support since 10.2.                                                | Low. Standard syntax is compatible; specific MySQL-only extensions are rare.                       |

### System Variables & Defaults

This section helps the DBA avoid "Unknown variable" errors when they first try to start the MariaDB service using a MySQL configuration file.

| Feature / Variable | MySQL 8.0 / 8.4 Defaults                                      | MariaDB Defaults                                                                | Migration Impact                                                                        |
| ------------------ | ------------------------------------------------------------- | ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Configuration File | Reads `my.cnf` / `my.ini`.                                    | Reads `my.cnf` / `my.ini` and `mariadb.cnf`.                                    | None. MariaDB maintains compatibility with existing MySQL config files.                 |
| Removed Variables  | Many 5.7 variables removed in 8.4 (e.g., `expire_logs_days`). | Often retains these legacy variables as aliases.                                | Low. MariaDB is generally more forgiving of "old" variables than MySQL 8.4.             |
| Default Charset    | `utf8mb4_0900_ai_ci` (MySQL 8.0+).                            | `utf8mb4_uca1400_ai_ci` (MariaDB 11.4+).                                        | Medium. Sorting/Collation behavior may differ slightly for modern Unicode characters.   |
| Explicit Defaults  | `explicit_defaults_for_timestamp` is `ON`.                    | `explicit_defaults_for_timestamp` defaults to `OFF` (for legacy compatibility). | Medium. Can cause different behavior for `TIMESTAMP` columns without explicit defaults. |

### **SQL Syntax & Data Types**

| Component         | MySQL 8.0 / 8.4 Behavior                                    | MariaDB Behavior                                             | Migration Impact                                                                          |
| ----------------- | ----------------------------------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| JSON Support      | Native binary format (`JSON` type).                         | Alias for `LONGTEXT` with `CHECK` constraints.               | Medium. Syntax is compatible, but binary-level storage and indexing optimizations differ. |
| Reserved Words    | Frequent additions (e.g., `WINDOW`, `EXCEPT`, `INTERSECT`). | Also uses these, but some unique MariaDB keywords may exist. | Low. Standard SQL reserved words are largely synchronized.                                |
| Invisible Columns | Supported (8.0.23+).                                        | Supported (10.3.3+).                                         | None. Highly compatible syntax.                                                           |
| Window Functions  | Standard support.                                           | Standard support.                                            | None. Functionally identical for standard SQL use cases.                                  |

### **System Variables & Defaults**

| Feature / Variable | MySQL 8.0 / 8.4 Defaults                            | MariaDB Defaults                             | Migration Impact                                                                 |
| ------------------ | --------------------------------------------------- | -------------------------------------------- | -------------------------------------------------------------------------------- |
| Config File        | Reads `my.cnf` / `my.ini`.                          | Reads `my.cnf`, `my.ini`, and `mariadb.cnf`. | None. MariaDB maintains compatibility with existing MySQL configuration files.   |
| Default Charset    | `utf8mb4_0900_ai_ci`.                               | `utf8mb4_uca1400_ai_ci` (11.4+).             | Medium. Sorting/Collation behavior may differ for modern Unicode characters.     |
| Timestamp Defaults | `explicit_defaults_for_timestamp` is `ON`.          | Defaults to `OFF` for legacy compatibility.  | Medium. May cause different auto-population behavior for `TIMESTAMP` columns.    |
| Removed Vars       | Many vars removed in 8.4 (e.g. `expire_logs_days`). | Often retains legacy variables as aliases.   | Low. MariaDB is generally more forgiving of legacy configuration than MySQL 8.4. |

### Replication & GTIDs

| Feature        | MySQL 8.0 / 8.4 Behavior             | MariaDB Behavior                                       | Migration Impact                                                               |
| -------------- | ------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------------------------------ |
| GTID Format    | `UUID:Sequence`                      | `Domain:ServerID:Sequence`                             | Critical. Formats are incompatible. GTID replication cannot be mixed directly. |
| Repl. Syntax   | Uses `SOURCE` / `REPLICA` (8.0.22+). | Supports both `MASTER`/`SLAVE` and `SOURCE`/`REPLICA`. | None. MariaDB is bi-lingual regarding replication syntax.                      |
| Binary Logging | Defaulted to `ON`.                   | Defaulted to `ON` in recent versions.                  | Low. Standard binary log events are generally compatible.                      |

