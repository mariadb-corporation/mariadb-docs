---
description: >-
  Set up a Java project for GridGain 9 — add the GridGain repository and the
  client dependency, and learn which GridGain modules to add for each feature.
---

# Project Setup and Required Modules

This page describes how to set up a Java project for GridGain 9, and which GridGain modules you should add as dependencies.

## Prerequisites

{% include "../../.gitbook/includes/prereqs-java.md" %}

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
    <version>9.1</version>
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

## Required Modules

The following table lists the GridGain modules an application developer adds as dependencies. Add `ignite-client` for any thin-client application; add the other modules only when you use the corresponding feature or integration.

| Artifact ID | Add it when you use | Reference |
| --- | --- | --- |
| `ignite-client` | Table API, Key-Value API, SQL API, Compute, Transactions, Catalog, Data Streamer, Continuous Queries — any thin-client application. | [Java Client](clients/java.md) |
| `ignite-jdbc` | The JDBC driver to connect over SQL. | [JDBC Driver](clients/jdbc-driver.md) |
| `gridgain-jdbc-cache-store` | An external JDBC cache store. | [Cache](cache.md) |
| `gridgain-map-structure` | Distributed map data structures (the `org.gridgain.structure` API), in addition to `ignite-client`. | [Distributed Map](data-structures/map-structure.md) |
| `gridgain-hibernate` | Hibernate ORM integration. | [Hibernate](../extensions/hibernate.md) |
| `spring-data-ignite` | Spring Data integration. | [Spring Data](../extensions/spring-data.md) |
| `spring-boot-starter-ignite-client` | Spring Boot autoconfiguration for the client. | [Spring Boot](../extensions/spring-boot.md) |

{% hint style="info" %}
The `gridgain-hibernate`, `spring-data-ignite`, and `spring-boot-starter-ignite-client` modules require JDK 17 or later.
{% endhint %}

## Next Steps

- [Use Java API](../get-started/java-api.md) — an end-to-end example using the modules above.
- [Java Client](clients/java.md) — full client configuration reference.
- [Table API](table-api.md) — work with data once the client is connected.
