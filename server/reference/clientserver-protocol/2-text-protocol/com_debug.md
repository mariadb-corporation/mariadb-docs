---
description: >-
  This command forces the server to dump debug information to the standard
  output or log, requiring the SUPER privilege.
---

# COM\_DEBUG

The `COM_DEBUG` command forces the server to dump debug information to stdout. It requires the [SUPER](../../sql-statements/account-management-sql-statements/grant.md#super) privilege.

## Fields

* [int<1>](../protocol-data-types.md#fixed-length-integers) `0xOD` : `COM_DEBUG` header.

## Response

[EOF Packet](../4-server-response-packets/eof_packet.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
