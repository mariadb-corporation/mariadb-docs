---
description: >-
  Synonym for TINYINT(1). This type is commonly used to represent boolean
  values, where 0 is considered false and non-zero values are true.
---

# BOOL

## Overview

See [TINYINT](tinyint.md).

## EXAMPLES

```sql
CREATE TABLE bool_example (
  example BOOL
) DEFAULT CHARSET=latin1;
```

```sql
SHOW CREATE TABLE bool_example\G
```

```sql
*************************** 1. row ***************************
       Table: bool_example
Create Table: CREATE TABLE `bool_example` (
  `example` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
