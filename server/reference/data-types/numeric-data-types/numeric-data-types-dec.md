---
description: >-
  Synonym for DECIMAL. This keyword creates a fixed-point column with exact
  precision, suitable for financial calculations.
---

# DEC

See [DECIMAL](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/data-types/data-types-numeric-data-types/data-types-decimal/README.md).

## EXAMPLES

```sql
CREATE TABLE dec_example (
  example DEC
);
```

```sql
SHOW CREATE TABLE dec_example\G
```

```sql
*************************** 1. row ***************************
       Table: dec_example
Create Table: CREATE TABLE `dec_example` (
  `example` decimal(10,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
