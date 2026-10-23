---
description: >-
  Span partitions with atomic multi-key writes, no cross-shard glue code required.
---

# Atomic Operations Across Keys: The Transaction Problem

<!-- TODO (release): the Maven version 8.10.0 is not yet published on the GridGain Nexus repository (it has no 8.10 version), so the pom in this page cannot resolve until it is. After the 8.10.0 release, check that each of these resolves, update this page if the final names differ, and delete this comment. -->

## Introduction

In a sharded cache, multi-key writes are only atomic when the keys live on the same shard. Cross-shard atomicity has historically meant application-layer work: key co-location, per-shard scripting, or compensation after partial failures. Each option pushes consistency work back into your code. You already covered `txStart`, `commit`, and the optimistic retry pattern on a single-node cluster. This tutorial puts that same API on a three-node cluster, shows how `OPTIMISTIC + REPEATABLE_READ` silently drops writes, and ends with the production retry pattern wrapped around any optimistic transaction.

## Prerequisites

- **A running three-node cluster** using `cache-cluster/docker-compose-3nodes.yml` from [Understand How Your Cache Is Distributed](../cache-centric-foundations/understand-cache-distribution.md). The per-node configs in `cache-cluster/docker-compose-3nodes.yml` pin discovery and communication ports and register a `BasicAddressResolver` so a host JVM thick client can reach each container through the loopback address. Peer class loading is enabled on every server.
- **Transaction API familiarity** from [Use Transactions with the Cache API](../cache-centric-foundations/cache-transactions.md)
- **Java 17 or later** for the client runtime
- **Maven 3.6** or later
- **Docker Compose 2.23** or later

This tutorial builds a fresh Maven project called `cross-partition-tx/`. It does not extend the `cache-client/` project from the foundations path because the cache shape is different.

<details>
<summary>Resuming this tutorial: verify the three-node cluster is running</summary>

Check that all three nodes are up:

```bash
docker ps --filter name=gridgain8-node --format "table {{.Names}}\t{{.Status}}"
```

Expected output:

```text
NAMES             STATUS
gridgain8-node1   Up X hours
gridgain8-node2   Up X hours
gridgain8-node3   Up X hours
```

If a container is stopped, restart with `docker compose -f cache-cluster/docker-compose-3nodes.yml start`. If the cluster was destroyed, recreate it from the three-node compose in the cache distribution tutorial. The cache is in memory. Running `ConfigureAccountCache` after a restart recreates it.

</details>

## What You Will Learn

In this tutorial, you:

- Configure a `TRANSACTIONAL` cache and verify its atomicity mode from a host JVM thick client
- Run a `txStart` transfer between two keys on a multi-node cluster and watch the commit phase complete without any explicit cross-partition handling
- Watch one transaction silently overwrite another's committed work under `OPTIMISTIC + REPEATABLE_READ`
- Catch the same conflict under `OPTIMISTIC + SERIALIZABLE` as `org.apache.ignite.transactions.TransactionOptimisticException` and apply exponential backoff with a bounded retry budget

## Configure a Transactional Account Cache

Create a Maven project called `cross-partition-tx/`. The `pom.xml` depends on `gridgain-core` and includes the `--add-opens` entries Java 17 reflection requires. The thick client joins the cluster through the discovery seeds the host can reach (`127.0.0.1:47500`, `47501`, `47502`). The per-node `BasicAddressResolver` maps each container's hostname to `127.0.0.1` so the rest of the protocol routes through the loopback interface. `-Djava.net.preferIPv4Stack=true` skips the IPv6 join attempt that otherwise costs ten seconds on a fresh client.

