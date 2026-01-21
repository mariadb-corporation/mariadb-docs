---
description: >-
  This command requests the server to shut down, it requires the SHUTDOWN
  privilege to be executed successfully.
---

# COM\_SHUTDOWN

Shuts down the server. To execute this command, the [SHUTDOWN](../../sql-statements/account-management-sql-statements/grant.md#shutdown) privilege is required.

## Fields

* [int<1>](../protocol-data-types.md) 0x0A COM\_SHUTDOWN
* [int<1>](../protocol-data-types.md) option

## **Options**

|                   |       |
| ----------------- | ----- |
| Constant          | Value |
| SHUTDOWN\_DEFAULT | 0     |

#### Response

[OK Packet](../4-server-response-packets/ok_packet.md) or [ERR packet](../4-server-response-packets/err_packet.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
