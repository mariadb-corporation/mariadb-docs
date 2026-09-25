---
description: >-
  Use GridGain's SQL API to configure queryable fields, run queries, execute DML and DDL, specify schemas, and cancel long-running queries.
---

# SQL API

In addition to using the JDBC driver, Java developers can use GridGain's SQL APIs to query and modify data stored in GridGain.

The `SqlFieldsQuery` class is an interface for executing SQL statements and navigating through the results. `SqlFieldsQuery` is executed through the `IgniteCache.query(SqlFieldsQuery)` method, which returns a query cursor.

## Configuring Queryable Fields

If you want to query a cache using SQL statements, you need to define which fields of the value objects are queryable. Queryable fields are the fields of your data model that the SQL engine can "see" and query.

{% hint style="info" %}
If you create tables using JDBC or SQL tools, you do not need to define queryable fields.
{% endhint %}

{% hint style="info" %}
Indexing capabilities are provided by the 'ignite-indexing' module. If you start GridGain from java code, [add this module to the classpath of your application](../setup.md#enabling-modules).
{% endhint %}

In Java, queryable fields can be configured in two ways:

- using annotations
- by defining query entities

### @QuerySqlField Annotation

To make specific fields queryable, annotate the fields in the value class definition with the `@QuerySqlField` annotation and call `CacheConfiguration.setIndexedTypes(...)`.

{% tabs %}
{% tab title="Java" %}
```java
class Person implements Serializable {
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

public static void main(String[] args) {
	Ignite ignite = Ignition.start();
	CacheConfiguration<Long, Person> personCacheCfg = new CacheConfiguration<Long, Person>();
	personCacheCfg.setName("Person");

	personCacheCfg.setIndexedTypes(Long.class, Person.class);
	IgniteCache<Long, Person> cache = ignite.createCache(personCacheCfg);
}
```

Make sure to call `CacheConfiguration.setIndexedTypes(...)` to let the SQL engine know about the annotated fields.
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

    /**
      * Indexed field sorted in descending order.
      * Will be visible to the SQL engine.
    */
    [QuerySqlField(IsIndexed = true, IsDescending = true)]
    public float Salary;
}

public static void SqlQueryFieldDemo()
{
    var cacheCfg = new CacheConfiguration
    {
        Name = "cacheName",
        QueryEntities = new[]
        {
            new QueryEntity(typeof(int), typeof(Person))
        }
    };

    var ignite = Ignition.Start();
    var cache = ignite.CreateCache<int, Person>(cacheCfg);
}
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

### Query Entities

You can define queryable fields using the `QueryEntity` class. Query entities can be configured via XML configuration.

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
class Person implements Serializable {
	private long id;

	private String name;

	private int age;

	private float salary;
}

public static void main(String[] args) {
	Ignite ignite = Ignition.start();
	CacheConfiguration<Long, Person> personCacheCfg = new CacheConfiguration<Long, Person>();
	personCacheCfg.setName("Person");

	QueryEntity queryEntity = new QueryEntity(Long.class, Person.class)
	        .addQueryField("id", Long.class.getName(), null).addQueryField("age", Integer.class.getName(), null)
	        .addQueryField("salary", Float.class.getName(), null)
	        .addQueryField("name", String.class.getName(), null);

	queryEntity.setIndexes(Arrays.asList(new QueryIndex("id"), new QueryIndex("salary", false)));

	personCacheCfg.setQueryEntities(Arrays.asList(queryEntity));

	IgniteCache<Long, Person> cache = ignite.createCache(personCacheCfg);
}
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
private class Person
{
    public long Id;

    public string Name;

    public int Age;

    public float Salary;
}

public static void QueryEntitiesDemo()
{
    var personCacheCfg = new CacheConfiguration
    {
        Name = "Person",
        QueryEntities = new[]
        {
            new QueryEntity
            {
                KeyType = typeof(long),
                ValueType = typeof(Person),
                Fields = new[]
                {
                    new QueryField("Id", typeof(long)),
                    new QueryField("Name", typeof(string)),
                    new QueryField("Age", typeof(int)),
                    new QueryField("Salary", typeof(float))
                },
                Indexes = new[]
                {
                    new QueryIndex("Id"),
                    new QueryIndex(true, "Salary"),
                }
            }
        }
    };
    var ignite = Ignition.Start();
    var personCache = ignite.CreateCache<int, Person>(personCacheCfg);
}
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Querying

