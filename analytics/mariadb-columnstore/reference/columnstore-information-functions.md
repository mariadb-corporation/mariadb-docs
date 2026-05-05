---
description: >-
  MariaDB ColumnStore information functions return distributed-storage
  metadata: block IDs (idbBlockId), DBRoot, extent boundaries
  (idbExtentMin/Max), and the originating PrimProc node.
---

# ColumnStore Information Functions

## Functions

MariaDB ColumnStore information functions are selectable pseudo functions that return MariaDB ColumnStore specific “meta” information, to ensure queries can be locally directed to a specific node. These functions can be specified in the projection (`SELECT`), `WHERE`, `GROUP BY`, `HAVING` and `ORDER BY` portions of the SQL statement and are processed in a distributed manner.

| Function                     | Description                                                                                       |
| ---------------------------- | ------------------------------------------------------------------------------------------------- |
| idbBlockId(column)           | The Logical Block Identifier (LBID) for the block containing the physical row                     |
| idbDBRoot(column)            | The DBRoot where the physical row resides                                                         |
| idbExtentId(column)          | The Logical Block Identifier (LBID) for the first block in the extent containing the physical row |
| idbExtentMax(column)         | The max value from the extent map entry for the extent containing the physical row                |
| idbExtentMin(column)         | The min value from the extent map entry for the extent containing the physical row                |
| idbExtentRelativeRid(column) | The row id (1 to 8,388,608) within the column's extent                                            |
| idbLocalPm()                 | The PrimProc from which the query was launched.                                                   |
| idbPartition(column)         | The three part partition id (Directory.Segment.DBRoot)                                            |
| idbPm(column)                | The PrimProc where the physical row resides                                                       |
| idbSegmentDir(column)        | The lowest level directory id for the column file containing the physical row                     |
| idbSegment(column)           | The number of the segment file containing the physical row                                        |

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
