---
description: >-
  Fixed-length character string type. CHARACTER columns store strings of a
  specified length (0 to 255), padding with spaces if necessary.
---

# CHARACTER

## Overview

This is a synonym for [CHAR](char.md).

## EXAMPLES

```sql
CREATE TABLE character_example (
  example CHARACTER
);
```

```sql
SHOW CREATE TABLE character_example\G
```

```sql
*************************** 1. row ***************************
       Table: character_example
Create Table: CREATE TABLE `character_example` (
  `example` char(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
