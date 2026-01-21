---
description: >-
  This command resets the data of a prepared statement on the server, clearing
  any buffers or previous parameter values.
---

# COM\_STMT\_RESET

Resets a prepared statement on the client and server to state after preparing.

## Fields

* [int<1>](../protocol-data-types.md#fixed-length-integers) `0x1A` `COM_STMT_RESET` header.
* [int<4>](../protocol-data-types.md#fixed-length-integers) Statement ID.

## Response

[ERR\_Packet](../4-server-response-packets/err_packet.md) or [OK\_Packet](../4-server-response-packets/ok_packet.md).

## Example

```
05 00 00 00 1A 04 00 00 00
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
