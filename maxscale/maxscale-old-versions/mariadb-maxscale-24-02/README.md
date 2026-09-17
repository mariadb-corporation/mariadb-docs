---
description: >-
  MariaDB MaxScale 24.02 added binlog compression, tightened REST API
  security, and improved the MaxGUI interface.
---

# MariaDB MaxScale 24.02

{% hint style="info" %}
MariaDB MaxScale 24.02 is a **bug-fix release**. It receives bug fixes until its end of life on **1 March 2028**, but no backported features. New functionality goes into the [current MaxScale release](../../README.md).
{% endhint %}

## About MariaDB MaxScale

| Page | Description |
| --- | --- |
| [About MariaDB MaxScale](maxscale-24-02about/mariadb-maxscale-2402-maxscale-2402-about-mariadb-maxscale.md) | MariaDB MaxScale is a database proxy that forwards database statements to one or more database servers. |
| [Changelog](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/maxscale/24.02/24.02-changelog) | Every change in each 24.02 point release, in the release notes. |
| [Limitations](maxscale-24-02about/mariadb-maxscale-2402-maxscale-2402-limitations-and-known-issues-within-mariadb-maxscale.md) | This document lists known issues and limitations in MariaDB MaxScale and its plugins. |

## Getting Started

| Page | Description |
| --- | --- |
| [MariaDB MaxScale Installation Guide](maxscale-24-02getting-started/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-installation-guide.md) | We recommend to install MaxScale on a separate server, to ensure that there can be no competition of resources between MaxScale and a MariaDB Server that it manages. |
| [Building MariaDB MaxScale from Source Code](maxscale-24-02getting-started/mariadb-maxscale-2402-maxscale-2402-building-mariadb-maxscale-from-source-code.md) | MariaDB MaxScale can be built on any system that meets the requirements. |
| [Configuration Guide](maxscale-24-02getting-started/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-configuration-guide.md) | This document describes how to configure MariaDB MaxScale and presents some possible usage scenarios. |
| [MaxGUI](maxscale-24-02getting-started/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-maxgui-guide.md) | MaxGUI is a browser-based interface for MaxScale REST-API and query execution. |

## Upgrading MariaDB MaxScale

| Page | Description |
| --- | --- |
| [Upgrading MaxScale](maxscale-24-02upgrading/README.md) | Before upgrading to MariaDB MaxScale 24.02, it's critical to review the changes. This guide outlines new features, altered parameters, and deprecated functionality to… |

## Reference

| Page | Description |
| --- | --- |
| [MaxCtrl - Command Line Admin Interface](maxscale-24-02reference/mariadb-maxscale-2402-maxscale-2402-maxctrl.md) | MaxCtrl is a command line administrative client for MaxScale which uses the MaxScale REST API for communication. |
| [MaxScale REST API](maxscale-24-02rest-api/mariadb-maxscale-2402-maxscale-2402-rest-api.md) | Version 1 of the MaxScale REST API: resources, endpoints, and response formats. |
| [Module Commands](maxscale-24-02reference/mariadb-maxscale-2402-maxscale-2402-module-commands.md) | Introduced in MaxScale 2.1, the module commands are special, module-specific commands. |
| [Routing Hints](maxscale-24-02reference/mariadb-maxscale-2402-maxscale-2402-hint-syntax.md) | Routing individual queries with hints. The syntax itself is documented with the Hintfilter. |

## Tutorials

The main tutorial for MariaDB MaxScale consist of setting up MariaDB MaxScale for the environment you are using with either a connection-based or a read/write-based configuration.

| Page | Description |
| --- | --- |
| [MariaDB MaxScale Tutorial](maxscale-24-02tutorials/mariadb-maxscale-2402-maxscale-2402-setting-up-mariadb-maxscale.md) | This document is designed as a quick introduction to setting up MariaDB MaxScale. |

These tutorials are for specific use cases and module combinations.

