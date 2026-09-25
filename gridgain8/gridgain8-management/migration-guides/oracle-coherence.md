---
description: >-
  How Oracle Coherence Data Grid concepts map to GridGain — entry processors,
  queries, indexing, locking, transactions, affinity colocation, and binary objects.
---

# Migrating from Oracle Coherence

## Overview

GridGain, in addition to the Data Grid functionality, also provides a feature rich in-memory compute grid, streaming functionality including event workflow and CEP sliding windows support, and a Hadoop Accelerator. However, since Oracle Coherence is mainly a Data Grid product, migration from Oracle Coherence to GridGain revolves largely around the Data Grid features.

This documentation provides main abstractions and concepts to ease the migration from Coherence to GridGain. For more specific use cases and examples, refer to the main GridGain Documentation.

## EntryProcessor

A direct analogy for Coherence EntryProcessor is the `invoke(...)` closure in GridGain. The `invoke` closure is invoked atomically regardless of any other concurrent updates or transactions. Similar to the Coherence EntryProcessor API, the GridGain `invoke` closure receives a previous entry value, potentially updates it, and returns a new value (user can also return null if the entry should be deleted from cache).

As an example, the following Coherence code uses EntryProcessor to increment an integer stored in cache:

**Coherence**

{% code title="Java" %}
```java
final NamedCache cache = CacheFactory.getCache("cacheName");
final String key = "key";

cache.put(key, new Integer(1));

cache.invoke(key, new MyCounterProcessor());

...
public static class MyCounterProcessor extends AbstractProcessor {
    public Object process(InvocableMap.Entry entry) {
        Integer i = (Integer) entry.getValue();

        entry.setValue(new Integer(i.intValue() + 1));

        return null;
    }
}
```
{% endcode %}

Here is the GridGain equivalent code example, which behaves identically to the above Coherence EntryProcessor example:

**GridGain (Java 8)**

{% code title="Java" %}
```java
IgniteCache<String, Integer> cache = ignite.cache("mycache");

// Invokes EntryProcessor for a given key sequentially.
cache.invoke("mykey", (entry, args) -> {
  Integer val = entry.getValue();

  entry.setValue(val == null ? 1 : val + 1);

  return null;
});
```
{% endcode %}

## Queries and Indexing

