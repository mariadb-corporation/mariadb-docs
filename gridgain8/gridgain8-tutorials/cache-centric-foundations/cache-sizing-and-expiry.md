---
description: >-
  Solve the two invalidation problems that make a cache usable in production: bound the on-heap tier with LRU eviction, set entry lifetime with JCache expiry policies, and watch the cache manage itself.
---

# Cache Sizing and Expiry

## Introduction

"There are only two hard things in computer science: cache invalidation and naming things" (attributed to Phil Karlton, a principal engineer at Netscape in the 1990s). This tutorial takes on the first one.

You can put and get data with `IgniteCache` after [Work with the Cache API](work-with-cache-api.md). That is enough to call it a cache, but two problems make an unbounded cache unusable in production.

Without a size ceiling, every put expands the memory footprint until the JVM or the server's off-heap region runs out. A cache with no entry expiry is worse. It keeps serving data that has already gone stale in the source system. Neither is a bug that surfaces in a 1,000-entry test. Both are real under production load.

This tutorial solves both. You add on-heap LRU eviction to bound the JVM-heap footprint, set TTL with a JCache `ExpiryPolicy` to control freshness, and watch a real-time snapshot of the cache shrinking itself as entries leave under both rules. By the end, you have the vocabulary and code patterns the next tutorial needs when it connects the cache to a MariaDB database and leans on expiry semantics to keep cache-aside coherent.

One distinction sets up everything that follows. A cache is not a `ConcurrentMap`. A `ConcurrentMap` grows forever and holds data until the application explicitly removes it. A cache is a bounded, ephemeral view over data that actively manages what it keeps. Eviction and expiry are not features bolted onto a Map. They separate a cache from a map that happens to live in memory.

This tutorial works with both Ignite 2 and GridGain 8. The Java API is identical. Select your product version in the tabs where Maven coordinates and Docker container names differ.

This tutorial labels itself "beginner" for Ignite. The surrounding Java stack (Maven, JDBC, Spring XML) is assumed prior knowledge. If any of those is new, skim the linked primer before starting.

## Prerequisites

- **A running single-node cluster** from [Start a Local Cache Development Cluster](start-local-cache-cluster.md)
- **Java 11** or later (the Ignite 2 and GridGain 8 toolchains are tested against Java 11 and exhibit peer-class-loading edge cases on newer JDKs)
- **Maven 3.6** or later
- **JCache `ExpiryPolicy` terminology** will be introduced; no prior knowledge assumed.

<details>
<summary>Returning to these tutorials? Verify your cluster is running.</summary>

Check that the cluster container is up:

{% tabs %}
{% tab title="Apache Ignite 2" %}

```bash
docker ps --filter name=ignite2-node1 --format "table {{.Names}}\t{{.Status}}"
```

Expected output:

```text
NAMES            STATUS
ignite2-node1    Up X hours
```

{% endtab %}

{% tab title="GridGain 8" %}

```bash
docker ps --filter name=gridgain8-node1 --format "table {{.Names}}\t{{.Status}}"
```

Expected output:

```text
NAMES             STATUS
gridgain8-node1   Up X hours
```

{% endtab %}

{% endtabs %}

**If the container is stopped**, restart it from the directory containing your `docker-compose.yml`:

```bash
docker compose -f cache-cluster/docker-compose.yml start
```

**If the cluster was destroyed** (`docker compose down`), recreate it:

```bash
docker compose -f cache-cluster/docker-compose.yml up -d
```

The cluster runs in-memory. Destroying and recreating it starts with an empty cache.

</details>

## What You Will Learn

You build four small programs that progress from a naive unbounded cache to a self-managing cache. Each program reveals one mechanism.

- Write an unbounded cache and see why it is a memory leak
- Bound the on-heap tier with `LruEvictionPolicyFactory`, and understand why that does not bound the off-heap store
- Set entry lifetime with JCache `CreatedExpiryPolicy`, and choose between the four policy variants
- Watch a two-tier snapshot loop as the cache shrinks itself under combined eviction and expiry rules