| Page | Description |
| --- | --- |
| [Administration Tutorial](maxscale-24-02tutorials/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-administration-tutorial.md) | The purpose of this tutorial is to introduce the MariaDB MaxScale Administrator to a few of the common administration tasks. |
| [Avro Router Tutorial](maxscale-24-02tutorials/mariadb-maxscale-2402-maxscale-2402-avrorouter-tutorial.md) | This tutorial is a short introduction to the Avrorouter, how to set it up and how it interacts with the binlogrouter. |
| [Connection Routing Tutorial](maxscale-24-02tutorials/mariadb-maxscale-2402-maxscale-2402-connection-routing-with-mariadb-maxscale.md) | The goal of this tutorial is to configure a system that has two ports available, one for write connections and another for read connections. |
| [Filter Tutorial](maxscale-24-02tutorials/mariadb-maxscale-2402-maxscale-2402-filters.md) | The filter mechanism in MariaDB MaxScale is a means by which processing can be inserted into the flow of requests and responses between the client connection to MariaDB… |
| [MariaDB Monitor Failover Tutorial](maxscale-24-02tutorials/mariadb-maxscale-2402-maxscale-2402-automatic-failover-with-mariadb-monitor.md) | The MariaDB Monitor is not only capable of monitoring the state of a MariaDB primary-replica cluster but is also capable of performing failover and switchover. |
| [Read Write Splitting Tutorial](maxscale-24-02tutorials/mariadb-maxscale-2402-maxscale-2402-read-write-splitting-with-mariadb-maxscale.md) | The goal of this tutorial is to configure a system that appears to the client as a single database. |
| [Simple Schema Sharding Tutorial](maxscale-24-02tutorials/mariadb-maxscale-2402-maxscale-2402-simple-sharding-with-two-servers.md) | Sharding is the method of splitting a single logical database server into separate physical databases. |

Here are tutorials on monitoring and managing MariaDB MaxScale in cluster environments.

| Page | Description |
| --- | --- |
| [REST API Tutorial](maxscale-24-02tutorials/mariadb-maxscale-2402-maxscale-2402-rest-api-tutorial.md) | This tutorial is a quick overview of what the MaxScale REST API offers, how it can be used to inspect the state of MaxScale and how to use it to modify the runtime… |

## Routers

The routing module is the core of a MariaDB MaxScale service. The router documentation contains all module specific configuration options and detailed explanations of their use.

| Page | Description |
| --- | --- |
| [Avrorouter](maxscale-24-02routers/mariadb-maxscale-2402-maxscale-2402-avrorouter.md) | The avrorouter is a MariaDB 10.0 binary log to Avro file converter. |
| [Binlogrouter](maxscale-24-02routers/mariadb-maxscale-2402-maxscale-2402-binlogrouter.md) | The binlogrouter is a router that acts as a replication proxy for MariaDB primary-replica replication. |
| [Cat](maxscale-24-02routers/mariadb-maxscale-2402-maxscale-2402-cat.md) | The cat router is a special router that concatenates result sets. |
| [KafkaCDC](maxscale-24-02routers/mariadb-maxscale-2402-maxscale-2402-kafkacdc.md) | The KafkaCDC module reads data changes in MariaDB via replication and converts them into JSON objects that are then streamed to a Kafka broker. |
| [KafkaImporter](maxscale-24-02routers/mariadb-maxscale-2402-maxscale-2402-kafkaimporter.md) | The KafkaImporter module reads messages from Kafka and streams them into a MariaDB server. |
| [MirrorRouter](maxscale-24-02routers/mariadb-maxscale-2402-maxscale-2402-mirror.md) | The mirror router is designed for data consistency and database behavior verification during system upgrades. |
| [Read Connection Router](maxscale-24-02routers/mariadb-maxscale-2402-maxscale-2402-readconnroute.md) | This document provides an overview of the readconnroute router module and its intended use case scenarios. |
| [Read Write Split](maxscale-24-02routers/mariadb-maxscale-2402-maxscale-2402-readwritesplit.md) | This document provides a short overview of the readwritesplit router module and its intended use case scenarios. |
| [Schemarouter](maxscale-24-02routers/mariadb-maxscale-2402-maxscale-2402-schemarouter.md) | The SchemaRouter provides an easy and manageable sharding solution by building a single logical database server from multiple separate ones. |
| [SmartRouter](maxscale-24-02routers/mariadb-maxscale-2402-maxscale-2402-smartrouter.md) | SmartRouter is the query router of the SmartQuery framework. |

The following routers are only available in MaxScale Enterprise.

* Diff

## Filters

Here are detailed documents about the filters MariaDB MaxScale offers. They contain configuration guides and example use cases. Before reading these, you should have read the filter tutorial so that you know how they work and how to configure them.

