---
description: >-
  List plugins and their library files. View information about installed plugins
  and their associated shared object names.
---

# SHOW PLUGINS SONAME

## Syntax

```sql
SHOW PLUGINS SONAME { library | LIKE 'pattern' | WHERE expr };
```

## Description

`SHOW PLUGINS SONAME` displays information about compiled-in and all server plugins in the [plugin\_dir](../../../plugins/plugin-overview.md) directory, including plugins that haven't been installed.

## Examples

```sql
SHOW PLUGINS SONAME 'ha_example.so';
+----------+---------------+----------------+---------------+---------+
| Name     | Status        | Type           | Library       | License |
+----------+---------------+----------------+---------------+---------+
| EXAMPLE  | NOT INSTALLED | STORAGE ENGINE | ha_example.so | GPL     |
| UNUSABLE | NOT INSTALLED | DAEMON         | ha_example.so | GPL     |
+----------+---------------+----------------+---------------+---------+
```

There is also a corresponding [information\_schema](../../../system-tables/information-schema/) table, called [ALL\_PLUGINS](../../../system-tables/information-schema/information-schema-tables/all-plugins-table-information-schema.md), which contains more complete information.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
