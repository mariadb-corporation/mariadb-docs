---
description: >-
  LONG and LONG VARCHAR are compatibility synonyms for the MEDIUMTEXT string
  data type.
---

# LONG and LONG VARCHAR

`LONG` and `LONG VARCHAR` are synonyms for [MEDIUMTEXT](mediumtext.md).

```sql
CREATE TABLE t1 (a LONG, b LONG VARCHAR);

DESC t1;
+-------+------------+------+-----+---------+-------+
| Field | Type       | Null | Key | Default | Extra |
+-------+------------+------+-----+---------+-------+
| a     | mediumtext | YES  |     | NULL    |       |
| b     | mediumtext | YES  |     | NULL    |       |
+-------+------------+------+-----+---------+-------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