| Page | Description |
| --- | --- |
| [Binlog Filter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-binlog-filter.md) | This filter was introduced in MariaDB MaxScale 2.3.0. |
| [Cache](maxscale-24-02filters/mariadb-maxscale-2402-cache.md) | This filter was introduced in MariaDB MaxScale 2.1. |
| [Comment Filter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-comment-filter.md) | With the comment filter it is possible to define comments that are injected before the actual statements. |
| [Consistent Critical Read Filter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-consistent-critical-read-filter.md) | This filter was introduced in MariaDB MaxScale 2.1. |
| [Hint Filter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-hintfilter.md) | This filter adds routing hints to a service. |
| [LDIFilter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-ldi-filter.md) | The ldi (LOAD DATA INFILE) filter was introduced in MaxScale 23.08.0 and it extends the MariaDB LOAD DATA INFILE syntax to support loading data from any object storage… |
| [Luafilter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-lua-filter.md) | The luafilter is a filter that calls a set of functions in a Lua script. |
| [Masking Filter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-masking.md) | This filter was introduced in MariaDB MaxScale 2.1. |
| [Maxrows Filter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-maxrows.md) | This filter was introduced in MariaDB MaxScale 2.1. |
| [Named Server Filter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-named-server-filter.md) | The namedserverfilter is a MariaDB MaxScale filter module able to route queries to servers based on regular expression (regex) matches. |
| [Query Log All](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-query-log-all-filter.md) | The Query Log All (QLA) filter logs query content. |
| [Regex Filter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-regex-filter.md) | The Regex filter is a filter module for MariaDB MaxScale that is able to rewrite query content using regular expression matches and text substitution. |
| [Rewrite Filter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-rewrite-filter.md) | The rewrite filter allows modification of sql queries on the fly. |
| [Tee Filter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-tee-filter.md) | The tee filter is a "plumbing" fitting in the MariaDB MaxScale filter toolkit. |
| [Throttle Filter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-throttle.md) | This filter was added in MariaDB MaxScale 2.3 |
| [Top N Filter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-top-filter.md) | The top filter is a filter module for MariaDB MaxScale that monitors every SQL statement that passes through the filter. |
| [Transaction Performance Monitoring Filter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-transaction-performance-monitoring-filter.md) | Note: This module is experimental and must be built from source. |

The following filters are only available in MaxScale Enterprise.

* Wcar

## Monitors

Common options for all monitor modules.

| Page | Description |
| --- | --- |
| [Monitor Common](maxscale-24-02monitors/mariadb-maxscale-2402-maxscale-2402-common-monitor-parameters.md) | The settings supported by every monitor module. |

Module specific documentation.

| Page | Description |
| --- | --- |
| [Galera Monitor](maxscale-24-02monitors/mariadb-maxscale-2402-maxscale-2402-galera-monitor.md) | The Galera Monitor is a monitoring module for MaxScale that monitors a Galera cluster. |
| [MariaDB Monitor](maxscale-24-02monitors/mariadb-maxscale-2402-maxscale-2402-mariadb-monitor.md) | MariaDB Monitor monitors a Primary-Replica replication cluster. |

## Protocols

Documentation for MaxScale protocol modules.

| Page | Description |
| --- | --- |
| [MariaDB](maxscale-24-02protocols/mariadb-maxscale-2402-maxscale-2402-mariadb-protocol-module.md) | The mariadbprotocol module implements the MariaDB client-server protocol. |
| [Change Data Capture (CDC) Protocol](maxscale-24-02protocols/mariadb-maxscale-2402-maxscale-2402-change-data-capture-cdc-protocol.md) | CDC is a new protocol that allows compatible clients to authenticate and register for Change Data Capture events. |
| [Change Data Capture (CDC) Users](maxscale-24-02protocols/mariadb-maxscale-2402-maxscale-2402-change-data-capture-cdc-users.md) | Change Data Capture (CDC) is a new MaxScale protocol that allows compatible clients to authenticate and register for Change Data Capture events. |
| [NoSQL](maxscale-24-02protocols/mariadb-maxscale-2402-maxscale-2402-nosql-protocol-module.md) | The nosqlprotocol module allows a MariaDB server or cluster to be used as the backend of an application using a MongoDB® client library. |

The MaxScale CDC Connector provides a C++ API for consuming data from a CDC system.

| Page | Description |
| --- | --- |
| [CDC Connector](maxscale-24-02connectors/mariadb-maxscale-2402-maxscale-2402-maxscale-cdc-connector.md) | The C++ connector for the MariaDB MaxScale CDC system. |

## Authenticators

A short description of the authentication module type can be found in the Authentication Modules document.

| Page | Description |
| --- | --- |
| [MariaDB/MySQL Authenticator](maxscale-24-02authenticators/mariadb-maxscale-2402-maxscale-2402-mariadbmysql-authenticator.md) | The MariaDBAuth-module implements the client and backend authentication for the server plugin mysqlnativepassword. |
| [GSSAPI Authenticator](maxscale-24-02authenticators/mariadb-maxscale-2402-maxscale-2402-gssapi-client-authenticator.md) | GSSAPI is an authentication protocol that is commonly implemented with Kerberos on Unix or Active Directory on Windows. |
| [PAM Authenticator](maxscale-24-02authenticators/mariadb-maxscale-2402-maxscale-2402-pam-authenticator.md) | Pluggable authentication module (PAM) is a general purpose authentication API. |
| [Ed25519 Authenticator](../mariadb-maxscale-23-02/mariadb-maxscale-23-02-authenticators/mariadb-maxscale-2302-ed25519-authenticator.md) | Ed25519 is a highly secure authentication method based on public key cryptography. |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
