---
description: >-
  This event is used for LOAD DATA INFILE operations, managing the execution
  phase similar to a QUERY_EVENT but with extra static fields for file handling.
---

# EXECUTE\_LOAD\_QUERY\_EVENT

This event is written to the binary log file for [LOAD DATA INFILE](../../sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) events. The event format is similar to a [QUERY\_EVENT](query_event.md), except that it has extra static fields.

## Header

* Event Type = 0x12.

## Fields

### Fixed Data Part

* [uint<4>](../protocol-data-types.md#fixed-length-integers) The ID of the thread that issued this statement on the master.
* [uint<4>](../protocol-data-types.md#fixed-length-integers) The time in seconds that the statement took to execute.
* [uint<1>](../protocol-data-types.md#fixed-length-integers) The length of the name of the database which was the default database when the statement was executed. This name appears later, in the variable data part. It is necessary for statements such as `INSERT INTO t VALUES(1)` that don't specify the database and rely on the default database previously selected by `USE`.
* [uint<2>](../protocol-data-types.md#fixed-length-integers) The error code resulting from execution of the statement on the master.
* [uint<2>](../protocol-data-types.md#fixed-length-integers) The length of the status variable block.
* [uint<4>](../protocol-data-types.md#fixed-length-integers) The ID of the loaded file.
* [uint<4>](../protocol-data-types.md#fixed-length-integers) Offset from the start of the statement to the beginning of the filename.
* [uint<4>](../protocol-data-types.md#fixed-length-integers) Offset from the start of the statement to the end of the filename.
* [uint<1>](../protocol-data-types.md#fixed-length-integers) How `LOAD DATA INFILE` handles duplicates (0x0: error, 0x1: ignore, 0x2: replace).

### Variable Data Part

* [byte](../protocol-data-types.md#fixed-length-bytes) Zero or more status variables. Each status variable consists of one byte code identifying the variable stored, followed by the value of the variable. The format of the value is variable-specific.\
  The number of bytes 'n' is the length of the status variable block (read in fixed data part)
* [string](../protocol-data-types.md#fixed-length-bytes) The default database name (null-terminated).
* [string](../protocol-data-types.md#fixed-length-bytes) The SQL statement. By subtraction the size of the statement can be known.

## Example

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
