# HandlerSocket Configuration Options

The [HandlerSocket](./) plugin has the following options.

See also the [Full list of MariaDB options, system and status variables](../../../full-list-of-mariadb-options-system-and-status-variables.md).

Add the options to the `[mysqld]` section of your `my.cnf` file.

#### `handlersocket_accept_balance`

* Description: When set to a value other than zero ('`0`'), `handlersocket` will try to balance accepted connections among threads. Default is `0` , but if you use persistent connections (for example if you use client-side connection pooling), a non-zero value is recommended.
* Command line: `--handlersocket-accept-balance="value"`
* Scope: Global
* Dynamic: No
* Type: number
* Range: `0` to `10000`
* Default Value: `0`

#### `handlersocket_address`

* Description: Specify the IP address to bind to.
* Command line: `--handlersocket-address="value"`
* Scope: Global
* Dynamic: No
* Type: IP Address
* Default Value: Empty, previously `0.0.0.0`

#### `handlersocket_backlog`

* Description: Specify the listen backlog length.
* Command line: `--handlersocket-backlog="value"`
* Scope: Global
* Dynamic: No
* Type: number
* Range: `5` to `1000000`
* Default Value: `32768`

#### `handlersocket_epoll`

* Description: Specify whether to use epoll for I/O multiplexing.
* Command line: `--handlersocket-epoll="value"`
* Scope: Global
* Dynamic: No
* Type: number
* Valid values:
  * Min: `0`
  * Max: `1`
* Default Value: `1`

#### `handlersocket_plain_secret`

* Description: When set, enables plain-text authentication for the listener for read requests, with the value of the option specifying the secret authentication key.
* Command line: `--handlersocket-plain-secret="value"`
* Dynamic: No
* Type: string
* Default Value: Empty

#### `handlersocket_plain_secret_wr`

* Description: When set, enables plain-text authentication for the listener for write requests, with the value of the option specifying the secret authentication key.
* Command line: `--handlersocket-plain-secret-wr="value"`
* Dynamic: No
* Type: string
* Default Value: Empty

#### `handlersocket_port`

* Description: Specify the port to bind to for reads. An empty value disables the listener.
* Command line: `--handlersocket-port="value"`
* Scope: Global
* Dynamic: No
* Type: number
* Default Value: Empty, previously `9998`

#### `handlersocket_port_wr`

* Description: Specify the port to bind to for writes. An empty value disables the listener.
* Command line: `--handlersocket-port-wr="value"`
* Scope: Global
* Dynamic: No
* Type: number
* Default Value: Empty, previously `9999`

#### `handlersocket_rcvbuf`

* Description: Specify the maximum socket receive buffer (in bytes). If '0' then the system default is used.
* Command line: `--handlersocket-rcvbuf="value"`
* Scope: Global
* Dynamic: No
* Type: number
* Range: `0` to `1677216`
* Default Value: `0`

#### `handlersocket_readsize`

* Description: Specify the minimum length of the request buffer. Larger values consume available memory but can make handlersocket faster for large requests.
* Command line: `--handlersocket-readsize="value"`
* Scope: Global
* Dynamic: No
* Type: number
* Range: `0` to `1677216`
* Default Value: `0` (possibly `4096`)

#### `handlersocket_sndbuf`

* Description: Specify the maximum socket send buffer (in bytes). If '0' then the system default is used.
* Command line: `--handlersocket-sndbuf="value"`
* Scope: Global
* Dynamic: No
* Type: number
* Range: `0` to `1677216`
* Default Value: `0`

#### `handlersocket_threads`

* Description: Specify the number of worker threads for reads. \
  Recommended value = number of CPU cores \* 2.
* Command line: `--handlersocket-threads="value"`
* Scope: Global
* Dynamic: No
* Type: number
* Range: `1` to `3000`
* Default Value: `16`

#### `handlersocket_threads_wr`

* Description: Specify the number of worker threads for writes. Recommended value = 1.
* Command line: `--handlersocket-threads-wr="value"`
* Scope: Global
* Dynamic: No
* Type: number
* Range: `1` to `3000`
* Default Value: `1`

#### `handlersocket_timeout`

* Description: Specify the socket timeout in seconds.
* Command line: `--handlersocket-timeout="value"`
* Scope: Global
* Dynamic: No
* Type: number
* Range: `30` to `3600`
* Default Value: `300`

#### `handlersocket_verbose`

* Description: Specify the logging verbosity.
* Command line: `--handlersocket-verbose="value"`
* Scope: Global
* Dynamic: No
* Type: number
* Valid values:
  * Min: `0`
  * Max: `10000`
* Default Value: `10`

#### `handlersocket_wrlock_timeout`

* Description: The write lock timeout in seconds. When acting on write requests, handlersocket locks an advisory lock named 'handlersocket\_wr' and this option sets the timeout for it.
* Command line: `--handlersocket-wrlock-timeout="value"`
* Scope: Global
* Dynamic: No
* Type: number
* Range: `0` to `3600`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
