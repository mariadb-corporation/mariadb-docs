---
description: >-
  How memory quotas prevent GridGain nodes from running out of memory when SQL
  queries return large result sets, including global and per-query quotas and offloading.
---

# Memory Quotas for SQL Queries

Memory quotas are a mechanism for preventing GridGain nodes from running out of memory when executing SQL queries that
return large result sets. A query loads objects from caches into memory. If there are too many objects, or the objects
are too large, the JVM can easily run out of memory. With memory quotas, the SQL engine imposes a limit on the heap
memory available to queries and handle the query if the limit is reached.

Memory quota size can be configured in:

- Kilobytes - append 'K' or 'k', for example: `10k`, `400K`;
- Megabytes - append 'M' or 'm', for example: `60m`, `420M`;
- Gigabytes - append 'G' or 'g', for example: `7g`, `2G`;
- Percent of heap - append the '%' sign, for example: `45%`, `80%`.

The SQL engine can handle the situation when the limit is reached in two ways, depending on
if [query offloading](#query-offloading) is enabled:

- If query offloading is disabled, the SQL engine throws an `IgniteSQLException` letting the user application
react accordingly.
- If query offloading is enabled, the query data is offloaded to disk, and the query is eventually executed.

Quotas are configured for each node individually.
You can have different limits on different nodes, depending on the amount of RAM available to the nodes.
It is important to remember that queries are
[distributed to multiple nodes in a map-reduce manner](../../gridgain8-usage/sql/sql-introduction.md#distributed-queries),
and any part of the query can exceed the quota on the node where it's executed.

{% hint style="warning" %}
If your GridGain cluster is protected by authorization, only users with the
`SET_QUERY_MEMORY_QUOTA` [security permission](../../security/authorization-permissions.md#supported-permissions) can change memory quotas.
{% endhint %}

When the limit is reached, GridGain prints an error message to the log similar to the one below:

```
SEVERE: Failed to execute local query.
org.apache.ignite.cache.query.exceptions.SqlMemoryQuotaExceededException: SQL query ran out of memory: Global quota was exceeded.
    at org.apache.ignite.internal.processors.query.h2.QueryMemoryManager.onQuotaExceeded(QueryMemoryManager.java:214)
    at org.apache.ignite.internal.processors.query.h2.QueryMemoryManager.reserve(QueryMemoryManager.java:151)
    at org.apache.ignite.internal.processors.query.h2.QueryMemoryTracker.reserveFromParent(QueryMemoryTracker.java:154)
    at org.apache.ignite.internal.processors.query.h2.QueryMemoryTracker.reserve(QueryMemoryTracker.java:124)
    at org.apache.ignite.internal.processors.query.h2.QueryMemoryTracker$ChildMemoryTracker.reserve(QueryMemoryTracker.java:361)
    at org.apache.ignite.internal.processors.query.h2.H2ManagedLocalResult.hasAvailableMemory(H2ManagedLocalResult.java:115)
    at org.apache.ignite.internal.processors.query.h2.H2ManagedLocalResult.addRow(H2ManagedLocalResult.java:360)
    at org.h2.command.dml.Select.queryFlat(Select.java:752)
    at org.h2.command.dml.Select.queryWithoutCache(Select.java:903)
    at org.h2.command.dml.Query.queryWithoutCacheLazyCheck(Query.java:151)
    at org.h2.command.dml.Query.query(Query.java:415)
    at org.h2.command.dml.Query.query(Query.java:397)
    at org.h2.command.CommandContainer.query(CommandContainer.java:145)
    at org.h2.command.Command.executeQuery(Command.java:202)
    at org.h2.jdbc.JdbcPreparedStatement.executeQuery(JdbcPreparedStatement.java:115)
    at org.apache.ignite.internal.processors.query.h2.IgniteH2Indexing.executeSqlQuery(IgniteH2Indexing.java:817)
    at org.apache.ignite.internal.processors.query.h2.IgniteH2Indexing.executeSqlQueryWithTimer(IgniteH2Indexing.java:924)
    at org.apache.ignite.internal.processors.query.h2.twostep.GridMapQueryExecutor.onQueryRequest0(GridMapQueryExecutor.java:421)
    at org.apache.ignite.internal.processors.query.h2.twostep.GridMapQueryExecutor.onQueryRequest(GridMapQueryExecutor.java:247)
    at org.apache.ignite.internal.processors.query.h2.IgniteH2Indexing.onMessage(IgniteH2Indexing.java:2259)
    at org.apache.ignite.internal.processors.query.h2.twostep.GridReduceQueryExecutor$1.applyx(GridReduceQueryExecutor.java:152)
    at org.apache.ignite.internal.processors.query.h2.twostep.GridReduceQueryExecutor$1.applyx(GridReduceQueryExecutor.java:147)
    at org.apache.ignite.internal.util.lang.IgniteInClosure2X.apply(IgniteInClosure2X.java:37)
    at org.apache.ignite.internal.processors.query.h2.IgniteH2Indexing.send(IgniteH2Indexing.java:2384)
    at org.apache.ignite.internal.processors.query.h2.twostep.GridReduceQueryExecutor.send(GridReduceQueryExecutor.java:1151)
    at org.apache.ignite.internal.processors.query.h2.twostep.GridReduceQueryExecutor.query(GridReduceQueryExecutor.java:473)
    at org.apache.ignite.internal.processors.query.h2.IgniteH2Indexing$7.iterator(IgniteH2Indexing.java:1769)
    at org.apache.ignite.internal.processors.cache.QueryCursorImpl.iter(QueryCursorImpl.java:101)
    at org.apache.ignite.internal.processors.cache.query.RegisteredQueryCursor.iter(RegisteredQueryCursor.java:73)
    at org.apache.ignite.internal.processors.cache.QueryCursorImpl.getAll(QueryCursorImpl.java:120)
    at com.gridgain.test.MemoryQuotasTest.testQueryQuotas(MemoryQuotasTest.java:79)
    at com.gridgain.test.MemoryQuotasTest.main(MemoryQuotasTest.java:45)
```

Refer to the [documentation on using SQL queries](../../gridgain8-usage/sql/sql-api.md#preventing-outofmemory-exceptions)
for more information on how to catch this exception.

## Global Memory Quota

By default, a global quota for SQL queries is set to 60% of the heap memory available to the node.
It means that the total amount of memory required for multiple queries running simultaneously cannot exceed that amount.
The query that requests additional memory beyond the configured limit is handled by the SQL engine according to
the [offloading property](#query-offloading).

You can change the global limit as follows:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

    <property name="sqlConfiguration">
        <bean class="org.apache.ignite.configuration.SqlConfiguration">

            <property name="sqlGlobalMemoryQuota" value="300M"/>

            <property name="sqlQueryMemoryQuota" value="30M"/>
            <property name="sqlOffloadingEnabled" value="true"/>

        </bean>
    </property>

    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <property name="ipFinder">

                <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                    <property name="addresses">
                        <list>
                            <value>127.0.0.1:47500..47509</value>
                        </list>
                    </property>
                </bean>
            </property>
        </bean>
    </property>
</bean>

            <property name="sqlGlobalMemoryQuota" value="300M"/>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();

SqlConfiguration sqlCfg = new SqlConfiguration().setSqlGlobalMemoryQuota("300M");

cfg.setSqlConfiguration(sqlCfg);

Ignite ignite = Ignition.start(cfg);

```
{% endtab %}

{% tab title="C#/.NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Memory Quota for a Single Query

You can set the limit of memory that is applied to every individual query.
The default value is 0 (no quota).
If any query exceeds the limit, the SQL engine handles the query according to the [offloading property](#query-offloading).
Memory quotas for queries take effect on the node where they are defined.

{% hint style="info" %}
The SQL engine always observes the global quota irrespective of whether individual query quotas are defined or
not. For example, if the global quota is set to 300M, you cannot have 3 concurrent queries with each using more than
100M even if the per-query quota allows for this.
{% endhint %}

You can configure the per-query quota as follows:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

    <property name="sqlConfiguration">
        <bean class="org.apache.ignite.configuration.SqlConfiguration">

            <property name="sqlGlobalMemoryQuota" value="300M"/>

            <property name="sqlQueryMemoryQuota" value="30M"/>
            <property name="sqlOffloadingEnabled" value="true"/>

        </bean>
    </property>

    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <property name="ipFinder">

                <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                    <property name="addresses">
                        <list>
                            <value>127.0.0.1:47500..47509</value>
                        </list>
                    </property>
                </bean>
            </property>
        </bean>
    </property>
</bean>

            <property name="sqlQueryMemoryQuota" value="30M"/>
```
{% endtab %}

{% tab title="Java" %}
```java
SqlConfiguration sqlCfg = new SqlConfiguration();

sqlCfg.setSqlQueryMemoryQuota("30M");

```
{% endtab %}

{% tab title="C#/.NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Query Offloading

When a SQL query reaches its memory quota, the SQL engine can offload the query to disk instead of throwing an exception.
This means that the objects that have been already loaded to memory as a result of the query execution are saved to
disk and the occupied memory is freed. This process may affect the query execution performance, but won't stop the query.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

    <property name="sqlConfiguration">
        <bean class="org.apache.ignite.configuration.SqlConfiguration">

            <property name="sqlGlobalMemoryQuota" value="300M"/>

            <property name="sqlQueryMemoryQuota" value="30M"/>
            <property name="sqlOffloadingEnabled" value="true"/>

        </bean>
    </property>

    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <property name="ipFinder">

                <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                    <property name="addresses">
                        <list>
                            <value>127.0.0.1:47500..47509</value>
                        </list>
                    </property>
                </bean>
            </property>
        </bean>
    </property>
</bean>

            <property name="sqlQueryMemoryQuota" value="30M"/>
            <property name="sqlOffloadingEnabled" value="true"/>
```
{% endtab %}

{% tab title="Java" %}
```java
sqlCfg.setSqlOffloadingEnabled(true);

```
{% endtab %}

{% tab title="C#/.NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

When query offloading is enabled, GridGain uses the `$IGNITE_WORK_DIR/tmp/spill` directory to temporarily store
query data for the queries that exceed the quota.
Read more about the `$IGNITE_WORK_DIR` directory [here](../../gridgain8-usage/setup.md#configuring-work-directory).

## Using JMX to Set Memory Quotas

You can view and change the values of memory quotas at runtime using the following JMX Bean.

**Mbean's Object Name:**

```
group="SQL Query",name=SqlQueryMXBeanImpl
```

| Attribute | Type | Description | Scope |
|---|---|---|---|
| SqlGlobalMemoryQuota | String | The value of the global memory quota. | Node |
| SqlQueryMemoryQuota | String | The value of the per-query memory quota. | Node |
| SqlOffloadingEnabled | Boolean | Enable query off-loading. | Node |

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
