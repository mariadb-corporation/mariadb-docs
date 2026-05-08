---
description: >-
  Add MariaDB Connector/J to a Maven project by declaring the
  mariadb-java-client dependency in pom.xml, then connect to MariaDB using
  standard JDBC DriverManager methods.
---

# Java Connector Using Maven

[MariaDB Connector/J](./) is used to connect applications developed in Java to MariaDB and MySQL databases using the standard JDBC API.

## Prerequisites

* A MariaDB / MySQL server running on localhost using the default port 3306
* Java version >= 8
* Maven

## Create Maven Project

Create a simple Java project with Maven:

```bash
mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=my-app 
-DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
```

_Replace "com.mycompany.app" and "my-app" with appropriate values_

The new project will be created in the folder "my-app". This folder contains the file `pom.xml` that permits configuring Maven.

## Get MariaDB Java Driver

Declares driver in `pom.xml` (and setting java minimal version to 1.8) :

pom.file will then be :

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.mycompany.app</groupId>
    <artifactId>my-app</artifactId>
    <packaging>jar</packaging>
    <version>1.0-SNAPSHOT</version>
    <name>my-app</name>
    <url>http://maven.apache.org</url>

    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>3.8.1</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.mariadb.jdbc</groupId>
            <artifactId>mariadb-java-client</artifactId>
            <version>3.4.1</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.6.0</version>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                </configuration>
            </plugin>
        </plugins>
    </build>

</project>
```

#### Connection

Standard JDBC methods [DriverManager.getConnection(String url, String user, String password)](https://docs.oracle.com/javase/8/docs/api/java/sql/DriverManager.html#getConnection-java.lang.String-java.lang.String-java.lang.String-) are used to connect to the database.

Basic url string is standardized for the MariaDB driver : `jdbc:(mysql|mariadb):[replication:|failover:|sequential:|aurora:]//<hostDescription>[,<hostDescription>...]/[database][?<key1>=<value1>[&<key2>=<value2>]]`

The MariaDB driver is registered automatically for a url that begins with "jdbc:mariadb:" or "jdbc:mysql:".

Assuming a server is installed on the local machine with default port 3306, the url String is then `"jdbc:mariadb://localhost/"`.

Basic maven archetype has created a simple Java file `App.java` in `src/main/java/com/mycompany/app`.\
Update the file `App.java` with the following content: (assuming a server is installed on the local machine, with a user "root" with no password) :

```java
package com.mycompany.app;

import java.sql.*;

public class App {

    public static void main( String[] args ) throws SQLException {
        //create connection for a server installed in localhost, with a user "root" with no password
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

Compile project:

```bash
mvn install
```

Maven will automatically download the driver and compile the App file.

Run it using maven:

```shell
C:\temp\my-app>mvn exec:java -Dexec.mainClass="com.mycompany.app.App"
[INFO] Scanning for projects...
[INFO]
[INFO] ------------------------------------------------------------------------
[INFO] Building my-app 1.0-SNAPSHOT
[INFO] ------------------------------------------------------------------------
[INFO]
[INFO] --- exec-maven-plugin:1.6.0:java (default-cli) @ my-app ---
Hello World!
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 0.837 s
[INFO] Finished at: 2017-10-25T11:16:06+02:00
[INFO] Final Memory: 10M/245M
[INFO] ------------------------------------------------------------------------
```

## See Also

* More information at [About MariaDB Connector/J](about-mariadb-connector-j.md)

{% @marketo/form formId="4316" %}
