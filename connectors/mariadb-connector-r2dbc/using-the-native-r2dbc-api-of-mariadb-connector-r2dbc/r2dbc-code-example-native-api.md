---
description: >-
  Complete Java code example using the MariaDB Connector/R2DBC native API to
  query a MariaDB table with MariadbConnectionFactory and reactive Flux
  result handling.
---

# R2DBC Code Example (Native API)

### Overview

The following example uses the native R2DBC API to select data from the table defined in [Setup for Examples](setup-for-connector-r2dbc-examples-native-api.md). Complete information on using [Connector/R2DBC natively](./) is available.

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

      // Initialize Connection
      initConnection();

      // Print contacts
      printContactList();

      // Close Connection
      conn.close();
   }

   public static void initConnection() {

      try {
         // Configure the Connection
         conf = MariadbConnectionConfiguration.builder()
              .host("192.0.2.1").port(3306)
              .username("db_user").password("db_user_password")
              .database("test").build();

         // Instantiate a Connection Factory
         connFactory = new MariadbConnectionFactory(conf);

         // Instantiate a Connection
         conn = connFactory.create().block();
      }
      catch (java.lang.IllegalArgumentException e) {
         System.err.println("Issue encountered while getting connection");
         e.printStackTrace();
      }
   }

   public static void printContactList() {

      try {
         // Initialize Statement
         Statement stmnt = conn.createStatement(
            "SELECT first_name, last_name, email FROM test.contacts");

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
      }
   }
}
```

### Example output:

```
* John Smith <john.smith@example.com>
* Jon Smith <jon.smith@example.com>
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>


{% @marketo/form formId="4316" %}
