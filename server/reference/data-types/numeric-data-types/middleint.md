---
description: Synonym for MEDIUMINT. This keyword refers to the 3-byte integer type.
---

# MIDDLEINT

## Overview

See [MEDIUMINT](mediumint.md).

## EXAMPLES

```sql
CREATE TABLE middleint_example (
  example MIDDLEINT
);
```

```sql
SHOW CREATE TABLE middleint_example\G
```

```sql
*************************** 1. row ***************************
       Table: middleint_example
Create Table: CREATE TABLE `middleint_example` (
  `example` mediumint(9) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
