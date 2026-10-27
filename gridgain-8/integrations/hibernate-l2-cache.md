---
description: >-
  Use GridGain 8 as the second-level cache of Hibernate ORM 7.4 with the
  ignite-hibernate-7.4 module.
---

# Hibernate Second-Level Cache

You can use GridGain as the second-level (L2) cache of Hibernate ORM 7.4. The L2 cache keeps entities, collections, and query results in GridGain caches, so every application server that shares a GridGain cluster also shares the cached data. This reduces the number of queries that reach the underlying database.

The integration is provided by the `ignite-hibernate-7.4` module. The module uses the Jakarta Persistence (`jakarta.persistence`) namespace.

{% hint style="info" %}
GridGain 8.10 supports Hibernate 7.4 only. The `ignite-hibernate-4.2`, `ignite-hibernate-5.1`, `ignite-hibernate-5.3`, and `ignite-hibernate-core` modules are removed. If your application uses an earlier Hibernate version, upgrade it to Hibernate 7.4 or stay on GridGain 8.9.x.
{% endhint %}

## Adding the Module to Your Application

The region factory runs inside your application, next to Hibernate. Add the `ignite-hibernate-7.4` module to the application as a Maven dependency:

```xml
<properties>
    <gridgain.version>8.10</gridgain.version>
</properties>

<dependencies>
    <dependency>
        <groupId>org.gridgain</groupId>
        <artifactId>ignite-hibernate-7.4</artifactId>
        <version>${gridgain.version}</version>
    </dependency>
</dependencies>
```

