---
description: >-
  Configure listening ports for client connections. This reference details how
  to define listeners, associate them with services, and enable protocol
  features like Proxy Protocol.
---

# MaxScale Listeners

A listener defines a port MaxScale listens on for incoming connections. Accepted connections are linked with a MaxScale service. Multiple listeners can feed the same service.

## Configuration

A listener requires a unique name, a type of `listener`, a service to forward traffic to, and a port or socket.

```ini
[Read-Write-Listener]
type=listener
service=Read-Write-Service
protocol=MariaDBClient
port=4006
```

## Settings

### `service`

* Type: service
* Mandatory: Yes
* Dynamic: No

The service to which the listener is associated. This is the name of a service that is defined elsewhere in the configuration file.

### `protocol`

* Type: protocol
* Mandatory: No
* Dynamic: No
* Default: `mariadb`

The name of the protocol module used for communication between the client and MaxScale. The same protocol is also used for backend communication.

Usually this does not need to be defined as the default protocol is the MariaDB network protocol that is used by SQL connections.

For NoSQL client connections, the protocol must be set to `protocol=nosqlprotocol`. For more details on how to configure the NoSQL protocol, refer to the [NoSQL Protocol](maxscale-protocols/maxscale-nosql-protocol-module.md) module documentation.

### `address`

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `"::"`

This sets the address the listening socket is bound to. The address may be specified as an IP address in 'dot notation' or as a hostname. If left undefined the listener will bind to all network interfaces.

### `port`

* Type: number
* Mandatory: Yes, if `socket` is not provided.
* Dynamic: No
* Default: `0`

The port the listener listens on. If left undefined a default port for the protocol is used.

### `socket`

* Type: string
* Mandatory: Yes, if `port` is not provided.
* Dynamic: No
* Default: `""`

If defined, the listener uses Unix domain sockets to listen for incoming connections. The parameter value is the name of the socket to use.

If you want to use both network ports and UNIX domain sockets with a service, define two separate listeners that connect to the same service.

### `authenticator`

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

The authenticator module to use. Each protocol module defines a default authentication module, which is used if the setting is left undefined. MariaDB protocol support multiple authenticators and they can be used simultaneously by giving a comma-separated list e.g. `authenticator=mariadbauth,gssapiauth`

### `authenticator_options`

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

This defines additional options for authentication. As of MaxScale 2.5.0, only _MariaDBClient_ and its authenticators support additional options. The value of this parameter should be a comma-separated list of key-value pairs. See authenticator specific documentation for more details.

### `sql_mode`

