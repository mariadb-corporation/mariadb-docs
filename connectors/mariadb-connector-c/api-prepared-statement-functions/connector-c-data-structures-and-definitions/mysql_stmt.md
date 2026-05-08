---
description: >-
  MYSQL_STMT is the MariaDB Connector/C handle for a prepared statement,
  allocated by mysql_stmt_init and released by mysql_stmt_close; all its
  members are private.
---

# MYSQL\_STMT

The `MYSQL_STMT` structure is a handle for a prepared statement. The handle will be allocated by [mysql\_stmt\_init()](../mysql_stmt_init.md) and released by [mysql\_stmt\_close()](../mysql_stmt_close.md).

* All members of `MYSQL_STMT` are private and not intended for application use.
* Multiple statement handles can be opened within the same connection.
* After a successful call to [mysql\_stmt\_prepare()](../mysql_stmt_prepare.md) a prepared statement will also allocate resources on the server.
* Closing the connection with [mysql\_close()](../../api-functions/mysql_close.md) invalidates the statements but doesn't free resources on the client.


{% @marketo/form formId="4316" %}
