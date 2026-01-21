---
description: >-
  Create a new database container. This command initializes a new database
  namespace with optional character set and collation settings.
---

# CREATE DATABASE

## Syntax

```sql
CREATE [OR REPLACE] {DATABASE | SCHEMA} [IF NOT EXISTS] db_name
    [create_specification] ...

create_specification:
    [DEFAULT] CHARACTER SET [=] charset_name
  | [DEFAULT] COLLATE [=] collation_name
  | COMMENT [=] 'comment'
```

## Description

`CREATE DATABASE` creates a database with the given name. To use this statement, you need the [CREATE privilege](../../account-management-sql-statements/grant.md#database-privileges) for the database. `CREATE SCHEMA` is a synonym for `CREATE DATABASE`.

For valid identifiers to use as database names, see [Identifier Names](../../../sql-structure/sql-language-structure/identifier-names.md).

#### OR REPLACE

If the optional `OR REPLACE` clause is used, it acts as a shortcut for:

```sql
DROP DATABASE IF EXISTS db_name;
CREATE DATABASE db_name ...;
```

#### IF NOT EXISTS

When the `IF NOT EXISTS` clause is used, MariaDB will return a warning instead of an error if the specified database already exists.

#### COMMENT

{% tabs %}
{% tab title="Current" %}
The maximum length of a comment is 1024 bytes. If the comment length exceeds this length, an error/warning code 4144 is thrown. The database comment is also added to the `db.opt` file, as well as to the [information\_schema.schemata table](../../../system-tables/information-schema/information-schema-tables/information-schema-schemata-table.md).
{% endtab %}

{% tab title="< 10.5.0" %}
Comments added for databases do not exist.
{% endtab %}
{% endtabs %}

## Examples

```sql
CREATE DATABASE db1;
Query OK, 1 row affected (0.18 sec)

CREATE DATABASE db1;
ERROR 1007 (HY000): Can't create database 'db1'; database exists

CREATE OR REPLACE DATABASE db1;
Query OK, 2 rows affected (0.00 sec)

CREATE DATABASE IF NOT EXISTS db1;
Query OK, 1 row affected, 1 warning (0.01 sec)

SHOW WARNINGS;
+-------+------+----------------------------------------------+
| Level | Code | Message                                      |
+-------+------+----------------------------------------------+
| Note  | 1007 | Can't create database 'db1'; database exists |
+-------+------+----------------------------------------------+
```

Setting the [character sets and collation](../../../data-types/string-data-types/character-sets/). See [Setting Character Sets and Collations](../../../data-types/string-data-types/character-sets/setting-character-sets-and-collations.md) for more details.

```sql
CREATE DATABASE czech_slovak_names 
  CHARACTER SET = 'keybcs2'
  COLLATE = 'keybcs2_bin';
```

```sql
CREATE DATABASE presentations COMMENT 'Presentations for conferences';
```

## See Also

* [Identifier Names](../../../sql-structure/sql-language-structure/identifier-names.md)
* [DROP DATABASE](../drop/drop-database.md)
* [SHOW CREATE DATABASE](../../administrative-sql-statements/show/show-create-database.md)
* [ALTER DATABASE](../alter/alter-database.md)
* [SHOW DATABASES](../../administrative-sql-statements/show/show-databases.md)
* [Character Sets and Collations](../../../data-types/string-data-types/character-sets/supported-character-sets-and-collations.md)
* [Information Schema SCHEMATA Table](../../../system-tables/information-schema/information-schema-tables/information-schema-schemata-table.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
