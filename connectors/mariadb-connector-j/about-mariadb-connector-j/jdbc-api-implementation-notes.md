---
description: >-
  How MariaDB Connector/J implements the JDBC API: parsec authentication,
  time zones, LOAD DATA LOCAL INFILE, streaming, and prepared statements.
---

# MariaDB Connector/J JDBC API Implementation Notes

This page describes how MariaDB Connector/J implements parts of the JDBC API, and where its behavior needs attention.

## Parsec authentication

Since 3.5.1, parsec authentication is implemented in connector. Since 3.5.11 and 4.0.0, it works on any supported Java version without an additional dependency.

Connector/J 3.5.1 to 3.5.10 require java 15+ (to use java native ed25519 Algorithm implementation). In order to use parsec authentication with those versions on an older java, BouncyCastle is required as dependency:

```xml
<dependency>
            <groupId>org.bouncycastle</groupId>
            <artifactId>bcpkix-jdk18on</artifactId>
            <version>1.78.1</version>
        </dependency>
```

## Timezone consideration

### **The Ideal Scenario**

The simplest approach to avoid time zone headaches is for the client and server to operate in the same time zone.

### **Java Connector Timezone Options**

There are 3 options that control timestamps behavior in the java connector:

* connectionTimeZone: (LOCAL | SERVER | `<user-defined time zone>`) - This option defines the connection's time zone. LOCAL retrieves the JVM's default time zone, SERVER fetches the server's global time zone upon connection creation, and `<user-defined time zone>` allows specifying a server time zone without requesting it during connection establishment. A user-defined value must be a valid [Java ZoneId](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/time/ZoneId.html): either a region ID such as `Europe/Berlin` or `America/Los_Angeles`, or a fixed offset such as `+02:00`. An unrecognized value fails the connection with an `Unknown zoneId` error.
* forceConnectionTimeZoneToSession: (true | false) - This setting dictates whether the connector enforces the connection time zone for the session.
* preserveInstants: (true | false) - This option controls whether the connector converts Timestamp values to the connection's time zone. When enabled, a `java.sql.Timestamp` is written as its wall-clock value in the connection time zone and, on read, that wall-clock value is converted back to the same instant in the JVM's default time zone. See the "A (Discouraged) Workaround" section below for the limitations of this conversion.

### **Recommendation**

By default, the connector adopts the JVM's default time zone. If the client and server reside in different time zones, it's recommended to configure the connection time zone to match the JVM's default by setting forceConnectionTimeZoneToSession to true.\
This ensures proper operation of time functions.

