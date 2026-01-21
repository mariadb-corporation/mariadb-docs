---
description: >-
  NATIONAL CHARACTER is a synonym for the CHAR data type using the predefined
  utf8 character set.
---

# NATIONAL CHARACTER

## Overview

See [NATIONAL CHAR](national-char.md).

## EXAMPLES

```sql
CREATE TABLE national_character_example (
  example NATIONAL CHARACTER(32)
);
```

```sql
SHOW CREATE TABLE national_character_example\G
```

```sql
*************************** 1. row ***************************
       Table: national_character_example
Create Table: CREATE TABLE `national_character_example` (
  `example` char(32) CHARACTER SET utf8 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
