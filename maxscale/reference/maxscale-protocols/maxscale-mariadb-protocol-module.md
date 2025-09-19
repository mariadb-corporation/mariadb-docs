# MaxScale MariaDB Protocol Module

## MariaDB Protocol Module

The `mariadbprotocol` module implements the MariaDB client-server protocol.

The legacy protocol names `mysqlclient`, `mariadb` and `mariadbclient` are all
aliases to `mariadbprotocol`.

* [MariaDB Protocol Module](maxscale-mariadb-protocol-module.md#mariadb-protocol-module)
  * [Configuration](maxscale-mariadb-protocol-module.md#configuration)
  * [Settings](maxscale-mariadb-protocol-module.md#settings)
    * [allow\_replication](maxscale-mariadb-protocol-module.md#allow_replication)

### Configuration

Protocol level parameters are defined in the listeners. They must be defined
using the scoped parameter syntax where the protocol name is used as the prefix.

```
[MyListener]
type=listener
service=MyService
protocol=mariadbprotocol
mariadbprotocol.allow_replication=false
port=3306
```

For the MariaDB protocol module, the prefix is always `mariadbprotocol`.

### Settings

#### `allow_replication`

* Type: [boolean](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true

Whether the use of the replication protocol is allowed through this listener. If
disabled with `mariadbprotocol.allow_replication=false`, all attempts to start
replication will be rejected with a ER\_FEATURE\_DISABLED error (error number
1289\).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
