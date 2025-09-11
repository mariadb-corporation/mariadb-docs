# Connect from Java App

MariaDB Connector/J enables Java applications to connect to SkySQL using a native MariaDB connector.

## Install MariaDB Connector/J via JAR

To download the JAR file manually:

1. Go to the [MariaDB Connector/J download page](https://mariadb.com/downloads/connectors/connectors-data-access/java8-connector/)
2. Within the "Product" dropdown, choose the "Java 8+ connector".
3. In the "Version" dropdown, choose the desired version.
4. Click the "Download" button to download the JAR file.
5. When the JAR file finishes downloading, place it into the relevant directory on your system.
6. Similarly, install dependency JAR files, if any are used.

## Install MariaDB Connector/J via Maven

Maven can install MariaDB Connector/J as a dependency of your application during build. Set the `<version>` element to correspond to the version of MariaDB Connector/J that you would like to install.

To use Maven to install MariaDB Connector/J, add the dependency to your `pom.xml` file:

```xml
<dependency>
   <groupId>org.mariadb.jdbc</groupId>
   <artifactId>mariadb-java-client</artifactId>
   <version>3.4.1</version>
</dependency>
```

For additional information on available releases, see the "[Release Notes for MariaDB Connector/J](https://mariadb.com/kb/en/mariadb-connector-j-release-notes/)".

Depending on the features you plan to use, you may need to add some additional dependencies to `pom.xml`.

If you downloaded the connector JAR, place it on your CLASSPATH

```bash
export CLASSPATH="/path/to/application:/path/to/mariadb-java-client-3.4.1.jar"
```

#### **Connector/J 3.0**

In MariaDB Connector/J 3.0, TLS is enabled for connections to SkySQL using the `sslMode` parameter.

```java
import java.sql.*;
import java.util.Properties;

public class App {
    public static void main(String[] argv) {
        Properties connConfig = new Properties();
        connConfig.setProperty("user", "db_user");
        connConfig.setProperty("password", "db_user_password");
        **connConfig.setProperty("sslMode", "verify-full");**

        try (Connection conn = DriverManager.getConnection("jdbc:mariadb://HOST:PORT", connConfig)) {
            try (Statement stmt = conn.createStatement()) {
                try (ResultSet contact_list = stmt.executeQuery("SELECT first_name, last_name, email FROM test.contacts")) {
                    while (contact_list.next()) {
                        System.out.println(String.format("%s %s <%s>",
                            contact_list.getString("first_name"),
                            contact_list.getString("last_name"),
                            contact_list.getString("email")));
                    }
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

#### **Connector/J 2.7**

In MariaDB Connector/J 2.7 and before, TLS is enabled for connections to SkySQL using the `useSsl` parameter.

```java
import java.sql.*;
import java.util.Properties;

public class App {
    public static void main(String[] argv) {
        Properties connConfig = new Properties();
        connConfig.setProperty("user", "db_user");
        connConfig.setProperty("password", "db_user_password");
        **connConfig.setProperty("useSsl", "true");**

        try (Connection conn = DriverManager.getConnection("jdbc:mariadb://HOST:PORT", connConfig)) {
            try (Statement stmt = conn.createStatement()) {
                try (ResultSet contact_list = stmt.executeQuery("SELECT first_name, last_name, email FROM test.contacts")) {
                    while (contact_list.next()) {
                        System.out.println(String.format("%s %s <%s>",
                            contact_list.getString("first_name"),
                            contact_list.getString("last_name"),
                            contact_list.getString("email")));
                    }
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```
