---
description: >-
  Complete MariaDB MaxScale configuration guide. Complete reference for
  listeners, servers, monitors, routers, and SSL settings with comprehensive
  examples and.
---

# MaxScale Configuration Guide

## Introduction

This document describes how to configure MariaDB MaxScale and presents some possible usage scenarios. MariaDB MaxScale is designed with flexibility in mind, and consists of an event processing core with various support functions and plugin modules that tailor the behavior of the program.

## Concepts

### Glossary

| Word                | Description                                                                                                                                                                                                                                                                                                                                      |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| connection routing  | Connection routing is a method of handling requests in which MariaDB MaxScale will accept connections from a client and route data on that connection to a single database using a single connection. Connection based routing will not examine individual requests on a connection and it will not move that connection once it is established. |
| statement routing   | Statement routing is a method of handling requests in which each request within a connection will be handled individually. Requests may be sent to one or more servers and connections may be dynamically added or removed from the session.                                                                                                     |
| module              | A module is a separate code entity that may be loaded dynamically into MariaDB MaxScale to increase the available functionality. Modules are implemented as run-time loadable shared objects.                                                                                                                                                    |
| connection failover | When a connection currently being used between MariaDB MaxScale and the database server fails a replacement will be automatically created to another server by MariaDB MaxScale without client intervention                                                                                                                                      |
| backend database    | A term used to refer to a database that sits behind MariaDB MaxScale and is accessed by applications via MariaDB MaxScale.                                                                                                                                                                                                                       |
| REST API            | HTTP administrative interface                                                                                                                                                                                                                                                                                                                    |

### Objects

#### Server

A server represents an individual database server to which a client can be connected via MariaDB MaxScale. The status of a server varies during the lifetime of the server and typically the status is updated by some monitor. However, it is also possible to update the status of a server manually.

