---
description: >-
  Oracle-compatible synonym for DECIMAL. This type is used for fixed-point
  arithmetic.
---

# NUMBER

```sql
NUMBER[(M[,D])] [SIGNED | UNSIGNED | ZEROFILL]
```

In [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle), `NUMBER` is a synonym for [DECIMAL](decimal.md).

## EXAMPLES

Number\_Example

```sql
SET sql_mode='oracle';
```

```
CREATE TABLE number_example (
  example NUMBER
);
```

```sql
SHOW CREATE TABLE number_example\G
```

```sql
*************************** 1. row ***************************
       Table: number_example
Create Table: CREATE TABLE "number_example" (
  "example" double DEFAULT NULL
)
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
