---
description: >-
  Dictionary-based cache data compression in GridGain using Zstandard or gzip,
  including configuration, ZSTD dictionary tuning, and limitations.
---

# Data Compression

GridGain supports dictionary-based cache data compression using [Zstandard library](https://github.com/facebook/zstd) or [gzip algorithm](http://www.gzip.org/). Gzip compression is also supported on z/OS. To enable compression, add `gridgain-compress` Maven dependency to your project or move the `gridgain-compress` folder from `{gridgain}/libs/optional` to `{gridgain}/libs` when using ZIP archive:

{% hint style="info" %}
Cache Data Compression feature is available only with GridGain Ultimate Edition.
{% endhint %}

{% tabs %}
{% tab title="pom.xml" %}
```xml
<dependencies>
    ...
    <dependency>
        <groupId>org.gridgain</groupId>
        <artifactId>gridgain-compress</artifactId>
        <version>${gridgain.version}</version>
    </dependency>
</dependencies>
```
{% endtab %}

{% tab title="ZIP archive" %}
```bash
$ mv ./libs/optional/gridgain-compress ./libs/
```
{% endtab %}
{% endtabs %}

You can enable it on per-cache basis by setting `CacheConfiguration.setEntryCompressionConfiguration(new ZstdDictionaryCompressionConfiguration)` or `CacheConfiguration.setEntryCompressionConfiguration(new GzipCompressionConfiguration)`. When any cache data is created or updated, its key and value may be transparently compressed. When the data is accessed, it is transparently decompressed. No change in the behavior of user code is expected when enabling or disabling data compression.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="cacheConfiguration">
        <bean class="org.apache.ignite.configuration.CacheConfiguration">
            <property name="name" value="compressedCache"/>
            <property name="entryCompressionConfiguration">
                <bean class="org.gridgain.grid.cache.compress.ZstdDictionaryCompressionConfiguration">
                    <!-- Default values for all properties listed below. -->
                    <property name="compressKeys" value="false"/>
                    <property name="requireDictionary" value="true"/>
                    <property name="dictionarySize" value="1024"/>
                    <property name="samplesBufferSize" value="#{4 * 1024 * 1024}"/>
                    <property name="compressionLevel" value="2"/>
                </bean>
            </property>
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
```
{% endtab %}

{% tab title="Java" %}
```java
CacheConfiguration cfg = new CacheConfiguration();
cfg.setName("compressedCache");

ZstdDictionaryCompressionConfiguration compressionCfg = new ZstdDictionaryCompressionConfiguration();
// Default values for all properties listed below:
compressionCfg.setCompressKeys(false);
compressionCfg.setRequireDictionary(true);
compressionCfg.setDictionarySize(1024);
compressionCfg.setSamplesBufferSize(4 * 1024 * 1024);
compressionCfg.setCompressionLevel(2);

cfg.setEntryCompressionConfiguration(compressionCfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Data compression sometimes yields only modest size savings due to data entropy. High-entropy data is typically encountered in encrypted or random data, such as UUID values. The savings are even lower for smaller partitions due to ZIP overhead. See [performance and tuning tips](../../ha-and-performance/performance-tuning/general-tips.md#recommended-high-performance-settings) for more information.
{% endhint %}

## Performance Considerations

Data compression allows saving RAM and disk space by storing compressed data in cache entries, at the cost of spending CPU time on compression and decompression. Enabling data compression leads to reduced Off-Heap utilization and checkpoint directory size, as well as slightly shorter WAL. If native persistence is used, it is possible to save space while improving performance at the same time if the load pattern is I/O bound.

## ZSTD Compression configuration

### Configuring Dictionary

External dictionary use is based on the assumption that cache data items are small and have similar structure and content. Thus a pre-trained dictionary allows a decent compression ratio of 40% to 60% on real-world samples that otherwise see little to no benefit from compression. With default settings, GridGain collects values as samples when they are added to the cache. When enough samples are accumulated, a dictionary is trained based on these samples. After the dictionary is ready, it is applied to every new value. The value is stored in the compressed form if it yields sufficient benefit over plain serialized form. Some values are collected as samples after a dictionary is trained, and a new dictionary is trained periodically. If this new dictionary shows greater benefit than the existing one, it is used onwards; otherwise, it is discarded. Dictionaries are kept alongside cache data.

A separate set of samples and dictionaries is kept for each individual cache, unless it is a part of the [cache group](cache-groups.md), in which case they are shared between all caches in the group.

{% hint style="info" %}
Keys are not compressed by default since they are usually shorter than values. Common usage patterns have frequent key access, leading to higher performance cost of compressing keys combined with smaller benefit. It is possible to enable key compression by setting the `compressKeys` property.
{% endhint %}

The default dictionary size is `1024` bytes. As a heuristic, dictionary size should be on par with the average value size in the cache. It can be specified by setting the `dictionarySize` property. Longer dictionaries lead to increased performance cost but potentially better compression ratio. The recommended range of dictionary size is `264` to `16384` bytes.

As per the underlying algorithm, it is possible to specify the compression level by setting the `compressionLevel` property. The default value is `2`, which combines decent compression performance and ratio. Tuning compression level is usually less important than choosing the best dictionary size. You may also change the length of buffer used to accumulate samples for dictionary training by modifying the `samplesBufferSize` property. The samples are held on a heap, with a total size of 4 megabytes by default. You may decrease it to have smaller heap usage and train the dictionary faster or increase it to have a slightly better compression ratio (especially in the case of larger `dictionarySize` values).

### Compression Without Dictionary

The `requireDictionary` property is `true` by default, meaning that a dictionary is required to compress data. Suppose you set this property to `false`. In that case, when the dictionary is not ready, data that is added to the cache will be compressed without a dictionary and stored in the compressed form if it yields sufficient benefit after compression. As soon as a dictionary is ready, it is always used. If the values stored in the cache are large and self-contained, you may also set `dictionarySize` to `0`. In this mode of operation, no samples are collected; the dictionary is never trained or used.

{% hint style="info" %}
It is recommended to use compression without a dictionary if your cache values are larger than 16 kilobytes.
{% endhint %}

## Using Compression with Snapshots

You can use GZIP compression and ZSTD compression with `dictionaryRequired=false dictionarySize=0` fields specified to create caches for nodes with snapshots. You cannot use ZSTD compression with `dictionarySize` field above to create caches for nodes with snapshots.

## Limitations

Currently, enabling data compression for a cache disables the [historical rebalancing](../../architecture/rebalancing/historical-rebalancing.md) of that cache. Full partition rebalance is used instead.

If the `compressKeys` property is set, the data key and data value are considered for compression separately. The key may end up compressed, but the value will not, or vice versa. The same dictionary is used for the compression of both keys and values.

Currently, only [binary objects](../../architecture/data-modeling/introduction.md#binary-object-format) will be compressed. This covers most of the usage patterns: POJO classes, SQL tables, and BinaryObject. Primitive types are not compressed. Therefore, if `String` or `byte[]` is desired to be used as a compressed key/value type, it needs to be stored as an object field.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
