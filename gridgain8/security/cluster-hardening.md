---
description: >-
  Harden a GridGain 8 cluster by preventing SQL injection with parameterized
  queries and switching to Spring 6.
---

# Cluster Hardening

## Avoiding SQL Injections

SQL injections are a common type of attack of databases. GridGain is protected from most common types of SQL injections, however the attackers may try to find a weak spot not yet covered. To reduce the risk, it is recommended to use parametrized queries.

If you are using the Java SQL API, use parametrized queries instead of plain text queries:

```java
IgniteCache<Long, Person> cache = ignite.cache("personCache");

cache.query(new SqlFieldsQuery("INSERT INTO Person(id, firstName, lastName) VALUES(?, ?, ?)").setArgs(1L,
		"John", "Smith")).getAll();
```

This way, GridGain treats each argument as a separate entity with a specific column to store it in, removing the threat of separate arguments forming malicious code.

If you are using JDBC, you can use `PreparedStatements` to achieve the same result:

```java
// Insert a Person with a Long key.
PreparedStatement stmt = conn
        .prepareStatement("INSERT INTO Person(_key, name, age) VALUES(CAST(? as BIGINT), ?, ?)");

stmt.setInt(1, 1);
stmt.setString(2, "John Smith");
stmt.setInt(3, 25);

stmt.execute();
```

## Switching to Spring 6

GridGain uses Spring 5 by default. This version has known vulnerabilities, however is supported for backwards compatibility. If your cluster is running Java 17 or later, you can switch to a more secure and up-to-date Spring 6.

### Local Installation

When running GridGain as a local installation, you need to enable the optional Spring 6 module:

- Delete or move the `{GRIDGAIN_HOME}/libs/ignite-spring` directory.
- Copy the [ignite-spring6 directory](../gridgain8-usage/setup.md#enabling-modules) from the `{GRIDGAIN_HOME}/libs/optional` directory to `{GRIDGAIN_HOME}/libs`. Do not rename it.

When you next start GridGain, it will automatically use Spring 6.

{% hint style="warning" %}
Make sure only one Spring module is in the `/libs` directory. If multiple Spring versions are there, a random one will be chosen leading to unexpected behavior.
{% endhint %}

### Docker Installation

To use Spring 6 in Docker, select the image with the `-spring6` postfix. This image will have Spring 6 enabled by default.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
