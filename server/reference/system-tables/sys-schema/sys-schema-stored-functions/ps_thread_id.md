---
description: >-
  The ps_thread_id function returns the internal Performance Schema thread ID
  associated with a given connection ID.
---

# ps\_thread\_id

{% include "../../../../.gitbook/includes/sys-schema-is-available-fro....md" %}

## Syntax

```
sys.ps_thread_id(connection_id)
```

## Description

`ps_thread_id` is a [stored function](../../../../server-usage/stored-routines/stored-functions/) available with the [Sys Schema](../) that returns the thread\_id associated with the given _connection\_id_. If the _connection\_id_ is `NULL`, returns the thread\_id for the current connection.

## Examples

```sql
SELECT * FROM performance_schema.threads\G
*************************** 13. row ***************************
          THREAD_ID: 13
               NAME: thread/sql/one_connection
               TYPE: FOREGROUND
     PROCESSLIST_ID: 3
   PROCESSLIST_USER: msandbox
   PROCESSLIST_HOST: localhost
     PROCESSLIST_DB: test
PROCESSLIST_COMMAND: Query
   PROCESSLIST_TIME: 0
  PROCESSLIST_STATE: Sending data
   PROCESSLIST_INFO: SELECT * FROM performance_schema.threads
   PARENT_THREAD_ID: 1
               ROLE: NULL
       INSTRUMENTED: YES
            HISTORY: YES
    CONNECTION_TYPE: Socket
       THREAD_OS_ID: 24379


SELECT sys.ps_thread_id(3);
+---------------------+
| sys.ps_thread_id(3) |
+---------------------+
|                  13 |
+---------------------+

SELECT sys.ps_thread_id(NULL);
+------------------------+
| sys.ps_thread_id(NULL) |
+------------------------+
|                     13 |
+------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
