---
description: >-
  NATIONAL CHARACTER VARYING is a synonym for VARCHAR using the predefined utf8
  character set.
---

# NATIONAL CHARACTER VARYING

## Overview

See [NATIONAL VARCHAR](national-char.md).

## EXAMPLES

```sql
CREATE TABLE national_character_varying_example (
  example NATIONAL CHARACTER VARYING(32)
);
```

```sql
SHOW CREATE TABLE national_character_varying_example\G
```

```sql
*************************** 1. row ***************************
       Table: national_character_varying_example
Create Table: CREATE TABLE `national_character_varying_example` (
  `example` varchar(32) CHARACTER SET utf8 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
