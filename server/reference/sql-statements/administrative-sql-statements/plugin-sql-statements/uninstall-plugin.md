---
description: >-
  Remove a specific plugin from the server. This statement unloads the plugin
  code and deletes its entry from the mysql.plugin table to prevent reloading.
---

# UNINSTALL PLUGIN

## Syntax

```sql
UNINSTALL PLUGIN [IF EXISTS] plugin_name
```

## Description

This statement removes a single installed [plugin](../../../plugins/). To uninstall the whole library which contains the plugin, use [UNINSTALL SONAME](uninstall-soname.md). You cannot uninstall a plugin if any table that uses it is open.

`plugin_name` must be the name of some plugin that is listedin the [mysql.plugin](../../../system-tables/the-mysql-database-tables/mysql-plugin-table.md) table. The server executes the plugin's deinitializationfunction and removes the row for the plugin from the `mysql.plugin`table, so that subsequent server restarts will not load and initializethe plugin. `UNINSTALL PLUGIN` does not remove the plugin'sshared library file.

To use `UNINSTALL PLUGIN`, you must have the [DELETE](../../account-management-sql-statements/grant.md) privilege for the [mysql.plugin](../../../system-tables/the-mysql-database-tables/mysql-plugin-table.md) table.

#### IF EXISTS

If the `IF EXISTS` clause is used, MariaDB will return a note instead of an error if the plugin does not exist. See [SHOW WARNINGS](../show/show-warnings.md).

## Examples

```sql
UNINSTALL PLUGIN example;
```

```sql
UNINSTALL PLUGIN IF EXISTS example;
Query OK, 0 rows affected (0.099 sec)

UNINSTALL PLUGIN IF EXISTS example;
Query OK, 0 rows affected, 1 warning (0.000 sec)

SHOW WARNINGS;
+-------+------+-------------------------------+
| Level | Code | Message                       |
+-------+------+-------------------------------+
| Note  | 1305 | PLUGIN example does not exist |
+-------+------+-------------------------------+
```

## See Also

* [Plugin Overview](../../../plugins/plugin-overview.md)
* [mysql\_plugin](../../../../clients-and-utilities/legacy-clients-and-utilities/mysql_plugin.md)
* [INSTALL PLUGIN](install-plugin.md)
* [List of Plugins](../../../plugins/information-on-plugins/list-of-plugins.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
