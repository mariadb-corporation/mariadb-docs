# mysql\_thread\_end

## Syntax

```c
void mysql_thread_end(void );
```

## Description

The `mysql_thread_end()` function needs to be called before a client thread ends. It will release thread-specific memory, which was allocated by a previous [mysql\_thread\_init()](mysql_thread_init.md) call. Returns void.

{% hint style="info" %}
Unlike [mysql\_thread\_init()](mysql_thread_init.md) `mysql_thread_end()` will not be invoked automatically if the thread ends. To avoid memory leaks `mysql_thread_end()` must be called explicitly.
{% endhint %}

{% hint style="warning" %}
This function has been deprecated since MariaDB Connector/C 3.0.0.
{% endhint %}

## See also

* [mysql\_thread\_init()](mysql_thread_init.md)
* [mysql\_thread\_safe()](mysql_thread_safe.md)

{% @marketo/form formId="4316" %}
