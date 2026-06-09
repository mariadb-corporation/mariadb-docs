# mysql\_load\_plugin

## Syntax

```bnf
#include <mysql.h>

struct st_mysql_client_plugin *
mysql_load_plugin(struct st_mysql *mysql, const char *name, int type,
                  int argc, ...);
```

## Parameters

| Parameter | Description                                                                                                                                   |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `mysql`   | A connection handle previously allocated by [mysql\_init()](mysql_init.md) and connected by [mysql\_real\_connect()](mysql_real_connect.md).  |
| `name`    | The name of the plugin to load.                                                                                                               |
| `type`    | The plugin type, or `-1` to accept any type.                                                                                                  |
| `argc`    | The number of optional arguments that follow.                                                                                                 |
| `...`     | Optional arguments passed to the plugin's initialization function.                                                                            |

## Description

`mysql_load_plugin` searches the client plugin directory for a plugin matching the given name and type, loads it, and calls its initialization function with any supplied arguments. If a plugin with that name is already loaded, the existing instance is returned without reloading.

## Valid Plugin Types

* `MYSQL_CLIENT_AUTHENTICATION_PLUGIN`&#x20;
* `MARIADB_CLIENT_PVIO_PLUGIN`
* `MARIADB_CLIENT_REMOTEIO_PLUGIN`&#x20;
* `MARIADB_CLIENT_CONNECTION_PLUGIN` or `MARIADB_CLIENT_COMPRESSION_PLUGIN`.

## Return Value

A pointer to the plugin handle, or `NULL` if an error occurred.

{% hint style="info" %}
* If the type of the plugin is not known, -1 needs to be specified for parameter type.
* The directory which contains the plugin can be specified either by the environment variable `MARIADB_PLUGIN_DIR` or it can be specified with [mysql\_optionsv()](mysql_optionsv.md) using the option `MYSQL_PLUGIN_DIR`.
{% endhint %}

## See Also

* [mysql\_optionsv()](mysql_optionsv.md)
