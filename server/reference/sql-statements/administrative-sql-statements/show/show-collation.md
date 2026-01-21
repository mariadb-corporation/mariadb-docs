---
description: >-
  List available collations. View the character set associated with each
  collation and identifying properties like ID and default status.
---

# SHOW COLLATION

## Syntax

```sql
SHOW COLLATION
    [LIKE 'pattern' | WHERE expr]
```

## Description

The output from `SHOW COLLATION` includes all available [collations](../../../data-types/string-data-types/character-sets/). The `LIKE` clause, if present on its own, indicates which collation names to match. The `WHERE` and `LIKE` clauses can be given to select rows using more general conditions, as discussed in [Extended SHOW](extended-show.md).

{% tabs %}
{% tab title="Current" %}
Similar information, including some extra information, can be queried from the [Information Schema COLLATIONS](../../../system-tables/information-schema/information-schema-tables/information-schema-collations-table.md) table.
{% endtab %}

{% tab title="< 11.4.5" %}
No similar information or extra information can be queried from the [Information Schema COLLATIONS](../../../system-tables/information-schema/information-schema-tables/information-schema-collations-table.md) table.
{% endtab %}
{% endtabs %}

See [Setting Character Sets and Collations](../../../data-types/string-data-types/character-sets/setting-character-sets-and-collations.md) for details on specifying the collation at the server, database, table and column levels.

{% tabs %}
{% tab title="Current" %}
The `pad_attribute` column (not shown in the examples below) has a value of `NO PAD` or `PAD SPACE`. This attribute affects whether trailing spaces are significant in string comparisons. See the [INFORMATION\_SCHEMA.COLLATIONS](../../../system-tables/information-schema/information-schema-tables/information-schema-collations-table.md) table description for more information.

```sql
SHOW COLLATION LIKE 'utf8mb4_bin'; 
+-------------+---------+------+---------+----------+---------+---------------+ 
| Collation   | Charset | Id   | Default | Compiled | Sortlen | Pad_attribute | 
+-------------+---------+------+---------+----------+---------+---------------+ 
| utf8mb4_bin | utf8mb4 | 46   |         | Yes      | 1       | PAD SPACE     | 
+-------------+---------+------+---------+----------+---------+---------------+
```
{% endtab %}

{% tab title="< 12.1" %}
The `pad_attribute` column is not available.
{% endtab %}
{% endtabs %}

## Examples

```sql
SHOW COLLATION LIKE 'latin1%';
+-------------------------+---------+------+---------+----------+---------+
| Collation               | Charset | Id   | Default | Compiled | Sortlen |
+-------------------------+---------+------+---------+----------+---------+
| latin1_german1_ci       | latin1  |    5 |         | Yes      |       1 |
| latin1_swedish_ci       | latin1  |    8 | Yes     | Yes      |       1 |
| latin1_danish_ci        | latin1  |   15 |         | Yes      |       1 |
| latin1_german2_ci       | latin1  |   31 |         | Yes      |       2 |
| latin1_bin              | latin1  |   47 |         | Yes      |       1 |
| latin1_general_ci       | latin1  |   48 |         | Yes      |       1 |
| latin1_general_cs       | latin1  |   49 |         | Yes      |       1 |
| latin1_spanish_ci       | latin1  |   94 |         | Yes      |       1 |
| latin1_swedish_nopad_ci | latin1  | 1032 |         | Yes      |       1 |
| latin1_nopad_bin        | latin1  | 1071 |         | Yes      |       1 |
+-------------------------+---------+------+---------+----------+---------+
```

```sql
SHOW COLLATION WHERE Sortlen LIKE '8' AND Charset LIKE 'utf8mb4';
+------------------------------+---------+------+---------+----------+---------+
| Collation                    | Charset | Id   | Default | Compiled | Sortlen |
+------------------------------+---------+------+---------+----------+---------+
| utf8mb4_unicode_ci           | utf8mb4 |  224 |         | Yes      |       8 |
| utf8mb4_icelandic_ci         | utf8mb4 |  225 |         | Yes      |       8 |
| utf8mb4_latvian_ci           | utf8mb4 |  226 |         | Yes      |       8 |
| utf8mb4_romanian_ci          | utf8mb4 |  227 |         | Yes      |       8 |
| utf8mb4_slovenian_ci         | utf8mb4 |  228 |         | Yes      |       8 |
| utf8mb4_polish_ci            | utf8mb4 |  229 |         | Yes      |       8 |
| utf8mb4_estonian_ci          | utf8mb4 |  230 |         | Yes      |       8 |
| utf8mb4_spanish_ci           | utf8mb4 |  231 |         | Yes      |       8 |
| utf8mb4_swedish_ci           | utf8mb4 |  232 |         | Yes      |       8 |
| utf8mb4_turkish_ci           | utf8mb4 |  233 |         | Yes      |       8 |
| utf8mb4_czech_ci             | utf8mb4 |  234 |         | Yes      |       8 |
| utf8mb4_danish_ci            | utf8mb4 |  235 |         | Yes      |       8 |
| utf8mb4_lithuanian_ci        | utf8mb4 |  236 |         | Yes      |       8 |
| utf8mb4_slovak_ci            | utf8mb4 |  237 |         | Yes      |       8 |
| utf8mb4_spanish2_ci          | utf8mb4 |  238 |         | Yes      |       8 |
| utf8mb4_roman_ci             | utf8mb4 |  239 |         | Yes      |       8 |
| utf8mb4_persian_ci           | utf8mb4 |  240 |         | Yes      |       8 |
| utf8mb4_esperanto_ci         | utf8mb4 |  241 |         | Yes      |       8 |
| utf8mb4_hungarian_ci         | utf8mb4 |  242 |         | Yes      |       8 |
| utf8mb4_sinhala_ci           | utf8mb4 |  243 |         | Yes      |       8 |
| utf8mb4_german2_ci           | utf8mb4 |  244 |         | Yes      |       8 |
| utf8mb4_croatian_mysql561_ci | utf8mb4 |  245 |         | Yes      |       8 |
| utf8mb4_unicode_520_ci       | utf8mb4 |  246 |         | Yes      |       8 |
| utf8mb4_vietnamese_ci        | utf8mb4 |  247 |         | Yes      |       8 |
| utf8mb4_croatian_ci          | utf8mb4 |  608 |         | Yes      |       8 |
| utf8mb4_myanmar_ci           | utf8mb4 |  609 |         | Yes      |       8 |
| utf8mb4_unicode_nopad_ci     | utf8mb4 | 1248 |         | Yes      |       8 |
| utf8mb4_unicode_520_nopad_ci | utf8mb4 | 1270 |         | Yes      |       8 |
+------------------------------+---------+------+---------+----------+---------+
```

## See Also

* [Supported Character Sets and Collations](../../../data-types/string-data-types/character-sets/supported-character-sets-and-collations.md)
* [Setting Character Sets and Collations](../../../data-types/string-data-types/character-sets/setting-character-sets-and-collations.md)
* [Information Schema COLLATIONS](../../../system-tables/information-schema/information-schema-tables/information-schema-collations-table.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
