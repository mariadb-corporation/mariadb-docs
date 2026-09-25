---
description: >-
  Define GridGain SQL indexes and queryable fields using annotations or query entities, configure group indexes, inline size, and custom keys.
---

# Defining Indexes

In addition to common DDL commands, such as CREATE/DROP INDEX, developers can use GridGain's [SQL APIs](sql-api.md) to define indexes.

{% hint style="info" %}
Indexing capabilities are provided by the 'ignite-indexing' module. If you start GridGain from Java code, [add this module to your classpath](../setup.md#enabling-modules).
{% endhint %}

GridGain automatically creates indexes for each primary key and affinity key field.
When you define an index on a field in the value object, GridGain will create a composite index consisting of the indexed field and the cache's primary key.
In SQL terms, it means that the index will be composed of two columns: the column you want to index and the primary key column.

## Configuring Indexes Using Annotations

Indexes, as well as queryable fields, can be configured from code via the `@QuerySqlField` annotation. In the example below, the GridGain SQL engine will create indexes for the `id` and `salary` fields.

{% tabs %}
{% tab title="Java" %}
```java
public class Person implements Serializable {
    /** Indexed field. Will be visible to the SQL engine. */
    @QuerySqlField(index = true)
    private long id;

    /** Queryable field. Will be visible to the SQL engine. */
    @QuerySqlField
    private String name;

    /** Will NOT be visible to the SQL engine. */
    private int age;

    /**
     * Indexed field sorted in descending order. Will be visible to the SQL engine.
     */
    @QuerySqlField(index = true, descending = true)
    private float salary;
}
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
class Person
{
    // Indexed field. Will be visible to the SQL engine.
    [QuerySqlField(IsIndexed = true)] public long Id;

    //Queryable field. Will be visible to the SQL engine
    [QuerySqlField] public string Name;

    //Will NOT be visible to the SQL engine.
    public int Age;

    /** Indexed field sorted in descending order.
      * Will be visible to the SQL engine. */
    [QuerySqlField(IsIndexed = true, IsDescending = true)]
    public float Salary;
}
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

The type name is used as the table name in SQL queries. In this case, our table name will be `Person` (schema name usage and definition is explained in the [Schemas](schemas.md) section).

Both `id` and `salary` are indexed fields. `id` will be sorted in ascending order (default) and `salary` in descending order.

If you do not want to index a field, but you still need to use it in SQL queries, then the field must be annotated without the `index = true` parameter.
Such a field is called a _queryable field_.
In the example above, `name` is defined as a [queryable field](sql-api.md#configuring-queryable-fields).

The `age` field is neither queryable nor is it an indexed field, and thus it will not be accessible from SQL queries.

When you define the indexed fields, you need to [register indexed types](#registering-indexed-types).

{% hint style="info" %}
**Updating Indexes and Queryable Fields at Runtime**

Use the [CREATE/DROP INDEX](../../reference/sql/ddl.md#create-index) commands if you need to manage indexes or make an object's new fields visible to the SQL engine at​ runtime.
{% endhint %}

### Indexing Nested Objects with Annotations

Fields of nested objects can also be indexed and queried using annotations. For example, consider a `Person` object that has an `Address` object as a field:

```java
public class Person {
    /** Indexed field. Will be visible for SQL engine. */
    @QuerySqlField(index = true)
    private long id;

    /** Queryable field. Will be visible for SQL engine. */
    @QuerySqlField
    private String name;

    /** Will NOT be visible for SQL engine. */
    private int age;

    /** Indexed field. Will be visible for SQL engine. */
    @QuerySqlField(index = true)
    private Address address;
}
```

Where the structure of the `Address` class might look like:

```java
public class Address {
    /** Indexed field. Will be visible for SQL engine. */
    @QuerySqlField (index = true)
    private String street;

    /** Indexed field. Will be visible for SQL engine. */
    @QuerySqlField(index = true)
    private int zip;
}
```

In the above example, the `@QuerySqlField(index = true)` annotation is specified on all the fields of the `Address` class, as well as the `Address` object in the `Person` class.

This makes it possible to execute SQL queries like the following:

```java
QueryCursor<List<?>> cursor = personCache.query(new SqlFieldsQuery(
  "select * from Person where street = 'street1'"));
```

Note that you do not need to specify `address.street` in the WHERE clause of the SQL query. This is because the fields of the `Address` class are flattened within the `Person` table which simply allows us to access the `Address` fields in the queries directly.

{% hint style="warning" %}
If you create indexes for nested objects, you won't be able to run UPDATE or INSERT statements on the table.
{% endhint %}

### Registering Indexed Types

After indexed and queryable fields are defined, they have to be registered in the SQL engine along with the object types they belong to.

To specify which types should be indexed, pass the corresponding key-value pairs in the `CacheConfiguration.setIndexedTypes()` method as shown in the example below.

{% tabs %}
{% tab title="Java" %}
```java
// Preparing configuration.
CacheConfiguration<Long, Person> ccfg = new CacheConfiguration<>();

// Registering indexed type.
ccfg.setIndexedTypes(Long.class, Person.class);
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var ccfg = new CacheConfiguration
{
    QueryEntities = new[]
    {
        new QueryEntity(typeof(long), typeof(Person))
    }
};
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

This method accepts only pairs of types: one for key class and another for value class. Primitives are passed as boxed types.

{% hint style="info" %}
**Predefined Fields**

In addition to all the fields marked with a `@QuerySqlField` annotation, each table will have two special predefined fields: `_key` and `_val`, which represent links to whole key and value objects. This is useful, for instance, when one of them is of a primitive type and you want to filter by its value. To do this, run a query like: `SELECT * FROM Person WHERE _key = 100`.
{% endhint %}

{% hint style="info" %}
Since GridGain supports [Binary Objects](../key-value-api/binary-objects.md), there is no need to add classes of indexed types to the classpath of cluster nodes. The SQL query engine can detect values of indexed and queryable fields, avoiding object deserialization.
{% endhint %}

### Group Indexes

To set up a multi-field index that can accelerate queries with complex conditions, you can use a `@QuerySqlField.Group` annotation. You can add multiple `@QuerySqlField.Group` annotations in `orderedGroups` if you want a field to be a part of more than one group.

For instance, in the `Person` class below we have the field `age` which belongs to an indexed group named `age_salary_idx` with a group order of "0" and descending sort order. Also, in the same group, we have the field `salary` with a group order of "3" and ascending sort order. Furthermore, the field `salary` itself is a single column index (the `index = true` parameter is specified in addition to the `orderedGroups` declaration). Group `order` does not have to be a particular number. It is needed only to sort fields inside of a particular group.

{% tabs %}
{% tab title="Java" %}
```java
public class Person implements Serializable {
	/** Indexed in a group index with "salary". */
	@QuerySqlField(orderedGroups = { @QuerySqlField.Group(name = "age_salary_idx", order = 0, descending = true) })
	private int age;

	/** Indexed separately and in a group index with "age". */
	@QuerySqlField(index = true, orderedGroups = { @QuerySqlField.Group(name = "age_salary_idx", order = 3) })
	private double salary;
}
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
class Person
{
    [QuerySqlField(IndexGroups = new[] {"age_salary_idx"})]
    public int Age;

    [QuerySqlField(IsIndexed = true, IndexGroups = new[] {"age_salary_idx"})]
    public double Salary;
}
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Annotating a field with `@QuerySqlField.Group` outside of `@QuerySqlField(orderedGroups={...})` will have no effect.
{% endhint %}

## Configuring Indexes Using Query Entities

Indexes and queryable fields can also be configured via the `org.apache.ignite.cache.QueryEntity` class which is convenient for Spring XML based configuration.

{% hint style="info" %}
You can also set query entities using the [SQL API](sql-api.md#query-entities).
{% endhint %}

Most concepts that are discussed as part of the annotation-based configuration above are also valid for the `QueryEntity` based approach. 

{% hint style="info" %}
[Indexing Nested Objects with Query Entities](#indexing-nested-objects-with-query-entities) differs from  [Indexing Nested Objects with Annotations](#indexing-nested-objects-with-annotations).  
{% endhint %}

The types whose fields are configured with the `@QuerySqlField` annotation and are registered with the `CacheConfiguration.setIndexedTypes()` method are internally converted into query entities.

The example below shows how to define a single field index, group indexes, and queryable fields.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration" id="ignite.cfg">
    <property name="cacheConfiguration">
        <bean class="org.apache.ignite.configuration.CacheConfiguration">
            <property name="name" value="Person"/>
            <!-- Configure query entities -->
            <property name="queryEntities">
                <list>
                    <bean class="org.apache.ignite.cache.QueryEntity">
                        <!-- Setting  the type of the key -->
                        <property name="keyType" value="java.lang.Long"/>

                        <property name="keyFieldName" value="id"/>

                        <!-- Setting type of the value -->
                        <property name="valueType" value="org.apache.ignite.examples.Person"/>

                        <!-- Defining fields that will be either indexed or queryable.
                             Indexed fields are added to the 'indexes' list below.-->
                        <property name="fields">
                            <map>
                                <entry key="id" value="java.lang.Long"/>
                                <entry key="name" value="java.lang.String"/>
                                <entry key="salary" value="java.lang.Float "/>
                            </map>
                        </property>
                        <!-- Defining indexed fields.-->
                        <property name="indexes">
                            <list>
                                <!-- Single field (aka. column) index -->
                                <bean class="org.apache.ignite.cache.QueryIndex">
                                    <constructor-arg value="name"/>
                                </bean>
                                <!-- Group index. -->
                                <bean class="org.apache.ignite.cache.QueryIndex">
                                    <constructor-arg>
                                        <list>
                                            <value>id</value>
                                            <value>salary</value>
                                        </list>
                                    </constructor-arg>
                                    <constructor-arg value="SORTED"/>
                                </bean>
                            </list>
                        </property>
                    </bean>
                </list>
            </property>
        </bean>
    </property>
</bean>
```
{% endtab %}
{% tab title="Java" %}
```java
CacheConfiguration<Long, Person> cache = new CacheConfiguration<Long, Person>("myCache");

QueryEntity queryEntity = new QueryEntity();

queryEntity.setKeyFieldName("id").setKeyType(Long.class.getName()).setValueType(Person.class.getName());

LinkedHashMap<String, String> fields = new LinkedHashMap<>();
fields.put("id", "java.lang.Long");
fields.put("name", "java.lang.String");
fields.put("salary", "java.lang.Long");

queryEntity.setFields(fields);

queryEntity.setIndexes(Arrays.asList(new QueryIndex("name"),
        new QueryIndex(Arrays.asList("id", "salary"), QueryIndexType.SORTED)));

cache.setQueryEntities(Arrays.asList(queryEntity));
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var cacheCfg = new CacheConfiguration
{
    Name = "myCache",
    QueryEntities = new[]
    {
        new QueryEntity
        {
            KeyType = typeof(long),
            KeyFieldName = "id",
            ValueType = typeof(dotnet_helloworld.Person),
            Fields = new[]
            {
                new QueryField
                {
                    Name = "id",
                    FieldType = typeof(long)
                },
                new QueryField
                {
                    Name = "name",
                    FieldType = typeof(string)
                },
                new QueryField
                {
                    Name = "salary",
                    FieldType = typeof(long)
                },
            },
            Indexes = new[]
            {
                new QueryIndex("name"),
                new QueryIndex(false, QueryIndexType.Sorted, new[] {"id", "salary"})
            }
        }
    }
};
Ignition.Start(new IgniteConfiguration
{
    CacheConfiguration = new[] {cacheCfg}
});
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

A short name of the `valueType` is used as a table name in SQL queries. In this case, our table name will be `Person` (schema name usage and definition is explained on the [Schemas](schemas.md) page).

Once the `QueryEntity` is defined, you can execute the SQL query as follows:

```java
SqlFieldsQuery qry = new SqlFieldsQuery("SELECT id, name FROM Person" + "WHERE id > 1500 LIMIT 10");
```

{% hint style="info" %}
**Updating Indexes and Queryable Fields at Runtime**

Use the [CREATE/DROP INDEX](../../reference/sql/ddl.md#create-index) command if you need to manage indexes or make new fields of the object visible to the SQL engine at​ runtime.
{% endhint %}

### Indexing Nested Objects with Query Entities

Fields of nested objects can be indexed and queried using query entities. For example:

```java
public class Person {
    private long id;
    private String name;
    private int age;
    private Address address;
}
public class Address {
    private String street;
    private int zip;
}
```

We can index the street and zip from the address by doing the following.

```java
QueryEntity queryEntity = new QueryEntity();
queryEntity.setKeyFieldName("id").setKeyType(Long.class.getName()).setValueType(Person.class.getName());
LinkedHashMap<String, String> fields = new LinkedHashMap<>();
fields.put("id", "java.lang.Long");
fields.put("name", "java.lang.String");
fields.put("Address.street", "java.lang.String");
fields.put("Address.zip", "int");
queryEntity.setFields(fields);
queryEntity.setIndexes(Arrays.asList(new QueryIndex("name"), 
        new QueryIndex(Arrays.asList("id", "name"), QueryIndexType.SORTED)));
```

This makes it possible to execute SQL queries like the following:

```java
QueryCursor<List<?>> cursor = personCache.query(new SqlFieldsQuery(
  "select * from Person where street = 'street1'"));
```

## Creating Indexes Using SQL Command

Refer to the [CREATE INDEX](../../reference/sql/ddl.md#create-index) section.

## Configuring Index Inline Size

Proper index inline size can help speed up queries on indexed fields. Refer to the dedicated section in the [SQL Tuning guide](../../ha-and-performance/performance-tuning/sql-tuning.md#increasing-index-inline-size) for more information on how to choose a proper inline size for your situation. If there are any problems with index size, check logs to find out the reason.

By default, total length of all included fields is used. GridGain assumes the 10 bytes length for variable-length fields, such as strings or arrays, with length not specified.

You can change the default value by setting either:

- inline size for a specific index. To do this, use one of the methods below.
- `CacheConfiguration.sqlIndexMaxInlineSize` - limits size for all indexes within a given cache, Not used by default.
- `IGNITE_MAX_INDEX_PAYLOAD_SIZE` - system property limits inline size for all indexes in the cluster. Default value is 64 bytes.

The settings are applied in the order listed above. In all cases, the value is set in bytes.

{% hint style="info" %}
On every Nth PUT operation per index (N = `IGNITE_THROTTLE_INLINE_SIZE_CALCULATION`, default `1000`), GridGain computes how many bytes the row's indexed columns would need to be fully inlined and compares the result to the index's current inline size. If the natural size exceeds the configured inline size, a warning is logged recommending a larger inline size for that index. The throttle bounds the CPU cost of this check on hot write paths — lower values surface under-sized-index warnings sooner, higher values reduce per-PUT overhead.
{% endhint %}

You can also configure inline size for each index individually, which will overwrite the default value.
To set the index inline size for a user-defined index, use one of the following methods. In all cases, the value is set in bytes and cannot exceed 427 bytes.

- When using annotations:

  {% tabs %}
  {% tab title="Java" %}
  ```java
  @QuerySqlField(index = true, inlineSize = 13)
  private String country;
  ```
  {% endtab %}
  {% tab title="C#/.NET" %}
  ```csharp
  [QuerySqlField(IsIndexed = true, IndexInlineSize = 13)]
  public string Country { get; set; }
  ```
  {% endtab %}
  {% tab title="C++" %}
  unsupported
  {% endtab %}
  {% endtabs %}
- When using `QueryEntity`:

  {% tabs %}
  {% tab title="Java" %}
  ```java
  QueryIndex idx = new QueryIndex("country");
  idx.setInlineSize(13);
  queryEntity.setIndexes(Arrays.asList(idx));
  ```
  {% endtab %}
  {% tab title="C#/.NET" %}
  ```csharp
  var qe = new QueryEntity
  {
      Indexes = new[]
      {
          new QueryIndex
          {
              InlineSize = 13
          }
      }
  };
  ```
  {% endtab %}
  {% tab title="C++" %}
  unsupported
  {% endtab %}
  {% endtabs %}
- If you create indexes using the `CREATE INDEX` command, you can use the `INLINE_SIZE` option to set the inline size. See examples in the [corresponding section](../../reference/sql/ddl.md).

  ```sql
  create index country_idx on Person (country) INLINE_SIZE 13;
  ```

## Custom Keys

If you use only predefined SQL data types for primary keys, then you do not need to perform additional manipulation with the SQL schema configuration. Those data types are defined by the `GridQueryProcessor.SQL_TYPES` constant, as listed below.

Predefined SQL data types include:

- all the primitives and their wrappers except `char` and `Character`
- `String`
- `BigDecimal`
- `byte[]`
- `java.util.Date`, `java.sql.Date`, `java.sql.Timestamp`
- `java.util.UUID`

However, once you decide to introduce a custom complex key and refer to its fields from DML statements, you need to:

- Define those fields in the `QueryEntity` the same way as you set fields for the value object.
- Use the new configuration parameter `QueryEntity.setKeyFields(..)` to distinguish key fields from value fields.

The example below shows how to do this.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="cacheConfiguration">
        <bean class="org.apache.ignite.configuration.CacheConfiguration">
            <property name="name" value="personCache"/>
            <!-- Configure query entities -->
            <property name="queryEntities">
                <list>
                    <bean class="org.apache.ignite.cache.QueryEntity">
                        <!-- Registering key's class. -->
                        <property name="keyType" value="CustomKey"/>
                        <!-- Registering value's class. -->
                        <property name="valueType" value="org.apache.ignite.examples.Person"/>
                        <!-- Defining all the fields that will be accessible from DML. -->
                        <property name="fields">
                            <map>
                                <entry key="firstName" value="java.lang.String"/>
                                <entry key="lastName" value="java.lang.String"/>
                                <entry key="intKeyField" value="java.lang.Integer"/>
                                <entry key="strKeyField" value="java.lang.String"/>
                            </map>
                        </property>
                        <!-- Defining the subset of key's fields -->
                        <property name="keyFields">
                            <set>
                                <value>intKeyField</value>
                                <value>strKeyField</value>
                            </set>
                        </property>
                    </bean>
                </list>
            </property>
        </bean>
    </property>
    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <property name="ipFinder">
                <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                    <property name="addresses">
                        <list>
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
// Preparing cache configuration.
CacheConfiguration<Long, Person> cacheCfg = new CacheConfiguration<Long, Person>("personCache");

// Creating the query entity.
QueryEntity entity = new QueryEntity("CustomKey", "Person");

// Listing all the queryable fields.
LinkedHashMap<String, String> fields = new LinkedHashMap<>();

fields.put("intKeyField", Integer.class.getName());
fields.put("strKeyField", String.class.getName());

fields.put("firstName", String.class.getName());
fields.put("lastName", String.class.getName());

entity.setFields(fields);

// Listing a subset of the fields that belong to the key.
Set<String> keyFlds = new HashSet<>();

keyFlds.add("intKeyField");
keyFlds.add("strKeyField");

entity.setKeyFields(keyFlds);

// End of new settings, nothing else here is DML related

entity.setIndexes(Collections.<QueryIndex>emptyList());

cacheCfg.setQueryEntities(Collections.singletonList(entity));

ignite.createCache(cacheCfg);
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var ccfg = new CacheConfiguration
{
    Name = "personCache",
    QueryEntities = new[]
    {
        new QueryEntity
        {
            KeyTypeName = "CustomKey",
            ValueTypeName = "Person",
            Fields = new[]
            {
                new QueryField
                {
                    Name = "intKeyField",
                    FieldType = typeof(int),
                    IsKeyField = true
                },
                new QueryField
                {
                    Name = "strKeyField",
                    FieldType = typeof(string),
                    IsKeyField = true
                },
                new QueryField
                {
                    Name = "firstName",
                    FieldType = typeof(string)
                },
                new QueryField
                {
                    Name = "lastName",
                    FieldType = typeof(string)
                }
            }
        },
    }
};
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

{% hint style="info" %}
**Automatic Hash Code Calculation and Equals Implementation**

If a custom key can be serialized into a binary form, then GridGain will calculate its hash code and implement the `equals()` method automatically.

However, if the key's type is `Externalizable`, and if it cannot be serialized into the binary form, then you are required to implement the `hashCode` and `equals` methods manually. 
See the [Binary Objects](../key-value-api/binary-objects.md) page for more details.
{% endhint %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
