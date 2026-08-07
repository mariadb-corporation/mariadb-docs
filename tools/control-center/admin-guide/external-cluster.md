---
description: >-
  Running GridGain Control Center against an external GridGain 8 cluster to
  separate Control Center data from its backend process.
---

# Running Control Center with an External GridGain 8 Cluster

Using an external GridGain 8 cluster separates Control Center data from its backend process, improving scalability and resilience. The backend becomes stateless, while the external cluster ensures data durability.

{% hint style="info" %}
Before using an external multinode cluster, upgrade Control Center to 2025.4.1+ version.
{% endhint %}

## Prepare the External Cluster

- If you are connecting Control Center to an external GridGain 8 Enterprise Edition or GridGain 8 Ultimate Edition cluster, you must set `ignite.includeGridGainPlugin=true` in the [`application.properties` file](configuration.md).
- If you are using GridGain 8 Community Edition as the external cluster, no additional changes in the `application.properties` file are required.

Ensure that the GridGain 8 version matches the Control Center client version. Control Center internal GridGain node version can be found in the [release notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/control-center/2025.4.1#updating-to-2025-4-1-with-an-external-cluster).

If the GridGain 8 cluster version differs from the version expected by Control Center, enable [rolling upgrades](http://gridgain.com/docs/gridgain8/latest/installation-guide/rolling-upgrades) mode to support mixed-version nodes.

{% hint style="info" %}
Rolling upgrades mode is available only in GridGain 8 Enterprise Edition and GridGain 8 Ultimate Edition.
{% endhint %}

The external cluster requires a specific data region configuration. Use the following configuration as an example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
            http://www.springframework.org/schema/beans/spring-beans.xsd">
    <bean class="org.apache.ignite.configuration.IgniteConfiguration">
        <property name="failureDetectionTimeout" value="10000"/>
        <property name="clientFailureDetectionTimeout" value="10000"/>
        <property name="networkTimeout" value="10000"/>
        <!-- <property name="workDirectory" value="/path/to/work"/> -->

    <!--
    <property name="gridLogger">
        <bean class="org.apache.ignite.logger.log4j2.Log4J2Logger">
            <constructor-arg type="java.lang.String" value="/path/to/logger/ignite-log4j2.xml"/>
        </bean>
    </property>
    -->
        <property name="communicationSpi">
            <bean class="org.apache.ignite.spi.communication.tcp.TcpCommunicationSpi">
                <property name="socketWriteTimeout" value="10000"/>
                <property name="messageQueueLimit"  value="1024"/>
            </bean>
        </property>

        <property name="discoverySpi">
            <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
                <property name="ipFinder">
                    <!-- Configure discovery to Control Center node here. -->
                    <!--
                    <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                        <property name="addresses">
                            <list>
                                <value>127.0.0.1:47500..47510</value>
                            </list>
                        </property>
                    </bean>
                    -->
                </property>
            </bean>
        </property>

        <property name="transactionConfiguration">
            <bean class="org.apache.ignite.configuration.TransactionConfiguration">
                <property name="txTimeoutOnPartitionMapExchange" value="#{60L * 1000L}"/>
                <property name="DefaultTxTimeout" value="20000"/>
            </bean>
        </property>

        <property name="dataStorageConfiguration">
            <bean class="org.apache.ignite.configuration.DataStorageConfiguration">
                <property name="metricsEnabled" value="true"/>

                <property name="walSegmentSize" value="#{128L * 1024 * 1024}"/>
                <property name="writeThrottlingEnabled" value="true"/>
                <property name="walMode" value="LOG_ONLY"/>

                <property name="defaultDataRegionConfiguration">
                    <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                        <property name="initialSize" value="#{1024L * 1024L * 1024L}"/>
                        <property name="maxSize" value="#{1600L * 1024L * 1024L}"/>
                        <property name="metricsEnabled" value="true"/>
                        <property name="persistenceEnabled" value="true"/>
                    </bean>
                </property>
                <property name="dataRegionConfigurations">
                    <list>
                        <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                            <property name="name" value="in-memory"/>
                            <property name="initialSize" value="#{10L * 1024 * 1024}"/>
                            <property name="maxSize" value="#{1024L * 1024L * 1024L}"/>
                            <property name="metricsEnabled" value="true"/>
                        </bean>
                    </list>
                </property>
            </bean>
        </property>
    </bean>
</beans>
```

After setup, ensure that the cluster is [activated](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/baseline-topology#baseline-topology-in-persistent-clusters).

## Configure Control Center

The default `ignite-config.xml` in the Control Center root directory should be replaced with the client configuration. Refer to the following as an example:

```xml
<?xml version="1.0" encoding="UTF-8"?>

<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd">

    <!-- Template of client node to use for tests. -->
    <bean id="clientNode" class="org.apache.ignite.configuration.IgniteConfiguration">
        <property name="igniteInstanceName" value="cc_client"/>
        <property name="clientMode" value="true"/>
        <property name="metricsLogFrequency" value="0"/>
        <property name="failureDetectionTimeout" value="3000"/>
        <property name="networkTimeout" value="5000"/>

        <!-- Disable all clients. -->
        <property name="connectorConfiguration"><null/></property>
        <property name="clientConnectorConfiguration"><null/></property>

        <!-- Logging configuration. -->
        <property name="gridLogger">
            <bean class="org.apache.ignite.logger.slf4j.Slf4jLogger"/>
        </property>

        <property name="discoverySpi">
            <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
                <property name="ipFinder">
                    <!-- Configure discovery to an external GridGain cluster here. -->
                    <!--
                    <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                        <property name="addresses">
                            <list>
                                <value>127.0.0.1:47500..47510</value>
                            </list>
                        </property>
                    </bean>
                    -->
                </property>
            </bean>
        </property>
    </bean>
</beans>
```

## Run Control Center With External Cluster

Start the external GridGain cluster, then start Control Center.

The client node connects to the external cluster, storing all Control Center data there.

Now, all Control Center data, including users, attached clusters, dashboards, alerts, metrics, and query history, is reliably stored in the external GridGain cluster. If Control Center loses its local persistent data, it will reconnect to the external storage after recovery and continue operating without data loss.
