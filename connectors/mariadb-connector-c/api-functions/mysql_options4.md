# mysql\_options4

## Syntax

```bnf
#include <mysql.h>

int mysql_options4(MYSQL *mysql,
                   enum mysql_option option,
                   const void *arg1,
                   const void *arg2);
```

## Parameters

| Parameter | Description                                                                                                                                         |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `mysql`   | A connection handle previously allocated by [mysql\_init()](mysql_init.md). Must be called before [mysql\_real\_connect()](mysql_real_connect.md).  |
| `option`  | The option to set.                                                                                                                                  |
| `arg1`    | The first value for the option.                                                                                                                     |
| `arg2`    | The second value for the option.                                                                                                                    |

## Description

`mysql_options4` is used to set extra connect options and affect behavior for a connection. This function may be called multiple times to set several options. It must be called after `mysql_init()` and before `mysql_real_connect()`.

## Return Value

Returns zero on success, non-zero if the option is unknown or the value is invalid.

## Options

An overview of the possible options can be found in the description of the [`mysql_optionsv()`](mysql_optionsv.md) API function.

{% hint style="info" %}
This function is deprecated, new implementations should use [`mysql_optionsv()`](mysql_optionsv.md) api function instead.
{% endhint %}

## See Also

* [`mysql_optionsv()`](mysql_optionsv.md)
* [`mysql_options()` ](mysql_options.md)
* [mysql\_real\_connect()](mysql_real_connect.md)
