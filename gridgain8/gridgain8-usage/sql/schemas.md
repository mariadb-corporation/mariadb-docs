---
description: >-
  GridGain provides default schemas and supports custom schemas, defined in configuration or created automatically for each cache.
---

# Understanding Schemas

## Overview

GridGain has a number of default schemas and supports creating custom schemas.

There are two schemas that are available by default:

- The IGNITE schema, which contains a number of system views with information about cluster nodes. You can't create tables in this schema. Refer to the [System Views](../../reference/monitoring/system-views.md) page for further information.
- The [PUBLIC schema](#public-schema), which is used by default whenever a schema is not specified.

Custom schemas are created in the following cases:

- You can specify custom schemas in the cluster configuration. See [Custom Schemas](#custom-schemas).
- GridGain creates a schema for each cache created via one of the programming interfaces or XML configuration. See [Cache and Schema Names](#cache-and-schema-names).

## PUBLIC Schema

The PUBLIC schema is used by default whenever a schema is required and is not specified. For example, when you connect to the cluster via JDBC without setting the schema explicitly, you will connect to the PUBLIC schema.

## Custom Schemas

Custom schemas can be set via the `sqlSchemas` property of `IgniteConfiguration`. You can specify a list of schemas in the configuration before starting your cluster and then create objects in these schemas at runtime.

Below is a configuration example with two custom schemas.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="sqlConfiguration">
        <bean class="org.apache.ignite.configuration.SqlConfiguration">
            <property name="sqlSchemas">
                <list>
                    <value>MY_SCHEMA</value>
                    <value>MY_SECOND_SCHEMA</value>
                </list>
            </property>
        </bean>
    </property>
</bean>
```
{% endtab %}
{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();

SqlConfiguration sqlCfg = new SqlConfiguration();

sqlCfg.setSqlSchemas("sqlSchemas");
        
cfg.setSqlConfiguration(sqlCfg);
        
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration
{
    SqlSchemas = new[]
    {
        "MY_SCHEMA",
        "MY_SECOND_SCHEMA"
    }
};
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

To connect to a specific schema via, for example, a JDBC driver, provide the schema name in the connection string:

```text
jdbc:ignite:thin://127.0.0.1/MY_SCHEMA
```

## Cache and Schema Names

When you create a cache with [queryable fields](sql-api.md#configuring-queryable-fields), you can manipulate the cached data using the [SQL API](sql-api.md). In SQL terms, each such cache corresponds to a separate schema whose name equals the name of the cache.

Similarly, when you create a table via a DDL statement, you can access it as a key-value cache via GridGain's supported programming interfaces. The name of the corresponding cache can be specified by providing the `CACHE_NAME` parameter in the `WITH` part of the `CREATE TABLE` statement.

```sql
CREATE TABLE City (
  ID INT(11),
  Name CHAR(35),
  CountryCode CHAR(3),
  District CHAR(20),
  Population INT(11),
  PRIMARY KEY (ID, CountryCode)
) WITH "backups=1, CACHE_NAME=City";
```

See the [CREATE TABLE](../../reference/sql/ddl.md#create-table) page for more details.

If you do not use this parameter, the cache name is defined in the following format (in capital letters):

```
SQL_<SCHEMA_NAME>_<TABLE_NAME>
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
