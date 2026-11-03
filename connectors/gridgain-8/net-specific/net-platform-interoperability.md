---
description: >-
  How GridGain.NET interoperates with Java and C++ through the common binary format,
  including identifier mapping, type and collection compatibility, and mixed-platform clusters.
---

# GridGain.NET and Platform Interoperability

GridGain allows different platforms, such as .NET, Java and C++, to interoperate with each other.
Classes and objects defined and written to Ignite by one platform can be read and used by another platform.

## Identifiers

To achieve interoperability Ignite writes objects using the common binary format. This format encodes object type and
fields using integer identifiers.

To transform an object's type and field names to an integer value, Ignite passes them through two stage:

- Name transformation: full type name and field names are passed to `IBinaryNameMapper` interface and converted to some common form.
- ID transformation: resulting strings are passed to `IBinaryIdMapper` to produce either type ID or field ID.

Mappers can be set either globally in `BinaryConfiguration` or for concrete type in `BinaryTypeConfiguration`.

Java has the same interfaces `BinaryNameMapper` and `BinaryIdMapper`. They are set on `BinaryConfiguration` or `BinaryTypeConfiguration`.

.NET and Java types must map to the same type ID and relevant fields must map to the same field ID.

## Default Behavior

The .NET part of GridGain.NET applies the following conversions by default:

- Name transformation: the `System.Type.FullName` property for non-generics types; field or property name is unchanged.
- ID transformation: names are converted to lower case and then ID is calculated in the same way as in the `java.lang.String.hashCode()` method in Java.

The Java part of GridGain.NET applies the following conversions by default:

- Name transformation: the `Class.getName()` method to get class name; field name is unchanged.
- ID transformation: names are converted to lower case and then `java.lang.String.hashCode()` is used to calculate IDs.

For example, the following two types will automatically map to each other, if they are outside namespaces (.NET) and packages (Java):

{% tabs %}
{% tab title="C#" %}
```csharp
class Person
{
    public int Id { get; set; }
    public string Name { get; set; }
    public byte[] Data { get; set; }
}
```
{% endtab %}
{% tab title="Java" %}
```java
class Person
{
    public int id;
    public String name;
    public byte[] data;
}
```
{% endtab %}
{% endtabs %}

However, the types are normally within some namespace or package. And naming conventions for packages and namespaces
differ in Java and .NET. It may be problematic to have .NET namespace be the same as Java package.

Simple name mapper (which ignores namespace) can be used to avoid this problem. It should be configured both for .NET and Java:

{% tabs %}
{% tab title="Java Spring XML" %}
```xml
<bean id="grid.cfg" class="org.apache.ignite.configuration.IgniteConfiguration">
    ...
    <property name="binaryConfiguration">
        <bean class="org.apache.ignite.configuration.BinaryConfiguration">
            <property name="nameMapper">
                <bean class="org.apache.ignite.binary.BinaryBasicNameMapper">
                    <property name="simpleName" value="true"/>
                </bean>
            </property>
        </bean>
    </property>
    ...
</bean>
```
{% endtab %}
{% tab title="C#" %}
```csharp
var cfg = new IgniteConfiguration
{
  BinaryConfiguration = new BinaryConfiguration
  {
    NameMapper = new BinaryBasicNameMapper {IsSimpleName = true}
  }
}
```
{% endtab %}
{% tab title="app.config" %}
```xml
<igniteConfiguration>
  <binaryConfiguration>
    <nameMapper type="Apache.Ignite.Core.Binary.BinaryBasicNameMapper, Apache.Ignite.Core" isSimpleName="true" />
  </binaryConfiguration>
</igniteConfiguration>
```
{% endtab %}
{% endtabs %}

## Types Compatibility

| `C#` | `Java` |
|---|---|
| `bool` | `boolean` |
| `byte (*), sbyte` | `byte` |
| `short, ushort (*)` | `short` |
| `int, uint (*)` | `int` |
| `long, ulong (*)` | `long` |
| `char` | `char` |
| `float` | `float` |
| `double` | `double` |
| `decimal` | `java.math.BigDecimal (**)` |
| `string` | `java.lang.String` |
| `Guid` | `java.util.UUID` |
| `DateTime` | `java.util.Date, java.sql.Timestamp` |

