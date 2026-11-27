---
description: >-
  Create tables, zones, and indexes directly from Java POJOs using the GridGain 9
  catalog API, with annotation-based and builder-based examples.
---

# Creating Tables from Java Classes

## Overview

While [SQL DDL](../reference/sql/ddl.md) supports a comprehensive set of table manipulation commands, you can also create tables and build indexes directly from a POJO using a simple Java API.

This API supports custom annotations and simple builders; it works seamlessly with the Mapper interface, thus facilitating [KeyValueView and RecordView](table-api.md).

{% hint style="info" %}
The Java examples on this page use the thin client, which requires the `ignite-client` module. For repository and dependency configuration, see [Project Setup and Required Modules](project-setup.md).
{% endhint %}

The Java API lets you perform the following operations:

- CREATE ZONE
- CREATE TABLE
- CREATE INDEX
- DROP ZONE
- DROP TABLE
- DROP INDEX
- CREATE SCHEMA
- DROP SCHEMA

Use the @Table and other annotations located in the `org.apache.ignite.catalog.annotations` package.

## Examples

### Key-Value POJO Compatible with KeyValueView

The example below creates a table called `kv_pojo` by using the POJO compatible with `KeyValueView`:

```java
@Table(value = "kv_pojo",
        zone = @Zone(value = "zone_test", replicas = 2, storageProfiles = "default"),
        colocateBy = {@ColumnRef("id"), @ColumnRef("id_str")},
        indexes = @Index(value = "ix", columns = {@ColumnRef("f_name"), @ColumnRef("l_name")}))

public static class PojoKey {
    @Id
    Integer id;

    @Id(SortOrder.DEFAULT)
    @Column(value = "id_str", length = 20)
    String idStr;

    public PojoKey(Integer id, String idStr) {
        this.id = id;
        this.idStr = idStr;
    }
}

public static class PojoValue {
    @Column("f_name")
    private String firstName;

    @Column("l_name")
    private String lastName;

    public PojoValue(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }
}

public static void main(String[] args) {

    System.out.println("\nConnecting to server...");

    try (IgniteClient client = IgniteClient.builder()
            .addresses("127.0.0.1:10800")
            .build()
    ) {

        org.apache.ignite.table.Table myTable = client.catalog().createTable(PojoKey.class, PojoValue.class);

        KeyValueView<PojoKey, PojoValue> kvView = myTable.keyValueView(PojoKey.class, PojoValue.class);
        PojoKey key = new PojoKey(1, "sample");
        PojoValue putValue = new PojoValue("John", "Smith");
        kvView.put(null, key, putValue);

        PojoValue getValue = kvView.get(null, key);
        System.out.println(
                "\nRetrieved values:\n"
                        + "    Account ID: " + key.id + '\n'
                        + "    First name: " + getValue.firstName + '\n'
                        + "    Last name" + getValue.lastName);

    }
}
```

