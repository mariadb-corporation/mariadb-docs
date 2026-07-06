---
description: >-
  CHAR VARYING is a synonym for the VARCHAR string data type.
---

# CHAR VARYING

## Overview

This is a synonym for [VARCHAR](varchar.md).

## EXAMPLES

```sql
CREATE TABLE char_varying_example (
  example CHAR VARYING(32)
);
```

```sql
SHOW CREATE TABLE char_varying_example\G
```

```sql
*************************** 1. row ***************************
       Table: char_varying_example
Create Table: CREATE TABLE `char_varying_example` (
  `example` varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
