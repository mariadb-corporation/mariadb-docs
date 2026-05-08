---
description: >-
  mysql_character_set_name returns the name of the default client character
  set for a specified MariaDB Connector/C connection.
---

# mysql\_character\_set\_name

## Syntax

```c
const char * mysql_character_set_name(MYSQL * mysql);
```

`mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

Returns the default client [character set](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets) for the specified connection.


{% @marketo/form formId="4316" %}
