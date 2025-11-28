# InnoDB Troubleshooting Overview

As with most errors, first take a look at the contents of the [MariaDB error log](../../../../server-management/server-monitoring-logs/error-log.md). If dealing with a deadlock, setting the [innodb\_print\_all\_deadlocks](../innodb-system-variables.md) option (off by default) will output details of all deadlocks to the error log.

It can also help to enable the various [InnoDB Monitors](../innodb-monitors.md) relating to the problem you are experiencing. There are four types: the standard InnoDB monitor, the InnoDB Lock Monitor, InnoDB Tablespace Monitor and the InnoDB Table Monitor.

Running [CHECK TABLE](../../../../reference/sql-statements/table-statements/check-table.md) will help determine whether there are errors in the table.

For problems with the InnoDB Data Dictionary, see [InnoDB Data Dictionary Troubleshooting](innodb-data-dictionary-troubleshooting.md).

## See Also

* [InnoDB Data Dictionary Troubleshooting](innodb-data-dictionary-troubleshooting.md)
* [InnoDB Recovery Modes](innodb-recovery-modes.md)
* [Error Codes](../../../../reference/error-codes/)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
