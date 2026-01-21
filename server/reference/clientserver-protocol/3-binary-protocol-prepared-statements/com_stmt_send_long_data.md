---
description: >-
  This command sends long data, such as BLOB or TEXT values, in chunks for a
  specific parameter of a prepared statement.
---

# COM\_STMT\_SEND\_LONG\_DATA

When data for a specific column is large, it can be sent separately to avoid the limitation of `max_allowed_packet` (see [packet splitting](../0-packet.md#packet-splitting)).

Multiple `COM_STMT_SEND_LONG_DATA` commands with the same column ID append the data. `COM_STMT_SEND_LONG_DATA` is sent before [COM\_STMT\_EXECUTE](com_stmt_execute.md).

## Fields

* [int<1>](../protocol-data-types.md#fixed-length-integers) `0x18` `COM_STMT_SEND_LONG_DATA` header.
* [int<4>](../protocol-data-types.md#fixed-length-integers) statement id.
* [int<2>](../protocol-data-types.md#fixed-length-integers) parameter number.
* [byte](../protocol-data-types.md#end-of-file-length-bytes) data.

## Response

Server doesn't send response.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
