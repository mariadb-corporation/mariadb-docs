---
description: >-
  mysql_session_track_get_next retrieves subsequent session state change
  notifications after mysql_session_track_get_first, called repeatedly until a
  nonzero value signals end of data.
---

# mysql\_session\_track\_get\_next

## Syntax

```c
int mysql_session_track_get_next(MYSQL * mysql,enum enum_session_state_type type, const char **data, size_t *length );
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

`mysql_session_track_get_next()` retrieves the session status change information received from the server after a successful call to [mysql\_session\_track\_get\_first()](mysql_session_track_get_first.md).

`mysql_session_track_get_next()` needs to be called repeatedly until a non-zero return value indicates the end of data.

## Return Value

Zero for success, nonzero if an error occurred.

## History

`mysql_session_track_get_next()` was added in Connector/C 3.0 and MariaDB Server 10.2.

## See Also

* [mysql\_session\_track\_get\_first()](mysql_session_track_get_first.md)

{% @marketo/form formId="4316" %}
