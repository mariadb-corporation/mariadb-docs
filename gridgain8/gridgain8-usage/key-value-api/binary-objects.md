---
description: >-
  Work directly with GridGain binary objects to read and modify cached data without deserialization or class definitions.
---

# Working with Binary Objects

## Overview

In GridGain, data is stored in [binary format](../../architecture/data-modeling/introduction.md#binary-object-format) and is deserialized into objects every time you call cache methods. However, you can work directly with the binary objects avoiding deserialization.

A binary object is a wrapper over the binary representation of an entry stored in a cache. Each binary object has the `field(name)` method which returns the value of the given field and the `type()` method that extracts the [information about the type of the object](#binary-type-and-binary-fields).
Binary objects are useful when you want to work only with some fields of the objects and do not need to deserialize the entire object.

You do not need to have the class definition to work with binary objects and can [change the structure of objects dynamically](#creating-and-modifying-binary-objects) without restarting the cluster.

The binary object format is universal for all supported platforms, i.e. Java, .NET, and C++. You can start a Java cluster, then connect to it from .NET or C++ clients and use binary objects in those platforms with no need to define classes on the client side.

{% hint style="warning" %}
**Restrictions**

There are several restrictions that are implied by the binary object format implementation:

- Internally, the type and fields of a binary object are identified by their IDs. The IDs are calculated as the hash codes of the corresponding string names. Consequently, fields or types with the identical name hash are not allowed. However, you can [provide your own implementation of ID generation](#configuring-binary-objects) via the configuration.
- For the same reason, the binary object format does not allow identical field names on different levels of class hierarchy.
- If a class implements the `Externalizable` interface, GridGain uses `OptimizedMarshaller` instead of the binary one. `OptimizedMarshaller` uses the `writeExternal()` and `readExternal()` methods to serialize and deserialize objects; therefore, the class must be added to the classpath of the server nodes.
{% endhint %}

{% hint style="info" %}
Binary Object Keys must have exactly the same field order to match. This includes the ones generated with Builder and those converted from POJOs. Set the system property / environment variable `IGNITE_BINARY_SORT_OBJECT_FIELDS` to `true` on all server and client nodes to make GridGain enforce field order automatically.
{% endhint %}

## Enabling Binary Mode for Caches

By default, when you request entries from a cache, they are returned in the deserialized format.
To work with the binary format, obtain an instance of the cache using the `withKeepBinary()` method.
This instance returns objects in the binary format (when possible).

{% tabs %}
{% tab title="Java" %}
```java
// Create a regular Person object and put it into the cache.
Person person = new Person(1, "FirstPerson");
ignite.cache("personCache").put(1, person);

// Get an instance of binary-enabled cache.
IgniteCache<Integer, BinaryObject> binaryCache = ignite.cache("personCache").withKeepBinary();
BinaryObject binaryPerson = binaryCache.get(1);
```

Note that not all objects are converted to the binary object format.

The following classes are never converted (e.g., the `toBinary(Object)` method returns the original object, and instances of these classes are stored without changes):

- All primitives (`byte`, `int`, etc) and their wrapper classes (`Byte`, `Integer`, etc)
- Arrays of primitives (byte[], int[], ...)
- `String` and array of `Strings`
- `UUID` and array of `UUIDs`
- `Date` and array of `Dates`
- `Timestamp` and array of `Timestamps`
- `Enums` and array of enums
- Maps, collections and arrays of objects

{% hint style="info" %}
Objects inside the following maps, collections, and arrays are converted to binary if possible:

- ArrayList
- LinkedList
- HashSet
- LinkedHashSet
- HashMap
- LinkedHashMap
{% endhint %}
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
ICache<int, IBinaryObject> binaryCache = cache.WithKeepBinary<int, IBinaryObject>();
IBinaryObject binaryPerson = binaryCache[1];
string name = binaryPerson.GetField<string>("Name");

IBinaryObjectBuilder builder = binaryPerson.ToBuilder();
builder.SetField("Name", name + " - Copy");

IBinaryObject binaryPerson2 = builder.Build();
binaryCache[2] = binaryPerson2;
```

Note that not all types can be represented as `IBinaryObject`. Primitive types, `string`, `Guid`, `DateTime`, collections and arrays of these types are always returned as is.
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Creating and Modifying Binary Objects

Instances of binary objects are immutable. To update fields or create a new binary object, use a binary object builder. A binary object builder is a utility class that allows you to modify the fields of binary objects without having the class definition of the objects.

{% hint style="info" %}
**Limitations**

- You cannot change the types of existing fields.
- You cannot change the order of enum values or add new constants at the beginning or in the middle of the list of enum's values. You can add new constants to the end of the list though.
{% endhint %}

You can obtain an instance of the binary object builder for a specific type as follows:

{% tabs %}
{% tab title="Java" %}
```java
BinaryObjectBuilder builder = ignite.binary().builder("com.gridgain.snippets.Person");

builder.setField("id", 2L);
builder.setField("name", "SecondPerson");

binaryCache.put(2, builder.build());
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
IIgnite ignite = Ignition.Start();

IBinaryObjectBuilder builder = ignite.GetBinary().GetBuilder("Book");

IBinaryObject book = builder
  .SetField("ISBN", "xyz")
  .SetField("Title", "War and Peace")
  .Build();
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

Builders created in this way contain no fields.
You can add fields by calling the `setField(...)` method.

You can also obtain a binary object builder from an existing binary object by calling the `toBuilder()` method.
In this case, all field values are copied from the binary object to the builder.

In the following example, we use an entry processor to update an object on the server node without having the object's class deployed on that node and without full object deserialization.

{% tabs %}
{% tab title="Java" %}
```java
// The EntryProcessor is to be executed for this key.
int key = 1;
ignite.cache("personCache").<Integer, BinaryObject>withKeepBinary().invoke(key,
    (entry, arguments) -> {
        // Create a builder from the old value.
        BinaryObjectBuilder bldr = entry.getValue().toBuilder();

        //Update the field in the builder.
        bldr.setField("name", "GridGain");

        // Set new value to the entry.
        entry.setValue(bldr.build());

        return null;
    });
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
// Not supported in C# for now
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Binary Type and Binary Fields

Binary objects hold the information about the type of objects they represent. The type information includes the field names, field types and the affinity field name.

The type of each field is represented by a `BinaryField` object.
Once obtained, a `BinaryField` object can be reused multiple times if you need to read the same field from each object in a collection.
Reusing a `BinaryField` object is faster than reading the field value directly from each binary object.
Below is an example of using a binary field.

{% tabs %}
{% tab title="Java" %}
```java
Collection<BinaryObject> persons = getPersons();

BinaryField salary = null;
double total = 0;
int count = 0;

for (BinaryObject person : persons) {
    if (salary == null) {
        salary = person.type().field("salary");
    }

    total += (float)salary.value(person);
    count++;
}

double avg = total / count;
```
{% endtab %}
{% tab title="C#/.NET" %}
unsupported
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Getting the Serialized Size

To get the size, in bytes, of a binary object's serialized form, call the `size()` method:

{% code title="Java" %}
```java
BinaryObject binaryObj = ignite.binary().toBinary(person);

int size = binaryObj.size();
```
{% endcode %}

The returned value is the size of the object's canonical, uncompressed binary representation. It does not reflect cache storage transforms such as [data compression](../configuring-caches/data-compression.md), and it does not include cache storage overhead.

## Recommendations on Binary Objects Tuning

GridGain keeps a _schema_ for every  Binary Object of a given type, which specifies the fields present in the object as well as their order and types.
Schemas are replicated to all cluster nodes.
Binary objects that have the same fields but in different order are considered to have different schemas.
We strongly recommend you should always add fields to binary objects in the same order.

A null field would normally take five bytes to store — four bytes for the field ID plus one byte for the field length.
Memory-wise, it's preferable to not include a field, rather than include a null field.
However, if you do not include a field, GridGain creates a new schema for this object, and that schema is different from the schema of the objects that do include the field. If you have multiple fields that are set to `null` in random combinations, GridGain maintains a different Binary Object schema for each combination, and your heap may be exhausted by the total size of the Binary Object schemas.
It is better to have a few schemas for your Binary Objects, with the same set of fields of same types, set in the same order. Choose one of them when creating Binary Object by supplying the same set of fields, even with null value. This is also the reason you need to supply field type for null field.

You can also nest your Binary Objects if you have a subset of fields which are optional but either all absent or all present.
You can put them in a separate BinaryObject, which is either stored under a field in the parent object or set as null.

If you have a large number of fields which are all optional in any combinations, and very often null, you can store them in a map field.
You will have several fixed fields in your value object, and one map for extra properties.

## Configuring Binary Objects

In the vast majority of use cases, there is no need to configure binary objects. However, if you need to change the type and field IDs generation or plug in a custom serializer, you can do this via the configuration.

The type and fields of a binary object are identified by their IDs. The IDs are calculated as the hash codes of the corresponding string names and are stored in each binary object. You can define your own implementation of ID generation in the configuration.

The name-to-ID conversion is done in two steps.
First, the type name (class name) or a field name is transformed by a name mapper, then an ID mapper calculates the IDs.
You can specify a global name mapper, a global ID mapper, and a global binary serializer as well as per-type mappers and serializers.
Wildcards are supported for per-type configuration, in which case the provided configuration is applied to all types that match the type name template.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

    <property name="binaryConfiguration">
        <bean class="org.apache.ignite.configuration.BinaryConfiguration">
            <property name="nameMapper" ref="globalNameMapper"/>
            <property name="idMapper" ref="globalIdMapper"/>
            <property name="typeConfigurations">
                <list>
                    <bean class="org.apache.ignite.binary.BinaryTypeConfiguration">
                        <property name="typeName" value="org.apache.ignite.examples.*"/>
                        <property name="serializer" ref="exampleSerializer"/>
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
IgniteConfiguration igniteCfg = new IgniteConfiguration();

BinaryConfiguration binaryConf = new BinaryConfiguration();
binaryConf.setNameMapper(new MyBinaryNameMapper());
binaryConf.setIdMapper(new MyBinaryIdMapper());

BinaryTypeConfiguration binaryTypeCfg = new BinaryTypeConfiguration();
binaryTypeCfg.setTypeName("com.gridgain.snippets.*");
binaryTypeCfg.setSerializer(new ExampleSerializer());

binaryConf.setTypeConfigurations(Collections.singleton(binaryTypeCfg));

igniteCfg.setBinaryConfiguration(binaryConf);
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration
{
    BinaryConfiguration = new BinaryConfiguration
    {
        NameMapper = new ExampleGlobalNameMapper(),
        IdMapper = new ExampleGlobalIdMapper(),
        TypeConfigurations = new[]
        {
            new BinaryTypeConfiguration
            {
                TypeName = "org.apache.ignite.examples.*",
                Serializer = new ExampleSerializer()
            }
        }
    }
};
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