* Type: [enum](maxscale-listeners.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `default`, `oracle`
* Default: `default`

Specify the sql mode for the listener similarly to global `sql_mode` setting. If both are used this setting will override the global setting for this listener.

### `proxy_protocol_networks`

Define an IP-address or a subnetwork which may send a [proxy protocol header](https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt) when connecting. The proxy header contains the original client IP-address and port, and MaxScale will use that information in its internal bookkeeping. This means the client is authenticated as if it was connecting from the host in the proxy header. If proxy protocol is also enabled in MaxScale server settings, MaxScale will relay the original client address and port to the server. See [server settings](maxscale-listeners.md#proxy_protocol) for more information.

This setting may be useful if a compatible load balancer is relaying client connections to MaxScale. If proxy headers are used, both MaxScale and the backends will know where the client originally came from.

The `proxy_protocol_networks`-setting works similarly to the equivalent setting in [MariaDB Server](../../server/clients-and-utilities/server-client-software/client-libraries/proxy-protocol-support.md). The value can be a single IP or subnetwork, or a comma-separated list of them. Subnetworks are given in CIDR-format, e.g. "192.168.0.0/16". "\*" is a valid value, allowing anyone to send the header. "localhost" allows proxy headers from domain socket connections.

Only trusted IPs should be added to the list, as the proxy header may affect authentication results.

```
proxy_protocol_networks=192.168.0.1,198.168.0.0/16
```

Similar to MariaDB Server, MaxScale will also accept normal connections even if `proxy_protocol_networks` is configured for the listener.

### `connection_init_sql_file`

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

Path to a text file with sql queries. Any sessions created from the listener will send the contents of the file to backends after authentication. Each non-empty line in the file is interpreted as a query. Each query must succeed for the backend connection to be usable for client queries. The queries should not return any data.

```
connection_init_sql_file=/home/dba/init_queries.txt
```

Example query file:

```sql
set @myvar = 'mytext';
set @myvar2 = 4;
```

### `user_mapping_file`

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

Path to a json-text file with user and group mapping, as well as server credentials. Only affects MariaDB-protocol based listeners. Default value is empty, which disables the feature.

```
user_mapping_file=/home/root/mapping.json
```

Should not be used together with [PAM Authenticator](maxscale-authenticators/maxscale-pam-authenticator.md) settings `pam_backend_mapping` or `pam_mapped_pw_file`, as these may overwrite the mapped credentials. Is most powerful when combined with service setting `user_accounts_file`, as then MaxScale can accept users that do not exist on backends and map them to backend users.

This file functions very similar to [PAM-based mapping](../../server/reference/plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/user-and-group-mapping-with-pam.md) Both user-to-user and group-to-user mappings can be defined. Also, the password and authentication plugin for the mapped users can be added. The file is only read during listener creation (typically MaxScale start) or when a listener is modified during runtime. When a client logs into MaxScale, their username is searched from the mapping data. If the name matches either a name mapping or a Linux group mapping, the username is replaced by the mapped name. The mapped name is then used when logging into backends. If the file also contains credentials for the mapped user, then those are used. Otherwise, MaxScale tries to log in with an empty password and default MariaDB authentication.

Three arrays are read from the file: _user\_map_, _group\_map_ and _server\_credentials_, none of which are mandatory.

Each array element in the _user\_map_-array must define the following fields:

* original\_user: String. Incoming client username.
* mapped\_user: String. Username the client is mapped to.

Each array element in the _group\_map_-array must define the following fields:

* original\_group: String. Incoming client Linux group.
* mapped\_user: String. Username the client is mapped to.

Each array element in the _server\_credentials_-array can define the following fields:

* mapped\_user: String. The mapped username this password is for.
* password: String. Backend server password. Can be encrypted with maxpasswd.
* plugin: String, optional. Authentication plugin to use. Must be enabled on the listener. Defaults to empty, which results in standard MariaDB authentication.

When a client successfully logs into MaxScale, MaxScale first searches for name-based mapping. The incoming client does not need to be a Linux user for name-based mapping to take place. If the name is not found, MaxScale checks if the client is a Linux user with a group membership matching an element in the group mapping array. If the client is a member of more than 100 groups, this check may fail.

If a mapping is found, MaxScale searches the credentials array for a matching username, and uses the password and plugin listed. The plugin need not be the same as the one the original user used. Currently, "mysql\_native\_password" and "pam" are supported as mapped plugins.

An example mapping file is below.

```json
{
    "user_map": [
        {
            "original_user": "bob",
            "mapped_user": "janet"
        },
        {
            "original_user": "karen",
            "mapped_user": "janet"
        }
    ],
    "group_map": [
        {
            "original_group": "visitors",
            "mapped_user": "db_user"
        }
    ],
    "server_credentials": [
        {
            "mapped_user": "janet",
            "password": "secret_pw",
            "plugin": "mysql_native_password"
        },
        {
            "mapped_user": "db_user",
            "password": "secret_pw2",
            "plugin": "pam"
        }
    ]
}
```

### `connection_metadata`

* Type: stringlist
* Default: `character_set_client=auto,character_set_connection=auto,character_set_results=auto,max_allowed_packet=auto,system_time_zone=auto,time_zone=auto,tx_isolation=auto,maxscale=auto`
* Dynamic: Yes
* Mandatory: No

Metadata that's sent to all connecting clients. The value must be a comma-separated list of key-value arguments. The keys or values cannot contain commas in them.

Any values that are set to `auto` will be substituted with the value of the corresponding MariaDB system variable. Any system variables that do not not exist or have empty or null values will not be sent to the client. The system variable values are read from the first `Master` server that's reachable from the listener's service. If no `Master` server is reachable, the value is read from the first `Slave` server and if no `Slave` servers are available, from the first `Running` server. If no running servers are available, the system variables are not sent.

The exception to this is the `maxscale=auto` value where the `auto` will be replaced with the MaxScale version string. This is useful for detecting whether a client is connected to MaxScale. To make MaxScale completely transparent to the client application, the `maxscale=auto` value can be removed from `connection_metadata`.

MaxScale will always send a metadata value for `threads_connected` that contains the current number of connections to the service that the listener points to and for `connection_id` that contains the 64-bit connection ID value. The values can be overridden by defining them with some value, for example, `connection_metadata=threads_connected=0,connection_id=0`.

The metadata is implemented using [the session state information](../../server/reference/clientserver-protocol/4-server-response-packets/ok_packet.md#session-state-info) that is embedded in the OK packets that are generated by MaxScale. The values are encoded as system variables changes. This information can be accessed by all connectors that support reading the session state information. One example of this is the MariaDB Connector/C that implements it with the [mysql\_session\_track\_get\_first](https://github.com/mariadb-corporation/mariadb-connector-c/wiki/mysql_session_track_get_first) and [mysql\_session\_track\_get\_next](https://github.com/mariadb-corporation/mariadb-connector-c/wiki/mysql_session_track_get_next) functions.

The following example demonstrates the use of `connection_metadata`:

```
connection_metadata=redirect_url=localhost:3306,service_name=my-service,max_allowed_packet=auto
```

The configuration has three variables, `redirect_url`, `service_name` and `max_allowed_packet` that have the values `localhost:3306`, `my-service` and `auto`. The `auto` value is special and gets replaced with the `max_allowed_packet` value from the MariaDB server. This means that the final metadata that is sent to the client would be `redirect_url=localhost:3306`, `service_name=my-service` and `max_allowed_packet=16777216`.

**Version-specific Behavior**

If the `connection_metadata` variable list contains the `tx_isolation` variable and the backend MariaDB server from which the variable is retrieved is MariaDB 11 or newer, the value is renamed to `transaction_isolation`. The `tx_isolation` parameter was deprecated in favor of `transaction_isolation` in MariaDB 11 (MDEV-21921).

### `redirect_url`

* Type: URL
* Mandatory: No
* Dynamic: Yes
* Default: `""`

Database URL where clients are redirected.

If set, the `redirect_url` system variable tracker is sent in the final response to the client after authentication is complete. The URL must start with a valid connection prefix, either `mariadb://` or `mysql://`, and if a port is defined it must be a number.

If the [connection metadata](maxscale-listeners.md#connection_metadata) has `redirect_url` in it and the `redirect_url` parameter is defined, the value of the `redirect_url` parameter is used.

For more information about connection redirection and how MaxScale deals with it, read the [Connection Redirection](maxscale-protocols/maxscale-mariadb-protocol-module.md#connection-redirection) section in the MariaDB protocol module documentation.
