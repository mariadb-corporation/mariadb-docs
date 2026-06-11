---
description: >-
  UPDATE for MariaDB ColumnStore changes data in existing rows with
  single-table or multi-table syntax, supporting WHERE, ORDER BY, and LIMIT
  clauses.
---

# ColumnStore UPDATE

The `UPDATE` statement changes data stored in rows.

## Syntax

### Single-Table Syntax

```bnf
UPDATE  table_reference 
  SET col1={expr1|DEFAULT} [,col2={expr2|DEFAULT}] ...
  [WHERE where_condition]
  [ORDER BY ...]
  [LIMIT row_count]
```

### Multiple-Table Syntax

```sql
UPDATE table_references
    SET col1={expr1|DEFAULT} [, col2={expr2|DEFAULT}] ...
    [WHERE where_condition]
```

{% hint style="info" %}
Only **one** table can be updated from the table list in `table_reference`.\
However, multiple columns can be updated.
{% endhint %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
