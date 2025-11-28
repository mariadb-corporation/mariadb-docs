---
description: >-
  NATIONAL VARCHARACTER is a synonym for VARCHAR using the predefined utf8
  character set.
---

# NATIONAL VARCHARACTER

## Overview

See [NATIONAL VARCHAR](national-char.md).

## EXAMPLES

```sql
CREATE TABLE national_varcharacter_example (
  example NATIONAL VARCHARACTER(32)
);
```

```sql
SHOW CREATE TABLE national_varcharacter_example\G
```

```sql
*************************** 1. row ***************************
       Table: national_varcharacter_example
Create Table: CREATE TABLE `national_varcharacter_example` (
  `example` varchar(32) CHARACTER SET utf8 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
