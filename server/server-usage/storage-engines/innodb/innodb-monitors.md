---
description: >-
  InnoDB Monitors, such as the Standard, Lock, and Tablespace monitors, provide
  detailed internal state information to the error log for diagnostics.
---

# InnoDB Monitors

The [InnoDB](./) Monitor refers to particular kinds of monitors included in MariaDB and since the early versions of MySQL.

There are two types: the standard InnoDB Monitor and the InnoDB Lock Monitor.

## Standard InnoDB Monitor

The standard InnoDB Monitor returns extensive InnoDB information, particularly lock, semaphore, I/O and buffer activity:

To enable the standard InnoDB Monitor, set the [innodb\_status\_output](innodb-system-variables.md) system variable to 1. To disable it, set the system variable to zero.

For a description of the output, see [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md).

## InnoDB Lock Monitor

The InnoDB Lock Monitor displays additional lock information.

To enable the InnoDB Lock Monitor, the standard InnoDB monitor must be enabled. Then set the [innodb\_status\_output\_locks](innodb-system-variables.md) system variable to 1. To disable it, set the system variable to zero.

## SHOW ENGINE INNODB STATUS

The [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) statement can be used to obtain the standard InnoDB Monitor output when required, rather than sending it to the error log. It will also display the InnoDB Lock Monitor information if the [innodb\_status\_output\_locks](innodb-system-variables.md) system variable is set to `1`.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
