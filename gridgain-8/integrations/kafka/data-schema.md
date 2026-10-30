---
description: >-
  Explains how GridGain Kafka Connectors map Ignite types to Kafka schema types, and how they handle updates, removals, schema migration, schemaless operation, schema caching, and nullability.
---

# Kafka Connector Data Schema

GridGain Kafka Connectors support data schemas. This enables numerous existing non-Ignite Sink Connectors to understand data injected with Ignite Source Connector and the Ignite Sink Connector to understand data injected by non-Ignite Source Connectors.

## Ignite Type Support

Source and Sink Connectors work with Ignite data in Ignite Binary format.

The table below provides mappings between Java Ignite types and Kafka Schema types and Logical types

| Java Type / Ignite Type | Kafka Type | Examples and Notes |
|---|---|---|
| byte (Byte) | INT8 | |
| short (Short) | INT16 | |
| int (INT) | INT32 | |
| char (CHAR) | INT32 | |
| long (LONG) | INT64 | |
| float (FLOAT) | FLOAT32 | |
| double (DOUBLE) | FLOAT64 | |
| boolean (BOOL) | BOOLEAN | |
| String (STR) | STRING | |
| Class<?> (CLASS) | STRING | Same as `Class.getName()`. |
| UUID | STRING | |
| enum (ENUM) | INT32 | Same as `enumPolicy.ORDINAL`. |
| enum (ENUM) | STRING | Same as `enumPolicy.SHORT_NAME`,`enumPolicy.LONG_NAME` and `enumPolicy.FULL_NAME`. |
| java.util.Date (DATE) | [TIMESTAMP](https://docs.confluent.io/platform/current/connect/javadocs/javadoc/org/apache/kafka/connect/data/Timestamp.html) | |
| java.sql.Date (OBJ) | [DATE](https://docs.confluent.io/platform/current/connect/javadocs/javadoc/org/apache/kafka/connect/data/Date.html) | Kafka expects that time part (HH:mm:ss:ms) of Date instance is set to 0. |
| java.sql.Time (TIME) | [TIME](https://docs.confluent.io/platform/current/connect/javadocs/javadoc/org/apache/kafka/connect/data/Time.html) | Kafka expects that date part (DD:MM:YYYY) of Time instance is set to 0. |
| java.sql.Timestamp (TIMESTAMP) | [TIMESTAMP](https://docs.confluent.io/platform/current/connect/javadocs/javadoc/org/apache/kafka/connect/data/Timestamp.html) | |
| BigDecimal (DECIMAL) | [DECIMAL](https://docs.confluent.io/platform/current/connect/javadocs/javadoc/org/apache/kafka/connect/data/Decimal.html) | |
| byte[] (BYTE_ARR) | BYTES | |
| Map<K,V> (MAP) | MAP (KV_schema) | The schemas of maps are inferred from first `map_entry` or `array_element`.<br>Heterogeneous collections/maps (e.g.`[1, «foo», 42.0]`) can trigger `DataException`. |
| Collection<V> (COL) | ARRAY (element_schema) | The schemas of collection(array) are inferred from first `map_entry` or `array_element`.<br>Heterogeneous collections/maps (e.g.`[1, «foo», 42.0]`) can trigger `DataException`. |
| V[] (SHORT_ARR INT_ARR LONG_ARR FLOAT_ARR DOUBLE_ARR CHAR_ARR BOOLEAN_ARR DECIMAL_ARR STRING_ARR UUID_ARR DATE_ARR OBJ_ARR ENUM_ARR TIME_ARR DATE_ARR TIMESTAMP_ARR DECIMAL_ARR) | ARRAY (element_schema) | The schemas of collection(array) are inferred from first `map_entry` or `array_element`.<br>Heterogeneous collections/maps (e.g.`[1, «foo», 42.0]`) can trigger `DataException`. |
| Pojo (OBJ) | STRUCT | |

{% hint style="warning" %}
**Java Annotations Based Configuration Is Lost**

GridGain Kafka Connectors do not import and export field information specified via Java annotations. For example, annotation-based configuration of Affinity keys, SQL queryable fields, and indices does not exist in Kafka.
Use a configuration-based approach to specify such information for the sink caches.
{% endhint %}

## Updates and Removals

By default, Source Connector does not process removed Ignite cache entries. Set the `shallProcessRemovals` configuration setting to `true` to make the Source Connector process removals. In this case Source Connector injects a record with `null` value into Kafka to indicate that the key was removed. Sink Connector removes keys with `null` values from the cache. Using `null` as a value to indicate a removed entry works because Ignite does not support `null` cache values.

For performance reasons, Sink Connector does not support existing cache entry update by default. Set `shallProcessUpdates` configuration setting to `true` to make the Sink Connector update existing entries.

## Schema Migration

Schema migration is implicit for GridGain Connectors. Both the Source and Sink Connectors pull and push cache entries in cross-platform Ignite Binary format, which intrinsically supports changing schemas. Ignite cache keys and values are dynamic objects that could have a different set of fields.

For performance reasons, Source connector reuses key and values schemas that are created when the first cache entry is pulled. If it is expected that key or value schema could be changed over time, consider setting `isSchemaDynamic` to `true`.

## Schemaless Operation

Source Connector does not generate schemas if the `isSchemaless` configuration setting is `true`.

Disabling schemas improves performance because the Connectors would not build schemas and would not convert keys and values into Kafka format. This comes at a cost of non-Ignite Sink converters unable to understand the data injected into Kafka in the Ignite Binary format.

Some examples when disabling Source schema makes sense:

- You are ready to do some coding to extend a non-Ignite converter to process the Ignite Binary objects to achieve higher performance.
- The [Ignite Data Replication](example-data-replication.md) example does not need schemas since both the Source and Sink are GridGain connectors.

## Schema Caching

GridGain connector has a feature for caching Kafka schemas of already resolved binary objects. This can be extremely useful in case if same cache stores objects with different binary types.

For example, let us assume that caches stores 2 types of objects: **A** and **B**. A stream of objects that were pulled by connector from the cache might look like this:
**A<sub>1</sub>  B<sub>1</sub>  A<sub>2</sub>  A<sub>3</sub>  A<sub>4</sub>  B<sub>2</sub>  B<sub>3</sub>  ...**. With the default settings, the connector will infer initial Kafka schema from **A<sub>1</sub>** and try to apply it for all subsequent **B<sub>1..3</sub>** objects. This will lead to errors. As described above, you must set the `isSchemaDynamic=true` property to get correct results, this option forces the connector to perform schema resolution for each incoming object. Performing schema resolution each time is not a cheap process from performance perspective, so we can improve it by enabling schema caching with the `enableSchemaCache=true` property. After that, the connector will resolve kafka schemas only during first encounter of object with unknown type, for example:

- Kafka schema for type **A** will be calculated during A<sub>1</sub> processing and reused for **A<sub>2</sub>  A<sub>3</sub>  A<sub>4</sub> … A<sub>x</sub>**
- Kafka schema for type **B** will be calculated during B<sub>1</sub> processing and reused for **B<sub>2</sub>  B<sub>3</sub> … B<sub>x</sub>**

When caching is enabled, the connector is still able to detect simple changes in binary types, like appearance of new field, but it cannot detect changes in inner composite types. For example let us assume that type **A** has field of type **C**.

```java
public class A {
    C foo;
}

public class C {
    String f1;
}
```

If Kafka schema for type A was already resolved, but instance of class **C**, that is stored in field foo of new incoming object **A<sub>x</sub>**, contains new field **f2**, connector will not detect it because binary schema of type **A** was not changed.

## Nullability

Kafka Connect always requires that you provide a type schema for provided data. GridGain connector can infer proper kafka schema for fields of scalar types or other known logical types (date, time, decimal), but it is not always possible for complex objects or collections. For example, if you have an object `obj` of composite type `T1` with field `foo = null`:

```java
public class T1 {
    T2 foo = null;
}
```

While processing binary representation of `obj`, GridGain Connector will not be able to infer `obj.foo` type, because it does not have a binary instance of T2 that it can use for schema resolution. Similar case happens when some field is supposed to store a generic collection like `List<Person>`. If collection value is `null`, the collection is empty or collection consists of nulls only, we will not be able to infer the type of collection elements as well.

To work around this obstacle, GridGain Connector introduces a special `fieldNullabilityPolicy` option with the followingmodes:

- **LAZY** mode, connector will simply skip nullable fields, so they will not be a part of either kafka schema or kafka connect record. This is same behavior that the connector had prior to the appearance of this policy (ver < 8.9.8).
- **EAGER** mode will force the GridGain connector to do its best to infer Kafka schema of nullable field. In case if it is not possible to successfully complete schema resolution  `STRUCT(name=o.g.k.c.s.undef)` placeholder will be used.

{% hint style="warning" %}
Consider disabling schema cache (`enableSchemaCache=false`) if you cannot guarantee that the first occurrence of particular binary type instance does not have nullable fields. Otherwise, the connector will cache a partially populated schema, where some nullable fields have a `STRUCT(name=o.g.k.c.s.undef)` placeholder, and reuse it even for subsequent entries that do not have nullable fields.
{% endhint %}
