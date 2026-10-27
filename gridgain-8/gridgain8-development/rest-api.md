---
description: >-
  Enable and configure the GridGain 8 REST API — the ignite-rest-http module, Jetty configuration, the Jetty 12 module for Java 17, and REST security.
---

# Using the REST API

To enable HTTP connectivity, make sure that the `ignite-rest-http` module is enabled.
If you use the binary distribution, copy the `ignite-rest-http` module from `IGNITE_HOME/libs/optional/` to the `IGNITE_HOME/libs` folder.
See [Enabling modules](project-setup.md#enabling-modules) for details.

{% hint style="info" %}
GridGain ships two REST-HTTP modules, and a node's classpath must contain **exactly one** of them:

- `ignite-rest-http` — the default module, built on Jetty 9.4.
- `ignite-rest-http-jetty-12` — an optional module built on Jetty 12 that requires Java 17 or later. It provides the same HTTP REST server. See [Jetty 12 REST Module (Java 17)](#jetty-12-rest-module-java-17).

Both modules define the same `GridJettyRestProtocol` class. If both are present in `IGNITE_HOME/libs`, two copies end up on the classpath and the node fails to start. Before you enable the Jetty 12 module, remove `ignite-rest-http` from `libs` if it is already there.
{% endhint %}

Explicit configuration is not required; the connector starts up automatically and listens on port `8080`. You can check if it works with curl:

```shell
curl 'http://localhost:8080/ignite?cmd=version'
```

Request parameters may be provided as either a part of URL or in a form data:

```shell
curl 'http://localhost:8080/ignite?cmd=put&cacheName=myCache' -X POST -H 'Content-Type: application/x-www-form-urlencoded' -d 'key=testKey&val=testValue'
```

## Configuration

You can change HTTP server parameters as follows:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration" id="ignite.cfg">
    <property name="connectorConfiguration">
        <bean class="org.apache.ignite.configuration.ConnectorConfiguration">
            <property name="jettyPath" value="jetty.xml"/>
        </bean>
    </property>
</bean>

```
{% endtab %}

{% tab title="Java(configuration)" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();
cfg.setConnectorConfiguration(new ConnectorConfiguration().setJettyPath("jetty.xml"));
```
{% endtab %}

{% tab title="Java_API" %}
```java
// This example loads configuration from a file.
// You can use a custom configuration following the instructions in jetty documentation at https://jetty.org/.
private static class JettyServerFactory implements Factory<Server> {

    private static final long serialVersionUID = 0L;

    @Override public Server create() {
        log.info(">>>>> Using custom Jetty server initialization.");

        URL cfgUrl = U.resolveIgniteUrl(JETTY_CFG_PATH);

        XmlConfiguration cfg;

        try {
            cfg = new XmlConfiguration(Resource.newResource(cfgUrl));
        }
        catch (FileNotFoundException e) {
            throw new IgniteSpiException("Failed to find configuration file: " + cfgUrl, e);
        }
        catch (SAXException e) {
            throw new IgniteSpiException("Failed to parse configuration file: " + cfgUrl, e);
        }
        catch (IOException e) {
            throw new IgniteSpiException("Failed to load configuration file: " + cfgUrl, e);
        }
        catch (Exception e) {
            throw new IgniteSpiException("Failed to start HTTP server with configuration file: " + cfgUrl, e);
        }

        try {
            return (Server)cfg.configure();
        }
        catch (Exception e) {
            throw new IgniteException("Failed to start Jetty HTTP server.", e);
        }
    }
}

public IgniteConfiguration createIgniteConfiguration() {
    IgniteConfiguration igniteConfig = new IgniteConfiguration();

    ConnectorConfiguration connectorConfig = new ConnectorConfiguration();
    connectorConfig.setJettyServerFactory(new JettyServerFactory());

    igniteConfig.setConnectorConfiguration(connectorConfig);

    return igniteConfig;
}
```
{% endtab %}

{% tab title="C#/.NET" %}
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

The following table describes the properties of `ConnectorConfiguration` that are related to the http server:

|Parameter Name|Description|Optional|Default Value|
|---|---|---|---|
|`setSecretKey(String)`|Defines secret key used for client authentication. When provided, client request must contain `HTTP header X-Signature` with the string "[1]:[2]", where [1] is timestamp in milliseconds and [2] is the Base64 encoded SHA1 hash of the secret key.|Yes|`null`|
|`setPortRange(int)`|Port range for Jetty server. If the port provided in Jetty configuration or `IGNITE_JETTY_PORT` system property is already in use, Ignite iteratively increments port by 1 and tries to bind once again until provided port range is exceeded.|Yes|`100`|
|`setJettyPath(String)`|Path to Jetty configuration file. Should be either absolute or relative to `IGNITE_HOME`. If the path is not set, GridGain starts a Jetty server with a simple HTTP connector. This connector uses `IGNITE_JETTY_HOST` and `IGNITE_JETTY_PORT` system properties as `host` and `port` respectively. If `IGNITE_JETTY_HOST` is not provided, `localhost` is used as default. If `IGNITE_JETTY_PORT` is not provided, port `8080` is used.|Yes|`null`|
|`setMessageInterceptor(ConnectorMessageInterceptor)`|The interceptor provides the ability to transform all objects exchanged via REST protocol. For example, if you use custom serialization on client you can write an interceptor to transform binary representations received from the client to Java objects and later access them from Java code directly.|Yes|`null`|

### Example Jetty XML Configuration

Path to this configuration should be set to `ConnectorConfiguration.setJettyPath(String)` as explained above.

```xml
<?xml version="1.0"?>
<!DOCTYPE Configure PUBLIC "-//Jetty//Configure//EN" "http://www.eclipse.org/jetty/configure.dtd">
<Configure id="Server" class="org.eclipse.jetty.server.Server">
    <Arg name="threadpool">
        <!-- Default queued blocking thread pool -->
        <New class="org.eclipse.jetty.util.thread.QueuedThreadPool">
            <Set name="minThreads">20</Set>
            <Set name="maxThreads">200</Set>
        </New>
    </Arg>
    <New id="httpCfg" class="org.eclipse.jetty.server.HttpConfiguration">
        <Set name="secureScheme">https</Set>
        <Set name="securePort">8443</Set>
        <Set name="sendServerVersion">true</Set>
        <Set name="sendDateHeader">true</Set>
    </New>
    <Call name="addConnector">
        <Arg>
            <New class="org.eclipse.jetty.server.ServerConnector">
                <Arg name="server"><Ref refid="Server"/></Arg>
                <Arg name="factories">
                    <Array type="org.eclipse.jetty.server.ConnectionFactory">
                        <Item>
                            <New class="org.eclipse.jetty.server.HttpConnectionFactory">
                                <Ref refid="httpCfg"/>
                            </New>
                        </Item>
                    </Array>
                </Arg>
                <Set name="host">
                  <SystemProperty name="IGNITE_JETTY_HOST" default="localhost"/>
                </Set>
                <Set name="port">
                  <SystemProperty name="IGNITE_JETTY_PORT" default="8080"/>
                </Set>
                <Set name="idleTimeout">30000</Set>
                <Set name="reuseAddress">true</Set>
            </New>
        </Arg>
    </Call>
    <Set name="handler">
        <New id="Handlers" class="org.eclipse.jetty.server.handler.HandlerCollection">
            <Set name="handlers">
                <Array type="org.eclipse.jetty.server.Handler">
                    <Item>
                        <New id="Contexts" class="org.eclipse.jetty.server.handler.ContextHandlerCollection"/>
                    </Item>
                </Array>
            </Set>
        </New>
    </Set>
    <Set name="stopAtShutdown">false</Set>
</Configure>
```

## Jetty 12 REST Module (Java 17)

`ignite-rest-http-jetty-12` is an optional module that provides the same HTTP REST server as the default `ignite-rest-http` module, but runs on Jetty 12 and requires Java 17 or later. Use it when your deployment runs on Java 17 or later and you want the REST connector on the Jetty 12 line.

To enable the module in a standalone node, move the `optional/ignite-rest-http-jetty-12` folder into the `IGNITE_HOME/libs` folder before you run the `ignite.{sh|bat}` script. See [Enabling modules](project-setup.md#enabling-modules) for details.

{% hint style="warning" %}
Enable exactly one of `ignite-rest-http` and `ignite-rest-http-jetty-12`. Both modules define the same `GridJettyRestProtocol` class, so having both in `libs` puts two copies on the classpath and the node fails to start. If `ignite-rest-http` is already in `libs`, remove it before enabling the Jetty 12 module.
{% endhint %}

The connector is configured the same way as the default module: the `ConnectorConfiguration` properties described in [Configuration](#configuration) — including `setJettyPath(String)` and `setJettyServerFactory(Factory)` — behave identically.

### Migrating a jetty.xml File to Jetty 12

A `jetty.xml` file written for the default Jetty 9.4 module does not load on Jetty 12. If you pass a custom configuration file with `setJettyPath(String)`, apply the following changes for the Jetty 12 module. The default module (`ignite-rest-http`) is unaffected — keep your existing file there.

- **Rename the server thread-pool argument.** The `Server` constructor parameter was renamed from `threadpool` (Jetty 9.4) to `threadPool` (Jetty 12). A named `<Arg name="threadpool">` no longer matches the constructor and makes the whole constructor unmatchable. Rename it, or drop the name to use a positional argument:

  ```xml
  <Arg name="threadPool">
      <New class="org.eclipse.jetty.util.thread.QueuedThreadPool"> ... </New>
  </Arg>
  ```

- **Remove the handler block.** `HandlerCollection` and `HandlerList` were removed in Jetty 12. GridGain installs its own REST handler after your file is applied, so any `<Set name="handler">...HandlerCollection...</Set>` block was already overridden and can be deleted.

The `<!DOCTYPE ...>` declaration needs no change: Jetty 12 maps the old Jetty 9 public and system identifiers to its current DTD.

### Configuring HTTPS on Jetty 12

On the Jetty 12 module, the SSL connector uses `org.eclipse.jetty.util.ssl.SslContextFactory$Server`. A minimal HTTPS connector looks as follows:

```xml
<New id="httpsCfg" class="org.eclipse.jetty.server.HttpConfiguration">
    <Call name="addCustomizer">
        <Arg><New class="org.eclipse.jetty.server.SecureRequestCustomizer"/></Arg>
    </Call>
</New>

<New id="sslContextFactory" class="org.eclipse.jetty.util.ssl.SslContextFactory$Server">
    <Set name="keyStorePath">/path/to/keystore.jks</Set>
    <Set name="keyStorePassword">yourPassword</Set>
    <!-- Mutual TLS: add a trust store and require client certificates.
    <Set name="trustStorePath">/path/to/truststore.jks</Set>
    <Set name="trustStorePassword">yourPassword</Set>
    <Set name="needClientAuth">true</Set>
    -->
</New>

<Call name="addConnector">
    <Arg>
        <New class="org.eclipse.jetty.server.ServerConnector">
            <Arg><Ref refid="Server"/></Arg>
            <Arg>
                <Array type="org.eclipse.jetty.server.ConnectionFactory">
                    <Item>
                        <New class="org.eclipse.jetty.server.SslConnectionFactory">
                            <Arg><Ref refid="sslContextFactory"/></Arg>
                            <Arg>http/1.1</Arg>
                        </New>
                    </Item>
                    <Item>
                        <New class="org.eclipse.jetty.server.HttpConnectionFactory">
                            <Arg><Ref refid="httpsCfg"/></Arg>
                        </New>
                    </Item>
                </Array>
            </Arg>
            <Set name="host"><SystemProperty name="IGNITE_JETTY_HOST" default="0.0.0.0"/></Set>
            <Set name="port"><SystemProperty name="IGNITE_JETTY_PORT" default="8443"/></Set>
        </New>
    </Arg>
</Call>
```

`SecureRequestCustomizer` enables SNI host checking by default. If the certificate's CN or SAN does not match the address the connector binds to, disable the check with `<Set name="sniHostCheck">false</Set>`.

## Security

{% hint style="info" %}
Refer to the [SSL Guide](https://www.gridgain.com/docs/tutorials/security/ssl-guide) for a comprehensive instruction on SSL.
{% endhint %}

When [authentication](../security/authentication.md) is configured in the cluster, all applications that use REST API request authentication by providing security credentials.
The authentication request returns a session token that can be used with any command within that session.

There are two ways to request authorization:

1. Use the authenticate command with `ignite.login=[user]&ignite.password=[password]` parameters.

   ```
   https://[host]:[port]/ignite?cmd=authenticate&ignite.login=[user]&ignite.password=[password]
   ```

2. Use any REST command with `ignite.login=[user]&ignite.password=[password]` parameters in the path of your connection string. In our example below, we use the `version` command:

   ```
   http://[host]:[port]/ignite?cmd=version&ignite.login=[user]&ignite.password=[password]
   ```

In both examples above, replace `[host]`, `[port]`, `[user]`, and `[password]` with actual values.

{% hint style="info" %}
REST authentication works on per-node basis. When working with multiple nodes in the same cluster, get the credentials for each node you need individually.
{% endhint %}

Executing any one of the above strings in a browser returns a response with a session token which looks like this:

```
{"successStatus":0,"error":null,"sessionToken":"EF6013FF590348CE91DEAE9870183BEF","response":true}
```

Once you obtain the session token, use the sessionToken parameter with your connection string as shown in the example below:

```
http://[host]:[port]/ignite?cmd=top&sessionToken=[sessionToken]
```

In the above connection string, replace `[host]`, `[port]`, and `[sessionToken]` with actual values.

{% hint style="warning" %}
Either user credentials or a session token is required when authentication is enabled on the server.
Failure to provide either a `sessionToken` or `user` & `password` parameters in the REST connection string results in an error:

```json
{
    "successStatus":2,
    "sessionToken":null,
    "error":"Failed to handle request - session token not found or invalid",
    "response":null
}
```
{% endhint %}

{% hint style="info" %}
**Session Token Expiration**

A session token is valid only for 30 seconds. Using an expired session token results in an error, like the one below:

```json
{
    "successStatus":1,
    "error":"Failed to handle request - unknown session token (maybe expired session) [sesTok=12FFFD4827D149068E9FFF59700E5FDA]",
    "sessionToken":null,
    "response":null
}
```

To set a custom expire time, set the system variable: `IGNITE_REST_SESSION_TIMEOUT` (in seconds).

```
-DIGNITE_REST_SESSION_TIMEOUT=3600
```
{% endhint %}
