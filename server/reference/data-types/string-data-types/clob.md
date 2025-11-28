---
description: >-
  In Oracle mode, CLOB is an alias for the LONGTEXT data type used to store
  large text objects.
---

# CLOB

## Overview

This is a synonym for [LONGTEXT](longtext.md).

## EXAMPLES

```sql
SET sql_mode='oracle';

CREATE TABLE clob_example (
  example CLOB
);
```

```sql
SHOW CREATE TABLE clob_example\G
```

```sql
*************************** 1. row ***************************
       Table: clob_example
Create Table: CREATE TABLE "clob_example" (
  "example" longtext DEFAULT NULL
)
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
