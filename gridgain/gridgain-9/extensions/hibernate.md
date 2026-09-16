---
description: >-
  Use GridGain 9 with Hibernate as a query database and a second-level (L2)
  cache provider — installation, dialect configuration, entities, and cache
  concurrency strategies.
---

# GridGain With Hibernate

{% hint style="warning" %}
This is an experimental API. It can change significantly in later releases.
{% endhint %}

GridGain provides [Hibernate](https://hibernate.org/) integration that lets you use GridGain 9 as both a query database (via JDBC and a custom SQL dialect) and a Hibernate second-level (L2) cache provider.

## Prerequisites

- Java 21 or later
- Hibernate 6.1.7 or later
  {% hint style="info" %}
  The integration uses `jakarta.persistence`, not `javax.persistence`. Update entity imports accordingly when migrating from Hibernate 5.x.
  {% endhint %}
- GridGain 9.1.23 or later
- [GridGain JDBC Driver](https://www.gridgain.com/tryfree) for the same GridGain version
- Entity tables must already exist in GridGain. The dialect does not auto-create entity tables; only the L2 cache table is created automatically. See [Configuring Second-Level Cache](#configuring-second-level-cache) for more information.

## Installation

The integration ships as a single artifact, `org.gridgain:gridgain-hibernate`, that contains both the SQL dialect and the L2 region factory. Add it to your project together with Hibernate Core and the GridGain JDBC driver:

{% code title="pom.xml" %}
```xml
<repositories>
    <repository>
        <id>GridGain External Repository</id>
        <url>https://www.gridgainsystems.com/nexus/content/repositories/external</url>
    </repository>
</repositories>

<dependencies>
    <!-- Hibernate Core (6.1.x) -->
    <dependency>
        <groupId>org.hibernate.orm</groupId>
        <artifactId>hibernate-core</artifactId>
        <version>6.1.7.Final</version>
    </dependency>

    <!-- GridGain JDBC Driver -->
    <dependency>
        <groupId>org.gridgain</groupId>
        <artifactId>ignite-jdbc</artifactId>
        <version>9.1</version>
    </dependency>

    <!-- GridGain Hibernate Integration (dialect + L2 region factory) -->
    <dependency>
        <groupId>org.gridgain</groupId>
        <artifactId>gridgain-hibernate</artifactId>
        <version>9.1</version>
    </dependency>
</dependencies>
```
{% endcode %}

## Configuration

### Basic Configuration

Configure Hibernate to use GridGain through the `hibernate.cfg.xml` configuration file:

{% code title="hibernate.cfg.xml" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<hibernate-configuration>
    <session-factory>
        <!-- JDBC Connection Settings -->
        <property name="hibernate.connection.driver_class">
            org.apache.ignite.jdbc.IgniteJdbcDriver
        </property>
        <property name="hibernate.connection.url">
            jdbc:ignite:thin://127.0.0.1:10800/PUBLIC
        </property>

        <!-- GridGain Dialect -->
        <property name="hibernate.dialect">
            org.gridgain.hibernate.GridGain9Dialect
        </property>

        <!-- Schema used by GridGain Tables -->
        <property name="hibernate.default_schema">PUBLIC</property>

        <!-- Session Context -->
        <property name="hibernate.current_session_context_class">thread</property>
    </session-factory>
</hibernate-configuration>
```
{% endcode %}

### Configuration Properties

The following Hibernate properties are used to configure GridGain integration:

|Property|Required|Description|
|---|---|---|
|hibernate.connection.driver_class|Yes|JDBC driver class. Must be set to `org.apache.ignite.jdbc.IgniteJdbcDriver`.|
|hibernate.connection.url|Yes|JDBC connection URL to GridGain cluster. Format: `jdbc:ignite:thin://host:port/schema`. For available JDBC URL parameters, see [JDBC Driver documentation](../developers-guide/clients/jdbc-driver.md).|
|hibernate.dialect|Yes|SQL dialect for GridGain. Must be set to `org.gridgain.hibernate.GridGain9Dialect`.|
|hibernate.default_schema|No|Default schema for database operations. If not specified, `PUBLIC` schema is used.|
|hibernate.current_session_context_class|No|Session context management strategy. Common values: `thread` (thread-bound sessions), `jta` (JTA transactions). If not specified, sessions must be managed manually.|
|hibernate.connection.username|No|Username for cluster authentication. Required only if authentication is enabled on the cluster.|
|hibernate.connection.password|No|Password for cluster authentication. Required only if authentication is enabled on the cluster.|

## Defining Entities

Define entity classes with standard JPA annotations from the `jakarta.persistence` package. Enable second-level caching per entity with Hibernate's `@Cache` annotation:

{% code title="Item.java" %}
```java
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

import org.hibernate.annotations.Cache;
import org.hibernate.annotations.CacheConcurrencyStrategy;

@Entity(name = "Item")
@Table(name = "Item")
@Cache(usage = CacheConcurrencyStrategy.READ_WRITE, region = "item")
public class Item {

    @Id
    @Column(name = "item_id")
    private int itemId;

    @Column(name = "item_name")
    private String name;

    @Column(name = "item_price")
    private double price;

    public Item() {}

    public int getItemId() {
        return itemId;
    }

    public void setItemId(int itemId) {
        this.itemId = itemId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }
}
```
{% endcode %}

The corresponding entity table must already exist in GridGain. The following SQL creates the table for the entity above:

```sql
CREATE TABLE IF NOT EXISTS Item (
    item_id    INT PRIMARY KEY,
    item_name  VARCHAR,
    item_price DOUBLE
);
```

The `region` attribute on `@Cache` is the L2 cache region name; it is independent of the entity's `@Table` name and can be any stable string.

### Supported Column Types

The dialect maps the following JDBC types to GridGain SQL types:

|JDBC Type|GridGain SQL Type|
|---|---|
|`BIGINT`|`bigint`|
|`SMALLINT`|`smallint`|
|`TINYINT`|`tinyint`|
|`INTEGER`|`integer`|
|`DECIMAL`|`decimal`|
|`FLOAT`|`float`|
|`DOUBLE`|`double precision`|
|`BOOLEAN`|`boolean`|
|`CHAR`, `VARCHAR`|`varchar($l)`|
|`DATE`|`date`|
|`TIME`|`time`|
|`TIMESTAMP`|`timestamp`|
|`BINARY`, `VARBINARY`, `LONGVARBINARY`, `BLOB`|`varbinary($l)`|

JDBC types not listed above fall back to Hibernate's generic mapping, which emits SQL keywords that the GridGain SQL engine may not accept. The following types in particular are unlikely to work and should be avoided:

- LOB types: `CLOB`, `NCLOB`.
- National (wide-character) types: `NCHAR`, `NVARCHAR`, `LONGNVARCHAR`.
- Time-zone-aware datetime types: `TIMESTAMP WITH TIME ZONE`, `TIME WITH TIME ZONE`.
- Structured types: `ARRAY`, `STRUCT`, `REF`, `JAVA_OBJECT`, `SQLXML`, `ROWID`.

For text columns, use `VARCHAR`. For binary or serialized payloads, use `VARBINARY`. For values that need time-zone semantics, store the offset alongside a `TIMESTAMP` and apply the conversion in application code.

## Configuring Second-Level Cache

### Enabling L2 Cache

To enable GridGain-backed second-level cache, add the following configuration to your `hibernate.cfg.xml`:

{% code title="hibernate.cfg.xml" %}
```xml
<hibernate-configuration>
    <session-factory>
        <!-- ... other properties ... -->

        <!-- L2 Cache Configuration -->
        <property name="hibernate.cache.region.factory_class">
            org.gridgain.hibernate.cache.GridGainJdbcRegionFactory
        </property>

        <!-- Enable second-level cache and query cache -->
        <property name="hibernate.cache.use_second_level_cache">true</property>
        <property name="hibernate.cache.use_query_cache">true</property>
    </session-factory>
</hibernate-configuration>
```
{% endcode %}

`GridGainJdbcRegionFactory` reuses the same `hibernate.connection.*` properties listed in [Configuration Properties](#configuration-properties) to connect to the cluster. When the `SessionFactory` is initialized, the factory issues `CREATE TABLE IF NOT EXISTS HIBERNATE_L2_CACHE (...)` over a JDBC connection.

The statement is unqualified, so the table is created in the schema the JDBC URL resolves to — not in `hibernate.default_schema`. The connecting user must be allowed to create tables in that schema. Because of `IF NOT EXISTS`, restarts are idempotent and existing cache entries are preserved.

The table is created in the cluster's default zone with the default storage profile; the factory provides no override. To use a non-default zone or storage profile, create the table manually with the layout shown below before starting Hibernate.

The table has the following layout:

|Column|Type|Description|
|---|---|---|
|region|VARCHAR (NOT NULL, part of primary key)|Name of the cache region (for example, the entity region name or a query cache region).|
|cache_key|VARBINARY (NOT NULL, part of primary key)|Serialized cache key.|
|cache_val|VARBINARY (nullable)|Serialized cached value (entity data or query results).|

The primary key is the composite `(region, cache_key)`. Entries are written by deleting any existing row for the key and inserting the new row, so writes are idempotent within a single region.

### Cache Concurrency Strategies

`GridGainJdbcRegionFactory` is built on Hibernate's non-transactional region-factory template and supports the following cache concurrency strategies:

|Strategy|Description|
|---|---|
|READ_ONLY|For entities that never change after they are created. Provides the best performance.|
|NONSTRICT_READ_WRITE|For entities that are updated infrequently. Does not guarantee strict consistency between the cache and the database.|
|READ_WRITE|For entities that are updated more frequently. Provides strict consistency via soft locks, at the additional cost of write coordination.|

{% hint style="info" %}
The `TRANSACTIONAL` strategy is not supported by this region factory.
{% endhint %}

The example below shows how to configure a concurrency strategy on an entity:

{% code title="Java" %}
```java
@Entity
@Table(name = "Product")
@Cache(usage = CacheConcurrencyStrategy.READ_WRITE, region = "products")
public class Product {
    @Id
    private Long id;

    private String name;
    private BigDecimal price;

    // Getters and setters
}
```
{% endcode %}

## Using Hibernate with GridGain

Once Hibernate is configured, use it the same way you would with any other JDBC database:

{% code title="Java" %}
```java
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

public class HibernateExample {

    public static void main(String[] args) {
        try (SessionFactory sessionFactory = new Configuration()
                .configure()
                .addAnnotatedClass(Item.class)
                .buildSessionFactory();
             Session session = sessionFactory.openSession()) {

            Transaction tx = session.beginTransaction();
            try {
                // First load goes to the database and populates L1 + L2 caches.
                Item item = session.get(Item.class, 1);
                System.out.println("Name: " + item.getName());

                // Second load in the same session is served from the L1 cache.
                Item itemCached = session.get(Item.class, 1);

                // Evict from the L1 cache so the next read consults L2.
                session.evict(item);

                // Third load is served from the L2 cache (HIBERNATE_L2_CACHE table).
                Item itemFromL2 = session.get(Item.class, 1);

                tx.commit();
            } catch (RuntimeException e) {
                tx.rollback();
                throw e;
            }
        }
    }
}
```
{% endcode %}
