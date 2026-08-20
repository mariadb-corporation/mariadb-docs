---
description: >-
  MariaDB MaxScale 25.01 introduced Workload Capture and Replay for
  production traffic analysis and the Diff Router for comparing server
  behavior.
---

# MariaDB MaxScale 25.01

{% hint style="info" %}
MariaDB MaxScale 25.01 is a **bug-fix release**. It receives bug fixes until its end of life on **16 January 2033**, but no backported features. New functionality goes into the [current MaxScale release](../../README.md).
{% endhint %}

## About MariaDB MaxScale

| Page | Description |
| --- | --- |
| [About MariaDB MaxScale](maxscale-25-01-about.md) | What MariaDB MaxScale is and what it does. |
| [Changelog](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/maxscale/25.01/25.01-changelog) | Every change in each 25.01 point release, in the release notes. |
| [Limitations](../../maxscale-management/mariadb-maxscale-limitations-guide.md) | Review the current constraints of MariaDB MaxScale. This document lists known issues regarding transaction parsing, protocol support, and specific module limitations. |

## Getting Started

| Page | Description |
| --- | --- |
| [MariaDB MaxScale Installation Guide](mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-installation-guide.md) | We recommend to install MaxScale on a separate server, to ensure that there can be no competition of resources between MaxScale and a MariaDB Server that it manages. |
| [Building MariaDB MaxScale from Source Code](mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-building-mariadb-maxscale-from-source-code.md) | MariaDB MaxScale can be built on any system that meets the requirements. |
| [Configuration Guide](mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md) | This document describes how to configure MariaDB MaxScale and presents some possible usage scenarios. |
| [MaxGUI](mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-maxgui-guide.md) | MaxGUI is a browser-based interface for MaxScale REST-API and query execution. |

## Upgrading MariaDB MaxScale

| Page | Description |
| --- | --- |
| [Upgrading MaxScale](../../maxscale-management/deployment/upgrading-maxscale/upgrade-to-maxscale-25.01.md) | Follow the specific steps to upgrade MariaDB MaxScale to version 25.01. This guide covers new package structures, removed features, and critical configuration changes… |

## Reference

| Page | Description |
| --- | --- |
| [Hardening](mariadb-maxscale-25-01-reference/mariadb-maxscale-2501-maxscale-2501-securing-your-maxscale-deployment.md) | The five components to complete before running MaxScale in production. |
| [MaxCtrl - Command Line Admin Interface](mariadb-maxscale-25-01-reference/mariadb-maxscale-2501-maxscale-2501-maxctrl.md) | MaxCtrl is a command line administrative client for MaxScale which uses the MaxScale REST API for communication. |
| [MaxScale REST API](mariadb-maxscale-25-01-rest-api/mariadb-maxscale-2501-maxscale-2501-rest-api.md) | Version 1 of the MaxScale REST API: resources, endpoints, and response formats. |
| [Module Commands](mariadb-maxscale-25-01-reference/mariadb-maxscale-2501-maxscale-2501-module-commands.md) | Introduced in MaxScale 2.1, the module commands are special, module-specific commands. |
| [Routing Hints](mariadb-maxscale-25-01-reference/mariadb-maxscale-2501-maxscale-2501-hint-syntax.md) | Routing individual queries with hints. The syntax itself is documented with the Hintfilter. |
| [Settings](mariadb-maxscale-25-01-reference/mariadb-maxscale-2501-maxscale-2501-configuration-settings.md) | Every MaxScale configuration setting, global and per-object. |

## Tutorials

The main tutorial for MariaDB MaxScale consist of setting up MariaDB MaxScale for the environment you are using with either a connection-based or a read/write-based configuration.

| Page | Description |
| --- | --- |
| [MariaDB MaxScale Tutorial](mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-setting-up-mariadb-maxscale.md) | This document is designed as a quick introduction to setting up MariaDB MaxScale. |

These tutorials are for specific use cases and module combinations.