{% code title="cross-partition-tx/pom.xml" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>cross-partition-tx</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.release>17</maven.compiler.release>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <exec.mainClass>com.example.transactions.ConfigureAccountCache</exec.mainClass>
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
                        <argument>--add-opens</argument>
                        <argument>java.base/java.math=ALL-UNNAMED</argument>
                        <argument>--add-opens</argument>
                        <argument>java.base/java.net=ALL-UNNAMED</argument>
                        <argument>--add-opens</argument>
                        <argument>jdk.management/com.sun.management.internal=ALL-UNNAMED</argument>
                        <argument>-Djava.net.preferIPv4Stack=true</argument>
                        <argument>-DIGNITE_QUIET=true</argument>
                        <argument>-DIGNITE_NO_ASCII=true</argument>
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

The `Account` model is a plain serializable POJO. The cluster stores the bytes and never deserializes the value server-side. Only the host JVM reads back what it wrote, so Java serialization is enough for this tutorial.

{% code title="cross-partition-tx/src/main/java/com/example/transactions/model/Account.java" %}
```java
package com.example.transactions.model;

import java.io.Serializable;
import java.math.BigDecimal;

/**
 * Account record stored in the transactional Account cache.
 *
 * BigDecimal stores money values exactly. The server stores raw bytes
 * and only the host JVM ever deserializes the value, so implementing
 * Serializable is the minimum bar. A custom binary type would buy
 * faster put/get at the cost of an annotation pass that this tutorial
 * does not need.
 *
 * The cluster never inspects the fields. SQL queries are out of scope
 * for this tutorial, so no @QuerySqlField annotations are required.
 * Adding SQL on this cache in a later tutorial would require those
 * annotations and the bytecode would need to load on the server JVM.
 */
public class Account implements Serializable {
    private static final long serialVersionUID = 1L;

    private Integer accountId;
    private BigDecimal balance;

    public Account() {}

    public Account(Integer accountId, BigDecimal balance) {
        this.accountId = accountId;
        this.balance = balance;
    }

    public Integer getAccountId() { return accountId; }
    public void setAccountId(Integer accountId) { this.accountId = accountId; }

    public BigDecimal getBalance() { return balance; }
    public void setBalance(BigDecimal balance) { this.balance = balance; }
}
```
{% endcode %}

`ConfigureAccountCache` creates the cache with `setAtomicityMode(CacheAtomicityMode.TRANSACTIONAL)` and one backup per partition. ATOMIC caches throw if you operate on them inside a transaction, as the cache transactions tutorial showed. This cache stays TRANSACTIONAL throughout.

{% code title="cross-partition-tx/src/main/java/com/example/transactions/ConfigureAccountCache.java" %}
```java
package com.example.transactions;

import java.util.Arrays;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.cache.CacheAtomicityMode;
import org.apache.ignite.configuration.CacheConfiguration;
import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi;
import org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder;

import com.example.transactions.model.Account;

/**
 * Creates the Account cache the rest of the tutorial depends on.
 *
 * The cache is TRANSACTIONAL with one backup per partition.
 * TRANSACTIONAL is the opt-in for txStart. ATOMIC caches throw
 * IgniteException when used inside a transaction. backups=1
 * means every primary partition has a replica on a second node, so a
 * single-node failure does not lose uncommitted writes.
 *
 * getOrCreateCache is idempotent. Re-running this class on an
 * existing cache returns the existing configuration without
 * overwriting settings. That makes the class safe to run between
 * scenarios while iterating on the rest of the tutorial.
 *
 * The class shows the baseline thick-client connection pattern.
 * Every other class (CrossPartitionTransfer, SilentDropDemo,
 * RetryingTransfer) repeats the same discovery and IgniteConfiguration
 * setup, then does its work.
 */
public class ConfigureAccountCache {

    /** Cluster-wide name of the cache. The name is the contract.
     *  Every other class in this project calls cache("Account") to
     *  reach the same data. */
    private static final String CACHE_NAME = "Account";

    public static void main(String[] args) {
        // The cluster's BasicAddressResolver advertises 127.0.0.1
        // alongside the docker-internal IP, so the host JVM reaches
        // each node via loopback. The address list spans the three
        // discovery ports pinned in cache-cluster/ignite-config-nodeN.xml.
        TcpDiscoverySpi disco = new TcpDiscoverySpi();
        disco.setIpFinder(new TcpDiscoveryVmIpFinder()
            .setAddresses(Arrays.asList(
                "127.0.0.1:47500",
                "127.0.0.1:47501",
                "127.0.0.1:47502")));

        IgniteConfiguration cfg = new IgniteConfiguration();
        cfg.setDiscoverySpi(disco);
        cfg.setClientMode(true);
        // Peer class loading must match the server's flag. The cluster
        // config has it enabled, so a mismatch fails the handshake.
        cfg.setPeerClassLoadingEnabled(true);

        try (Ignite ignite = Ignition.start(cfg)) {
            // TRANSACTIONAL is the opt-in for txStart. The default
            // (ATOMIC) is faster for single-key operations but throws
            // when wrapped in a transaction. setBackups(1) keeps a
            // replica on a second node so the partition survives a
            // primary failure between commit and the next read.
            CacheConfiguration<Integer, Account> ccfg =
                new CacheConfiguration<Integer, Account>(CACHE_NAME)
                    .setAtomicityMode(CacheAtomicityMode.TRANSACTIONAL)
                    .setBackups(1);

            IgniteCache<Integer, Account> cache = ignite.getOrCreateCache(ccfg);

            // Read the configuration back from the cache to verify
            // the cluster accepted the requested atomicity and backup
            // count. A pre-existing cache with different settings
            // would surface in this output as a sanity check.
            CacheConfiguration<?, ?> current =
                cache.getConfiguration(CacheConfiguration.class);
            System.out.println("=== Account cache configured ===");
            System.out.println("name:          " + current.getName());
            System.out.println("atomicityMode: " + current.getAtomicityMode());
            System.out.println("backups:       " + current.getBackups());
        }

        // Force clean shutdown so GridGain's background discovery threads
        // do not keep the JVM alive after the client closes.
        System.exit(0);
    }
}
```
{% endcode %}

Run it. Compile first because `exec:exec` does not trigger compilation on its own.

```bash
mvn -f cross-partition-tx/pom.xml compile
mvn -f cross-partition-tx/pom.xml exec:exec
```

Expected output:

```text
=== Account cache configured ===
name:          Account
atomicityMode: TRANSACTIONAL
backups:       1
```

`getOrCreateCache` is idempotent. Re-running this class on an existing cache returns the existing configuration without overwriting it.

{% hint style="success" %}
**Checkpoint:** The Account cache exists with TRANSACTIONAL atomicity and one backup, ready for `txStart` operations.
{% endhint %}

## Run a Cross-Partition Transfer

Seed four accounts at 100.00 each and transfer 25.00 between two of them inside a transaction. The cluster has three nodes with 1024 partitions by default. Each account ID hashes to a partition whose primary sits on one of the three nodes. Two account IDs may land on the same primary or on different primaries depending on their hashes, and the application code stays identical either way.

{% code title="cross-partition-tx/src/main/java/com/example/transactions/CrossPartitionTransfer.java" %}
```java
package com.example.transactions;

import java.math.BigDecimal;
import java.util.Arrays;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi;
import org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder;
import org.apache.ignite.transactions.Transaction;

import com.example.transactions.model.Account;

/**
 * Runs a transfer between two account keys inside a default
 * (PESSIMISTIC + REPEATABLE_READ) transaction on a multi-node cluster.
 *
 * The cache has 1024 partitions distributed across three nodes. Two
 * account IDs (1001, 1003) hash to two partitions, and whether those
 * partitions share a primary node depends on the affinity function
 * and the current topology. The application code is identical either
 * way: txStart, get, get, put, put, commit. The cluster routes 2PC
 * participants automatically.
 *
 * Each operation prints a microsecond timestamp from the start of
 * main. The trace exposes the wall-clock breakdown of a single
 * transaction. The commit-phase line at the end isolates the 2PC
 * duration from the rest of the work.
 *
 * The seed step at the top resets balances to 100.00 so re-runs are
 * deterministic. Production code would not include the seeder. It
 * exists in this tutorial because the steps assume a fresh start each
 * run.
 */
public class CrossPartitionTransfer {

    private static final String CACHE_NAME = "Account";

    public static void main(String[] args) {
        // Discovery + client setup is identical across the four classes
        // in this project. See ConfigureAccountCache for the rationale.
        TcpDiscoverySpi disco = new TcpDiscoverySpi();
        disco.setIpFinder(new TcpDiscoveryVmIpFinder()
            .setAddresses(Arrays.asList(
                "127.0.0.1:47500",
                "127.0.0.1:47501",
                "127.0.0.1:47502")));

        IgniteConfiguration cfg = new IgniteConfiguration();
        cfg.setDiscoverySpi(disco);
        cfg.setClientMode(true);
        cfg.setPeerClassLoadingEnabled(true);

        try (Ignite ignite = Ignition.start(cfg)) {
            IgniteCache<Integer, Account> cache = ignite.cache(CACHE_NAME);

            // Reset balances so each run starts from a known state.
            // IDs 1001-1004 give the baseline transfer pair (1001 -> 1002)
            // and two spare accounts. SilentDropDemo and RetryingTransfer
            // seed a fresh ID (1006) inside their own classes so each
            // scenario is independent. The seed below is idempotent.
            for (int id : new int[]{1001, 1002, 1003, 1004}) {
                cache.put(id, new Account(id, new BigDecimal("100.00")));
            }
            System.out.println("Seeded 4 accounts at 100.00 each");

            int FROM = 1001;
            int TO = 1003;
            BigDecimal amount = new BigDecimal("25.00");

            System.out.printf("Before: %d=%s, %d=%s%n",
                FROM, cache.get(FROM).getBalance(),
                TO, cache.get(TO).getBalance());

            final long startWall = System.nanoTime();

            // txStart() defaults to PESSIMISTIC + REPEATABLE_READ. Each
            // get below acquires a write lock on the primary owner of
            // its key. Cross-partition keys land on different primaries,
            // so the locks live on different nodes.
            try (Transaction tx = ignite.transactions().txStart()) {
                logUs(startWall, "txStart");

                Account from = cache.get(FROM);
                logUs(startWall, "read " + FROM + "=" + from.getBalance());

                Account to = cache.get(TO);
                logUs(startWall, "read " + TO + "=" + to.getBalance());

                // put writes to the transaction-local view. The cluster
                // does not see these writes until commit.
                cache.put(FROM, new Account(FROM, from.getBalance().subtract(amount)));
                logUs(startWall, "put " + FROM);

                cache.put(TO, new Account(TO, to.getBalance().add(amount)));
                logUs(startWall, "put " + TO);

                long preCommit = (System.nanoTime() - startWall) / 1_000;
                // 2PC: commit() returns after prepare-then-commit lands
                // on every partition primary the transaction touched.
                // Cross-node primaries add a round trip versus colocated.
                tx.commit();
                long postCommit = (System.nanoTime() - startWall) / 1_000;
                logUs(startWall, "committed");
                System.out.printf("commit phase: %d us%n", postCommit - preCommit);
            }

            System.out.printf("After:  %d=%s, %d=%s%n",
                FROM, cache.get(FROM).getBalance(),
                TO, cache.get(TO).getBalance());
        }

        System.exit(0);
    }

    /**
     * Prints a microsecond stamp since the start of main for the
     * given event label. Microseconds rather than milliseconds
     * because the cluster's intra-LAN latencies can be sub-millisecond
     * and milliseconds would round most operations to 0.
     *
     * @param start Reference nanosecond timestamp from System.nanoTime.
     * @param event Label to print after the timestamp.
     */
    private static void logUs(long start, String event) {
        long us = (System.nanoTime() - start) / 1_000;
        System.out.printf("  [%7dus] %s%n", us, event);
    }
}
```
{% endcode %}

Run it:

```bash
mvn -f cross-partition-tx/pom.xml compile
mvn -f cross-partition-tx/pom.xml exec:exec -Dexec.mainClass=com.example.transactions.CrossPartitionTransfer
```

Expected output (run-to-run timing varies):

```text
Seeded 4 accounts at 100.00 each
Before: 1001=100.00, 1003=100.00
  [   1678us] txStart
  [  11346us] read 1001=100.00
  [  15042us] read 1003=100.00
  [  15525us] put 1001
  [  15841us] put 1003
  [  24151us] committed
commit phase: 8198 us
After:  1001=75.00, 1003=125.00
```

The trace records four operations and a commit:

1. `txStart` opens the transaction.
2. The two `cache.get` calls acquire pessimistic locks on the primary owners of each key.
3. The two `cache.put` calls write to the transaction-local view.
4. `commit` runs the two-phase protocol across whichever primaries own the keys.

Commit duration is the only number that depends on whether the keys live on different nodes. Cross-node commits add a network round trip per primary. The partition layout never surfaces in the application code.

Commit-phase microseconds reflect the two-phase protocol against every primary the transaction touched. The thick client drives prepare and commit messages over the communication SPI to those primaries directly, so the wall-clock trace records the network round trips that a single-connection client would have collapsed into one figure.

{% hint style="success" %}
**Checkpoint:** The transaction commits and the balances change to 75.00 and 125.00. The `txStart` pattern from the foundations path runs against the multi-node cluster unchanged.
{% endhint %}

## Watch OPTIMISTIC + REPEATABLE_READ Silently Lose Writes

The previous step used `PESSIMISTIC + REPEATABLE_READ`, the default returned by the no-argument `txStart()`. Pessimistic locking acquires a write lock on every key the transaction touches, so two contending transactions serialize. One waits for the other to release. Switching the concurrency to `OPTIMISTIC` removes the locks and trades them for a commit-time validation step, but the validation runs only under specific isolation levels.

OPTIMISTIC concurrency relies on commit-time validation. When the transaction tries to commit, the cluster checks whether any key in the read set was modified by another transaction that committed first. A modified read key fails the commit. That validation runs under `TransactionIsolation.SERIALIZABLE` only. `REPEATABLE_READ` and `READ_COMMITTED` skip it.

That makes `OPTIMISTIC + REPEATABLE_READ` unsafe whenever a key is read and then written based on what was read. Two transactions reading the same pre-write value both write a value derived from it, and the second commit overwrites the first. No exception is thrown, so the lost transaction never surfaces to the application.

This step proves the behavior with a deterministic interleave. tx1 reads, tx2 commits its own transfer inside tx1's window, then tx1 writes and commits with the values it read before tx2 ran. The lost-update outcome is the same shape a concurrent race between two contending transactions produces. The sequential interleave is the honest tradeoff: same outcome, deterministic across runs, no timing assumptions baked into the code. Thick-client transactions bind to the current thread through thread-local state, so a single thread cannot hold two transactions open at once. The interleave runs on two threads inside one GridGain client. Two `CountDownLatch` instances enforce the order. tx1 releases the first latch after reading, which lets tx2 run a full transfer and commit. tx2 releases the second latch in a `finally` block, which lets tx1 wake up and write its own values.

{% code title="cross-partition-tx/src/main/java/com/example/transactions/SilentDropDemo.java" %}
```java
package com.example.transactions;

import java.math.BigDecimal;
import java.util.Arrays;
import java.util.concurrent.CountDownLatch;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.IgniteTransactions;
import org.apache.ignite.Ignition;
import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi;
import org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder;
import org.apache.ignite.transactions.Transaction;
import org.apache.ignite.transactions.TransactionConcurrency;
import org.apache.ignite.transactions.TransactionIsolation;

import com.example.transactions.model.Account;

/**
 * Two interleaved OPTIMISTIC + REPEATABLE_READ transactions show how
 * the cluster silently drops one transaction's update.
 *
 * Both transactions read the same pre-transfer balances, compute
 * derived writes from those reads, and commit successfully. The
 * second commit overwrites the first. The first transaction's update
 * is silently lost. No error fires on either side.
 *
 * The interleave is sequential, not concurrent. Inside tx1's
 * read-write window, tx2 starts, transfers, and commits. Then tx1
 * writes and commits with stale data. The sequential interleave makes
 * the outcome deterministic across runs,
 * with no timing assumptions baked into the test.
 *
 * Thick-client transactions bind to the current thread through
 * thread-local state, so a single thread cannot hold two transactions
 * open at once. The interleave runs on two threads inside one GridGain
 * client. Two CountDownLatch instances enforce the order. tx1
 * releases the first latch after reading, which lets tx2 run a full
 * transfer and commit. tx2 releases the second latch in a finally
 * block, which lets tx1 wake up and write its own values.
 *
 * One GridGain client serves both threads because each thread has its
 * own thread-local transaction state. Two clients on the same JVM
 * would also work but pay the discovery handshake twice and surface
 * two members in the cluster topology, which would obscure the
 * single-application-process framing.
 *
 * Under OPTIMISTIC, the cluster validates the read set at commit
 * only when the isolation level is SERIALIZABLE. REPEATABLE_READ
 * does not validate. The next class (RetryingTransfer) shows
 * SERIALIZABLE catching this exact scenario and how to retry it.
 */
public class SilentDropDemo {

    private static final String CACHE_NAME = "Account";

    public static void main(String[] args) throws InterruptedException {
        // Discovery seeds for the three-node cluster. See
        // ConfigureAccountCache for the rationale.
        TcpDiscoverySpi disco = new TcpDiscoverySpi();
        disco.setIpFinder(new TcpDiscoveryVmIpFinder()
            .setAddresses(Arrays.asList(
                "127.0.0.1:47500",
                "127.0.0.1:47501",
                "127.0.0.1:47502")));

        IgniteConfiguration cfg = new IgniteConfiguration();
        cfg.setDiscoverySpi(disco);
        cfg.setClientMode(true);
        cfg.setPeerClassLoadingEnabled(true);

        try (Ignite ignite = Ignition.start(cfg)) {
            IgniteCache<Integer, Account> cache = ignite.cache(CACHE_NAME);

            // Reset balances so re-runs are deterministic. The lost-
            // update outcome depends on tx1 and tx2 starting from the
            // same value. A previous run that left non-100.00 balances
            // would produce printed sums that do not match the prose.
            cache.put(1001, new Account(1001, new BigDecimal("100.00")));
            cache.put(1006, new Account(1006, new BigDecimal("100.00")));

            System.out.println("Initial:  1001=100.00, 1006=100.00 (sum=200.00)");

            // The latches force the lost-update interleave: tx1 captures
            // its read set, hands control to tx2, waits for tx2 to
            // commit, then writes its own derived values.
            CountDownLatch tx1ReadDone = new CountDownLatch(1);
            CountDownLatch tx2Committed = new CountDownLatch(1);

            IgniteTransactions txs = ignite.transactions();

            // tx1: OPTIMISTIC + REPEATABLE_READ does not validate the
            // read set at commit, so tx1's writes silently overwrite the
            // tx2 values that committed in the gap.
            Thread t1 = new Thread(() -> {
                try (Transaction tx1 = txs.txStart(
                        TransactionConcurrency.OPTIMISTIC,
                        TransactionIsolation.REPEATABLE_READ)) {
                    Account from1 = cache.get(1001);
                    Account to1 = cache.get(1006);
                    System.out.printf("tx1 reads 1001=%s, 1006=%s%n",
                        from1.getBalance(), to1.getBalance());

                    tx1ReadDone.countDown();
                    tx2Committed.await();

                    cache.put(1001, new Account(1001,
                        from1.getBalance().subtract(new BigDecimal("10.00"))));
                    cache.put(1006, new Account(1006,
                        to1.getBalance().add(new BigDecimal("10.00"))));
                    tx1.commit();
                    System.out.println("tx1 transfers 10.00 (1001 -> 1006), commits");
                } catch (InterruptedException ie) {
                    Thread.currentThread().interrupt();
                }
            }, "tx1");

            // tx2 waits for tx1's read set, then runs and commits before
            // tx1 writes. The finally block releases the second latch so
            // tx1 cannot deadlock if tx2 throws.
            Thread t2 = new Thread(() -> {
                try {
                    tx1ReadDone.await();
                    try (Transaction tx2 = txs.txStart(
                            TransactionConcurrency.OPTIMISTIC,
                            TransactionIsolation.REPEATABLE_READ)) {
                        Account from2 = cache.get(1001);
                        Account to2 = cache.get(1006);
                        cache.put(1001, new Account(1001,
                            from2.getBalance().subtract(new BigDecimal("25.00"))));
                        cache.put(1006, new Account(1006,
                            to2.getBalance().add(new BigDecimal("25.00"))));
                        tx2.commit();
                        System.out.println("tx2 transfers 25.00 (1001 -> 1006), commits");
                    }
                } catch (InterruptedException ie) {
                    Thread.currentThread().interrupt();
                } finally {
                    tx2Committed.countDown();
                }
            }, "tx2");

            t1.start();
            t2.start();
            t1.join();
            t2.join();

            // Final values reflect tx1's derived writes; REPEATABLE_READ
            // skipped the read-set validation that would have caught the
            // conflict, so tx2's update is silently lost.
            BigDecimal a = cache.get(1001).getBalance();
            BigDecimal b = cache.get(1006).getBalance();
            System.out.printf("%nExpected if both transfers persisted:  1001=65.00, 1006=135.00%n");
            System.out.printf("Actual final:                          1001=%s, 1006=%s%n", a, b);
            System.out.println("                                       ^---- tx2's 25.00 transfer silently lost");
        }

        System.exit(0);
    }
}
```
{% endcode %}

Run it:

```bash
mvn -f cross-partition-tx/pom.xml compile
mvn -f cross-partition-tx/pom.xml exec:exec -Dexec.mainClass=com.example.transactions.SilentDropDemo
```

Expected output:

```text
Initial:  1001=100.00, 1006=100.00 (sum=200.00)
tx1 reads 1001=100.00, 1006=100.00
tx2 transfers 25.00 (1001 -> 1006), commits
tx1 transfers 10.00 (1001 -> 1006), commits

Expected if both transfers persisted:  1001=65.00, 1006=135.00
Actual final:                          1001=90.00, 1006=110.00
                                       ^---- tx2's 25.00 transfer silently lost
```

Two transactions ran, both committed, and both APIs returned without an error. Only tx1's transfer of 10.00 is visible in the final state. tx2's transfer of 25.00 is gone. The sum is still 200.00 because tx1 was an internally balanced transfer, and the application has no signal that tx2's work was discarded.

The failure mode is the contract. `REPEATABLE_READ` does not validate the read set, and `OPTIMISTIC` defers all conflict detection to commit-time validation. With validation off, both transactions read the same value, both compute writes derived from it, and both commits succeed. The second commit wins and the earlier transaction's update is silently overwritten.

`SERIALIZABLE` is the only isolation level that catches this. Under `OPTIMISTIC + SERIALIZABLE`, the cluster validates the read set at commit and throws if another transaction has modified a read key. The next step runs the same scenario under `SERIALIZABLE` and shows how to recover.

{% hint style="success" %}
**Checkpoint:** Both transactions committed without an exception, but the final balances show only one transfer survived. The other transaction's work was silently overwritten.
{% endhint %}

## Catch and Retry Optimistic Conflicts

Switch the isolation level from `REPEATABLE_READ` to `SERIALIZABLE` and the same interleave produces a different outcome. The cluster now validates the read set at commit, sees that another transaction modified a key after tx1 read it, and rejects tx1's commit. The lost update from the prior step becomes a typed failure the application can catch and retry.

The thick client surfaces optimistic conflicts as `org.apache.ignite.transactions.TransactionOptimisticException`, a subclass of `IgniteException`. A `catch` block matched on that type is the production discriminator. No message-text inspection is required. Other failure modes (timeout, deadlock, communication failure) surface as their own typed subclasses and propagate independently.

`RetryingTransfer` runs two scenarios from `main`. The first reuses the conflict pattern from the previous step under `SERIALIZABLE` and catches the exception so you can see what surfaces. The second runs the same operations inside a retry loop that recovers on the next attempt.

{% code title="cross-partition-tx/src/main/java/com/example/transactions/RetryingTransfer.java" %}
```java
package com.example.transactions;

import java.math.BigDecimal;
import java.util.Arrays;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.IgniteTransactions;
import org.apache.ignite.Ignition;
import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi;
import org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder;
import org.apache.ignite.transactions.Transaction;
import org.apache.ignite.transactions.TransactionConcurrency;
import org.apache.ignite.transactions.TransactionIsolation;
import org.apache.ignite.transactions.TransactionOptimisticException;

import com.example.transactions.model.Account;

/**
 * Catches and retries OPTIMISTIC + SERIALIZABLE conflicts.
 *
 * Two scenarios run from main:
 *
 *   1) forcedConflictDemo: opens tx1, runs a conflicting tx2 on a
 *      separate thread, then tries to commit tx1. The commit throws
 *      TransactionOptimisticException because tx2 modified a key tx1
 *      had read. The exception type is the production discriminator.
 *      No message-text inspection is required.
 *
 *   2) retryDemo: same scenario wrapped in a retry loop. Attempt 0
 *      hits the planted conflict and sleeps. Attempt 1 reads the
 *      post-conflict state and commits cleanly. Exponential backoff
 *      with a cap spreads retries across different intervals so a
 *      crowd of contending transactions does not re-collide on the
 *      same boundary.
 *
 * Thick-client transactions bind to the current thread, so the
 * conflicting tx2 must run on a separate thread. The helper
 * runConflictingWrite spawns a thread, runs tx2 to commit, joins,
 * and returns. The surrounding tx1 sees a fait accompli when it
 * resumes.
 *
 * The retry budget bounds unrecoverable contention. Five attempts
 * cover a planted conflict, but a real workload may exhaust the
 * budget when contention is heavy enough that every retry re-collides
 * on the same boundary. Treat budget exhaustion as a typed failure
 * that alerts, dead-letters the work, or escalates to a human.
 */
public class RetryingTransfer {

    private static final String CACHE_NAME = "Account";

    /** Maximum retry attempts before giving up. Five is enough to
     *  recover from the planted conflict in retryDemo and from
     *  brief two- or three-way contention in production code. */
    private static final int RETRY_BUDGET = 5;

    /** Backoff multiplier in milliseconds. Powers of two give 10, 20,
     *  40, 80, 160ms. The cap below trims the high end to 100ms. */
    private static final long BASE_BACKOFF_MILLIS = 10L;

    /** Cap on per-attempt backoff to keep total retry time bounded. */
    private static final long MAX_BACKOFF_MILLIS = 100L;

    public static void main(String[] args) throws InterruptedException {
        // Discovery seeds for the three-node cluster. See
        // ConfigureAccountCache for the rationale.
        TcpDiscoverySpi disco = new TcpDiscoverySpi();
        disco.setIpFinder(new TcpDiscoveryVmIpFinder()
            .setAddresses(Arrays.asList(
                "127.0.0.1:47500",
                "127.0.0.1:47501",
                "127.0.0.1:47502")));

        IgniteConfiguration cfg = new IgniteConfiguration();
        cfg.setDiscoverySpi(disco);
        cfg.setClientMode(true);
        cfg.setPeerClassLoadingEnabled(true);

        try (Ignite ignite = Ignition.start(cfg)) {
            IgniteCache<Integer, Account> cache = ignite.cache(CACHE_NAME);
            IgniteTransactions txs = ignite.transactions();

            // Reset balances so each scenario starts clean.
            cache.put(1001, new Account(1001, new BigDecimal("100.00")));
            cache.put(1006, new Account(1006, new BigDecimal("100.00")));

            System.out.println("=== Forced conflict (no retry) ===");
            forcedConflictDemo(cache, txs);

            // Reset between scenarios. The first scenario rolled back
            // tx1 but tx2 committed, so the cache state has drifted
            // from the documented starting point.
            cache.put(1001, new Account(1001, new BigDecimal("100.00")));
            cache.put(1006, new Account(1006, new BigDecimal("100.00")));

            System.out.println("\n=== Same scenario with retry-with-backoff ===");
            retryDemo(cache, txs);
        }

        System.exit(0);
    }

    /**
     * Opens tx1 on the main thread, reads account 1001, then runs a
     * separate thread that opens tx2 and commits a write to the same
     * account. tx1's commit must throw because its read set was
     * invalidated by tx2's commit.
     *
     * The catch matches TransactionOptimisticException only. Other
     * failure modes (TransactionTimeoutException,
     * TransactionDeadlockException, IgniteClientDisconnectedException,
     * etc.) propagate out as uncaught throwables. That is the right
     * behavior for a tutorial focused on optimistic conflicts.
     *
     * @param cache The Account cache.
     * @param txs The cluster's transactions handle.
     * @throws InterruptedException If the conflicting-write helper
     *                              thread is interrupted while joining.
     */
    private static void forcedConflictDemo(IgniteCache<Integer, Account> cache,
                                            IgniteTransactions txs) throws InterruptedException {
        try (Transaction tx1 = txs.txStart(
                TransactionConcurrency.OPTIMISTIC,
                TransactionIsolation.SERIALIZABLE)) {
            Account from = cache.get(1001);
            System.out.println("tx1 read 1001=" + from.getBalance());

            // Plant a conflicting tx2 commit between tx1's read and
            // tx1's commit. runConflictingWrite joins its thread before
            // returning so the interleave is deterministic.
            runConflictingWrite(cache, txs);
            System.out.println("tx2 committed (modified 1001)");

            cache.put(1001, new Account(1001, from.getBalance().subtract(new BigDecimal("10.00"))));
            cache.put(1006, new Account(1006, cache.get(1006).getBalance().add(new BigDecimal("10.00"))));

            System.out.println("tx1 about to commit");
            // OPTIMISTIC + SERIALIZABLE validates the read set at commit.
            // Because 1001 changed since tx1 read it, commit() throws.
            tx1.commit();
            System.out.println("UNEXPECTED: tx1 committed without conflict");
        } catch (TransactionOptimisticException e) {
            // Typed catch. The class is the contract. The message body
            // names the conflicting key for diagnostics only.
            System.out.println("tx1 commit threw optimistic conflict");
            System.out.println("Class: " + e.getClass().getName());
            System.out.println("Message starts: " + firstLine(e.getMessage()));
        }
    }

    /**
     * Same scenario as forcedConflictDemo, but wraps the work in a
     * retry-with-backoff loop. The first attempt always conflicts
     * because runConflictingWrite plants a tx2 commit during the
     * attempt. The retry sees the post-conflict state and commits
     * cleanly without invoking runConflictingWrite again.
     *
     * Backoff matters when many transactions retry the same conflict.
     * Without it, every losing transaction retries at the same instant,
     * re-collides on the next attempt, and exhausts the budget in
     * milliseconds. Powers of two with a cap stagger the retries so
     * only a fraction collide on any given attempt.
     *
     * @param cache The Account cache.
     * @param txs The cluster's transactions handle.
     * @throws InterruptedException If the retry sleep is interrupted.
     */
    private static void retryDemo(IgniteCache<Integer, Account> cache,
                                   IgniteTransactions txs) throws InterruptedException {
        int retries = 0;
        boolean done = false;

        for (int attempt = 0; attempt < RETRY_BUDGET && !done; attempt++) {
            try (Transaction tx1 = txs.txStart(
                    TransactionConcurrency.OPTIMISTIC,
                    TransactionIsolation.SERIALIZABLE)) {
                Account from = cache.get(1001);

                // Plant the conflict on the first attempt only. Later
                // attempts read the post-conflict state and commit clean.
                if (attempt == 0) {
                    runConflictingWrite(cache, txs);
                }

                cache.put(1001, new Account(1001, from.getBalance().subtract(new BigDecimal("10.00"))));
                cache.put(1006, new Account(1006, cache.get(1006).getBalance().add(new BigDecimal("10.00"))));
                tx1.commit();
                done = true;
                System.out.printf("attempt %d committed%n", attempt);
            } catch (TransactionOptimisticException e) {
                retries++;
                long sleepMs = Math.min(BASE_BACKOFF_MILLIS * (1L << attempt),
                                         MAX_BACKOFF_MILLIS);
                System.out.printf("attempt %d: conflict, sleeping %dms%n", attempt, sleepMs);
                try {
                    Thread.sleep(sleepMs);
                } catch (InterruptedException ignored) {
                    Thread.currentThread().interrupt();
                    return;
                }
            }
        }

        if (!done) {
            // Budget exhausted. Retry alone cannot fix this.
            // Production code alerts, dead-letters, or escalates to
            // a human. This example prints the failure for the trace.
            System.out.printf("Retry budget exhausted after %d attempts%n", RETRY_BUDGET);
        } else {
            System.out.printf("Retries: %d, final result: committed%n", retries);
        }

        System.out.printf("Final balances: 1001=%s, 1006=%s%n",
            cache.get(1001).getBalance(),
            cache.get(1006).getBalance());
    }

    /**
     * Runs a conflicting write to account 1001 on a separate thread
     * and waits for it to commit. The new thread starts its own
     * OPTIMISTIC + SERIALIZABLE transaction because thick-client
     * transactions bind to the current thread. Running the write on
     * the main thread would collide with the surrounding tx1.
     *
     * The write adds 5.00 to the current balance. The amount itself
     * does not matter. Any modification of key 1001 produces the
     * same conflict.
     *
     * @param cache The Account cache the write targets.
     * @param txs The transactions handle the helper thread uses.
     * @throws InterruptedException If join is interrupted.
     */
    private static void runConflictingWrite(IgniteCache<Integer, Account> cache,
                                             IgniteTransactions txs) throws InterruptedException {
        Thread t = new Thread(() -> {
            try (Transaction tx2 = txs.txStart(
                    TransactionConcurrency.OPTIMISTIC,
                    TransactionIsolation.SERIALIZABLE)) {
                Account from2 = cache.get(1001);
                cache.put(1001, new Account(1001,
                    from2.getBalance().add(new BigDecimal("5.00"))));
                tx2.commit();
            }
        }, "tx2");
        t.start();
        t.join();
    }

    /**
     * Returns the leading text of an exception message, truncating at
     * the first "[" so the conflicting-key payload (and any nested
     * server-side diagnostics like BinaryInvalidTypeException during
     * value formatting) does not bloat the tutorial output. The
     * truncated suffix is replaced with "[...]" so the reader sees
     * that detail was elided.
     */
    private static String firstLine(String s) {
        if (s == null) return "(null)";
        int newline = s.indexOf('\n');
        String first = newline < 0 ? s : s.substring(0, newline);
        int bracket = first.indexOf('[');
        return bracket < 0 ? first : first.substring(0, bracket).trim() + " [...]";
    }
}
```
{% endcode %}

Run it:

```bash
mvn -f cross-partition-tx/pom.xml compile
mvn -f cross-partition-tx/pom.xml exec:exec -Dexec.mainClass=com.example.transactions.RetryingTransfer
```

Expected output:

```text
=== Forced conflict (no retry) ===
tx1 read 1001=100.00
tx2 committed (modified 1001)
tx1 about to commit
tx1 commit threw optimistic conflict
Class: org.apache.ignite.transactions.TransactionOptimisticException
Message starts: Failed to prepare transaction, read/write conflict [...]

=== Same scenario with retry-with-backoff ===
attempt 0: conflict, sleeping 10ms
attempt 1 committed
Retries: 1, final result: committed
Final balances: 1001=95.00, 1006=110.00
```

The first scenario confirms that the conflict surfaces at `tx1.commit()` as `TransactionOptimisticException`, a typed subclass of `IgniteException`. The catch block matches the exact exception class, so other failure modes (timeout, deadlock, communication failure) propagate out untouched. The full message names the conflicting key. On GridGain 8 it also includes a benign `BinaryInvalidTypeException` from the server's value-formatting path, so `firstLine` truncates at the first `[` to keep the trace readable. The contract is the type, not the text.

The second scenario wraps the same operations inside a retry loop. Attempt 0 hits the planted conflict and sleeps 10ms. Attempt 1 sees the post-tx2 state (1001 = 105.00) and commits its own transfer cleanly. The final balances match the arithmetic: tx2 added 5.00 to 1001, tx1 subtracted 10.00 from 1001 and added 10.00 to 1006, so 1001 ends at 95.00 and 1006 ends at 110.00.

The retry budget is the production failure surface. Five attempts cover the planted conflict, but a real workload may exhaust the budget when contention is heavy enough that every retry re-collides on the same boundary. Treat budget exhaustion as a typed failure that alerts, dead-letters the work, or escalates to a human. Retrying forever is not an option.

Exponential backoff matters when more than two transactions retry the same conflict. Without backoff, every losing transaction retries at the same instant, re-collides on the next attempt, and exhausts the budget in milliseconds. Powers of two (10, 20, 40, 80) with a cap of 100ms stagger the retries so only a fraction collide on any given attempt.

{% hint style="success" %}
**Checkpoint:** The forced conflict prints the exception class and message. The retry scenario recovers on the second attempt and the final balances match the expected post-transfer values.
{% endhint %}

## Summary

You ran `txStart` against a three-node cluster, and the transaction committed across two partition primaries without the application code ever seeing the routing. Two interleaved transactions then ran under `OPTIMISTIC + REPEATABLE_READ`. Both committed without an exception, but only one transfer survived. The other was silently overwritten. You closed the loop with `OPTIMISTIC + SERIALIZABLE`, which catches the same conflict, and a retry-with-backoff utility that recovers automatically.

**Cross-partition is not a separate API surface.** The cluster routes 2PC participants to whichever primaries own the transaction's keys, so the application opens a transaction, reads, writes, and commits with the same code it would use against a single key. The partition boundary appears in cluster timing rather than in code.

**The retry budget is the contract.** OPTIMISTIC concurrency converts contention into commit failures the application must handle. A retry loop with exponential backoff covers the recoverable cases, and the budget bounds the unrecoverable ones. When the budget exhausts, contention has crossed a threshold that retries cannot fix, and the alert lands on a human rather than on a transaction silently looping forever.

**OPTIMISTIC must pair with SERIALIZABLE.** `REPEATABLE_READ` under `OPTIMISTIC` is legal Java that returns no error and silently loses writes. The default `txStart()` returns `PESSIMISTIC + REPEATABLE_READ`, which is correct. Whenever you change the concurrency to `OPTIMISTIC`, change the isolation to `SERIALIZABLE` in the same call.

### What's Next

- `setDistributedJoins(true)` for the case where colocation is not possible, covered in [When to Break Colocation](../data-locality/when-to-break-colocation.md).
- Deadlock detection on `PESSIMISTIC` via the four-argument `txStart(c, i, timeout, txSize)` overload (coming soon). In the meantime, see [Deadlock Detection](../../gridgain8-development/transactions.md#deadlock-detection) in Performing Transactions.
- `TransactionConfiguration` for cluster-wide defaults that change every transaction's behavior at once (coming soon). In the meantime, see [Performing Transactions](../../gridgain8-development/transactions.md).

The next tutorial in this learning path, [Compute Where the Data Lives: The Round-Trip Problem](colocated-compute.md), moves from atomic writes to compute. When the data is too large to pull to the client, the answer is to ship the code to the data.

### Related

- [Use Transactions with the Cache API](../cache-centric-foundations/cache-transactions.md) covers the transaction API on a single-node cluster, including the `OPTIMISTIC + SERIALIZABLE` retry pattern that this tutorial extends.
- [Understand How Your Cache Is Distributed](../cache-centric-foundations/understand-cache-distribution.md) covers the partition layout and the Affinity API for inspecting placement. This tutorial reuses that cluster.
