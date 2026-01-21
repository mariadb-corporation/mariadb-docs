---
description: >-
  Synonym for DOUBLE. This keyword declares a double-precision floating-point
  column.
---

# FLOAT8

## Overview

See [DOUBLE](double.md).

## EXAMPLES

```sql
CREATE TABLE float8_example (
  example FLOAT8
);
```

```sql
SHOW CREATE TABLE float8_example\G

*************************** 1. row ***************************
       Table: float8_example
Create Table: CREATE TABLE `float8_example` (
  `example` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
