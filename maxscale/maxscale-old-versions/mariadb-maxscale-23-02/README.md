---
description: >-
  MariaDB MaxScale 23.02 introduced MaxGUI, the browser-based administration
  and monitoring interface, along with other feature enhancements.
---

# MariaDB MaxScale 23.02

{% hint style="info" %}
MariaDB MaxScale 23.02 is a **bug-fix release**. It receives bug fixes until its end of life on **1 March 2027**, but no backported features. New functionality goes into the [current MaxScale release](../../README.md).
{% endhint %}

## About MariaDB MaxScale

| Page | Description |
| --- | --- |
| [About MariaDB MaxScale](mariadb-maxscale-23-02-about/mariadb-maxscale-2302-about-mariadb-maxscale.md) | MariaDB MaxScale is a database proxy that forwards database statements to one or more database servers. |
| [Changelog](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/maxscale/23.02/23.02-changelog) | Every change in each 23.02 point release, in the release notes. |
| [Limitations](mariadb-maxscale-23-02-about/mariadb-maxscale-2302-limitations-and-known-issues-within-mariadb-maxscale.md) | This document lists known issues and limitations in MariaDB MaxScale and its plugins. |

## Getting Started

| Page | Description |
| --- | --- |
| [MariaDB MaxScale Installation Guide](mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-installation-guide.md) | We recommend to install MaxScale on a separate server, to ensure that there can be no competition of resources between MaxScale and a MariaDB Server that it manages. |
| [Building MariaDB MaxScale from Source Code](mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-building-mariadb-maxscale-from-source-code.md) | MariaDB MaxScale can be built on any system that meets the requirements. |
| [Configuration Guide](mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md) | This document describes how to configure MariaDB MaxScale and presents some possible usage scenarios. |
| [MaxGUI](mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-maxgui-guide.md) | MaxGUI is a browser-based interface for MaxScale REST-API and query execution. |

## Upgrading MariaDB MaxScale

| Page | Description |
| --- | --- |
| [Upgrading MaxScale](mariadb-maxscale-23-02-upgrading/mariadb-maxscale-2302-maxscale-2302-upgrading-mariadb-maxscale.md) | For more information about what has changed, please refer to the ChangeLog and to the release notes. |

## Reference

| Page | Description |
| --- | --- |
| [MaxCtrl - Command Line Admin Interface](mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl.md) | MaxCtrl is a command line administrative client for MaxScale which uses the MaxScale REST API for communication. |
| [MaxScale REST API](mariadb-maxscale-23-02-rest-api/mariadb-maxscale-2302-rest-api.md) | Version 1 of the MaxScale REST API: resources, endpoints, and response formats. |
| [Module Commands](mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-module-commands.md) | Introduced in MaxScale 2.1, the module commands are special, module-specific commands. |
| [Routing Hints](mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-hint-syntax.md) | Routing individual queries with hints. The syntax itself is documented with the Hintfilter. |

## Tutorials

The main tutorial for MariaDB MaxScale consist of setting up MariaDB MaxScale for the environment you are using with either a connection-based or a read/write-based configuration.

| Page | Description |
| --- | --- |
| [MariaDB MaxScale Tutorial](mariadb-maxscale-23-02-tutorials/mariadb-maxscale-2302-setting-up-mariadb-maxscale.md) | This document is designed as a quick introduction to setting up MariaDB MaxScale. |

These tutorials are for specific use cases and module combinations.