## Set up the Maven Project

Create a project directory alongside your `cache-cluster` directory and add a `pom.xml`:

```bash
mkdir -p cache-client/src/main/java/com/example
```

{% tabs %}
{% tab title="Apache Ignite 2" %}

Create `cache-client/pom.xml`:

{% code title="pom.xml" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>cache-client</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <exec.mainClass>com.example.UnboundedCache</exec.mainClass>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.apache.ignite</groupId>
            <artifactId>ignite-core</artifactId>
            <version>2.16.0</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>exec-maven-plugin</artifactId>
                <version>3.1.0</version>
                <configuration>
                    <executable>java</executable>
                    <arguments>
                        <argument>--add-opens</argument>
                        <argument>java.base/java.nio=ALL-UNNAMED</argument>
                        <argument>--add-opens</argument>
                        <argument>java.base/sun.nio.ch=ALL-UNNAMED</argument>
                        <argument>--add-opens</argument>
                        <argument>java.base/java.lang=ALL-UNNAMED</argument>
                        <argument>--add-opens</argument>
                        <argument>java.base/java.util=ALL-UNNAMED</argument>
                        <argument>-classpath</argument>
                        <classpath/>
                        <argument>${exec.mainClass}</argument>
                    </arguments>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```
{% endcode %}

{% endtab %}

{% tab title="GridGain 8" %}

Create `cache-client/pom.xml`:

{% code title="pom.xml" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>cache-client</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <exec.mainClass>com.example.UnboundedCache</exec.mainClass>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.gridgain</groupId>
            <artifactId>gridgain-core</artifactId>
            <version>8.9.32</version>
        </dependency>
    </dependencies>

    <repositories>
        <repository>
            <id>GridGain External Repository</id>
            <url>https://www.gridgainsystems.com/nexus/content/repositories/external</url>
        </repository>
    </repositories>

    <build>
        <plugins>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>exec-maven-plugin</artifactId>
                <version>3.1.0</version>
                <configuration>
                    <executable>java</executable>
                    <arguments>
                        <argument>--add-opens</argument>
                        <argument>java.base/java.nio=ALL-UNNAMED</argument>
                        <argument>--add-opens</argument>
                        <argument>java.base/sun.nio.ch=ALL-UNNAMED</argument>
                        <argument>--add-opens</argument>
                        <argument>java.base/java.lang=ALL-UNNAMED</argument>
                        <argument>--add-opens</argument>
                        <argument>java.base/java.util=ALL-UNNAMED</argument>
                        <argument>-classpath</argument>
                        <classpath/>
                        <argument>${exec.mainClass}</argument>
                    </arguments>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```
{% endcode %}

GridGain 8 artifacts are published to GridGain's Nexus repository, not Maven Central. The `<repositories>` block tells Maven where to find the `gridgain-core` dependency.

{% endtab %}

{% endtabs %}

This `pom.xml` matches the one from [Work with the Cache API](work-with-cache-api.md). If you kept that project, you can continue using it; the four classes in this tutorial live in the same `com.example` package and the same `exec-maven-plugin` invocation runs them. The `exec.mainClass` property in `<properties>` is overridden on each `mvn exec:exec` call, so you switch between classes without editing the pom.

{% hint style="info" %}
Ignite 2.16.0 and GridGain 8.9.32 were released when Java 11 was the standard LTS. Peer class loading and lambda serialization paths inside these products are tested against Java 11. Newer JDKs compile and run the basic cache API, but event-subscription APIs that deploy classes across nodes (continuous queries, JCache entry listeners) exhibit deployment edge cases on Java 17 and later. This tutorial does not register such listeners, but pinning to Java 11 keeps your environment consistent with the products' tested toolchain.
{% endhint %}

{% hint style="success" %}
**Checkpoint:** The `pom.xml` is in `cache-client/` and `mvn compile` succeeds with no errors.
{% endhint %}

## Observe the Unbounded Cache Problem

Start with the naive case to see what goes wrong. An `IgniteCache` created with no configuration beyond its name has no size ceiling and no entry lifetime. Every call to `put` grows the footprint. Nothing ever leaves.

Create `cache-client/src/main/java/com/example/UnboundedCache.java`:

{% code title="UnboundedCache.java" %}
```java
package com.example;

import java.util.Collections;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.configuration.CacheConfiguration;
import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi;
import org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder;

/**
 * Demonstrates the unbounded-cache failure mode. A default cache
 * has no size ceiling. Loading 1,000 entries results in a cache
 * holding 1,000 entries. Every put grows the footprint.
 */
public class UnboundedCache {
    public static void main(String[] args) {
        TcpDiscoverySpi disco = new TcpDiscoverySpi();
        disco.setIpFinder(new TcpDiscoveryVmIpFinder()
            .setAddresses(Collections.singleton("127.0.0.1:47500")));

        IgniteConfiguration cfg = new IgniteConfiguration();
        cfg.setDiscoverySpi(disco);
        cfg.setClientMode(true);

        try (Ignite ignite = Ignition.start(cfg)) {
            // A default cache configuration has no eviction policy.
            // The cache grows without limit until the JVM runs out
            // of memory, which is the problem this tutorial solves.
            CacheConfiguration<Integer, String> cacheCfg =
                new CacheConfiguration<>("unbounded");

            IgniteCache<Integer, String> cache = ignite.getOrCreateCache(cacheCfg);
            cache.clear();

            System.out.println();
            System.out.println("=== Unbounded Cache ===");

            // Load 1,000 entries one at a time to make the growth visible.
            for (int i = 0; i < 1000; i++) {
                cache.put(i, "value-" + i);
            }

            System.out.println("After loading 1,000 entries, cache size: "
                + cache.size());
            System.out.println(
                "Every put expanded the footprint. This is a memory leak.");

            cache.destroy();
        }

        System.exit(0);
    }
}
```
{% endcode %}

Run it:

```bash
mvn -f cache-client/pom.xml compile exec:exec
```

After the Ignite startup output, you see:

```text
=== Unbounded Cache ===
After loading 1,000 entries, cache size: 1000
Every put expanded the footprint. This is a memory leak.
```

One thousand entries in, one thousand entries stored. A cache that keeps everything you write is a slower `ConcurrentMap`. In production, the loop does not stop at 1,000. It stops when the server runs out of memory. The remaining steps give the cache answers to two questions it cannot answer yet: when should it discard an entry to keep memory bounded, and when does an entry become stale?

{% hint style="success" %}
**Checkpoint:** The output reads `cache size: 1000`. The cache stored every entry you put.
{% endhint %}

## Bound the On-Heap Tier With Eviction

Eviction answers one question: when the cache is full, what do I discard? An eviction policy picks an entry at the moment a put would exceed the configured ceiling. LRU (least recently used) is the default choice for caching workloads because recency predicts future access. Ignite ships FIFO, sorted, and random policies as well, but LRU is the right starting point unless the access pattern gives you a better signal.

One piece of mental model before the code. Ignite stores cache data primarily off-heap, outside the JVM heap. The off-heap store avoids garbage-collection pressure and lets a single JVM hold many gigabytes of cached data. The on-heap tier is an optional bounded overlay for hot entries, and policy-based eviction operates on that overlay. Opt in with `setOnheapCacheEnabled(true)`. Without it, the cluster rejects the cache configuration with `IgniteCheckedException: Onheap cache must be enabled if eviction policy is configured`.

LRU therefore caps the on-heap tier, not the total cached data. That maps to what most production deployments need: a bound on the JVM heap footprint per cache. Bounding the off-heap region is a data-region configuration covered in a later tutorial.

Create `cache-client/src/main/java/com/example/BoundedCache.java`:

{% code title="BoundedCache.java" %}
```java
package com.example;

import java.util.Collections;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.cache.CachePeekMode;
import org.apache.ignite.cache.eviction.lru.LruEvictionPolicyFactory;
import org.apache.ignite.configuration.CacheConfiguration;
import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi;
import org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder;

/**
 * Demonstrates bounding the cache's on-heap tier with
 * LruEvictionPolicy. Ignite 2 stores data primarily off-heap and
 * optionally keeps a bounded on-heap copy of hot entries. The LRU
 * policy caps the on-heap tier at 100 entries. All 1,000 entries
 * remain in the off-heap primary store.
 */
public class BoundedCache {
    public static void main(String[] args) {
        TcpDiscoverySpi disco = new TcpDiscoverySpi();
        disco.setIpFinder(new TcpDiscoveryVmIpFinder()
            .setAddresses(Collections.singleton("127.0.0.1:47500")));

        IgniteConfiguration cfg = new IgniteConfiguration();
        cfg.setDiscoverySpi(disco);
        cfg.setClientMode(true);

        try (Ignite ignite = Ignition.start(cfg)) {
            CacheConfiguration<Integer, String> cacheCfg =
                new CacheConfiguration<>("bounded");

            // On-heap caching is opt-in because Ignite's primary storage
            // is off-heap. Policy-based eviction tracks entries on the
            // JVM heap, so the on-heap tier must be enabled. Without
            // this, cache creation throws:
            //   IgniteCheckedException: Onheap cache must be enabled
            //   if eviction policy is configured
            cacheCfg.setOnheapCacheEnabled(true);

            // LRU discards the least recently used entry from the
            // on-heap tier when it exceeds setMaxSize. The factory form
            // (over the deprecated setEvictionPolicy) is required
            // because cache configuration is distributed across the
            // cluster on node join; factories serialize cleanly where a
            // pre-instantiated policy would not.
            cacheCfg.setEvictionPolicyFactory(
                new LruEvictionPolicyFactory<>(100));

            IgniteCache<Integer, String> cache = ignite.getOrCreateCache(cacheCfg);
            cache.clear();

            System.out.println();
            System.out.println("=== Bounded Cache (LRU on-heap, maxSize=100) ===");

            for (int i = 0; i < 1000; i++) {
                cache.put(i, "value-" + i);
            }

            // Three size views expose the two-tier model. The total size
            // includes the off-heap primary store; the on-heap size is
            // bounded by the LRU policy.
            System.out.println("Total entries (all tiers):    " + cache.size());
            System.out.println("On-heap entries (LRU bound):  "
                + cache.size(CachePeekMode.ONHEAP));
            System.out.println("Off-heap entries (primary):   "
                + cache.size(CachePeekMode.OFFHEAP));
            System.out.println();
            System.out.println(
                "LRU capped the on-heap hot tier at 100 entries. "
                    + "The off-heap store holds the full 1,000.");

            cache.destroy();
        }

        System.exit(0);
    }
}
```
{% endcode %}

Run it:

```bash
mvn -f cache-client/pom.xml exec:exec -Dexec.mainClass=com.example.BoundedCache
```

```text
=== Bounded Cache (LRU on-heap, maxSize=100) ===
Total entries (all tiers):    1000
On-heap entries (LRU bound):  100
Off-heap entries (primary):   1000
LRU capped the on-heap hot tier at 100 entries. The off-heap store holds the full 1,000.
```

Three distinct counts tell the story. `cache.size()` without arguments reports 1,000 across all tiers because every entry still lives somewhere. The `ONHEAP` peek mode returns 100, exactly the `setMaxSize` ceiling on the bounded hot tier. The `OFFHEAP` peek mode returns 1,000 from the primary store, unaffected by the on-heap policy.

A few details to note:

- **`LruEvictionPolicyFactory`** is the current idiom. The older `setEvictionPolicy(new LruEvictionPolicy(100))` setter is `@Deprecated` in favor of the factory form. Cache configuration is serialized across the cluster on node join, and a factory serializes cleanly where a pre-instantiated policy does not.
- **Eviction is lazy**. LRU discards an entry only when a put would exceed the bound, not on a continuous background pass. The on-heap count sits at exactly 100 for the same reason: the policy keeps demoting one older entry per new put.
- **Other eviction policies exist**. Ignite 2 ships `FifoEvictionPolicyFactory` (discard the oldest insertion), `SortedEvictionPolicyFactory` (discard by a custom comparator), and a random policy. LRU is the right starting point for most caching workloads; pick one of the others when your access pattern gives you a better signal than recency.

{% hint style="info" %}
This tutorial caps the on-heap tier. The off-heap region grows until it hits the data region's configured limit (default 20% of system memory), at which point off-heap page eviction kicks in using a page-based policy configured on the data region. For production sizing, both layers matter. On-heap policy bounds the JVM heap; off-heap data-region settings bound the total data footprint. A later tutorial covers off-heap region configuration.
{% endhint %}

{% hint style="success" %}
**Checkpoint:** The output shows `Total entries: 1000`, `On-heap entries: 100`, and `Off-heap entries: 1000`. The on-heap count is exactly `setMaxSize`.
{% endhint %}

## Set Entry Lifetime With Expiry

Eviction keeps memory bounded. Expiry is about freshness: when does an entry become stale enough to stop trusting? The two controls answer different questions, and a single cache can configure both.

`ExpiryPolicy` is a JCache (JSR-107) interface. Ignite honors it regardless of whether on-heap caching is enabled or an eviction policy is configured. The four built-in policies anchor lifetime to a different lifecycle event each:

- **`CreatedExpiryPolicy`**: entries expire N time units after the first put. Subsequent reads and updates do not reset the clock. Use when data has a fixed freshness window, such as an API response cache where the upstream response is only trustworthy for a known interval.
- **`ModifiedExpiryPolicy`**: entries expire N time units after the last put. Use for a catalog with occasional updates: writes mean the value is fresh again.
- **`AccessedExpiryPolicy`**: entries expire N time units after the last read. Use for a session cache where hot sessions should stay and cold ones should drop.
- **`TouchedExpiryPolicy`**: entries expire N time units after either a read or a write. Use when both access patterns should keep an entry alive.

This step uses `CreatedExpiryPolicy`. The others share the same setter and the same factory pattern.

Create `cache-client/src/main/java/com/example/ExpiringCache.java`:

{% code title="ExpiringCache.java" %}
```java
package com.example;

import java.util.Collections;
import java.util.concurrent.TimeUnit;

import javax.cache.expiry.CreatedExpiryPolicy;
import javax.cache.expiry.Duration;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.configuration.CacheConfiguration;
import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi;
import org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder;

/**
 * Demonstrates entry lifetime with CreatedExpiryPolicy. Entries
 * live for three seconds after they are first put. A four-second
 * sleep leaves the cache empty. The server's background TTL
 * cleanup thread sweeps expired entries every 500ms.
 */
public class ExpiringCache {
    public static void main(String[] args) throws InterruptedException {
        TcpDiscoverySpi disco = new TcpDiscoverySpi();
        disco.setIpFinder(new TcpDiscoveryVmIpFinder()
            .setAddresses(Collections.singleton("127.0.0.1:47500")));

        IgniteConfiguration cfg = new IgniteConfiguration();
        cfg.setDiscoverySpi(disco);
        cfg.setClientMode(true);

        try (Ignite ignite = Ignition.start(cfg)) {
            CacheConfiguration<Integer, String> cacheCfg =
                new CacheConfiguration<>("expiring");

            // setEagerTtl(true) is the default on both Apache Ignite 2
            // and GridGain 8. The call is explicit in this tutorial to
            // make the setting visible: a reader tuning expiry later
            // knows exactly where to change the policy. Setting it to
            // false disables the background ttl-cleanup-worker sweep;
            // expired entries then leave the cache only when a later
            // get() touches them.
            cacheCfg.setEagerTtl(true);

            // CreatedExpiryPolicy sets a fixed lifetime measured from the
            // moment an entry is first put into the cache. Subsequent
            // reads and updates do not reset the clock. Use this when the
            // question is "how fresh is this data?", such as an API
            // response cache where data is only valid for a known window.
            //
            // Three other JCache policies exist and answer different
            // freshness questions:
            //   ModifiedExpiryPolicy (reset on update)
            //   AccessedExpiryPolicy (reset on read)
            //   TouchedExpiryPolicy  (reset on either)
            cacheCfg.setExpiryPolicyFactory(
                CreatedExpiryPolicy.factoryOf(
                    new Duration(TimeUnit.SECONDS, 3)));

            IgniteCache<Integer, String> cache = ignite.getOrCreateCache(cacheCfg);
            cache.clear();

            System.out.println();
            System.out.println("=== Expiring Cache (CreatedExpiryPolicy, 3s) ===");

            for (int i = 0; i < 10; i++) {
                cache.put(i, "value-" + i);
            }

            System.out.println("Immediately after loading 10 entries: size="
                + cache.size());
            System.out.println("Sleeping 4 seconds past the 3-second TTL...");

            TimeUnit.SECONDS.sleep(4);

            System.out.println("After sleep: size=" + cache.size());
            System.out.println(
                "Entries expired on the server's TTL cleanup sweep.");

            cache.destroy();
        }

        System.exit(0);
    }
}
```
{% endcode %}

Run it:

```bash
mvn -f cache-client/pom.xml exec:exec -Dexec.mainClass=com.example.ExpiringCache
```

```text
=== Expiring Cache (CreatedExpiryPolicy, 3s) ===
Immediately after loading 10 entries: size=10
Sleeping 4 seconds past the 3-second TTL...
After sleep: size=0
Entries expired on the server's TTL cleanup sweep.
```

The count drops to zero with no application call to remove anything. Expiry fires eagerly. Each server node runs a background worker (`ttl-cleanup-worker`) every 500ms that scans for expired entries and removes them. The four-second sleep is long enough for every entry's three-second TTL to elapse and for the sweep to catch them.

Three follow-on details worth surfacing:

- **`setEagerTtl(true)` is explicit for visibility, not for correctness**. Both products default to true. A production operator who wants lazy expiry (lower sweep CPU cost, at the price of expired entries occupying memory until a later read) sets this to false.
- **Per-operation TTL** overrides the cache-wide policy for a single call. Use `cache.withExpiryPolicy(CreatedExpiryPolicy.factoryOf(new Duration(TimeUnit.MINUTES, 1)).create()).put(key, value)` when one entry needs a different lifetime from the rest. The returned view shares the underlying cache; only that operation's entry lifetime changes.
- **Expiry removes from every tier**. Unlike on-heap eviction, which demotes an entry out of the hot tier while leaving it in off-heap, expiry removes the entry from on-heap and off-heap together. That is why `cache.size()` drops to zero and stays there.

{% hint style="success" %}
**Checkpoint:** The count reads `size=10` immediately after the load and `size=0` after the four-second sleep. Entries left the cache with no application call.
{% endhint %}

## Watch the Cache Manage Itself

So far each control has been visible through a single before-and-after count. A production cache manages itself continuously, not at snapshot boundaries. This final program combines both controls, loads entries just over the on-heap cap, and prints a real-time snapshot of both tiers every 500 milliseconds so you watch the cache shrink as it runs.

Configuration in this step:

- **On-heap cap: 20** (smaller than Step 3 so the evicted count is visible against the 30-entry load)
- **TTL: 2 seconds** (short enough that the snapshot loop captures the decay)
- **30 entries loaded** (overflows the on-heap cap by 10, leaves room for the TTL sweep)

Create `cache-client/src/main/java/com/example/ManagedCache.java`:

{% code title="ManagedCache.java" %}
```java
package com.example;

import java.util.Collections;
import java.util.concurrent.TimeUnit;

import javax.cache.expiry.CreatedExpiryPolicy;
import javax.cache.expiry.Duration;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.cache.CachePeekMode;
import org.apache.ignite.cache.eviction.lru.LruEvictionPolicyFactory;
import org.apache.ignite.configuration.CacheConfiguration;
import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi;
import org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder;

/**
 * Combines on-heap eviction with TTL expiry, then watches the cache
 * actively manage itself over time. LRU caps the on-heap tier at 20
 * while loading 30 entries; the off-heap store holds all 30 until
 * TTL expiry removes them from both tiers.
 *
 * The snapshot loop surfaces the active management that a
 * ConcurrentMap never does: entries leave without any application
 * call to remove. Production applications typically subscribe to
 * invalidation events through IgniteCache.registerCacheEntryListener
 * (JCache) or Ignite's continuous queries. Those APIs ship listener
 * classes to the server at runtime and require peer-class-loading
 * configuration beyond the scope of this tutorial.
 */
public class ManagedCache {
    public static void main(String[] args) throws InterruptedException {
        TcpDiscoverySpi disco = new TcpDiscoverySpi();
        disco.setIpFinder(new TcpDiscoveryVmIpFinder()
            .setAddresses(Collections.singleton("127.0.0.1:47500")));

        IgniteConfiguration cfg = new IgniteConfiguration();
        cfg.setDiscoverySpi(disco);
        cfg.setClientMode(true);

        try (Ignite ignite = Ignition.start(cfg)) {
            CacheConfiguration<Integer, String> cacheCfg =
                new CacheConfiguration<>("managed");
            cacheCfg.setOnheapCacheEnabled(true);
            // See ExpiringCache for why setEagerTtl(true) is explicit:
            // AI2 defaults to eager, GG8 defaults to lazy.
            cacheCfg.setEagerTtl(true);
            cacheCfg.setEvictionPolicyFactory(
                new LruEvictionPolicyFactory<>(20));
            cacheCfg.setExpiryPolicyFactory(
                CreatedExpiryPolicy.factoryOf(
                    new Duration(TimeUnit.SECONDS, 2)));

            IgniteCache<Integer, String> cache = ignite.getOrCreateCache(cacheCfg);
            cache.clear();

            System.out.println();
            System.out.println("=== Managed Cache (on-heap=20, TTL=2s) ===");
            System.out.println(
                "Loading 30 entries into a cache with two controls: "
                    + "on-heap bounded at 20 (LRU), entry lifetime 2 seconds.");
            System.out.println();

            long startNanos = System.nanoTime();
            for (int i = 0; i < 30; i++) {
                cache.put(i, "value-" + i);
            }

            // Poll the two-tier counts every 500ms. On-heap stays at 20
            // during the load because LRU demoted the older entries.
            // Off-heap holds all 30 until the server's 500ms TTL sweep
            // begins removing expired entries around t+2.0s.
            System.out.println("Time    On-heap  Off-heap");
            System.out.println("------  -------  --------");
            for (int tick = 0; tick <= 6; tick++) {
                double elapsed = (System.nanoTime() - startNanos) / 1_000_000_000.0;
                int onHeap = cache.size(CachePeekMode.ONHEAP);
                int offHeap = cache.size(CachePeekMode.OFFHEAP);
                System.out.printf("%4.1fs   %7d  %8d%n", elapsed, onHeap, offHeap);

                if (onHeap == 0 && offHeap == 0)
                    break;

                TimeUnit.MILLISECONDS.sleep(500);
            }

            System.out.println();
            System.out.println(
                "No application code removed entries. The cache discarded "
                    + "them on its own under the size and expiry rules.");

            cache.destroy();
        }

        System.exit(0);
    }
}
```
{% endcode %}

Run it:

```bash
mvn -f cache-client/pom.xml exec:exec -Dexec.mainClass=com.example.ManagedCache
```

```text
=== Managed Cache (on-heap=20, TTL=2s) ===
Loading 30 entries into a cache with two controls: on-heap bounded at 20 (LRU), entry lifetime 2 seconds.

Time    On-heap  Off-heap
------  -------  --------
 0.0s        20        30
 0.6s        20        30
 1.1s        20        30
 1.6s        20        30
 2.1s        20        25
 2.7s         0         0

No application code removed entries. The cache discarded them on its own under the size and expiry rules.
```

Read the snapshot top to bottom. At `t+0.0s`, the load just finished: on-heap is capped at 20 (LRU pushed entries 0 through 9 out of the hot tier as entries 20 through 29 came in), off-heap holds all 30. For the first two seconds nothing changes, because neither rule has triggered yet. At `t+2.1s` the server's TTL sweep has caught five expired entries and dropped them from both tiers. By `t+2.7s`, the remaining entries have expired and the cache is empty. The whole show took under three seconds and did not involve a single application-level remove.

A few things are worth noticing:

- **On-heap at 20 during the load means LRU worked during the puts**, not after. The policy fires inline with each put that would otherwise exceed the cap, demoting the least recently used on-heap entry. Off-heap still holds the demoted entry.
- **Off-heap drops in batches, not one-by-one**. The TTL sweep processes up to 1,000 expired entries per cache per pass. The 30 → 25 → 0 pattern reflects sweep timing, not a per-entry delay.
- **The time column exposes the cadence**. Production monitoring that tracks cache size over time shows the same shape: the on-heap count flatlines at the LRU cap while writes are arriving, then both tiers decay once traffic subsides and TTL catches up.

{% hint style="info" %}
This step polls the cache to observe its state. Production applications typically subscribe to invalidation events directly. Three APIs cover that ground: JCache entry listeners (`cache.registerCacheEntryListener` with a `CacheEntryExpiredListener` implementation), Ignite continuous queries, and the Ignite remote events API. All three ship listener classes from the client to the server at runtime. That requires peer class loading or pre-deployed server jars, which is cluster-level configuration outside this tutorial's scope. Ignite's documentation on continuous queries and entry listeners is the next stop when you need event-driven invalidation in a real system.
{% endhint %}

{% hint style="success" %}
**Checkpoint:** The snapshot table shows on-heap stuck at 20 while off-heap holds 30, then both columns decay to zero by `t+2.7s`. The cache removed entries without any call from your code.
{% endhint %}

## Summary

A cache is not a `ConcurrentMap`. It actively manages its contents under rules the application configures once and never touches again. You built four programs that make those rules visible:

- `UnboundedCache` held every entry you wrote, which named the problem the rest of the tutorial solves.
- `BoundedCache` bounded the on-heap tier with `LruEvictionPolicyFactory` and surfaced Ignite's two-tier storage model. LRU caps the JVM-heap footprint per cache. Bounding the off-heap region itself is a data-region configuration covered in a later tutorial.
- `ExpiringCache` set a three-second entry lifetime with `CreatedExpiryPolicy`. The other three JCache policies cover update-based, access-based, and touched-based freshness windows.
- `ManagedCache` combined both controls and watched the cache discard entries on its own. The two-tier snapshot loop is a diagnostic; production applications usually subscribe to invalidation events through JCache listeners or Ignite continuous queries.

Those four programs map to the two failure modes of a naive cache. Eviction is the answer to unbounded memory growth: LRU discards the least recently used on-heap entry whenever a put would exceed the cap. Expiry is the answer to stale data, with four JCache policies that anchor entry lifetime to creation, modification, access, or either. Configured together, the two controls turn a distributed `ConcurrentMap` into something that behaves like a cache under real workloads.

## Next Step

The next tutorial adds a database. Cache-aside reads the cache first, falls through to MariaDB on a miss, and populates the cache with the fresh row. Cache-aside has no answer for stale data on its own. The expiry semantics you just set are what keep the pattern coherent over time.

<hr />

