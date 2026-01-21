---
description: >-
  Convert dynamic columns to JSON. This function returns a JSON string
  representation of the data stored in a dynamic column blob.
---

# COLUMN\_JSON

## Syntax

```sql
COLUMN_JSON(dyncol_blob)
```

## Description

Returns a JSON representation of data in `dyncol_blob`. Can also be used to display nested columns. See [dynamic columns](../../../sql-structure/nosql/dynamic-columns.md) for more information.

## Example

```sql
SELECT item_name, COLUMN_JSON(dynamic_cols) FROM assets;
+-----------------+----------------------------------------+
| item_name       | COLUMN_JSON(dynamic_cols)              |
+-----------------+----------------------------------------+
| MariaDB T-shirt | {"size":"XL","color":"blue"}           |
| Thinkpad Laptop | {"color":"black","warranty":"3 years"} |
+-----------------+----------------------------------------+
```

{% hint style="warning" %}
Limitation: `COLUMN_JSON` decodes nested dynamic columns at a nesting level of not more than 10 levels deep. Dynamic columns that are nested deeper than 10 levels are shown as `BINARY` string, without encoding.
{% endhint %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
