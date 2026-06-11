---
description: >-
  mysql_session_track_get_first retrieves the first session state change
  notification from the server, covering schema changes, system variables, and
  state flags. Added in Connector/C 3.0.
---

# mysql\_session\_track\_get\_first

## Syntax

```c
int mysql_session_track_get_first(MYSQL * mysql,enum enum_session_state_type type, const char **data, size_t *length );
```

## Parameters

* `mysql` - mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).
* `type` - type of information. Valid values are
  * `SESSION_TRACK_SYSTEM_VARIABLES`
  * `SESSION_TRACK_SCHEMA`
  * `SESSION_TRACK_STATE_CHANGE`
  * `SESSION_TRACK_GTIDS` (unsupported)
* `data` - pointer to data, which must be declared as `const char *`
* `length` - pointer to a `size_t` variable, which will contain the length of data

## Description

`mysql_session_track_get_first()` retrieves the first session status change information received from the server.

Depending on the specified type the read only data pointer will contain the following information:

* `SESSION_TRACK_SCHEMA`: The name of the default schema (database)
* `SESSION_TRACK_SYSTEM_VARIABLES`: If a session system variable is changed, the first call contains the name of the changed system variable, the second call contains the new value. Both name and value are represented as strings.
* `SESSION_TRACK_STATE_CHANGE`: shows whether the session status has changed. The value is changed as string "1" (changed) or "0" (unchanged).

Further data needs to be obtained by calling [mysql\_session\_track\_get\_next()](mysql_session_track_get_next.md).

## Returns

Zero for success, nonzero if an error occurred.

## History

`mysql_session_track_get_first()` was added in Connector/C 3.0 and MariaDB Server 10.2.

## See also

[mysql\_session\_track\_get\_next()](mysql_session_track_get_next.md)

{% @marketo/form formId="4316" %}
