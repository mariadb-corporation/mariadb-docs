---
description: >-
  mysql_get_character_set_info populates a MY_CHARSET_INFO structure with
  details about the current default character set for a MariaDB Connector/C
  connection.
---

# mysql\_get\_character\_set\_info

## Syntax

```c
void mysql_get_character_set_info(MYSQL * mysql,
                                  MY_CHARSET_INFO * charset);
```

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).
* `charset` - a pointer to a MY\_CHARSET\_INFO structure, in which the information will be copied.

## Description

Returns information about the current default [character set](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets) for the specified connection.

{% hint style="info" %}
A complete list of supported character sets in the client library is listed in the function description for [mysql\_set\_character\_set\_info()](mysql_set_character_set.md).
{% endhint %}


{% @marketo/form formId="4316" %}
