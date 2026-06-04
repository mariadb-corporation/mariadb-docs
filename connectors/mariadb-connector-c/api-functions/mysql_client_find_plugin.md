# mysql\_client\_find\_plugin

## Syntax

```bnf
#include <mysql.h>
struct st_mysql_client_plugin * 
mysql_client_find_plugin(MYSQL *mysql, const char *name, int type);
```

## Parameters

* `mysql` is a connection identifier, which was previously initialized by [mysql\_init()](mysql_init.md) and optional connected by [mysql\_real\_connect()](mysql_real_connect.md).
* `name` The name of the plugin.
* `type` The plugin type.

## Valid Plugin Types

* `MYSQL_CLIENT_AUTHENTICATION_PLUGIN`
* `MARIADB_CLIENT_PVIO_PLUGIN`
* `MARIADB_CLIENT_REMOTEIO_PLUGIN`
* `MARIADB_CLIENT_CONNECTION_PLUGIN` or `MARIADB_CLIENT_COMPRESSION_PLUGIN`.

## Return Value

A pointer to the plugin handle, or NULL if an error occurred.

{% hint style="info" %}
If the type of the plugin is not known, -1 needs to be specified for parameter type.
{% endhint %}

## See Also

* [mysql\_load\_plugin()](mysql_load_plugin.md)
