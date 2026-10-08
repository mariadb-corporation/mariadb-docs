---
description: >-
  The GLOBAL_VARIABLES and SESSION_VARIABLES tables store the global and session
  values of all system variables, respectively.
---

# Information Schema GLOBAL\_VARIABLES and SESSION\_VARIABLES Tables

The [Information Schema](../) `GLOBAL_VARIABLES` and `SESSION_VARIABLES` tables stores a record of all [system variables](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md) and their global and session values respectively. This is the same information as displayed by the [SHOW VARIABLES](../../../sql-statements/administrative-sql-statements/show/show-variables.md) commands `SHOW GLOBAL VARIABLES` and `SHOW SESSION VARIABLES`.

It contains the following columns:

| Column          | Description              |
| --------------- | ------------------------ |
| VARIABLE\_NAME  | System variable name.    |
| VARIABLE\_VALUE | Global or session value. |

## Example

```sql
SELECT * FROM information_schema.GLOBAL_VARIABLES ORDER BY VARIABLE_NAME\G
*************************** 1. row *****************************
 VARIABLE_NAME: ARIA_BLOCK_SIZE
VARIABLE_VALUE: 8192
*************************** 2. row *****************************
 VARIABLE_NAME: ARIA_CHECKPOINT_LOG_ACTIVITY
VARIABLE_VALUE: 1048576
*************************** 3. row *****************************
 VARIABLE_NAME: ARIA_CHECKPOINT_INTERVAL
VARIABLE_VALUE: 30
...
*************************** 455. row ***************************
 VARIABLE_NAME: VERSION_COMPILE_MACHINE
VARIABLE_VALUE: x86_64
*************************** 456. row ***************************
 VARIABLE_NAME: VERSION_COMPILE_OS
VARIABLE_VALUE: debian-linux-gnu
*************************** 457. row ***************************
 VARIABLE_NAME: WAIT_TIMEOUT
VARIABLE_VALUE: 600
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
