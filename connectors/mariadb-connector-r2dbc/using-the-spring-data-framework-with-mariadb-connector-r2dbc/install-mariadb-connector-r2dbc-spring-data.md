---
description: >-
  Install MariaDB Connector/R2DBC with Spring Data via Maven using
  spring-boot-starter-data-r2dbc; Spring Boot 3.0 and later manage the
  r2dbc-mariadb connector version automatically.
---

# Install MariaDB Connector/R2DBC (Spring Data)

### Overview

Spring Data R2DBC and MariaDB Connector/R2DBC are usually installed using Maven.

It should also be possible to install Spring Data R2DBC and MariaDB Connector/R2DBC by downloading the JAR files. Because Spring Data R2DBC has many dependencies we recommend using Maven, so that dependencies can be resolved by Maven.

### Install MariaDB Connector/R2DBC via Maven

1. To install Spring module for R2DBC, add the spring-boot-starter-data-r2dbc package dependency to your application's pom.xml file:

```xml
<dependency>
   <groupId>org.springframework.boot</groupId>
   <artifactId>spring-boot-starter-data-r2dbc</artifactId>
   <version>3.3.5</version>
</dependency>
```

1. Since spring boot 3.0, the MariaDB connector is defined as a possible dependency. So setting dependency just needs:

```xml
<dependency>
    <groupId>org.mariadb</groupId>
    <artifactId>r2dbc-mariadb</artifactId>
</dependency>
```

1. For spring boot before 3.0, a connector compatible with the R2DBC 0.9.1 spec needs to be set in place of org.mariadb:r2dbc-mariadb (be careful not to have any org.mariadb:r2dbc-mariadb dependency set):

```xml
<dependency>
    <groupId>org.mariadb</groupId>
    <artifactId>r2dbc-mariadb-0.9.1-spec</artifactId>
    <version>1.2.2</version>
</dependency>
```

1. To build your application, run Maven:

```bash
$ mvn package
```

During the build process, Maven downloads and installs MariaDB Connector/R2DBC and other dependencies from the relevant repositories.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>


{% @marketo/form formId="4316" %}
