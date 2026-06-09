# mariadb\_get\_info

## Syntax

```bnf
#include <mysql.h>

my_bool mariadb_get_info(MYSQL *mysql, enum mariadb_value value, void *arg)
```

## Description

Retrieves generic or connection related information.

{% hint style="info" %}
This function is deprecated. Please use [mariadb\_get\_infov()](mariadb_get_infov.md) instead.
{% endhint %}

## See Also

* [mariadb\_get\_infov()](mariadb_get_infov.md)&#x20;