To execute a select query on a cache, simply create an object of `SqlFieldsQuery` providing the query string to the constructor and run `cache.query(...)`.
Note that in the following example, the Person cache must be configured to be [visible to the SQL engine](#configuring-queryable-fields).

{% tabs %}
{% tab title="Java" %}
```java
IgniteCache<Long, Person> cache = ignite.cache("Person");

SqlFieldsQuery sql = new SqlFieldsQuery("select concat(firstName, ' ', lastName) from Person");

// Iterate over the result set.
try (QueryCursor<List<?>> cursor = cache.query(sql)) {
	for (List<?> row : cursor)
		System.out.println("personName=" + row.get(0));
}
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var cache = ignite.GetCache<long, Person>("Person");

var sql = new SqlFieldsQuery("select concat(FirstName, ' ', LastName) from Person");

using (var cursor = cache.Query(sql))
{
    foreach (var row in cursor)
    {
        Console.WriteLine("personName=" + row[0]);
    }
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
Cache<int64_t, Person> cache = ignite.GetOrCreateCache<int64_t, Person>("Person");

// Iterate over the result set.
// SQL Fields Query can only be performed using fields that have been listed in "QueryEntity" been of the config!
QueryFieldsCursor cursor = cache.Query(SqlFieldsQuery("select concat(firstName, ' ', lastName) from Person"));
while (cursor.HasNext())
{
    std::cout << "personName=" << cursor.GetNext().GetNext<std::string>() << std::endl;
}
```
{% endtab %}
{% endtabs %}

`SqlFieldsQuery` returns a cursor that iterates through the results that match the SQL query.

In .NET, this cursor implements `IAsyncEnumerable<T>`, so you can iterate the rows with `await foreach`, streaming each page as it arrives without blocking the calling thread:

{% code title="C#/.NET" %}
```csharp
// Query() returns the cursor synchronously; iterate it with await foreach to
// stream rows as each page arrives, without blocking the calling thread.
var sql = new SqlFieldsQuery("select concat(FirstName, ' ', LastName) from Person");

await foreach (var row in cache.Query(sql))
{
    Console.WriteLine("personName=" + row[0]);
}
```
{% endcode %}

### Local Execution

To force local execution of a query, use `SqlFieldsQuery.setLocal(true)`. In this case, the query is executed against the data stored on the node where the query is run. It means that the results of the query are almost always incomplete. Use the local mode only if you are confident you understand this limitation.

### Subqueries in WHERE Clause

`SELECT` queries used in `INSERT` and `MERGE` statements as well as `SELECT` queries generated by `UPDATE` and `DELETE` operations are distributed and executed in either [colocated or non-colocated distributed modes](distributed-joins.md).

However, if there is a subquery that is executed as part of a `WHERE` clause, then it can be executed in the colocated mode only.

For instance, let's consider the following query:

```sql
DELETE FROM Person WHERE id IN
    (SELECT personId FROM Salary s WHERE s.amount > 2000);
```

The SQL engine generates the `SELECT` query in order to get a list of entries to be deleted. The query is distributed and executed across the cluster and looks like the one below:

```sql
SELECT _key, _val FROM Person WHERE id IN
    (SELECT personId FROM Salary s WHERE s.amount > 2000);
```

However, the subquery from the `IN` clause (`SELECT personId FROM Salary ...`) is not distributed further and is executed over the local data set available on the node.

## Inserting, Updating, Deleting, and Merging

With `SqlFieldsQuery` you can execute the other DML commands in order to modify the data:

{% tabs %}
{% tab title="INSERT" %}
```java
IgniteCache<Long, Person> cache = ignite.cache("personCache");

cache.query(new SqlFieldsQuery("INSERT INTO Person(id, firstName, lastName) VALUES(?, ?, ?)").setArgs(1L,
		"John", "Smith")).getAll();
```
{% endtab %}
{% tab title="UPDATE" %}
```java
IgniteCache<Long, Person> cache = ignite.cache("personCache");

cache.query(new SqlFieldsQuery("UPDATE Person set lastName = ? " + "WHERE id >= ?").setArgs("Jones", 2L))
		.getAll();
```
{% endtab %}
{% tab title="DELETE" %}
```java
IgniteCache<Long, Person> cache = ignite.cache("personCache");

cache.query(new SqlFieldsQuery("DELETE FROM Person " + "WHERE id >= ?").setArgs(2L)).getAll();
```
{% endtab %}
{% tab title="MERGE" %}
```java
IgniteCache<Long, Person> cache = ignite.cache("personCache");

cache.query(new SqlFieldsQuery(
		"MERGE INTO Person(id, firstName, lastName)" + " values (1, 'John', 'Smith'), (5, 'Mary', 'Jones')"))
		.getAll();
```
{% endtab %}
{% endtabs %}

When using `SqlFieldsQuery` to execute DDL statements, you must call `getAll()` on the cursor returned from the `query(...)` method.

## Specifying the Schema

By default, any SELECT statement executed via `SqlFieldsQuery` is resolved against the PUBLIC schema. However, if the table you want to query is in a different schema, you can specify the schema by calling `SqlFieldsQuery.setSchema(...)`. In this case, the statement is executed in the given schema.

{% tabs %}
{% tab title="Java" %}
```java
SqlFieldsQuery sql = new SqlFieldsQuery("select name from City").setSchema("PERSON");
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var sqlFieldsQuery = new SqlFieldsQuery("select name from City") {Schema = "PERSON"};
```
{% endtab %}
{% tab title="C++" %}
```cpp
// SQL Fields Query can only be performed using fields that have been listed in "QueryEntity" been of the config!
SqlFieldsQuery sql = SqlFieldsQuery("select name from City");
sql.SetSchema("PERSON");
```
{% endtab %}
{% endtabs %}

Alternatively, you can define the schema in the statement:

```java
SqlFieldsQuery sql = new SqlFieldsQuery("select name from Person.City");
```

## Creating Tables

You can pass any supported DDL statement to `SqlFieldsQuery` and execute it on a cache as shown below.

{% tabs %}
{% tab title="Java" %}
```java
IgniteCache<Long, Person> cache = ignite
		.getOrCreateCache(new CacheConfiguration<Long, Person>().setName("Person"));

// Creating City table.
cache.query(new SqlFieldsQuery("CREATE TABLE City (id int primary key, name varchar, region varchar)"))
		.getAll();
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var cache = ignite.GetOrCreateCache<long, Person>(
    new CacheConfiguration
    {
        Name = "Person"
    }
);

//Creating City table
cache.Query(new SqlFieldsQuery("CREATE TABLE City (id int primary key, name varchar, region varchar)"));
```
{% endtab %}
{% tab title="C++" %}
```cpp
Cache<int64_t, Person> cache = ignite.GetOrCreateCache<int64_t, Person>("Person");

// Creating City table.
cache.Query(SqlFieldsQuery("CREATE TABLE City (id int primary key, name varchar, region varchar)"));
```
{% endtab %}
{% endtabs %}

In terms of SQL schema, the following tables are created as a result of executing the code:

- Table "Person" in the "Person" schema (if it hasn't been created before).
- Table "City" in the "Person" schema.

To query the "City" table, use statements like `select * from Person.City` or `new SqlFieldsQuery("select * from City").setSchema("PERSON")` (note the uppercase).

## Cancelling Queries

There are two ways to cancel long running queries.

The first approach is to prevent run away queries by setting a query execution timeout.

{% tabs %}
{% tab title="Java" %}
```java
SqlFieldsQuery query = new SqlFieldsQuery("SELECT * from Person");

// Setting query execution timeout
query.setTimeout(10_000, TimeUnit.SECONDS);
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var query = new SqlFieldsQuery("select * from Person") {Timeout = TimeSpan.FromSeconds(10)};
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

The second approach is to halt the query by using `QueryCursor.close()`.

{% tabs %}
{% tab title="Java" %}
```java
SqlFieldsQuery query = new SqlFieldsQuery("SELECT * FROM Person");

// Executing the query
QueryCursor<List<?>> cursor = cache.query(query);

// Halting the query that might be still in progress.
cursor.close();
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var qry = new SqlFieldsQuery("select * from Person");
var cursor = cache.Query(qry);

//Executing query

//Halting the query that might be still in progress
cursor.Dispose();
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Preventing OutOfMemory Exceptions

GridGain has a mechanism that prevents OutOfMemory exceptions by setting a limit to the amount of heap allocated to SQL queries.
If a query reaches the limit, it is either stopped or offloaded to disk, depending on whether query offloading is enabled.
Refer to the [Memory Quotas](../../ha-and-performance/performance-tuning/sql-memory-management.md) page for details.

The following code snippets illustrates how to catch a memory quota exception:

{% tabs %}
{% tab title="Java" %}
```java

try {
    List<List<?>> list = cache.query(new SqlFieldsQuery("select * from myTable")).getAll();
} catch (SqlMemoryQuotaExceededException e) {
    //handle the exception here
    System.out.println("run out of memory");
}
```
{% endtab %}
{% tab title="C#/.NET" %}
unsupported
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Example

The GridGain distribution package includes a ready-to-run `SqlDmlExample` that demonstrates the usage of all the above-mentioned DML operations.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
