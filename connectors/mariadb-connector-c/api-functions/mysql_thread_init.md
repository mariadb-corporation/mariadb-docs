# mysql\_thread\_init

## Syntax

```c
my_bool mysql_thread_init(void );
```

## Description

Thread initialization for multi-threaded clients. Multi-threaded clients should call `mysql_thread_init()` at the beginning of the thread initialization to initialize thread specific client library variables. If <sub>`mysql_thread_init()`</sub> was not called explicitly, it will be called automatically by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

Returns zero if successful or 1 if an error occurred.

{% hint style="info" %}
Before a client thread ends the [mysql\_thread\_end()](mysql_thread_end.md) function must be called to release memory - otherwise the client library will report an error.
{% endhint %}

{% hint style="warning" %}
This function has been deprecated since MariaDB Connector/C 3.0.0.
{% endhint %}

## See also

* [mysql\_thread\_end()](mysql_thread_end.md)
* [mysql\_thread\_safe()](mysql_thread_safe.md)

{% @marketo/form formId="4316" %}
