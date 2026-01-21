---
description: >-
  This command fetches rows from an existing result set of a prepared statement
  that was executed with a cursor.
---

# COM\_STMT\_FETCH

Fetch rows from a prepared statement.

A [COM\_STMT\_EXECUTE](com_stmt_execute.md) with a non-zero cursor flag must have been successfully executed before any `COM_STMT_FETCH` commands can be executed.

## Fields

* [int<1>](../protocol-data-types.md) 0x1C COM\_STMT\_FETCH header.
* [int<4>](../protocol-data-types.md) statement id.
* [int<4>](../protocol-data-types.md) number of rows to fetch.

## Response

Returns one or more [binary result set rows](../4-server-response-packets/resultset-row.md#binary-resultset-row) followed by an [EOF packet](../4-server-response-packets/eof_packet.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
