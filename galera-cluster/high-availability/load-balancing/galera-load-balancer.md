---
hidden: true
---

# Galera Load Balancer (glbd)

{% hint style="danger" %}
The Galera Load Balancer (`glbd`) is no longer under active development.\
It is provided here for **historical and reference purposes only**.\
For new deployments, we recommend using a modern, fully supported proxy such as [MariaDB MaxScale](https://mariadb.com/products/enterprise/maxscale/).
{% endhint %}

Galera Load Balancer (`glbd`) is a simple, multi-threaded TCP connection balancer, optimized for database workloads.

It was inspired by **pen**, but unlike it, GLB focuses only on balancing **generic TCP connections**.

## Features

| Feature                     | Description                                                                                        |
| --------------------------- | -------------------------------------------------------------------------------------------------- |
| Server Draining             | Remove servers smoothly without interrupting active connections.                                   |
| High Performance            | Uses Linux `epoll` API (2.6+).                                                                     |
| Multithreading              | Leverages multi-core CPUs for better performance.                                                  |
| Optional Watchdog Module    | Monitors server health.                                                                            |
| Seamless Client Integration | Uses `libglb` for load balancing without changing applications, by intercepting `connect()` calls. |

## Installation

GLB must be built from source. There are no pre-built packages.

```bash
git clone https://github.com/codership/glb
cd glb/
./bootstrap.sh
./configure
make
sudo make install
```

This installs:

* `glbd` (daemon) → `/usr/sbin`
* `libglb` (shared library)

### Running as a Service

To run as a service:

```bash
# cp files/glbd.sh /etc/init.d/glb
# cp files/glbd.cfg /etc/sysconfig/glbd.cfg   # Red Hat / CentOS
# cp files/glbd.cfg /etc/default/glbd.cfg     # Debian / Ubuntu
```

Manage with:

```bash
service glb start|stop|restart|getinfo|getstats|add|remove|drain
```

## Configuration

GLB can be configured either via **command-line options** or via a configuration file.

#### Command-Line Options {#command-line-options}

```bash
glbd --help
```

### Configuration File (`glbd.cfg`)

| Parameter         | Description                                        |
| ----------------- | -------------------------------------------------- |
| `LISTEN_ADDR`     | Address/port GLB listens on for client connections |
| `DEFAULT_TARGETS` | Space-separated list of backend servers            |
| `OTHER_OPTIONS`   | Extra GLB options (e.g. balancing policy)          |

#### **Example**:

```ini
# Galera Load Balancer Configuration
LISTEN_ADDR="8010"
DEFAULT_TARGETS="192.168.1.1 192.168.1.2 192.168.1.3"
OTHER_OPTIONS="--random --top 3"
```

## Destination Selection Policies

GLB supports five policies:

| Policy                          | Description                                                                                                |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Least Connecte&#x64;_(default)_ | Routes new connections to the server with the fewest active connections (adjusted for weight).             |
| Round Robin                     | Sequentially cycles through available servers.                                                             |
| Single                          | Routes all connections to the highest-weight server until it fails or a higher-weight server is available. |
| Random                          | Distributes connections randomly among servers.                                                            |
| Source Tracking                 | Routes all connections from the same client IP to the same server (best-effort).                           |

**`-T | --top` option**: restricts balancing to servers with the highest weight.

## Runtime Management

GLB can be managed at runtime via:

* FIFO file
* Control socket (`-c <addr:port>`)

### Commands

| Command           | Example                                           | Description                                 |
| ----------------- | ------------------------------------------------- | ------------------------------------------- |
| Add/Modify server | `echo "192.168.0.1:3307:5" \| nc 127.0.0.1 4444`  | Add backend with weight 5                   |
| Drain server      | `echo "192.168.0.1:3307:0" \| nc 127.0.0.1 4444`  | Stop new connections, keep existing         |
| Delete server     | `echo "192.168.0.1:3307:-1" \| nc 127.0.0.1 4444` | Remove backend and close active connections |
| Get routing table | `echo "getinfo" \| nc 127.0.0.1 4444`             | Show backends, weight, usage, connections   |
| Get stats         | `echo "getstat" \| nc 127.0.0.1 4444`             | Show raw performance counters               |

## Performance Statistics

Example:

```bash
echo "getstat" | nc -q 1 127.0.0.1 4444
in: 6930 out: 102728 recv: 109658 / 45 send: 109658 / 45 conns: 0 / 4 poll: 45 / 0 / 45 elapsed: 1.03428
```

| Field         | Description                                    |
| ------------- | ---------------------------------------------- |
| `in / out`    | Bytes received/sent via client interface       |
| `recv / send` | Bytes passed and number of recv()/send() calls |
| `conns`       | Created / concurrent connections               |
| `poll`        | Read-ready / write-ready / total poll calls    |
| `elapsed`     | Time since last report (seconds)               |

## Watchdog

The watchdog module performs **asynchronous health checks** beyond simple TCP reachability.

Enable with:

```bash
glbd -w exec:"mysql.sh -utest -ptestpass" -t 2 3306 192.168.0.1 192.168.0.2
```

* Runs `mysql.sh` with `host:port` as first argument.
* Exit code `0` = healthy, non-zero = failure.
* Use `-i` to set check interval.
* With Galera, `-D|--discover` enables auto-discovery of nodes.

## libglb (Shared Library)

`libglb` enables transparent load balancing by intercepting the `connect()` system call.

### Basic Example

```bash
export LD_PRELOAD=/path/to/libglb.so
export GLB_OPTIONS="--random 3306 192.168.0.1 192.168.0.2 192.168.0.3"

mysql -uroot -p -h127.0.0.1 -P3306
```

### Environment Variables

| Variable       | Description                                     |
| -------------- | ----------------------------------------------- |
| `GLB_WATCHDOG` | Same as `--watchdog` option                     |
| `GLB_TARGETS`  | Comma-separated list of backends (`H:P:W`)      |
| `GLB_BIND`     | Local bind address for intercepted connections  |
| `GLB_POLICY`   | Balancing policy (`single`, `random`, `source`) |
| `GLB_CONTROL`  | Control socket for runtime commands             |

## Operational Limits

* Limited by system open files (`ulimit -n`)
* With default `1024` → \~493 connections
* With `4096` (typical unprivileged user) → \~2029 connections
* Adjust in `/etc/security/limits.conf` if needed

## See Also

* [MariaDB MaxScale](https://mariadb.com/products/enterprise/maxscale/) – recommended modern proxy
* [Codership GLB on GitHub](https://github.com/codership/glb)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
