---
description: >-
  This command checks if the server is alive and reachable, the server responds
  with an OK packet if it is running.
---

# COM\_PING

`COM_PING` permits sending a packet containing one byte to check that the connection is active.

## Fields

* [int<1>](../protocol-data-types.md#fixed-length-integers) 0x0e : `COM_PING` header.

## Response

[OK\_Packet](../4-server-response-packets/ok_packet.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
