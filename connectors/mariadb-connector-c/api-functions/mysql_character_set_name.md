---
description: >-
  mysql_character_set_name returns the name of the default client character set
  for a specified MariaDB Connector/C connection.
---

# mysql\_character\_set\_name

## Syntax

```c
const char * mysql_character_set_name(MYSQL * mysql);
```

## Parameter

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

Returns the default client [character set](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets) for the specified connection.

## Return value

The character set name used for the specified connection.

{% hint style="info" %}
This function is deprecated. Instead, use [mariadb\_get\_infov()](mariadb_get_infov.md) with option `MARIADB_CONNECTION_CHARSET_INFO`.
{% endhint %}

## See Also

* [mysql\_set\_character\_set()](mysql_set_character_set.md)

{% @marketo/form formId="4316" %}
