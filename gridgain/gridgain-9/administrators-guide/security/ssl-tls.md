---
description: >-
  Configure SSL/TLS encryption between GridGain 9 cluster nodes and the clients
  that connect to them, including keystores, truststores, and mutual TLS.
---

# SSL/TLS

This page explains how to configure SSL/TLS encryption between the cluster nodes (server and client) and the clients that connect to your cluster.

## Considerations

All internal connections in the cluster context, as well as cluster's user interaction interfaces, are SSL-enabled. The communication categories are as follows:

- Between the user and the cluster (node): REST
- Between the user and the platform clients
- Between nodes: Network (Messaging, Scalecube)

All SSL configurations activities are performed at the node level.

GridGain does not support direct paths to SSL certificates. Instead, it reads them from a keystore.
Set the `type` property of a keystore or truststore to `PKCS12` or `JKS`. The default is `PKCS12`.

### Keystores and Truststores

A **keystore** holds an identity: a certificate and the private key that belongs to it. A **truststore** holds the certificates of the other side that you are willing to trust.

- The server's keystore holds the server's own certificate and private key, which it uses to prove its identity to clients.
- The client's truststore lists the certificates the client accepts, so that it can verify the server's certificate.
- The client's keystore is only needed when the server requires client authentication. The client then proves its identity the same way the server does.
- The server's truststore is only needed in that same case, so that the server can verify the client's certificate.

