---
description: >-
  GridGain 8.8.9 adds the ability to disable client SSL/TLS certificate validation, along with other improvements and fixes.
hidden: true
---

# GridGain 8.8.9 Release Notes

## New Features

### Ability to Disable Client SSL/TLS Certificate Validation

Historically, Thick Clients were required to provide client certificates if SSL/TLS was enabled in the cluster. This made SSL/TLS configuration significantly harder.

Starting this version, the cluster can be configured to not require client certificates validation.
To do this, set the `needClientAuth=false` property in the `SslContextFactory` configuration.

This mode must be used together with `forceClientToServerConnections=true` to make sure that thick clients never accept connections.

By default, thick clients are still required to provide SSL/TLS certifiicates. This behavior is kept for compatibility.

Note that Thin Clients already are not required to provide SSL/TLS certificates.

The following configuration can be used if thick client certificate validation is not needed:

Server:

{% code title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="sslContextFactory">
        <bean class="org.apache.ignite.ssl.SslContextFactory">
            <property name="keyStoreFilePath" value="keystore.jks"/>
            <property name="keyStorePassword" value="keystorepwd"/>
            <property name="trustStoreFilePath" value="truststore.jks"/>
            <property name="trustStorePassword" value="truststorepwd"/>

            <!-- This property turns off client certificate validation -->
            <property name="needClientAuth" value="false"/>
        </bean>
    </property>
</bean>
```
{% endcode %}

Client:

{% code title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="sslContextFactory">
        <!-- If client certificate validation is turned off on the server, server certificate is issued by a trusted CA,
            and forceClientToServerConnections is enabled then no additional configuration is required. -->
        <bean class="org.apache.ignite.ssl.SslContextFactory"/>

        <!-- If server certificate is self-signed, you may still need to provide a trust store. -->
        <!-- <bean class="org.apache.ignite.ssl.SslContextFactory">
            <property name="trustStoreFilePath" value="truststore.jks"/>
            <property name="trustStorePassword" value="truststorepwd"/>
        </bean> -->
    </property>

    <property name="forceClientToServerConnections" value="true"/>
</bean>
```
{% endcode %}

### Affinity Fields in Binary Objects are Supported in C++ Thin Clients

С++ thin clients now also support affinity fields for binary objects. Here is how you can use them:

{% code title="C++" %}
```cpp
IgniteClient client = IgniteClient::Start();
compute::ComputeClient compute = ignite.GetCompute();

std::string echoValue = "Task returns this value";

std::string res = compute.ExecuteJavaTask<std::string>("my.company.MyEchoTask", echoValue);

assert(res == echoValue);
```
{% endcode %}

## Known Issues

### GridGain May Crash when Using OpenJDK 11

In some rare environments, GridGain servers may crash with a `SocketTimeoutException` exception when running on OpenJDK 11. Consider using OpenJDK 8 or a different JDK provider instead.

Here is an example of the exception that can occur:

```
Exception in thread "main" java.net.SocketTimeoutException: Accept timed out
        at java.base/java.net.PlainSocketImpl.socketAccept(Native Method)
        at java.base/java.net.AbstractPlainSocketImpl.accept(AbstractPlainSocketImpl.java:458)
        at java.base/java.net.ServerSocket.implAccept(ServerSocket.java:565)
        at java.base/java.net.ServerSocket.accept(ServerSocket.java:533)
        at Example.main(Example.java:6)
```

You can track the status of this issue in [openJDK issue tracker](https://bugs.openjdk.java.net/browse/JDK-8237858).

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-33784 | GridGain Integrations | Upgraded Jackson from 2.11.0 to 2.11.4 version to fix a vulnerability. |
| GG-33705 | Cluster Storage Engine | Index page metrics are now calculated correctly. |
| GG-33400 | Platforms & Thin Clients | CPP: Added support for Affinity Fields. Define the void BinaryType<T>::GetAffinityFieldName(std::string&) static method to provide it. |
| GG-33349 | Cluster Storage Engine | Fixed OutOfBoundsException during write-behind flusher lookup. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-33858 | Cluster Communication | It is now possible to disable client SSL certificate validation for thick clients and management tools. |
| GG-33616 | Cluster Security | Added a property (IGNITE_CHECK_SENDER_NODE_SUBJECT), which enables an additional security check for subject id on client nodes. |
| GG-33615 | Cluster Security | System cache operations are forbidden for client nodes by default when the IGNITE_SECURITY_FOR_SYS_CACHE_ENABLED property is enabled. |
| GG-33534 | Cluster Security | Client nodes cannot authorize another local client anymore. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-33827 | Cluster Data Snapshots and Recovery | Fixed potential snapshot corruption for the statically configured caches. |
| GG-33417 | Cluster Snapshot Utility | Added a new --excluded_caches parameter for create, check, and restore operations. This parameter and the --caches parameter for these operations now support cache groups. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.7.2-p15`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.5-p1`, `8.7.6`, `8.7.6-p1`, `8.7.7`, `8.7.8`, `8.7.9`, `8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`, `8.7.19`, `8.7.19-p1`, `8.7.20`, `8.7.21`, `8.7.22`, `8.7.23`, `8.7.24`, `8.7.25`, `8.7.26`, `8.7.26-p1`, `8.7.27`, `8.7.27-p1`, `8.7.28`, `8.7.29`, `8.7.29-p1`, `8.7.30`, `8.7.31`, `8.7.32`, `8.7.33`, `8.7.33-p2`, `8.7.34`, `8.7.35`, `8.7.36`, `8.7.37`, `8.7.38`, `8.8.1`, `8.8.2`, `8.8.3`, `8.8.4`, `8.8.5`, `8.8.6`, `8.8.7`

### Known Limitations

#### Jetty Configuration Incompatibility in GridGain 8.7.21 and Later

If you are upgrading from version 8.7.20 or earlier, consider an incompatibility issue related to Jetty configuration introduced in GridGain 8.7.21.

Your setup may be affected if:

- You use the `ignite-rest-http` module (e.g. to connect to GridGain Web Console)
- You have a custom Jetty configuration that enables SSL for REST
- Your Jetty configuration uses the `org.eclipse.jetty.util.ssl.SslContextFactory` class
- The keystore specified in the Jetty configuration contains both the CA certificate and the private certificate

In this case, after starting a new version, an exception is thrown with an error message similar to the following:

```text
java.lang.IllegalStateException: KeyStores with multiple certificates are not supported on the base class
org.eclipse.jetty.util.ssl.SslContextFactory. (Use org.eclipse.jetty.util.ssl.SslContextFactory$Server
or org.eclipse.jetty.util.ssl.SslContextFactory$Client instead)
```

To workaround this issue, alter the Jetty configuration to use `org.eclipse.jetty.util.ssl.SslContextFactory$Server` or `org.eclipse.jetty.util.ssl.SslContextFactory$Client`.
See the configuration example at the [Client Certificate Authentication](https://www.gridgain.com/docs/latest/administrators-guide/security/authentication#client-certificate-authentication) page.

#### Default `rebalanceThreadPoolSize` in GridGain 8.7.26 and Later

In GridGain 8.7.26, the default value of the property `IgniteConfiguration.rebalanceThreadPoolSize` changed from `1` to `min(4, number of CPU / 4)`.
It may cause a compatibility issue under the following conditions:

- When a Rolling Upgrade is performed
- The upgrade is performed from 8.5.7 version (or earlier) to 8.5.x or from 8.7.3 (or earlier) to 8.7.x
- The server nodes have at least 8 CPU cores
- The nodes configuration does not have the property `IgniteConfiguration.rebalanceThreadPoolSize`, so the default value is used

In this case, an exception is thrown with an error message similar to the following:

```text
сlass org.apache.ignite.IgniteException: Rebalance configuration mismatch (fix configuration or set -DIGNITE_SKIP_CONFIGURATION_CONSISTENCY_CHECK=true system property).
Different values of such parameter may lead to rebalance process instability and hanging.  [rmtNodeId=5fc58fb7-209d-489a-8034-0127a81abed6, locRebalanceThreadPoolSize = 4, rmtRebalanceThreadPoolSize = 1]
```

To workaround this issue, change the configuration of the server nodes to `rebalanceThreadPoolSize=1` so that it matches
the previous default configuration. For example:

```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="rebalanceThreadPoolSize" value="1"/>

    <!-- The rest of the configuration goes here -->
</bean>
```

#### Jetty Doesn't Accept Incorrect Configuration in GridGain 8.7.31 and Later

In GridGain 8.7.31 Jetty was upgraded to 9.4.33. Starting that version, Jetty has more strict validation of the
provided configuration files. Before that version, an incorrectly spelled property in the configuration file had no effect.
Starting this version, errors in the configuration will lead to an error on start.

Your setup may be affected if:

- You use the `ignite-rest-http` module (e.g. to connect to GridGain Web Console)
- You have a custom Jetty configuration for REST
- The custom configuration has errors in it

You will need to fix the custom Jetty configuration before upgrading.

#### `ignite.sh` No Longer Enables Remote JMX by Default in GridGain 8.7.31 and Later

Starting from 8.7.31 version, GridGain no longer attempts to automatically enable the remote JMX.
Default settings are known to cause issues if customized (for example, secure the connection).
Also, in most cases, remote JMX is not required since many tools use local JMX connections (not using TCP).

Your setup may be affected if:

- You start GridGain nodes via `ignite.sh` script
- You connect to GridGain nodes' JMX interface remotely over TCP using the default configuration

To continue using remote JMX, you need to manually specify the required JMX settings.
Please see the example below.
Note that you don't need remote JMX if you use a local connection,
such as connecting JConsole to a GridGain process on the same host.

```bash
export JVM_OPTS="-Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=33333 \
    -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false"

bin/ignite.sh
```

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
