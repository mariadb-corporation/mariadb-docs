---
description: LONG VARCHAR is a compatibility synonym for the MEDIUMTEXT string data type.
---

# LONG VARCHAR

## Overview

See [MEDIUMTEXT](mediumtext.md).

## EXAMPLES

```sql
CREATE TABLE long_varchar_example (
  example LONG VARCHAR
);
```

```sql
SHOW CREATE TABLE long_varchar_example\G
```

```sql
*************************** 1. row ***************************
       Table: long_varchar_example
Create Table: CREATE TABLE `long_varchar_example` (
  `example` mediumtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
