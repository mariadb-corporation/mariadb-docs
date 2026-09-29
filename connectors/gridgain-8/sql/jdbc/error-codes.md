---
description: >-
  ANSI SQLSTATE error codes returned by the GridGain JDBC drivers through
  SQLException, with their descriptions.
---

# Error Codes

Ignite JDBC drivers pass error codes in the `java.sql.SQLException` class, used to facilitate exception handling on the application side. To get an error code, use the `java.sql.SQLException.getSQLState()` method. It returns a string containing the ANSI SQLSTATE error code:

```java
// Register JDBC driver.
Class.forName("org.apache.ignite.IgniteJdbcThinDriver");

// Open JDBC connection.
Connection conn = DriverManager.getConnection("jdbc:ignite:thin://127.0.0.1");

PreparedStatement ps;

try {
    ps = conn.prepareStatement("INSERT INTO Person(id, name, age) values (1," + "'John', 'unparseableString')");
} catch (SQLException e) {
    switch (e.getSQLState()) {
    case "0700B":
        System.out.println("Conversion failure");
        break;

    case "42000":
        System.out.println("Parsing error");
        break;

    default:
        System.out.println("Unprocessed error: " + e.getSQLState());
        break;
    }
}
```

The table below lists all the [ANSI SQLSTATE](https://en.wikipedia.org/wiki/SQLSTATE) error codes currently supported by GridGain. Note that the list may be extended in the future.

| Code | Description |
| --- | --- |
| 0700B | Conversion failure (for example, a string expression cannot be parsed as a number or a date). |
| 0700E | Invalid transaction isolation level. |
| 08001 | The driver failed to open a connection to the cluster. |
| 08003 | The connection is in the closed state. Happened unexpectedly. |
| 08004 | The connection was rejected by the cluster. |
| 08006 | I/O error during communication. |
| 22004 | Null value not allowed. |
| 22023 | Unsupported parameter type. |
| 23000 | Data integrity constraint violation. |
| 24000 | Invalid result set state. |
| 0A000 | Requested operation is not supported. |
| 40001 | Concurrent update conflict. See [Concurrent Updates](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/transactions/mvcc#concurrent-updates). |
| 42000 | Query parsing exception. |
| 50000 | Ignite internal error.<br>The code is not defined by ANSI and refers to an Ignite specific error. Refer to the `java.sql.SQLException` error message for more information. |
