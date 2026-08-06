# MaxScale 23.08 MariaDB Protocol Module

## MaxScale 23.08 MariaDB Protocol Module

## MariaDB Protocol Module

The `mariadbprotocol` module implements the MariaDB client-server protocol.

The legacy protocol names `mysqlclient`, `mariadb` and `mariadbclient` are all
aliases to `mariadbprotocol`.

* [MariaDB Protocol Module](mariadb-maxscale-2308-maxscale-2308-mariadb-protocol-module.md#mariadb-protocol-module)
  * [Configuration](mariadb-maxscale-2308-maxscale-2308-mariadb-protocol-module.md#configuration)
    * [allow\_replication](mariadb-maxscale-2308-maxscale-2308-mariadb-protocol-module.md#allow_replication)

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

#### `allow_replication`

* Type: [boolean](https://mariadb.com/kb/en/maxscale-2308-getting-started-mariadb-maxscale-configuration-guide/#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true

Whether the use of the replication protocol is allowed through this listener. If
disabled with `mariadbprotocol.allow_replication=false`, all attempts to start
replication will be rejected with a ER\_FEATURE\_DISABLED error (error number\
1289\).

CC BY-SA / Gnu FDL
