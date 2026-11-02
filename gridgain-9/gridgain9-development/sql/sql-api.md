---
description: >-
  Use the Java SQL API in GridGain 9 to create tables, run queries, work with
  statements and parameters, execute scripts, and cancel queries.
---

# Java SQL API

In your Java projects, you can use the Java SQL API to execute SQL statements and getting results.

{% hint style="info" %}
The Java examples on this page use the thin client, which requires the `ignite-client` module. For repository and dependency configuration, see [Project Setup and Required Modules](../project-setup.md).
{% endhint %}

## Creating Tables

Here is an example of how you can create a new table on a cluster:

```java
client.sql().executeScript(
        "CREATE TABLE CITIES ("
                + "ID   INT PRIMARY KEY,"
                + "NAME VARCHAR);"

                + "CREATE TABLE ACCOUNTS ("
                + "    ACCOUNT_ID INT PRIMARY KEY,"
                + "    CITY_ID    INT,"
                + "    FIRST_NAME VARCHAR,"
                + "    LAST_NAME  VARCHAR,"
                + "    BALANCE    DOUBLE)"
);
```

### Using Sequences

When creating a table, you can designate the primary key column to be filled automatically from the sequence the values for your primary key by using sql sequences:

```java
client.sql().execute(null, "CREATE SEQUENCE IF NOT EXISTS defaultSequence;");
client.sql().execute(null, "CREATE TABLE IF NOT EXISTS Person (ID BIGINT DEFAULT NEXTVAL('defaultSequence') PRIMARY KEY, "
        + "CITY_ID BIGINT, "
        + "NAME VARCHAR, "
        + "AGE INT, "
        + "COMPANY VARCHAR);");

client.sql().execute(null,
        "INSERT INTO Person (CITY_ID, NAME, AGE, COMPANY) VALUES " +
                "(1, 'Alice', 30, 'Google'), " +
                "(2, 'Bob', 40, 'Meta'), " +
                "(3, 'Charlie', 25, 'Spotify')");
```

## Filling Tables