The module depends on `ignite-core` and `org.hibernate.orm:hibernate-core` 7.4. For the GridGain Maven repository and the other GridGain dependencies, see [Using Maven](../gridgain8-development/project-setup.md#using-maven).

If you start the GridGain node from a Spring XML configuration file (see [Connecting to a GridGain Node](#connecting-to-a-gridgain-node)), also add the `ignite-spring` module.

## Enabling the L2 Cache

To enable the L2 cache, set the following Hibernate properties:

* `hibernate.cache.use_second_level_cache` - set to `true`.
* `hibernate.cache.region.factory_class` - set to `org.apache.ignite.cache.hibernate.IgniteRegionFactory`.

Then tell the region factory which GridGain node to use. For details, see [Connecting to a GridGain Node](#connecting-to-a-gridgain-node).

The following example shows a minimal `hibernate.cfg.xml` file that attaches the L2 cache to a node named `hibernate-grid`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE hibernate-configuration PUBLIC
        "-//Hibernate/Hibernate Configuration DTD 3.0//EN"
        "http://www.hibernate.org/dtd/hibernate-configuration-3.0.dtd">
<hibernate-configuration>
    <session-factory>
        <!-- Database connection settings are omitted. -->

        <!-- Enable the second-level cache and the query cache. -->
        <property name="hibernate.cache.use_second_level_cache">true</property>
        <property name="hibernate.cache.use_query_cache">true</property>

        <!-- Use GridGain as the second-level cache. -->
        <property name="hibernate.cache.region.factory_class">org.apache.ignite.cache.hibernate.IgniteRegionFactory</property>

        <!-- Attach to the GridGain node started with this instance name. -->
        <property name="hibernate.cache.ignite.instance_name">hibernate-grid</property>

        <!-- Default concurrency strategy for entities that do not declare one. -->
        <property name="hibernate.cache.ignite.default_access_type">READ_WRITE</property>
    </session-factory>
</hibernate-configuration>
```

You can set the same properties in a `hibernate.properties` file, in `persistence.xml`, or in any other Hibernate settings source:

```properties
hibernate.cache.use_second_level_cache = true
hibernate.cache.region.factory_class = org.apache.ignite.cache.hibernate.IgniteRegionFactory
hibernate.cache.ignite.instance_name = hibernate-grid
```

## Connecting to a GridGain Node

The region factory gets its caches from a GridGain node in the same JVM. You can attach it to a node that your application starts, or let the region factory start the node:

* **Attach to a running node.** Start the node in your application before you build the Hibernate `SessionFactory`, and set `hibernate.cache.ignite.instance_name` to the node's instance name. If you set neither `instance_name` nor `configuration`, the region factory attaches to the node started without an instance name. The node keeps running when the `SessionFactory` is closed.
* **Start a node.** Set `hibernate.cache.ignite.configuration` to the path or URL of a GridGain Spring XML configuration file. The region factory starts a node from that file and stops it when the `SessionFactory` is closed. This option requires the `ignite-spring` module on the application classpath. If both properties are set, `configuration` is used.

The node is usually a [client node](../gridgain8-management/clustering/README.md) that joins your GridGain cluster. The cached data is then stored on the cluster's server nodes and shared by every application that connects to the cluster.

## Configuration Properties

All GridGain-specific properties start with the `hibernate.cache.ignite.` prefix.

| Property | Description | Default |
|---|---|---|
| `hibernate.cache.ignite.instance_name` | The instance name of a running GridGain node to attach to. | None |
| `hibernate.cache.ignite.configuration` | The path or URL of a GridGain Spring XML configuration file. The region factory starts a node from this file. Takes precedence over `instance_name`. | None |
| `hibernate.cache.ignite.cache_name_prefix` | A prefix added to the name of every GridGain cache that backs a Hibernate region. | None |
| `hibernate.cache.ignite.region.<region-name>` | Maps the Hibernate region `<region-name>` to a GridGain cache with the given name. Regions without a mapping use a cache named after the region. | None |
| `hibernate.cache.ignite.default_access_type` | The concurrency strategy for entities and collections that do not declare one. Accepted values: `READ_ONLY`, `READ_WRITE`, `NONSTRICT_READ_WRITE`. | `READ_WRITE` |

## Concurrency Strategies

The GridGain L2 cache supports the following Hibernate cache concurrency strategies:

* `READ_ONLY`
* `READ_WRITE`
* `NONSTRICT_READ_WRITE`

The `TRANSACTIONAL` strategy is not supported. If you set `hibernate.cache.ignite.default_access_type` to `TRANSACTIONAL`, the `SessionFactory` fails to start.

Declare the strategy on each cached entity or collection with the standard Hibernate annotations:

```java
import jakarta.persistence.Cacheable;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import org.hibernate.annotations.Cache;
import org.hibernate.annotations.CacheConcurrencyStrategy;

@Entity
@Cacheable
@Cache(usage = CacheConcurrencyStrategy.READ_WRITE)
public class User {
    @Id
    private Long id;

    private String name;

    // Constructors, getters, and setters.
}
```

## Mapping Regions to GridGain Caches

Hibernate stores cached data in regions. The region factory backs each region with a GridGain cache:

* An entity is cached in a region named after the fully qualified entity class name, for example `com.example.User`, unless you set a region explicitly with `@Cache(region = "...")`.
* Query results and update timestamps are cached in their own regions when the query cache is enabled.

By default, the GridGain cache has the same name as the region, with the optional `cache_name_prefix` in front of it. To use a different cache, map the region with the `hibernate.cache.ignite.region.<region-name>` property:

```properties
hibernate.cache.ignite.cache_name_prefix = hib_
hibernate.cache.ignite.region.com.example.User = user-cache
```

In this example, the `com.example.User` entity is cached in the `hib_user-cache` GridGain cache.

If a cache with the resulting name does not exist, the region factory creates it with the default cache configuration. To control backups, the atomicity mode, expiration, or other cache settings, define the caches in the node configuration with the same names:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="igniteInstanceName" value="hibernate-grid"/>
    <property name="clientMode" value="true"/>

    <property name="cacheConfiguration">
        <list>
            <bean class="org.apache.ignite.configuration.CacheConfiguration">
                <property name="name" value="hib_user-cache"/>
                <property name="cacheMode" value="PARTITIONED"/>
                <property name="backups" value="1"/>
            </bean>
        </list>
    </property>

    <!-- Discovery and other settings. -->
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration()
    .setIgniteInstanceName("hibernate-grid")
    .setClientMode(true)
    .setCacheConfiguration(new CacheConfiguration<>("hib_user-cache")
        .setCacheMode(CacheMode.PARTITIONED)
        .setBackups(1));

// Start the node before you build the Hibernate SessionFactory.
Ignite ignite = Ignition.start(cfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

For more information about cache settings, see [Cache Configuration](../gridgain8-development/configuring-caches/configuration-overview.md).
