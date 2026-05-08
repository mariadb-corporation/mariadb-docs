---
description: >-
  Install MariaDB Connector/R2DBC via Maven by adding the r2dbc-mariadb
  dependency to pom.xml, or manually by downloading the JAR and adding it to
  the Java CLASSPATH alongside r2dbc-pool.
---

# Install MariaDB Connector/R2DBC

MariaDB Connector/R2DBC is usually installed using Maven or by manually downloading the JAR file. The Maven build process connects to repositories to download and install dependencies, including MariaDB Connector/R2DBC and any other specified dependencies your application may require.

When downloading MariaDB Connector/R2DBC, you must manually add dependencies to your Java CLASSPATH.

## Install MariaDB Connector/R2DBC via JAR

To download the JAR file manually:\
Go to the [MariaDB Connector/R2DBC download page](https://mariadb.com/downloads/connectors/connectors-data-access/r2dbc-connector/)

1. Ensure the "Product" dropdown reads "R2DBC connector."
2. In the "Version" dropdown, select the version you want to download.
3. Click the "Download" button to download the JAR file.
4. When the JAR file finishes downloading, place it into the relevant directory on your system.
5. If you plan to use [Connection Pools](connection-pools-with-mariadb-connector-r2dbc-native-api.md), download the JAR file for the [r2dbc-pool package](https://github.com/r2dbc/r2dbc-pool), and place it into the relevant directory on your system.
6. Confirm that the relevant JAR files are in your Java CLASSPATH.

## Install MariaDB Connector/R2DBC via Maven

1. Add the r2dbc-mariadb package as a dependency for your application to your application's pom.xml file.\
   To install the latest Connector/R2DBC 1.0 release, add the following:

```xml
<dependency>
   <groupId>org.mariadb</groupId>
   <artifactId>r2dbc-mariadb</artifactId>
   <version>1.0.3</version>
</dependency>
```

To install the latest Connector/R2DBC 1.2 release, add the following:

```xml
<dependency>
   <groupId>org.mariadb</groupId>
   <artifactId>r2dbc-mariadb</artifactId>
   <version>1.2.2</version>
</dependency>
```

1. If you plan to use [Connection Pools](connection-pools-with-mariadb-connector-r2dbc-native-api.md), add the [r2dbc-pool package](https://github.com/r2dbc/r2dbc-pool) as an additional dependency for your application to your application's pom.xml file.

For Connector/R2DBC 1.0:

```xml
<dependency>
    <groupId>io.r2dbc</groupId>
    <artifactId>r2dbc-pool</artifactId>
    <version>0.8.7.RELEASE</version>
</dependency>
```

For Connector/R2DBC 1.2:

```xml
<dependency>
    <groupId>io.r2dbc</groupId>
    <artifactId>r2dbc-pool</artifactId>
    <version>0.9.0.M2</version>
</dependency>
```

1. Run Maven to build your application:

```bash
$ mvn package
```

During the build process, Maven downloads and installs MariaDB Connector/R2DBC and other dependencies from the relevant repositories. After the build process completes and the MariaDB Connector/R2DBC has been installed, it can be used in a Java application.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
