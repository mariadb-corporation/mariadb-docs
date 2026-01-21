---
description: >-
  List available character sets. View the default collation, maximum length, and
  description for each supported character set.
---

# SHOW CHARACTER SET

## Syntax

```sql
SHOW CHARACTER SET
    [LIKE 'pattern' | WHERE expr]
```

## Description

The `SHOW CHARACTER SET` statement shows all available [character sets](../../../data-types/string-data-types/character-sets/). The `LIKE` clause, if present on its own, indicates which character set names to match. The `WHERE` and `LIKE` clauses can be given to select rows using more general conditions, as discussed in [Extended SHOW](extended-show.md).

The same information can be queried from the [Information Schema CHARACTER\_SETS](../../../system-tables/information-schema/information-schema-tables/information-schema-character_sets-table.md) table.

See [Setting Character Sets and Collations](../../../data-types/string-data-types/character-sets/setting-character-sets-and-collations.md) for details on specifying the character set at the server, database, table and column levels.

## Examples

```sql
SHOW CHARACTER SET LIKE 'latin%';
+---------+-----------------------------+-------------------+--------+
| Charset | Description                 | Default collation | Maxlen |
+---------+-----------------------------+-------------------+--------+
| latin1  | cp1252 West European        | latin1_swedish_ci |      1 |
| latin2  | ISO 8859-2 Central European | latin2_general_ci |      1 |
| latin5  | ISO 8859-9 Turkish          | latin5_turkish_ci |      1 |
| latin7  | ISO 8859-13 Baltic          | latin7_general_ci |      1 |
+---------+-----------------------------+-------------------+--------+
```

```sql
SHOW CHARACTER SET WHERE Maxlen LIKE '2';
+---------+---------------------------+-------------------+--------+
| Charset | Description               | Default collation | Maxlen |
+---------+---------------------------+-------------------+--------+
| big5    | Big5 Traditional Chinese  | big5_chinese_ci   |      2 |
| sjis    | Shift-JIS Japanese        | sjis_japanese_ci  |      2 |
| euckr   | EUC-KR Korean             | euckr_korean_ci   |      2 |
| gb2312  | GB2312 Simplified Chinese | gb2312_chinese_ci |      2 |
| gbk     | GBK Simplified Chinese    | gbk_chinese_ci    |      2 |
| ucs2    | UCS-2 Unicode             | ucs2_general_ci   |      2 |
| cp932   | SJIS for Windows Japanese | cp932_japanese_ci |      2 |
+---------+---------------------------+-------------------+--------+
```

## See Also

* [Supported Character Sets and Collations](../../../data-types/string-data-types/character-sets/supported-character-sets-and-collations.md)
* [Setting Character Sets and Collations](../../../data-types/string-data-types/character-sets/setting-character-sets-and-collations.md)
* [Information Schema CHARACTER\_SETS](../../../system-tables/information-schema/information-schema-tables/information-schema-character_sets-table.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
