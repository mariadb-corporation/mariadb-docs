---
description: >-
  Synonym for YEAR. This keyword is an alias used for declaring a column to
  store year values.
---

# SQL\_TSI\_YEAR

## Overview

See [YEAR](../../sql-functions/date-time-functions/year.md).

## EXAMPLES

```sql
CREATE TABLE sql_tsi_year_example (
  example SQL_TSI_YEAR
);
```

```sql
SHOW CREATE TABLE sql_tsi_year_example\G
```

```sql
*************************** 1. row ***************************
       Table: sql_tsi_year_example
Create Table: CREATE TABLE `sql_tsi_year_example` (
  `example` year(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
