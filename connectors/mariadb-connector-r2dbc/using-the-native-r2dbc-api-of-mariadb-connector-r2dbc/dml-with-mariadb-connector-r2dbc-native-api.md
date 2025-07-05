# DML with MariaDB Connector/R2DBC (Native API)

Java developers can use MariaDB Connector/R2DBC to connect to MariaDB database products using the Reactive Relational Database Connectivity (R2DBC) API. R2DBC operations are non-blocking, which makes R2DBC more scalable than Java's standard JDBC API.

## DML Operations

DML (Data Manipulation Language) refers to all SQL-data statements in the SQL standard (ISO/IEC 9075-2:2016), for example: [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/changing-deleting-data/delete), [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/insert), [REPLACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/changing-deleting-data/replace), [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/select), and [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/changing-deleting-data/update).

With R2DBC, DML operations are performed with the following classes:

| Class                    | Description                                   |
| ------------------------ | --------------------------------------------- |
| Class                    | Description                                   |
| io.r2dbc.spi.Statement   | Creates a statement to execute on the server. |
| io.r2dbc.spi.Result      | Contains the result-set from the server.      |
| io.r2dbc.spi.Row         | Contains a single row.                        |
| io.r2dbc.spi.RowMetadata | Contains metadata for a row.                  |

## Code Example: INSERT

The following example shows how to insert data into the example table created in [Setup for Examples](setup-for-connector-r2dbc-examples-native-api.md):

```java
//Module Imports
import org.mariadb.r2dbc.MariadbConnectionConfiguration;
import org.mariadb.r2dbc.MariadbConnectionFactory;
import io.r2dbc.spi.Connection;
import io.r2dbc.spi.Statement;
import reactor.core.publisher.Mono;

// Main Application Class
public class App {

   // Connection Configuration
   private static MariadbConnectionConfiguration conf;
   private static MariadbConnectionFactory connFactory;
   private static Connection conn;

   // Main Process
   public static void main(String[] args) {
      //Initialize Connection Factory
      initConnectionFactory();

      // Insert a contact
      insertContact("John", "Smith", "js@example.com");
   }

   public static void initConnectionFactory() {

      try {
         // Configure the Connection
         conf = MariadbConnectionConfiguration.builder()
            .host("192.0.2.1").port(3306)
            .username("db_user").password("db_user_password")
            .database("test").build();

         // Instantiate a Connection Factory
         connFactory = new MariadbConnectionFactory(conf);

      }
      catch (java.lang.IllegalArgumentException e) {
         System.err.println("Issue encountered while getting connection");
         e.printStackTrace();
      }
   }

   public static void insertContact(String first_name, String last_name, String email) {

      try {
         //Initialize a Connection
         conn = connFactory.create().block();

         // Initialize Statement
         Statement stmnt = conn.createStatement(
            "INSERT INTO test.contact (first_name, last_name, email) VALUES (?, ?, ?)");

         // Bind Values to Statement
         stmnt.bind(0, first_name);
         stmnt.bind(1, last_name);
         stmnt.bind(2, email);

         // Execute Statement
         Mono.from(stmnt.execute()).subscribe();

      }
      // Catch Exception
      catch (java.lang.IllegalArgumentException e) {
         System.err.println("Issue encountered while adding contact");
         e.printStackTrace();
      } finally {
         // Close Connection
         conn.close();
      }
   }
}
```

The bind(int index, Object value) method binds non-null values to indexed parameters. The index is an integer that starts at 0, and it should not be null. If the index is invalid, the method throws an `IllegalArgumentException`, which is handled in the catch block.

Alternatively, the bind(String name, Object value) method could be used to bind a non-null value to a named parameter.

The `execute()` method executes the statement, and returns the results as a `Publisher<? extends Result>` instance.

Result instances must be fully consumed to ensure full execution of the corresponding Statement instance.

Confirm the data was properly inserted by using MariaDB Client to execute a SELECT statement:

```sql
SELECT * FROM test.contact;
```