(This isn’t the default behavior because there is a server Requirements to set tzinfo depending on the JVM's time zones)

### **TIMESTAMP vs. DATETIME: Know the Difference**

Just like Java's Instant and LocalDateTime, server-side TIMESTAMP and DATETIME fields serve distinct purposes. One represents a specific point in time (a moment), while the other doesn't.

* TIMESTAMP: This represents an exact moment on the timeline, expressed using the connection's time zone. When stored, it gets converted to UTC (Coordinated Universal Time) for consistency. Upon retrieval, it's converted back to the connection's time zone for display.
* DATETIME: This combines date and time-of-day information but doesn't represent a specific moment.

### **The Misuse of DATETIME:**

Due to its wider range, DATETIME is sometimes mistakenly used to store a specific point in time. While this might work if the client and server share the same time zone, it creates problems when they differ.

### **A (Discouraged) Workaround:**

While using DATETIME instead of TIMESTAMP is generally discouraged, a specific combination of settings ("preserveInstants=true\&connectionTimeZone=SERVER") can force all Java Timestamp exchanges to be converted to the connection's time zone during storage and retrieval. This keeps existing DATETIME columns usable as instants when the client and server time zones differ.

This workaround has an inherent limitation: it is not a temporary fix that becomes wrong over time, but a conversion that is only reliable for a range of dates.

* A `java.sql.Timestamp` is an instant. To store it in a DATETIME column, the connector renders it as a wall-clock value in the connection time zone. On retrieval, it reinterprets that wall-clock value in the connection time zone and converts it to the same instant in the JVM's default time zone.
* Each conversion applies the time zone rules of that specific date: the UTC offset and any daylight saving time (DST) transitions in effect at that moment. For dates far from the present, such as `9999-12-31` or dates before the time zone was standardized, those rules are extrapolated or historical, and the JVM's rules can differ from the ones the server used when the value was written.
* A wall-clock value that falls inside a DST gap (a local time that never occurred) or a DST overlap (a local time that occurred twice) cannot be mapped back to a single instant. The connector picks one, so the value can shift by the size of the DST change.

The result is that a Timestamp can round-trip to a different value, typically shifted by an hour or by the difference in offset rules. Whether this matters depends on your data. Applications that only store dates near the present, in a time zone without DST, or with a fixed-offset `connectionTimeZone` such as `+00:00`, are usually unaffected. Applications that store sentinel values like `9999-12-31 23:59:59`, or dates spanning many decades, should store instants in TIMESTAMP columns instead.

### **Compatibility with Older Connectors (Pre-3.4):**

The MariaDB Connector/J versions before 3.4 offered a single "timezone" option. While this functionality remains compatible, it's now separated into two distinct settings: connectionTimeZone and forceConnectionTimeZoneToSession. Here's a breakdown of how the old option translates to the new ones:\
"timezone=America/Los\_Angeles" is equivalent to "connectionTimeZone=America/Los\_Angeles\&forceConnectionTimeZone=true

To mimic the behavior of the "useLegacyDatetimeCode=false" option from MariaDB 2.x, you can set the following combination: “connectionTimeZone=SERVER\&preserveInstants=true”

Note: Unlike the MySQL Connector, the MariaDB Connector/J defaults connectionTimeZone to LOCAL (JVM's default) instead of SERVER.

## "LOAD DATA INFILE"

{% hint style="info" %}
LOAD DATA INFILE was the fastest way to load data. Now the fastest way is the standard JDBC executeBatch() when option 'useBulkStmts' is enabled
{% endhint %}

The fastest way to load lots of data is using [LOAD DATA INFILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile). However, using "LOAD DATA LOCAL INFILE" (ie: loading a file from the client) may be a security problem if someone can execute a query from the client, he can have access to any file on the client (according to the rights of the user running the client process).

A specific option "allowLocalInfile" (default to true) can disable this functionality on the client side.\
The global variable [local\_infile](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#local_infile) can disable LOAD DATA LOCAL INFILE on the server side.

You can provide custom stream as well using a specific setLocalInfileInputStream

```xml
Statement statement = connection.createStatement();
        org.mariadb.jdbc.Statement mariaDbStatement =
            statement.unwrap(org.mariadb.jdbc.Statement.class);
        mariaDbStatement.setLocalInfileInputStream(in);

        String sql =
            "LOAD DATA LOCAL INFILE 'notUsed'"
                + " INTO TABLE myTable "
                + " FIELDS TERMINATED BY '\\t' ENCLOSED BY ''"
                + " ESCAPED BY '\\\\' LINES TERMINATED BY '\\n'";
        statement.execute(sql);
```

Contrary to mysql connector, `setLocalInfileInputStream` value can only be used for next execution.

## Set a Query Timeout

Driver follow the JDBC specifications, permitting `Statement.setQueryTimeout()` for a particular statement.

If the goal is to set a timeout for all queries, the server permits a [limiting query time](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/aborting-statements) by setting the system variable [max\_statement\_time](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_statement_time).

This solution will handle query timeout better (and faster) than java solutions (JPA2, "javax.persistence.query.timeout", Pools integrated solution like tomcat jdbc-pool "queryTimeout"...).

Option "sessionVariables" permit to set this system variable easily :\
Example :

```java
#will set a maximum query timeout of 10 seconds for this connection
jdbc:mariadb://localhost/db?user=user&sessionVariables=max_statement_time=10
```

## Streaming Result Sets

By default, `Statement.executeQuery()` will read the full result set from the server. With large result sets, this will require large amounts of memory.

To avoid using too much memory, rather use Statement.setFetchSize(int numberOfRowInMemory) to indicate the number of rows that will be stored in memory\
Example :\
using `Statement.setFetchSize(1000)` indicates that 1000 rows will be stored in memory.\
So, when the query has executed, 1000 rows will be in memory. After 1000 `ResultSet.next()`, the next 1000 rows will be stored in memory, and so on.

{% hint style="danger" %}
If another query is run on same connection while the resultset has not been completely read, the connector will fetch all remaining rows before executing the query. This can lead to still needing lots of memory. Recommendation is then to use another connection for simultaneous operations.
{% endhint %}

Note that the server usually expects clients to read off the result set relatively quickly. The [net\_write\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#net_write_timeout) server variable controls this behavior (defaults to 60s).\
If you don't expect results to be handled in this amount of time there is a different possibility:

* With you can use the query "SET STATEMENT net\_write\_timeout=10000 FOR XXX" with XXX your "normal" query. This will indicate that specifically for this query, [net\_write\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#net_write_timeout) will be set to a longer time (10000 in this example).
* for older servers, a specific query will have to temporarily set net\_write\_timeout ("SET STATEMENT net\_write\_timeout=..."), and set it back afterward.
* if your application usually uses a lot of long queries with fetch size, the connection can be set using the option "sessionVariables=net\_write\_timeout=xxx"

Even using setFetchSize, the server will send all results to the client.

If another query is executed on the same connection when a streaming resultset has not been fully read, the connector will put the whole remaining streaming resultset in memory in order to execute the next query. This can lead to OutOfMemoryError if not handled.

### Sequential access

Since Connector/J 4.0, `Statement.setFetchSize(Integer.MIN_VALUE)` (or the `defaultFetchSize=-2147483648` option) enables sequential access on a forward-only, read-only statement. A regular streaming result set still loads each row entirely in memory before the application can read it. With sequential access, the driver reads a row from the socket one column at a time, on demand:

* Regular getters (`getInt()`, `getString()`, ...) load only the column being read into a small reusable buffer.
* `getBinaryStream()`, `getBlob()`, `getCharacterStream()`, and `getClob()` hand out a stream bound to the socket, so a large `BLOB` or `TEXT` column is never loaded in memory. The application can copy it to a file or another stream as it is received.

Sequential access has restrictions compared to a regular result set:

* Columns must be read in increasing index order. Reading a column skips the columns before it that were not read. A column can be read again only if it was not read as a stream.
* A stream, `Blob`, `Clob`, or `Reader` must be consumed before reading a following column or calling `ResultSet.next()`. It is then invalidated and cannot be read anymore.
* The result set is forward-only. `ResultSet.TYPE_SCROLL_INSENSITIVE` statements ignore the sequential-access fetch size and behave as usual.

Like other streaming result sets, if another command is executed on the same connection while the sequential result set is still being read, the remaining rows are loaded in memory first, so the result set stays usable but memory is no longer bounded.

Example: copy large files stored in a table to disk without loading any of them in memory.

```java
try (Connection con = DriverManager.getConnection("jdbc:mariadb://localhost/myDb?user=myUser&password=MyPwd");
     Statement stmt = con.createStatement()) {
  // sequential access: rows are read from the socket one column at a time
  stmt.setFetchSize(Integer.MIN_VALUE);
  try (ResultSet rs = stmt.executeQuery("SELECT name, content FROM documents")) {
    while (rs.next()) {
      // column 1 must be read before column 2
      String name = rs.getString(1);
      // the stream reads directly from the socket; it must be fully consumed
      // before rs.next() is called
      try (InputStream content = rs.getBinaryStream(2)) {
        Files.copy(content, Paths.get("/tmp/export", name));
      }
    }
  }
}
```

## Prepared Statements

The driver uses server prepared statements as a standard to communicate with the database (since 1.3.0). If the "allowMultiQueries" options are set to true, the driver will only use text protocol. Prepared statements (parameter substitution) is handled by the driver, on the client side.

## CallableStatement

Callable statement implementation won't need to access the stored procedure metadata ([mysql.proc](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-proc-table)) table if both of the following are true

* CallableStatement.getMetadata() is not used
* Parameters are accessed by index, not by name

When possible, following the two rules above provides both better speed and
eliminates concerns about SELECT privileges on the [mysql.proc](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-proc-table) table.

## Generated keys limitation

Java permit retrieving last generated keys,using [Statement.getGeneratedKeys()](https://docs.oracle.com/en/java/javase/11/docs/api/java.sql/java/sql/Statement.html#getGeneratedKeys\(\)).

Example:

```
Statement stmt = sharedConn.createStatement();
    stmt.execute(
            "INSERT INTO executeGenerated(t2) values (100)", Statement.RETURN_GENERATED_KEYS);
    ResultSet rs = stmt.getGeneratedKeys();
    rs.next();
    System.out.println(rs.getInt(1));
```

Only the first generated key will be returned, meaning that for multi-insert the generated key retrieved will correspond to the first generated value of the command.

If retrieving all generated values for multiple insert is needed, please use [INSERT...RETURNING](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insertreturning) command.

## Optional JDBC Classes

The following optional interfaces are implemented by the org.mariadb.jdbc.MariaDbDataSource class : `javax.sql.DataSource`, `javax.sql.ConnectionPoolDataSource`, `javax.sql.XADataSource`

careful : `org.mariadb.jdbc.MySQLDataSource` doesn't exist anymore and should be replaced with `org.mariadb.jdbc.MariaDbDataSource` since v1.3.0

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
