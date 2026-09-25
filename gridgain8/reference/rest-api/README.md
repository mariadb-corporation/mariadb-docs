---
description: >-
  GridGain's HTTP REST API — how to enable and configure the connector, the
  supported data types, authentication, and the full command reference.
---

# REST API

GridGain provides an HTTP REST client that gives you the ability to communicate with the grid over HTTP and HTTPS protocols using the REST approach. REST APIs can be used to perform different operations like read/write from/to cache, execute tasks, get various metrics, and more.

Internally, GridGain uses Jetty to provide HTTP server features. See [Configuration](#configuration) section below for details on how to configure jetty.

## Getting Started

To enable HTTP connectivity, make sure that the `ignite-rest-http` module is enabled.
If you use the binary distribution, copy the `ignite-rest-http` module from `IGNITE_HOME/libs/optional/` to the `IGNITE_HOME/libs` folder.
See [Enabling modules](../../gridgain8-usage/setup.md#enabling-modules) for details.

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

### Configuration

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
    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <property name="ipFinder">
                <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                    <property name="addresses">
                        <list>
                            <!-- In distributed environment, replace with actual host IP address. -->
                            <value>127.0.0.1:47500..47509</value>
                        </list>
                    </property>
                </bean>
            </property>
        </bean>
    </property>
</bean>

    <property name="connectorConfiguration">
        <bean class="org.apache.ignite.configuration.ConnectorConfiguration">
            <property name="jettyPath" value="jetty.xml"/>
        </bean>
    </property>
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
|`setMessageInterceptor(ConnectorMessageInterceptor)`|The interceptor provides the ability to transform all objects exchanged via REST protocol. For example, if you use custom serialisation on client you can write an interceptor to transform binary representations received from the client to Java objects and later access them from Java code directly.|Yes|`null`|

#### Example Jetty XML Configuration

Path to this configuration should be set to `ConnectorConfiguration.setJettyPath(String)` as explained above.

```xml
```

### Jetty 12 REST Module (Java 17)

`ignite-rest-http-jetty-12` is an optional module that provides the same HTTP REST server as the default `ignite-rest-http` module, but runs on Jetty 12 and requires Java 17 or later. Use it when your deployment runs on Java 17 or later and you want the REST connector on the Jetty 12 line.

To enable the module in a standalone node, move the `optional/ignite-rest-http-jetty-12` folder into the `IGNITE_HOME/libs` folder before you run the `ignite.{sh|bat}` script. See [Enabling modules](../../gridgain8-usage/setup.md#enabling-modules) for details.

{% hint style="warning" %}
Enable exactly one of `ignite-rest-http` and `ignite-rest-http-jetty-12`. Both modules define the same `GridJettyRestProtocol` class, so having both in `libs` puts two copies on the classpath and the node fails to start. If `ignite-rest-http` is already in `libs`, remove it before enabling the Jetty 12 module.
{% endhint %}

The connector is configured the same way as the default module: the `ConnectorConfiguration` properties described in [Configuration](#configuration) — including `setJettyPath(String)` and `setJettyServerFactory(Factory)` — behave identically.

#### Migrating a jetty.xml File to Jetty 12

A `jetty.xml` file written for the default Jetty 9.4 module does not load on Jetty 12. If you pass a custom configuration file with `setJettyPath(String)`, apply the following changes for the Jetty 12 module. The default module (`ignite-rest-http`) is unaffected — keep your existing file there.

- **Rename the server thread-pool argument.** The `Server` constructor parameter was renamed from `threadpool` (Jetty 9.4) to `threadPool` (Jetty 12). A named `<Arg name="threadpool">` no longer matches the constructor and makes the whole constructor unmatchable. Rename it, or drop the name to use a positional argument:

  ```xml
  <Arg name="threadPool">
      <New class="org.eclipse.jetty.util.thread.QueuedThreadPool"> ... </New>
  </Arg>
  ```

- **Remove the handler block.** `HandlerCollection` and `HandlerList` were removed in Jetty 12. GridGain installs its own REST handler after your file is applied, so any `<Set name="handler">...HandlerCollection...</Set>` block was already overridden and can be deleted.

The `<!DOCTYPE ...>` declaration needs no change: Jetty 12 maps the old Jetty 9 public and system identifiers to its current DTD.

#### Configuring HTTPS on Jetty 12

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

### Security

{% hint style="info" %}
Refer to the [SSL Guide](https://www.gridgain.com/docs/tutorials/security/ssl-guide) for a comprehensive instruction on SSL.
{% endhint %}

When [authentication](../../security/authentication.md) is configured in the cluster, all applications that use REST API request authentication by providing security credentials.
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

## Data Types

The REST API also provides support for Java built-in types for put/get operations via `keyType` and `valueType` optional parameters.
Note that unless one of the below mentioned types are explicitly specified, the REST protocol exchanges the key-value data in `String` format.
This means that the data is stored and retrieved to/from the cluster as a `String`.

|REST KeyType/ValueType|Corresponding Java Type|
|---|---|
|`boolean`|`java.lang.Boolean`|
|`byte`|`java.lang.Byte`|
|`short`|`java.lang.Short`|
|`integer`|`java.lang.Integer`|
|`long`|`java.lang.Long`|
|`float`|`java.lang.Float`|
|`double`|`java.lang.Double`|
|`date`|`java.sql.Date`<br><br>The date value should be in the format as specified in the `valueOf(String)` method in the [Java documentation](https://docs.oracle.com/javase/8/docs/api/java/sql/Date.html#valueOf-java.lang.String-)<br><br>Example: 2018-01-01|
|`time`|`java.sql.Time`<br><br>The time value should be in the format as specified in the `valueOf(String)` method in the [Java documentation](https://docs.oracle.com/javase/8/docs/api/java/sql/Date.html#valueOf-java.lang.String-)<br><br>Example: 01:01:01|
|`timestamp`|`java.sql.Timestamp`<br><br>The timestamp value should be in the format as specified in the `valueOf(String)` method in the [Java documentation](https://docs.oracle.com/javase/8/docs/api/java/sql/Date.html#valueOf-java.lang.String-)<br><br>Example: 2018-02-18%2001:01:01|
|`uuid`|`java.util.UUID`|
|`IgniteUuid`|`org.apache.ignite.lang.IgniteUuid`|

The following example shows a `put` command with `keyType=int` and `valueType=date`:

```
http://[host]:[port]/ignite?cmd=put&key=1&val=2018-01-01&cacheName=myCache&keyType=int&valueType=date
```

Similarly, the `get` command with `keyType=int` and `valueType=date` would be:

```
http://[host]:[port]/ignite?cmd=get&key=1&cacheName=myCache&keyType=int&valueType=date
```

## Custom Data Types

The GridGain REST API does not recognize custom data types out-of-the-box. However, you can handle custom data types with the use of `ConnectorMessageInterceptor` - a function that intercepts an API call with a custom data type, converts it to a user's class. After that, GridGain can work with an instance of that class as with any other object.

For example:

```java
IgniteConfiguration igniteConfiguration = new IgniteConfiguration();

ConnectorConfiguration connectorConfiguration = new ConnectorConfiguration();

connectorConfiguration.setMessageInterceptor(new ConnectorMessageInterceptor() {
    @Override
    public Object onReceive(Object obj) {
        if (obj instanceof String) {
            // Converting the JSON representation to a user-defined object using the Jackson library.
            return JSON_MAPPER.readValue((String) obj, CustomObject.class);
        }

        return obj;
    }

    @Override
    public Object onSend(Object obj) {
        if (obj instanceof CustomObject) {
            return JSON_MAPPER.writeValueAsString(obj);
        }

        return obj;
    }
});
```

## Binary Objects in Query Results

By default, query commands deserialize cache entries into their Java classes on the server node. If a class is missing from the server classpath, the query fails. Use the `keepBinary=true` parameter to keep entries in binary form. GridGain serializes each binary object to JSON directly from its type metadata. The server never loads the class.

The parameter is supported by [SQL Query Execute](#sql-query-execute), [SQL Fields Query Execute](#sql-fields-query-execute), and [SQL Scan Query Execute](#sql-scan-query-execute). The setting applies to the whole query, so later pages fetched with [SQL Query Fetch](#sql-query-fetch) stay in binary form.

A binary object is rendered as a flat JSON object with one property per field. Field order follows the type metadata. Nested binary objects are rendered the same way.

The output matches what the same query returns without `keepBinary`. In a fields query, a binary value appears as a JSON object in its column position.

## Returned Value

The HTTP REST request returns a JSON object which has a similar structure for each command:

|Field|Type|Description|Example|
|---|---|---|---|
|`affinityNodeId`|`string`|Affinity node ID.|`2bd7b049-3fa0-4c44-9a6d-b5c7a597ce37`|
|`error`|`string`|This field contains description of error if server could not handle the request.|Specifically for each command.|
|`sessionToken`|`string`|When authentication is enabled on the server, this field contains a session token that can be used with any command within that session. If authentication is off, this field contains `null`. When authentication is enabled - `EF6013FF590348CE91DEAE9870183BEF`|Otherwise, `null`.|
|`response`|`jsonObject`|This field contains the result of the command.|Specifically for each command.|
|`successStatus`|`integer`|Exit status code. It might have the following values:<br><br>`success = 0`<br><br>`failed = 1`<br><br>`authorization failed = 2`<br><br>`security check failed = 3`|`0`|

## REST API Reference

### Version

Returns the GridGain version.

**Request:**

```shell
http://host:port/ignite?cmd=version
```

**Response:**

```json
{
  "error": "",
  "response": "1.0.0",
  "successStatus": 0
}
```

### Activate

Activates the cluster.

**Request:**

```shell
http://host:port/ignite?cmd=activate
```

**Response:**

```json
{
  "successStatus":0,
  "error":null,
  "sessionToken":null,
  "response":"activate started"
}
```

### Deactivate

Starts the deactivation process for a persistence-enabled cluster.

{% include "../../.gitbook/includes/gg8-note-on-deactivation.md" %}

**Request:**

```shell
http://host:port/ignite?cmd=deactivate
```

**Response:**

```json
{
  "successStatus":0,
  "error":null,
  "sessionToken":null,
  "response":"deactivate started"
}
```

### Current State

Returns the current state (active/inactive) of the cluster.

**Request:**

```shell
http://host:port/ignite?cmd=currentstate
```

**Response:**

Returns `true` if the cluster is active. Returns `false` if the cluster in inactive.

```json
{
  "successStatus":0,
  "error":null,
  "sessionToken":null,
  "response":true
}
```

### Increment

Adds and gets current value of given atomic long.

**Request:**

```shell
http://host:port/ignite?cmd=incr&key={incrKey}&init={initialValue}&delta={delta}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`key`|string||The name of atomic long.|counter|
|`init`|long|Yes|Initial value.|15|
|`delta`|long||Number to be added.|42|

**Response:**

The response contains the value after the operation.

```json
{
  "affinityNodeId": "e05839d5-6648-43e7-a23b-78d7db9390d5",
  "error": "",
  "response": 42,
  "successStatus": 0
}
```

### Decrement

Subtracts and gets current value of given atomic long.

**Request:**

```shell
http://host:port/ignite?cmd=decr&key={key}&init={init_value}&delta={delta}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`key`|string||The name of atomic long.|counter|
|`init`|long|Yes|Initial value.|`15`|
|`delta`|long||Number to be subtracted.|`42`|

**Response:**

The response contains the value after the operation.

```json
{
  "affinityNodeId": "e05839d5-6648-43e7-a23b-78d7db9390d5",
  "error": "",
  "response": -42,
  "successStatus": 0
}
```

### Cache Metrics

Shows metrics for a cache.

**Request:**

```shell
http://host:port/ignite?cmd=cache&cacheName={cacheName}&destId={nodeId}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`cacheName`|string|Yes|Cache name.|partitionedCache|
|`destId`|string|Yes|Node ID for which the metrics are to be returned.|8daab5ea-af83-4d91-99b6-77ed2ca06647|

**Response:**

```json
{
  "affinityNodeId": "",
  "error": "",
  "response": {
    "hits": 0,
    "misses": 0,
    "reads": 0,
    "writes": 2
  },
  "successStatus": 0
}
```

|Field|Type|Description|Example|
|---|---|---|---|
|`response`|jsonObject|The JSON object contains cache metrics such as create time, count reads and etc.|`{ "createTime": 1415179251551, "hits": 0, "misses": 0, "readTime":1415179251551, "reads": 0,"writeTime": 1415179252198, "writes": 2 }`|

### Cache Size

Gets the number of all entries cached across all nodes.

**Request:**

```shell
http://host:port/ignite?cmd=size&cacheName={cacheName}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`cacheName`|string|Yes|Cache name.|partitionedCache|

**Response:**

```json
{
  "affinityNodeId": "",
  "error": "",
  "response": 1,
  "successStatus": 0
}
```

|Field|Type|Description|Example|
|---|---|---|---|
|`response`|number|Number of all entries cached across all nodes.|5|

### Cache Metadata

Gets metadata for a cache.

**Request:**

```shell
http://host:port/ignite?cmd=metadata&cacheName={cacheName}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`cacheName`|String|Yes|Cache name.|partitionedCache|

**Response:**

```json
{
  "error": "",
  "response": {
    "cacheName": "partitionedCache",
    "types": [
      "Person"
    ],
    "keyClasses": {
      "Person": "java.lang.Integer"
    },
    "valClasses": {
      "Person": "org.apache.ignite.Person"
    },
    "fields": {
      "Person": {
        "_KEY": "java.lang.Integer",
        "_VAL": "org.apache.ignite.Person",
        "ID": "java.lang.Integer",
        "FIRSTNAME": "java.lang.String",
        "LASTNAME": "java.lang.String",
        "SALARY": "double"
      }
    },
    "indexes": {
      "Person": [
        {
          "name": "ID_IDX",
          "fields": [
            "id"
          ],
          "descendings": [],
          "unique": false
        },
        {
          "name": "SALARY_IDX",
          "fields": [
            "salary"
          ],
          "descendings": [],
          "unique": false
        }
      ]
    }
  },
  "sessionToken": "",
  "successStatus": 0
}
```

### Compare-And-Swap

Stores a given key-value pair in a cache only if the previous value is equal to the expected value passed in.

**Request:**

```shell
https://[host]:[port]/ignite?cmd=authenticate&ignite.login=[user]&ignite.password=[password]
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`cacheName`|string|Yes|Cache name.|partitionedCache|
|`key`|string||Key to store in cache.|name|
|`val`|string||Value associated with the given key.|Jack|
|`val2`|string||Expected value.|Bob|
|`destId`|string|Yes|Node ID for which the metrics are to be returned.|8daab5ea-af83-4d91-99b6-77ed2ca06647|

**Response:**

The response returns `true` if the value was replaced, `false` otherwise.

```json
{
  "affinityNodeId": "1bcbac4b-3517-43ee-98d0-874b103ecf30",
  "error": "",
  "response": true,
  "successStatus": 0
}
```

### Append

Appends a line for value which is associated with key.

**Request:**

```shell
http://host:port/ignite?cmd=append&key={appendKey}&val={_suffix}&cacheName={cacheName}&destId={nodeId}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`cacheName`|string|Yes|Cache name.|partitionedCache|
|`key`|string||Key to store in cache.|name|
|`val`|string||Value to be appended to the current value.|Jack|
|`destId`|string|Yes|Node ID for which the metrics are to be returned.|8daab5ea-af83-4d91-99b6-77ed2ca06647|

**Response:**

```json
{
  "affinityNodeId": "1bcbac4b-3517-43ee-98d0-874b103ecf30",
  "error": "",
  "response": true,
  "successStatus": 0
}
```

|Field|Type|Description|Example|
|---|---|---|---|
|`response`|boolean|`true` if replace happened, `false` otherwise.|true|

### Prepend

Adds prefix to the value that is associated with a given key.

**Request:**

```shell
http://host:port/ignite?cmd=prepend&key={key}&val={value}&cacheName={cacheName}&destId={nodeId}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`cacheName`|string|Yes|Cache name.|myCache|
|`key`|string||Key to store in cache.|name|
|`val`|string||The string to be prepended to the current value.|Name_|
|`destId`|string|Yes|Node ID for which the metrics are to be returned.|8daab5ea-af83-4d91-99b6-77ed2ca06647|

**Response:**

```json
{
  "affinityNodeId": "1bcbac4b-3517-43ee-98d0-874b103ecf30",
  "error": "",
  "response": true,
  "successStatus": 0
}
```

|Field|Type|Description|Example|
|---|---|---|---|
|`response`|boolean|`true` if replace happened, `false` otherwise.|true|

### Replace

Stores a given key-value pair in a cache if the cache already contains the key.

**Request:**

```shell
http://host:port/ignite?cmd=rep&key=repKey&val=newValue&cacheName={cacheName}&destId={nodeId}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`cacheName`|string|Yes|Cache name.|partitionedCache|
|`key`|string||Key to store in cache.|name|
|`val`|string||Value associated with the given key.|Jack|
|`destId`|string|Yes|Node ID for which the metrics are to be returned.|8daab5ea-af83-4d91-99b6-77ed2ca06647|
|`exp`|long|Yes|Expiration time in milliseconds for the entry. When the parameter is set, the operation is executed with [ModifiedExpiryPolicy](../../gridgain8-usage/configuring-caches/expiry-policies.md).|60000|

**Response:**

The response contains `true` if the value was replaced, `false` otherwise.

```json
{
  "affinityNodeId": "1bcbac4b-3517-43ee-98d0-874b103ecf30",
  "error": "",
  "response": true,
  "successStatus": 0
}
```

### Get

Retrieves the value mapped to a specified key from a cache.

**Request:**

```shell
http://host:port/ignite?cmd=get&key={getKey}&cacheName={cacheName}&destId={nodeId}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`cacheName`|string|Yes|Cache name.|partitionedCache|
|`key`|string||Key whose associated value is to be returned.|testKey|
|`keyType`|Java built-in type|Yes|See [Data Types](#data-types) for more details.||
|`destId`|string|Yes|Node ID for which the metrics are to be returned.|8daab5ea-af83-4d91-99b6-77ed2ca06647|

### Get All

Retrieves values mapped to the specified keys from a given cache.

**Request:**

```shell
http://host:port/ignite?cmd=getall&k1={getKey1}&k2={getKey2}&k3={getKey3}&cacheName={cacheName}&destId={nodeId}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`cacheName`|string|Yes|Cache name.|partitionedCache|
|`k1...kN`|string||Keys whose associated values are to be returned.|key1, key2, ..., keyN|
|`destId`|string|Yes|Node ID for which the metrics are to be returned.|8daab5ea-af83-4d91-99b6-77ed2ca06647|

**Response:**

```json
{
  "affinityNodeId": "",
  "error": "",
  "response": {
    "key1": "value1",
    "key2": "value2"
  },
  "successStatus": 0
}
```

{% hint style="info" %}
**Get output as array**

To obtain the output as an array, use the `IGNITE_REST_GETALL_AS_ARRAY=true` system property.
Once the property is set, the `getall` command provides the response in the following format:

`{“successStatus”:0,“affinityNodeId”:null,“error”:null,“sessionToken”:null,“response”:[{“key”:“key1”,“value”:“value1”},{“key”:“key2”,“value”:“value2”}]}`
{% endhint %}

### Get and Remove

Removes the given key mapping from cache and returns the previous value.

**Request:**

```shell
http://host:port/ignite?cmd=getrmv&cacheName={cacheName}&destId={nodeId}&key={key}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`cacheName`|string|Yes|Cache name.|partitionedCache|
|`key`|string||Key whose mapping is to be removed from the cache.|name|
|`destId`|string|Yes|Node ID for which the metrics are to be returned.|8daab5ea-af83-4d91-99b6-77ed2ca06647|

**Response:**

```json
{
  "affinityNodeId": "1bcbac4b-3517-43ee-98d0-874b103ecf30",
  "error": "",
  "response": value,
  "successStatus": 0
}
```

|Field|Type|Description|Example|
|---|---|---|---|
|`response`|jsonObject|Value for the key.|`{"name": "bob"}`|

### Get and Put

Stores a given key-value pair in a cache and returns the existing value if there is one.

**Request:**

```shell
http://host:port/ignite?cmd=getput&key=getKey&val=newVal&cacheName={cacheName}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`cacheName`|string|Yes|Cache name.|partitionedCache|
|`key`|string||Key to be associated with value.|name|
|`val`|string||Value to be associated with key.|Jack|
|`destId`|string|Yes|Node ID for which the metrics are to be returned.|8daab5ea-af83-4d91-99b6-77ed2ca06647|

**Response:**

The response contains the previous value for the key.

```json
{
  "affinityNodeId": "2bd7b049-3fa0-4c44-9a6d-b5c7a597ce37",
  "error": "",
  "response": {"name": "bob"},
  "successStatus": 0
}
```

### Get and Put If Absent

Stores given key-value pair in cache only if cache had no previous mapping for it. If cache previously contained value for the given key, then this value is returned.

**Request:**

```shell
http://host:port/ignite?cmd=getputifabs&key=getKey&val=newVal&cacheName={cacheName}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`cacheName`|string|Yes|Cache name.|partitionedCache|
|`key`|string||Key to be associated with value.|name|
|`val`|string||Value to be associated with key.|Jack|
|`destId`|string|Yes|Node ID for which the metrics are to be returned.|8daab5ea-af83-4d91-99b6-77ed2ca06647|

**Response:**

```json
{
  "affinityNodeId": "2bd7b049-3fa0-4c44-9a6d-b5c7a597ce37",
  "error": "",
  "response": "value",
  "successStatus": 0
}
```

|Field|Type|Description|Example|
|---|---|---|---|
|`response`|jsonObject|Previous value for the given key.|`{"name": "bob"}`|

### Get and Replace

Stores a given key-value pair in cache only if there is a previous mapping for it.

**Request:**

```shell
http://host:port/ignite?cmd=getrep&key={key}&val={val}&cacheName={cacheName}&destId={nodeId}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`cacheName`|string|Yes|Cache name.|partitionedCache|
|`key`|string||Key to store in cache.|name|
|`val`|string||Value associated with the given key.|Jack|
|`destId`|string|Yes|Node ID for which the metrics are to be returned.|8daab5ea-af83-4d91-99b6-77ed2ca06647|

**Response:**

The response contains the previous value associated with the specified key.

```json
{
  "affinityNodeId": "1bcbac4b-3517-43ee-98d0-874b103ecf30",
  "error": "",
  "response": oldValue,
  "successStatus": 0
}
```

|Field|Type|Description|Example|
|---|---|---|---|
|`response`|jsonObject|The previous value associated with the specified key.|`{"name": "Bob"}`|

### Replace Value

Replaces the entry for a key only if currently mapped to a given value.

**Request:**

```shell
http://host:port/ignite?cmd=repval&key={key}&val={newValue}&val2={oldVal}&cacheName={cacheName}&destId={nodeId}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`cacheName`|string|Yes|Cache name.|partitionedCache|
|`key`|string||Key to store in cache.|name|
|`val`|string||Value associated with the given key.|Jack|
|`val2`|string||Value expected to be associated with the specified key.|oldValue|
|`destId`|string|Yes|Node ID for which the metrics are to be returned.|8daab5ea-af83-4d91-99b6-77ed2ca06647|

**Response:**

```json
{
  "affinityNodeId": "1bcbac4b-3517-43ee-98d0-874b103ecf30",
  "error": "",
  "response": true,
  "successStatus": 0
}
```

|Field|Type|Description|Example|
|---|---|---|---|
|`response`|boolean|`true` if replace happened, `false` otherwise.|true|

### Remove

Removes the given key mapping from cache.

**Request:**

```shell
http://host:port/ignite?cmd=rmv&key={rmvKey}&cacheName={cacheName}&destId={nodeId}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`cacheName`|string|Yes|Cache name.|partitionedCache|
|`key`|string||Key - for which the mapping is to be removed from cache.|name|
|`destId`|string|Yes|Node ID for which the metrics are to be returned.|8daab5ea-af83-4d91-99b6-77ed2ca06647|

**Response:**

```json
{
  "affinityNodeId": "1bcbac4b-3517-43ee-98d0-874b103ecf30",
  "error": "",
  "response": true,
  "successStatus": 0
}
```

|Field|Type|Description|Example|
|---|---|---|---|
|`response`|boolean|`true` if replace happened, `false` otherwise.|true|

### Remove All

Removes given key mappings from a cache.

**Request:**

```shell
http://host:port/ignite?cmd=rmvall&k1={rmKey1}&k2={rmKey2}&k3={rmKey3}&cacheName={cacheName}&destId={nodeId}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`cacheName`|string|Yes|Cache name.|partitionedCache|
|`k1...kN`|string||Keys whose mappings are to be removed from  the cache.|name|
|`destId`|string|Yes|Node ID for which the metrics are to be returned.|8daab5ea-af83-4d91-99b6-77ed2ca06647|

**Response:**

```json
{
  "affinityNodeId": "1bcbac4b-3517-43ee-98d0-874b103ecf30",
  "error": "",
  "response": true,
  "successStatus": 0
}
```

|Field|Type|Description|Example|
|---|---|---|---|
|`response`|boolean|`true` if replace happened, `false` otherwise.|true|

### Remove Value

Removes the mapping for a key only if currently mapped to the given value.

**Request:**

```shell
http://host:port/ignite?cmd=rmvval&key={rmvKey}&val={rmvVal}&cacheName={cacheName}&destId={nodeId}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`cacheName`|string|Yes|Cache name.|partitionedCache|
|`key`|string||Key whose mapping is to be removed from the cache.|name|
|`val`|string||Value expected to be associated with the specified key.|oldValue|
|`destId`|string|Yes|Node ID for which the metrics are to be returned.|8daab5ea-af83-4d91-99b6-77ed2ca06647|

**Response:**

```json
{
  "affinityNodeId": "1bcbac4b-3517-43ee-98d0-874b103ecf30",
  "error": "",
  "response": true,
  "successStatus": 0
}
```

|Field|Type|Description|Example|
|---|---|---|---|
|`response`|boolean|`false` if there was no matching key.|true|

### Add

Stores a given key-value pair in a cache if the cache does not contain the key.

**Request:**

```shell
http://host:port/ignite?cmd=add&key=newKey&val=newValue&cacheName={cacheName}&destId={nodeId}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`cacheName`|string|Yes|Cache name.|partitionedCache|
|`key`|string||Key to be associated with the value.|name|
|`val`|string||Value to be associated with the key.|Jack|
|`destId`|string|Yes|Node ID for which the metrics are to be returned.|8daab5ea-af83-4d91-99b6-77ed2ca06647|
|`exp`|long|Yes|Expiration time in milliseconds for the entry. When the parameter is set, the operation is executed with [ModifiedExpiryPolicy](../../gridgain8-usage/configuring-caches/expiry-policies.md).|60000|

**Response:**

```json
{
  "affinityNodeId": "1bcbac4b-3517-43ee-98d0-874b103ecf30",
  "error": "",
  "response": true,
  "successStatus": 0
}
```

|Field|Type|Description|Example|
|---|---|---|---|
|`response`|boolean|`true` if value was stored in cache, `false` otherwise.|true|

### Put

Stores a given key-value pair in a cache.

**Request:**

```shell
http://host:port/ignite?cmd=put&key=newKey&val=newValue&cacheName={cacheName}&destId={nodeId}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`cacheName`|string|Yes|Cache name.|partitionedCache|
|`key`|string||Key to be associated with values.|name|
|`val`|string||Value to be associated with keys.|Jack|
|`destId`|string|Yes|Node ID for which the metrics are to be returned.|8daab5ea-af83-4d91-99b6-77ed2ca06647|
|`exp`|long|Yes|Expiration time in milliseconds for the entry. When the parameter is set, the operation is executed with [ModifiedExpiryPolicy](../../gridgain8-usage/configuring-caches/expiry-policies.md).|60000|

**Response:**

```json
{
  "affinityNodeId": "1bcbac4b-3517-43ee-98d0-874b103ecf30",
  "error": "",
  "response": true,
  "successStatus": 0
}
```

|Field|Type|Description|Example|
|---|---|---|---|
|`response`|boolean|`true` if value was stored in cache, `false` otherwise.|true|

### Put all

Stores the given key-value pairs in cache.

**Request:**

```shell
http://host:port/ignite?cmd=putall&k1={putKey1}&k2={putKey2}&k3={putKey3}&v1={value1}&v2={value2}&v3={value3}&cacheName={cacheName}&destId={nodeId}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`cacheName`|string|Yes|Cache name.|partitionedCache|
|`k1...kN`|string||Keys to be associated with values.|name|
|`v1...vN`|string||Values to be associated with keys.|Jack|
|`destId`|string|Yes|Node ID for which the metrics are to be returned.|8daab5ea-af83-4d91-99b6-77ed2ca06647|

**Response:**

```json
{
  "affinityNodeId": "1bcbac4b-3517-43ee-98d0-874b103ecf30",
  "error": "",
  "response": true,
  "successStatus": 0
}
```

|Field|Type|Description|Example|
|---|---|---|---|
|`response`|boolean|`true` if the values were stored in cache, `false` otherwise.|true|

### Put If Absent

Stores a given key-value pair in a cache if the cache does not contain the given key.

**Request:**

```shell
http://host:port/ignite?cmd=putifabs&key={getKey}&val={newVal}&cacheName={cacheName}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`cacheName`|string|Yes|Cache name.|partitionedCache|
|`key`|string||Key to be associated with value.|name|
|`val`|string||Value to be associated with key.|Jack|
|`destId`|string|Yes|Node ID for which the metrics are to be returned.|8daab5ea-af83-4d91-99b6-77ed2ca06647|
|`exp`|long|Yes|Expiration time in milliseconds for the entry. When the parameter is set, the operation is executed with [ModifiedExpiryPolicy](../../gridgain8-usage/configuring-caches/expiry-policies.md).|60000|

**Response:**

The response field contains `true` if the entry was put, `false` otherwise.

```json
{
  "affinityNodeId": "2bd7b049-3fa0-4c44-9a6d-b5c7a597ce37",
  "error": "",
  "response": true,
  "successStatus": 0
}
```

### Contains Key

Determines if cache contains an entry for the specified key.

**Request:**

```shell
http://host:port/ignite?cmd=conkey&key={getKey}&cacheName={cacheName}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`cacheName`|string|Yes|Cache name.|partitionedCache|
|`key`|string||Key whose presence in this cache is to be tested.|testKey|
|`destId`|string|Yes|Node ID for which the metrics are to be returned.|8daab5ea-af83-4d91-99b6-77ed2ca06647|

**Response:**

```json
{
  "affinityNodeId": "2bd7b049-3fa0-4c44-9a6d-b5c7a597ce37",
  "error": "",
  "response": true,
  "successStatus": 0
}
```

|Field|Type|Description|Example|
|---|---|---|---|
|`response`|boolean|`true` if this map contains a mapping for the specified key.|true|

### Contains keys

Determines if cache contains any entries for the specified keys.

**Request:**

```shell
http://host:port/ignite?cmd=conkeys&k1={getKey1}&k2={getKey2}&cacheName={cacheName}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`cacheName`|string|Yes|Cache name.|partitionedCache|
|`k1...kN`|string||Key whose presence in this cache is to be tested.|key1, key2, ..., keyN|
|`destId`|string|Yes|Node ID for which the metrics are to be returned.|`8daab5ea-af83-4d91-99b6-77ed2ca06647`|

**Response:**

```json
{
  "affinityNodeId": "2bd7b049-3fa0-4c44-9a6d-b5c7a597ce37",
  "error": "",
  "response": true,
  "successStatus": 0
}
```

|Field|Type|Description|Example|
|---|---|---|---|
|`response`|boolean|`true` if this cache contains a mapping for the specified keys.|true|

### Get or Create Cache

Creates a cache with the given name if it does not exist.

**Request:**

```shell
http://host:port/ignite?cmd=getorcreate&cacheName={cacheName}
```

|Parameter|Type|Optional|Description|
|---|---|---|---|
|`cacheName`|String|Yes|Cache name.|
|`backups`|int|Yes|Number of backups for cache data. Default is 0.|
|`dataRegion`|String|Yes|Name of the data region the cache should belong to.|
|`templateName`|String|Yes|Name of the cache template registered in Ignite to use as a configuration for the distributed cache. See the [Cache Template](../../gridgain8-usage/configuring-caches/configuration-overview.md#cache-templates) section for more information.|
|`cacheGroup`|String|Yes|Name of the group the cache should belong to.|
|`writeSynchronizationMode`|String|Yes|Sets the write synchronization mode for the given cache: `FULL_SYNC`, `FULL_ASYNC`, `PRIMARY_SYNC`|

**Response:**

```json
{
  "error": "",
  "response": null,
  "successStatus": 0
}
```

### Destroy cache

Destroys cache with given name.

**Request:**

```shell
http://host:port/ignite?cmd=destcache&cacheName={cacheName}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`cacheName`|string|Yes|Cache name.|partitionedCache|

**Response:**

```json
{
  "error": "",
  "response": null,
  "successStatus": 0
}
```

### Node

Gets information about a node.

**Request:**

```shell
http://host:port/ignite?cmd=node&attr={includeAttributes}&mtr={includeMetrics}&id={nodeId}&caches={includeCaches}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`mtr`|boolean|Yes|Response includes metrics if this parameter is `true`.|`true`|
|`attr`|boolean|Yes|Response includes attributes if this parameter is `true`.|`true`|
|`ip`|string||This parameter is optional if the `id` parameter is specified. Response is returned for node which has the given IP.|`192.168.0.1`|
|`id`|string||This parameter is optional if the `ip` parameter is specified. Response is returned for node which has the given node ID.|`8daab5ea-af83-4d91-99b6-77ed2ca06647`|
|`caches`|boolean|Yes|When set to `true` the cache information returned by node includes: name, mode, and SQL Schema.<br><br>When set to `false` the node command does not return any cache information.<br><br>Default value is `true`.|`true`|

**Response:**

```json
{
  "error": "",
  "response": {
    "attributes": null,
    "caches": {},
    "consistentId": "127.0.0.1:47500",
    "defaultCacheMode": "REPLICATED",
    "metrics": null,
    "nodeId": "2d0d6510-6fed-4fa3-b813-20f83ac4a1a9",
    "replicaCount": 128,
    "tcpAddresses": ["127.0.0.1"],
    "tcpHostNames": [""],
    "tcpPort": 11211
  },
  "successStatus": 0
}
```

### Log

Shows server logs.

**Request:**

```shell
http://host:port/ignite?cmd=log&from={from}&to={to}&path={pathToLogFile}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`from`|integer|Yes|Number of line to start from. Parameter is mandatory if to is passed.|`0`|
|`path`|string|Yes|The path to log file. If not provided the a default one is used.|`/log/cache_server.log`|
|`to`|integer|Yes|Number to line to finish on. Parameter is mandatory if from is passed.|`1000`|

**Response:**

```json
{
  "error": "",
  "response": ["[14:01:56,626][INFO ][test-runner][GridDiscoveryManager] Topology snapshot [ver=1, nodes=1, CPUs=8, heap=1.8GB]"],
  "successStatus": 0
}
```

### Topology

Gets the information about cluster topology.

**Request:**

```shell
http://host:port/ignite?cmd=top&attr=true&mtr=true&id=c981d2a1-878b-4c67-96f6-70f93a4cd241
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`mtr`|boolean|Yes|Response will include metrics, if this parameter is `true`.|true|
|`attr`|boolean|Yes|Response will include attributes, if this parameter is `true`.|true|
|`ip`|string|Yes|This parameter is optional, if the `id` parameter is passed. Response will be returned for node which has the IP.|192.168.0.1|
|`id`|string|Yes|This parameter is optional, if the `ip` parameter is passed. Response will be returned for node which has the node ID.|8daab5ea-af83-4d91-99b6-77ed2ca06647|
|`caches`|boolean|Yes|When set to `true` the cache information returned by top will include: `name`, `mode`, and `SQL Schema`.<br>When set to `false` the top command does not return any cache information.<br>Default value is `true`.|true|

**Response:**

```json
{
  "error": "",
  "response": [
    {
      "attributes": {
        ...
      },
      "caches": [
        {
          name: "",
          mode: "PARTITIONED"
        },
        {
          name: "partitionedCache",
          mode: "PARTITIONED",
          sqlSchema: "partitionedCache"
        }
      ],
      "consistentId": "127.0.0.1:47500",
      "metrics": {
        ...
      },
      "nodeId": "96baebd6-dedc-4a68-84fd-f804ee1ed995",
      "replicaCount": 128,
      "tcpAddresses": ["127.0.0.1"],
      "tcpHostNames": [""],
      "tcpPort": 11211
   },
   {
     "attributes": {
       ...
     },
		 "caches": [
       {
         name: "",
         mode: "REPLICATED"
       }
     ],
     "consistentId": "127.0.0.1:47501",
     "metrics": {
       ...
     },
     "nodeId": "2bd7b049-3fa0-4c44-9a6d-b5c7a597ce37",
     "replicaCount": 128,
     "tcpAddresses": ["127.0.0.1"],
     "tcpHostNames": [""],
     "tcpPort": 11212
   }
  ],
  "successStatus": 0
}
```

### Execute a Task

Executes a given task in the cluster.

**Request:**

```shell
http://host:port/ignite?cmd=exe&name=taskName&p1=param1&p2=param2&async=true
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`name`|string||Name of the task to execute.|`summ`|
|`p1...pN`|string|Yes|Argument of task execution.|arg1...argN|
|`async`|boolean|Yes|Determines whether the task is performed asynchronously.|`true`|

**Response:**

The response contains an error message, unique identifier of the task, the status and result of computation.

```json
{
  "error": "",
  "response": {
    "error": "",
    "finished": true,
    "id": "~ee2d1688-2605-4613-8a57-6615a8cbcd1b",
    "result": 4
  },
  "successStatus": 0
}
```

### Result of a Task

Returns  the computation result for a given task.

**Request:**

```shell
http://host:port/ignite?cmd=res&id={taskId}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`id`|string||ID of the task whose result is to be returned.|69ad0c48941-4689aae0-6b0e-4d52-8758-ce8fe26f497d~4689aae0-6b0e-4d52-8758-ce8fe26f497d|

**Response:**

The response contains information about errors (if any), ID of the task, and the status and result of computation.

```json
{
  "error": "",
  "response": {
    "error": "",
    "finished": true,
    "id": "69ad0c48941-4689aae0-6b0e-4d52-8758-ce8fe26f497d~4689aae0-6b0e-4d52-8758-ce8fe26f497d",
    "result": 4
  },
  "successStatus": 0
}
```

### SQL Query Execute

Runs SQL query over cache.

**Request:**

```shell
http://host:port/ignite?cmd=qryexe&type={type}&pageSize={pageSize}&cacheName={cacheName}&arg1=1000&arg2=2000&qry={query}&keepBinary={keepBinary}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`type`|string||Type for the query|String|
|`pageSize`|number||Page size for the query.|3|
|`cacheName`|string|Yes|Cache name.|testCache|
|`arg1...argN`|string||Query arguments|1000,2000|
|`qry`|strings||Encoding sql query|`salary+%3E+%3F+and+salary+%3C%3D+%3F`|
|`keepBinary`|boolean|Yes|Keeps the query results in binary form. Defaults to `false`. See [Binary Objects in Query Results](#binary-objects-in-query-results).|true|

**Response:**

The response object contains the items returned by the query, a flag indicating the last page, and `queryId`.

```json
{
  "error":"",
  "response":{
    "fieldsMetadata":[],
    "items":[
      {"key":3,"value":{"name":"Jane","id":3,"salary":2000}},
      {"key":0,"value":{"name":"John","id":0,"salary":2000}}],
    "last":true,
    "queryId":0},
  "successStatus":0
}
```

### SQL Fields Query Execute

Runs SQL fields query over cache.

**Request:**

```shell
http://host:port/ignite?cmd=qryfldexe&pageSize=10&cacheName={cacheName}&qry={qry}&keepBinary={keepBinary}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`pageSize`|number||Page size for the query.|3|
|`cacheName`|string|Yes|Cache name.|testCache|
|`arg1...argN`|string||Query arguments.|1000,2000|
|`qry`|strings||Encoding sql fields query.|`select+firstName%2C+lastName+from+Person`|
|`keepBinary`|boolean|Yes|Keeps the query results in binary form. Defaults to `false`. See [Binary Objects in Query Results](#binary-objects-in-query-results).|true|

**Response:**

The response object contains the items returned by the query, fields query metadata, a flag indicating the last page, and `queryId`.

```json
{
  "error": "",
  "response": {
    "fieldsMetadata": [
      {
        "fieldName": "FIRSTNAME",
        "fieldTypeName": "java.lang.String",
        "schemaName": "person",
        "typeName": "PERSON"
      },
      {
        "fieldName": "LASTNAME",
        "fieldTypeName": "java.lang.String",
        "schemaName": "person",
        "typeName": "PERSON"
      }
    ],
    "items": [["Jane", "Doe" ], ["John", "Doe"]],
    "last": true,
    "queryId": 0
  },
  "successStatus": 0
}
```

### SQL Scan Query Execute

Runs a scan query over a cache.

**Request:**

```shell
http://host:port/ignite?cmd=qryscanexe&pageSize={pageSize}&cacheName={cacheName}&className={className}&keepBinary={keepBinary}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`pageSize`|Number||Page size for the query|3|
|`cacheName`|String|Yes|Cache name.|testCache|
|`className`|String|Yes|Predicate class name for scan query. Class should implement `IgniteBiPredicate` interface.|`org.apache.ignite.filters.PersonPredicate`|
|`keepBinary`|Boolean|Yes|Keeps the query results in binary form. Defaults to `false`. See [Binary Objects in Query Results](#binary-objects-in-query-results).|true|

**Response:**

The response  object contains the items returned by the scan query, fields query metadata, a flag indicating last page, and `queryId`.

```json
{
  "error": "",
  "response": {
    "fieldsMetadata": [
      {
        "fieldName": "key",
        "fieldTypeName": "",
        "schemaName": "",
        "typeName": ""
      },
      {
        "fieldName": "value",
        "fieldTypeName": "",
        "schemaName": "",
        "typeName": ""
      }
    ],
    "items": [
      {
        "key": 1,
        "value": {
          "firstName": "Jane",
          "id": 1,
          "lastName": "Doe",
          "salary": 1000
        }
      },
      {
        "key": 3,
        "value": {
          "firstName": "Jane",
          "id": 3,
          "lastName": "Smith",
          "salary": 2000
        }
      }
    ],
    "last": true,
    "queryId": 0
  },
  "successStatus": 0
}
```

### SQL Query Fetch

Gets next page for the query.

**Request:**

```shell
http://host:port/ignite?cmd=qryfetch&pageSize={pageSize}&qryId={queryId}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`pageSize`|number||Page size for the query.|3|
|`qryId`|number||Query id that is returned from the `Sql query execute`, `sql fields query execute`, or `sql fetch` commands.|0|

**Response:**

The response object contains the items returned by the query, a flag indicating the last page, and `queryId`.

```json
{
  "error":"",
  "response":{
    "fieldsMetadata":[],
    "items":[["Jane","Doe"],["John","Doe"]],
    "last":true,
    "queryId":0
  },
  "successStatus":0
}
```

### SQL Query Close

Closes query resources.

**Request:**

```shell
http://host:port/ignite?cmd=qrycls&qryId={queryId}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`qryId`|number||Query id that is returned from the `SQL query execute`, `SQL fields query execute`, or `SQL fetch` commands.|0|

**Response:**

The command returns 'true' if the query was closed successfully.

```json
{
  "error":"",
  "response":true,
  "successStatus":0
}
```

### Probe

Probes a node for Kubernetes liveness, readiness, and startup checks. The optional
`kind` query parameter (case-insensitive) selects the check; without it, the command
returns whether the Ignite kernel has started.

|`kind` value|Meaning|
|---|---|
|*(omitted)* or `liveness`|**Liveness.** Returns whether the Ignite kernel has started. Backs the `livenessProbe`. A node that is rebalancing or in maintenance mode is still considered alive.|
|`readiness`|**Readiness/startup.** Returns whether the node is ready to serve traffic. Backs the `readinessProbe` and `startupProbe`. A (re)joining node reports not-ready until it has finished pulling its partitions, so a rolling restart does not bounce the next pod mid-rebalance and lose data.|

The readiness check is evaluated in order and reports ready only when the kernel has
started, the node is not in maintenance mode, the node is not draining, and either the
cluster is inactive or the node's initial rebalance has completed. Once a node completes
its initial rebalance it stays ready for the rest of its lifetime; later topology-change
rebalances do not flip it back to not-ready.

**Request:**

```shell
http://host:port/ignite?cmd=probe&kind=readiness
```

**Response:**

Returns HTTP status code 200 when the check passes, and 503 otherwise. For a failed
readiness check, the `error` field carries the reason: `kernel not started`,
`maintenance mode`, `draining`, or `rebalance in progress`. An unrecognized `kind` value
returns a failed status with the message
`Unknown probe kind: <value> (expected one of: liveness, readiness)`.

```json
{
  "error": "",
  "response": "ready",
  "successStatus": 0
}
```

### Drain

Sets, clears, or reads a node's *drain flag* — a Kubernetes pod-lifecycle switch for
graceful rolling restarts. While the flag is set, `cmd=probe&kind=readiness` reports 503,
so Kubernetes removes the pod from the Service endpoints and stops routing new traffic to
it before the pod is terminated. The required `action` query parameter (case-insensitive)
selects the operation.

|`action` value|Meaning|
|---|---|
|`start`|Sets the drain flag. Under the [`GRACEFUL` shutdown policy](../../gridgain8-usage/starting-nodes.md), the command is refused with 503 if this node is the sole owner of any cache group's partitions, so that terminating it would not make that data unavailable; pass `force=true` to override and accept the data loss. Requires `ADMIN_OPS` privilege.|
|`stop`|Clears the drain flag, returning the node to normal readiness behavior. Requires `ADMIN_OPS` privilege.|
|`status`|Returns whether the drain flag is currently set. Does not require authentication.|

The drain flag is held in node memory and is not persisted: it is automatically cleared
when the node restarts. The unique-data guard on `start` applies only under the `GRACEFUL`
shutdown policy; under `IMMEDIATE` the flag is set without the ownership check.

**Request:**

```shell
http://host:port/ignite?cmd=drain&action=start&force=true
```

**Response:**

Returns HTTP status code 200 on success. For `action=status`, the current flag is carried
in the `response` field:

```json
{
  "error": "",
  "response": {
    "draining": true
  },
  "successStatus": 0
}
```

When `action=start` is refused because the node holds the only copy of a cache group's
data, the command returns HTTP status code 503, the `error` field names the affected cache
groups, and the `response` field lists them:

```json
{
  "error": "unique data held on cache groups: [myCache]",
  "response": {
    "uniqueDataHeld": true,
    "cacheGroups": ["myCache"]
  },
  "successStatus": 503
}
```

### Supply Status

Reports whether a node is still supplying partitions to other nodes, and optionally gates a
graceful shutdown on that answer. Use this endpoint during a rolling restart to confirm that a node can be
stopped without interrupting rebalance. The optional `shutdown` query parameter selects the
behavior.

|`shutdown` value|Meaning|
|---|---|
|*(omitted)* or `false`|**Informational read.** Reports the node's supply state and its active client connections. Does not require authentication.|
|`true`|**Check-and-shutdown gate.** Reports the same information, and stops the node gracefully only if every safety check passes. Requires `ADMIN_OPS` privilege.|

With `shutdown=true` is set, the node is stopped only when all of the following checks pass. They are
evaluated in order, and the node keeps running if any of them fails:

1. The node is not the sole owner of any cache group's partitions, under the [`GRACEFUL` shutdown policy](../../gridgain8-usage/starting-nodes.md). Pass `force=true` to skip this check and accept data loss.
2. No partition map exchange is in progress.
3. The node is not pulling partitions from other nodes.
4. The node is not supplying partitions to other nodes.
5. No other node is committing a graceful stop at the same moment.

When every check passes, the command returns 200 and the node stops after the response has been sent.
Calling the command again reports the same information without triggering a second stop.

{% hint style="info" %}
Under the `IMMEDIATE` shutdown policy the sole-owner check does not apply, but the remaining
checks still do.
{% endhint %}

**Request:**

```shell
http://host:port/ignite?cmd=supply-status&shutdown=true
```

**Response:**

Returns HTTP status code 200 when the node is not supplying, or, for `shutdown=true`, when the
node passed every check and is stopping. The `response` field carries the supply state, the cache
groups involved, and the active client connections by type:

```json
{
  "error": "",
  "response": {
    "supplying": false,
    "supplyingCacheGroups": [],
    "totalClients": 3,
    "clientsByType": {
      "thin": 2,
      "jdbc": 1
    },
    "uniqueDataHeld": false,
    "uniqueDataCacheGroups": []
  },
  "successStatus": 0
}
```

When `shutdown=true` is refused, the command returns HTTP status code 503, the node keeps running,
and the `error` field names the check that failed: `unique data held on cache groups: [...]`,
`pme in progress`, `rebalancing: [...]`, `supplying: [...]`, or
`concurrent graceful shutdown commit - retry`.

```json
{
  "error": "supplying: [myCache]",
  "response": {
    "supplying": true,
    "supplyingCacheGroups": ["myCache"],
    "totalClients": 0,
    "clientsByType": {},
    "uniqueDataHeld": false,
    "uniqueDataCacheGroups": []
  },
  "successStatus": 503
}
```

### Cache List

Lists the caches, cache groups, or atomic sequences on the cluster. This command is the REST
equivalent of `control.sh --cache list` and reports the same information. The cluster must be
active.

By default, the command lists caches.

Pass the `groups=true` parameter to list cache groups instead, or `seq=true` parameter to list atomic sequences.

Pass `config=true` to include each cache's configuration in the response. This parameter is only compatible
with listing caches, so you cannot combine it with `groups` or `seq`.

{% hint style="info" %}
This command has no dedicated REST permission. When security is enabled, the caller needs
`TASK_EXECUTE` for `VisorViewCacheTask` and `GridCacheAdapter$SizeLongTask`, and, when you pass
`config=true`, for `VisorCacheConfigurationCollectorTask` as well. These are the same permissions
`control.sh --cache list` requires, so no security configuration change is needed when you move
from `control.sh` to the REST API.
{% endhint %}

**Request:**

```shell
http://host:port/ignite?cmd=cachelist&regex={regex}&config={config}&nodeId={nodeId}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`regex`|string|Yes|Java regular expression that a cache, cache group, or sequence name must match to be listed.<br>Default value is `.*`, which matches every name.|cache[12]|
|`groups`|boolean|Yes|Set to `true` to list cache groups instead of caches. Default value is `false`. Cannot be combined with `seq` or `config`.|true|
|`seq`|boolean|Yes|Set to `true` to list atomic sequences instead of caches. Default value is `false`. Cannot be combined with `groups` or `config`.|true|
|`config`|boolean|Yes|Set to `true` to include each cache's configuration in the response. Default value is `false`. Cannot be combined with `groups` or `seq`.|true|
|`nodeId`|string|Yes|ID of the server node that collects the information. Must be a server node.<br>If you omit it, the node that receives the request is used when it is a server node, otherwise the oldest server node in the cluster is used.|8daab5ea-af83-4d91-99b6-77ed2ca06647|

**Response:**

The `response` field holds an array whose entries describe the objects the requested mode lists:

{% tabs %}
{% tab title="Caches" %}
By default, each entry describes a cache:

```json
{
  "error": null,
  "response": [
    {
      "cacheName": "partitionedCache",
      "cacheId": 1035368619,
      "grpName": "myGroup",
      "grpId": 98629247,
      "prim": 1024,
      "mapped": 1024,
      "mode": "PARTITIONED",
      "atomicity": "ATOMIC",
      "backups": 1,
      "affCls": "RendezvousAffinityFunction",
      "cacheSize": 100
    }
  ],
  "successStatus": 0
}
```

|Field|Type|Description|Example|
|---|---|---|---|
|`prim`|number|Number of partitions the cache's affinity function is configured with.|1024|
|`mapped`|number|Number of primary partitions currently mapped to server data nodes.|1024|
|`affCls`|string|Simple class name of the affinity function.|RendezvousAffinityFunction|
|`cacheSize`|number|Total number of entries in the cache across the cluster.|100|
{% endtab %}

{% tab title="Cache groups" %}
With `groups=true`, each entry describes a cache group. The fields are the same as for caches,
except that `cacheName` and `cacheId` are replaced by `cachesCnt`:

```json
{
  "error": null,
  "response": [
    {
      "grpName": "myGroup",
      "grpId": 98629247,
      "cachesCnt": 2,
      "prim": 1024,
      "mapped": 1024,
      "mode": "PARTITIONED",
      "atomicity": "ATOMIC",
      "backups": 1,
      "affCls": "RendezvousAffinityFunction",
      "cacheSize": 200
    }
  ],
  "successStatus": 0
}
```

|Field|Type|Description|Example|
|---|---|---|---|
|`cachesCnt`|number|Number of caches in the group.|2|
|`prim`|number|Number of partitions the group's affinity function is configured with.|1024|
|`mapped`|number|Number of primary partitions currently mapped to server data nodes.|1024|
|`affCls`|string|Simple class name of the affinity function.|RendezvousAffinityFunction|
|`cacheSize`|number|Total number of entries in all caches of the group across the cluster.|200|
{% endtab %}

{% tab title="Atomic sequences" %}
With `seq=true`, each entry describes an atomic sequence:

```json
{
  "error": null,
  "response": [
    {
      "seqName": "mySequence",
      "curVal": 1000
    }
  ],
  "successStatus": 0
}
```

|Field|Type|Description|Example|
|---|---|---|---|
|`seqName`|string|Sequence name.|mySequence|
|`curVal`|number|Current sequence value.|1000|

Because a sequence reserves values in batches, `curVal` is the upper bound of the currently
reserved batch and can therefore be greater than the last value the application actually used. If
the cluster has no atomic sequences, the command returns an empty array rather than an error.
{% endtab %}

{% tab title="Caches with configuration" %}
With `config=true`, each entry carries the cache name, the number of mapped partitions, and the
cache configuration. The `configuration` object holds the full cache configuration and is
abbreviated in the example below:

```json
{
  "error": null,
  "response": [
    {
      "cacheName": "partitionedCache",
      "mapped": 1024,
      "configuration": {
        "name": "partitionedCache",
        "groupName": "myGroup",
        "mode": "PARTITIONED",
        "atomicityMode": "ATOMIC",
        "affinityConfiguration": {
          "function": "RendezvousAffinityFunction",
          "partitions": 1024,
          "partitionedBackups": 1
        }
      }
    }
  ],
  "successStatus": 0
}
```

|Field|Type|Description|Example|
|---|---|---|---|
|`mapped`|number|Number of primary partitions currently mapped to server data nodes. It is `null` for a cache that is configured on the cluster but not started on any server node yet.|1024|
|`configuration`|jsonObject|The cache configuration.|See the example above.|
{% endtab %}
{% endtabs %}

When validation fails, the command returns `successStatus` 1 and describes the problem in the
`error` field.

### Cache Distribution

Reports how cache group partitions are distributed across the cluster's server nodes. This command
is the REST equivalent of `control.sh --cache distribution` and reports the same information. The
cluster must be active.

By default, the command collects information from every server node and reports every cache group.
Use `nodeId` to restrict collection to a single node, and `caches` to restrict the report to the
groups that own the named caches.

{% hint style="warning" %}
The `caches` parameter filters by cache **group**, not by individual cache. If a name you
pass shares a group with other caches, the whole group is reported and its `cacheNames` field
lists every cache in it, including caches you did not name.
{% endhint %}

{% hint style="info" %}
This command has no dedicated REST permission. When security is enabled, the caller needs
`TASK_EXECUTE` for `CacheDistributionTask`. This is the same permission
`control.sh --cache distribution` requires, so no security configuration change is needed when you
move from `control.sh` to the REST API.
{% endhint %}

**Request:**

```shell
http://host:port/ignite?cmd=cachedistribution&caches={caches}&nodeId={nodeId}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`caches`|string|Yes|Comma-separated list of cache names whose groups are reported. If you omit it, every cache group is reported. The command fails if any name in the list is not an existing cache.|cache1,cache2|
|`nodeId`|string|Yes|ID of the server node to collect information from. Must be a server node.<br>If you omit it, every server node in the cluster is used.|8daab5ea-af83-4d91-99b6-77ed2ca06647|
|`userAttributes`|string|Yes|Comma-separated list of node user attribute names to include in the `userAttributes` field of each node entry. If you omit it, `userAttributes` is `null`. An attribute that a node does not have is reported with a `null` value.|region,zone|

**Response:**

The `response` field holds an object whose `nodes` array carries one entry per node, each listing
its cache groups and the partitions the node holds for them:

```json
{
  "error": null,
  "response": {
    "nodes": [
      {
        "nodeId": "8daab5ea-af83-4d91-99b6-77ed2ca06647",
        "addresses": "[127.0.0.1, 192.168.1.5]",
        "userAttributes": {
          "region": "us-east"
        },
        "groups": [
          {
            "groupId": 98629247,
            "groupName": "myGroup",
            "cacheNames": ["cache1", "cache2"],
            "partitions": [
              {
                "partition": 0,
                "primary": true,
                "state": "OWNING",
                "updateCounter": 42,
                "size": 100
              }
            ]
          }
        ]
      }
    ],
    "errors": null
  },
  "successStatus": 0
}
```

|Field|Type|Description|Example|
|---|---|---|---|
|`addresses`|string|The node's network addresses, rendered as a single bracketed string.|[127.0.0.1, 192.168.1.5]|
|`userAttributes`|jsonObject|The node user attributes named by the `userAttributes` request parameter.|`{"region": "us-east"}`|
|`primary`|boolean|Whether the node holds this partition as primary. `false` means it holds a backup copy.|true|
|`state`|string|Partition state on this node. One of `MOVING`, `OWNING`, `RENTING`, `EVICTED`, or `LOST`.|OWNING|
|`updateCounter`|number|Partition update counter, which you can compare across nodes to spot divergence.|42|
|`size`|number|Number of entries in the partition on this node.|100|

The `errors` field is `null` when every node succeeded. When collection fails on some nodes,
`errors` maps each failed node's ID to its error message, and those nodes are omitted from the
`nodes` array, which still reports the nodes that succeeded:

```json
{
  "error": null,
  "response": {
    "nodes": [],
    "errors": {
      "8daab5ea-af83-4d91-99b6-77ed2ca06647": "Failed to collect distribution"
    }
  },
  "successStatus": 0
}
```

When validation fails, the command returns `successStatus` 1 and describes the problem in the
`error` field.

### List Properties

Lists all distributed properties available on the cluster. This command is the REST equivalent of `control.sh --property list`.

{% hint style="info" %}
This command requires the `ADMIN_READ_DISTRIBUTED_PROPERTY` permission when security is enabled on the cluster.
{% endhint %}

**Request:**

```shell
http://host:port/ignite?cmd=listproperties
```

**Response:**

```json
{
  "error": "",
  "response": [
    {
      "name": "baselineAutoAdjustEnabled",
      "value": "true",
      "type": "Boolean"
    },
    {
      "name": "sql.disabledFunctions",
      "value": null,
      "type": null
    }
  ],
  "successStatus": 0
}
```

A `null` `value` and `type` mean the property is not set; the cluster uses its built-in default.

### Get Property

Returns the current value of a single distributed property.

{% hint style="info" %}
This command requires the `ADMIN_READ_DISTRIBUTED_PROPERTY` permission when security is enabled on the cluster.
{% endhint %}

**Request:**

```shell
http://host:port/ignite?cmd=getproperty&name={propertyName}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`name`|string||Name of the distributed property to read.|baselineAutoAdjustEnabled|

**Response:**

```json
{
  "error": "",
  "response": {
    "name": "baselineAutoAdjustEnabled",
    "value": "true",
    "type": "Boolean"
  },
  "successStatus": 0
}
```

If the named property is not registered on the cluster, the response uses a non-zero `successStatus` and the `error` field contains `Unknown distributed property: {name}`.

### Set Property

Sets the value of a distributed property cluster-wide.

{% hint style="info" %}
This command requires the `ADMIN_WRITE_DISTRIBUTED_PROPERTY` permission when security is enabled on the cluster.
{% endhint %}

**Request:**

```shell
http://host:port/ignite?cmd=setproperty&name={propertyName}&val={propertyValue}
```

|Parameter|Type|Optional|Description|Example|
|---|---|---|---|---|
|`name`|string||Name of the distributed property to set.|baselineAutoAdjustEnabled|
|`val`|string||New value. The value is parsed according to the property's declared `type`.|true|

**Response:**

```json
{
  "error": "",
  "response": {
    "name": "baselineAutoAdjustEnabled",
    "value": "true",
    "type": "Boolean"
  },
  "successStatus": 0
}
```

If the named property is not registered, or the supplied value fails to parse, the response uses a non-zero `successStatus` and the `error` field describes the failure.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
