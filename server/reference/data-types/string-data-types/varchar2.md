---
description: >-
  Variable-length character string type. VARCHAR2 columns store strings of
  variable length up to a specified maximum (up to 65,535).
---

# VARCHAR2

## Overview

This is a synonym for [VARCHAR](varchar.md).

## EXAMPLES

```sql
SET sql_mode='oracle';

CREATE TABLE varchar2_example (
  example VARCHAR2(32)
);
```

```sql
SHOW CREATE TABLE varchar2_example\G
```

```sql
*************************** 1. row ***************************
       Table: varchar2_example
Create Table: CREATE TABLE "varchar2_example" (
  "example" varchar(32) DEFAULT NULL
)
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
