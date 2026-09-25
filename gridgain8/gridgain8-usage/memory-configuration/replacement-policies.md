---
description: >-
  Configuring page replacement in GridGain when Native Persistence is on, including
  the Random-LRU, Segmented-LRU, and CLOCK page replacement algorithms.
---

# Replacement Policies

When [Native Persistence](../../architecture/storage/native-persistence.md) is on and the amount of data, which Ignite stores on the disk, is bigger than the off-heap memory amount allocated for the data region, another page should be evicted from the off-heap to the disk to preload a page from the disk to the completely full off-heap memory. This process is called _page rotation_ or _page replacement_.

When Native Persistence is off, _eviction_ is used instead of _page replacement_. See the [Eviction Policies](eviction-policies.md) page for more information.

Page replacement is implemented as follows:

When Ignite requires a page, it tries to find this page in the off-heap memory. If the page is not currently in the off-heap memory (a page fault occurs), this page is preloaded from the disk. At the same time, when off-heap memory is already full, another page should be chosen to be replaced (to stored to the disk and evicted).

Ignite supports three algorithms to find pages to replace:

* Random-LRU algorithm;
* Segmented-LRU algorithm;
* CLOCK algorithm.

Page replacement algorithm can be configured by the `PageReplacementMode` property of `DataRegionConfiguration`. By default, CLOCK algorithm is used.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
  <!-- Memory configuration. -->
  <property name="dataStorageConfiguration">
    <bean class="org.apache.ignite.configuration.DataStorageConfiguration">
      <property name="dataRegionConfigurations">
        <list>
            <!--
            Defining a persistent data region with Segmented LRU page replacement mode.
            -->
            <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
            <!-- Data region name. -->
            <property name="name" value="persistent_data_region"/>

            <!-- Enable persistence. -->
            <property name="persistenceEnabled" value="true"/>

            <!-- 20 GB maximum size (RAM). -->
            <property name="maxSize" value="#{20L * 1024 * 1024 * 1024}"/>

            <!-- Enabling SEGMENTED_LRU page replacement for this region.  -->
            <property name="pageReplacementMode" value="SEGMENTED_LRU"/>
          </bean>
        </list>
      </property>
    </bean>
  </property>

  <!-- The rest of the configuration. -->
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
// Node configuration.
IgniteConfiguration cfg = new IgniteConfiguration();

// Memory configuration.
DataStorageConfiguration storageCfg = new DataStorageConfiguration();

// Creating a new data region.
DataRegionConfiguration regionCfg = new DataRegionConfiguration();

// Region name.
regionCfg.setName("persistent_data_region");

// Enabling persistence.
regionCfg.setPersistenceEnabled(true);

// 20 GB max size (RAM).
regionCfg.setMaxSize(20L * 1024 * 1024 * 1024);

// Enabling SEGMENTED_LRU page replacement for this region.
regionCfg.setPageReplacementMode(PageReplacementMode.SEGMENTED_LRU);

// Setting the data region configuration.
storageCfg.setDataRegionConfigurations(regionCfg);

// Applying the new configuration.
cfg.setDataStorageConfiguration(storageCfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

The choice of the algorithm depends on your workload. For most cases, CLOCK (default) is a good candidate, but on some workloads other algorithms can perform better.

## Random-LRU Algorithm

Every time a page is accessed, its timestamp is updated. When a page fault occurs, and some pages need replacement, the algorithm randomly chooses 5 pages from the page memory and evicts a page with the latest timestamp.

This algorithm has zero maintenance cost, but it is not very effective in terms of finding the next page to replace. We recommend that you use it in environments, where page replacement is not needed (when working with large enough data region to store all the amount of data) or happens very seldom.

## Segmented-LRU Algorithm

Segmented-LRU algorithm is a scan-resistant variation of the Least Recently Used (LRU) algorithm. Segmented-LRU pages list is divided into two segments: A probationary segment and a protected segment. Pages in each segment are ordered from the least to the most recently accessed. New pages are added to the most recently accessed end (tail) of the probationary segment. Existing pages are removed from wherever they currently reside and added to the most recently accessed end of the protected segment. Pages in the protected segment have thus been accessed at least twice. The protected segment is finite, so migration of a page from the probationary segment to the protected segment may force the migration of the LRU page in the protected segment to the most recently used end of the probationary segment. This gives the page another chance to be accessed before being replaced. Page to replace is polled from the least recently accessed end (head) of the probationary segment.

This algorithm requires additional memory to store pages list that also needs to be updated on each page access. At the same time, the algorithm has a near-optimal page to replace selection policy. So, there can be a little performance drop for environments without page replacement (compared to random-LRU and CLOCK), but for environments with a high rate of page replacement, and a large amount of one-time scans segmented-LRU can outperform random-LRU and CLOCK.

## CLOCK Algorithm

The CLOCK algorithm keeps a circular list of pages in memory, with the "hand" pointing to the last examined page frame in the list. When a page fault occurs and no empty frames exist, the hit flag of the page is inspected at the hand's location. If the hit flag is 0, the new page is put in the place of the page that the "hand" points to, and the hand is advanced one position further. Otherwise, the hit flag is cleared, then the clock hand is incremented, and the process is repeated until a page is replaced.

This algorithm has near to zero maintenance cost and replacement policy efficiency between random-LRU and segmented-LRU.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
