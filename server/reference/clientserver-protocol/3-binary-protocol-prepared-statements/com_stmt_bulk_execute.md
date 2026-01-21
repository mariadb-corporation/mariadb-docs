---
description: >-
  This command executes a bulk insert for a previously prepared statement, using
  a compact binary format for efficiency.
---

# COM\_STMT\_BULK\_EXECUTE

Executes a bulk insert of a previously prepared statement.

A command that returns a result set returns an error (Error packet).

## Direction

Client to server.

## Fields

* [int<1>](../protocol-data-types.md#fixed-length-integers) `0xfa` : `COM_STMT_BULK_EXECUTE` header.
* [int<4>](../protocol-data-types.md#fixed-length-integers) statement id.
* [int<2>](../protocol-data-types.md#fixed-length-integers) [bulk flags](com_stmt_bulk_execute.md#bulk-flags).
* If (`bulk_flag` & `SEND_TYPES_TO_SERVER`):
  * For each parameter:
    * byte<1>: [field type](../4-server-response-packets/result-set-packets.md).
    * byte<1>: [parameter type flag](com_stmt_bulk_execute.md#parameter-type-flag).
* Until end of packet:
  * For each parameter (i.e `param_count` times):
    * byte<1>: [parameter indicator](com_stmt_bulk_execute.md#parameter-indicator).
    * If indicator == `NONE`:
      * byte : binary parameter value.

## Flags

### Bulk Flags

| Flag                    | Value | Details                                                                                                                                          |
| ----------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| SEND\_UNIT\_RESULTS     | 64    | Return generated affected rows and auto-increment IDs as a result set (only when server supports `MARIADB_CLIENT_BULK_UNIT_RESULTS` capability). |
| SEND\_TYPES\_TO\_SERVER | 128   | Send types to server.                                                                                                                            |

### Parameter Type Flag

|     |          |
| --- | -------- |
| 128 | unsigned |

### Parameter Indicator

|   |         |                                                    |
| - | ------- | -------------------------------------------------- |
| 0 | NONE    | Value follow                                       |
| 1 | NULL    | Value is null                                      |
| 2 | DEFAULT | For INSERT/UPDATE, value is default                |
| 3 | IGNORE  | Value is default for insert, Is ignored for update |

## Response

The server can answer with 3 different responses:

* 0xff: [ERR\_Packet](../4-server-response-packets/err_packet.md) if any errors occur.
* 0x00: [OK\_packet](../4-server-response-packets/ok_packet.md) when query execution works without result set.
* A result set containing affected rows and auto-increment IDs when bulk flag `SEND_UNIT_RESULTS` is set.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
