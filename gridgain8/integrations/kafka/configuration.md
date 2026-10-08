---
description: >-
  Configuration reference for the GridGain Kafka Source and Sink Connectors, including failover policy, schema, filtering, and error handling settings.
---

# Kafka Connector Configuration

Both the Source and Sink Kafka Connectors are self-documenting. The below configuration reference is captured from `IgniteSourceConnectorConfig.conf().toRst()` and `IgniteSinkConnectorConfig.conf().toRst()` methods output.

{% hint style="info" %}
**Same Settings for All Caches**

Both the Sink and Source Connectors support multiple caches and all the settings below are used for all the caches. This minimizes the amount of configuration and encourages consistency but it can happen you need different settings for different caches. A workaround is deploying multiple instances of the Connector with different configuration files.
{% endhint %}

## Source Connector

`failoverPolicy`

The mode of handling Kafka Connect Worker failover and rebalancing. The options are:

**NONE**: the Ignite cache updates that happened during the Connector downtime due to failover or rebalancing are lost. This option provides maximum performance.

**FULL_SNAPSHOT**: pull all data from the Ignite caches each time the Connector starts. This option prevents data loss but is feasible only for small caches.

**BACKLOG**: resume from the last committed offset. The Connector creates a special Kafka Backlog cache in Ignite where data from all caches are replicated and assigned offsets.The data is pulled from the Kafka Backlog. This option prevents data loss but consumes additional Ignite resources to manage the Kafka backlog cache and is less efficient due to extra data marshalling.

- Type: string
- Default: NONE
- Importance: high

`igniteCfg`

Path to the Ignite configuration file. `$IGNITE_HOME/config/default-config.xml` is used if no Ignite config is configured.

- Type: string
- Default: ""
- Importance: high

`shallLoadInitialData`

Whether to load data already existing in Ignite caches at the time the Connector starts.

- Type: boolean
- Default: `true`
- Importance: high

`shallProcessRemovals`

Set this setting to `true` to make the Connector process removals. In this case the Connector injects a record with a `null` value into Kafka to indicate that the key was removed.

- Type: boolean
- Default: `false`
- Importance: medium

`backlogCacheName`

Name of a backlog cache created in Ignite where data from all caches are replicated and assigned offsets. This setting is valid only when `failoverPolicy` is set to `BACKLOG`.

- Type: string
- Default: `kafka-connect-backlog`
- Importance: low

`backlogCacheBackups`

The number of backlog cache backups. Setting this property to a value higher than 0 prevents partition loss if a node becomes unstable.

- Type: int
- Default: `1`
- Importance: low

`backlogFlushFreq`

Frequency in milliseconds that the Backlog service flushes data to the Backlog cache. `0` means the setting is disabled. This setting is valid only when `failoverPolicy` is set to `BACKLOG`.

- Type: int
- Default: `500`
- Importance: low

`backlogMemoryRegionName`

Name of a memory region used to store backlog cache in Ignite. This setting is valid only when `failoverPolicy` is set to `BACKLOG`.

- Type: string
- Default: `kafka-connect`
- Importance: low

{% hint style="info" %}
Make sure the `kafka-connect` region exists. Alternatively, change the default region in the `backlogMemoryRegionName` property to an existing (desired) one.
{% endhint %}

`backlogServiceName`

Name of a backlog service that manages backlog cache in Ignite. This setting is valid only when `failoverPolicy` is set to `BACKLOG`.

- Type: string
- Default: `kafka-connect-backlog-service`
- Importance: low

`batchSize`

Maximum number of entries to send to Kafka in single batch.

- Type: int
- Default: `10000`
- Importance: low

`cacheBlacklist`

List of regular expressions to match against names of caches to exclude from copying. If both `cacheWhitelist` and `cacheBlacklist` are specified, then `cacheWhitelist` is analysed first.

- Type: list
- Default: `null`
- Importance: low

`cacheFilter`

Class name of a custom `java.util.function.Predicate<org.gridgain.kafka.CacheEntry>` implementation to filter data pulled from Ignite caches.

- Type: class
- Default: `null`
- Importance: low

`cacheListPollInterval`

Frequency in milliseconds to poll for the latest list of caches existing in Ignite.

- Type: long
- Default: `5000`
- Importance: low

`cacheWhitelist`

List of regular expressions to match against names of caches to copy data from.

- Type: list
- Default: `null`
- Importance: low

`enableSchemaCache`

Set this property to `true` to allow caching resolved kafka schemas. This can be useful in case when same cache can have objects with different binary schemas, so schemas caching can help us to avoid performing resolution for every incoming object.

- Type: boolean
- Default: `false`
- Importance: low

`enumPolicy`

