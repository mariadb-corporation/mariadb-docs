---
description: >-
  Watch a cache spread 10,000 entries across three nodes and then four.
---

# Understand How Your Cache Is Distributed

<!-- TODO (decision): The `platform: linux/amd64` pin and the "amd64 only / Rosetta" guidance are kept as originally written (the author used Apple Silicon). The official `gridgain/enterprise:8.10.0` image is multi-arch (amd64 and arm64), so the pin is probably no longer needed. Decide whether to drop the pin (also in start-local-cache-cluster, understand-cache-distribution and native-persistence-beyond-cache), then delete this comment. -->

## Introduction

The cache API looks like a `ConcurrentMap`, and on a single-node cluster it behaves like one. It is not one. Entries are distributed across nodes by a hash of the key, each partition has a primary and, with `backups=1`, a backup on a different node. The partition layout shifts when the topology changes. A one-node development cluster hides every detail.

You make the distribution visible here. You create a partitioned cache, seed it with 10,000 entries, and use the Affinity API to ask the cluster which node owns what. Then you scale from one node to three and watch entries redistribute without any code running. Scale to four and watch it happen again.

## Prerequisites

- **A running single-node cluster** from [Start a Local Cache Development Cluster](../../quick-start/start-local-cache-cluster.md)
- **Cache API familiarity** from [Work with the Cache API](../../quick-start/work-with-cache-api.md)
- **Java 17 or later for the client runtime.** The Maven project compiles to Java 17 bytecode, the same version the server JVM runs.
- **Maven 3.6** or later
- **Docker Compose 2.23** or later

The first step in this tutorial adds replacement compose files and per-node configs to your `cache-cluster/` directory. Your existing single-node setup stays in place unchanged.

<details>
<summary>Returning to these tutorials? Verify your cluster is running.</summary>

Check that the cluster container is up:

```bash
docker ps --filter name=gridgain8-node1 --format "table {{.Names}}\t{{.Status}}"
```

Expected output:

```text
NAMES             STATUS
gridgain8-node1   Up X hours
```

If the container is stopped, restart it with `docker compose -f cache-cluster/docker-compose.yml start`. If the cluster was destroyed, bring it back with `docker compose -f cache-cluster/docker-compose.yml up -d`. The cache is in memory, so destroying the cluster discards any cache data. The program recreates and reseeds the cache on its next run.

</details>

## What You Will Learn

In this tutorial, you:

- Configure a partitioned cache with an explicit partition count and `backups=1`
- Use `ignite.affinity(cacheName)` to inspect which node owns each partition
- Observe that a single-node cluster owns every primary partition and zero backups
- Scale the cluster to three nodes and watch partitions redistribute without code changes
- Scale to four nodes and confirm that rebalance is incremental and preserves the cache data
- Predict how key-to-partition and partition-to-node mappings change under topology changes

## Create the Cache-Distribution Project

Create a Maven project named `cache-distribution/`. It needs one source file and a `pom.xml` that targets Java 17 bytecode and suppresses the engine's startup logs so the program's output stands out.

