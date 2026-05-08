---
description: >-
  Application development with MariaDB Connector/R2DBC native API covers
  building Java projects with Maven or JAR, adding the connector to the
  classpath, and running compiled applications.
---

# Application Development with MariaDB Connector/R2DBC (Native API)

Methods for building projects with MariaDB Connector/R2DBC vary depending on the installation method you use.

## Building with Maven

When building your Java application with Maven, the build downloads and installs the relevant JAR dependencies, and compiles your project:

## Build the package:

```bash
$ mvn package
```

Run the application:

```bash
$ java -jar target/app.jar
```

Building with JAR

1. To build your Java application from a download:
2. Add your application and the JAR for MariaDB Connector/R2DBC to the Java CLASSPATH:

```bash
$ export CLASSPATH="/path/to/application:/path/to/r2dbc-mariadb-1.2.0.jar"
```

1. Compile your application:

```bash
$ javac App.java
```

1. Execute the Java class:

```bash
$ java App
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
