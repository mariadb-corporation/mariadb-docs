---
description: Synonym for DECIMAL. This type stores exact numeric data values.
---

# NUMERIC

## Overview

See [DECIMAL](decimal.md).

## EXAMPLES

```sql
CREATE TABLE numeric_example (
  example NUMERIC
);
```

```sql
SHOW CREATE TABLE numeric_example\G
```

```sql
*************************** 1. row ***************************
       Table: numeric_example
Create Table: CREATE TABLE `numeric_example` (
  `example` decimal(10,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
