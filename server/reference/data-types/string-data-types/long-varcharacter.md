---
description: >-
  LONG VARCHARACTER is a compatibility synonym for the MEDIUMTEXT string data
  type.
---

# LONG VARCHARACTER

## Overview

See [MEDIUMTEXT](mediumtext.md).

## EXAMPLES

```sql
CREATE TABLE long_varcharacter_example (
  example LONG VARCHARACTER
);
```

```sql
SHOW CREATE TABLE long_varcharacter_example\G
```

```sql
*************************** 1. row ***************************
       Table: long_varcharacter_example
Create Table: CREATE TABLE `long_varcharacter_example` (
  `example` mediumtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
