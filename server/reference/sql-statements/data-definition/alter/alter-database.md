---
description: >-
  Modify database characteristics. Learn how to change global properties like
  the default character set and collation for a specific database.
---

# ALTER DATABASE

## Syntax

```sql
ALTER {DATABASE | SCHEMA} [db_name]
    alter_specification ...
ALTER {DATABASE | SCHEMA} db_name
    UPGRADE DATA DIRECTORY NAME

alter_specification:
    [DEFAULT] CHARACTER SET [=] charset_name
  | [DEFAULT] COLLATE [=] collation_name
  | COMMENT [=] 'comment'
```

## Description

`ALTER DATABASE` enables you to change the overall characteristics of a database. These characteristics are stored in the `db.opt` file in the database directory. To use `ALTER DATABASE`, you need the `ALTER` privilege on the database. `ALTER SCHEMA` is a synonym for `ALTER DATABASE`.

The `CHARACTER SET` clause changes the default database character set. The `COLLATE` clause changes the default database collation. See [Character Sets and Collations](../../../data-types/string-data-types/character-sets/) for more.

You can see what character sets and collations are available using, respectively, the [SHOW CHARACTER SET](../../administrative-sql-statements/show/show-character-set.md) and [SHOW COLLATION](../../administrative-sql-statements/show/show-collation.md) statements.

Changing the default character set/collation of a database does not change the character set/collation of any [stored procedures](../../../../server-usage/stored-routines/stored-procedures/) or [stored functions](../../../../server-usage/stored-routines/stored-functions/) that were previously created, and relied on the defaults. These need to be dropped and recreated in order to apply the character set/collation changes.

The database name can be omitted from the first syntax, in which case the statement applies to the default database.

The syntax that includes the `UPGRADE DATA DIRECTORY NAME` clause. It updates the name of the directory associated with the database to use the encoding implemented in MySQL for mapping database names to database directory names (see [Identifier to File Name Mapping](../../../sql-structure/sql-language-structure/identifier-to-file-name-mapping.md)). This clause is for use under these conditions:

* It is intended when upgrading MySQL from older versions.
* It is intended to update a database directory name to the current encoding format if the name contains special characters that need encoding.
* The statement is used by [mariadb-check](../../../../clients-and-utilities/table-tools/mariadb-check.md) (as invoked by [mariadb-upgrade](../../../../clients-and-utilities/deployment-tools/mariadb-upgrade.md)).

For example, if a database in MySQL 5.0 has a name of `a-b-c`, the name contains instance of the \`-' character. In 5.0, the database directory is also named `a-b-c`, which is not necessarily safe for all file systems. In MySQL, the same database name is encoded as `a@002db@002dc` to produce a file-system-neutral directory name.

When a MySQL installation is upgraded from an older version, the server displays a name such as `a-b-c` (which is in the old format) as `#mysql50#a-b-c`, and you must refer to the name using the `#mysql50#` prefix. Use `UPGRADE DATA DIRECTORY NAME` in this case to explicitly tell the server to re-encode the database directory name to the current encoding format:

```sql
ALTER DATABASE `#mysql50#a-b-c` UPGRADE DATA DIRECTORY NAME;
```

After executing this statement, you can refer to the database as a-b-c without the special `#mysql50` prefix.

{% hint style="info" %}
**MariaDB starting with** [**10.5.0**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

From [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0), it is possible to add a comment of a maximum of 1024 bytes. If the comment length exceeds this length, a error/warning code 4144 is thrown. The database comment is also added to the db.opt file, as well as to the [information\_schema.schemata table](../../../system-tables/information-schema/information-schema-tables/information-schema-schemata-table.md).
{% endhint %}

## Examples

{% tabs %}
{% tab title="Current" %}
```sql
ALTER DATABASE p COMMENT='Presentations';
```
{% endtab %}

{% tab title="< 10.5" %}
```sql
ALTER DATABASE test CHARACTER SET='utf8'  COLLATE='utf8_bin';
```
{% endtab %}
{% endtabs %}

## See Also

* [CREATE DATABASE](../create/create-database.md)
* [DROP DATABASE](../drop/drop-database.md)
* [SHOW CREATE DATABASE](../../administrative-sql-statements/show/show-create-database.md)
* [SHOW DATABASES](../../administrative-sql-statements/show/show-databases.md)
* [Character Sets and Collations](../../../data-types/string-data-types/character-sets/supported-character-sets-and-collations.md)
* [Information Schema SCHEMATA Table](../../../system-tables/information-schema/information-schema-tables/information-schema-schemata-table.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
