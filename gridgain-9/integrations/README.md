---
description: >-
  Integrate GridGain 9 with external systems and frameworks, including Apache
  Kafka, Spring Boot, Spring Data, and Hibernate.
icon: wrench
---

# Integrations

GridGain 9 provides ready-made integrations that connect your cluster to popular data-streaming systems and application frameworks. Use these extensions to move data in and out of GridGain with Apache Kafka, or to work with GridGain from Spring and Hibernate applications.

- [Kafka Sink Connector](kafka-sink.md) — import Kafka topic data into GridGain tables.
- [Kafka Source Connector](kafka-source.md) — export GridGain table data to Kafka topics.
- [Spring Boot integration](spring-boot.md) — auto-configure a GridGain client in a Spring Boot application.
- [Spring Data integration](spring-data.md) — use Spring Data JDBC repositories with GridGain.
- [Hibernate integration](hibernate.md) — use GridGain as a query database and a Hibernate second-level cache.

{% columns %}
{% column %}
{% content-ref url="kafka-sink.md" %}
[Kafka Sink Connector](kafka-sink.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Import Kafka topic data into GridGain 9 tables with the GridGain Kafka Sink Connector — configuration, topic mapping, type conversion, and streamer receivers.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="kafka-source.md" %}
[Kafka Source Connector](kafka-source.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Export GridGain 9 table data to Kafka topics with the GridGain Kafka Source Connector — configuration, topic mapping, and type conversion.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="spring-boot.md" %}
[Spring Boot Integration](spring-boot.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Use GridGain 9 in a Spring Boot application through auto-configuration — Maven setup, client configuration, authentication, and SSL/TLS.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="spring-data.md" %}
[Spring Data Integration](spring-data.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Use Spring Data JDBC repositories with GridGain 9 through the IgniteDialect — Maven setup, entities, repositories, custom queries, and pagination.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="hibernate.md" %}
[Hibernate Integration](hibernate.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Use GridGain 9 with Hibernate as a query database and a second-level (L2) cache provider — installation, dialect configuration, entities, and cache concurrency strategies.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="k8s-operator/" %}
[Kubernetes Operator](k8s-operator/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Deploy and manage GridGain 9 clusters on Kubernetes with the GridGain Kubernetes Operator.
{% endcolumn %}
{% endcolumns %}
