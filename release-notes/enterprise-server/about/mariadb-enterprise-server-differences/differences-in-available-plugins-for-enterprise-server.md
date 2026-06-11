---
description: Plugin Evolution Across Enterprise Releases
hidden: true
---

# Differences in Available Plugins for Enterprise Server

The availability, maturity, and package inclusions of [plugins](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/plugin-overview) continuously change from version to version to maintain a predictable operational ecosystem:

## MariaDB Enterprise Server 11.8

* [**caching\_sha2\_password**](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-caching_sha2_password#overview) **Plugin**: This authentication plugin was added to provide MySQL-compatible authentication, allowing users to be moved from MySQL to MariaDB without changing their passwords (it is not installed by default).
* [**PARSEC**](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-parsec) **Plugin**: Available in [MariaDB Enterprise Server 11.8](../../../community-server/11.8/what-is-mariadb-118.md).
* [**HashiCorp Vault**](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/automated-mariadb-deployment-and-administration/hashicorp-vault-and-mariadb) **Upgrade**: Namespace support was added to HashiCorp Vault to integrate with HashiCorp enterprise namespaces.
* [**file\_key\_management**](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin) **Encryption Plugin**: This plugin can now read keys from a Unix socket instead of just local files. It also added key rotation capability along with a new Information Schema table named [FILE\_KEY\_MANAGEMENT\_KEYS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-file_key_management_keys).
* [**Enterprise Audit**](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-enterprise-audit) **Buffering**: Audit logging buffer writes are now possible, controlled by the server\_audit\_file\_buffer\_size variable and manually flushed using `server_audit_sync_log_file`.

## MariaDB Enterprise Server 11.4

* **`PARSEC` Authentication**: This plugin (Password Authentication using Response Signed with Elliptic Curve) is included as a backported feature. It uses salted passwords, pbkdf2 key derivation, and signed responses to mitigate replay and man-in-the-middle attacks.
* [**password\_reuse\_check**](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/password-reuse-check-plugin) **Plugin**: Included as a backported feature to prevent users from reusing previous passwords. _(Note: Upgrading this plugin to version 2.0 alters the data storage format to fix a weakness under_ [_MDEV-28838_](https://jira.mariadb.org/browse/MDEV-28838)_, which invalidates older v1.0 history)_.
* [**SQL Error Log**](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/sql-error-log-plugin) **Plugin**: Enhanced to display the active thread ID and the default schema for errors when `sql_error_log_with_db_and_thread_info=ON` is set.

## MariaDB Enterprise Server 10.6

* **Object Filtering for Audit**: Advanced filtering was added to MariaDB Enterprise Audit, allowing administrators to define JSON filters (`ignore_databases`, `ignore_tables`, `log_databases`, `log_tables`) to restrict logging to specific databases or tables. This capability was also backported to [Enterprise Server 10.5.12-8](../../old-releases/10.5/10.5.12-8.md) and [Enterprise Server 10.4.21-13](../../old-releases/10.4/10.4.21-13.md).

## MariaDB Enterprise Server 10.5

* [**ColumnStore Storage Engine Plugin**](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/mariadb-columnstore/architecture/columnstore-storage-engine-overview): MariaDB ColumnStore 5 was introduced as an integrated enterprise plugin to provide distributed columnar storage for analytical workloads.
* [**Spider Storage Engine Plugin**](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-storage-engine-introduction): Updated to support an ODBC foreign data wrapper and added the[ information\_schema.SPIDER\_WRAPPER\_PROTOCOLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/information-schema-spider_wrapper_protocols-table) system table.
* **Plugin Phase-outs & Repository Splits**:
  * [**TokuDB**](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb/tokudb-overview) **and** [**Cassandra**](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/cassandra): Both storage engine plugins were completely phased out and removed from installation packages.
  * [**CONNECT Storage Engine**](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect): Moved from the main Enterprise repository to an "unsupported" repository. To ensure it functions, you must explicitly include the `--include-unsupported` flag in the `mariadb_es_repo_setup` script, or else the library `ha_connect.so` will be unavailable.

## MariaDB Enterprise Server 10.4

* **Aria System Tables**: System tables transitioned to use the crash-safe Aria storage engine plugin by default.
* **Multi-Plugin Authentication**: Added the ability to specify multiple authentication plugins for an individual user account using `OR` fallback constraints (e.g., executing `IDENTIFIED VIA unix_socket OR mysql_native_password`).

## Querying Plugin Information

Because your specific installation state depends on repository definitions (such as whether the `unsupported` repository is active), documentation can diverge from real-time database deployments. You can dynamically query plugin availability via the following database interface methods:

### Using `SHOW PLUGINS`

The simplest statement to review all loaded plugins and identify hard-coded components:

```sql
SHOW PLUGINS;
```

_Mechanic:_ If a plugin's `Library` column returns a `NULL` value, the plugin is natively built-in and cannot be uninstalled.

### Using `information_schema.PLUGINS`

To filter plugins systematically by maturity level, type, or library names:

```sql
SELECT PLUGIN_NAME, 
       PLUGIN_STATUS, 
       PLUGIN_TYPE, 
       PLUGIN_MATURITY,
       PLUGIN_LIBRARY 
FROM information_schema.PLUGINS 
WHERE PLUGIN_STATUS = 'ACTIVE'
ORDER BY PLUGIN_NAME;
```

_Mechanic:_ If the `PLUGIN_LIBRARY` column is `NULL`, the plugin is built-in and cannot be uninstalled.

### Using `mysql.plugin`

To see exactly which plugins have been explicitly installed onto the database system registry:

```sql
SELECT name, dl FROM mysql.plugin;
```

_Critical Nuance:_ This table only retains records for plugins explicitly loaded via the `INSTALL SONAME` statement, the `INSTALL PLUGIN` statement, or the offline `mariadb-plugin` utility. It does not contain information about built-in plugins or plugins loaded temporarily at server startup using the `--plugin-load` or `--plugin-load-add` configuration options.
