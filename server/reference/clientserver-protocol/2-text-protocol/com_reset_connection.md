---
description: >-
  This command resets the session state (variables, tables, etc.) to its initial
  values without closing the connection.
---

# COM\_RESET\_CONNECTION

`COM_RESET_CONNECTION` resets a connection without reauthentication.

The command does this:

* Roll back any open transactions.
* Reset transaction isolation level.
* Rset session variables.
* Delete user variables.
* Remove temporary tables.
* Remove all `PREPARE` statements.

Database will `NOT` be reset to initial value.

## Fields

* [int<1>](../protocol-data-types.md#fixed-length-integers) 0x1f : `COM_RESET_CONNECTION` Header

## Response

[ERR\_Packet](../4-server-response-packets/err_packet.md) or [OK\_Packet](../4-server-response-packets/ok_packet.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
