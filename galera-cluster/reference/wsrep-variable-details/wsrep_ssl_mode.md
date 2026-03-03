# wsrep\_ssl\_mode

{% hint style="info" %}
This system variable is available from MariaDB 11.4 and 10.6.
{% endhint %}

Select which SSL implementation is used for wsrep provider communications: PROVIDER - wsrep provider internal SSL implementation; SERVER - use server side SSL implementation; SERVER\_X509 - as SERVER and require valid X509 certificate.

## Usage

The `wsrep_ssl_mode` system variable is used to configure the `WSREP` TLS Mode used by MariaDB Enterprise Cluster, powered by Galera.

When set to `SERVER` or `SERVER_X509`, MariaDB Enterprise Cluster uses the TLS configuration for MariaDB Enterprise Server:

```ini
[mariadb]
...
wsrep_ssl_mode = SERVER_X509

ssl_ca = /certs/ca-cert.pem
ssl_cert = /certs/server-cert.pem
ssl_key = /certs/server-key.pem
```

When set to `PROVIDER`, MariaDB Enterprise Cluster obtains its TLS configuration from the [wsrep\_provider\_options](../galera-cluster-system-variables.md#wsrep_provider_options) system variable:

```ini
[mariadb]
...
wsrep_ssl_mode = PROVIDER
wsrep_provider_options = "socket.ssl=true;socket.ssl_cert=/certs/server-cert.pem;socket.ssl_ca=/certs/ca-cert.pem;socket.ssl_key=/certs/server-key.pem"
```

## Details

The `wsrep_ssl_mode` system variable configures the `WSREP` TLS Mode. The following `WSREP` TLS Modes are supported:

| **WSREP TLS Mode** | **Values**                                 | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------ | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Provider           | <ul><li><code>PROVIDER</code></li></ul>    | <ul><li>TLS is optional for Enterprise Cluster replication traffic.</li><li>Each node obtains its TLS configuration from the <a href="../galera-cluster-system-variables.md#wsrep_provider_options">wsrep_provider_options</a> system variable. When the provider is not configured to use TLS on a node, the node will connect to the cluster without TLS.</li><li>The Provider WSREP TLS Mode is backward compatible with ES 10.5 and earlier. When performing a rolling upgrade from ES 10.5 and earlier, the Provider WSREP TLS Mode can be configured on the upgraded nodes.</li></ul> |
| Server             | <ul><li><code>SERVER</code></li></ul>      | <ul><li>TLS is mandatory for Enterprise Cluster replication traffic, but X509 certificate verification is not performed.</li><li>Each node obtains its TLS configuration from the node's MariaDB Enterprise Server configuration. When MariaDB Enterprise Server is not configured to use TLS on a node, the node will fail to connect to the cluster.</li><li>The Server WSREP TLS Mode is the default in ES 10.6.</li></ul>                                                                                                                                                               |
| Server X509        | <ul><li><code>SERVER_X509</code></li></ul> | <ul><li>TLS and X509 certificate verification are mandatory for Enterprise Cluster replication traffic.</li><li>Each node obtains its TLS configuration from the node's MariaDB Enterprise Server configuration. When MariaDB Enterprise Server is not configured to use TLS on a node, the node will fail to connect to the cluster.</li></ul>                                                                                                                                                                                                                                             |

When the `wsrep_ssl_mode` system variable is set to `PROVIDER`, each node obtains its TLS configuration from the [wsrep\_provider\_options](../galera-cluster-system-variables.md#wsrep_provider_options) system variable. The following options are used:

| **WSREP Provider Option**              | **Description**                                                  |
| -------------------------------------- | ---------------------------------------------------------------- |
| [socket.ssl](socket.ssl.md)            | Set this option to `true` to enable TLS.                         |
| [socket.ssl\_ca](socket.ssl_ca.md)     | Set this option to the path of the CA chain file.                |
| [socket.ssl\_cert](socket.ssl_cert.md) | Set this option to the path of the node's X509 certificate file. |
| [socket.ssl\_key](socket.ssl_key.md)   | Set this option to the path of the node's private key file.      |

When the `wsrep_ssl_mode` system variable is set to `SERVER` or `SERVER_X509`, each node obtains its TLS configuration from the node's MariaDB Enterprise Server configuration. The following system variables are used:

| **System Variable**          | **Description**                                                                                                                                                                                                                                                                                             |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ssl\_ca](ssl_ca.md)         | Set this system variables to the path of the CA chain file.                                                                                                                                                                                                                                                 |
| [ssl\_capath](ssl_capath.md) | Optionally set this system variables to the path of the CA chain directory. The directory must have been processed by `openssl rehash`. When your CA chain is stored in a single file, use the [ssl\_ca](https://docs-archive.mariadb.net/server/ref/mdb/system-variables/ssl_ca/) system variable instead. |
| [ssl\_cert](ssl_cert.md)     | Set this system variable to the path of the node's X509 certificate file.                                                                                                                                                                                                                                   |
| [ssl\_key](ssl_key.md)       | Set this system variable to the path of the node's private key file.                                                                                                                                                                                                                                        |

#### Parameters

| Command-line          | --wsrep\_ssl\_mode={PROVIDER\|SERVER\|SERVER\_X509} |
| --------------------- | --------------------------------------------------- |
| Configuration file    | Supported                                           |
| Dynamic               | No                                                  |
| Scope                 | Global                                              |
| Data Type             | ENUM (PROVIDER, SERVER, SERVER\_X509)               |
| Product Default Value | SERVER                                              |

<br>
