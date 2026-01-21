---
description: >-
  This command deallocates a prepared statement on the server, freeing up
  associated resources.
---

# COM\_STMT\_CLOSE

Closes a previously prepared statement.

## Direction

Client to server.

## Implemented by

* [mysql\_stmt\_close()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-prepared-statement-functions/mysql_stmt_close).
* [mysql\_stmt\_prepare()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-prepared-statement-functions/mysql_stmt_prepare).

## Fields

* [int<1>](../protocol-data-types.md#fixed-length-integers) `0x19` `COM_STMT_CLOSE` header.
* [int<4>](../protocol-data-types.md#fixed-length-integers) statement id.

## Example

05 00 00 00 19 04 00 00 00

## Response

No response from server.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
