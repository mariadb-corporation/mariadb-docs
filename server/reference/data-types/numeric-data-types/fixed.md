---
description: >-
  Synonym for DECIMAL. This keyword is used to define columns that require exact
  numeric precision, such as currency.
---

# FIXED

## Overview

See [DECIMAL](decimal.md).

## EXAMPLES

```sql
CREATE TABLE fixed_example (
  example FIXED
);
```

```sql
SHOW CREATE TABLE fixed_example\G

*************************** 1. row ***************************
       Table: fixed_example
Create Table: CREATE TABLE `fixed_example` (
  `example` decimal(10,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