`* byte, ushort, uint, ulong` do not have Java counterparts, and are mapped directly byte-by-byte (no range check).
For example, `byte` value of `200` in C# will result in signed `byte` value of `-56` in Java.

`** Java BigDecimal` has arbitrary size and precision, while C# decimal is fixed to 16 bytes and 28-29 digit precision. GridGain.NET will throw `BinaryObjectException` if a `BigDecimal` value does not fit into `decimal` on deserialization.

`Enum` - In Ignite, Java `writeEnum` can only write ordinal values, but in .NET you can assign any number to the `enumValue`.
So, note that any custom enum-to-primitive value bindings are not taken into account.

{% hint style="danger" %}
**DateTime Serialization**

DateTime can be Local and UTC; Java Timestamp can only be UTC. Because of that, GridGain.NET can serialize DateTime in
following ways:

- .NET style (can work with non-UTC values, does not work in SQL) and as Timestamp (throws exception on non-UTC values, works properly in SQL).

- Reflective serialization: mark field with `[QuerySqlField]` to enforce Timestamp serialization, or set `BinaryReflectiveSerializer.ForceTimestamp`
to true; this can be done on per-type basis, or globally like this:
`IgniteConfiguration.BinaryConfiguration = new BinaryConfiguration { Serializer = new BinaryReflectiveSerializer { ForceTimestamp = true } }`

- `IBinarizable`: use IBinaryWriter.WriteTimestamp method.

When it is not possible to modify class to mark fields with `[QuerySqlField]` or implement `IBinarizable`, use the `IBinarySerializer` approach.
See [Serialization page](net-serialization.md) for more details.
{% endhint %}

## Collection Compatibility

Arrays of simple types (from the table above) and arrays of objects are interoperable in all cases. For all other collections
and arrays default behavior (with reflective serialization or `IBinaryWriter.WriteObject`) in GridGain.NET is to use `BinaryFormatter`,
and the result can not be read by Java code (this is done to properly support generics). To write collections in interoperable
format, implement 'IBinarizable' interface and use `IBinaryWriter.WriteCollection`, `IBinaryWriter.WriteDictionary`,
`IBinaryReader.ReadCollection`, `IBinaryReader.ReadDictionary`methods.

## Nullable Primitive Types

The `BinaryConfiguration.UnwrapNullablePrimitiveTypes` flag, when `on`, changes the .NET behavior to match that of Java when writing object fields of nullable primitive types. By default, .NET defines such fields as `object`, which causes incompatibility with Java that defines them as a specific type, such as `int`.

The `BinaryConfiguration.UnwrapNullablePrimitiveTypes` flag is `off` by default, and this fact is reflected by a warning in the log. We recommend setting this flag `on`.

{% hint style="info" %}
Setting the `BinaryConfiguration.UnwrapNullablePrimitiveTypes` flag `on` might cause backward incompatibility. Make sure this won't happen in your environment.
{% endhint %}

## Mixed-Platform Clusters

Ignite, GridGain.NET and Ignite.C++ nodes can join the same cluster

All platforms are built on top of Java, so any node can execute Java computations.
However, .NET and C++ computations can be executed only by corresponding nodes.

The following GridGain.NET functionality is not supported when there is at least one non-.NET node in the cluster:

- Scan Queries with filter
- Continuous Queries with filter
- ICache.Invoke methods
- ICache.LoadCache with filter
- IMessaging.RemoteListen
- IEvents.RemoteQuery

Blog post with detailed walk-through: [Multi-Platform Ignite Cluster: Java + .NET](https://ptupitsyn.github.io/Ignite-Multi-Platform-Cluster/)

## Compute in Mixed-Platform Clusters

The `ICompute.ExecuteJavaTask` methods work without limitations in any cluster. Other `ICompute` methods will execute
closures only on .NET nodes.
</content>
