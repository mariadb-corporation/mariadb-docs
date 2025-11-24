---
description: >-
  NATIONAL VARCHAR is a synonym for the VARCHAR data type using the predefined
  utf8 character set.
---

# NATIONAL VARCHAR

## Overview

Variable-length string of specific character set with limit up to 65,535 bytes.

## EXAMPLES

```sql
CREATE TABLE national_varchar_example (
  example NATIONAL VARCHAR(32)
);
```

```sql
SHOW CREATE TABLE national_varchar_example\G
```

```sql
*************************** 1. row ***************************
       Table: national_varchar_example
Create Table: CREATE TABLE `national_varchar_example` (
  `example` varchar(32) CHARACTER SET utf8 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
