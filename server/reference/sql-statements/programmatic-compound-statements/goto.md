---
description: >-
  Jump to a labeled point in the code. This Oracle-compatible statement
  transfers execution control to a specific label within the stored program.
---

# GOTO

## Syntax

```sql
GOTO label
```

## Description

The `GOTO` statement causes the code to jump to the specified label, and continue operating from there. It is only accepted when in [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle).

## Example

```sql
SET sql_mode=ORACLE;

DELIMITER //

CREATE OR REPLACE PROCEDURE p1 AS

BEGIN

  SELECT 1;
  GOTO label;
  SELECT 2;
  <<label>>
  SELECT 3;

END;

//

DELIMITER 

CALL p1();
+---+
| 1 |
+---+
| 1 |
+---+
1 row in set (0.000 sec)

+---+
| 3 |
+---+
| 3 |
+---+
1 row in set (0.000 sec)
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
