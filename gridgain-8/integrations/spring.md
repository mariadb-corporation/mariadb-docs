---
description: >-
  Use GridGain 8 with Spring Framework 7: start a node from a Spring
  application context, use GridGain as a Spring cache, and manage GridGain
  transactions with Spring.
---

# Spring Integration

The `ignite-spring` module integrates GridGain with the Spring Framework. With this module, you can:

- Load node configuration from Spring XML files.
- Start a node from a Spring application context and inject Spring beans into GridGain tasks and jobs.
- Use GridGain caches as a Spring cache provider.
- Run GridGain transactions through Spring's declarative transaction management.

## Requirements

GridGain 8.10 uses Spring Framework 7. Spring Framework 5 and 6 are not supported.

Spring Framework 7 requires Java 17 or later, which matches the GridGain 8 [system requirements](../gridgain8-development/project-setup.md#system-requirements).

If your application runs on Spring Framework 5 or 6, see [Upgrading from GridGain 8.9](#upgrading-from-gridgain-8.9).

## Adding the Spring Module

In the binary distribution, the `ignite-spring` module is enabled by default and located in the `{GRIDGAIN_HOME}/libs/ignite-spring` directory. Besides the Spring Framework libraries, the directory contains `micrometer-observation`, `micrometer-commons`, and `jspecify`, which Spring Framework 7 requires at runtime. If you build the application classpath manually, include all libraries from this directory.

In a Maven project, add the `ignite-spring` dependency:

```xml
<properties>
    <gridgain.version>8.10</gridgain.version>
</properties>

<repositories>
    <repository>
        <id>GridGain Repository</id>
        <url>https://www.gridgainsystems.com/nexus/content/repositories/external</url>
    </repository>
</repositories>

<dependencies>
    <dependency>
        <groupId>org.gridgain</groupId>
        <artifactId>ignite-spring</artifactId>
        <version>${gridgain.version}</version>
    </dependency>
</dependencies>
```

Maven resolves the Spring Framework 7 libraries and their runtime dependencies transitively. Make sure that other dependencies in your project do not pull in an older Spring Framework version.

## Starting a Node from Spring

### IgniteSpringBean

`IgniteSpringBean` starts a GridGain node as a Spring bean, so you can reference the node from other beans without calling `Ignition` methods. The bean starts the node after all other singleton beans are initialized, and stops it when the application context is closed.

```xml
<bean id="mySpringBean" class="org.apache.ignite.IgniteSpringBean">
    <property name="configuration">
        <bean class="org.apache.ignite.configuration.IgniteConfiguration">
            <property name="igniteInstanceName" value="mySpringGrid"/>
        </bean>
    </property>
</bean>
```

If you omit the `configuration` property, the node starts with the default configuration.

```java
AbstractApplicationContext ctx = new FileSystemXmlApplicationContext("/path/to/spring/file");

// Stop the node when the JVM shuts down.
ctx.registerShutdownHook();

Ignite ignite = (Ignite)ctx.getBean("mySpringBean");
```

{% hint style="warning" %}
Because the node starts after other beans are initialized, do not reference `IgniteSpringBean` from bean initialization methods such as `@PostConstruct`. If another bean needs the node during initialization, use it from a `ContextRefreshedEvent` listener in that bean.
{% endhint %}

### IgniteSpring

The `IgniteSpring.start(...)` methods start a node and pass it a Spring application context. GridGain uses this context to inject Spring beans and the application context into tasks, jobs, and other GridGain components through the `@SpringResource` and `@SpringApplicationContextResource` annotations. For details, see [Resource Injection](../gridgain8-development/key-value-api/basic-cache-operations.md#resource-injection).

```java
ApplicationContext springCtx = new ClassPathXmlApplicationContext("app-context.xml");

Ignite ignite = IgniteSpring.start("config/ignite-config.xml", springCtx);
```

## Using GridGain as a Spring Cache

`SpringCacheManager` implements the [Spring Cache Abstraction](https://docs.spring.io/spring-framework/reference/integration/cache.html). Results of methods annotated with `@Cacheable` and related annotations are stored in GridGain caches. If a cache with the requested name does not exist, `SpringCacheManager` creates it on first access.

To use it, run a GridGain node in the same JVM as your application, and register `SpringCacheManager` as the cache manager in your application context. The cache manager can start the node itself or connect to a node that is already running.

Start a node from a configuration file. The path can be absolute or relative to `GRIDGAIN_HOME`:

```xml
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:cache="http://www.springframework.org/schema/cache"
       xsi:schemaLocation="
        http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/cache http://www.springframework.org/schema/cache/spring-cache.xsd">

    <bean id="cacheManager" class="org.apache.ignite.cache.spring.SpringCacheManager">
        <property name="configurationPath" value="config/spring-cache.xml"/>
    </bean>

    <cache:annotation-driven/>
</beans>
```

Use a node that is already running in the application:

```xml
<bean id="cacheManager" class="org.apache.ignite.cache.spring.SpringCacheManager">
    <property name="igniteInstanceName" value="myGrid"/>
</bean>
```

Then annotate the methods whose results you want to cache:

```java
@Cacheable("averageSalary")
public long averageSalary(int organizationId) {
    // Runs only if the result is not cached yet.
    ...
}

@CacheEvict(value = "averageSalary", key = "#e.organizationId")
public void updateSalary(Employee e) {
    ...
}
```

### SpringCacheManager Properties

| Property | Description | Default |
| --- | --- | --- |
| `configurationPath` | Path to the node configuration file. The cache manager starts a node with this configuration. Cannot be used together with `configuration`. | |
| `configuration` | `IgniteConfiguration` bean. The cache manager starts a node with this configuration. Cannot be used together with `configurationPath`. | |
| `igniteInstanceName` | Name of a running node to use. Used if neither `configurationPath` nor `configuration` is set. If no node with this name is running, an exception is thrown. | The default (unnamed) node |
| `dynamicCacheConfiguration` | `CacheConfiguration` template for caches the cache manager creates on first access. The cache name is set from the name used in the annotation. | Default cache configuration |
| `dynamicNearCacheConfiguration` | `NearCacheConfiguration` template for caches the cache manager creates on first access. If set, the caches are created with a [near cache](../gridgain8-development/near-caches.md). | |
| `locksCount` | Number of distributed locks used to synchronize value loading for `@Cacheable(sync = true)`. Keys are distributed among the locks by hash. | `512` |

If both `configurationPath` and `configuration` are set, the cache manager throws an `IllegalArgumentException`.

## Managing Transactions with Spring

`SpringTransactionManager` implements Spring's `PlatformTransactionManager`, so you can manage GridGain [transactions](../gridgain8-development/transactions.md) with `@Transactional` and other Spring transaction mechanisms. Cache operations in a method annotated with `@Transactional` run in a single GridGain transaction.

Like `SpringCacheManager`, the transaction manager uses a node in the same JVM, which it can start itself (`configurationPath` or `configuration`) or find by name (`igniteInstanceName`):

```xml
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:tx="http://www.springframework.org/schema/tx"
       xsi:schemaLocation="
        http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/tx http://www.springframework.org/schema/tx/spring-tx.xsd">

    <bean id="transactionManager" class="org.apache.ignite.transactions.spring.SpringTransactionManager">
        <property name="igniteInstanceName" value="myGrid"/>
        <property name="transactionConcurrency" value="PESSIMISTIC"/>
    </bean>

    <tx:annotation-driven/>
</beans>
```

The `transactionConcurrency` property sets the [concurrency mode](../gridgain8-development/transactions.md#concurrency-modes-and-isolation-levels) of all transactions the manager starts. If it is not set, the default concurrency from the node's `TransactionConfiguration` is used. To use both modes in one application, define two transaction managers and select one with a qualifier:

```xml
<bean id="optimisticTransactionManager" class="org.apache.ignite.transactions.spring.SpringTransactionManager">
    <property name="igniteInstanceName" value="myGrid"/>
    <property name="transactionConcurrency" value="OPTIMISTIC"/>
</bean>

<bean id="pessimisticTransactionManager" class="org.apache.ignite.transactions.spring.SpringTransactionManager">
    <property name="igniteInstanceName" value="myGrid"/>
    <property name="transactionConcurrency" value="PESSIMISTIC"/>
</bean>
```

```java
@Transactional("optimisticTransactionManager")
public void doOptimistically() {
    ...
}

@Transactional("pessimisticTransactionManager")
public void doPessimistically() {
    ...
}
```

The transaction manager maps `@Transactional` attributes to GridGain transaction parameters as follows:

| `@Transactional` attribute | GridGain transaction |
| --- | --- |
| `isolation = READ_COMMITTED`, `REPEATABLE_READ`, or `SERIALIZABLE` | The same isolation level. |
| `isolation = DEFAULT` | The default isolation from the node's `TransactionConfiguration`. |
| `isolation = READ_UNCOMMITTED` | Not supported. The transaction fails with `InvalidIsolationLevelException`. |
| `timeout` | Transaction timeout, converted from seconds to milliseconds. If not set, the default timeout from the node's `TransactionConfiguration` is used. |
| `propagation = NESTED` | Not supported. Nested transactions are not allowed. |

## Upgrading from GridGain 8.9

GridGain 8.9 used Spring Framework 5 by default and provided Spring Framework 6 through the optional `ignite-spring6` module. GridGain 8.10 uses only Spring Framework 7, and the `ignite-spring6` module is removed.

To upgrade:

1. Move applications that embed GridGain through Spring to Spring Framework 7 and Java 17 or later. If you cannot do that yet, keep using GridGain 8.9.
2. If you enabled `ignite-spring6` in GridGain 8.9, use the default `libs/ignite-spring` directory of the new distribution. Do not copy the old Spring module into `libs`.
3. If you build the classpath manually, add `micrometer-observation`, `micrometer-commons`, and `jspecify` from `libs/ignite-spring`.

Existing Spring XML configuration files continue to work. If they use `org.springframework.beans.factory.config.PropertyPlaceholderConfigurer`, consider switching to `org.springframework.context.support.PropertySourcesPlaceholderConfigurer`: `PropertyPlaceholderConfigurer` is deprecated in Spring Framework 7 and marked for removal.
