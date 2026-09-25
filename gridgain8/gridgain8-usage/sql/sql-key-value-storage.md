---
description: >-
  Access cached data with both SQL and the key-value API, using a sample project that creates a SQL schema and queries it both ways.
---

# SQL and Key-Value Usage

GridGain lets you use SQL and the key-value API to access cached data even when tables/caches were created and pre-loaded with SQL. You can use one or both of the methods, according to your application requirements.

This tutorial shows you how to query the cluster using both SQL and the key-value APIs using a sample project available on [GitHub](https://github.com/dmagda/ignite_world_demo).

The project creates a SQL schema of cities of the world, populates it with data from a script, and:

- Accesses the loaded data using SQL queries.
- Accesses the loaded data using key-value operations.
- Processes data remotely.

## Creating Schema and Loading Data

To create a SQL schema and load data, follow the instructions provided in the [README.md file](https://github.com/dmagda/ignite_world_demo). Basically, you need to create tables using the [CREATE TABLE](../../reference/sql/ddl.md#create-table) statement.

The `CREATE TABLE` statement supports a number of additional parameters allowing you to specify the properties of the underlying cache. For example, the statement that creates the city table is as follows:

```sql
CREATE TABLE City (
  ID INT(11),
  Name CHAR(35),
  CountryCode CHAR(3),
  District CHAR(20),
  Population INT(11),
  PRIMARY KEY (ID, CountryCode)
) WITH "template=partitioned, backups=1, affinityKey=CountryCode, CACHE_NAME=City, KEY_TYPE=demo.model.CityKey, VALUE_TYPE=demo.model.City";
```

Note that we define the key class and the value class using the `KEY_TYPE` and `VALUE_TYPE` parameters at the end of the statement. If you do not define these parameters, Ignite will create the required classes with default names.

For further information on how the names of the cache and corresponding keys are generated, see [CREATE TABLE](../../reference/sql/ddl.md#create-table).

## Using Key-Value API

The `IgniteCache` interface provides a number of methods used to access the cache via the key-value API. For example, `IgniteCache.get(key)` allows you to retrieve the value for a specific key. In the example below, we retrieve the Amsterdam record and update the `POPULATION` field. This code is executed on the client node (the data is fetched from the server nodes).

{% tabs %}
{% tab title="Java" %}
```java
try (Ignite ignite = Ignition.start("config/ignite-config.xml")) {
    IgniteCache<CityKey, City> cityCache = ignite.cache("City");

    CityKey key = new CityKey(5, "NLD");

    //getting the city by ID and country code
    City city = cityCache.get(key);

    System.out.println(">> Updating Amsterdam record:");

    city.setPopulation(city.getPopulation() - 10_000);

    cityCache.put(key, city);

    System.out.println(cityCache.get(key));
}
```
{% endtab %}
{% tab title="C#/.NET" %}
unsupported
{% endtab %}
{% tab title="C++" %}
```cpp
IgniteConfiguration cfg;
cfg.springCfgPath = "/path/to/configuration.xml";

Ignite ignite = Ignition::Start(cfg);

Cache<CityKey, City> cityCache = ignite.GetOrCreateCache<CityKey, City>("City");

CityKey key = CityKey(5, "NLD");

cityCache.Put(key, 100000);

//getting the city by ID and country code
City city = cityCache.Get(key);

std::cout << ">> Updating Amsterdam record:" << std::endl;
city.population = city.population - 10000;

cityCache.Put(key, city);

std::cout << cityCache.Get(key).ToString() << std::endl;
```
{% endtab %}
{% endtabs %}

You can also use [binary objects](../key-value-api/binary-objects.md) to access the cached data. The benefit of using binary objects is that you avoid deserialization, which is important if you access objects from a server node that does not have the ​object's class representation.

{% tabs %}
{% tab title="Java" %}
```java
try (Ignite ignite = Ignition.start("config/ignite-config.xml")) {
    IgniteCache<BinaryObject, BinaryObject> cityCacheBinary = ignite.cache(CITY_CACHE_NAME).withKeepBinary();

    BinaryObjectBuilder cityKeyBuilder = ignite.binary().builder("demo.model.CityKey");

    cityKeyBuilder.setField("ID", 5);
    cityKeyBuilder.setField("COUNTRYCODE", "NLD");

    BinaryObject amKey = cityKeyBuilder.build();

    BinaryObject amsterdam = cityCache.get(amKey);

    System.out.printf("%1s people live in %2s \n", amsterdam.field("population"), amsterdam.field("name"));

    System.out.println(">> Updating Amsterdam record:");
    amsterdam = amsterdam.toBuilder().setField("POPULATION", (int) amsterdam.field("POPULATION") - 10_000).build();

    cityCache.put(amKey, amsterdam);

}
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Executing SQL Queries

In this example, we execute SQL queries using a `SqlFieldsQuery` object and then iterate through the results:

{% tabs %}
{% tab title="Java" %}
```java
try (Ignite ignite = Ignition.start("config/ignite-config.xml")) {
    IgniteCache cityCache = ignite.cache(CITY_CACHE_NAME);
    IgniteCache countryCache = ignite.cache(COUNTRY_CACHE_NAME);
    IgniteCache languageCache = ignite.cache(COUNTRY_LANGUAGE_CACHE_NAME);

    SqlFieldsQuery query = new SqlFieldsQuery(
        "SELECT name, population FROM country " +
        "ORDER BY population DESC LIMIT 10");

    FieldsQueryCursor<List<?>> cursor = countryCache.query(query);

    Iterator<List<?>> iterator = cursor.iterator();

    while (iterator.hasNext()) {
        List row = iterator.next();

        System.out.println("    >>> " + row.get(1) + " people live in " + row.get(0));
    }
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
IgniteConfiguration cfg;
cfg.springCfgPath = "config/sql.xml";

Ignite ignite = Ignition::Start(cfg);

Cache<int64_t, std::string> cityCache = ignite.GetOrCreateCache<int64_t, std::string>(CITY_CACHE_NAME);
Cache<int64_t, Country> countryCache = ignite.GetOrCreateCache<int64_t, Country>(COUNTRY_CACHE_NAME);
Cache<int64_t, std::string> languageCache = ignite.GetOrCreateCache<int64_t, std::string>(COUNTRY_LANGUAGE_CACHE_NAME);

// SQL Fields Query can only be performed using fields that have been listed in "QueryEntity" been of the config!
SqlFieldsQuery query = SqlFieldsQuery("SELECT name, population FROM country ORDER BY population DESC LIMIT 10");

QueryFieldsCursor cursor = countryCache.Query(query);
while (cursor.HasNext())
{
    QueryFieldsRow row = cursor.GetNext();
    std::string name = row.GetNext<std::string>();
    std::string population = row.GetNext<std::string>();
    std::cout << "    >>> " << population << " people live in " << name << std::endl;
}
```
{% endtab %}
{% endtabs %}

See the [SQL API](sql-api.md) page for more information on how to use SQL queries.

## Running Compute Tasks

In the example above, where we updated the population in the Amsterdam record, the data was fetched from the server node. With [affinity colocation](../../architecture/data-modeling/affinity-colocation.md), you can run custom code on the node at which a specific key is located without pulling the data to the client node.

{% hint style="info" %}
To use affinity colocation with custom classes which are not available in the classpath of the server nodes, set the `IgniteConfiguration.peerClassLoadingEnabled` parameter to `true`.
{% endhint %}

In the next example, we update the Amsterdam record directly on the server node. Note that you need to specify the country code as the value of the affinity key in the second argument of the `affinityRun()` method.

{% tabs %}
{% tab title="Java" %}
```java
ignite.compute().affinityRun(CITY_CACHE_NAME, "NLD", new IgniteRunnable() {

    @IgniteInstanceResource
    private Ignite ignite;

    @Override
    public void run() {

        IgniteCache<BinaryObject, BinaryObject> cityCache = ignite.cache(CITY_CACHE_NAME).withKeepBinary();
        //building the key for Amsterdam
        BinaryObject key = ignite.binary().builder("demo.model.CityKey").setField("ID", 5)
                .setField("COUNTRYCODE", "NLD").build();

        BinaryObject city = cityCache.localPeek(key);

        city = city.toBuilder().setField("POPULATION", (int) city.field("POPULATION") - 10_000).build();
        cityCache.put(key, city);

        System.out.println(cityCache.localPeek(key));
    }
});
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

In this example, we access the data using binary objects. This means that the data is not de-serialized into objects of the `City` class (and, therefore, the class files are not required on the server node).

{% hint style="info" %}
You can also get the cache without keeping the binary format and access/work with objects of the `City` class. In this case, the value class must be available in the classpath of the server nodes.
{% endhint %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