| Page | Description |
| --- | --- |
| [Administration Tutorial](mariadb-maxscale-23-02-tutorials/mariadb-maxscale-2302-mariadb-maxscale-administration-tutorial.md) | The purpose of this tutorial is to introduce the MariaDB MaxScale Administrator to a few of the common administration tasks. |
| [Avro Router Tutorial](mariadb-maxscale-23-02-tutorials/mariadb-maxscale-2302-avrorouter-tutorial.md) | This tutorial is a short introduction to the Avrorouter, how to set it up and how it interacts with the binlogrouter. |
| [Connection Routing Tutorial](mariadb-maxscale-23-02-tutorials/mariadb-maxscale-2302-connection-routing-with-mariadb-maxscale.md) | The goal of this tutorial is to configure a system that has two ports available, one for write connections and another for read connections. |
| [Filter Tutorial](mariadb-maxscale-23-02-tutorials/mariadb-maxscale-2302-filters.md) | The filter mechanism in MariaDB MaxScale is a means by which processing can be inserted into the flow of requests and responses between the client connection to MariaDB… |
| [MariaDB Monitor Failover Tutorial](mariadb-maxscale-23-02-tutorials/mariadb-maxscale-2302-automatic-failover-with-mariadb-monitor.md) | The MariaDB Monitor is not only capable of monitoring the state of a MariaDB primary-replica cluster but is also capable of performing failover and switchover. |
| [Read Write Splitting Tutorial](mariadb-maxscale-23-02-tutorials/mariadb-maxscale-2302-read-write-splitting-with-mariadb-maxscale.md) | The goal of this tutorial is to configure a system that appears to the client as a single database. |
| [Simple Schema Sharding Tutorial](mariadb-maxscale-23-02-tutorials/mariadb-maxscale-2302-simple-sharding-with-two-servers.md) | A client connects through MariaDB MaxScale, which shards queries between two backend servers holding different schemas. |

Here are tutorials on monitoring and managing MariaDB MaxScale in cluster environments.

| Page | Description |
| --- | --- |
| [REST API Tutorial](mariadb-maxscale-23-02-tutorials/mariadb-maxscale-2302-rest-api-tutorial.md) | This tutorial is a quick overview of what the MaxScale REST API offers, how it can be used to inspect the state of MaxScale and how to use it to modify the runtime… |

## Routers

The routing module is the core of a MariaDB MaxScale service. The router documentation contains all module specific configuration options and detailed explanations of their use.

| Page | Description |
| --- | --- |
| [Avrorouter](mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-avrorouter.md) | The avrorouter is a MariaDB 10.0 binary log to Avro file converter. |
| [Binlogrouter](mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-binlogrouter.md) | The binlogrouter is a router that acts as a replication proxy for MariaDB primary-replica replication. |
| [Cat](mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-cat.md) | The cat router is a special router that concatenates result sets. |
| [KafkaCDC](mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-kafkacdc.md) | The KafkaCDC module reads data changes in MariaDB via replication and converts them into JSON objects that are then streamed to a Kafka broker. |

* KafkaImporter

| Page | Description |
| --- | --- |
| [MirrorRouter](mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-mirror.md) | The mirror router is designed for data consistency and database behavior verification during system upgrades. |
| [Read Connection Router](mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-readconnroute.md) | This document provides an overview of the readconnroute router module and its intended use case scenarios. |
| [Read Write Split](mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-readwritesplit.md) | This document provides a short overview of the readwritesplit router module and its intended use case scenarios. |
| [Schemarouter](mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-schemarouter.md) | The SchemaRouter provides an easy and manageable sharding solution by building a single logical database server from multiple separate ones. |
| [SmartRouter](mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-smartrouter.md) | SmartRouter is the query router of the SmartQuery framework. |

## Filters

Here are detailed documents about the filters MariaDB MaxScale offers. They contain configuration guides and example use cases. Before reading these, you should have read the filter tutorial so that you know how they work and how to configure them.

| Page | Description |
| --- | --- |
| [Binlog Filter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-binlog-filter.md) | This filter was introduced in MariaDB MaxScale 2.3.0. |
| [Cache](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-cache.md) | This filter was introduced in MariaDB MaxScale 2.1. |
| [Comment Filter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-comment-filter.md) | With the comment filter it is possible to define comments that are injected before the actual statements. |
| [Consistent Critical Read Filter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-consistent-critical-read-filter.md) | This filter was introduced in MariaDB MaxScale 2.1. |
| [Hint Filter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-hintfilter.md) | This filter adds routing hints to a service. |
| [Luafilter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-lua-filter.md) | The luafilter is a filter that calls a set of functions in a Lua script. |
| [Masking Filter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-masking.md) | This filter was introduced in MariaDB MaxScale 2.1. |
| [Maxrows Filter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-maxrows.md) | This filter was introduced in MariaDB MaxScale 2.1. |
| [Named Server Filter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-named-server-filter.md) | The namedserverfilter is a MariaDB MaxScale filter module able to route queries to servers based on regular expression (regex) matches. |
| [Query Log All](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-query-log-all-filter.md) | The Query Log All (QLA) filter logs query content. |
| [Regex Filter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-regex-filter.md) | The Regex filter is a filter module for MariaDB MaxScale that is able to rewrite query content using regular expression matches and text substitution. |
| [Rewrite Filter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-rewrite-filter.md) | The rewrite filter allows modification of sql queries on the fly. |
| [Tee Filter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-tee-filter.md) | The tee filter is a "plumbing" fitting in the MariaDB MaxScale filter toolkit. |
| [Throttle Filter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-throttle.md) | This filter was added in MariaDB MaxScale 2.3 |
| [Top N Filter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-top-filter.md) | The top filter is a filter module for MariaDB MaxScale that monitors every SQL statement that passes through the filter. |
| [Transaction Performance Monitoring Filter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-transaction-performance-monitoring-filter.md) | Note: This module is experimental and must be built from source. |

