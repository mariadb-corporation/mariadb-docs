---
description: >-
  Complete MariaDB installation guide. Complete setup instructions for Linux,
  Windows, and macOS with configuration and verification for production use.
---

# Installing MariaDB Connector/J

{% hint style="info" %}
The most recent [_**Stable**_](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/release-criteria) _**(GA)**_ release of [MariaDB Connector/J](../connectors-quickstart-guides/mariadb-connector-j-guide.md) is:[**MariaDB Connector/J 3.5.3**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/java/3.5/3.5.3)
{% endhint %}

[Download MariaDB Connector/J](https://mariadb.com/downloads/connectors/)

## Installing MariaDB Connector/J with a Package Manager

The recommended way to install MariaDB Connector/J is to use a package manager like [Maven](https://maven.apache.org/what-is-maven.html) or [Gradle](https://gradle.org/).

### Installing MariaDB Connector/J with Maven

To install MariaDB Connector/J with [Maven](https://maven.apache.org/what-is-maven.html), add the following dependency to your `pom.xml` configuration file:

```xml
<dependency> 
<groupId>org.mariadb.jdbc</groupId>
<artifactId>mariadb-java-client</artifactId>
<version>$VERSION</version>
</dependency>
```

Ensure to replace the  `$VERSION` with a valid MariaDB Connector/J version number. See [About MariaDB Connector/J: Java Compatibility](about-mariadb-connector-j.md) to determine which MariaDB Connector/J release series supports your Java version.

### Installing MariaDB Connector/J with Gradle

To install MariaDB Connector/J with [Gradle](https://gradle.org/), add the following dependency to your `build.gradle` configuration file:

```java
implementation 'org.mariadb.jdbc:mariadb-java-client:$VERSION'
```

Ensure to replace the  `$VERSION` with a valid MariaDB Connector/J version number. See [About MariaDB Connector/J: Java Compatibility](about-mariadb-connector-j.md) to determine which MariaDB Connector/J release series supports your Java version.

[Gradle configuration](java-connector-using-gradle.md).

## Installing MariaDB Connector/J Manually with the JAR File

It is not generally the recommended method, but MariaDB Connector/J can also be installed by manually installing the `.jar` file to a directory in your [CLASSPATH](https://docs.oracle.com/javase/tutorial/essential/environment/paths.html). MariaDB Connector/J `.jar` files can be downloaded from the following URL:

* [https://mariadb.com/downloads/connectors/](https://mariadb.com/downloads/connectors/)

## Installing MariaDB Connector/J from Source

This section deals with building the connector from the source and testing it. If you have downloaded a ready-built connector in the package as a jar file, then this section may be skipped.

The source code is available at the [mariadb-connector-j repository](https://github.com/MariaDB/mariadb-connector-j) on GitHub. You can clone it by executing the following:

```bash
git clone https://github.com/MariaDB/mariadb-connector-j.git
```

If you would prefer a packaged source tarball release, then MariaDB Connector/J `.jar` source code tarballs can be downloaded from the following URL:

* [https://downloads.mariadb.org/connector-java/](https://downloads.mariadb.org/connector-java/)

MariaDB Connector/J has the following build requirements:

* [Maven](https://maven.apache.org/what-is-maven.html)
* Java JDK

If you would like to run the unit tests, then you'll need a MariaDB or MySQL server. It has to meet the following requirements:

* It must be listening on `localhost` a TCP port `3306`.
* It must have a database called `testj`.
* It must have a `root` user account with an empty password.

If you would like to build MariaDB Connector/J and run the unit tests, then execute the following:

```bash
mvn package
```

If you would like to build MariaDB Connector/J without running the unit tests, then execute the following:

```bash
mvn -Dmaven.test.skip=true package
```

Once the build is complete, you should have a `.jar` file with a name like the one `mariadb-java-client-x.y.z.jar` in the `target` subdirectory.

{% @marketo/form formId="4316" %}
