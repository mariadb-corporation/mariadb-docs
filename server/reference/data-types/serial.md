---
description: >-
  Alias for BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE. This shorthand data
  type is often used to define primary keys.
---

# SERIAL

## Overview

This is an alias for `BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE`.

## EXAMPLES

```sql
CREATE TABLE serial_example (
  id SERIAL,
  data VARCHAR(32)
);
```

```sql
SHOW CREATE TABLE serial_example\G
```

```sql
*************************** 1. row ***************************
       Table: serial_example
Create Table: CREATE TABLE `serial_example` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `data` varchar(32) DEFAULT NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

## EXTERNAL REFERENCES

Additional information is available [here](auto_increment.md).

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
