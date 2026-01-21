---
description: >-
  The EOF_Packet marks the end of a result set or a sequence of packets,
  containing warning counts and server status flags.
---

# EOF\_Packet

The `EOF_Packet` marks the end of a result set, and returns status and warnings.

When testing for an EOF packet, the packet size must be less than 9 bytes in length. The result set can send data that begin with a `0xfe` byte, but then the packet length will be greater than 9.

## Fields

* [int<1>](../protocol-data-types.md#fixed-length-integers) 0xfe : EOF header.
* [int<2>](../protocol-data-types.md#fixed-length-integers) warning count.
* [int<2>](../protocol-data-types.md#fixed-length-integers) [server status](ok_packet.md#server-status-flag).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