| Status                   | Description                                                                                                                                                                                                                                                                                                                |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Running                  | The server is running.                                                                                                                                                                                                                                                                                                     |
| Master                   | The server is the primary.                                                                                                                                                                                                                                                                                                 |
| Slave                    | The server is a replica.                                                                                                                                                                                                                                                                                                   |
| Draining                 | The server is being drained. Existing connections can continue to be used, but no new connections will be created to the server. Typically this status bit is turned on manually using maxctrl, but a monitor may also turn it on.                                                                                         |
| Drained                  | The server has been drained. The server was being drained and now the number of connections to the server has dropped to 0.                                                                                                                                                                                                |
| Auth Error               | The monitor cannot login and query the server due to insufficient privileges.                                                                                                                                                                                                                                              |
| Maintenance              | The server is under maintenance. Typically this status bit is turned on manually using maxctrl, but it will also be turned on for a server that for some reason is blocking connections from MaxScale. When a server is in maintenance mode, no connections will be created to it and existing connections will be closed. |
| Slave of External Master | The server is a replica of a primary that is not being monitored.                                                                                                                                                                                                                                                          |
| Master Stickiness        | The server is monitored by a galeramon with disable\_master\_failback=true. See [disable\_master\_failback](../../../../reference/maxscale-monitors/galera-monitor.md#disable_master_failback) for more information.                                                                                                          |

For more information on how to manually set these states via MaxCtrl, read the [Administration Tutorial](../../../../mariadb-maxscale-tutorials/maxscale-administration-tutorial.md).

#### Monitor

A monitor module is capable of monitoring the state of a particular kind of cluster and making that state available to the routers of MaxScale.

Examples of monitor modules are `mariadbmon` that is capable of monitoring a regular primary-replica cluster and in addition of performing both _switchover_ and _failover_, `galeramon` that is capable of monitoring a Galera cluster, and `csmon` that is capable of monitoring a ColumnStore cluster.

Monitor modules have sections of their own in the MaxScale configuration file.

#### Filter

A filter module resides in front of routers in the request processing chain of MaxScale. That is, a filter will see a request before it reaches the router and before a response is sent back to the client. This allows filters to reject, handle, alter or log information about a request.

Examples of filters `cache` that provides query caching according to rules, `regexfilter` that can rewrite requests according to regular expressions, and `qlafilter` that logs information about requests.

Filters have sections of their own in the MaxScale configuration file that are referred to from _services_.

Simple filters that do not have any settings can be created automatically by referring to them by the module name in the `filters` list of a service. For example, using `filters=hintfilter` in a service will create a filter named `hintfilter` using the module `hintfilter`.

Limitations:

* MaxScale: No limitations.
* MaxScale Lite: At most 2 filters can be created.

#### Router

A router module is capable of routing requests to backend servers according to the characteristics of a request and/or the algorithm the router implements. Examples of routers are `readconnroute` that provides _connection routing_, that is, the server is chosen according to specified rules when the session is created and all requests are subsequently routed to that server, and `readwritesplit` that provides _statement routing_, that is, each individual request is routed to the most appropriate server.

Routers do not have sections of their own in the MaxScale configuration file, but are referred to from _services_.

#### Service

A service abstracts a set of databases and makes them appear as a single one to the client. Depending on what router (e.g. `readconnroute` or `readwritesplit`) the service uses, the servers are used in some particular way. If the service uses filters, then all requests will be pre-processed in some way before they reach the router.

Services have sections of their own in the MaxScale configuration file.

Limitations:

* MaxScale: No limitations.
* MaxScale Lite: At most 2 services can be created.

#### Listener

A listener defines a port MaxScale listens on. Connection requests arriving on that port will be forwarded to the service the listener is associated with. A listener may be associated with a single service, but several listeners may be associated with the same service.

Listeners have sections of their own in the MaxScale configuration file.

#### Include

An [include section](#include-1) defines common parameters used in other configuration sections.

## Administration

The administration of MaxScale can be divided in two parts:

* Writing the MaxScale configuration file, which is described in the following [section](#configuration).
* Performing runtime modifications using [MaxCtrl](../../../../reference/maxscale-maxctrl.md)

For detailed information about _MaxCtrl_ please refer to the specific documentation referred to above. In the following it will only be explained how MaxCtrl relate to each other, as far as user credentials go.

**Note**: By default all runtime configuration changes are saved on disk and loaded on startup. Refer to the [Dynamic Configuration](#dynamic-configuration) section for more details on how it works and how to disable it.

MaxCtrl can connect using TCP/IP sockets. When connecting with MaxCtrl using TCP/IP sockets, the user and password must be provided and are checked against a separate user credentials database. By default, that database contains the user `admin` whose password is `mariadb`.

Note that if MaxCtrl is invoked without explicitly providing a user and password then it will by default use `admin` and `mariadb`. That means that when the default user is removed, the credentials must always be provided.

### Administration audit file

The REST API calls to MaxScale can be logged by enabling [admin\_audit](global-settings.md#admin_audit).

For more detail see the admin audit configuration values `admin_audit`, `admin_audit_file` and `admin_audit_exclude_methods` below and [Administration Tutorial](../../../../mariadb-maxscale-tutorials/maxscale-administration-tutorial.md).

### Static Configuration Parameters

The following global configuration parameters can **NOT** be changed at runtime and can only be defined in a configuration file:

* `admin_auth`
* `admin_enabled`
* `admin_gui`
* `admin_host`
* `admin_pam_readonly_service`
* `admin_pam_readwrite_service`
* `admin_readonly_hosts`
* `admin_readwrite_hosts`
* `admin_port`
* `admin_secure_gui`
* `admin_ssl_ca`
* `admin_ssl_version`
* `admin_jwt_algorithm`
* `admin_jwt_key`
* `admin_jwt_issuer`
* `auto_tune`
* `connector_plugindir`
* `core_file`
* `datadir`
* `debug`
* `libdir`
* `load_persisted_configs`
* `persist_runtime_changes`
* `local_address`
* `log_augmentation`
* `log_warn_super_user`
* `logdir`
* `module_configdir`
* `persistdir`
* `piddir`
* `query_retries`
* `require_secure_transport`
* `secretsdir`
* `sharedir`
* `sql_mode`
* `substitute_variables`
* `threads_max`

All other parameters that relate to objects can be altered at runtime or can be changed by destroying and recreating the object in question.

## Configuration

MaxScale by default reads configuration from the file `/etc/maxscale.cnf`. If the command line argument `--configdir=<path>` is given, `maxscale.cnf` is searched for in _\<path>_ instead. If the argument `--config=<file>` is given, configuration is read from the file _\<file>_.

MaxScale also looks for a directory with the same name as the configuration file, followed by ".d" (for example `/etc/maxscale.cnf.d`). If found, MaxScale recursively reads all files with the ".cnf" suffix in the directory hierarchy. Other files are ignored.

After loading normal configuration files, MaxScale reads runtime-generated configuration files, if any, from the [persisted configuration files directory](global-settings.md#persistdir).

Different configuration sections can be arranged with little restrictions. Global path settings such as `logdir`, `piddir` and `datadir` are only read from the main configuration file. Other global settings are also best left in the main file to ensure they are read before other configuration sections are parsed.

The configuration file format used is [INI](https://en.wikipedia.org/wiki/INI_file), similar to the MariaDB Server. The files contain sections and each section can contain multiple key-value pairs.

Comments are defined by prefixing a row with a hash (#). Trailing comments are not supported.

```
# This is a comment before a parameter
some_parameter=123
```

A parameter can be defined on multiple lines as shown below. A value spread over multiple lines is simply concatenated. The additional lines of the value definition need to have at least one whitespace character in the beginning.

```
[MyService]
type=service
router=readconnroute
servers=server1,
        server2,
        server3
```

### Names

Section names may not contain whitespace and must not start with the characters `@@`.

As the object names are used to form URLs in the MaxScale REST API, they must be safe for use in URLs. This means that only alphanumeric characters (i.e. `a-z`, `A-Z` and `0-9`) and the special characters `_.~-` can be used.

### Dynamic Configuration

By default all changes done at runtime via the MaxScale GUI, MaxCtrl or the REST API will be saved on disk, inside the [persistdir](global-settings.md#persistdir) directory. The changes done at runtime will override the configuration found in the static configuration files for that particular object.

This means that if an object that is found in `/etc/maxscale.cnf` is modified at runtime, all future changes to it must also be done at runtime. Any modifications done to `/etc/maxscale.cnf` after a runtime change has been made are ignored for that object.

To prevent the saving of runtime changes and to make all runtime changes volatile, add [persist\_runtime\_changes=false](global-settings.md#persist_runtime_changes) and [load\_persisted\_configs=false](global-settings.md#load_persisted_configs) under the `[maxscale]` section. This will make MaxScale behave like the MariaDB server does: any changes done with `SET GLOBAL` statements are lost if the process is restarted.

### Special Parameter Types

#### Booleans

Boolean type parameters interpret the values `true`, `yes`, `on` and `1` as _true_ values and `false`, `no`, `off` and `0` as _false_ values. Starting with MaxScale 23.02, the REST API also accepts the same boolean values for boolean type parameters.

#### Sizes

Where _specifically noted_, a number denoting a size can be suffixed by a subset of the IEC binary prefixes or the SI prefixes. In the former case the number will be interpreted as a certain multiple of 1024 and in the latter case as a certain multiple of 1000. The supported IEC binary suffixes are `Ki`, `Mi`, `Gi` and `Ti` and the supported SI suffixes are `k`, `M`, `G` and `T`. In both cases, the matching is case-insensitive.

For instance, the following entries

```
max_size=1099511628000
max_size=1073741824Ki
max_size=1048576Mi
max_size=1024Gi
max_size=1Ti
```

are equivalent, as are the following

```
max_size=1000000000000
max_size=1000000000k
max_size=1000000M
max_size=1000G
max_size=1T
```

#### Durations

A number denoting a duration can be suffixed by one of the case-insensitive suffixes `h`, `m` or `min`, `s` and `ms`, for specifying durations in hours, minutes, seconds and milliseconds, respectively.

For instance, the following entries

```
soft_ttl=1h
soft_ttl=60m
soft_ttl=60min
soft_ttl=3600s
soft_ttl=3600000ms
```

are equivalent.

Note that if an explicit unit is not specified, then it is specific to the configuration parameter whether the duration is interpreted as seconds or milliseconds.

_Not_ providing an explicit unit has been deprecated in MaxScale 2.4.

#### Percent

A number denoting a percent must be suffixed with `%`.

For instance

```
some_param=42%
```

#### Regular Expressions

Many modules have settings which accept a regular expression. In most cases, these settings are named either _match_ or _exclude_, and are used to filter users or queries. MaxScale uses the [PCRE2-library](https://www.pcre.org/current/doc/html/) for matching regular expressions.

When writing a regular expression (regex) type parameter to a MaxScale configuration file, the pattern string should be enclosed in slashes e.g. `^select` -> `match=/^select/`. This clarifies where the pattern begins and ends, even if it includes whitespace. Without slashes the configuration loader trims the pattern from the ends. The slashes are removed before compiling the pattern. For backwards compatibility, the slashes are not mandatory. Omitting them is, however, deprecated. The _binlogfilter_, _ccrfilter_, _namedserverfilter_, _qlafilter_, _regexfilter_, _tee_, _topfilter_, _avrorouter_, _kafkacdc_, and _schemarouter_ modules accept parameters in this type of regular expression form. Other modules may not handle the slashes correctly.

PCRE2 supports a complicated regular expression [syntax](https://www.pcre.org/current/doc/html/pcre2syntax.html). MaxScale typically uses regular expressions simply, only checking whether the pattern and subject match at some point. For example, using the QLAFilter and setting `match=/SELECT/` causes the filter to accept any query with the text "SELECT" somewhere within. To force the pattern to only match at the beginning of the query, set `match=/^SELECT/`. To only match the end, set`match=/SELECT$/`.

Modules which accept regular expression parameters also often accept options which affect how the patterns are compiled. Typically, this setting is called _options_ and accepts values such as `ignorecase`, `case` and `extended`.

* `ignorecase`: Causes the regular expression matcher to ignore letter case, and is often on by default. When enabled, `/SELECT/` would match both `SELECT` and`select`.
* `extended`: Ignores whitespace and `#` comments in the pattern. Note that this is not the same as the extended regular expression syntax that for example`grep -E` uses.
* `case`: Turns on case-sensitive matching. This means that `/SELECT/` will not match `select`.

These settings can also be defined in the pattern itself, so they can be used even in modules without pattern compilation settings. The pattern settings are `(?i)` for `ignorecase` and `(?x)` for `extended`. See the [PCRE2 syntax documentation](https://www.pcre.org/current/doc/html/pcre2syntax.html#SEC16) for more information.

**Standard regular expression settings for filters**

Many filters use the settings _match_, _exclude_ and _options_. Since these settings are used in a similar way across these filters, the settings are explained here. The documentation of the filters link here and describe any exceptions to this generalized explanation.

These settings typically limit the queries the filter module acts on. _match_ and _exclude_ define PCRE2 regular expression patterns while _options_ affects how both of the patterns are compiled. _options_ works as explained above, accepting the values `ignorecase`, `case` and `extended`, with `ignorecase` being the default.

The queries are matched as they arrive to the filter on their way to a routing module. If _match_ is defined, the filter only acts on queries matching that pattern. If _match_ is not defined, all queries are considered to match.

If _exclude_ is defined, the filter only acts on queries not matching that pattern. If _exclude_ is not defined, nothing is excluded.

If both are defined, the query needs to match _match_ but not match _exclude_.

Even if a filter does not act on a query, the query is not lost. The query is simply passed on to the next module in the processing chain as if the filter was not there.

#### Enumerations

Enumeration type parameters have a predefined set of accepted values. For types declared as `enum`, only one value is accepted. For `enum_mask` types, multiple values can be defined by separating them with commas. All enumeration values in MaxScale are case-sensitive.

For example the `router_options` parameter in the `readconnroute` router is a mask type enumeration:

```
router_options=master,slave
```

#### Path Lists

A `pathlist` type parameter expects one or more filesystem paths separated by colons. The value must not include space between the separators.

Here is an example path list parameter that points to `/tmp/something.log` and `/var/log/maxscale/maxscale.log`:

```
path_list_parameter=/tmp/something.log:/var/log/maxscale/maxscale.log
```

### Global Settings

The global settings, in a section named `[MaxScale]`, allow various parameters that affect MariaDB MaxScale as a whole to be tuned. This section must be defined in the root configuration file which by default is `/etc/maxscale.cnf`.

**Note**: MariaDB MaxScale providess multiple global diagnostic and debugging options (including `gdb-stacktrace` and `dump-network-traffic`), which can be used to diagnose and troubleshoot core behavior.

For convenience, here is a quick overview of available diagnostic and debugging settings:

| Settings                    | Brief Description                                       |
| --------------------------- | ------------------------------------------------------- |
| `disable-module-unloading`  | Prevents modules from unloading during runtime          |
| `enable-module-unloading`   | Allows the unloading of modules during runtime          |
| `redirect-output-to-file`   | Reroutes `stdout` and `stderr` to a specified file.     |
| `enable-statement-logging`  | Allows logging of all SQL statements                    |
| `disable-statement-logging` | Disables SQL statement logging                          |
| `enable-cors`               | Enables Cross-Origin Resource Sharing (CORS) support    |
| `cors-allow-origin`         | Specifies COR's allowed origin                          |
| `allow-duplicate-servers`   | Multiple servers can use the same address and port      |
| `gdb-stacktrace`            | Enables the generation of gdb stacktraces upon crash    |
| `sql-batch-size`            | Determines the batch size for processing SQL statements |
| `disable-fcrdns`            | Disables the forward-confirmed reverse DNS lookup       |
| `dump-network-traffic`      | Dumps network traffic for debugging purposes            |
| `exception-frequency`       | Sets the frequency of generated API exceptions          |

See the [MaxScale Configuration Settings](../../../../reference/maxscale-configuration-settings.md) page for a comprehensive list of these configuration parameters.

Every global setting, with its type, default, and behavior, is described in [MaxScale Global Settings](global-settings.md), in alphabetical order.

#### REST API Configuration

The MaxScale REST API is an HTTP interface that provides JSON format data intended to be consumed by monitoring applications and visualization tools.

The following options must be defined under the `[maxscale]` section in the configuration file.

The REST API settings are the global settings whose names start with `admin_`. They are described in [MaxScale Global Settings](global-settings.md).

### Events

MaxScale logs warnings and errors for various reasons and often it is self- evident and generally applicable whether some occurrence should warrant a warning or an error, or perhaps just an info-level message.

However, there are events whose seriousness is not self-evident. For instance, in some environments an authentication failure may simply indicate that someone has made a typo, while in some other environment that can only happen in case there has been a security breech.

To handle events like these, MaxScale defines _events_ whose logging facility and level can be controlled by the administrator. Given an event `X`, its facility and level are controlled in the following manner:

```
event_X_facility=LOG_LOCAL0
event_X_level=LOG_ERR
```

The above means that if event _X_ occurs, then that is logged using the facility `LOG_LOCAL0` and the level `LOG_ERR`.

The valid values of `facility` are the facility values reported by`man syslog`, e.g.`LOG_AUTH`,`LOG_LOCAL0`and`LOG_USER`. Likewise, the valid values for `level`are the ones also reported by`man syslog`, e.g.`LOG_WARNING`,`LOG_ERR`and`LOG\_CRIT\`.

Note that MaxScale does not act upon the level, that is, even if the level of a particular event is defined to be `LOG_EMERG`, MaxScale will not shut down if that event occurs.

The default facility is `LOG_USER` and the default level is `LOG_WARNING`.

Note that you may also have to configure `rsyslog` to ensure that the event can be logged to the intended log file. For instance, if the facility is chosen to be `LOG_AUTH`, then `/etc/rsyslog.conf` should contain a line like

```
auth,authpriv.*                 /var/log/auth.log
```

for the logged events to end up in `/var/log/auth.log`, where the initial`auth` is the relevant entry.

The available events are:

#### `authentication_failure`

This event occurs when there is an authentication failure.

```
event_authentication_failure_facility=LOG_AUTH
event_authentication_failure_level=LOG_CRIT
```

#### `firewall_incident`

This event occurs when the firewall blocks a query.

```
event_firewall_incident_facility=LOG_AUTH
event_firewall_incident_level=LOG_CRIT
```

#### `session_start`

{% hint style="info" %}
This event is available from MaxScale 26.10.
{% endhint %}

This event occurs when a client session is successfully started.
```
event_session_start_facility=LOG_AUTH
event_session_start_level=LOG_NOTICE
```

#### `session_stop`

{% hint style="info" %}
This event is available from MaxScale 26.10.
{% endhint %}

This event occurs when a client disconnects.
```
event_session_stop_facility=LOG_AUTH
event_session_stop_level=LOG_NOTICE
```

{% tabs %}
{% tab title="< 26.10" %}
This feature is only available in MaxScale 26.10.0 and later.
{% endtab %}
{% endtabs %}

#### `transaction_replay_failure`

This event occurs when a readwritesplit service with `transaction_replay=true` fails to replay a transaction.

```
event_transaction_replay_failure_level=LOG_INFO
```

{% tabs %}
{% tab title="< 26.10" %}
This feature is only available in MaxScale 26.10.0 and later.
{% endtab %}
{% endtabs %}

### Service

A service represents the database service that MariaDB MaxScale offers to the clients. In general a service consists of a set of backend database servers and a routing algorithm that determines how MariaDB MaxScale decides to send statements or route connections to those backend servers.

A service may be considered as a virtual database server that MariaDB MaxScale makes available to its clients.

Several different services may be defined using the same set of backend servers. For example a connection based routing service might be used by clients that already performed internal read/write splitting, whilst a different statement based router may be used by clients that are not written with this functionality in place. Both sets of applications could access the same data in the same databases.

A service is identified by a service name, which is the name of the configuration file section and a type parameter of service.

```
[Test-Service]
type=service
```

In order for MariaDB MaxScale to forward any requests it must have at least one service defined within the configuration file. The definition of a service alone is not enough to allow MariaDB MaxScale to forward requests however, the service is merely present to link together the other configuration elements.

Every service setting, with its type, default, and behavior, is described in [MaxScale Service Settings](service-settings.md), in alphabetical order.

### Filter

Filters provide a means to manipulate or process requests as they pass through MariaDB MaxScale between the client side protocol and the query router. A full explanation of each filter's functionality can be found in its documentation.

#### `module`

* Type: filter
* Mandatory: Yes
* Dynamic: No
* Description: The module parameter specifies the name of the filter module that is included in the routing chain.

The `module` parameter defines the name of the filter module that is added to the routing chain.

### Server

Server sections define the backend database servers MaxScale uses. A server is identified by its section name in the configuration file. The only mandatory parameter of a server is _type_, but _address_ and _port_ are also usually defined. A server may be a member of one or more services. A server may only be monitored by at most one monitor.

```
[MyMariaDBServer1]
type=server
address=127.0.0.1
port=3000
```

For a complete list of server configuration parameters, see the [Server Reference](../../../../reference/maxscale-servers.md).

Limitations:

* MaxScale: No limitations.
* MaxScale Trial: At most 3 servers can be created.

### Monitor

Monitor sections are used to define the monitoring module that watches a set of servers. Each server can only be monitored by one monitor.

Common monitor parameters [can be found here](../../../../reference/maxscale-monitors/common-monitor-parameters.md).

### Listener

A listener defines a port MaxScale listens on for incoming connections. Accepted connections are linked with a MaxScale service. Multiple listeners can feed the same service. Mandatory parameters are _type_, _service_ and _protocol_. _address_ is optional, it limits connections to a certain network interface only. _socket_ is also optional and is used for Unix socket connections.

The network socket where the listener listens may have a backlog of connections. The size of this backlog is controlled by the _net.ipv4.tcp\_max\_syn\_backlog_ and _net.core.somaxconn_ kernel parameters.

Increasing the size of the backlog by modifying the kernel parameters helps with sudden connection spikes and rejected connections. For more information see [listen(2)](https://man7.org/linux/man-pages/man2/listen.2.html).

```
[MyListener1]
type=listener
service=MyService1
port=3006
```

For a complete list of listener configuration parameters, see the [Listener Reference](../../../../reference/maxscale-listeners.md).

#### `sni_mapping_file`

{% hint style="info" %}
This setting is available from MaxScale 26.10.
{% endhint %}

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: none
* Description: Defines the path to a JSON file that maps SNI hostnames to certificates and services.

Path to file that contains the
[SNI](https://en.wikipedia.org/wiki/Server_Name_Indication) hostname-to-service
mapping for this listener. SNI allows a client to connect to different MaxScale
services through one listener. To work, SNI-mapping requires the following:

* Client-to-MaxScale connection is encrypted.
* Multiple hostnames are registered to the MaxScale host machine.
* Client application or connector sends the target hostname during SSL
  negotiation.

Ensure that your client application or connector supports SNI before attempting
to use SNI service mapping in MaxScale. For example,
[Connector/C 3.4.8](https://mariadb.com/docs/release-notes/connectors/c/3.4/3.4.8) and
[Connector/J 3.5.7](https://mariadb.com/docs/release-notes/connectors/java/3.5/3.5.7)
include SNI support.

When this feature is enabled, MaxScale reads the hostname the client wants to
connect to during SSL negotiation. If the hostname is found in the SNI mapping
configuration, MaxScale changes both the certificate MaxScale presents to the
client and the MaxScale service the client connects to from the standard
listener values to the ones defined in the mapping. The client essentially sees
a different MaxScale depending on the hostname it connects to, even if the final
IP address is unchanged. If the mapping contains no hostname that matches the
one the client requested, the client will use the standard service configured to
the listener.

If set, `sni_mapping_file` must point to a readable file in JSON format. The
file can contain two sub-elements: *certificates* and
*hostname_to_service_mapping*.  The former defines the certificate and key files
used in the latter.

*certificates* is an object that contains sub-objects, one for each certificate
and keyfile pair.  Each certificate sub-object must define the following:

* ssl_cert: String. Path to the certificate file.
* ssl_key: String. Path to the certificate private key file.

The key of the sub-object defines the name for the certificate file pair. This
name is used to refer to the certificate in *hostname_to_service_mapping*. The
certificate files referred to by the SNI configuration are processed similarly
to other MaxScale certificate files. Thus, it's recommended to also generate
them using similar tools and settings.

*hostname_to_service_mapping* defines an array of mapping elements. Each element
 must contain:

* hostnames: Array of strings. Each string must at least look like a valid
  hostname. Defines the hostnames this mapping element applies to.
* certificate: String. Name of the certificate presented to the client. Must
  match one of the certificate names defined in *certificates*.
* service: String. Name of the MaxScale service the client should be routed to.
  Must be a valid MaxScale service.

The certificates and the mapping are stored in different objects so that one
certificate can be easily shared between multiple service mapping elements.

An example SNI mapping file is below.

```
{
    "certificates":
    {
        "my-alternate-crt1": {
            "ssl_cert": "/home/me/ssl/alt-crt1.crt",
            "ssl_key": "/home/me/ssl/alt-crt2.key"
        },
        "my-alternate-crt2": {
            "ssl_cert": "/home/me/ssl/alt-crt2.crt",
            "ssl_key": "/home/me/ssl/alt-crt2.key"
        }
    },

    "hostname_to_service_mapping": [
        {
            "hostnames": ["alternate-host1", "alternate-host1b", "alternate-host1c"],
            "certificate": "my-alternate-crt1",
            "service": "Alt-Service-A"
        },
        {
            "hostnames": ["alternate-host2"],
            "certificate": "my-alternate-crt2",
            "service": "Alt-Service-B"
        },
        {
            "hostnames": ["alternate-host3"],
            "certificate": "my-alternate-crt2",
            "service": "Alt-Service-C"
        }
    ]
}
```

### Include

An _include_ section defined common parameters used in other configuration sections. Consider the following configuration.

```
[Monitor1]
type=monitor
module=mariadbmon
user=the_user
password=the_password
handle_events=false
monitor_interval=2000ms
backend_connect_timeout = 3s
backend_connect_attempts = 5
servers=Server1, Server2

[Monitor2]
type=monitor
module=mariadbmon
user=the_user
password=the_password
handle_events=false
monitor_interval=2000ms
backend_connect_timeout = 3s
backend_connect_attempts = 5
servers=Server3, Server4
```

The two monitor sections are identical except for the `servers` setting. If they otherwise should remain identical, a change must be made in two places. With an `include` section the situation can be simplified.

```
[Monitor-Common]
type=include
module=mariadbmon
user=the_user
password=the_password
handle_events=false
monitor_interval=2000ms
backend_connect_timeout = 3s
backend_connect_attempts = 5

[Monitor1]
type=monitor
@include=Monitor-Common
servers=Server1, Server2

[Monitor2]
type=monitor
@include=Monitor-Common
servers=Server3, Server3
```

With an `include` section, all common settings can be defined in one place, and then included to any number of other sections using the `@include` parameter.

The `@include` parameter takes a list of section names, so the settings can be distributed across several `include` sections.

```
@include=Some-Common-Attributes, Other-Common-Attributes
```

It is permissible to specify in the _including_ section, parameters that have already been specified in the _included_ section and they will take precedence. For instance, if `Monitor2` in the example above should have a longer backend connect timeout it can be specified as follows.

```
[Monitor2]
type=monitor
@include=Monitor-Common
servers=Server3, Server3
backend_connect_timeout = 5s
```

Note that an included section **must** be an `include` section and that an `include` section **cannot** include another `include` section. For instance, both of the following sections would cause an error at startup.

```
[Monitor-Common]
type=include
@include=Base-Common
...

[Monitor2]
type=monitor
@include=Monitor1
...
```

Note also that if an included parameter is changed using `maxctrl`, it will be changed _only_ on the actual object the change is applied on, not on the `include` section where the parameter is originally specified.

## Available Protocols

Protocol modules in MaxScale define what kind of clients can connect to a listener and what type of backend servers are supported. Protocol is defined in listener settings, and affects both the listener and any services the listener is linked to.

### `MariaDB` or `MariaDBClient`

Implements MariaDB protocol. The listener will accept MariaDB/MySQL connections from clients and route the client queries through a linked MaxScale service to backend servers. The backends used by the service should be MariaDB servers or compatible.

### `CDC`

See [Change Data Capture Protocol](../../../../reference/maxscale-protocols/maxscale-change-data-capture-cdc-protocol.md) for more information.

### `nosqlprotocol`

Accepts MongoDB® connections, yet stores and fetches results to/from MariaDB servers. See [NoSQL documentation](../../../../reference/maxscale-protocols/maxscale-nosql-protocol-module/README.md) for more information.

## TLS/SSL encryption

This section describes TLS/SSL-related configuration parameters for both servers and listeners.

To enable TLS/SSL for a listener, set the `ssl` parameter to `allow` or
`require`. Listeners are SSL-enabled by default. If the clients expect a
specific certificate from MaxScale, set the `ssl_cert` and `ssl_key` parameters
for the listener. If a certificate is not defined, MaxScale will use an
auto-generated self-signed certificate. The generated certificate can pass
verification when used with a recent (11.4 or greater) client version.

To enable TLS/SSL-connections to a server, set its `ssl` parameter to `allow` or
`require`. If the backend database server has certificate verification enabled,
configure the `ssl_cert` and `ssl_key` parameters of the server. The database
server itself must also be configured to use TLS/SSL-connections if backend
connection encryption is enforced.

Custom CA certificates can be defined with the `ssl_ca` parameter. If `ssl_verify_peer_certificate` is enabled yet `ssl_ca` is not set, MaxScale will load CA certificates from the system default location.

If a listener is configured with `ssl=require`, the listener will reject any
unencrypted connections. To allow both encrypted and unencrypted connections to
the same listener, set `ssl` to `allow`. `allow` is the default mode.

Multiple listeners with different configurations can be created to enable
different encryption schemes.

If a server is configured with `ssl=require`, MaxScale enforces SSL usage for
all connections to the server. If an encrypted connection to the server cannot
be established, the connection fails.

Starting with MaxScale 2.5.20, if the TLS certificate given to MaxScale has the X509v3 extended key usage information, MaxScale will check it and refuse to use a certificate with the wrong usage. This means that a certificate with only clientAuth can only be used with servers and a certificate with only serverAuth can only be used with listeners. In order to use the same certificate for both listeners and servers, it must have both the clientAuth and serverAuth usages.

**From MaxScale 26.10,** listeners are SSL-enabled by default and can accept
both encrypted and unencrypted connections. In earlier versions they are not
SSL-enabled by default and cannot accept both.

### Settings for TLS/SSL Encryption

#### `ssl_ca_cert`

Deprecated since MariaDB MaxScale 22.08. See `ssl_ca`.

#### `ssl_ca`

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`
* Description: Specifies the CA certificate used to validate the peer’s certificate.

A string giving a file path that identifies an existing readable file. The file must be a Certificate Authority (CA) certificate. It will be used to verify that the peer certificate (sent by either client or a MariaDB Server) is valid. The CA certificate can consist of a certificate chain.

**NOTE** Up until MariaDB MaxScale 6, the parameter was called `ssl_ca_cert`, which is still accepted as an alias for `ssl_ca`.

#### `ssl_cert_verify_depth`

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `9`
* Description: Specifies the maximum depth of the CA chain during verification.

The maximum length of the certificate authority chain that will be accepted. The default value is 9, same as the OpenSSL default. The configured value must be larger than 0.

#### `ssl_cert`

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`
* Description: Deprecated - use [ssl\_ca](#ssl_ca) instead.

A string giving a file path that identifies an existing readable file. The file must be the SSL certificate MaxScale should use. The certificate must match the key defined in `ssl_key`. This is an optional parameter for listeners and servers.

#### `ssl_cipher`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`
* Description: Provides the list of TLS ciphers to use for SSL connections.

Set the list of TLS ciphers. By default, no explicit ciphers are defined and the system defaults are used. Note that this parameter does not modify TLSv1.3 ciphers.

#### `ssl_crl`

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`
* Description: Specifies the CRL file used to validate revoked SSL certificates.

A string giving a file path that identifies an existing readable file. The file must be a Certificate Revocation List in the PEM format that defines the revoked certificates. This parameter is only accepted by listeners.

**Example SSL enabled server configuration**

```
[server1]
type=server
address=10.131.24.62
port=3306
ssl=true
ssl_cert=/usr/local/mariadb/maxscale/ssl/crt.max-client.pem
ssl_key=/usr/local/mariadb/maxscale/ssl/key.max-client.pem
ssl_ca_cert=/usr/local/mariadb/maxscale/ssl/crt.ca.maxscale.pem
```

This example configuration requires all connections to this server to be encrypted with SSL. The paths to the certificate files and the Certificate Authority file are also provided.

**Example SSL enabled listener configuration**

```
[RW-Split-Listener]
type=listener
service=RW-Split-Router
port=3306
ssl=true
ssl_cert=/usr/local/mariadb/maxscale/ssl/crt.maxscale.pem
ssl_key=/usr/local/mariadb/maxscale/ssl/key.csr.maxscale.pem
ssl_ca_cert=/usr/local/mariadb/maxscale/ssl/crt.ca.maxscale.pem
```

This example configuration requires all connections to be encrypted with SSL. The paths to the certificate files and the Certificate Authority file are also provided.

#### `ssl_key`

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`
* Description: Specifies the path to the SSL/TLS private key that is used for secure connections.

A string giving a file path that identifies an existing readable file. The file must be the SSL certificate private key MaxScale should use. This is an optional parameter for listeners but an optional parameter for servers.

#### `ssl_passphrase`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`
* Description: Defines the passphrase used to decrypt the SSL/TLS private key.

If the private key specified using [ssl\_key](#ssl_key) requires a password, it should be provided with `ssl_passphrase`. The setting supports 3 different ways for providing the passphrase, indicated by the used prefix:

* `env:string`: The string is the name of an environment variable specifying the password.
* `file:string`: The string is the path of a file containing the password.
* `pass:string`: The string is the password.

In the case of `file`, the password is assumed to be the first read line, excluding a trailing line-feed. Any additional data is ignored. A failure to read the line will cause errors to be logged, but will not cause MaxScale to terminate.

It is an error, not to provide a prefix.

Examples:

```
ssl_passphrase=env:MY_SECRET_PASSWORD
ssl_passphrase=file:/path/to/pass.txt
ssl_passphrase=pass:MySecretPassword
```

#### `ssl_verify_peer_certificate`

* Type: [boolean](#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`
* Description: Verifies the peer's SSL/TLS certificate against a trusted CA.

Peer certificate verification. This functionality is disabled by default. In versions prior to 2.3.17 the feature was enabled by default.

When this feature is enabled, the peer (client or MariaDB Server) must send a certificate. The certificate sent by the peer is verified against the configured Certificate Authority to ensure the peer is who they claim to be. For listeners, this behaves as if `REQUIRE X509` was defined for all users.

If this feature is enabled for a server yet `ssl_ca` is not set, MaxScale will attempt to verify the backend server certificate after authentication as explained [here](https://mariadb.org/mission-impossible-zero-configuration-ssl/). This verification method is only supported with MariaDBAuth and Ed25519Auth and requires MariaDB Server version 11.4 or later.

#### `ssl_verify_peer_host`

* Type: [boolean](#booleans)
* Mandatory No
* Dynamic: Yes
* Default: `false`
* Description: Verifies the peer's hostname or IP address using its SSL/TLS certificate.

Peer host verification.

When this feature is enabled, the peer (client or MariaDB Server) hostname or IP is verified against the certificate sent by the peer. If the IP address or the hostname does not match the one in the certificate, the connection is closed.

If the peer does not provide a certificate, host verification is skipped. To require peer certificates, also enable `ssl_verify_peer_certificate`. For servers, the combination of

```
ssl_verify_peer_certificate=true
ssl_verify_peer_host=true
```

behaves like the `--ssl-verify-server-cert` command line option for the `mysql` client.

#### `ssl_version`

* Type: [enum\_mask](#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `MAX`, `TLSv1.0`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`, `TLSv10`, `TLSv11`, `TLSv12`, `TLSv13`
* Default: `MAX`
* Description: Lists the TLS protocol versions that are allowed for SSL/TLS connections.

This parameter controls the allowed TLS version. Accepted values are:

* `TLSv10`
* `TLSv11`
* `TLSv12`
* `TLSv13` (not supported on OpenSSL 1.0)
* `MAX`

MaxScale versions 6.4.16, 22.08.13, 23.02.10, 23.08.6, 24.02.2 and all newer releases accept also the following alias values:

* `TLSv1.0`
* `TLSv1.1`
* `TLSv1.2`
* `TLSv1.3` (not supported on OpenSSL 1.0)

The default setting (MAX) allows all supported versions. MaxScale supports TLSv1.0, TLSv1.1, TLSv1.2 and TLSv1.3 depending on the OpenSSL library version. TLSv1.0 and TLSv1.1 are considered deprecated and should not be used, so setting `ssl_version=TLSv1.2,TLSv1.3` or `ssl_version=TLSv1.3` is recommended.

In MaxScale versions 6.4.13, 22.08.11, 23.02.7, 23.08.3 and earlier, this setting defined the _only_ allowed TLS version, e.g. `ssl_version=TLSv12` would only enable TLSv12. The interpretation changed in MaxScale versions 6.4.14, 22.08.12, 23.02.8, 23.08.4 to enable the user to disable old versions while allowing multiple recent TLS versions. In these versions, `ssl_version=TLSv1.2` enabled both TLSv1.2 and TLSv1.3.

The interpretation changed again in MaxScale versions 6.4.16, 22.08.13, 23.02.10, 23.08.6, 24.02.2. In these versions the value of `ssl_version` is an enumeration of accepted TLS protocol versions. This means that `admin_ssl_version=TLSv1.2` again only allows TLSv1.2. To retain the behavior from the previous releases where the newer versions were automatically enabled, the protocol versions must be explicitly listed, for example `admin_ssl_version=TLSv1.2,TLSv1.3`. The change was done to make the `ssl_version` behave identically to how the MariaDB [tls\_version](../../../../../server/security/encryption/data-in-transit-encryption/ssltls-system-variables.md#tls_version) parameter works.

#### `ssl`

* Type: [enumeration](#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `disable`, `allow`, `require`
* Default: `allow`
* Description: Configures the SSL encryption for connections.

Enables SSL connections when set to `allow` or `require`. The old boolean values
can still be used and map to `require` (true) and `disable` (false).

In listener configuration, `allow` means that the listener accepts both
encrypted and unencrypted connections. `disable` only accepts unencrypted
connections and `require` only accepts encrypted connections.

In server configuration, `disable` only uses unencrypted connections to the
server. `require` only uses encrypted connections. `allow`-mode is flexible, and
means that MaxScale generally prefers to use encrypted connections but falls
back to unencrypted connections if the server does not support encryption. In
some cases (e.g. the
[Binlogrouter](../../../../reference/maxscale-routers/maxscale-binlogrouter.md))
`allow` may default to unencrypted connections. Use `allow` when encryption is
not essential, or when MariaDB Server SSL support may change while MaxScale is
running.

Starting with MaxScale 21.06.18, 22.08.15, 23.02.12, 23.08.8, 24.02.4 and
24.08.1, if SSL is disabled for a listener, MariaDB user accounts that require
SSL cannot log in through that listener. Any user account with a non-empty
_ssl\_type_-field in _mysql.user_-table is blocked. This includes users created
with `REQUIRE SSL` or `REQUIRE X509`.

**From MaxScale 26.10,** the value `allow` is available and is the default.
In earlier versions the setting is a boolean and the default is `false`.

## Module Types

### Routing Modules

The main task of MariaDB MaxScale is to accept database connections from client applications and route the connections or the statements sent over those connections to the various services supported by MariaDB MaxScale.

A number of routing modules are available, these are designed for a range of different needs.

Connection based load balancing:

* [ReadConnRoute](../../../../reference/maxscale-routers/maxscale-readconnroute.md)

Read/Write aware statement based router:

* [ReadWriteSplit](../../../../reference/maxscale-routers/maxscale-readwritesplit/README.md)

Simple sharding on database level:

* [SchemaRouter](../../../../reference/maxscale-routers/maxscale-schemarouter.md)

Binary log server:

* [Binlogrouter](../../../../reference/maxscale-routers/maxscale-binlogrouter.md)

### Monitor Modules

Monitor modules are used by MariaDB MaxScale to internally monitor the state of the backend databases in order to set the server flags for each of those servers. The router modules then use these flags to determine if the particular server is a suitable destination for routing connections for particular query classifications. The monitors are run within separate threads of MariaDB MaxScale and do not affect MariaDB MaxScale's routing performance.

* [MariaDB Monitor](../../../../reference/maxscale-monitors/mariadb-monitor/README.md)
* [Galera Monitor](../../../../reference/maxscale-monitors/galera-monitor.md)

The use of monitors in MaxScale is not absolutely mandatory: it is possible to run MariaDB MaxScale without a monitor module. In this case an external monitoring system must the status of each server via MaxCtrl or the REST API. **Only do this if you know what you are doing.**

### Filter Modules

```mermaid
flowchart LR
    accTitle: Client query flowing through the QLA and Regex filters to the backend server
    accDescr {
        The Client connects to a MaxScale router session. Inside the router
        session the query passes in order through the QLA filter and then the
        Regex filter before the router session forwards it to the backend
        server. The QLA filter also writes a copy of each query to the query
        log.
    }
    Client((Client)):::client -.-> QLA
    subgraph RS["Router session"]
        direction LR
        QLA["QLA"]:::proc
        Regex["Regex"]:::proc
        QLA -.-> Regex
    end
    Regex -.-> Backend[("Backend<br/>server")]:::node
    QLA -.-> QueryLog[["Query log"]]:::file

    classDef node fill:#e2f0f2,stroke:#0a5a6b,stroke-width:2px,color:#111;
    classDef proc fill:#fbe5d6,stroke:#c15911,stroke-width:2px,color:#111;
    classDef file fill:#eaf2fb,stroke:#2f5b8f,stroke-width:2px,color:#111;
    classDef client fill:#eeeeee,stroke:#333333,stroke-width:2px,color:#111;
```
_A client's query passes through the router session's QLA and Regex filters on its way to the backend server, with QLA also logging the query._

Filters provide a means to manipulate or process requests as they pass through MariaDB MaxScale between the client side protocol and the query router. A full explanation of each filter's functionality can be found in its documentation.

The [Filter Tutorial](../../../../mariadb-maxscale-tutorials/filters.md) document shows how you can add a filter to a service and combine multiple filters in one service.

* [Query Log All (QLA) Filter](../../../../reference/maxscale-filters/maxscale-query-log-all-filter.md)
* [Regular Expression Filter](../../../../reference/maxscale-filters/maxscale-regex-filter.md)
* [Tee Filter](../../../../reference/maxscale-filters/maxscale-tee-filter.md)
* [Top Filter](../../../../reference/maxscale-filters/maxscale-top-filter.md)
* [Query Redirection Filter](../../../../reference/maxscale-filters/maxscale-named-server-filter.md)

## Encrypting Passwords

Passwords stored in the maxscale.cnf file may optionally be encrypted for added security. This is done by creation of an encryption key on installation of MariaDB MaxScale. Encryption keys may be created manually by executing the maxkeys utility with the argument of the filename to store the key. The default location MariaDB MaxScale stores the keys is `/var/lib/maxscale`. The passwords are encrypted using 256-bit AES CBC encryption.

```
# Usage: maxkeys [PATH]
maxkeys /var/lib/maxscale/
```

Changing the encryption key for MariaDB MaxScale will invalidate any currently encrypted keys stored in the maxscale.cnf file.

**Note**: The password encryption format changed in MaxScale 2.5. All encrypted passwords created with MaxScale 2.4 or older need to be re-encrypted.

### Creating Encrypted Passwords

Encrypted passwords are created by executing the maxpasswd command with the location of the .secrets file and the password you require to encrypt as an argument.

```
# Usage: maxpasswd PATH PASSWORD
maxpasswd /var/lib/maxscale/ MaxScalePw001
61DD955512C39A4A8BC4BB1E5F116705
```

The output of the maxpasswd command is a hexadecimal string, this should be inserted into the maxscale.cnf file in place of the ordinary, plain text, password. MariaDB MaxScale will determine this as an encrypted password and automatically decrypt it before sending it the database server.

```
[Split-Service]
type=service
router=readwritesplit
servers=server1,server2,server3,server4
user=maxscale
password=61DD955512C39A4A8BC4BB1E5F116705
```

## Runtime Configuration Changes

The [MaxCtrl](../../../../reference/maxscale-maxctrl.md) and [REST-API](../../../../reference/maxscale-rest-api/maxscale-rest-api.md) documents provide information about making runtime changes.

All changes to the configuration done via MaxCtrl are persisted as individual configuration files in `/var/lib/maxscale/maxscale.cnf.d/`. The content of these files will override any configurations found in the main configuration file or any auxiliary configuration files.

Refer to the [Dynamic Configuration](#dynamic-configuration) section for more details on how this mechanism works and how to disable it.

### Configuration Synchronization

The configuration synchronization mechanism is intended for synchronizing configuration changes done on one MaxScale to all other MaxScales. This is done by propagating the changes via the database cluster used by Maxscale.

When configuring configuration synchronization for the first time, the same static configuration files should be used on all MaxScale instances that use the same cluster: the value of `config_sync_cluster` must be the same on all MaxScale instances and the cluster (i.e. the monitor) pointed by it and its servers must be the same in every configuration.

Whenever the MaxScale configuration is modified at runtime, the latest configuration is stored in the database cluster in the `mysql.maxscale_config` table. The table is created when the first modification to the configuration is done. A local copy of the configuration is stored in the data directory to allow MaxScale to function even if a connection to the cluster cannot be made. By default this file is stored at `/var/lib/maxscale/maxscale-config.json`.

Whenever MaxScale starts up, it checks if a local version of this configuration exists. If it does and it is a valid cached configuration, the static configuration file as well as any other generated configuration files are ignored. The exception is the `[maxscale]` section of the main static configuration file which is always read.

Each configuration has a version number with the initial configuration being version 0. Each time the configuration is modified, the version number is incremented. This version number is used to detect when MaxScale needs to update its configuration.

#### Error Handling in Configuration Synchronization

When doing a configuration change on the local MaxScale, if the configuration change completes on MaxScale but fails to be committed to the database, MaxScale will attempt to revert the local configuration change. If this attempt fails, MaxScale will discard the cached configuration and abort the process.

When synchronizing with the cluster, if MaxScale fails to apply a configuration retrieved from the cluster, it attempts to revert the configuration to the previous version. If successful, the failed configuration update is ignored. If the configuration update that fails cannot be reverted, the MaxScale configuration will be in an indeterminate state. When this happens, MaxScale will discard the cached configuration and abort the process.

When loading a locally cached configuration during startup, if any errors are found in the cached configuration, it is discarded and the MaxScale process will attempt to restart by exiting with code 75 from the main process. If MaxScale is being used as a SystemD service, this will automatically trigger a restart of MaxScale and no further actions are needed.

The most common reason for a failed configuration update is missing files. For example, if a configuration update adds encrypted connections to a server and the TLS certificates it uses were not copied over to all MaxScale nodes before the change was done, the operation will fail on all nodes that do not have these files.

If the synchronization of the configuration change fails at the step when the database transaction is being committed, the new configuration can be momentarily visible to the local MaxScale. This means the changes are not guaranteed to be atomic on the local MaxScale but are atomic from the cluster's point of view.

#### Synchronization of Encrypted Passwords

Starting with MaxScale 6.4.9, any passwords that are transmitted by the configuration synchronization are encrypted if password encryption has been enabled in MaxScale. This means that all MaxScale nodes in the same configuration cluster must be configured to use password encryption and they need to all use the same encryption keys that were created with `maxkeys`.

#### Managing Configuration Synchronization

The output of `maxctrl show maxscale` contains the `Config Sync` field with information about the current configuration state of the local Maxscale as well as the state of any other nodes using this cluster.

```
├──────────────┼─────────────────────────────────────────────────────────────┤
│ Config Sync  │ {                                                           │
│              │     "checksum": "3dd6b467760d1d2023f2bc3871a60dd903a3341e", │
│              │     "nodes": {                                              │
│              │         "maxscale": "OK",                                   │
│              │         "maxscale2": "OK"                                   │
│              │     },                                                      │
│              │     "origin": "maxscale",                                   │
│              │     "status": "OK",                                         │
│              │     "version": 2                                            │
│              │ }                                                           │
├──────────────┼─────────────────────────────────────────────────────────────┤
```

The `version` field is the logical configuration version and the `origin` is the node that originates the latest configuration change. The `checksum` field is the checksum of the logical configuration and can be used to compare whether two Maxscale instances are in the same configuration state. The `nodes` field contains the status of each MaxScale instance mapped to the hostname of the server. This field is updated whenever MaxScale reads the configuration from the cluster and can thus be used to detect which MaxScales have updated their configuration.

The `mysql.maxscale_config` table where the configuration changes are stored must not be modified manually. The only case when the table should be modified is when resetting the configuration synchronization.

To reset the configuration synchronization:

1. Stop all MaxScale instances
2. Remove the cached configuration file stored at `/var/lib/maxscale/maxscale-config.json` on all MaxScale instances
3. Drop the `mysql.maxscale_config` table
4. Start all MaxScale instances

To disable configuration synchronization, remove `config_sync_cluster` from the configuration file or set it to an empty string: `config_sync_cluster=""`. This can be done at runtime with MaxCtrl by passing an empty string to `config_sync_cluster`:

```
maxctrl alter maxscale config_sync_cluster ""
```

If MaxScale cannot create a connection to the database cluster, configuration changes are not possible until communication with the database is possible. To override this behavior and force the changes to be done, use the `--skip-sync` option for maxctrl or the `sync=false` HTTP parameter for the REST API. Any updates done with `--skip-sync` will overwritten by changes coming from the cluster.

#### Limitations in Configuration Synchronization

Only the MaxScale configuration is synchronized. Any external files (TLS certificates, configuration files for modules or data generated by MaxScale) are not synchronized. For example, the rule files for the cache filter must be synchronized separately if the filter itself is modified.

Starting with MaxScale 22.08, the `Maintenance` and `Draining` states of servers and modifications to the administrative users will be synchronized. In older versions servers had to be put into maintenance mode and users had to be modified separately on each MaxScale.

* ([MXS-3619](https://jira.mariadb.org/browse/MXS-3619)) External files are not synchronized.
* ([MXS-4276](https://jira.mariadb.org/browse/MXS-4276)) The `--export-config` option will not export the cluster configuration and instead exports only the static configuration files. To start a new MaxScale based off of a clustered configuration, copy the static configuration files as well as the JSON configuration in `/var/lib/maxscale/maxscale-config.json` to the new MaxScale instance.

### Backing Up Configuration Changes

The combination of configuration files can be done either manually (e.g. `rsync`) or with the `maxscale --export-config=FILE` command line option. See `maxscale --help` for more information about how to use the `--export-config` flag.

For example, to export the current runtime configuration, run the following command.

```
maxscale --export-config=/tmp/maxscale.cnf.combined
```

This will create the `/tmp/maxscale.cnf.combined` file and write the current configuration into the it. This allows new MaxScale instances to be easily set up without requiring copying of all runtime configuration files. The user executing the command must be able to read all MaxScale configuration files as well as create and write the provided filename.

## Backing Up a MaxScale Installation

The section above covers the runtime configuration alone. To copy or back up a whole MaxScale
installation, include its static configuration and the data its modules keep on disk.

The main configuration file for MaxScale is in `/etc/maxscale.cnf` and additional user-created configuration files are in `/etc/maxscale.cnf.d/`. Objects created or modified at runtime are stored in `/var/lib/maxscale/maxscale.cnf.d/`. Some modules also store internal data in `/var/lib/maxscale/` named after the module or the configuration object.

The simplest way to back up the configuration and runtime data of a MaxScale installation is to create an archive from the following files and directories:

* `/etc/maxscale.cnf`
* `/etc/maxscale.cnf.d/`
* `/var/lib/maxscale/`

This can be done with the following command:

```bash
tar -caf maxscale-backup.tar.gz /etc/maxscale.cnf /etc/maxscale.cnf.d/ /var/lib/maxscale/
```

If MaxScale is configured to store data in custom locations, these should be included in the backup as well.

## Encryption Key Managers

The encryption key managers are how MaxScale retrieves symmetric encryption keys from a key management system. Some parts of MaxScale require the `key_manager` to be configured in order to work. The key manager that is used is selected with the [key\_manager](global-settings.md#key_manager) parameter and the key manager itself is configured by placing the parameters in the `[maxscale]` section.

The encryption key managers can be enabled at runtime using `maxctrl alter maxscale` but cannot be disabled once enabled. To disable the encryption key management, stop Maxscale, remove any persisted configuration files and remove `key_manager` as well as any key manager options from the static configuration files.

### File-based Key Manager

The encryption keys are stored in a text file stored on a local filesystem.

The file uses the same format as the MariaDB server [File Key Management Encryption Plugin](../../../../../server/security/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin.md): a file consisting of an encryption key ID number and the hex-encoded encryption key separated by a semicolon. Read [Creating the Key File](../../../../../server/security/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin.md#creating-the-key-file) for more details on how to create the file.

For example, to configure encryption for the `nosqlprotocol` shared credentials using the file-based encryption key:

1. Create the key file with `(echo -n '1;' ; openssl rand -hex 32) | cat > /var/lib/maxscale/encryption.key`
2. Give MaxScale read permissions on it with `chown maxscale:maxscale /var/lib/maxscale/encryption.key`
3. Configure MaxScale with the following:

```
[maxscale]
key_manager=file
file.keyfile=/var/lib/maxscale/encryption.key

[NoSQL-Listener]
type=listener
service=My-Service
protocol=nosqlprotocol
nosqlprotocol.authentication_key_id=1
nosqlprotocol.authentication_user=my_user
nosqlprotocol.authentication_password=my_password

# Add services, servers, monitors etc.
```

1. Start MaxScale

#### Limitations

* Key versioning is not supported

#### Settings for File-based Key Manager

**`file.keyfile`**

* Type: path
* Mandatory: Yes
* Dynamic: Yes
* Description: Path to file containing encryption keys.

Path to the file that contains the encryption keys. The user MaxScale runs as (almost always `maxscale`) must be able to read this file. Encryption keys are read from disk only during startup or when any global MaxScale parameter is modified at runtime.

### KMIP Key Manager

Encryption keys are read from a KMIP server.

The KMIP key manager has been verified to work with the PyKMIP server.

#### Limitations

* Key versioning is not supported
* Encryption keys are not cached locally: whenever MaxScale needs an encryption key, it retrieves it from the KMIP server.

#### Settings for KMIP Key Manager

**`kmip.host`**

* Type: string
* Mandatory: Yes
* Dynamic: Yes
* Description: Defines the host where the KMIP server is.

The host where the KMIP server is.

**`kmip.port`**

* Type: integer
* Mandatory: Yes
* Dynamic: Yes
* Description: Defines the port on which the KMIP server listens.

The port on which the KMIP server listens on.

**`kmip.cert`**

* Type: path
* Mandatory: Yes
* Dynamic: Yes
* Description: Client certificate for KMIP authentication.

The client public certificate used when connecting to the KMIP server.

**`kmip.key`**

* Type: path
* Mandatory: Yes
* Dynamic: Yes
* Description: Specifies the client private key used for connecting to the KMIP server.

The client private key used when connecting to the KMIP server.

**`kmip.ca`**

* Type: path
* Default: `""`
* Dynamic: Yes
* Description: CA ceritficate for KMIP server.

The CA certificate to use. By default the system default certificates are used.

### HashiCorp Vault Key Manager

Encryption keys are read from a local or remote Vault server using the secret engine included in the Vault. This key manager supports versioned keys. Only version 2 key-value stores are supported.

The encryption keys use the same format as the MariaDB [HashiCorp Vault Key Management Plugin](../../../../../server/security/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin.md) The key-value secret for each encryption key ID must contain the field `data` which must contain a hex-encoded string that is either 32, 48 or 64 characters long.

An easy way to generate a correct encryption key is to use the `vault` and `openssl` command line clients. The following command creates a 256-bit encryption key using `openssl` and stores it using the key ID `1`:

```
$ openssl rand -hex 32|vault kv put secret/1 data=-
== Secret Path ==
secret/data/1

======= Metadata =======
Key                Value
---                -----
created_time       2022-06-23T06:50:55.29063873Z
custom_metadata    <nil>
deletion_time      n/a
destroyed          false
version            1
```

#### Limitations

* Encryption keys are not cached locally: whenever MaxScale needs an encryption key, it retrieves it from the Vault server.

#### Settings for HashiCorp Vault Key Manager

**`vault.token`**

* Type: password
* Mandatory: Yes
* Dynamic: Yes
* Description: Provides the authentication token to access the Vault server.

The authentication token used to connect to the Vault server. This can be encrypted using `maxpasswd`, similar to how other passwords are encrypted.

**`vault.host`**

* Type: string
* Default: `localhost`
* Dynamic: Yes
* Description: Specifies the hostname of the Vault server.

The host where the Vault server is.

**`vault.port`**

* Type: integer
* Default: `8200`
* Dynamic: Yes
* Description: Defines the port on which the Vault server listens.

The port on which the Vault server listens on.

**`vault.ca`**

* Type: path
* Default: `""`
* Dynamic: Yes
* Description: Defines the CA certificate used for validating Vault server connections.

The CA certificate to use. By default the system default certificates are used.

**`vault.tls`**

* Type: [boolean](#booleans)
* Default: true
* Dynamic: Yes
* Description: Manages whether encrypted (HTTPS) or unencrypted (HTTP) connections are used when communicating with the Vault server.

Whether to use encrypted connections (i.e. HTTPS or HTTP) when communicating with the Vault server.

**`vault.mount`**

* Type: string
* Default: `secret`
* Dynamic: Yes
* Description: Provides the Key-Value mount path in Vault where secrets are stored.

The Key-Value mount where the secret is stored. By default the `secret` mount is used which is present by default in most Vault installations.

**`vault.timeout`**

* Type: [duration](#durations)
* Default: 30s
* Dynamic: Yes
* Description: Sets the timeout for requests and connections to the Vault server.

The connection and request timeout used with the Vault server.

## Threads

For routing, MaxScale uses asynchronous I/O and a fixed number of threads (aka _routing workers_), whose number up until 23.02 was fixed at startup. From 23.02 onwards the number of threads can be altered at runtime, which is convenient, for instance, if MaxScale is running in a container whose properties are changed during the lifetime of the container.

A thread can be in three different states:

* **Active**: The thread is routing client traffic and is listening for new connections.
* **Draining**: The thread is routing client traffic but is **not** listening for new connections.
* **Dormant**: The thread is not routing client traffic (all sessions have ended), and is not listening for new connections, and is waiting to be terminated.

All threads start as _Active_ and may become _Draining_ if the number of threads is reduced. A draining thread will eventually become _Dormant_, unless the number of threads is increased while the thread is still _Draining_.

Note that it is not possible to terminate a specific thread, but it is only possible to specify the _number_ of threads that MaxScale should use, and that the threads will be terminated from the end. This has implications if the number of threads is reduced by more than 1, as a _Dormant_ thread will not be terminated before it is the last thread.

In the following, MaxScale has been started with `threads=4`.

```
$ bin/maxctrl show threads
┌────────────────────────┬────────┬────────┬────────┬────────┬─────┐
│ Id                     │ 0      │ 1      │ 2      │ 3      │ All │
├────────────────────────┼────────┼────────┼────────┼────────┼─────┤
│ State                  │ Active │ Active │ Active │ Active │ N/A │
├────────────────────────┼────────┼────────┼────────┼────────┼─────┤
...
```

All threads are _Active_. If we now decrease the number of threads

```
$ bin/maxctrl alter maxscale threads=2
OK
$ bin/maxctrl show threads
┌────────────────────────┬────────┬────────┬──────────┬──────────┬─────────┐
│ Id                     │ 0      │ 1      │ 2        │ 3        │ All     │
├────────────────────────┼────────┼────────┼──────────┼──────────┼─────────┤
│ State                  │ Active │ Active │ Draining │ Draining │ N/A     │
├────────────────────────┼────────┼────────┼──────────┼──────────┼─────────┤
...
```

we will see that the threads 2 and 3 are now _Draining_. The reason is that threads 2 and 3 still handle client sessions. If some client sessions now end, the situation may become like

```
┌────────────────────────┬────────┬────────┬─────────┬──────────┬────────┐
│ Id                     │ 0      │ 1      │ 2       │ 3        │ All    │
├────────────────────────┼────────┼────────┼─────────┼──────────┼────────┤
│ State                  │ Active │ Active │ Dormant │ Draining │ N/A    │
├────────────────────────┼────────┼────────┼─────────┼──────────┼────────┤
...
```

That is, thread 2 is _Dormant_ and thread 3 is _Draining_. All client sessions that were handled by thread 2 have ended and the thread is ready to be terminated. However, as thread 3 is still _Draining_, thread 2 will not be terminated but stay _Dormant_.

If the sessions handled by thread 3 end, then it will become _Dormant_ at which point first thread 3 will be terminated and immediately after that thread 2.

```
$ bin/maxctrl show threads
┌────────────────────────┬────────┬────────┬──────┐
│ Id                     │ 0      │ 1      │ All  │
├────────────────────────┼────────┼────────┼──────┤
│ State                  │ Active │ Active │ N/A  │
├────────────────────────┼────────┼────────┼──────┤
...
```

If the situation is like

```
$ bin/maxctrl show threads
┌────────────────────────┬────────┬────────┬─────────┬──────────┬────────┐
│ Id                     │ 0      │ 1      │ 2       │ 3        │ All    │
├────────────────────────┼────────┼────────┼─────────┼──────────┼────────┤
│ State                  │ Active │ Active │ Dormant │ Draining │ N/A    │
├────────────────────────┼────────┼────────┼─────────┼──────────┼────────┤
...
```

that is, the number of threads was 4 but has been reduced to 2, and while thread 2 has become drained it stays as _Dormant_ since thread 3 is still _Draining_, it is possible to make thread 2 _Active_ again by increasing the number of threads to 3.

```
$ bin/maxctrl alter maxscale threads=3
OK
wikman@johan-P53s:maxscale $ bin/maxctrl show threads
┌────────────────────────┬────────┬────────┬────────┬──────────┬────────┐
│ Id                     │ 0      │ 1      │ 2      │ 3        │ All    │
├────────────────────────┼────────┼────────┼────────┼──────────┼────────┤
│ State                  │ Active │ Active │ Active │ Draining │ N/A    │
├────────────────────────┼────────┼────────┼────────┼──────────┼────────┤
...
```

Once the sessions of thread 3 ends, we will have

```
$ bin/maxctrl show threads
┌────────────────────────┬────────┬────────┬────────┬──────┐
│ Id                     │ 0      │ 1      │ 2      │ All  │
├────────────────────────┼────────┼────────┼────────┼──────┤
│ State                  │ Active │ Active │ Active │ N/A  │
├────────────────────────┼────────┼────────┼────────┼──────┤
...
```

## Error Reporting

MariaDB MaxScale is designed to be executed as a service, therefore all error reports, including configuration errors, are written to the MariaDB MaxScale error log file. By default, MariaDB MaxScale will log to a file in `/var/log/maxscale` and the system log.

## Limitations

The current limitations of MaxScale are listed in the [Limitations](../../../mariadb-maxscale-limitations-guide.md) document.

## Performance Optimization

* Tune `query_classifier_cache_size` to allow maximal use of the query classifier cache. Increase the value and/or system memory until the set of unique SQL patterns fits into memory. By default at most 15% of the system memory is used for this cache. To detect if the SQL statements fit into memory, monitor the `QC cache evictions` value in `maxctrl show threads` to see how many evictions take place. If it keeps increasing, increase the size of the query classifier cache. Using the query classifier cache with a CPU bound workload gives a roughly 20% improvement in performance compared to when it is turned off.
* A faster CPU with more CPU cores is better. This is true for most applications but especially for MaxScale as it is mostly limited by the speed of the CPU. Using `threads=auto` is recommended (the default starting with MaxScale 6).
* Network throughput between the client, MaxScale and the database nodes governs how much traffic can be handled. The client-to-MaxScale network is likely to be saturated first: having multiple MaxScales in front of the cluster is an easy way of solving this problem.
* Certain MaxScale modules store data on disk. A faster disk improves their performance but depending on the module, this might not be a big enough of a problem to worry about. Filters like the `qlafilter` that write information to disk for every SQL query can cause performance bottlenecks.

### MaxScale Diagnostics using MaxCtrl

From 22.08.2 onwards, `maxctrl show maxscale` shows a `System` object with information about the system MaxScale is running on. The fields are:

| Field                                   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| machine.cores\_physical                 | The number of physical CPU cores on the machine.                                                                                                                                                                                                                                                                                                                                                                                           |
| machine.cores\_available                | The number of CPU cores available to MaxScale. This number may be smaller than machine.cores\_physical, if CPU affinities are used and only a subset of the physical cores are available to MaxScale.                                                                                                                                                                                                                                      |
| machine.cores\_virtual                  | The number of virtual CPU cores available to MaxScale. This number may be a decimal and smaller than machine.cores\_available, if MaxScale is running in a container whose CPU quota and period has been restricted. Note that if MaxScale is not, or fails to detect it is running in a container, the value shown will be identical with machine.cores\_available.                                                                       |
| machine.memory\_physical                | The amount of physical memory on the machine.                                                                                                                                                                                                                                                                                                                                                                                              |
| machine.memory\_available               | The amount of memory available to MaxScale. This number may be smaller than machine.memory\_physical, if MaxScale is running in a container whose memory has been restricted. Note that if MaxScale is not, or fails to detect it is running in a container, the value shown will be identical with machine.memory\_physical. Note also that the amount is available to all processes running in the same container, not just to MaxScale. |
| maxscale.query\_classifier\_cache\_size | The maximum size of the MaxScale query classifier cache.                                                                                                                                                                                                                                                                                                                                                                                   |
| maxscale.threads                        | The number of routing threads used by MaxScale.                                                                                                                                                                                                                                                                                                                                                                                            |

In addition there is an `os` object that contains what the Linux command `uname` displays.

#### Configuration

**`threads`**

If `threads` has not been specified at all in the MaxScale configuration file, or if its value is `auto`, then MaxScale will use as many routing threads as there are physical cores on the machine. This is the right choice, if MaxScale is running on a dedicated machine or in a container that has not been restricted in any way.

However, if the number of cores available to MaxScale have been restricted or if MaxScale is running in a container whose CPU quota and period have been limited, then it will lead to MaxScale using more routing threads than what is appropriate in the environment where it is running.

If `machine.cores_virtual` is less than `machine.cores_physical`, then `threads` should be specified explicitly in the MaxScale configuration file and its value should be that of `machine.cores_virtual` rounded up to the nearest integer. If that value is `1` it may be beneficial to check whether `2` gives better performance.

**`query_classifier_cache_size`**

If `query_classifier_cache_size` has not been specified in the MaxScale configuration file, then MaxScale will use at most 15% of the amount of physical memory in the machine for the cache. This is a good starting point, if MaxScale is running on a dedicated machine or in a container that has not been restricted in any way. Note that the amount specifies how much memory the cache at maximum is allowed to use, not what would immediately be allocated for the cache.

However, if the amount of memory available to MaxScale has been restricted, which may be the case if MaxScale is running in a container, this may cause the cache to grow beyond what is available, which will lead to a crash or MaxScale being killed.

If the value of `machine.memory_available` is less than that of `machine.memory_physical`, then `query_classifier_cache_size` should be explicitly set to 15% of `maxscale.memory_available`. The value can be larger, but must not be a bigger share of `machine.memory_available` than what is reasonable.

#### Example

```
$ maxctrl show maxscale
...
├──────────────┼────────────────────────────────────────────────────────────────────────────┤
│ System       │ {                                                                          │
│              │     "machine": {                                                           │
│              │         "cores_available": 8,                                              │
│              │         "cores_physical": 8,                                               │
│              │         "cores_virtual": 4,                                                │
│              │         "memory_available": 20858544128,                                   │
│              │         "memory_physical": 41717088256                                     │
│              │     },                                                                     │
│              │     "maxscale": {                                                          │
│              │         "query_classifier_cache_size": 6257563238,                         │
│              │         "threads": 8                                                       │
│              │     },                                                                     │
│              │     "os": {                                                                │
│              │         "machine": "x86_64",                                               │
│              │         "nodename": "johan-P53s",                                          │
│              │         "release": "5.4.0-125-generic",                                    │
│              │         "sysname": "Linux",                                                │
│              │         "version": "#141~18.04.1-Ubuntu SMP Thu Aug 11 20:15:56 UTC 2022"  │
│              │     }                                                                      │
│              │ }                                                                          │
└──────────────┴────────────────────────────────────────────────────────────────────────────┘
```

As can be seen, `maxscale.threads` is larger than `machine.cores_virtual` and thus, `threads=4` should explicitly be specified in the MaxScale configuration file.

`maxscale.query_classifier_cache_size` is the default 15% of `machine.memory_physical` but as `machine.memory_available` is just half of that, something like `query_classifier_cache_size=3100000000` (\~15% of `machine.memory_available`) should be added to the configuration file.

```
[maxscale]
threads=4
query_classifier_cache_size=3100000000
...
```

## Troubleshooting

For a list of common problems and their solutions, read the [MaxScale Troubleshooting](../../../maxscale-troubleshooting.md) article on the MariaDB documentation.

### Systemd Watchdog

If MaxScale is running as a systemd service, the systemd Watchdog will be enabled by default. To configure it, change the `WatchdogSec` option in the Service section of the maxscale systemd configuration file located in `/lib/systemd/system/maxscale.service`:

```
WatchdogSec=30s
```

It is not recommended to use a watchdog timeout less than 30 seconds. When enabled MaxScale will check that all threads are running and notify systemd with a "keep-alive ping".

Systemd reference: [systemd.service.html](https://www.freedesktop.org/software/systemd/man/systemd.service.html)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
