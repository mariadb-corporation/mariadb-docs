# Readonly

## Overview

This filter prevents writes from being done and returns a read-only error if one
is attempted. The error that is returned is
`ER_CANT_EXECUTE_IN_READ_ONLY_TRANSACTION`, error number 1792 with SQLSTATE
`25006` and the message `Cannot execute statement in a READ ONLY transaction`.

## Configuration

This filter is an *implicit filter* and has no configuration parameters and does
not need its own configuration section. To enable it, simply add it to the
service using the module name.

```
[Read-Service]
type=service
router=readconnroute
cluster=MyCluster
filters=readonly
```

## Limitations

The filter prevents writes in two ways: by parsing the SQL and detecting writes
and by setting the default mode of transactions to read-only. The parsing will
prevent any writes that are detected from reaching the database and the
read-only mode of transactions will prevent writes in stored procedures and user
functions as well as act as a backup method in case the parsing is ineffective
in detecting a write.

The `SET TRANSACTION READ WRITE` and `START TRANSACTION READ WRITE` statements
are blocked by this filter. This is done as a safeguard against accidental
removal of the read-only transaction mode. However, if the client disables the
read-only mode directly via `SET tx_read_only=0`, the change is not detected by
the filter and writes are possible.

Given that the detection of writes is based on parsing and that parsing is not
100% effective in detecting all possible permutations of this statement
(e.g. PREPARE and EXECUTE from user variables is not detected), this cannot be
used to prevent a mischievous user from being able to turn off the read-only
mode.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
