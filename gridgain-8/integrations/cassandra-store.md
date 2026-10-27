---
description: >-
  Use Apache Cassandra as the external storage for a GridGain 8 cache with the
  Cassandra cache store.
---

# Cassandra Cache Store

GridGain provides a `CacheStore` implementation that uses Apache Cassandra as the external storage for a cache. The Cassandra cache store does the following:

* Reads entries from Cassandra when they are missing in the cache (read-through), and writes cache updates to Cassandra (write-through).
* Runs batch operations such as `loadAll()`, `writeAll()`, and `deleteAll()` as asynchronous Cassandra queries.
* Creates the keyspaces and tables it needs in Cassandra.

The cache store connects to Cassandra through the DataStax Java driver 4.17 (`com.datastax.oss.driver.*`). The driver does not support native protocol versions 1 and 2, so you need Apache Cassandra 2.1 or later.

## Enabling the Module

The Cassandra cache store is provided by the `ignite-cassandra-store` module:

* To use it on a node started with the `ignite.sh` or `ignite.bat` script, move the `libs/optional/ignite-cassandra-store` folder to `libs` on every server node. For more information, see [Enabling Modules](../gridgain8-development/project-setup.md#enabling-modules).
* To use it in a Maven project, add the dependency:

  ```xml
  <dependency>
      <groupId>org.gridgain</groupId>
      <artifactId>ignite-cassandra-store</artifactId>
      <version>${gridgain.version}</version>
  </dependency>
  ```

To store objects as BLOBs serialized with Kryo, also enable the `ignite-cassandra-serializers` module.

## Configuring the Cache Store

To configure the Cassandra cache store, define three things in the node configuration:

* A `DataSource` bean that describes the connection to Cassandra.
* A `KeyValuePersistenceSettings` bean that describes how cache keys and values map to a Cassandra table.
* A cache that uses `CassandraCacheStoreFactory` as its cache store factory.

The following example configures the `cache1` cache to read and write entries through Cassandra:

```xml
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
        http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd">

    <!-- Connection to Cassandra. -->
    <bean id="cassandraDataSource" class="org.apache.ignite.cache.store.cassandra.datasource.DataSource">
        <property name="contactPoints" value="cassandra1.example.com,cassandra2.example.com"/>
        <property name="localDataCenter" value="datacenter1"/>
        <property name="credentials">
            <bean class="org.apache.ignite.cache.store.cassandra.datasource.PlainCredentials">
                <constructor-arg value="cassandra_user"/>
                <constructor-arg value="cassandra_password"/>
            </bean>
        </property>
        <property name="readConsistency" value="ONE"/>
        <property name="writeConsistency" value="ONE"/>
    </bean>

    <!-- Mapping of the cache keys and values to a Cassandra table. -->
    <bean id="cache1PersistenceSettings" class="org.apache.ignite.cache.store.cassandra.persistence.KeyValuePersistenceSettings">
        <constructor-arg type="org.springframework.core.io.Resource" value="classpath:persistence-settings-cache1.xml"/>
    </bean>

    <bean class="org.apache.ignite.configuration.IgniteConfiguration">
        <property name="cacheConfiguration">
            <list>
                <bean class="org.apache.ignite.configuration.CacheConfiguration">
                    <property name="name" value="cache1"/>
                    <property name="readThrough" value="true"/>
                    <property name="writeThrough" value="true"/>
                    <property name="cacheStoreFactory">
                        <bean class="org.apache.ignite.cache.store.cassandra.CassandraCacheStoreFactory">
                            <property name="dataSourceBean" value="cassandraDataSource"/>
                            <property name="persistenceSettingsBean" value="cache1PersistenceSettings"/>
                        </bean>
                    </property>
                </bean>
            </list>
        </property>

        <!-- Discovery and other settings. -->
    </bean>
</beans>
```

`CassandraCacheStoreFactory` looks up the `DataSource` and `KeyValuePersistenceSettings` beans by name in the Spring context of the node. You can also set the objects directly with the `dataSource` and `persistenceSettings` properties.

### Persistence Settings

The persistence settings file maps the cache keys and values to the columns of a Cassandra table. The following file stores `Long` keys and values in the `key` and `value` columns of the `test1.primitive_test1` table:

```xml
<persistence keyspace="test1" table="primitive_test1">
    <keyPersistence class="java.lang.Long" strategy="PRIMITIVE" column="key"/>
    <valuePersistence class="java.lang.Long" strategy="PRIMITIVE" column="value"/>
</persistence>
```

The `keyPersistence` and `valuePersistence` elements support the following strategies:

* `PRIMITIVE` - stores a simple Java type, such as `int`, `long`, `String`, `double`, or `Date`, in a column of the matching Cassandra type.
* `BLOB` - stores any Java object as a BLOB. Set the `serializer` attribute to `org.apache.ignite.cache.store.cassandra.serializer.JavaSerializer`, or to `org.apache.ignite.cache.store.cassandra.serializer.KryoSerializer` from the `ignite-cassandra-serializers` module.
* `POJO` - stores each field of the object in its own column. You can map fields to columns explicitly with `field` elements, and define the partition key and clustering key of the table with the `partitionKey` and `clusterKey` elements.

The `persistence` element also accepts an optional `ttl` attribute (row expiration, in seconds), and optional `keyspaceOptions` and `tableOptions` elements. The cache store uses those options when it creates the keyspace or the table.

## Data Source Properties

The `DataSource` bean supports the following properties.

| Property | Description | Default |
|---|---|---|
| `contactPoints` | Comma-separated list of Cassandra hosts. A host can include a port, for example `cassandra1.example.com:9142`. Required, unless the contact points are set in the driver configuration file. | None |
| `port` | The port used for the contact points that do not specify one. | `9042` |
| `localDataCenter` | The name of the local Cassandra datacenter for the default load balancing policy. Required when you set `contactPoints`, unless you set a custom load balancing policy class or set `basic.load-balancing-policy.local-datacenter` in the driver configuration. Otherwise, the cache store fails with `Cassandra local datacenter is not specified for the data source`. | None |
| `user`, `password` | The user name and password for Cassandra authentication. If `user` is set, `password` is required. | None |
| `credentials` | An object that implements `org.apache.ignite.cache.store.cassandra.datasource.Credentials`, for example `PlainCredentials`. Cannot be combined with `user` and `password`. | None |
| `authProvider` | A DataStax driver `AuthProvider` instance, for authentication schemes other than user name and password. | None |
| `useSSL` | If `true`, connects to Cassandra over SSL with the default JDK `SSLContext`. | `false` |
| `sslEngineFactory` | A DataStax driver `SslEngineFactory` instance, for custom SSL settings such as your own keystore, truststore, or cipher suites. | None |
| `protocolVersion` | The native protocol version, for example `4`. Versions `1` and `2` are not supported and fail with `Incorrect protocol version`. | Negotiated by the driver |
| `compression` | Transport compression: `lz4`, `snappy`, or `none`. | None |
| `fetchSize` | The number of rows to fetch at once when running a CQL statement. | Driver default |
| `readConsistency`, `writeConsistency` | The Cassandra consistency level for read and write operations, for example `ONE`, `QUORUM`, or `LOCAL_QUORUM`. | Driver default |
| `maxSchemaAgreementWaitSeconds` | The maximum time, in seconds, to wait for schema agreement after a DDL statement. | Driver default |
| `loadBalancingPolicyClass`, `reconnectionPolicyClass`, `retryPolicyClass`, `addressTranslatorClass`, `speculativeExecutionPolicyClass` | The class of the corresponding driver policy. The class must have a public constructor that takes a `DriverContext` and a `String`. The driver creates the instances. | Driver default |
| `configFile` | The name of a classpath resource with additional driver configuration, without the `.conf` extension. See [Driver Configuration File](#driver-configuration-file). | None |
| `sessionExpirationTimeout` | The time, in milliseconds, after which an idle Cassandra session is closed. A new session is created when it is needed. `0` disables the timeout. | `300000` |

The cache store validates the authentication settings when it opens a Cassandra session. If both `user`/`password` and `credentials` are set, it fails with `Both 'user'/'password' and 'credentials' are set for the data source`.

{% hint style="info" %}
When a `DataSource` is sent to other nodes, for example as part of a dynamically created cache, an `authProvider` or `sslEngineFactory` that does not implement `Serializable` is not transferred.
{% endhint %}

### Driver Configuration File

Driver options that do not have a `DataSource` property, such as connection pool size, socket options, and Netty settings, go to a driver configuration file. The file uses the HOCON format of the DataStax driver `application.conf` file, with all options under the `datastax-java-driver` root.

For example, save the following content as `cassandra-driver.conf` on the classpath of every server node:

```
datastax-java-driver {
  advanced.connection.pool.local.size = 2
  advanced.socket.tcp-no-delay = true
}
```

Then reference the file by its name without the extension:

```xml
<bean id="cassandraDataSource" class="org.apache.ignite.cache.store.cassandra.datasource.DataSource">
    <property name="contactPoints" value="cassandra1.example.com"/>
    <property name="localDataCenter" value="datacenter1"/>
    <property name="configFile" value="cassandra-driver"/>
</bean>
```

If the file is not found on the classpath or is empty, the cache store fails with `Cassandra driver config file is not found on classpath or is empty`.

The cache store applies the driver settings in the following order of precedence, from highest to lowest:

1. Java system properties.
2. The file set with `configFile`.
3. The `DataSource` properties.
4. The `application.conf` file of your application.
5. The cache store defaults: a request timeout of 12 seconds, and a request throttler that runs up to 1024 concurrent requests and queues up to 100000 more.
6. The driver defaults.

## Upgrading from GridGain 8.9.x

GridGain 8.10 moves the Cassandra cache store from the DataStax Java driver 3.2 to 4.17. Review your configuration before you upgrade:

* **Cassandra version.** Cassandra 2.1 or later is required. Setting `protocolVersion` to `1` or `2` fails with `Incorrect protocol version`. To upgrade a Cassandra 3 cluster to Cassandra 5, upgrade it to Cassandra 4 first.
* **Local datacenter.** Set `localDataCenter` if you set `contactPoints` and do not use a custom load balancing policy.
* **Policies.** Policies are set by class instead of by instance:

  | GridGain 8.9.x property | GridGain 8.10 property |
  |---|---|
  | `loadBalancingPolicy` | `loadBalancingPolicyClass` |
  | `reconnectionPolicy` | `reconnectionPolicyClass` |
  | `retryPolicy` | `retryPolicyClass` |
  | `addressTranslator` | `addressTranslatorClass` |
  | `speculativeExecutionPolicy` | `speculativeExecutionPolicyClass` |
  | `sslOptions` | `sslEngineFactory` |
  | `poolingOptions`, `socketOptions`, `nettyOptions` | Removed. Use `configFile` and a [Driver Configuration File](#driver-configuration-file). |
  | `collectMetrix`, `jmxReporting` | Removed. |

* **Authentication.** Set either `user` and `password`, or `credentials`, but not both.
* **Dynamically created caches.** GridGain 8.10 cannot read a `DataSource` serialized by an earlier version. If a cache that uses the Cassandra cache store was created dynamically, deserialization fails with `Unsupported DataSource serialization format version`. Drop such caches and create them again after the upgrade.
* **Large transactions.** The cache store writes the changes of a transaction to Cassandra as a single logged batch. A large transaction can exceed the `batch_size_fail_threshold` limit of Cassandra. Keep transactions small, or raise the limit in the Cassandra configuration.
