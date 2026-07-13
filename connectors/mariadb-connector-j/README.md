---
description: >-
  Explore MariaDB Connector/J, the official JDBC driver for Java applications to
  connect to MariaDB and MySQL databases.
icon: link
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# Connector/J

MariaDB Connector/J is the official JDBC driver for connecting Java applications to MariaDB and MySQL databases. It is LGPL licensed.

{% columns %}
{% column %}
{% content-ref url="about-mariadb-connector-j.md" %}
[about-mariadb-connector-j.md](about-mariadb-connector-j.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/J guide: JDBC driver reference covering connections, prepared statements, and transactions, plus Java version compatibility.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="failover-and-high-availability-with-mariadb-connector-j-for-2x-driver.md" %}
[failover-and-high-availability-with-mariadb-connector-j-for-2x-driver.md](failover-and-high-availability-with-mariadb-connector-j-for-2x-driver.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Failover and load balancing in MariaDB Connector/J 2.x support sequential, loadbalance, replication, and aurora modes across multi-master, master-slave, and Amazon Aurora clusters.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="failover-and-high-availability-with-mariadb-connector-j.md" %}
[failover-and-high-availability-with-mariadb-connector-j.md](failover-and-high-availability-with-mariadb-connector-j.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/J 3.0 and later support failover and high availability through sequential, loadbalance, replication, and load-balance-read modes with optional transaction replay.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="gssapi-authentication-with-mariadb-connector-j.md" %}
[gssapi-authentication-with-mariadb-connector-j.md](gssapi-authentication-with-mariadb-connector-j.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/J supports GSSAPI authentication via the server `gssapi` plugin, using JAAS on Unix or a Waffle-based native Windows implementation for Kerberos ticket validation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installing-mariadb-connectorj.md" %}
[installing-mariadb-connectorj.md](installing-mariadb-connectorj.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Install MariaDB Connector/J with a package manager (Maven or Gradle) or manually from the downloaded JAR file.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="java-connector-using-gradle.md" %}
[java-connector-using-gradle.md](java-connector-using-gradle.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Add MariaDB Connector/J to a Gradle project by declaring the `mariadb-java-client` dependency in `build.gradle`, then connect to MariaDB using standard JDBC DriverManager methods.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="java-connector-using-maven.md" %}
[java-connector-using-maven.md](java-connector-using-maven.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Add MariaDB Connector/J to a Maven project by declaring the `mariadb-java-client` dependency in `pom.xml`, then connect to MariaDB using standard JDBC DriverManager methods.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="option-batchmultisend-description.md" %}
[option-batchmultisend-description.md](option-batchmultisend-description.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
`useBatchMultiSend` enables bulk batch execution in MariaDB Connector/J, grouping `executeBatch` calls into multi-query packets to reduce round-trips between client and server.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="pool-datasource-implementation.md" %}
[pool-datasource-implementation.md](pool-datasource-implementation.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/J provides `MariaDbDataSource` and `MariaDbPoolDataSource` implementations with configurable pool size, idle timeout, validation delay, and JMX monitoring support.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="using-tls-ssl-with-mariadb-java-connector.md" %}
[using-tls-ssl-with-mariadb-java-connector.md](using-tls-ssl-with-mariadb-java-connector.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure TLS and SSL for MariaDB Connector/J using `sslMode`, `serverSslCert`, and `keyStore` options, supporting trust, verify-ca, verify-full, and zero-configuration encryption modes.
{% endcolumn %}
{% endcolumns %}
