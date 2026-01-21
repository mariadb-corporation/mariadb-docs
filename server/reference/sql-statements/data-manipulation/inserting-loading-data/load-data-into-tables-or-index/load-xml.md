---
description: >-
  Read data from an XML file into a table. This command parses XML content,
  mapping elements and attributes to table columns for direct data import.
---

# LOAD XML

## Syntax

```sql
LOAD XML [LOW_PRIORITY | CONCURRENT] [LOCAL] INFILE 'file_name'
    [REPLACE | IGNORE]
    INTO TABLE [db_name.]tbl_name
    [CHARACTER SET charset_name]
    [ROWS IDENTIFIED BY '<tagname>']
    [IGNORE number {LINES | ROWS}]
    [(column_or_user_var,...)]
    [SET col_name = expr,...]
```

## Description

The LOAD XML statement reads data from an XML file into a table. The`file_name` must be given as a literal string. The `tagname` in the optional `ROWS IDENTIFIED BY` clause must also be given as a literal\
string, and must be surrounded by angle brackets (< and >).

LOAD XML acts as the complement of running the [mariadb client](../../../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) in XML output mode (that is, starting the client with the --xml option). To write data from a table to an XML file, use a command such as the\
following one from the system shell:

```bash
shell> mariadb --xml -e 'SELECT * FROM mytable' > file.xml
```

To read the file back into a table, use LOAD XML INFILE. By default, the element is considered to be the equivalent of a database table row; this can be changed using the ROWS IDENTIFIED BY clause.

This statement supports three different XML formats:

* Column names as attributes and column values as attribute values:

```xml
<row column1="value1" column2="value2" .../>
```

* Column names as tags and column values as the content of these tags:

```xml
<row>
  <column1>value1</column1>
  <column2>value2</column2>
</row>
```

* Column names are the name attributes of tags, and values are\
  the contents of these tags:

```xml
<row>
  <field name='column1'>value1</field>
  <field name='column2'>value2</field>
</row>
```

This is the format used by other tools, such as [mariadb-dump](../../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md).

All 3 formats can be used in the same XML file; the import routine automatically detects the format for each row and interprets it correctly. Tags are matched based on the tag or attribute name and the\
column name.

The following clauses work essentially the same way for LOAD XML as they do for LOAD DATA:

* `LOW_PRIORITY` or `CONCURRENT`
* `LOCAL`
* `REPLACE` or `IGNORE`
* `CHARACTER SET`
* (column\_or\_user\_var,...)
* `SET`

See [LOAD DATA](load-data-infile.md) for more information about these clauses.

The `IGNORE` number `LINES` or `IGNORE` number `ROWS` clause causes the first number rows in the XML file to be skipped. It is analogous to the `LOAD DATA` statement's `IGNORE ... LINES` clause.

If the [LOW\_PRIORITY](../../changing-deleting-data/high_priority-and-low_priority.md) keyword is used, insertions are delayed until no other clients are reading from the table. The `CONCURRENT` keyword allows the use of [concurrent inserts](../concurrent-inserts.md). These clauses cannot be specified together.

This statement activates `INSERT` [triggers](../../../../../server-usage/triggers-events/triggers/).

## See Also

* The [CONNECT](../../../../../server-usage/storage-engines/connect/) storage engine has an [XML table type](../../../../../server-usage/storage-engines/connect/connect-table-types/connect-table-types-data-files.md#xml-table-type).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
