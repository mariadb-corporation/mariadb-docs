---
description: >-
  Displays help information from the server's help tables. Useful for looking up
  SQL syntax and command descriptions directly from the client.
---

# HELP Command

## Syntax

```sql
HELP search_string
```

## Description

The `HELP` command can be used in any MariaDB client, such as the [mariadb](../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) command-line client, to get basic syntax help and a short description for most commands and functions.

If you provide an argument to the `HELP` command, the [mariadb](../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) client uses it as a search string to access server-side help. The proper operation of this command requires that the help tables in the `mysql` database be initialized with help topic information.

If there is no match for the search string, the search fails. Use `HELP contents` to see a list of the help categories:

```sql
HELP contents
You asked for help about help category: "Contents"
For more information, type 'help <item>', where <item> is one of the following
categories:
   Account Management
   Administration
   Compound Statements
   Data Definition
   Data Manipulation
   Data Types
   Functions
   Functions and Modifiers for Use with GROUP BY
   Geographic Features
   Help Metadata
   Language Structure
   Plugins
   Procedures
   Sequences
   Table Maintenance
   Transactions
   User-Defined Functions
   Utility
```

If a search string matches multiple items, MariaDB shows a list of matching topics:

```sql
HELP drop
Many help items for your request exist.
To make a more specific request, please type 'help <item>',
where <item> is one of the following
topics:
   ALTER TABLE
   DROP DATABASE
   DROP EVENT
   DROP FUNCTION
   DROP FUNCTION UDF
   DROP INDEX
   DROP PACKAGE
   DROP PACKAGE BODY
   DROP PROCEDURE
   DROP ROLE
   DROP SEQUENCE
   DROP SERVER
   DROP TABLE
   DROP TRIGGER
   DROP USER
   DROP VIEW
```

Then you can enter a topic as the search string to see the help entry for that topic.

The help is provided with the MariaDB server and makes use of four help tables found in the `mysql` database: [help\_relation](../../system-tables/the-mysql-database-tables/mysql-help_relation-table.md), [help\_topic](../../system-tables/the-mysql-database-tables/mysql-help_topic-table.md), [help\_category](../../system-tables/the-mysql-database-tables/mysql-help_category-table.md) and [help\_keyword](../../system-tables/the-mysql-database-tables/mysql-help_keyword-table.md). These tables are populated by the [mariadb-install-db](../../../clients-and-utilities/deployment-tools/mariadb-install-db.md) or `fill_help_table.sql` scripts.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
