---
description: >-
  Configure SSL/TLS encryption for GridGain cluster nodes and clients, enable
  client certificate authentication, and manage certificates.
---

# SSL/TLS

This page explains how to configure SSL/TLS encryption between cluster nodes (both server and client nodes) and thin clients that connect to your cluster.

## Considerations

To ensure a sufficient level of security, we recommend that each node (server or client) has its own unique certificate in the node's keystore (including the private key).
This certificate must be trusted by all other server nodes.

Refer to Security Guide: Configuring SSL/TLS/HTTPS, which contains detailed instructions and scripts for generating private key and certificates.

## SSL/TLS for Nodes

To enable SSL/TLS for cluster nodes, configure an `SSLContext` factory in the node configuration.
You can use the `org.apache.ignite.ssl.SslContextFactory`, which is the default factory that uses a configurable keystore to initialize the SSL context.

Below is an example of `SslContextFactory` configuration:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

    <property name="sslContextFactory">
        <bean class="org.apache.ignite.ssl.SslContextFactory">
            <property name="keyStoreType" value="PKCS12"/>
            <property name="keyStoreFilePath" value="keystore/node.p12"/>
            <property name="keyStorePassword" value="123456"/>
            <property name="trustStoreType" value="PKCS12"/>
            <property name="trustStoreFilePath" value="keystore/trust.p12"/>
            <property name="trustStorePassword" value="123456"/>
            <property name="protocol" value="TLSv1.3"/>
        </bean>
    </property>

</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration igniteCfg = new IgniteConfiguration();

SslContextFactory factory = new SslContextFactory();

factory.setKeyStoreFilePath("keystore/node.p12");
factory.setKeyStorePassword("123456".toCharArray());
factory.setTrustStoreFilePath("keystore/trust.p12");
factory.setTrustStorePassword("123456".toCharArray());
factory.setProtocol("TLSv1.3");

igniteCfg.setSslContextFactory(factory);
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration
{
    SslContextFactory = new SslContextFactory
    {
        KeyStoreFilePath = "server.p12",
        KeyStorePassword = "123",
        TrustStoreFilePath = "trust.p12",
        TrustStorePassword = "345"
    }
};

Ignition.Start(cfg);
```
{% endtab %}

{% tab title="C++" %}
Not supported.
{% endtab %}
{% endtabs %}

The keystore must contain the node's certificate, including its private key.
The trust store must contain the trusted certificates for all other cluster nodes.

You can define other properties, such as key algorithm, key store type, or trust manager. See the description of the properties in the [SslContextFactory Properties](#sslcontextfactory-properties) section.

After starting the node, you should see the following messages in the logs:

```text
Security status [authentication=off, tls/ssl=on]
```

## SSL/TLS for Thin Clients and JDBC/ODBC

GridGain uses the same SSL/TLS properties for all clients, including thin clients and JDBC/ODBC connections. The properties are configured within the client connector configuration.
The client connector configuration is defined via the `IgniteConfiguration.clientConnectorConfiguration` property.

To enable SSL/TLS for client connections, set the `sslEnabled` property to `true` and provide an `SslContextFactory` in the client connector configuration.
You can configure an SSLContext factory that will be used for client connections only, or you can reuse the [SSLContextFactory configured for nodes](#ssl-tls-for-nodes).
Reusing the node factory for the client connector is not recommended. A single truststore guarding both the client
connector and the discovery ports can allow a server node to join the cluster using a client certificate.

Then, configure SSL on the client side in the same way. Refer to the specific client documentation for details.

Here is an example configuration that sets `SslContextFactory` for client connection:

{% tabs %}
{% tab title="XML" %}
```xml
<property name="clientConnectorConfiguration">
    <bean class="org.apache.ignite.configuration.ClientConnectorConfiguration">
        <property name="sslEnabled" value="true"/>
        <property name="useIgniteSslContextFactory" value="false"/>
        <property name="sslContextFactory">
            <bean class="org.apache.ignite.ssl.SslContextFactory">
                <property name="keyStoreType" value="PKCS12"/>
                <property name="keyStoreFilePath" value="keystore/node.p12"/>
                <property name="keyStorePassword" value="123456"/>
                <property name="trustStoreType" value="PKCS12"/>
                <property name="trustStoreFilePath" value="keystore/client-trust.p12"/>
            </bean>
        </property>
    </bean>
