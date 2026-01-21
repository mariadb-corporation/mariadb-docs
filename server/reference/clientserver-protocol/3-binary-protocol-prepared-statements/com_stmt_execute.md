---
description: >-
  This command executes a prepared statement using parameter values provided in
  the binary protocol format.
---

# COM\_STMT\_EXECUTE

Executes a previously prepared statement.

If specific data is large, it can be sent separately prior to this command (see [COM\_STMT\_SEND\_LONG\_DATA](com_stmt_send_long_data.md)).

If a statement is re-executed without changing the bind types, the types do not need to be sent to the server again.

## Direction

Client to server.

## Fields

* [int<1>](../protocol-data-types.md#fixed-length-integers) `0x17` : `COM_STMT_EXECUTE` header.
* [int<4>](../protocol-data-types.md#fixed-length-integers) [statement ID](com_stmt_execute.md#statement-id).
* [int<1>](../protocol-data-types.md#fixed-length-integers) flags.
* [int<4>](../protocol-data-types.md#fixed-length-integers) Iteration count (always 1).
* If (`param_count` > `0`)
  * byte<(param\_count + 7)/8> [null bitmap](com_stmt_execute.md#null-bitmap).
  * byte<1>: send type to server (0 / 1).
  * If (send type to server):
    * For each parameter:
      * byte<1>: [field type](../4-server-response-packets/result-set-packets.md).
      * byte<1>: [parameter flag](com_stmt_execute.md#parameter-flag).
  * For each parameter (for instance, `param_count` times):
    * If parameter is not null:
      * byte [binary parameter value](com_stmt_execute.md#binary-parameter-encoding).

## Statement ID

Statement ID is the identifier of the prepared statement (from [COM\_STMT\_PREPARE answer](com_stmt_prepare.md#com_stmt_prepare_ok)).

### Specific "-1" statement id value

Value `-1` (`0xFFFFFFFF`) can be used to indicate to use the last statement prepared on current connection if no `COM_STMT_PREPARE` has failed since.

This permit pipelining :

* Send `COM_STMT_PREPARE` + `COM_STMT_EXECUTE` with statement ID `-1`.
* Read `COM_STMT_PREPARE` + `COM_STMT_EXECUTE` response.

In case `COM_STMT_PREPARE` returns an error, `COM_STMT_EXECUTE` returns an error that statement ID `-1` is unknown. This permits to avoid much of the network latency.

## Flag

|   |                   |
| - | ----------------- |
| 0 | no cursor         |
| 1 | read only         |
| 2 | cursor for update |
| 4 | scrollable cursor |

### Cursors

If the flags of the `COM_STMT_EXECUTE` request a cursor to be opened, the returned result only contains the column definitions and the `EOF` that terminates it, and the result set rows are fetched using separate `COM_STMT_FETCH` commands.

Whether a cursor is actually opened is indicated by the `SERVER_STATUS_CURSOR_EXISTS` bit in the first EOF packet in the response to the `COM_STMT_EXECUTE`. If it is **not** set in, no cursor is opened and a normal result set is returned.

## Parameter Flag

Parameter type flag byte:

|     |          |
| --- | -------- |
| 128 | unsigned |

## NULL-Bitmap

The `NULL-Bitmap` indicates if parameters are null (one bit per parameter). If the parameter is `NULL`, the bit is set in the bitmap and the parameter value is not sent.

The size in bytes of the `NULL-bitmap` can be calculated with: `(parameter number + 7) / 8`

## Binary Parameter Encoding

The encoding of the `COM_STMT_EXECUTE` parameters are the same as the encoding of the [binary result sets](../4-server-response-packets/result-set-packets.md#field-types).

## Response

The server can answer with 3 different responses:

* `0xff`: [ERR\_Packet](../4-server-response-packets/err_packet.md) if any errors occur.
* `0x00`: [OK\_packet](../4-server-response-packets/ok_packet.md) when query execution works without result set.
* One (or more) [result set](../4-server-response-packets/result-set-packets.md), when query execution return rows (in case of `SELECT` query, for example).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
