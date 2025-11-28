---
description: >-
  This command asks the server to terminate a specific connection thread,
  functionally equivalent to the KILL statement.
---

# COM\_PROCESS\_KILL

Forces the server to terminate a specified connection.

## Fields

* [int<1>](../protocol-data-types.md) `0xC` `COM_PROCESS_KILL`.
* [int<4>](../protocol-data-types.md) process ID.

## Response

[OK Packet](../4-server-response-packets/ok_packet.md) or [ERR Packet](../4-server-response-packets/err_packet.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