</property>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration igniteCfg = new IgniteConfiguration();

ClientConnectorConfiguration clientCfg = new ClientConnectorConfiguration();
clientCfg.setSslEnabled(true);
clientCfg.setUseIgniteSslContextFactory(false);
SslContextFactory sslContextFactory = new SslContextFactory();
sslContextFactory.setKeyStoreFilePath("/path/to/server.p12");
sslContextFactory.setKeyStorePassword("123456".toCharArray());

sslContextFactory.setTrustStoreFilePath("/path/to/client-trust.p12");
sslContextFactory.setTrustStorePassword("123456".toCharArray());

clientCfg.setSslContextFactory(sslContextFactory);

igniteCfg.setClientConnectorConfiguration(clientCfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteClientConfiguration
{
    Endpoints = new[] {"127.0.0.1:10800"},
    SslStreamFactory = new SslStreamFactory
    {
        CertificatePath = ".../certs/client.pfx",
        CertificatePassword = "password",
    }
};
using (var client = Ignition.StartClient(cfg))
{
    //...
}
```
{% endtab %}

{% tab title="C++" %}
Not supported.
{% endtab %}
{% endtabs %}

If you want to reuse the SSLContext factory configured for nodes, you only need to set the `sslEnabled` property to `true`, and `ClientConnectorConfiguration` will look for the SSLContext configured in `IgniteConfiguration`:

{% tabs %}
{% tab title="XML" %}
```xml
<property name="clientConnectorConfiguration">
    <bean class="org.apache.ignite.configuration.ClientConnectorConfiguration">
        <property name="sslEnabled" value="true"/>
    </bean>
</property>
```
{% endtab %}

{% tab title="Java" %}
```java
ClientConnectorConfiguration clientConnectionCfg = new ClientConnectorConfiguration();
clientConnectionCfg.setSslEnabled(true);
```
{% endtab %}

{% tab title="C#/.NET" %}
Not supported.
{% endtab %}

{% tab title="C++" %}
Not supported.
{% endtab %}
{% endtabs %}

## Configuring Client SSL/TLS Authentication

In most cases, it is sufficient to only have SSL/TLS certificates on the server nodes. However, sometimes security policies require
client certificates validation (also referred to as "client SSL/TLS authentication", "mutual authentication", or "two-way SSL") to be enabled. This behavior can be configured for all types of GridGain clients.

### Thick Clients SSL/TLS Authentication

By default, thick clients have certificate validation enabled.

To disable it, set `SslContextFactory.needClientAuth=false` on the server nodes.

### Thin Clients SSL/TLS Authentication

By default, thin clients are not required to have client certificates.

To enable client certificate validation, set `ClientConnectorConfiguration.sslClientAuth=true` on the server nodes.

### Management Tools SSL/TLS Authentication

By default, management scripts such as `control.sh|bat`, `management.sh|bat`, and `snapshot-utility.sh|bat` are not required to have client certificates.

To enable client certificate validation, set `ConnectorConfiguration.sslClientAuth=true` on the server nodes.

### REST SSL/TLS Authentication

By default, REST does not require client certificate validation. This behavior is controlled by the Jetty configuration.

To enable client certificate validation, use the following Jetty `SslContextFactory` configuration on the server nodes:

{% code title="XML" %}
```xml
<New id="sslContextFactory" class="org.eclipse.jetty.util.ssl.SslContextFactory">
    <Set name="keyStorePath">server.p12</Set>
    <Set name="keyStorePassword">123456</Set>
    <Set name="keyStoreType">PKCS12</Set>
    <Set name="trustStorePath">trust.p12</Set>
    <Set name="trustStorePassword">123456</Set>
    <Set name="trustStoreType">PKCS12</Set>
    <Set name="needClientAuth">true</Set>
</New>
```
{% endcode %}

## Disabling Certificate Validation Completely

In some cases, it is useful to disable certificate validation, for example when connecting to a server with a self-signed certificate.
This can be achieved by using a disabled trust manager, which can be obtained by calling the `SslContextFactory.getDisabledTrustManager()` method.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

    <property name="sslContextFactory">
        <bean class="org.apache.ignite.ssl.SslContextFactory">
            <property name="keyStoreType" value="PKCS12"/>
            <property name="keyStoreFilePath" value="keystore/node.p12"/>
            <property name="keyStorePassword" value="123456"/>
            <property name="trustManagers">
                <bean class="org.apache.ignite.ssl.SslContextFactory" factory-method="getDisabledTrustManager"/>
            </property>
        </bean>
    </property>

</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration igniteCfg = new IgniteConfiguration();

SslContextFactory factory = new SslContextFactory();

factory.setKeyStoreFilePath("keystore/node.p12");
factory.setKeyStorePassword("123456".toCharArray());
factory.setTrustManagers(SslContextFactory.getDisabledTrustManager());

igniteCfg.setSslContextFactory(factory);
```
{% endtab %}
{% endtabs %}

Note that there is a difference between using `SslContextFactory.getDisabledTrustManager()` and disabling client authentication.
With `SslContextFactory.getDisabledTrustManager()`, all nodes are still required to have a certificate but its validity will not be checked.
If client authentication is disabled, clients are not required to have certificates at all.

## Upgrading Certificates

If your SSL certificates are about to expire or have been compromised, you can install new certificates without shutting down the whole cluster.

The following is a procedure for updating certificate.

### Trusted Certificate

If the new certificate is trusted by all cluster nodes, you can import the new certificate (including the private key) to the key store of the corresponding node and remove the old certificate. Then, gracefully restart the node. Repeat this procedure for all certificates you want to update.

### Untrusted Certificate

This approach is required if a new certificate is issued by the same certificate authority, but may or may not be trusted.

Repeat the following procedure for the nodes where the certificate is not trusted:

1. Import the new certificate to the trusted store of the node.
2. Gracefully restart the node.
3. Repeat these steps for all server nodes.

### Certificate from a New Certificate Authority

If the certificate is issues from a different certificate authority (CA) than the previous one, rolling restart is not possible for the cluster, as the running cluster cannot have certificates from different authorities active at the same time.

To change the certificate in this case:

1. Deactivate the cluster.
2. Shut down the cluster nodes.
3. Update certificate on all nodes in the cluster.
4. Restart the nodes and reactivate the cluster.

## SslContextFactory Properties

`SslContextFactory` supports the following properties:

| Property | Description | Default |
|---|---|---|
|`keyAlgorithm`|The key manager algorithm that will be used to create a key manager.|`SunX509`|
|`keyStoreFilePath`|The path to the key store file. This is a mandatory parameter since the SSL context can not be initialized without a key manager.|`N/A`|
|`keyStorePassword`|The key store password.|`N/A`|
|`keyStoreType`|The key store type.|`PKCS12`|
|`needClientAuth`|Whether the connecting clients are required to have a trusted SSL/TLS certificate.|`true`|
|`protocol`|The protocol for secure transport. [Supported algorithms](https://docs.oracle.com/en/java/javase/11/docs/specs/security/standard-names.html#sslcontext-algorithms).|`TLS`|
|`trustStoreFilePath`|The path to the trust store file.|`N/A`|
|`trustStorePassword`|The trust store password.|`N/A`|
|`trustStoreType`|The trust store type.|`PKCS12`|
|`trustManagers`|A list of pre-configured trust managers.|`N/A`|

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