For information on requiring client authentication, see [SSL Client Authentication (mTLS Support)](#ssl-client-authentication-mtls-support).

## REST

The standard implementation of SSL for REST involves configuring a secure connection on a separate port. GridGain supports HTTP and HTTPS, arch on its own port.

The GridGain 9 REST security configuration in the JSON format is provided below.

{% hint style="info" %}
In GridGain 9, you can create and maintain the configuration in either JSON or HOCON format.
{% endhint %}

```json
{
    "ignite" : {
        "rest" : {
            "dualProtocol" : false,
            "httpToHttpsRedirection" : false,
            "port" : 10300,
            "ssl" : {
                "ciphers" : "",
                "clientAuth" : "require",
                "enabled" : true,
                "keyStore" : {
                    "password" : "may be empty",
                    "path" : "must not be empty",
                    "type" : "PKCS12"
                },
                "port" : 10400,
                "trustStore" : {
                    "password" : "may be empty",
                    "path" : "must not be empty",
                    "type" : "PKCS12"
                }
            }
        }
    }
}
```

## Clients and JDBC

GridGain 9 Client implementation is based on the Netty framework, which supports configuration for security connections via `SSLContextBuilder`.

### Server-side Configuration

The default way to configure SSL on the server side is to update the configuration with SSL properties. The example below is in the JSON format.

{% hint style="info" %}
In GridGain 9, you can create and maintain the configuration in either JSON or HOCON format.
{% endhint %}

```json
{
    "ignite" : {
        "clientConnector" : {
            "ssl" : {
                "ciphers" : "",
                "clientAuth" : "require",
                "enabled" : true,
                "keyStore" : {
                    "type" : "PKCS12",
                    "path" : "must not be empty",
                    "password" : "may be empty"
                },
                "trustStore" : {
                    "type" : "PKCS12",
                    "path" : "must not be empty",
                    "password" : "may be empty"
                }
            }
        }
    }
}
```

If you have enabled SSL for `clientConnector`, and want to use JDBC, set the corresponding properties in your code:

```java
var url =
    "jdbc:ignite:thin://{address}:{port}"
        + "?sslEnabled=true"
        + "&trustStorePath=" + trustStorePath
        + "&trustStoreType=JKS"
        + "&trustStorePassword=" + password
        + "&clientAuth=require"
        + "&keyStorePath=" + keyStorePath
        + "&keyStoreType=PKCS12"
        + "&keyStorePassword=" + password;
        try (Connection conn = DriverManager.getConnection(url)) {
            // Other actions.
        }
```

## Client Configuration

## Java

To enable SSL in your Java clients, use the `IgniteClient` class and pass the ssl configuration to it:

```java
var sslConfiguration = SslConfiguration.builder()
                        .enabled(true)
                        .ciphers("TLS_AES_256_GCM_SHA384")
                        .trustStorePath(trustStorePath)
                        .trustStorePassword(password)
                        .keyStorePath(keyStorePath)
                        .keyStorePassword(password)
                        .build();

try (IgniteClient client = IgniteClient.builder()
    .addresses("localhost:10800")
    .ssl(sslConfiguration)
    .build();
)
```

### .NET

Add the `IgniteClientConfiguration.SslStreamFactory` property of type `ISslStreamFactory`.

Provide a [predefined implementation](https://github.com/apache/ignite/blob/66f43a4bee163aadb3ad731f6eb9a6dfde9faa73/modules/platforms/dotnet/Apache.Ignite.Core/Client/SslStreamFactory.cs).

Use the base class library `SslStream`.

Basic usage without client authorization:

```csharp
var cfg = new IgniteClientConfiguration { SslStreamFactory = new() }
```

## CLI

To point the CLI at an SSL-enabled REST endpoint, use the `cli config set` command:

```bash
cli config set ignite.cluster-endpoint-url=https://localhost:10400
cli config set ignite.rest.trust-store.path=<path>
cli config set ignite.rest.trust-store.password=<password>
```

If the cluster requires client authentication, also set `ignite.rest.key-store.path` and `ignite.rest.key-store.password`.
The `ignite.jdbc.trust-store.*` and `ignite.jdbc.key-store.*` parameters secure the JDBC connection that the CLI opens with the `connect` command.
The `ignite.jdbc.ssl-enabled`, `ignite.jdbc.client-auth` and `ignite.jdbc.ciphers` parameters apply to the same connection.
They do not apply to a JDBC URL you pass yourself.

For the full list of parameters, see [CLI Configuration Parameters](../config/cli-config.md#cli-configuration-parameters).

Store the CLI security configuration in a separate file with permission settings that protect it from unauthorized read/write operations. This configuration file must match profiles from the common configuration file.

## Network Configuration

The node network is based on the Netty framework. The configuration is the same as described for the GridGain Client part except for the part that addresses the GridGain 9 configuration.

{% hint style="info" %}
In GridGain 9, you can create and maintain the configuration in either JSON or HOCON format.
{% endhint %}

```json
{
    "ignite" : {
        "network" : {
            "ssl" : {
                "ciphers" : "",
                "enabled" : true,
                "keyStore" : {
                    "type" : "PKCS12",
                    "path" : "must not be empty",
                    "password" : "may be empty"
                },
                "trustStore" : {
                    "type" : "PKCS12",
                    "path" : "must not be empty",
                    "password" : "may be empty"
                }
            }
        }
    }
}
```

## SSL Client Authentication (mTLS Support)

Optionally, the connections you utilize can support the client authentication feature. Configure it separately for each connection on the server side.

Two-way authentication requires that both server and client have certificates they reciprocally trust. The client generates a private key, stores it in its keystore, and gets it signed by an entity the server's truststore trusts.

To support client authentication, a connection must include the `clientAuth`, `trustStore` and `keyStore` properties. Here is an example of a possible client configuration. The example below is in the JSON format.

{% hint style="info" %}
In GridGain 9, you can create and maintain the configuration in either JSON or HOCON format.
{% endhint %}

```json
{
    "ignite" : {
        "clientConnector" : {
            "ssl" : {
                "ciphers" : "",
                "clientAuth" : "require",
                "enabled" : true,
                "keyStore" : {
                    "type" : "PKCS12",
                    "path" : "must not be empty",
                    "password" : "may be empty"
                },
                "trustStore" : {
                    "type" : "JKS",
                    "path" : "must not be empty",
                    "password" : "may be empty"
                }
            }
        }
    }
}
```

## Example: Self-Signed Certificates for Development

The following walkthrough creates a self-signed certificate for `localhost`, puts it in a JKS keystore, and configures a node and the CLI to use it over the REST endpoint.
Client authentication is disabled, so only the server presents a certificate.

{% hint style="warning" %}
Self-signed certificates are for development and testing only. In production, use certificates issued by a certificate authority that your clients already trust.
{% endhint %}

First, issue a key and a self-signed certificate, then bundle them into a PKCS12 file and convert it to JKS:

```bash
# Issue a key and a self-signed certificate for localhost.
openssl req -x509 -newkey rsa:2048 \
  -keyout mykey.pem -out mycert.pem -days 365 -nodes \
  -subj "/CN=localhost/O=MyOrg/OU=Dev/C=GE" \
  -addext "subjectAltName=DNS:localhost,IP:127.0.0.1"

# Bundle the certificate and the key into PKCS12 format.
openssl pkcs12 -export \
  -in mycert.pem -inkey mykey.pem \
  -out mycert.p12 \
  -name myalias \
  -passout pass:changeit

# Convert PKCS12 to JKS.
keytool -importkeystore \
  -deststoretype JKS \
  -deststorepass changeit -destkeypass changeit \
  -destkeystore mykeystore.jks \
  -srckeystore mycert.p12 -srcstoretype PKCS12 \
  -srcstorepass changeit \
  -alias myalias
```

Next, create a truststore holding the same certificate, so that the CLI can verify the node:

```bash
keytool -importcert -noprompt -trustcacerts -storetype JKS \
  -file mycert.pem -alias myalias \
  -keystore truststore.jks -storepass changeit
```

Copy both files to a stable location, for example the configuration directory of a DEB or RPM installation.
ZIP installations keep their configuration under `$GRIDGAIN_HOME/etc` instead.
Writing to a system directory requires root privileges:

```bash
sudo cp mykeystore.jks truststore.jks /etc/gridgain9db/
```

Then enable SSL on the node's REST endpoint.
This is node configuration, so add it to the node configuration file of every node and restart the node for it to take effect.
The example below is in the HOCON format:

```javascript
ignite {
    network {
        nodeFinder {
            netClusterNodes=[
                "localhost:3344"
            ]
            type=STATIC
        }
        port=3344
    }
    rest {
        dualProtocol=false
        port=10300
        ssl {
            ciphers=""
            clientAuth=none
            enabled=true
            keyStore {
                password=changeit
                path="/etc/gridgain9db/mykeystore.jks"
                type=JKS
            }
            port=10400
        }
    }
}
```

Finally, point the CLI at the SSL port and give it the truststore:

```bash
cli config set ignite.cluster-endpoint-url=https://localhost:10400
cli config set ignite.rest.trust-store.path=/etc/gridgain9db/truststore.jks
cli config set ignite.rest.trust-store.password=changeit
```

## Troubleshooting SSL

Add the `-v` option to a CLI command to see what the CLI is doing.
Repeat the option to increase the detail of the reported REST calls: `-v` shows the request and the response, `-vv` adds the headers, and `-vvv` adds the body.

```bash
cluster status -v
```

The CLI also writes log files, which record the underlying SSL handshake errors.
By default they are in `~/.local/state/ignitecli/logs/`.
If the `XDG_STATE_HOME` environment variable is set, the CLI writes to `$XDG_STATE_HOME/ignitecli/logs/` instead.
The `IGNITE_CLI_LOGS_DIR` environment variable overrides both.
