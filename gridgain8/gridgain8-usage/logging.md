---
description: >-
  How to configure logging in GridGain, including JUL, Log4j2, Log4j, JCL, SLF4J,
  and Logback, plus suppressing sensitive information.
---

# Configuring Logging

## Overview

GridGain supports a number of logging libraries and frameworks:

- JUL (default),
- Log4j,
- Log4j2,
- JCL,
- SLF4J.

This section shows you how to set up the logger.

When a node starts, it outputs start-up information to the console, including the information about the configured logging library. Each logging library has its own configuration parameters and should be set up according to its official documentation. Besides library-specific configuration, there is a number of system properties that allow you to tune logging. These properties are presented in the following table.

| System Property | Description | Default Value|
|---|---|---|
| `IGNITE_LOG_INSTANCE_NAME` | If the property is set, GridGain includes its instance name in log messages. |  Not set|
| `IGNITE_QUIET` | Set to `false` to disable the quiet mode and enable the verbose mode.<br>In the verbose mode, the node logs a lot more information. | `false`|
| `IGNITE_LOG_DIR` | The directory where GridGain writes log files. | `$IGNITE_HOME/work/log`|
| `IGNITE_DUMP_THREADS_ON_FAILURE` | Set to `true` to output thread dumps to the log when a critical error is caught. | `true`|
| `IGNITE_SENSITIVE_DATA_LOGGING` | Set to "plain" (true) prints everything as is, to "hash" prints hash (primitives are printed as is), to "none" (false) doesn’t print anything. | `hash`|
| `IGNITE_CONSOLE_APPENDER` | If `true`, and if GridGain is launched in the verbose mode (see `IGNITE_QUIET` above), and if no console appenders can be found in configuration, the default console appender is added. Set to `false` to prevent appender addition. | `true`|

## Default Logging

By default, GridGain uses the java.util.logging (JUL) framework.
If you start GridGain using the `ignite.sh|bat` script from the distribution package, GridGain uses `$IGNITE_HOME/config/java.util.logging.properties` as the default logging configuration file and output all messages to log files in the `$IGNITE_HOME/work/log` directory. You can override the default logging directory by specifying the `IGNITE_LOG_DIR` system property.

If you use GridGain as a library in your application, the default logging configuration includes only console handler at INFO level.
You can provide a custom configuration file via the `java.util.logging.config.file` system property.

## Using Log4j2

