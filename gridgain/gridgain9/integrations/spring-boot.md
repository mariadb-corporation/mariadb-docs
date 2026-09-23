---
description: >-
  Use GridGain 9 in a Spring Boot application through auto-configuration —
  Maven setup, client configuration, authentication, and SSL/TLS.
---

# GridGain With Spring Boot

## Overview

GridGain provides Spring Boot integration through auto-configuration, making it easy to use GridGain client in your Spring Boot applications. The integration automatically configures an `IgniteClient` bean that can be injected into your Spring components, allowing you to interact with the GridGain cluster using familiar Spring patterns.

## Prerequisites

- Java 17 or higher
- Spring Boot 3.0 or higher
  {% hint style="info" %}
  Spring Data 4 is currently not supported.
  {% endhint %}
- A running GridGain 9 cluster

## Maven Configuration

To use GridGain with Spring Boot, add the following dependencies to your `pom.xml`:

{% code title="pom.xml" %}
```xml
<repositories>
    <repository>
        <id>GridGain External Repository</id>
        <url>https://www.gridgainsystems.com/nexus/content/repositories/external</url>
    </repository>
</repositories>

<dependencies>
    <dependency>
        <groupId>org.gridgain</groupId>
        <artifactId>spring-boot-starter-ignite-client</artifactId>
        <version>9.1</version>
    </dependency>
</dependencies>
```
{% endcode %}

The `spring-boot-starter-ignite-client` is a Spring Boot starter that includes all necessary dependencies and auto-configuration classes.

## Basic Configuration

### From Application Properties

The simplest way to configure GridGain in your Spring Boot application is through the `application.properties` file:

{% code title="application.properties" %}
```properties
ignite.client.addresses=127.0.0.1:10800
```
{% endcode %}

The auto-configuration will create an `IgniteClient` bean that connects to the specified address.

### Using the Client

Once configured, you can inject the `IgniteClient` into your Spring components:

{% code title="Java" %}
```java
@Service
public class MyService {

    @Autowired
    private IgniteClient client;

    public void createTable() {
        client.sql().execute(null,
            "CREATE TABLE IF NOT EXISTS Person (id INT PRIMARY KEY, name VARCHAR)");
    }

    public void insertData() {
        client.sql().execute(null,
            "INSERT INTO Person (id, name) VALUES (1, 'John')");
    }
}
```
{% endcode %}

## Configuration Properties

The Spring Boot integration supports all GridGain client configuration options through properties. All properties use the `ignite.client` prefix.

### Connection Properties

|Property|Type|Description|
|---|---|---|
|ignite.client.addresses|String[]|*Required.* Addresses of GridGain cluster nodes. Can be a comma-separated list.|
|ignite.client.connectTimeout|Long|Connection timeout in milliseconds. Default value is 5000 ms.|
|ignite.client.heartbeatInterval|Long|Heartbeat message interval in milliseconds. Default value is 1000 ms.|
|ignite.client.heartbeatTimeout|Long|Heartbeat message timeout in milliseconds. Default value is 5000 ms.|
|ignite.client.backgroundReconnectInterval|Long|Background reconnect interval in milliseconds. Default value is 30000 ms.|
|ignite.client.operationTimeout|Long|Operation timeout in milliseconds. Default value is 0 (no timeout).|

Example configuration with all connection properties:

{% code title="application.properties" %}
```properties
ignite.client.addresses=127.0.0.1:10800,127.0.0.1:10801
ignite.client.connectTimeout=10000
ignite.client.heartbeatInterval=30000
ignite.client.heartbeatTimeout=5000
ignite.client.backgroundReconnectInterval=30000
ignite.client.operationTimeout=60000
ignite.client.metricsEnabled=true
```
{% endcode %}

### Metrics Configuration

Enable client metrics to monitor connection statistics and performance:

{% code title="application.properties" %}
```properties
ignite.client.metricsEnabled=true
```
{% endcode %}

When metrics are enabled, the client will expose metrics that can be monitored using standard Java monitoring tools like JMX or JDK Mission Control.

## Authentication

### Basic Authentication

If [authentication](../security/authentication.md) is enabled on your GridGain cluster, you need to configure credentials. GridGain supports basic authentication with username and password.

#### Configuration File Approach

The simplest way to configure authentication is through properties:

{% code title="application.properties" %}
```properties
ignite.client.addresses=127.0.0.1:10800
ignite.client.auth.basic.username=myuser
ignite.client.auth.basic.password=mypassword
```
{% endcode %}

#### Programmatic Approach

For more control, you can configure authentication programmatically using `IgniteClientPropertiesCustomizer`:

{% code title="Java" %}
```java
@Configuration
public class IgniteConfiguration {

    @Bean
    public IgniteClientPropertiesCustomizer customizeClient() {
        return config -> {
            config.setAuthenticator(
                BasicAuthenticator.builder()
                    .username("myuser")
                    .password("mypassword")
                    .build()
            );
        };
    }
}
```
{% endcode %}

{% hint style="info" %}
The programmatic approach takes precedence over property-based configuration. If you define a customizer that sets an authenticator, it will override any authentication properties.
{% endhint %}

## SSL/TLS Configuration

GridGain supports SSL/TLS encryption for client-server communication. Configure SSL through properties:

{% code title="application.properties" %}
```properties
ignite.client.addresses=127.0.0.1:10800

# Enable SSL
ignite.client.sslConfiguration.enabled=true

# Keystore configuration
ignite.client.sslConfiguration.keyStorePath=/path/to/keystore.jks
ignite.client.sslConfiguration.keyStorePassword=keystorePassword

# Truststore configuration
ignite.client.sslConfiguration.trustStorePath=/path/to/truststore.jks
ignite.client.sslConfiguration.trustStorePassword=truststorePassword

# Optional: Specify allowed cipher suites (comma-separated)
# ignite.client.sslConfiguration.ciphers=TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,TLS_RSA_WITH_AES_128_GCM_SHA256
```
{% endcode %}

For detailed information on setting up SSL/TLS on the cluster side, see [SSL/TLS documentation](../security/ssl-tls.md).

## Setting Up Client

The example below shows how you can set up GridGain integration in your application:

{% code title="Java" %}
```java
@Service
public class PersonService {

    private final IgniteClient client;

    public PersonService(IgniteClient client) {
        this.client = client;
    }

    public void createPerson(int id, String name) {
        client.sql().execute(null,
            "INSERT INTO Person (id, name) VALUES (?, ?)",
            id, name);
    }

    public void createPersonInTransaction(int id, String name) {
        Transaction tx = client.transactions().begin();
        try {
            client.sql().execute(tx,
                "INSERT INTO Person (id, name) VALUES (?, ?)",
                id, name);
            tx.commit();
        } catch (Exception e) {
            tx.rollback();
            throw e;
        }
    }
}
```
{% endcode %}
