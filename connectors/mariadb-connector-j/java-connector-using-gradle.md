---
description: >-
  Add MariaDB Connector/J to a Gradle project by declaring the
  mariadb-java-client dependency in build.gradle, then connect to MariaDB
  using standard JDBC DriverManager methods.
---

# Java Connector Using Gradle

[MariaDB Connector/J](./) is used to connect applications developed in Java to MariaDB and MySQL databases using the standard JDBC API.

## Prerequisites

* A MariaDB/MySQL server running on localhost using the default port 3306
* Java version >= 8
* Gradle

## Create Gradle Project

Create a simple Java project with Gradle:

```bash
gradle init --type java-library
```

The new project will be created in the current folder. This folder contains the file `build. gradle` that permits configuring Gradle.

## Get MariaDB Java Driver

Declares driver in `build.gradle` (and setting Java minimal version to 1.8) :

The `build. gradle` file will then be :

```java
// Apply the Java-library plugin to add support for Java Library
apply plugin: 'java-library'

// In this section, you declare where to find the dependencies of your project
repositories.
    // Use jcenter for resolving your dependencies.
    // You can declare any Maven/Ivy/file repository here.
    jcenter()
}

sourceCompatibility = 1.8
targetCompatibility = 1.8

dependencies {
    // This dependency is exported to consumers, that is to say, found on their compile classpath.
    api 'org.apache.commons:commons-math3:3.6.1'

    // This dependency is used internally, and not exposed to consumers on their compile classpath.
    implementation 'com.google.guava:guava:22.0'

    // Use JUnit test framework
    testImplementation 'org.junit.jupiter:junit-jupiter-api:5.8.1'
    testRuntimeOnly 'org.junit.jupiter:junit-jupiter-engine:5.8.1'
	
    implementation 'org.mariadb.jdbc:mariadb-java-client:3.4.1'
	
}
```

#### Connection

Standard JDBC methods, [DriverManager.getConnection(String url, String user, String password)](https://docs.oracle.com/javase/8/docs/api/java/sql/DriverManager.html#getConnection-java.lang.String-java.lang.String-java.lang.String-), are used to connect to the database.

The basic URL string is standardized for the MariaDB driver: `jdbc:(mysql|mariadb):[replication:|failover:|sequential:|aurora:]//<hostDescription>[,<hostDescription>...]/[database][?<key1>=<value1>[&<key2>=<value2>]]`

The MariaDB driver is registered automatically for a URL that begins with "jdbc:mariadb:" or "jdbc:mysql:".

Assuming a server is installed on the local machine with default port 3306, the URL string is then `"jdbc:mariadb://localhost/"`.

Create a new file `App.java` in `src/main/java` with the following content:(assuming a server is installed on the local machine, with a user "root" with no password):

```java
Import java.sql.*;

public class App {

    public static void main( String[] args ) throws SQLException {
        //create a connection for a server installed on localhost, with a user "root" with no password
        try (Connection conn = DriverManager.getConnection("jdbc:mariadb://localhost/", "root", null)) {
            // create a Statement
            try (Statement stmt = conn.createStatement()) {
                //execute query
                try (ResultSet rs = stmt.executeQuery("SELECT 'Hello World!'")) {
                    //position result to first
                    rs.first();
                    System.out.println(rs.getString(1)); //result is "Hello World!"
                }
            }
        }
    }
}
```

To run the class app, add a new task in the build. Gradle:

```java
task run (type: JavaExec){
    description = "get started run"
    main = 'App'
    classpath = sourceSets.main.runtimeClasspath
}
```

Build project:

```shell
c:\temp\gradle>gradle build

BUILD SUCCESSFUL in 1s
4 actionable tasks: 4 up-to-date
```

Gradle will automatically download the driver and compile the app file. To run the App class, just launch the previously defined task "run":

```shell
c:\temp\gradle>gradle run

> Task: run
Hello World!


BUILD SUCCESSFUL in 1s
2 actionable tasks: 1 executed, 1 up-to-date
```

## See Also

* More information at [About MariaDB Connector/J](about-mariadb-connector-j.md)

{% @marketo/form formId="4316" %}
