---
description: >-
  mysql_options sets extra connection options on a MYSQL handle before
  calling mysql_real_connect. Deprecated since Connector/C 3.0 — use
  mysql_optionsv instead.
---

# mysql\_options

## Syntax

```c
int mysql_options(MYSQL * mysql,
                  enum mysql_option,
                  const void * arg);
```

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).
* `mysql_option` - the option you want to set. See description below.
* `arg` - the value for the option.

## Description

Used to set extra connect options and affect behavior for a connection. This function may be called multiple times to set several options. mysql\_options() should be called after [mysql\_init()](mysql_init.md) and before [mysql\_real\_connect()](mysql_real_connect.md).

Returns zero on success, non zero if an error occurred (invalid option or value).

{% hint style="warning" %}
This function is deprecated as of MariaDB Connector/C 3.0 and will be removed in future releases. It's preferable to use [mysql\_optionsv](mysql_optionsv.md).
{% endhint %}

### Options

See [mysql\_optionsv](mysql_optionsv.md).

## See also

* [mysql\_init()](mysql_init.md)
* [mysql\_optionsv](mysql_optionsv.md)
* [mysql\_real\_connect()](mysql_real_connect.md)


{% @marketo/form formId="4316" %}
