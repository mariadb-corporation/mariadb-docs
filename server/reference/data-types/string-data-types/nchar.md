---
description: >-
  NCHAR is a synonym for the fixed-length CHAR string data type using the utf8
  character set.
---

# NCHAR

## Overview

See [NATIONAL VARCHAR](national-char.md).

## EXAMPLES

```sql
CREATE TABLE nchar_example (
  example NCHAR(32)
);
```

```sql
SHOW CREATE TABLE nchar_example\G
```

```sql
*************************** 1. row ***************************
       Table: nchar_example
Create Table: CREATE TABLE `nchar_example` (
  `example` char(32) CHARACTER SET utf8 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
