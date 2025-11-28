---
description: LONG VARBINARY is a compatibility synonym for the MEDIUMBLOB binary data type.
---

# LONG VARBINARY

## Overview

See [MEDIUMBLOB](mediumblob.md).

## EXAMPLES

```sql
CREATE TABLE long_varbinary_example (
  example LONG VARBINARY
);
```

```sql
SHOW CREATE TABLE long_varbinary_example\G
```

```sql
*************************** 1. row ***************************
       Table: long_varbinary_example
Create Table: CREATE TABLE `long_varbinary_example` (
  `example` mediumblob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
