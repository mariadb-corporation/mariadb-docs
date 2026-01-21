---
description: >-
  Return the value from the N-th row. This function retrieves the value of an
  expression from the N-th row within the window frame.
---

# NTH\_VALUE

## Syntax

```sql
NTH_VALUE (expr[, num_row]) OVER ( 
  [ PARTITION BY partition_expression ] 
  [ ORDER BY order_list ]
)
```

## Description

The `NTH_VALUE` function returns the value evaluated at row number `num_row` of the window frame, starting from 1, or `NULL` if the row does not exist.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
