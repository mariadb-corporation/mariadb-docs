---
description: Quickstart Guide for Connector/J
---

# MariaDB Connector/J Guide

### Quickstart Guide: MariaDB Connector/J

MariaDB Connector/J is the official Java Database Connectivity (JDBC) driver for connecting Java applications to MariaDB and MySQL databases. It allows Java programs to interact with databases using the standard JDBC API.

See [About MariaDB Connector/J](https://mariadb.com/docs/connectors/mariadb-connector-j/about-mariadb-connector-j) for full content.

#### 1. Installation

You can include MariaDB Connector/J in your project using build tools like Maven or Gradle, or by manually adding the JAR file to your project's classpath.

a. Using Maven:

Add the following dependency to your pom.xml file:

```xml
<dependency>
    <groupId>org.mariadb.jdbc</groupId>
    <artifactId>mariadb-java-client</artifactId>
    <version>3.3.3</version> </dependency>
```

b. Using Gradle:

Add the following dependency to your build.gradle file:

```gradle
dependencies {
    implementation 'org.mariadb.jdbc:mariadb-java-client:3.3.3' // Use the latest stable version
}
```

**c. Manual Installation:**

1. Download the latest stable `.jar` file from the [MariaDB Downloads page](https://mariadb.com/downloads/#connectors).
2. Add the downloaded `.jar` file to your project's classpath.

#### 2. Basic Usage (Connecting to MariaDB)

Here's a simple Java example demonstrating how to establish a connection and execute a basic query using `DriverManager`.

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class MariaDBQuickstart {

    // Database connection parameters
    static final String DB_URL = "jdbc:mariadb://localhost:3306/your_database_name";
    static final String USER = "your_username";
    static final String PASS = "your_password";

    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;

        try {
            // Register JDBC driver (optional for modern JDBC, but good practice)
            // Class.forName("org.mariadb.jdbc.Driver");

            System.out.println("Connecting to database...");
            conn = DriverManager.getConnection(DB_URL, USER, PASS);

            System.out.println("Creating statement...");
            stmt = conn.createStatement();
            String sql = "SELECT id, name FROM your_table_name";
            rs = stmt.executeQuery(sql);

            // Extract data from result set
            while (rs.next()) {
                // Retrieve by column name
                int id = rs.getInt("id");
                String name = rs.getString("name");

                // Display values
                System.out.print("ID: " + id);
                System.out.println(", Name: " + name);
            }
        } catch (SQLException se) {
            // Handle errors for JDBC
            se.printStackTrace();
        } finally {
            // Close resources in finally block
            try {
                if (rs != null) rs.close();
            } catch (SQLException se2) {
                // Do nothing
            }
            try {
                if (stmt != null) stmt.close();
            } catch (SQLException se2) {
                // Do nothing
            }
            try {
                if (conn != null) conn.close();
            } catch (SQLException se) {
                se.printStackTrace();
            }
            System.out.println("Database resources closed.");
        }
    }
}
```

**Before Running:**

1. Replace `your_database_name`, `your_username`, `your_password`, and `your_table_name` with your actual database details.
2. Ensure you have a MariaDB server running and a database/table set up.

#### 3. Connection Strings

MariaDB Connector/J supports various connection string formats, including options for failover and load balancing. The basic format is:

`jdbc:mariadb://<hostDescription>[,<hostDescription>...]/[database][?<key1>=<value1>[&<key2>=<value2>]]`

For example:

* `jdbc:mariadb://localhost:3306/mydb`
* `jdbc:mariadb://server1:3306,server2:3306/mydb?failover=true`

#### 4. Connection Pooling (for Production)

For production applications, it's highly recommended to use a connection pool to manage database connections efficiently. MariaDB Connector/J can be used with external connection pooling libraries like HikariCP or Apache Commons DBCP, or its own `MariaDbPoolDataSource`.

* **`MariaDbDataSource`**: Creates a new connection each time.
* **`MariaDbPoolDataSource`**: Maintains a pool of connections for reuse.

When using an external pool, configure it to use `org.mariadb.jdbc.Driver` as the JDBC driver class.

{% @marketo/form formId="4316" %}