| Page | Description |
| --- | --- |
| [Administration Tutorial](mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-administration-tutorial.md) | The purpose of this tutorial is to introduce the MariaDB MaxScale Administrator to a few of the common administration tasks. |
| [Avro Router Tutorial](mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-avrorouter-tutorial.md) | This tutorial is a short introduction to the Avrorouter, how to set it up and how it interacts with the binlogrouter. |
| [Connection Routing Tutorial](mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-connection-routing-with-mariadb-maxscale.md) | The goal of this tutorial is to configure a system that has two ports available, one for write connections and another for read connections. |
| [Filter Tutorial](mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-filters.md) | The filter mechanism in MariaDB MaxScale is a means by which processing can be inserted into the flow of requests and responses between the client connection to MariaDB… |
| [MariaDB Monitor Failover Tutorial](mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-automatic-failover-with-mariadb-monitor.md) | The MariaDB Monitor is not only capable of monitoring the state of a MariaDB primary-replica cluster but is also capable of performing failover and switchover. |
| [Read Write Splitting Tutorial](mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-read-write-splitting-with-mariadb-maxscale.md) | The goal of this tutorial is to configure a system that appears to the client as a single database. |
| [Simple Schema Sharding Tutorial](mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-schemarouter-simple-sharding-with-two-servers.md) | Sharding is the method of splitting a single logical database server into separate physical databases. |

Here are tutorials on monitoring and managing MariaDB MaxScale in cluster environments.

| Page | Description |
| --- | --- |
| [REST API Tutorial](mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-rest-api-tutorial.md) | This tutorial is a quick overview of what the MaxScale REST API offers, how it can be used to inspect the state of MaxScale and how to use it to modify the runtime… |

## Routers

The routing module is the core of a MariaDB MaxScale service. The router documentation contains all module specific configuration options and detailed explanations of their use.

| Page | Description |
| --- | --- |
| [Avrorouter](mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md) | The Avrorouter was deprecated in MaxScale 25.01 and will be removed in the next major release. |
| [Binlogrouter](mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md) | The binlogrouter is a router that acts as a replication proxy for MariaDB primary-replica replication. |
| [Cat](mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-cat.md) | The cat router is a special router that concatenates result sets. |
| [Diff](mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md) | The diff-router, hereafter referred to as Diff, compares the behaviour of one MariaDB server version to that of another. |
| [KafkaCDC](mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md) | The KafkaCDC module reads data changes in MariaDB via replication and converts them into JSON objects that are then streamed to a Kafka broker. |
| [KafkaImporter](mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md) | The KafkaImporter module reads messages from Kafka and streams them into a MariaDB server. |
| [MirrorRouter](mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-mirror.md) | The mirror router is designed for data consistency and database behavior verification during system upgrades. |
| [Read Connection Router](mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readconnroute.md) | This document provides an overview of the readconnroute router module and its intended use case scenarios. |
| [Read Write Split](mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md) | This document provides a short overview of the readwritesplit router module and its intended use case scenarios. |
| [Schemarouter](mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-schemarouter.md) | The SchemaRouter provides an easy and manageable sharding solution by building a single logical database server from multiple separate ones. |
| [SmartRouter](mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-smartrouter.md) | SmartRouter is the query router of the SmartQuery framework. |

## Filters

Here are detailed documents about the filters MariaDB MaxScale offers. They contain configuration guides and example use cases. Before reading these, you should have read the filter tutorial so that you know how they work and how to configure them.

