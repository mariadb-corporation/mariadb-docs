---
description: >-
  This is an internal command used to represent a sleeping connection that is
  waiting for a new command from the client.
---

# COM\_SLEEP

This command is used inside the server only.

## Direction

Used inside server only.

## Fields

* [int<1>](../protocol-data-types.md#fixed-length-integers) `0x00`: `COM_SLEEP` header.

## Response

[ERR\_Packet](../4-server-response-packets/err_packet.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