{% hint style="info" %}
You need to create a [storage profile](../architecture/storage/README.md#creating-and-using-storage-profiles) in node configuration by using the CLI tool.
{% endhint %}

The result is equivalent to the following SQL multi-statement:

```sql
CREATE ZONE IF NOT EXISTS zone_test (PARTITIONS 2) STORAGE PROFILES['default'];

CREATE TABLE IF NOT EXISTS kv_pojo (
	id int,
	id_str varchar(20),
	f_name varchar,
	l_name varchar,
	str varchar,
	PRIMARY KEY (id, id_str)
)
COLOCATE BY (id, id_str)
WITH PRIMARY_ZONE='ZONE';

CREATE INDEX ix (f_name, l_name desc nulls last);
```

### Single POJO Compatible with RecordView

The example below creates the `pojo_sample` table by using the POJO compatible with `RecordView`:

```java
@Table(value = "pojo_sample",
        zone = @Zone(value = "zone_test", replicas = 2, storageProfiles = "default"),
        colocateBy = {@ColumnRef("id"), @ColumnRef("id_str")},
        indexes = @Index(value = "ix_sample", columns = {@ColumnRef("f_name"), @ColumnRef("l_name")}))

public static class Pojo {
    @Id
    Integer id;

    @Id(SortOrder.DEFAULT)
    @Column(value = "id_str", length = 20)
    String idStr;

    @Column("f_name")
    String firstName;

    @Column("l_name")
    String lastName;

    String str;
}

public static void main(String[] args) {

    System.out.println("\nConnecting to server...");

    try (IgniteClient client = IgniteClient.builder()
            .addresses("127.0.0.1:10800")
            .build()
    ) {

        org.apache.ignite.table.Table myTable = client.catalog().createTable(Pojo.class);

        RecordView<Tuple> view = myTable.recordView();
        Tuple insertTuple = Tuple.create()
                .set("id", 1)
                .set("id_str", "sample")
                .set("f_name", "John")
                .set("l_name", "Smith");
        view.insert(null, insertTuple);

        Tuple getTuple = view.get(null, insertTuple);
        System.out.println(
                "\nRetrieved record: " +
                        getTuple.stringValue("f_name")
        );
    }
}
```

### The Builder Alternative to the @Table Annotation

The example below uses a builder to create a table instead on creating it from a Java class:

{% hint style="info" %}
When using builders, only the `@Id` and `@Column` annotations on fields are supported.
{% endhint %}

```java
IgniteCatalog catalog = client.catalog();

catalog.createTable(
        TableDefinition.builder("sampleTable3")
                .primaryKey("myKey")
                .columns(
                        column("myKey", ColumnType.INT32),
                        column("myValue", ColumnType.VARCHAR)
                )
                .build()
);

Table myTable = client.tables().table("sampleTable3");
myTable.keyValueView().put(null, Tuple.create().set("myKey", 1), Tuple.create().set("myValue", "John"));

Tuple value = myTable.keyValueView().get(null, Tuple.create().set("myKey", 1));
System.out.println(
        "\nRetrieved value:\n" +
        value.stringValue("myValue")
);
```

## Partition Function

To set the [partition function](../architecture/storage/data-partitioning.md#available-partition-functions) of a table, use the `partitionFunction` attribute of the `@Table` annotation or the `partitionFunction` method of `TableDefinition.Builder`. The available functions are defined in the `org.apache.ignite.catalog.PartitionFunction` enum. To use a function other than the default, you must also set the colocation key with `colocateBy`. For guidance on when to use `MODULO`, see [Choosing a Partition Function](../architecture/storage/data-partitioning.md#choosing-a-partition-function).

The example below creates the `Warehouse` table by using the `@Table` annotation. If the `warehouseZone` zone does not exist, it is created with 16 partitions. If the zone already exists, its number of partitions does not change:

```java
@Table(
        value = "Warehouse",
        colocateBy = @ColumnRef("w_id"),
        partitionFunction = PartitionFunction.MODULO,
        zone = @Zone(value = "warehouseZone", partitions = 16, storageProfiles = "default")
)
public class WarehouseRecord {
    @Id
    @Column("w_id")
    Integer warehouseId;

    @Column
    String name;
}

client.catalog().createTable(WarehouseRecord.class);
```

The example below creates the same table by using the builder. With the builder, the `warehouseZone` zone must already exist:

```java
client.catalog().createTable(
        TableDefinition.builder("Warehouse")
                .columns(
                        column("w_id", ColumnType.INT32),
                        column("name", ColumnType.VARCHAR)
                )
                .primaryKey("w_id")
                .colocateBy("w_id")
                .partitionFunction(PartitionFunction.MODULO)
                .zone("warehouseZone")
                .build()
);
```

{% hint style="warning" %}
Servers of versions earlier than GridGain 9.2 support only the default partition function. If you create a table with a different function on such a server, the operation fails with a parse error.
{% endhint %}

To get the partition function of an existing table, use the `tableDefinition` method of `IgniteCatalog`:

```java
TableDefinition warehouse = client.catalog().tableDefinition("Warehouse");

PartitionFunction function = warehouse.partitionFunction(); // MODULO
```

The value returned by `partitionFunction` depends on how you got the `TableDefinition` object:

- If the object was returned by `tableDefinition`, the value is the partition function of the existing table. If the client is connected to a server of a version earlier than GridGain 9.2, the value is `null`, because such servers do not report the partition function.
- If you created the object with the builder, the value is the function you set, or `null` if you did not set one.

Caches work the same way. Use the `partitionFunction` attribute of the `@Cache` annotation, the `partitionFunction` method of `CacheDefinition.Builder`, and the `cacheDefinition` method of `IgniteCatalog`.

## Rack Awareness

To spread the replicas of a zone across [fault domains](../architecture/storage/distribution-zones.md#rack-awareness), set the name of the node attribute that defines the fault domains. Use the `replicaFilterAttribute` attribute of the `@Zone` annotation or the `replicaFilterAttribute` method of `ZoneDefinition.Builder`.

The example below creates the `rack_pojo` table by using the `@Table` annotation. If the `zone_rack` zone does not exist, it is created with 3 replicas of each partition, spread across the fault domains defined by the `rack` node attribute:

```java
@Table(value = "rack_pojo",
        zone = @Zone(value = "zone_rack", replicas = 3, replicaFilterAttribute = "rack", storageProfiles = "default"))
public static class PojoValue {
    // Table columns.
}
```

The example below creates the same zone by using the builder:

```java
client.catalog().createZone(
        ZoneDefinition.builder("zone_rack")
                .replicas(3)
                .replicaFilterAttribute("rack")
                .storageProfiles("default")
                .build()
);
```

{% hint style="warning" %}
Servers of versions earlier than GridGain 9.2 do not support the replica filter attribute. If you create a zone with this attribute on such a server, the operation fails with a parse error.
{% endhint %}

To get the replica filter attribute of an existing zone, use the `zoneDefinition` method of `IgniteCatalog`:

```java
ZoneDefinition zone = client.catalog().zoneDefinition("zone_rack");

String attribute = zone.replicaFilterAttribute(); // rack
```

If the zone does not use fault domains, or the client is connected to a server of a version earlier than GridGain 9.2, the value is `null`.

## Next Steps

Once you have created a table using the Java API, you can manipulate it using the [SQL commands](../reference/sql/ddl.md).

## See Also

- [Implement Schema With Java Annotations](../gridgain9-get-started/learning-paths/schema-design-for-distributed-sql/schema-java-annotations.md)

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
