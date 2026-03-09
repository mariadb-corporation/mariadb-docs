# Spider Status Variables

The following status variables are associated with the [Spider storage engine](../../../server-usage/storage-engines/spider/). See [Server Status Variables](server-status-variables.md) for a complete list of status variables that can be viewed with [SHOW STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-status.md).

See also the [Full list of MariaDB options, system and status variables](../../../reference/full-list-of-mariadb-options-system-and-status-variables.md).

#### `Spider_direct_aggregate`

* Description: Number of times direct aggregate has happened in spider. That is, in a partitioned spider table, instead of scanning individual rows in remote tables corresponding to partitions for aggregation functions like `SUM` and `COUNT`, spider forwards aggregate queries to these tables directly and aggregate the results.
* Scope: Global, Session
* Data Type: `numeric`

#### `Spider_direct_delete`

* Description:
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.3)

#### `Spider_direct_order_limit`

* Description:
* Scope: Global, Session
* Data Type: `numeric`

#### `Spider_direct_update`

* Description:
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.3)

#### `Spider_mon_table_cache_version`

* Description: The version of the spider monitoring table cache, always less than or equal to `Spider_mon_table_cache_version_req`. If the inequality is strict, then the cache is refreshed when the spider udf `spider_ping_table` is called. When the cache is refreshed, the value of `Spider_mon_table_cache_version` is brought up to be the same value as `Spider_mon_table_cache_version_req`.
* Scope: Global, Session
* Initial value: 0
* Data Type: `numeric`

#### `Spider_mon_table_cache_version_req`

* Description: The required version of the spider monitoring table cache. A call to the spider udf [spider\_flush\_table\_mon\_cache](../../../server-usage/storage-engines/spider/spider-functions/spider_flush_table_mon_cache.md) will cause its value to be incremented by one, thus ensuring a refresh of the cache will happen when needed.
* Scope: Global, Session
* Initial value: 1
* Data Type: `numeric`

#### `Spider_parallel_search`

* Description:
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.3)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
