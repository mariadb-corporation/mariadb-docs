---
description: >-
  Use GridGain 9 caches as temporary storage, create them from SQL, Java classes,
  or a builder, and connect a cache to an external JDBC database.
---

# Caches

GridGain Caches are designed as temporary storage for rapid response "cache" of data that may be required for local operation.

Cache data is always stored in a special *cache store*. By default, the cache maintains a weak consistency with the remote storage.

## Difference Between Caches and Tables

Unlike tables, in GridGain caches do not have persistence or store transaction history.

This means that caches also do not support read-only transactions and continuous queries, as those features rely on transaction history to ensure consistency.

Additionally, fields in caches cannot be nullable.

## Requirements

To use caches in your project, you need to add a `gridgain-jdbc-cache-store` dependency:

```xml
<dependency>
    <groupId>org.gridgain</groupId>
    <artifactId>gridgain-jdbc-cache-store</artifactId>
    <version>9.1</version>
</dependency>
```

## Creating a Cache

Caches are created by using the DDL [CREATE CACHE](../sql-reference/ddl.md#create-cache) command, for example:

{% hint style="warning" %}
When creating a cache, it must use the storage that has the `aimem` [storage type](../administrators-guide/storage/engines/aimem.md). In this example, we assume that the `in-memory` storage profile has already been configured to use the `aimem` storage engine.
{% endhint %}

### Using SQL

You can create a cache from SQL by using the [CREATE CACHE](../sql-reference/ddl.md#create-cache) command:

```sql
CREATE ZONE CACHES STORAGE PROFILES['in-memory'];

CREATE CACHE Accounts (
    accountNumber INT PRIMARY KEY,
    firstName VARCHAR,
    lastName VARCHAR,
    balance DOUBLE
) ZONE CACHES;
```

You can execute this SQL from your Java application as well, for example:

```java
client.sql().execute(null,
        "CREATE CACHE Accounts ("
                + "accountNumber INT PRIMARY KEY,"
                + "firstName VARCHAR,"
                + "lastName VARCHAR,"
                + "balance DOUBLE"
                + ") ZONE MYZONE"
);
```

### From Java Class

You can use the `@Cache` annotation in your Java code to create caches.

{% hint style="info" %}
You can only create caches from Key-Value POJOs.
{% endhint %}

```java
class AccountPojoKey {
    @Id
    Integer id;

    @Id(SortOrder.DESC)
    @Column(value = "id_str", length = 20)
    String idStr;
}

class AccountPojoValue {
    @Column("f_name")
    String firstName;

    @Column("l_name")
    String lastName;

    String str;
}

public void createCache() {
    org.apache.ignite.cache.Cache myCache = IgniteClient.builder()
            .addresses("127.0.0.1:10800")
            .build().catalog().createCache(AccountPojoKey.class, AccountPojoValue.class);

    KeyValueView<AccountPojoKey, AccountPojoValue> view = myCache.keyValueView(new JdbcCacheStoreFactory().setDialect(new H2Dialect()),
            Mapper.of(AccountPojoKey.class), Mapper.of(AccountPojoValue.class));
}
```

### With a Cache Builder

You can also use a builder to create a cache definition in your code instead of first creating a Java class.

{% hint style="info" %}
When using builders, only the `@Id` and `@Column` annotations on fields are supported.
{% endhint %}

The example below creates a simple cache:

```java
client.catalog().createCache(
        CacheDefinition.builder("test")
                .primaryKey("key")
                .columns(
                        column("key", ColumnType.INT32),
                        column("value", ColumnType.INT32)
                )
                .build()
);
```

## Cache-Only Transactions

Transactions cannot interact with both caches and tables at the same time. When you create a transaction, it must be specified as a cache-specific transaction by setting the `cacheOnly` option to `true`:

```java
AccountKey k2 = new AccountKey(2);
AccountValue a2 = new AccountValue("Bob", "Smith", 750);

Transaction tx = client.transactions()
        .begin(new TransactionOptions().cacheOnly(true).timeoutMillis(5));

boolean committed = false;

try {
    kvView.put(tx, k2, a2);
    committed = true;
} finally {
    if (!committed) {
        tx.rollback();
    }
}
```

## Caches as External Storage

Caches need to be connected to an external storage to store data permanently. When connected, you can read data directly from the external storage if required data is not available in the cache, or write data that was sent to cache into the persistent storage.

Currently, GridGain supports the *JDBC cache store*, which allows to connect a cache and a relational database contents. Support for more storages will be added later.

You can use tuples or POJOs to work with the database. In the examples below we will use the following POJOs:

{% tabs %}
{% tab title="POJO" %}
```java
public class AccountKey {
    public int accountNumber;

    public AccountKey() {}

    public AccountKey(int accountNumber) {
        this.accountNumber = accountNumber; }
}
public class AccountValue {
    public String firstName;
    public String lastName;
    public double balance;

    public void AccountValue() {}

    public AccountValue(String f, String l, double b) {
        firstName = f;
        lastName = l;
        balance = b;
    }
}
```
{% endtab %}

{% tab title="Tuple" %}
```java
// Tuple objects are created in code samples.
```
{% endtab %}
{% endtabs %}

To connect to an external database:

- Configure the connection to the external database:

```java
var dataSrc = JdbcConnectionPool.create("jdbc:h2:mem:CacheExample", "sa", "");
```

- Configure a cache store factory:

{% tabs %}
{% tab title="POJO" %}
```java
var storeFactory = new JdbcCacheStoreFactory();
storeFactory.setDialect(new H2Dialect());
```
{% endtab %}

{% tab title="Tuple" %}
```java
var storeFactory = new JdbcCacheStoreFactory();
storeFactory.setDialect(new H2Dialect());
```
{% endtab %}
{% endtabs %}

- Define mapping and:

{% tabs %}
{% tab title="POJO" %}
```java
var jdbcType = new JdbcType();
jdbcType.setDatabaseSchema("PUBLIC");
jdbcType.setDatabaseTable("Accounts");
jdbcType.setKeyType(AccountKey.class);
jdbcType.setKeyFields(
        new JdbcTypeField(Types.INTEGER, "accountNumber",
                Integer.class, "accountNumber"));
jdbcType.setValueType(AccountValue.class);
jdbcType.setValueFields(
        new JdbcTypeField(Types.VARCHAR, "firstName", String.class, "firstName"),
        new JdbcTypeField(Types.VARCHAR, "lastName", String.class, "lastName"),
        new JdbcTypeField(Types.DOUBLE, "balance", Double.class, "balance"));
return jdbcType;
```
{% endtab %}

{% tab title="Tuple" %}
```java
var jdbcType = new JdbcType();
jdbcType.setDatabaseSchema("PUBLIC");
jdbcType.setDatabaseTable("Accounts");
jdbcType.setKeyType(Tuple.class);
jdbcType.setKeyFields(
        new JdbcTypeField(Types.INTEGER, "id", Integer.class, "id"),
        new JdbcTypeField(Types.VARCHAR, "id_str", String.class, "idStr")
);
jdbcType.setValueType(Tuple.class);
jdbcType.setValueFields(
        new JdbcTypeField(Types.VARCHAR, "firstName", String.class, "firstName"),
        new JdbcTypeField(Types.VARCHAR, "lastName", String.class, "lastName"),
        new JdbcTypeField(Types.DOUBLE, "balance", Double.class, "balance")
);
return jdbcType;
```
{% endtab %}
{% endtabs %}

- Create a key-value view for the table in the underlying database:

{% tabs %}
{% tab title="POJO" %}
```java
KeyValueView<AccountKey, AccountValue> kvView = client.caches()
        .cache("Accounts")
        .keyValueView(storeFactory,
                Mapper.of(AccountKey.class),
                Mapper.of(AccountValue.class));
```
{% endtab %}

{% tab title="Tuple" %}
```java
KeyValueView<Tuple, Tuple> kvView = client.caches()
        .cache("Accounts")
        .keyValueView(storeFactory);
```
{% endtab %}
{% endtabs %}

The cache is now connected to the database. Write operations to the cache will be propagated to the database, and data missing in the cache will be retrieved automatically. For example, here is how you can retrieve a key:

{% tabs %}
{% tab title="POJO" %}
```java
AccountKey key1 = new AccountKey(123);
AccountValue val1 = kvView.get(null, key1);

AccountKey key2 = new AccountKey(1234);
AccountValue val2 = new AccountValue("John", "Smith", 100);
kvView.put(null, key2, val2);

boolean hasBoth = kvView.containsAll(null, List.of(key1, key2));

Map<AccountKey, AccountValue> values = kvView.getAll(null, List.of(key1, key2));
```
{% endtab %}

{% tab title="Tuple" %}
```java
Tuple key1 = Tuple.create().set("id", 123);
Tuple val1 = kvView.get(null, key1);

Tuple key2 = Tuple.create().set("id", 1234);
Tuple val2 = Tuple.create()
        .set("firstName", "John")
        .set("lastName", "Smith")
        .set("balance", 100.0);
kvView.put(null, key2, val2);

boolean hasBoth = kvView.containsAll(null, List.of(key1, key2));

Map<Tuple, Tuple> values = kvView.getAll(null, List.of(key1, key2));
```
{% endtab %}
{% endtabs %}

### External Storage Write-Behind

By default, GridGain keeps the cache consistent with the connected database. You can configure your cache to copy data from clients asynchronously by setting the `WRITE_MODE` parameter to `ASYNC`.

```sql
CREATE ZONE CACHES STORAGE PROFILES['in-memory'];

CREATE CACHE Accounts (
    accountNumber INT PRIMARY KEY,
    firstName VARCHAR,
    lastName VARCHAR,
    balance DOUBLE)
PRIMARY ZONE CACHES WRITE MODE ASYNC
```

When a cache is set to async mode, any data written to it from the client will be propagated to the database asynchronously. For example:

```java
IgniteClient client = IgniteClient.builder()
        .addresses("127.0.0.1:10800")
        .cache(ClientCacheConfiguration.builder()
                .cacheWriteBehindParallelOperations(2048)
                .build())
        .build();

KeyValueView<AccountKey, AccountValue> kvView = client.caches()
        .cache("Accounts")
        .keyValueView(storeFactory,
                Mapper.of(AccountKey.class),
                Mapper.of(AccountValue.class));
kvView.put(null, key, value);
```

The [`cacheWriteBehindParallelOperations`](https://www.gridgain.com/sdk/gridgain9/latest/javadoc/org/apache/ignite/client/ClientCacheConfiguration.html#cacheWriteBehindParallelOperations\(\)) client configuration option defines the maximum number of parallel write behind operations for the cache (1024 by default). If the write-behind queue is full, new tasks will be performed in `SYNC` mode.

Currently, only operations made from GridGain clients are be propagated in asynchronous mode.
