---
description: >-
  Declare variables based on existing types. This feature allows defining
  variables or parameters that inherit the data type of a table column or
  another variable.
---

# TYPE OF

## Overview

This is special declaration only available inside a stored procedure.

## EXAMPLES

```sql
CREATE TABLE typeof_table(
  descr VARCHAR(20),
  val INT
);
```

```sql
INSERT INTO typeof_table VALUES ('Life', 42);
```

```sql
DELIMITER $$
CREATE PROCEDURE typeof_proc()
BEGIN
  DECLARE descr TYPE OF typeof_table.descr;
  DECLARE val TYPE OF typeof_table.val;
  SELECT * INTO descr, val FROM typeof_table;
  SELECT descr, val;
END;
$$
DELIMITER ;
```

```sql
CALL typeof_proc();

+-------+------+
| descr | val  |
+-------+------+
| Life  |   42 |
+-------+------+
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