Specifies how enums mapped to Kafka schema. Possible values are:

**ORDINAL**: Use Enum's ordinal value.

**SHORT_NAME**: Use only the name of enum element, for example `BAR`.

**LONG_NAME**: Use the class name of enum element name, for example `Foo.BAR`.

**FULL_NAME**: Use the full name of enum element, for example `org.acme.Foo.BAR`.

- Type: string
- Default: `SHORT_NAME`
- Importance: low

`fieldNullabilityPolicy`

Specifies how null fields mapped to Kafka schema. Possible values are:

**LAZY**: Return `null` for null fields.

**EAGER**: Try to resolve the schema based on available metadata (binary type metadata or pojo field class).

- Type: string
- Default: `LAZY`
- Importance: low

`isSchemaDynamic`

By default, key and value schemas are created once and cached. Set this property to `true` to detect schema changes.

- Type: boolean
- Default: `false`
- Importance: low

`isSchemaless`

By default, source connector generates cache key and value schemas. Set this property to `true` to disable schema generation, which improves performance but does not allow non-Ignite sink connectors to understand the data structure.

- Type: boolean
- Default: `false`
- Importance: low

`pollInterval`

Frequency in milliseconds to poll for new data in each cache.

- Type: long
- Default: `2000`
- Importance: low

`schemaCacheMaxSize`

Maximum capacity of resolved schemas cache. This setting is valid only when `enableSchemaCache` is set to `true`.

- Type: int
- Default: 256
- Importance: low

`schemaCacheTtl`

Time in milliseconds, since last entry access, after which this entry will be evicted from cache. Negative value means that not TTL would be applied. This setting is valid only when `enableSchemaCache` is set to `true`.

- Type: int
- Default: -1
- Importance: low

`topicPrefix`

The connector pulls data from Ignite caches into Kafka topics named by prefixing the cache names with this prefix.

- Type: string
- Default: ""
- Importance: low

`errorHandlingPolicy`

How the source connector handles errors during cache entry processing (e.g., schema resolution, key/value transformations, etc.). The options are:

**LOG_ONLY**: Log problematic entry and skip it.

**STOP_TASK**: Log problematic entry and transfer control to Kafka Connect, which effectively stops the source task (similar to the default Kafka Connect behavior).

- Type: string
- Default: STOP_TASK
- Importance: low

## Sink Connector


`igniteCfg`

Path to the Ignite configuration file. `$IGNITE_HOME/config/default-config.xml` is used if no Ignite config is configured.

- Type: string
- Default: ""
- Importance: high

`shallProcessUpdates`

Indicates if overwriting or removing existing values in the sink cache is enabled. Sink connector performs better if this flag is disabled.

- Type: boolean
- Default: `false`
- Importance: medium

`cacheFilter`

Class name of a custom `java.util.function.Predicate<org.gridgain.kafka.CacheEntry>` implementation to filter data pushed to Ignite caches.

- Type: class
- Default: `null`
- Importance: low

`cachePrefix`

Sink cache name is built from this prefix and kafka topic without topic prefix. For example, if topic is `ignite.person`, `topicPrefix` is `ignite.` and `cachePrefix` is `ignite-` then sink cache name is `ignite-person`.

- Type: string
- Default: ""
- Importance: low

`flushOnOffsetCommit`

Set this setting to true to make the Connector flush records to Ignite by batches on kafka offset commit. By default flush executed after each processed record.

- Type: boolean
- Default: `false`
- Importance: low

`keyFields`

A comma-separated list of field names to use for the Ignite cache key. Not applicable if `keyPolicy` is set to `kafka`. All fields are used if the setting is not specified.

- Type: list
- Default: ""
- Importance: low

`keyPolicy`

Specifies what data to use for the Ignite cache key. The options are:

**key**: Fields from the record key are used.

**value**: Fields from the record key are used.

**kafka**: Ignite Binary Object having 3 fields - Kafka record's topic, partition, and offset - is used as the cache key.

- Type: string
- Default: `key`
- Importance: low

`pushInterval`

Frequency in milliseconds to push data to Ignite.

- Type: long
- Default: `2000`
- Importance: low

`topicPrefix`

Kafka topic is built from this prefix and cache name.

- Type: string
- Default: `ignite-`
- Importance: low

`errorHandlingPolicy`

How the connector handles errors during sink record processing (e.g., malformed record, key inference failure, etc.). The options are:

**LOG_ONLY**: Log problematic entry and skip it.

**STOP_TASK**: Log problematic entry and transfer control to Kafka Connect, which effectively stops the sink task (similar to the default Kafka Connect behavior).

- Type: string
- Default: STOP_TASK
- Importance: low