```
+----+------------+-----------+----------------+
| id | first_name | last_name | email          |
+----+------------+-----------+----------------+
|  1 | John       | Smith     | js@example.com |
+----+------------+-----------+----------------+
```

## Code Example: SELECT

SELECT is a DML (Data Manipulation Language) operation that reads the data from a table. The following example shows how to select data from the example table created in [Setup for Examples](setup-for-connector-r2dbc-examples-native-api.md):

```java
//Module Imports
import org.mariadb.r2dbc.MariadbConnectionConfiguration;
import org.mariadb.r2dbc.MariadbConnectionFactory;
import io.r2dbc.spi.Connection;
import io.r2dbc.spi.Statement;
import io.r2dbc.spi.Result;
import io.r2dbc.spi.Row;
import io.r2dbc.spi.RowMetadata;
import reactor.core.publisher.Flux;

public class App {

   // Connection Configuration
   private static MariadbConnectionConfiguration conf;
   private static MariadbConnectionFactory connFactory;
   private static Connection conn;

   public static void main(String[] argv) {

      //Initialize Connection Factory
      initConnectionFactory();

      // Print contacts
      printContactList();
   }

   public static void initConnectionFactory() {

      try {
         // Configure the Connection
         conf = MariadbConnectionConfiguration.builder()
              .host("192.0.2.1").port(3306)
              .username("db_user").password("db_user_password")
              .database("test").build();

         // Instantiate a Connection Factory
         connFactory = new MariadbConnectionFactory(conf);

      }
      catch (java.lang.IllegalArgumentException e) {
         System.err.println("Issue encountered while getting connection");
         e.printStackTrace();
      } finally {
      }
   }

   public static void printContactList() {

      try {
         //Initialize a Connection
         conn = connFactory.create().block();

         // Initialize Statement
         Statement stmnt = conn.createStatement(
            "SELECT first_name, last_name, email FROM test.contact");

         // Execute Statement and Iterate over the Result-set
         for (String contact_entry : Flux.from(stmnt.execute()).flatMap( res ->
            res.map( (row, metadata) -> {

            return String.format( "- %s %s <%s>",
               // Get First Name
               row.get(0, String.class),

               //  Get Last Name
               row.get(1, String.class),

               //Get Email
               row.get(2, String.class));
         })).toIterable()) {

            System.out.println(contact_entry);
         }
      }
      // Catch Exception
      catch (java.lang.IllegalArgumentException e) {
         System.err.println("Encountered issue querying contact list");
         e.printStackTrace();
      } finally {
         // Close Connection
         conn.close();
      }
   }
}
```

* The Flux must be fully consumed to retrieve results, for which the method call sequence `Flux.from(stmnt.execute()).flatMap(...)` is used.
* Results can be consumed only once by either consuming `getRowsUpdated()` or `map(BiFunction)` method in the Result class.
* Result object maintains a consumption state that may be backed by a cursor pointing to its current row of data. A Result allows read-only and forward-only consumption of statement results. Thus, you can consume either `getRowsUpdated()` or `map(BiFunction)` through it only once and only from the first row to the last row.
* The sample application makes use of the `map(BiFunction<Row, RowMetadata, ? extends T> mappingFunction)` method.
* The map method returns a mapping of the rows that are the results of a query against a database. It may be empty if the query did not return any rows. A Row can be only considered valid within a BiFunction mapping function callback. The mapping Function BiFunction maps a Row and RowMetadata to a value. It throws an `IllegalArgumentException` if `mappingFunction` is null, and throws `IllegalStateException` if the result was consumed.
* In a Row object, which represents a row returned from a database query, values from columns can be retrieved either by specifying a column name using the get(String name) method, or by specifying the column index using the get(int index) method. The sample application retrieves data by column index. Columns are numbered from 0.
* A row is invalidated after consumption in the `Result.map(BiFunction)` mapping function.
* The number, type, and characteristics of columns are described through RowMetadata.
* Use the `Flux.toIterable()` method to transform the Flux object into a lazy Iterable blocking on Iterator.next() calls.

## Example output:

```
John Smith <js@example.com>
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
