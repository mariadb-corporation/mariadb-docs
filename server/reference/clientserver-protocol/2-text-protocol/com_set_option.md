---
description: >-
  This command configures client-specific options for the current connection,
  such as enabling or disabling multi-statements.
---

# COM\_SET\_OPTION

Enables or disables server option.

## Fields

* [int<1>](../protocol-data-types.md) `0x1B` `COM_SET_OPTION` .
* [int<2>](../protocol-data-types.md) option.

## **Options**

| Constant                            | Value |
| ----------------------------------- | ----- |
| `MYSQL_OPTION_MULTI_STATEMENTS_ON`  | 0     |
| `MYSQL_OPTION_MULTI_STATEMENTS_OFF` | 1     |

## Response

[EOF Packet](../4-server-response-packets/eof_packet.md) on success or [ERR packet](../4-server-response-packets/err_packet.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