| Page | Description |
| --- | --- |
| [Binlog Filter](mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-binlog-filter.md) | This filter was introduced in MariaDB MaxScale 2.3.0. |
| [Cache](mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md) | This filter was introduced in MariaDB MaxScale 2.1. |
| [Comment Filter](mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-comment-filter.md) | With the comment filter it is possible to define comments that are injected before the actual statements. |
| [Consistent Critical Read Filter](mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md) | This filter was introduced in MariaDB MaxScale 2.1. |
| [Hint Filter](mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-hintfilter.md) | This filter adds routing hints to a service. |
| [LDIFilter](mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md) | The ldi (LOAD DATA INFILE) filter was introduced in MaxScale 23.08.0 and it extends the MariaDB LOAD DATA INFILE syntax to support loading data from any object storage… |
| [Luafilter](mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-lua-filter.md) | The luafilter is a filter that calls a set of functions in a Lua script. |
| [Masking Filter](mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md) | This filter was introduced in MariaDB MaxScale 2.1. |
| [Maxrows Filter](mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-maxrows.md) | This filter was introduced in MariaDB MaxScale 2.1. |
| [Named Server Filter](mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-named-server-filter.md) | The namedserverfilter is a MariaDB MaxScale filter module able to route queries to servers based on regular expression (regex) matches. |
| [Prepared Statement Reuse Filter](mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-psreuse.md) | The psreuse filter reuses identical prepared statements inside the same client connection. |
| [Optimistic Transaction Execution Filter](mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-optimistic-transaction-execution-filter.md) | The optimistictrx filter implements optimistic transaction execution. |
| [Query Log All](mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md) | The Query Log All (QLA) filter logs query content. |
| [Regex Filter](mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-regex-filter.md) | The Regex filter is a filter module for MariaDB MaxScale that is able to rewrite query content using regular expression matches and text substitution. |
| [Rewrite Filter](mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md) | The rewrite filter allows modification of sql queries on the fly. |
| [Tee Filter](mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md) | The tee filter is a "plumbing" fitting in the MariaDB MaxScale filter toolkit. |
| [Throttle Filter](mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-throttle.md) | This filter was added in MariaDB MaxScale 2.3 |
| [Top N Filter](mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-top-filter.md) | The top filter is a filter module for MariaDB MaxScale that monitors every SQL statement that passes through the filter. |
| [Transaction Performance Monitoring Filter](mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-transaction-performance-monitoring-filter.md) | Note: This module is experimental and must be built from source. |
| [Wcar](mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-workload-capture-and-replay.md) | The WCAR (Write Consistent Archive and Replay) module is a sophisticated feature designed to capture and archive client traffic passing through a MaxScale instance. |

## Monitors

Common options for all monitor modules.

| Page | Description |
| --- | --- |
| [Monitor Common](mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md) | The settings supported by every monitor module. |

Module specific documentation.

| Page | Description |
| --- | --- |
| [Galera Monitor](mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-galera-monitor.md) | The Galera Monitor is a monitoring module for MaxScale that monitors a Galera cluster. |
| [MariaDB Monitor](mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md) | MariaDB Monitor monitors a Primary-Replica replication cluster. |

## Protocols

Documentation for MaxScale protocol modules.

| Page | Description |
| --- | --- |
| [MariaDB](mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-mariadb-protocol-module.md) | The mariadbprotocol module implements the MariaDB client-server protocol. |
| [Change Data Capture (CDC) Protocol](mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-change-data-capture-cdc-protocol.md) | The CDC protocol was deprecated in MaxScale 24.08 and will be removed in the next major release. |
| [Change Data Capture (CDC) Users](mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-change-data-capture-cdc-users.md) | Change Data Capture (CDC) is a new MaxScale protocol that allows compatible clients to authenticate and register for Change Data Capture events. |
| [NoSQL](mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md) | The nosqlprotocol module allows a MariaDB server or cluster to be used as the backend of an application using a MongoDB® client library. |

The MaxScale CDC Connector provides a C++ API for consuming data from a CDC system.

| Page | Description |
| --- | --- |
| [CDC Connector](mariadb-maxscale-25-01-connectors/mariadb-maxscale-2501-maxscale-2501-maxscale-cdc-connector.md) | The C++ connector for the MariaDB MaxScale CDC system. |

## Authenticators

A short description of the authentication module type can be found in the Authentication Modules document.

| Page | Description |
| --- | --- |
| [MariaDB/MySQL Authenticator](mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-mariadbmysql-authenticator.md) | The MariaDBAuth-module implements the client and backend authentication for the server plugin mysqlnativepassword. |
| [GSSAPI Authenticator](mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-gssapi-client-authenticator.md) | GSSAPI is an authentication protocol that is commonly implemented with Kerberos on Unix or Active Directory on Windows. |
| [PAM Authenticator](mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-pam-authenticator.md) | Pluggable authentication module (PAM) is a general purpose authentication API. |
| [Ed25519 Authenticator](mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-ed25519-authenticator.md) | Ed25519 is a highly secure authentication method based on public key cryptography. |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
