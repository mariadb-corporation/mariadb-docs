---
description: >-
  The Information Schema COLLATION_CHARACTER_SET_APPLICABILITY table maps which
  character sets are associated with which collations.
---

# Information Schema COLLATION\_CHARACTER\_SET\_APPLICABILITY Table

The [Information Schema](../) `COLLATION_CHARACTER_SET_APPLICABILITY` table shows which [character sets](../../../data-types/string-data-types/character-sets/) are associated with which collations.

It contains the following columns:

| Column                | Description                                                        |
| --------------------- | ------------------------------------------------------------------ |
| COLLATION\_NAME       | Collation name.                                                    |
| CHARACTER\_SET\_NAME  | Name of the associated character set.                              |
| FULL\_COLLATION\_NAME | Name of the associated character set/collation combination.        |
| ID                    | The unique identifier of this character set/collation combination. |
| IS\_DEFAULT           | If the collation is the default for this character set.            |

The [COLLATIONS](information-schema-collations-table.md) table is table of the base `COLLATION_NAMES` in the same way that [CHARACTER\_SETS](information-schema-character_sets-table.md) table is table of the base `CHARACTER_SET_NAMES`. The `COLLATION_CHARACTER_SET_APPLICABILITY` table is the mapping between collations and character sets.

When joining the [information\_schema.TABLES](information-schema-tables-table.md) table with its field `TABLE_COLLATIONS`, this should be joined to `FULL_COLLATION_NAME` in the `COLLATION_CHARACTER_SET_APPLICABILITY` table.

See [Setting Character Sets and Collations](../../../data-types/string-data-types/character-sets/setting-character-sets-and-collations.md) for details on specifying the character set at the server, database, table and column levels.

## Example

```sql
SELECT * FROM information_schema.COLLATION_CHARACTER_SET_APPLICABILITY  WHERE
  CHARACTER_SET_NAME='utf32' ORDER BY IS_DEFAULT DESC, ID LIMIT 10;
+--------------------+--------------------+---------------------+-----+------------+
| COLLATION_NAME     | CHARACTER_SET_NAME | FULL_COLLATION_NAME | ID  | IS_DEFAULT |
+--------------------+--------------------+---------------------+-----+------------+
| utf32_general_ci   | utf32              | utf32_general_ci    |  60 | Yes        |
| utf32_bin          | utf32              | utf32_bin           |  61 |            |
| utf32_unicode_ci   | utf32              | utf32_unicode_ci    | 160 |            |
| utf32_icelandic_ci | utf32              | utf32_icelandic_ci  | 161 |            |
| utf32_latvian_ci   | utf32              | utf32_latvian_ci    | 162 |            |
| utf32_romanian_ci  | utf32              | utf32_romanian_ci   | 163 |            |
| utf32_slovenian_ci | utf32              | utf32_slovenian_ci  | 164 |            |
| utf32_polish_ci    | utf32              | utf32_polish_ci     | 165 |            |
| utf32_estonian_ci  | utf32              | utf32_estonian_ci   | 166 |            |
| utf32_spanish_ci   | utf32              | utf32_spanish_ci    | 167 |            |
+--------------------+--------------------+---------------------+-----+------------+
10 rows in set (0.004 sec)
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
