---
description: >-
  GridGain 9 is a unified real-time platform that stores and processes data
  across a cluster of interconnected machines.
icon: server
---

# GridGain 9

## What Is GridGain?

GridGain is a unified real-time platform for storing and processing data at scale.

GridGain is a platform that is designed to tackle speed and scale challenges. But what does that mean? In practice, it signifies that GridGain is capable of storing and processing your data across a cluster of interconnected machines that are deeply integrated into your environment.

GridGain APIs are developed in a way to minimize network traffic between cluster nodes and your applications. You can perform both distributed processing and distributed data storage for the applications.

GridGain builds on the technology that became Apache Ignite, whose original code was donated to the Apache Software Foundation (ASF) in 2014. Apache Ignite, one of the fastest ASF projects to graduate to top-level status, is now a top 5 ASF project in terms of contributions and dev-list activity and is downloaded millions of times annually.

GridGain 9 brings modern technologies to the platform, addressing the pain points of the previous major release.

## What Can You Do with GridGain?

We've seen many usage scenarios of GridGain in various environments and for various architectures. Among the benefits it provides are:

- Improved performance: In modern environments, performance is paramount. GridGain provides high throughput potential to keep up with demand of your customers.
- Dynamic scalability: You can scale your database dynamically to answer demand. New nodes can be added to GridGain cluster at peak demand times, and removed afterwards, all without downtime or performance drawbacks.
- Redundancy: While modern data centers provide high stability, it is still not guaranteed that your database server will not suddenly have an outage. GridGain provides redundancy for all data stored in it, potentially spanning several data centers for increased safety. Losing just one node does not significantly degrade the overall cluster performance, allowing you to keep up with any incidents.
- Distributed high performance computing (HPC): Computing tasks are vital for any modern business. With GridGain, you can have your computations split across multiple servers and colocated with required data, significantly increasing total computation performance.
- Digital integration: Almost no modern application uses a single tool, as there are best tools for each purpose. GridGain can act as the integration platform, rapidly transferring data between multiple interconnected systems.

{% columns %}
{% column %}
{% content-ref url="gridgain9-get-started/" %}
[Get Started](gridgain9-get-started/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A step-by-step introduction to GridGain 9: start a cluster, run SQL, persist data, use the Java API, work with secondary storage, and connect monitoring.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="architecture/" %}
[Architecture](architecture/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain 9 is built: cluster architecture, consensus, data distribution, consistency, availability, and storage.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="gridgain9-usage/" %}
[Usage](gridgain9-usage/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Guides for building applications on GridGain 9 — setting up a project, working with tables and SQL, and using the transactional, caching, and query APIs.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="gridgain9-management/" %}
[Management](gridgain9-management/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Guidance for operating a GridGain 9 cluster, covering configuration, storage, security, metrics, and recovery.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="security/" %}
[Security](security/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Secure a GridGain 9 cluster with SSL/TLS encryption, user authentication, role-based authorization, row-level security, and data encryption at rest.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="ha-and-performance/" %}
[HA and Performance](ha-and-performance/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Guidance for tuning GridGain 9 performance, covering general considerations, JVM, operating system, persistence, SQL, and data streaming.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="reference/" %}
[Reference](reference/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Reference material for GridGain 9: CLI, REST API, SQL syntax, configuration parameters, monitoring, error codes, and glossary.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="integrations/" %}
[Integrations](integrations/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Integrate GridGain 9 with external systems and frameworks, including Apache Kafka, Spring Boot, Spring Data, and Hibernate.
{% endcolumn %}
{% endcolumns %}
