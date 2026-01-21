---
description: >-
  Return values based on NULL status. This function returns the second argument
  if the first is not NULL, and the third argument if the first is NULL.
---

# NVL2

## Syntax

```sql
NVL2(expr1,expr2,expr3)
```

## Description

The `NVL2` function returns a value based on whether a specified expression is `NULL` or not. If _expr1_ is not `NULL`, then `NVL2` returns _expr2_. If _expr1_ is `NULL`, then `NVL2` returns _expr3_.

## Examples

```sql
SELECT NVL2(NULL,1,2);
+----------------+
| NVL2(NULL,1,2) |
+----------------+
|              2 |
+----------------+

SELECT NVL2('x',1,2);
+---------------+
| NVL2('x',1,2) |
+---------------+
|             1 |
+---------------+
```

## See Also

* [IFNULL (or NVL)](ifnull.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
