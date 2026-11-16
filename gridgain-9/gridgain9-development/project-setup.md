---
description: >-
  Set up a Java project for GridGain 9 — add the GridGain repository and the
  client dependency, and learn which GridGain modules to add for each feature.
---

# Project Setup and Required Modules

This page describes how to set up a Java project for GridGain 9, and which GridGain modules you should add as dependencies.

## Prerequisites

{% include "../.gitbook/includes/prereqs-java.md" %}

## Adding the GridGain Repository

GridGain modules are published to the GridGain repository, not to Maven Central. Add the repository to your build before declaring any GridGain dependency.

{% tabs %}
{% tab title="Maven" %}
```xml
<repositories>
    <repository>
        <id>GridGain External Repository</id>
        <url>https://www.gridgainsystems.com/nexus/content/repositories/external</url>
    </repository>
</repositories>
```
{% endtab %}

{% tab title="Gradle" %}
```groovy
repositories {
    maven {
        url = "https://www.gridgainsystems.com/nexus/content/repositories/external"
    }
}
```
{% endtab %}
{% endtabs %}

## Adding the Client Dependency

The thin client provides the Table, Key-Value, SQL, Compute, Transactions, Catalog, and Data Streamer APIs used throughout the examples — the `org.apache.ignite.*` packages you see in the code samples. Add it as the single dependency for client applications:

{% tabs %}
{% tab title="Maven" %}
```xml
<dependency>
    <groupId>org.gridgain</groupId>
    <artifactId>ignite-client</artifactId>
    <version>9.1.28</version>
</dependency>
```
{% endtab %}

{% tab title="Gradle" %}
```groovy
implementation 'org.gridgain:ignite-client:9.1'
```
{% endtab %}
{% endtabs %}

All GridGain modules share the `org.gridgain` group ID and the `9.1` version. Always declare the version that matches your cluster.

### Managing Versions With the BOM

Starting with GridGain 9.2.0, a bill of materials (BOM), `org.gridgain:gridgain9-bom`, pins every GridGain 9 module to the same release version. Import the BOM once with the version that matches your cluster, and declare GridGain dependencies without a version. The BOM does not manage the versions of third-party libraries.

{% tabs %}
{% tab title="Maven" %}
```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.gridgain</groupId>
            <artifactId>gridgain9-bom</artifactId>
            <version>9.2.0</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>

<dependencies>
    <dependency>
        <groupId>org.gridgain</groupId>
        <artifactId>ignite-client</artifactId>
    </dependency>
</dependencies>
```
{% endtab %}

{% tab title="Gradle" %}
```groovy
dependencies {
    implementation platform('org.gridgain:gridgain9-bom:9.2.0')
    implementation 'org.gridgain:ignite-client'
}
```
{% endtab %}
{% endtabs %}

## Required Modules

The following table lists the GridGain modules an application developer adds as dependencies. Add `ignite-client` for any thin-client application; add the other modules only when you use the corresponding feature or integration.

| Artifact ID | Add it when you use | Reference |
| --- | --- | --- |
| `ignite-client` | Table API, Key-Value API, SQL API, Compute, Transactions, Catalog, Data Streamer, Continuous Queries — any thin-client application. | [Java Client](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/CjGYMsT2MVP4nd3IyW2L/clients/java) |
| `ignite-jdbc` | The JDBC driver to connect over SQL. | [JDBC Driver](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/CjGYMsT2MVP4nd3IyW2L/clients/jdbc-driver) |
| `gridgain-jdbc-cache-store` | An external JDBC cache store. | [Cache](caches.md) |
| `gridgain-map-structure` | Distributed map data structures (the `org.gridgain.structure` API), in addition to `ignite-client`. | [Distributed Map](data-structures/distributed-maps.md) |
| `gridgain-hibernate` | Hibernate ORM integration. | [Hibernate](../integrations/hibernate.md) |
| `spring-data-ignite` | Spring Data integration. | [Spring Data](../integrations/spring-data.md) |
| `spring-boot-starter-ignite-client` | Spring Boot autoconfiguration for the client. | [Spring Boot](../integrations/spring-boot.md) |

{% tabs %}
{% tab title="9.2" %}
{% hint style="info" %}
All modules require JDK 21 or later.
{% endhint %}
{% endtab %}

{% tab title="9.1" %}
{% hint style="info" %}
The `gridgain-hibernate`, `spring-data-ignite`, and `spring-boot-starter-ignite-client` modules require JDK 17 or later.
{% endhint %}
{% endtab %}
{% endtabs %}

## Next Steps

- [Use Java API](../gridgain9-get-started/java-api.md) — an end-to-end example using the modules above.
- [Java Client](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/CjGYMsT2MVP4nd3IyW2L/clients/java) — full client configuration reference.
- [Table API](table-api.md) — work with data once the client is connected.

## See Also

- [How to Configure Logging for the Java Thin Client](../gridgain9-get-started/how-to-guides/configuring-java-client-logging.md)
- [Connect With the Java Thin Client](../gridgain9-get-started/learning-paths/distributed-sql-foundations/connect-java-thin-client.md)

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