{% code title="cache-distribution/pom.xml" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>cache-distribution</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.release>17</maven.compiler.release>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <exec.mainClass>com.example.distribution.Distribution</exec.mainClass>
    </properties>

    <repositories>
        <repository>
            <id>GridGain External Repository</id>
            <url>https://www.gridgainsystems.com/nexus/content/repositories/external</url>
        </repository>
    </repositories>

    <dependencies>
        <dependency>
            <groupId>org.gridgain</groupId>
            <artifactId>gridgain-core</artifactId>
            <version>8.10.0</version>
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
                        <argument>java.base/java.lang.invoke=ALL-UNNAMED</argument>
                        <argument>--add-opens</argument>
                        <argument>java.base/java.util=ALL-UNNAMED</argument>
                        <argument>--add-opens</argument>
                        <argument>java.base/java.io=ALL-UNNAMED</argument>
                        <argument>-DIGNITE_QUIET=true</argument>
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

{% hint style="info" %}

Without the flag, the client logs its startup handshake, topology snapshots, and communication events at INFO level, which drowns the program's output. With it, GridGain prints a short summary banner and then stays quiet. Remove the flag if you need to diagnose a connection problem.

{% endhint %}

Create a single source file at `src/main/java/com/example/distribution/Distribution.java`. The class opens a thick client, creates a partitioned cache if one does not exist, seeds 10,000 entries, and prints three views of the distribution:

{% code title="cache-distribution/src/main/java/com/example/distribution/Distribution.java" %}
```java
package com.example.distribution;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.UUID;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.cache.CacheMode;
import org.apache.ignite.cache.affinity.Affinity;
import org.apache.ignite.cache.affinity.rendezvous.RendezvousAffinityFunction;
import org.apache.ignite.cluster.ClusterNode;
import org.apache.ignite.configuration.CacheConfiguration;
import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi;
import org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder;

/**
 * Inspect how a partitioned cache distributes data across the
 * cluster. A single run creates the distribution-sample cache if it
 * does not exist, seeds it with 10,000 entries when empty, and
 * prints three views of the current distribution.
 *
 * The Affinity API reads the cluster's live topology, so re-running
 * the same program after a scale event shows the new distribution
 * without writing a single extra entry.
 */
public class Distribution {

    private static final String CACHE_NAME = "distribution-sample";
    private static final int PARTITIONS = 32;
    private static final int ENTRY_COUNT = 10_000;
    private static final int SAMPLE_KEY = 42;

    public static void main(String[] args) {
        // Static IP discovery. The seed list covers every possible
        // node's discovery port so the same client code works against
        // one-node, three-node, and four-node clusters. Unreachable
        // addresses are skipped.
        TcpDiscoverySpi disco = new TcpDiscoverySpi();
        disco.setIpFinder(new TcpDiscoveryVmIpFinder()
            .setAddresses(Arrays.asList(
                "127.0.0.1:47500..47503"
            )));

        IgniteConfiguration cfg = new IgniteConfiguration();
        cfg.setDiscoverySpi(disco);
        cfg.setClientMode(true);
        cfg.setPeerClassLoadingEnabled(true);

        try (Ignite ignite = Ignition.start(cfg)) {
            List<ClusterNode> servers = new ArrayList<>(ignite.cluster().forServers().nodes());
            servers.sort(Comparator.comparing(n -> n.consistentId().toString()));

            // Assign readable labels (node1, node2, ...) in a stable
            // order so the program's output never shows an
            // auto-generated Docker container ID. The label is a
            // client-side synonym; the cluster itself does not know
            // about it.
            Map<UUID, String> labels = new HashMap<>();
            for (int i = 0; i < servers.size(); i++) {
                labels.put(servers.get(i).id(), "node" + (i + 1));
            }

            System.out.println();
            System.out.println("=== Cache distribution ===");
            System.out.println("Server nodes in cluster: " + servers.size());

            // PARTITIONED is the default mode; setting it explicitly
            // documents the choice. backups=1 means every partition
            // has one backup on a different node.
            //
            // RendezvousAffinityFunction is the default function.
            // (false, 32) reads as "do not exclude neighbors, use
            // 32 partitions." The production default is 1024; 32
            // here keeps the per-node math countable by hand.
            CacheConfiguration<Integer, String> cacheCfg =
                new CacheConfiguration<Integer, String>(CACHE_NAME)
                    .setCacheMode(CacheMode.PARTITIONED)
                    .setBackups(1)
                    .setAffinity(new RendezvousAffinityFunction(false, PARTITIONS));

            IgniteCache<Integer, String> cache = ignite.getOrCreateCache(cacheCfg);

            // Seed only when the cache is empty. Runs against a
            // cluster that already has entries skip this step, which
            // is how the post-scale run proves the rebalance
            // preserved the data.
            if (cache.size() == 0) {
                System.out.println("Cache is empty. Seeding " + ENTRY_COUNT + " entries.");
                Map<Integer, String> seed = new HashMap<>(ENTRY_COUNT);
                for (int i = 0; i < ENTRY_COUNT; i++) {
                    seed.put(i, "v" + i);
                }
                cache.putAll(seed);
            } else {
                System.out.println("Cache already holds " + cache.size() + " entries. Skipping seed.");
            }

            // ignite.affinity(cacheName) returns a client-side handle
            // that computes partition ownership from the cached
            // topology view. The methods on this handle never make
            // a round trip to the server.
            Affinity<Integer> aff = ignite.affinity(CACHE_NAME);

            System.out.println();
            System.out.println("--- Partition summary ---");
            System.out.println("Total partitions: " + aff.partitions());

            for (ClusterNode node : servers) {
                int[] primary = aff.primaryPartitions(node);
                int[] backup = aff.backupPartitions(node);
                System.out.printf("  %s : %d primary, %d backup%n",
                    labels.get(node.id()), primary.length, backup.length);
            }

            // A single-key view. Partition number is deterministic
            // from the key hash; which node owns the partition
            // depends on the current topology.
            System.out.println();
            System.out.println("--- Single-key introspection: key " + SAMPLE_KEY + " ---");
            int partition = aff.partition(SAMPLE_KEY);
            ClusterNode primary = aff.mapKeyToNode(SAMPLE_KEY);
            Collection<ClusterNode> owners = aff.mapKeyToPrimaryAndBackups(SAMPLE_KEY);
            System.out.println("Partition: " + partition);
            System.out.println("Primary:   " + labels.getOrDefault(primary.id(), "(none)"));
            String backups = owners.stream()
                .skip(1)
                .map(n -> labels.getOrDefault(n.id(), "(none)"))
                .reduce((a, b) -> a + ", " + b)
                .orElse("(none)");
            System.out.println("Backup:    " + backups);

            System.out.println();
            System.out.println("--- Entry count per primary owner ---");
            Map<String, Integer> perNode = new TreeMap<>();
            for (int key = 0; key < ENTRY_COUNT; key++) {
                ClusterNode owner = aff.mapKeyToNode(key);
                perNode.merge(labels.get(owner.id()), 1, Integer::sum);
            }
            for (Map.Entry<String, Integer> e : perNode.entrySet()) {
                System.out.printf("  %s : %d entries%n", e.getKey(), e.getValue());
            }
        }
    }
}
```
{% endcode %}

Compile it:

```bash
mvn -f cache-distribution/pom.xml compile
```

{% hint style="success" %}
**Checkpoint:** The Maven build finishes with `BUILD SUCCESS` and `cache-distribution/target/classes/com/example/distribution/Distribution.class` exists.
{% endhint %}

## Add the Cluster Compose Files

The single-node cluster from [Start a Local Cache Development Cluster](../../quick-start/start-local-cache-cluster.md) does not expose the communication port (47100) that the thick client needs for direct cache operations. The prior tutorials worked around that through the server's initial discovery channel; this tutorial opens enough connections to need the comm port too.

Create three replacement compose files plus four per-node configs in your existing `cache-cluster/` directory. Your existing `docker-compose.yml` and `ignite-config.xml` stay in place and are ignored for the rest of this tutorial.

The per-node configs differ in three places: a unique discovery port, a unique communication port, and a `BasicAddressResolver` entry that exposes the container's hostname under `127.0.0.1` so the thick client on your host can reach each node through a distinct localhost port.

<details>
<summary><code>cache-cluster/docker-compose-1node.yml</code></summary>

{% code title="docker-compose-1node.yml" %}
```yaml
name: gridgain8

services:
  node1:
    image: gridgain/enterprise:8.10.0
    platform: linux/amd64
    container_name: gridgain8-node1
    hostname: node1
    environment:
      CONFIG_URI: /config/ignite-config.xml
      JVM_OPTS: "-Xms1g -Xmx1g"
    volumes:
      - ./ignite-config-node1.xml:/config/ignite-config.xml:ro
      - ./gridgain-license.xml:/opt/gridgain/gridgain-license.xml:ro
    ports:
      - "47500:47500"
      - "47100:47100"
      - "10800:10800"
```
{% endcode %}

</details>

<details>
<summary><code>cache-cluster/docker-compose-3nodes.yml</code></summary>

{% code title="docker-compose-3nodes.yml" %}
```yaml
name: gridgain8

x-node-defaults: &node-defaults
  image: gridgain/enterprise:8.10.0
  platform: linux/amd64
  environment:
    CONFIG_URI: /config/ignite-config.xml
    JVM_OPTS: "-Xms1g -Xmx1g"

services:
  node1:
    <<: *node-defaults
    container_name: gridgain8-node1
    hostname: node1
    volumes:
      - ./ignite-config-node1.xml:/config/ignite-config.xml:ro
      - ./gridgain-license.xml:/opt/gridgain/gridgain-license.xml:ro
    ports:
      - "47500:47500"
      - "47100:47100"
      - "10800:10800"

  node2:
    <<: *node-defaults
    container_name: gridgain8-node2
    hostname: node2
    volumes:
      - ./ignite-config-node2.xml:/config/ignite-config.xml:ro
      - ./gridgain-license.xml:/opt/gridgain/gridgain-license.xml:ro
    ports:
      - "47501:47501"
      - "47101:47101"
      - "10801:10800"

  node3:
    <<: *node-defaults
    container_name: gridgain8-node3
    hostname: node3
    volumes:
      - ./ignite-config-node3.xml:/config/ignite-config.xml:ro
      - ./gridgain-license.xml:/opt/gridgain/gridgain-license.xml:ro
    ports:
      - "47502:47502"
      - "47102:47102"
      - "10802:10800"
```
{% endcode %}

</details>

<details>
<summary><code>cache-cluster/docker-compose-4nodes.yml</code></summary>

Identical to the three-node file with a fourth service appended. Docker Compose treats identical service definitions across files as the same running container, which is what makes the scale-up in the final step non-destructive.

{% code title="docker-compose-4nodes.yml" %}
```yaml
name: gridgain8

x-node-defaults: &node-defaults
  image: gridgain/enterprise:8.10.0
  platform: linux/amd64
  environment:
    CONFIG_URI: /config/ignite-config.xml
    JVM_OPTS: "-Xms1g -Xmx1g"

services:
  node1:
    <<: *node-defaults
    container_name: gridgain8-node1
    hostname: node1
    volumes:
      - ./ignite-config-node1.xml:/config/ignite-config.xml:ro
      - ./gridgain-license.xml:/opt/gridgain/gridgain-license.xml:ro
    ports:
      - "47500:47500"
      - "47100:47100"
      - "10800:10800"

  node2:
    <<: *node-defaults
    container_name: gridgain8-node2
    hostname: node2
    volumes:
      - ./ignite-config-node2.xml:/config/ignite-config.xml:ro
      - ./gridgain-license.xml:/opt/gridgain/gridgain-license.xml:ro
    ports:
      - "47501:47501"
      - "47101:47101"
      - "10801:10800"

  node3:
    <<: *node-defaults
    container_name: gridgain8-node3
    hostname: node3
    volumes:
      - ./ignite-config-node3.xml:/config/ignite-config.xml:ro
      - ./gridgain-license.xml:/opt/gridgain/gridgain-license.xml:ro
    ports:
      - "47502:47502"
      - "47102:47102"
      - "10802:10800"

  node4:
    <<: *node-defaults
    container_name: gridgain8-node4
    hostname: node4
    volumes:
      - ./ignite-config-node4.xml:/config/ignite-config.xml:ro
      - ./gridgain-license.xml:/opt/gridgain/gridgain-license.xml:ro
    ports:
      - "47503:47503"
      - "47103:47103"
      - "10803:10800"
```
{% endcode %}

</details>

<details>
<summary><code>cache-cluster/ignite-config-node1.xml</code></summary>

{% code title="ignite-config-node1.xml" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
       http://www.springframework.org/schema/beans
       http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean class="org.apache.ignite.configuration.IgniteConfiguration">
        <property name="discoverySpi">
            <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
                <property name="localPort" value="47500"/>
                <property name="localPortRange" value="1"/>
                <property name="ipFinder">
                    <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                        <property name="addresses">
                            <list>
                                <value>node1:47500</value>
                                <value>node2:47501</value>
                                <value>node3:47502</value>
                                <value>node4:47503</value>
                            </list>
                        </property>
                    </bean>
                </property>
            </bean>
        </property>

        <property name="communicationSpi">
            <bean class="org.apache.ignite.spi.communication.tcp.TcpCommunicationSpi">
                <property name="localPort" value="47100"/>
                <property name="localPortRange" value="1"/>
            </bean>
        </property>

        <property name="peerClassLoadingEnabled" value="true"/>

        <property name="addressResolver">
            <bean class="org.apache.ignite.configuration.BasicAddressResolver">
                <constructor-arg>
                    <map>
                        <entry key="node1" value="127.0.0.1"/>
                    </map>
                </constructor-arg>
            </bean>
        </property>
    </bean>
</beans>
```
{% endcode %}

</details>

<details>
<summary><code>cache-cluster/ignite-config-node2.xml</code></summary>

Same as `ignite-config-node1.xml` with three edits: discovery `localPort` is `47501`, communication `localPort` is `47101`, and the `BasicAddressResolver` entry key is `node2`.

{% code title="ignite-config-node2.xml" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
       http://www.springframework.org/schema/beans
       http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean class="org.apache.ignite.configuration.IgniteConfiguration">
        <property name="discoverySpi">
            <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
                <property name="localPort" value="47501"/>
                <property name="localPortRange" value="1"/>
                <property name="ipFinder">
                    <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                        <property name="addresses">
                            <list>
                                <value>node1:47500</value>
                                <value>node2:47501</value>
                                <value>node3:47502</value>
                                <value>node4:47503</value>
                            </list>
                        </property>
                    </bean>
                </property>
            </bean>
        </property>

        <property name="communicationSpi">
            <bean class="org.apache.ignite.spi.communication.tcp.TcpCommunicationSpi">
                <property name="localPort" value="47101"/>
                <property name="localPortRange" value="1"/>
            </bean>
        </property>

        <property name="peerClassLoadingEnabled" value="true"/>

        <property name="addressResolver">
            <bean class="org.apache.ignite.configuration.BasicAddressResolver">
                <constructor-arg>
                    <map>
                        <entry key="node2" value="127.0.0.1"/>
                    </map>
                </constructor-arg>
            </bean>
        </property>
    </bean>
</beans>
```
{% endcode %}

</details>

<details>
<summary><code>cache-cluster/ignite-config-node3.xml</code></summary>

Same pattern: discovery port `47502`, communication port `47102`, resolver key `node3`.

{% code title="ignite-config-node3.xml" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
       http://www.springframework.org/schema/beans
       http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean class="org.apache.ignite.configuration.IgniteConfiguration">
        <property name="discoverySpi">
            <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
                <property name="localPort" value="47502"/>
                <property name="localPortRange" value="1"/>
                <property name="ipFinder">
                    <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                        <property name="addresses">
                            <list>
                                <value>node1:47500</value>
                                <value>node2:47501</value>
                                <value>node3:47502</value>
                                <value>node4:47503</value>
                            </list>
                        </property>
                    </bean>
                </property>
            </bean>
        </property>

        <property name="communicationSpi">
            <bean class="org.apache.ignite.spi.communication.tcp.TcpCommunicationSpi">
                <property name="localPort" value="47102"/>
                <property name="localPortRange" value="1"/>
            </bean>
        </property>

        <property name="peerClassLoadingEnabled" value="true"/>

        <property name="addressResolver">
            <bean class="org.apache.ignite.configuration.BasicAddressResolver">
                <constructor-arg>
                    <map>
                        <entry key="node3" value="127.0.0.1"/>
                    </map>
                </constructor-arg>
            </bean>
        </property>
    </bean>
</beans>
```
{% endcode %}

</details>

<details>
<summary><code>cache-cluster/ignite-config-node4.xml</code></summary>

Same pattern: discovery port `47503`, communication port `47103`, resolver key `node4`.

{% code title="ignite-config-node4.xml" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
       http://www.springframework.org/schema/beans
       http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean class="org.apache.ignite.configuration.IgniteConfiguration">
        <property name="discoverySpi">
            <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
                <property name="localPort" value="47503"/>
                <property name="localPortRange" value="1"/>
                <property name="ipFinder">
                    <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                        <property name="addresses">
                            <list>
                                <value>node1:47500</value>
                                <value>node2:47501</value>
                                <value>node3:47502</value>
                                <value>node4:47503</value>
                            </list>
                        </property>
                    </bean>
                </property>
            </bean>
        </property>

        <property name="communicationSpi">
            <bean class="org.apache.ignite.spi.communication.tcp.TcpCommunicationSpi">
                <property name="localPort" value="47103"/>
                <property name="localPortRange" value="1"/>
            </bean>
        </property>

        <property name="peerClassLoadingEnabled" value="true"/>

        <property name="addressResolver">
            <bean class="org.apache.ignite.configuration.BasicAddressResolver">
                <constructor-arg>
                    <map>
                        <entry key="node4" value="127.0.0.1"/>
                    </map>
                </constructor-arg>
            </bean>
        </property>
    </bean>
</beans>
```
{% endcode %}

</details>

{% hint style="success" %}
**Checkpoint:** Your `cache-cluster/` directory now contains three `docker-compose-*nodes.yml` files and four `ignite-config-node*.xml` files alongside your existing CC-01 setup.
{% endhint %}

## Run on one Node to see the Baseline

Stop the cluster from the previous tutorials if it is still running, then start the single-node variant you just created:

```bash
docker compose -f cache-cluster/docker-compose.yml down
docker compose -f cache-cluster/docker-compose-1node.yml up -d
```

Run the program:

```bash
mvn -f cache-distribution/pom.xml exec:exec
```

Expected output (trimmed; the engine prints its own startup banner above what appears here):

```text
=== Cache distribution ===
Server nodes in cluster: 1
Cache is empty. Seeding 10000 entries.

--- Partition summary ---
Total partitions: 32
  node1 : 32 primary, 0 backup

--- Single-key introspection: key 42 ---
Partition: 10
Primary:   node1
Backup:    (none)

--- Entry count per primary owner ---
  node1 : 10000 entries
```

The `node1`, `node2`, ... labels in the output are client-side synonyms the program assigns by sorting cluster members on their consistent ID. The cluster itself does not know about them. They exist because Docker's auto-generated container IDs would otherwise show up in the output as unreadable hex strings.

Three things to notice.

**The cache has 32 partitions even though only one node exists.** Partition count is a cache property set at creation time. It does not change with topology. One node owns all 32 primaries because there is nowhere else to put them.

**`backups=1` was configured, but the summary shows zero backups.** A backup on the same node as its primary would not survive the node's failure, so the engine refuses to place one there. With only one node the setting has nowhere to take effect; a second node activates it.

**Key 42 lives on partition 10.** `RendezvousAffinityFunction` hashes the key and picks a partition from the 32 available. The hash and the partition count are the only inputs, so key 42 maps to partition 10 on every run against any cluster.

{% hint style="info" %}

Production clusters typically run with the default of 1024 partitions rather than 32. The default strikes a balance between finer rebalance granularity (more partitions means smaller data chunks move at a time) and metadata overhead (every partition costs a bit of cluster bookkeeping). A later guide walks through when to change the default. For this tutorial, 32 makes the per-node numbers small enough to count at a glance.

{% endhint %}

{% hint style="success" %}
**Checkpoint:** Server count is 1, total partitions is 32, `node1` owns 32 primary partitions and 0 backups, and all 10,000 entries are on `node1`.
{% endhint %}

## Scale to Three Nodes

Stop the single-node cluster and bring up the three-node version. Each node exposes discovery and communication on a distinct host port so the thick client can reach all three.

```bash
docker compose -f cache-cluster/docker-compose-1node.yml down
docker compose -f cache-cluster/docker-compose-3nodes.yml up -d
```

`down` destroys the single-node cluster and its in-memory cache. `up -d` starts three fresh nodes. The next program run finds an empty cache and reseeds.

Wait for all three nodes to join. The cluster is ready when node1's logs show `servers=3`:

```bash
docker logs gridgain8-node1 2>&1 | grep "Topology snapshot" | tail -1
```

Expected output (trimmed to the interesting fields):

```text
Topology snapshot [ver=3, ..., servers=3, ...]
```

Re-run the same program:

```bash
mvn -f cache-distribution/pom.xml exec:exec
```

Expected output:

```text
=== Cache distribution ===
Server nodes in cluster: 3
Cache is empty. Seeding 10000 entries.

--- Partition summary ---
Total partitions: 32
  node1 : 10 primary, 10 backup
  node2 : 10 primary, 8 backup
  node3 : 12 primary, 14 backup

--- Single-key introspection: key 42 ---
Partition: 10
Primary:   node1
Backup:    node2

--- Entry count per primary owner ---
  node1 : 3124 entries
  node2 : 3125 entries
  node3 : 3751 entries
```

Your exact numbers will vary. Rendezvous depends on each node's cluster-assigned identity, which Docker regenerates every restart. The invariants hold regardless:

- Primary count per node sums to 32.
- Backup count per node also sums to 32. Every partition now has a backup on a different node.
- Entry count per node sums to 10,000.

Three things to notice.

**The client code did not change.** The Affinity API reads the cluster's current topology at the moment it is called, so the same `primaryPartitions(node)` call returns 32 on one node and about 11 on three nodes.

**Key 42 has a real backup.** Partition 10 sits on `node1` with a backup on `node2`. If `node1` fails, `node2` is promoted and the partition stays available. That is what `backups=1` buys you: survival of one simultaneous node loss per partition.

**Entry counts are roughly even, not exact.** Rendezvous spreads keys evenly in expectation, but any finite sample shows variance. The variance shrinks as the sample grows; a production cache with millions of entries distributes close to uniform.

{% hint style="info" %}

Key 42 is on partition 10 in every cluster, every time. The key-to-partition mapping is a hash, with nothing topology-dependent in it. What changed between the one-node and three-node runs is which node owns partition 10. On a different three-node cluster with different node identities, the primary and backup could be any two of the three.

{% endhint %}

{% hint style="success" %}
**Checkpoint:** Server count is 3, primary counts per node sum to 32, backup counts sum to 32, and every node holds roughly a third of the 10,000 entries.
{% endhint %}

## Scale to Four Nodes and Watch the Data Follow

Keep the three-node cluster running. Start the four-node variant alongside it:

```bash
docker compose -f cache-cluster/docker-compose-4nodes.yml up -d
```

Docker Compose reconciles: the three running services match the four-node file exactly, so they stay up and only `node4` starts. The engine detects the topology change and begins rebalance.

Confirm all four nodes are in the topology:

```bash
docker logs gridgain8-node1 2>&1 | grep "Topology snapshot" | tail -1
```

Expected output:

```text
Topology snapshot [ver=..., servers=4, ...]
```

Re-run the program one more time:

```bash
mvn -f cache-distribution/pom.xml exec:exec
```

Expected output:

```text
=== Cache distribution ===
Server nodes in cluster: 4
Cache already holds 10000 entries. Skipping seed.

--- Partition summary ---
Total partitions: 32
  node1 : 7 primary, 10 backup
  node2 : 8 primary, 5 backup
  node3 : 11 primary, 8 backup
  node4 : 6 primary, 9 backup

--- Single-key introspection: key 42 ---
Partition: 10
Primary:   node4
Backup:    node1

--- Entry count per primary owner ---
  node1 : 2185 entries
  node2 : 2500 entries
  node3 : 3438 entries
  node4 : 1877 entries
```

Look at the second output line: `Cache already holds 10000 entries. Skipping seed.` The program found the cache still populated from the three-node seed, so the seed loop did not run. No code migrated data. No script rebalanced partitions. The engine added `node4` to the topology, copied the right partitions onto it, and kept the cache serving reads and writes throughout.

Three things to notice.

**The cache survived the scale event.** Adding a server to a live cluster did not require an application-layer migration, a read-modify-write loop, or any special coordination from the client. The 10,000 entries that landed on three nodes in the previous step are still there, now spread across four.

**Rebalance is incremental, not wholesale.** Each existing node gave up a few primary partitions to `node4`. No node moved all of its partitions. Adding one node to a ten-node cluster would move roughly a tenth of the partitions, which keeps the cost bounded for large clusters.

**The key-to-partition mapping is still deterministic.** Key 42 is still on partition 10. In this run partition 10 moved from `node1` to `node4`, with `node1` now holding the backup. In your run it might stay on `node1` or land somewhere else; the Rendezvous function reassigns partitions based on the new topology. Either way the key is in the same partition it has always been.

{% hint style="success" %}
**Checkpoint:** Server count is 4, the cache reports 10,000 entries before any seeding runs, primary counts sum to 32, and each node holds roughly a quarter of the entries.
{% endhint %}

## Summary

You have the mental model for every cache on any cluster, including a single-node development cluster where the distribution is invisible.

**The cache is partitioned.** Every key hashes to a partition. Every partition has a primary and, with `backups=1`, a backup on a different node. The partition count is a cache property set at creation time. Which node owns a given partition depends on the live topology and shifts when nodes join or leave.

**A single node owns everything because it has to.** The partitions exist from the moment the cache is created, but with one node there is no other node to spread to. A second node activates `backups=1`.

**Rebalance is automatic, incremental, and loss-preserving.** When a node joins or leaves, the engine reassigns the minimum number of partitions to match the new topology, copies the underlying entries, and keeps the cache serving reads and writes.

**32 is a teaching number, not a production number.** The default of 1024 is the right choice for most workloads. You picked 32 so the per-node counts stayed small enough to count. A later guide covers when and how to change the default.

Beyond Key-Value and the Design for Data Locality path build directly on this mental model. The next layer is controlling placement, and control starts with knowing what the engine does on your behalf.

### What's Next

- [From Key-Value to SQL: The JOIN Problem](../beyond-key-value/from-keyvalue-to-sql.md) uses partitioning directly. JOIN correctness depends on putting related rows in the same partition, and the tutorial walks through the failure mode before showing the fix.
- [Design for Data Locality](../data-locality/README.md), a dedicated path for readers who will design a production schema, covers affinity keys, compute gravity, and the tradeoffs of partition count.
- [How to Choose a Partition Count for Your Workload](../../how-to-guides/choose-partition-count.md) covers the 1024 default and when to deviate.

### Related

- [Use Transactions with the Cache API](cache-transactions.md) added multi-key atomicity to the Foundations path. Transactions and distribution combine in the Beyond Key-Value path, where colocated writes commit faster than cross-node writes.
- [Work with the Cache API](../../quick-start/work-with-cache-api.md) introduced the thick client used throughout.
