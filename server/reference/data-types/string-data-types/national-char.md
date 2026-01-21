---
description: >-
  NATIONAL CHAR is a synonym for the CHAR data type that uses the predefined
  utf8 character set.
---

# NATIONAL CHAR

## Overview

Fixed-length string of specific character set with limit up to 255 bytes.

## Examples

```sql
CREATE TABLE national_char_example (
  example NATIONAL CHAR(32)
);
```

```sql
SHOW CREATE TABLE national_char_example\G
```

```sql
*************************** 1. row ***************************
       Table: national_char_example
Create Table: CREATE TABLE `national_char_example` (
  `example` char(32) CHARACTER SET utf8 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

## External References

Additional information is available [here](varchar.md).

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
