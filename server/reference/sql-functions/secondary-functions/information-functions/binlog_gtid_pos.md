---
description: >-
  Retrieve GTID position from a binary log file. This function returns the
  Global Transaction ID corresponding to a specific file and position in the
  binlog.
---

# BINLOG\_GTID\_POS

## Syntax

```sql
BINLOG_GTID_POS(binlog_filename,binlog_offset)
```

## Description

The BINLOG\_GTID\_POS() function takes as input an old-style [binary log](../../../../server-management/server-monitoring-logs/binary-log/) position in the form of a file name and a file offset. It looks up the position in the current binlog, and returns a string representation of the corresponding [GTID](../../../../ha-and-performance/standard-replication/gtid.md) position. If the position is not found in the current binlog, NULL is returned.

## Examples

```sql
SELECT BINLOG_GTID_POS("master-bin.000001", 600);
```

## See Also

* [SHOW BINLOG EVENTS](../../../sql-statements/administrative-sql-statements/show/show-binlog-events.md) - Show events and their positions in the binary log

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