## Monitors

Common options for all monitor modules.

| Page | Description |
| --- | --- |
| [Monitor Common](mariadb-maxscale-23-02-monitors/mariadb-maxscale-2302-common-monitor-parameters.md) | The settings supported by every monitor module. |

Module specific documentation.

| Page | Description |
| --- | --- |
| [Galera Monitor](mariadb-maxscale-23-02-monitors/mariadb-maxscale-2302-galera-monitor.md) | The Galera Monitor is a monitoring module for MaxScale that monitors a Galera cluster. |
| [MariaDB Monitor](mariadb-maxscale-23-02-monitors/mariadb-maxscale-2302-mariadb-monitor.md) | MariaDB Monitor monitors a Primary-Replica replication cluster. |

## Protocols

Documentation for MaxScale protocol modules.

| Page | Description |
| --- | --- |
| [MariaDB](mariadb-maxscale-23-02-protocols/mariadb-maxscale-2302-maxscale-2302-mariadb-protocol-module.md) | The mariadbprotocol module implements the MariaDB client-server protocol. |
| [Change Data Capture (CDC) Protocol](mariadb-maxscale-23-02-protocols/mariadb-maxscale-2302-change-data-capture-cdc-protocol.md) | CDC is a new protocol that allows compatible clients to authenticate and register for Change Data Capture events. |
| [Change Data Capture (CDC) Users](mariadb-maxscale-23-02-protocols/mariadb-maxscale-2302-change-data-capture-cdc-users.md) | Change Data Capture (CDC) is a new MaxScale protocol that allows compatible clients to authenticate and register for Change Data Capture events. |
| [NoSQL](mariadb-maxscale-23-02-protocols/mariadb-maxscale-2302-nosql-protocol-module.md) | The nosqlprotocol module allows a MariaDB server or cluster to be used as the backend of an application using a MongoDB® client library. |

The MaxScale CDC Connector provides a C++ API for consuming data from a CDC system.

| Page | Description |
| --- | --- |
| [CDC Connector](mariadb-maxscale-23-02-connectors/mariadb-maxscale-2302-maxscale-cdc-connector.md) | The C++ connector for the MariaDB MaxScale CDC system. |

## Authenticators

A short description of the authentication module type can be found in the Authentication Modules document.

| Page | Description |
| --- | --- |
| [MariaDB/MySQL Authenticator](mariadb-maxscale-23-02-authenticators/mariadb-maxscale-2302-mysql-authenticator.md) | The MariaDBAuth-module implements the client and backend authentication for the server plugin mysqlnativepassword. |
| [GSSAPI Authenticator](mariadb-maxscale-23-02-authenticators/mariadb-maxscale-2302-gssapi-client-authenticator.md) | GSSAPI is an authentication protocol that is commonly implemented with Kerberos on Unix or Active Directory on Windows. |
| [PAM Authenticator](mariadb-maxscale-23-02-authenticators/mariadb-maxscale-2302-pam-authenticator.md) | Pluggable authentication module (PAM) is a general purpose authentication API. |
| [Ed25519 Authenticator](mariadb-maxscale-23-02-authenticators/mariadb-maxscale-2302-ed25519-authenticator.md) | Ed25519 is a highly secure authentication method based on public key cryptography. |

## Design Documents

| Page | Description |
| --- | --- |
| [Plugin development guide](mariadb-maxscale-23-02-design-documents/mariadb-maxscale-2302-mariadb-maxscale-plugin-development-guide.md) | This document and the attached example code explain prospective plugin developers the MariaDB MaxScale plugin API and also present and explain some best practices and… |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