{% hint style="info" %}
You can parametrize the queries as described in the [Using Query Parameters](#using-query-parameters) section to make them safe from SQL injections and improve performance of repeated queries.
{% endhint %}

With GridGain 9, you can fill a table by inserting rows one at a time or by submitting them as a batch.  The example below shows how you can insert multiple lines into the table at the same time:

```java
rowsAdded = Arrays.stream(client.sql().executeBatch(tx,
                "INSERT INTO ACCOUNTS (ACCOUNT_ID, CITY_ID, FIRST_NAME, LAST_NAME, BALANCE) values (?, ?, ?, ?, ?)",
                BatchedArguments.of(1, 1, "John", "Doe", 1000.0d)
                        .add(2, 1, "Jane", "Roe", 2000.0d)
                        .add(3, 2, "Mary", "Major", 1500.0d)
                        .add(4, 3, "Richard", "Miles", 1450.0d)))
        .sum();

System.out.println("\nAdded accounts: " + rowsAdded);
```

## Getting Data From Tables

To get data from a table, execute the `SELECT` statement to get a set of results. SqlRow can provide access to column values by column name or column index. You can then iterate through results to get data.

{% hint style="info" %}
Always close the `ResultSet`, either by using a `try-with-resources` statement or by calling its `close()` method directly.
{% endhint %}

```java
try (ResultSet<SqlRow> rs = client.sql().execute(null,
        "SELECT a.FIRST_NAME, a.LAST_NAME, c.NAME FROM ACCOUNTS a "
                + "INNER JOIN CITIES c on c.ID = a.CITY_ID ORDER BY a.ACCOUNT_ID")) {
    while (rs.hasNext()) {
        SqlRow row = rs.next();

        System.out.println("    "
                + row.stringValue(0) + ", "
                + row.stringValue(1) + ", "
                + row.stringValue(2));
    }
}
```

## Partition-Specific SELECTs

When executing a SELECT operation, you can use the system `__partition_id` column to only `SELECT` data in a specific partition. To find out partition information, use the SELECT request that explicitly includes the `__partition_id` column as its part:

```sql
SELECT city_id, id, __partition_id  FROM Person;
```

Once you know the partition, you can use it in the `WHERE` clause:

```sql
SELECT city_id, id FROM Person WHERE __partition_id=23;
```

## Using Statements

You can customize statement behavior by creating a statement object and executing it. This way you can configure query-specific settings. For details on using parameters, see [Using Query Parameters](#using-query-parameters).

The example below shows how you can create a statement:

```java
Statement statement = client.sql().statementBuilder()
    .query("SELECT * FROM Person WHERE age > ?")
    .pageSize(100)
    .queryTimeout(30, TimeUnit.SECONDS)
    .build();

try (ResultSet<SqlRow> rs = client.sql().execute(null, statement, 25)) {
    // Process results
}
```

The following properties are available:

- `query` - Required. The SQL statement to execute.
- `queryTimeout` - Maximum time allowed for query execution. Must be positive. Default value: `0` (unlimited).
- `defaultSchema` - Default schema for unqualified table names in the query. Default value: `PUBLIC`.
- `pageSize` - Maximum number of result rows that can be fetched at a time. Must be positive. Default value: `1024`.
- `timeZoneId` - Time zone used for timestamp operations and functions like `CURRENT_TIME`, and when converting string literals to/from `TIMESTAMP WITH LOCAL TIME ZONE` columns. Default value: System default time zone.
- `memoryQuotaBlockSize` - Memory quota block size in bytes for statement execution. Must be positive or `null`. Default value: 512 KB.
- `allowFollowerReads` - Whether the SQL engine can read data from non-primary replicas when executing this statement. Set `true` or `false` to override the cluster-wide [`sql.allowFollowerReads`](../../reference/configuration/cluster-configuration-parameters.md#sql-configuration) setting for this statement. Default value: `null` (the cluster-wide setting applies).

## Using Query Parameters

{% hint style="info" %}
Use parametrized queries when possible. This approach protects against SQL injections and speeds up query execution by allowing the server to cache the query plan across multiple runs of the same statement.
{% endhint %}

You can create parameterized queries by using positional parameters. Replace literal values in your SQL with `?` placeholders, then pass the values as trailing arguments. Arguments are bound to placeholders in the order they appear in the query. The number of arguments must match the number of `?` placeholders in the parsed statement.

```java
try (ResultSet<SqlRow> rs = client.sql().execute(
        "DELETE FROM ACCOUNTS WHERE ACCOUNT_ID = ?", 1)) {
    System.out.println("Removed accounts: " + rs.affectedRows());
}
```

You can also bind parameters to a `Statement` object:

```java
Statement stmt = client.sql().createStatement(
        "INSERT INTO CITIES (ID, NAME) VALUES (?, ?)");

try (ResultSet<?> rs = client.sql().execute(tx, stmt, 1, "New York")) {
    rowsAdded += rs.affectedRows();
}
try (ResultSet<?> rs = client.sql().execute(tx, stmt, 2, "London")) {
    rowsAdded += rs.affectedRows();
}
```

### Supported Parameter Types

The following Java types can be used as parameter values:

| SQL column type | Java class |
| --- | --- |
| `BOOLEAN` | `java.lang.Boolean` |
| `TINYINT` | `java.lang.Byte` |
| `SMALLINT` | `java.lang.Short` |
| `INT` | `java.lang.Integer` |
| `BIGINT` | `java.lang.Long` |
| `REAL` | `java.lang.Float` |
| `DOUBLE` | `java.lang.Double` |
| `DECIMAL` | `java.math.BigDecimal` |
| `DATE` | `java.time.LocalDate` |
| `TIME` | `java.time.LocalTime` |
| `TIMESTAMP` | `java.time.LocalDateTime` |
| `TIMESTAMP WITH LOCAL TIME ZONE` | `java.time.Instant` |
| `UUID` | `java.util.UUID` |
| `VARCHAR` | `java.lang.String` |
| `VARBINARY` | `byte[]` |

## Using Scripts

The default API executes SQL statements one at a time. For large SQL statements, pass them to the `executeScript()` method. The statements will be batched together similar to using `SET STREAMING` command in GridGain 8, significantly improving performance when executing a large number of queries at once. These statements will be executed in order.

{% code title="Java" %}
```java
String script = "CREATE TABLE IF NOT EXISTS Person (id int primary key, name varchar, age int default 0);"
+ "INSERT INTO Person (id, name, age) VALUES ('1', 'John', '46');";
client.sql().executeScript(script);
```
{% endcode %}

{% hint style="info" %}
Execution of each statement is considered complete when the first page is ready to be returned. As a result, when working with large data sets, SELECT statement may be affected by later statements in the same script.
{% endhint %}

### Memory Quota Block Size

The Java, .NET, and JDBC clients support configuring memory quotas per SQL statement using the `memoryQuotaBlockSize` property. Setting a larger block size can improve performance for memory-intensive queries by reducing synchronization overhead with the node-level memory tracker. When not set, the cluster-wide `sql.memoryQuotaBlockSize` configuration value is used (default: `512k`).

The example below shows how to configure memory quota block size for a statement:

{% tabs %}
{% tab title="Java" %}
```java
// Configure memory quota block size for a resource-intensive query
Statement memoryOptimizedStmt = client.sql().statementBuilder()
        .query("SELECT a.FIRST_NAME, a.LAST_NAME, a.BALANCE, c.NAME " +
               "FROM ACCOUNTS a " +
               "INNER JOIN CITIES c ON c.ID = a.CITY_ID " +
               "ORDER BY a.BALANCE DESC")
        .memoryQuotaBlockSize(1024 * 1024L)  // 1 MB blocks
        .build();

try (ResultSet<SqlRow> rs = client.sql().execute(null, memoryOptimizedStmt)) {
    while (rs.hasNext()) {
        SqlRow row = rs.next();
        System.out.println("    "
                + row.stringValue(0) + ", "
                + row.stringValue(1) + ", "
                + row.doubleValue(2) + ", "
                + row.stringValue(3));
    }
}
```
{% endtab %}

{% tab title=".NET" %}
```csharp
var stmt = new SqlStatement("SELECT * FROM large_table")
{
    MemoryQuotaBlockSize = 1_048_576L  // 1 MB blocks
};

await using var resultSet = await client.Sql.ExecuteAsync(null, stmt);
```
{% endtab %}

{% tab title="JDBC" %}
```java
IgniteJdbcStatement stmt = conn.createStatement().unwrap(IgniteJdbcStatement.class);
stmt.setMemoryQuotaBlockSize(1_048_576L);  // 1 MB blocks
```
{% endtab %}
{% endtabs %}

### Query Cancellation

To cancel a query, create and pass the cancellation token to the execution method:

{% tabs %}
{% tab title="Java" %}
```java
CancelHandle cancelHandle = CancelHandle.create();
CancellationToken cancelToken = cancelHandle.token();

client.sql().executeAsync(
        null, cancelToken,
        "SELECT a.FIRST_NAME, b.LAST_NAME " +
                "FROM ACCOUNTS a, ACCOUNTS b, ACCOUNTS c ORDER BY a.ACCOUNT_ID"
);
```
{% endtab %}

{% tab title="C++" %}
```cpp
std::shared_ptr<cancel_handle> handle = cancel_handle::create();
std::shared_ptr<cancellation_token> token = handle->get_token();

client.get_sql().execute(nullptr, token.get(), "CREATE TABLE IF NOT EXISTS Person (id int primary key, name varchar, age int);", {});
```
{% endtab %}
{% endtabs %}

After the query is submitted, you can cancel all queries that use the tokens from the same `cancelHandle` object at any point by using the `cancel()` or `cancelAsync()` methods, for example:

{% tabs %}
{% tab title="Java" %}
```java
CompletableFuture<Void> cancelled = cancelHandle.cancelAsync();
cancelled.get(5, TimeUnit.SECONDS);

System.out.println("\nIs query cancelled: " + cancelled.isDone());
```
{% endtab %}

{% tab title=".NET" %}
```csharp
var cts = new CancellationTokenSource();
await using var resultSet = await Client.Sql.ExecuteAsync(null, "CREATE TABLE IF NOT EXISTS Person (id int primary key)", cts.Token);
await cts.CancelAsync();
```
{% endtab %}

{% tab title="C++" %}
```cpp
handle->cancel_async(ignite_result<void> cancellationResult) {
	// Handle cancellationResult here
});
```
{% endtab %}
{% endtabs %}

Another way to cancel queries is by using the SQL [KILL QUERY](../../reference/sql/operational-commands.md#kill-query) command. The query id can be retrieved via the `SQL_QUERIES` [system view](../../reference/monitoring/system-views.md).
