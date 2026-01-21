---
description: >-
  The Information Schema CHARACTER_SETS table contains a list of supported
  character sets, their default collations, and maximum lengths.
---

# Information Schema CHARACTER\_SETS Table

The [Information Schema](../) `CHARACTER_SETS` table contains a list of supported [character sets](../../../data-types/string-data-types/character-sets/), their default collations and maximum lengths.

It contains the following columns:

| Column                 | Description                |
| ---------------------- | -------------------------- |
| CHARACTER\_SET\_NAME   | Name of the character set. |
| DEFAULT\_COLLATE\_NAME | Default collation used.    |
| DESCRIPTION            | Character set description. |
| MAXLEN                 | Maximum length.            |

The [SHOW CHARACTER SET](../../../sql-statements/administrative-sql-statements/show/show-character-set.md) statement returns the same results (although in a different order), and both can be refined in the same way. For example, the following two statements return the same results:

```sql
SHOW CHARACTER SET WHERE Maxlen LIKE '2';
```

and

```sql
SELECT * FROM information_schema.CHARACTER_SETS 
WHERE MAXLEN LIKE '2';
```

See [Setting Character Sets and Collations](../../../data-types/string-data-types/character-sets/setting-character-sets-and-collations.md) for details on specifying the character set at the server, database, table and column levels, and [Supported Character Sets and Collations](../../../data-types/string-data-types/character-sets/supported-character-sets-and-collations.md) for a full list of supported characters sets and collations.

## Example

```sql
SELECT CHARACTER_SET_NAME FROM information_schema.CHARACTER_SETS 
WHERE DEFAULT_COLLATE_NAME LIKE '%chinese%';
+--------------------+
| CHARACTER_SET_NAME |
+--------------------+
| big5               |
| gb2312             |
| gbk                |
+--------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