Both GridGain and Oracle Coherence provide a rich set of querying capabilities. Even though the APIs are different, they are easily translated into one another. The main difference between the query APIs is that GridGain supports standard SQL query syntax, while the Coherence query API is based on [Java predicates](https://docs.oracle.com/javase/8/docs/api/java/util/function/Predicate.html).

In addition to basic scan querying capabilities, GridGain also provides the following data querying features not available in Oracle Coherence:

- [SQL queries](../../reference/sql/dml.md#select), including support for distributed JOIN operations
- SQL Field queries, allowing the retrieval of specific value fields instead of the whole object
- [MapReduce queries](../../gridgain8-usage/distributed-computing/map-reduce.md), allowing for preprocessing of the data on the data node side, instead of the client side, for better performance

### Query Execution

The example below illustrates how to query a Person object based on the salary field in Coherence:

**Coherence**

{% code title="Java" %}
```java
// Java predicate.
Filter filter = new EqualsFilter("getSalary", salary);

for (Iterator iter = cache.entrySet(filter).iterator(); iter.hasNext();) {
    Map.Entry entry = (Map.Entry) iter.next();
    // Process entry.
}
```
{% endcode %}

Here is the same example in GridGain:

**GridGain**

{% code title="Java" %}
```java
IgniteCache<Long, Person> cache = ignite.cache("mycache");

SqlQuery sql = new SqlQuery(Person.class, "salary > ?");

// Find only persons earning more than 1,000.
try (QueryCursor<Entry<Long, Person>> cursor = cache.query(sql.setArgs(1000))) {
  for (Entry<Long, Person> e : cursor)
    System.out.println(e.getValue().toString());
}
```
{% endcode %}

### Defining Indexes and Query Fields

This example creates an index in Oracle Coherence based on the salary field:

**Coherence**

{% code title="Java" %}
```java
NamedCache cache = CacheFactory.getCache("PersonCache");
ValueExtractor extractor = new ReflectionExtractor("getSalary");

cache.addIndex(extractor, true, null);
```
{% endcode %}

In GridGain, there are 3 ways to define indexes and fields available for querying. Indexes and queryable fields can be configured from code via the `@QuerySqlField` annotation. As shown in the example below, desired fields should be marked with this annotation.

**GridGain (Annotations)**

{% code title="Java" %}
```java
public class Person implements Serializable {
  /** Indexed field. Will be visible in SQL. */
  @QuerySqlField(index = true)
  private long id;

  /** Will be visible in SQL. */
  @QuerySqlField
  private Long salary;

  /** Will NOT be visible in SQL. */
  private int age;
}
```
{% endcode %}

Indexes and fields may also be configured with `org.apache.ignite.cache.QueryEntity` which is convenient for XML configuration using Spring.

**GridGain (XML)**

{% code title="xml" %}
```xml
<bean class="org.apache.ignite.configuration.CacheConfiguration">
    <property name="name" value="mycache"/>
    <!-- Configure query entities -->
    <property name="queryEntities">
        <list>
            <bean class="org.apache.ignite.cache.QueryEntity">
                <property name="keyType" value="java.lang.Long"/>
                <property name="valueType" value="org.apache.ignite.examples.Person"/>

                <property name="fields">
                    <map>
                        <entry key="id" value="java.lang.Long"/>
                        <entry key="name" value="java.lang.String"/>
                    </map>
                </property>

                <property name="indexes">
                    <list>
                        <bean class="org.apache.ignite.cache.QueryIndex">
                            <constructor-arg value="id"/>
                        </bean>
                    </list>
                </property>
            </bean>
        </list>
    </property>
</bean>
```
{% endcode %}

Indexes can also be created using DDL:

**GridGain (SQL)**

{% code title="sql" %}
```sql
CREATE INDEX person_idx ON PERSON (id);
```
{% endcode %}

{% hint style="info" %}
To create a multi-field index to speed up queries with complex conditions, you
can use the `@QuerySqlField.Group` annotation.
{% endhint %}

### Query Pagination

Both products support pagination of query results. The main difference is that GridGain handles pagination automatically, while Coherence leaves it up to the user to fetch the next page.

The Oracle Coherence example below executes the same query as before, but now in paginated form:

**Coherence**

{% code title="Java" %}
```java
int pageSize = 25;
Filter filter = new GreaterEqualsFilter("getSalary", salary);

// Get entries 1-25
Filter limitFilter = new LimitFilter(filter, pageSize);

Set entries = cache.entrySet(limitFilter);

// Iterate over result set.
...

// Get entries 26-50
limitFilter.nextPage();
entries = cache.entrySet(limitFilter);

// Iterate over result set.
...

```
{% endcode %}

In GridGain, Query abstract class represents an abstract paginated query to be executed on the distributed cache. You can set the page size for the returned cursor via the `Query.setPageSize(...)` method (default is 1024).

Here is the GridGain code that executes the same paginated query as above:

**GridGain**

{% code title="Java" %}
```java
IgniteCache<AffinityKey<Long>, Person> cache = Ignition.ignite().cache(PERSON_CACHE);

// SQL clause which selects salaries based on range.
String sql = "salary > ? and salary <= ?";
SqlQuery query = new SqlQuery<AffinityKey<Long>, Person>(Person.class, sql).setArgs(0, 1000);

// Page size
query.setPageSize(25);

// Iterate over the entries
cache.query(query).iterator();
```
{% endcode %}

## Explicit Locking

The Locking API is very similar between GridGain and Oracle Coherence.

**Coherence**

{% code title="Java" %}
```java
NamedCache cache = CacheFactory.getCache("txCache");
Object key = "example_key";
cache.lock(key, -1);

try {
    Object value = cache.get(key);
    // ...
    cache.put(key, value);
}
finally {
    cache.unlock(key);
}
```
{% endcode %}

Here is the equivalent GridGain locking code example, which is very similar to the Coherence example above:

**GridGain**

{% code title="Java" %}
```java
IgniteCache<String, Integer> cache = ignite.cache("myCache");

// Create a lock for the given key.
Lock lock = cache.lock("keyLock");
try {
    // Acquire the lock.
    lock.lock();

    cache.put("Hello", 11);
    cache.put("World", 22);
}
finally {
    // Release the lock.
    lock.unlock();
}
```
{% endcode %}

## Transactions

Both GridGain and Coherence support the same transactional semantics. However, GridGain transactions are very fast (orders of magnitude faster than Coherence) and are recommended whenever transactional behavior is required, even if a transaction spans multiple partitions. Transactions are typically much slower in Coherence, and users are generally recommended to use explicit locks or `EntryProcessor` (which does not work across multiple partitions) instead.

Transactions in GridGain and Coherence also look similar from an API standpoint, however, the GridGain API is more compact.

**Coherence**

{% code title="Java" %}
```java
Connection con = new DefaultConnectionFactory().createConnection("txCache");

con.setAutoCommit(false);

try {
    OptimisticNamedCache cache = con.getNamedCache("MyTxCache");

    cache.insert(key1, value1);
    cache.insert(key2, value2);
    con.commit();
}
catch (Exception e) {
    con.rollback();
    throw e;
}
finally {
    con.close();
}
```
{% endcode %}

The GridGain example below uses Java auto-closable syntax to complete a transaction, and therefore results in more compact code.

**GridGain**

{% code title="Java" %}
```java
try (Transaction tx = transactions.txStart(OPTIMISTIC, REPEATABLE_READ)) {
    Integer hello = cache.get("Hello");

    if (hello == 1)
        cache.put("Hello", 11);

    cache.put("World", 22);

    tx.commit();
}
```
{% endcode %}

Learn more about GridGain transactions [here](../../gridgain8-usage/transactions.md).

## Affinity Colocation

The Affinity Colocation feature provides the ability to colocate different keys together on the same physical JVM, allowing for efficient querying of different cache entries together. Both GridGain and Coherence support similar affinity colocation semantics with slightly different APIs.

### Affinity Colocation Using Key Class

For simple cases, Coherence requires that a key implements the `KeyAssociation` interface in order to be colocated with another key.

**Coherence**

{% code title="Java" %}
```java
public class PersonKey implements KeyAssociation {
    // ...

    public Object getAssociatedKey() {
       return getOrganizationId();
    }

    // ...
}
```
{% endcode %}

GridGain requires that the [`@AffinityKeyMapped`](https://www.gridgain.com/sdk/8.10/javadoc/org/apache/ignite/cache/affinity/AffinityKeyMapped.html) annotation be attached to the alternate affinity key field.

**GridGain**

{% code title="Java" %}
```java
public class PersonKey {
    // Person ID used to identify a person.
    private String personId;

    // Company ID which will be used for affinity.
    @AffinityKeyMapped
    private String companyId;
    ...
}
```
{% endcode %}

To learn more about colocating data in GridGain, see the [Affinity colocation](../../architecture/data-modeling/affinity-colocation.md) documentation.

## Binary Objects

Both, GridGain and Coherence allow for dynamic structure changes and cross-platform interoperability between Java, .NET, and C++. GridGain also allows accessing data from other languages, such as Python, Node.JS, and PHP via [thin clients]({connectors}/thin-clients/getting-started-with-thin-clients).

In GridGain, a concept similar to Coherence's Portable Objects is called BinaryObjects. GridGain serializes objects in a binary format and stores them in caches as `BinaryObjects`. There are several advantages to this binary format:

- It enables you to read an arbitrary field from an object's serialized form without full object deserialization. This ability completely removes the requirement to have the cache key and value classes deployed on the server node's classpath.
- It enables you to add and remove fields from objects of the same type. Given that server nodes do not have model classes definitions, this ability allows dynamic change to an objects structure, and even allows multiple clients with different versions of class definitions to co-exist.
- It enables you to construct new objects based on a type name without having class definitions at all, hence allowing dynamic type creation.

### Creating Binary Objects

One of the notorious issues with Coherence portable objects is that it requires extensive configuration for assigning portable IDs to every field. These IDs are hard to configure and are very hard to maintain, especially since they have to be unique across class hierarchies. GridGain, on the other hand, does not require any special handling for binary objects, and any existing Java, .NET, or C++ object can be treated as a Portable Object.

Here is an example of how to declare a portable object in Coherence:

**Coherence**

{% code title="Java" %}
```java
@Portable
public class Person {
   @PortableProperty(0)
   public String getFirstName() {
      return m_firstName;
   }

   private String m_firstName;

   @PortableProperty(1)
   private String m_lastName;

   @PortableProperty(2)
   private int m_age;
}
```
{% endcode %}

In GridGain, a binary object does not require any special annotations or configuration, so any existing object can become a binary object.

**GridGain**

{% code title="Java" %}
```java
// Any Java object can be used as a binary Object
public class Person {
   private String m_firstName;

   private String m_lastName;

   private int m_age;
}
```
{% endcode %}

### Declaring Binary Objects

Coherence requires that portable objects are declared in the configuration file and also requires specifying and maintaining of unique type IDs for every portable object.

GridGain does not require any configuration for binary objects. However, it provides an option to change the default behavior. Read more on Binary Objects [here](../../architecture/data-modeling/introduction.md#binary-object-format).

Click [here](https://github.com/apache/ignite/tree/master/examples/src/main/java/org/apache/ignite/examples/binary/datagrid) for examples on how to use binary objects in GridGain.

### Thin Clients

GridGain also provides Thin Clients - lightweight GridGain clients that connect to the cluster via a standard socket connection - for various languages. Thin clients are based on the binary client protocol making it possible to support Ignite connectivity from any programming language - Java, .NET, and C++, Python, Node.JS, and PHP.

## Configuration

Unlike Coherence, which only supports proprietary XML configuration syntax, GridGain supports standard Spring XML configuration syntax. In addition to the XML configuration, GridGain allows configuring the grid directly from code.

For more information about GridGain configuration, refer to [Understanding Configuration](../../gridgain8-usage/understanding-configuration.md).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
