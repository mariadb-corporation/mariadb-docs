---
description: >-
  In Oracle mode, RAW is a variable-length binary data type synonymous with
  VARBINARY.
---

# RAW

## Overview

See [VARBINARY](varbinary.md).

## EXAMPLES

```sql
SET sql_mode='oracle';
```

```
CREATE TABLE raw_example (
  example RAW(32)
);
```

```sql
SHOW CREATE TABLE raw_example\G
```

```sql
*************************** 1. row ***************************
       Table: raw_example
Create Table: CREATE TABLE "raw_example" (
  "example" varbinary(32) DEFAULT NULL
)
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