{% hint style="info" %}
Before using Log4j2, enable the [ignite-log4j2](setup.md#enabling-modules) module.
{% endhint %}

To enable Log4j2 logger, set the `gridLogger` property of `IgniteConfiguration`, as shown below:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration" id="ignite.cfg">
    <property name="gridLogger">
        <bean class="org.apache.ignite.logger.log4j2.Log4J2Logger">
            <!-- log4j2 configuration file -->
            <constructor-arg type="java.lang.String" value="log4j2-config.xml"/>
        </bean>
    </property>

    <!-- other properties --> 

    <!-- Explicitly configure TCP discovery SPI to provide list of initial nodes. -->
    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <property name="ipFinder">
                <!--
                    Ignite provides several options for automatic discovery that can be used
                    instead os static IP based discovery. For information on all options refer
                    to our documentation: http://apacheignite.readme.io/docs/cluster-config
                -->
                <!-- Uncomment static IP finder to enable static-based discovery of initial nodes. -->
                <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                    <!--bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.multicast.TcpDiscoveryMulticastIpFinder"-->
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
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();

IgniteLogger log = new Log4J2Logger("log4j2-config.xml");

cfg.setGridLogger(log);

// Start a node.
try (Ignite ignite = Ignition.start(cfg)) {
    ignite.log().info("Info Message Logged!");
}
```
{% endtab %}

{% tab title=".NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

In the above example, the path to `log4j2-config.xml` can be either an absolute path, a local path relative to META-INF in classpath or to `IGNITE_HOME`. An example log4j2 configuration file can be found in the distribution package (`$IGNITE_HOME/config/ignite-log4j2.xml`).

{% hint style="info" %}
Log4j2 supports runtime reconfiguration, i.e. changes in the configuration file is applied without the need to restart the application.
{% endhint %}

## Using Log4j

{% hint style="info" %}
Log4j was excluded from delivery packages as it is no longer officially supported. Before using Log4j, module ignite-log4j must be copied from previous version optional libs folder.
{% endhint %}

To enable Log4j logger, set the `gridLogger` property of `IgniteConfiguration`, as shown in the following example:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration" id="ignite.cfg">
    <property name="gridLogger">
        <bean class="org.apache.ignite.logger.log4j.Log4JLogger">
            <!-- log4j configuration file -->
            <constructor-arg type="java.lang.String" value="log4j-config.xml"/>
        </bean>
    </property>

    <!-- other properties --> 

    <!-- Explicitly configure TCP discovery SPI to provide list of initial nodes. -->
    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <property name="ipFinder">
                <!--
                    Ignite provides several options for automatic discovery that can be used
                    instead os static IP based discovery. For information on all options refer
                    to our documentation: http://apacheignite.readme.io/docs/cluster-config
                -->
                <!-- Uncomment static IP finder to enable static-based discovery of initial nodes. -->
                <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                    <!--bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.multicast.TcpDiscoveryMulticastIpFinder"-->
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
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();

IgniteLogger log = new Log4JLogger("log4j-config.xml");

cfg.setGridLogger(log);

// Start a node.
try (Ignite ignite = Ignition.start(cfg)) {
    ignite.log().info("Info Message Logged!");
}
```
{% endtab %}

{% tab title=".NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

In the above example, the path to `log4j-config.xml` can be either an absolute path, a local path relative to META-INF in classpath or to `IGNITE_HOME`. An example log4j configuration file can be found in the distribution package (`$IGNITE_HOME/config/ignite-log4j.xml`).

## Using JCL

{% hint style="info" %}
Before using JCL, enable the [ignite-jcl](setup.md#enabling-modules) module.
{% endhint %}

{% hint style="info" %}
Note that JCL simply forwards logging messages to an underlying logging system, which needs to be properly configured. Refer to the [JCL official documentation](https://commons.apache.org/proper/commons-logging/guide.html#Configuration) for more information. For example, if you want to use Log4j, make sure you add the required libraries to your classpath.
{% endhint %}

To enable Log4j2 logger, set the `gridLogger` property of `IgniteConfiguration`, as shown below:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration" id="ignite.cfg">
    <property name="gridLogger">
        <bean class="org.apache.ignite.logger.jcl.JclLogger">
        </bean>
    </property>

    <!-- other properties --> 

    <!-- Explicitly configure TCP discovery SPI to provide list of initial nodes. -->
    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <property name="ipFinder">
                <!--
                    Ignite provides several options for automatic discovery that can be used
                    instead os static IP based discovery. For information on all options refer
                    to our documentation: http://apacheignite.readme.io/docs/cluster-config
                -->
                <!-- Uncomment static IP finder to enable static-based discovery of initial nodes. -->
                <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                    <!--bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.multicast.TcpDiscoveryMulticastIpFinder"-->
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
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();

cfg.setGridLogger(new JclLogger());

// Start a node.
try (Ignite ignite = Ignition.start(cfg)) {
    ignite.log().info("Info Message Logged!");
}
```
{% endtab %}

{% tab title=".NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Using SLF4J

{% hint style="info" %}
Before using SLF4J, enable the [ignite-slf4j](setup.md#enabling-modules) module.
{% endhint %}

To enable the SLF4J logger, set the `gridLogger` property of `IgniteConfiguration`, as shown below:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration" id="ignite.cfg">
    <property name="gridLogger">
        <bean class="org.apache.ignite.logger.slf4j.Slf4jLogger">
        </bean>
    </property>

    <!-- other properties --> 

    <!-- Explicitly configure TCP discovery SPI to provide list of initial nodes. -->
    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <property name="ipFinder">
                <!--
                    Ignite provides several options for automatic discovery that can be used
                    instead os static IP based discovery. For information on all options refer
                    to our documentation: http://apacheignite.readme.io/docs/cluster-config
                -->
                <!-- Uncomment static IP finder to enable static-based discovery of initial nodes. -->
                <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                    <!--bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.multicast.TcpDiscoveryMulticastIpFinder"-->
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
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();

cfg.setGridLogger(new Slf4jLogger());

// Start a node.
try (Ignite ignite = Ignition.start(cfg)) {
    ignite.log().info("Info Message Logged!");
}
```
{% endtab %}

{% tab title=".NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

Refer to the [SLF4J user manual](https://www.slf4j.org/docs.html) for more information.

## Using Logback

[Logback](https://logback.qos.ch/) is one of the most widely used logging frameworks in the Java community. Because Logback doesn't have its own API, it uses [SLF4J](https://www.slf4j.org/docs.html) as its native interface. You need to use `ignite-slf4j` to bind Ignite to Logback. 

## Suppressing Sensitive Information

Logs can include the content of cache entries, system properties, startup options, etc.
In some cases, those can contain sensitive information.
You can prevent such information from being written to the log by setting the `IGNITE_TO_STRING_INCLUDE_SENSITIVE` system property to `false`.

```shell
./ignite.sh -J-DIGNITE_TO_STRING_INCLUDE_SENSITIVE=false
```

See [Setting JVM Options](starting-nodes.md#setting-jvm-options) to learn about different ways to set system properties.

## Logging Configuration Example

The following steps guide you through the process of configuring logging. This should be suitable for most cases.

1. Use either Log4j or Log4j2 as the logging framework. To enable it, follow the instructions provided in the corresponding section above.
2. If you use the default configuration file (either `ignite-log4j.xml` or `ignite-log4j2.xml`), uncomment the CONSOLE appender.
3. In the log4j configuration file, set the path to the log file. The default location is `${IGNITE_HOME}/work/log/ignite.log`.
4. Start the nodes in verbose mode:
   - If you use `ignite.sh` to start nodes, specify the `-v` option.
   - If you start nodes from Java code, use the `IGNITE_QUIET=false` system variable.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
