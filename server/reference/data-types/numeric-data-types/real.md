---
description: >-
  Synonym for DOUBLE. In standard SQL mode, REAL is a double-precision
  floating-point number.
---

# REAL

## Overview

See [DOUBLE](double.md).

## EXAMPLES

```sql
CREATE TABLE real_example (
  example REAL
);
```

```sql
SHOW CREATE TABLE real_example\G
```

```sql
*************************** 1. row ***************************
       Table: real_example
Create Table: CREATE TABLE `real_example` (
  `example` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
