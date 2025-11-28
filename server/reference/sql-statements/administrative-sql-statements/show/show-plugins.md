---
description: >-
  List installed server plugins. View the name, status, type, and library file
  for each active plugin.
---

# SHOW PLUGINS

## Syntax

```sql
SHOW PLUGINS;
```

## Description

`SHOW PLUGINS` displays information about installed [plugins](../../../plugins/). The `Library` column indicates the plugin library - if it is `NULL`, the plugin is built-in and cannot be uninstalled.

The [PLUGINS](../../../system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md) table in the `information_schema` database contains more detailed information.

For specific information about storage engines (a particular type of plugin), see the [information\_schema.ENGINES](../../../system-tables/information-schema/information-schema-tables/information-schema-engines-table.md) table and the [SHOW ENGINES](show-engines.md) statement.

## Examples

```sql
SHOW PLUGINS;
+----------------------------+----------+--------------------+-------------+---------+
| Name                       | Status   | Type               | Library     | License |
+----------------------------+----------+--------------------+-------------+---------+
| binlog                     | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| mysql_native_password      | ACTIVE   | AUTHENTICATION     | NULL        | GPL     |
| mysql_old_password         | ACTIVE   | AUTHENTICATION     | NULL        | GPL     |
| MRG_MyISAM                 | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| MyISAM                     | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| CSV                        | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| MEMORY                     | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| FEDERATED                  | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| PERFORMANCE_SCHEMA         | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| Aria                       | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| InnoDB                     | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| INNODB_TRX                 | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
...
| INNODB_SYS_FOREIGN         | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| INNODB_SYS_FOREIGN_COLS    | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| SPHINX                     | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| ARCHIVE                    | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| BLACKHOLE                  | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| FEEDBACK                   | DISABLED | INFORMATION SCHEMA | NULL        | GPL     |
| partition                  | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| pam                        | ACTIVE   | AUTHENTICATION     | auth_pam.so | GPL     |
+----------------------------+----------+--------------------+-------------+---------+
```

## See Also

* [List of Plugins](../../../plugins/information-on-plugins/list-of-plugins.md)
* [Plugin Overview](../../../plugins/plugin-overview.md)
* [INFORMATION\_SCHEMA.PLUGINS Table](../../../system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md)
* [INSTALL PLUGIN](../plugin-sql-statements/install-plugin.md)
* [INFORMATION\_SCHEMA.ALL\_PLUGINS Table](../../../system-tables/information-schema/information-schema-tables/all-plugins-table-information-schema.md) (all plugins, installed or not)
* [INSTALL SONAME](../plugin-sql-statements/install-soname.md)
* [UNINSTALL PLUGIN](../plugin-sql-statements/uninstall-plugin.md)
* [UNINSTALL SONAME](../plugin-sql-statements/uninstall-soname.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
