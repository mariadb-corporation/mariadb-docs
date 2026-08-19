# MaxScale 23.08 Contents

## MaxScale 23.08 Contents

## Contents

### About MariaDB MaxScale

* [About MariaDB MaxScale](mariadb-maxscale-23-08-about/mariadb-maxscale-2308-about-mariadb-maxscale.md)
* [Changelog](https://mariadb.com/kb/en/mariadb-maxscale-2308-maxscale-2308-changelog/)
* [Limitations](mariadb-maxscale-23-08-about/mariadb-maxscale-2308-limitations-and-known-issues-within-mariadb-maxscale.md)

### Getting Started

* [MariaDB MaxScale Installation Guide](mariadb-maxscale-23-08-getting-started/mariadb-maxscale-2308-mariadb-maxscale-installation-guide.md)
* [Building MariaDB MaxScale from Source Code](mariadb-maxscale-23-08-getting-started/mariadb-maxscale-2308-building-mariadb-maxscale-from-source-code.md)
* [Configuration Guide](https://mariadb.com/kb/en/maxscale-2308-getting-started-mariadb-maxscale-configuration-guide/)
* [MaxGUI](mariadb-maxscale-23-08-getting-started/mariadb-maxscale-2308-mariadb-maxscale-maxgui-guide.md)

### Upgrading MariaDB MaxScale

* [Upgrading MaxScale](https://mariadb.com/kb/en/maxscale-23-08-upgrading-mariadb-maxscale/)

### Reference

* [MaxCtrl - Command Line Admin Interface](mariadb-maxscale-23-08-reference/mariadb-maxscale-2308-maxctrl.md)
* [MaxScale REST API](https://mariadb.com/kb/en/mariadb-maxscale-2308-maxscale-rest-api/)
* [Module Commands](mariadb-maxscale-23-08-reference/mariadb-maxscale-2308-module-commands.md)
* [Routing Hints](https://mariadb.com/kb/en/mariadb-maxscale-2308-maxscale-2308-hint-syntax/)

### Tutorials

The main tutorial for MariaDB MaxScale consist of setting up MariaDB MaxScale for the environment you are using with either a connection-based or a read/write-based configuration.

* [MariaDB MaxScale Tutorial](mariadb-maxscale-23-08-tutorials/mariadb-maxscale-2308-setting-up-mariadb-maxscale.md)

These tutorials are for specific use cases and module combinations.

* [Administration Tutorial](mariadb-maxscale-23-08-tutorials/mariadb-maxscale-2308-mariadb-maxscale-administration-tutorial.md)
* [Avro Router Tutorial](mariadb-maxscale-23-08-tutorials/mariadb-maxscale-2308-avrorouter-tutorial.md)
* [Connection Routing Tutorial](mariadb-maxscale-23-08-tutorials/mariadb-maxscale-2308-connection-routing-with-mariadb-maxscale.md)
* [Filter Tutorial](mariadb-maxscale-23-08-tutorials/mariadb-maxscale-2308-filters.md)
* [MariaDB Monitor Failover Tutorial](mariadb-maxscale-23-08-tutorials/mariadb-maxscale-2308-automatic-failover-with-mariadb-monitor.md)
* [Read Write Splitting Tutorial](mariadb-maxscale-23-08-tutorials/mariadb-maxscale-2308-read-write-splitting-with-mariadb-maxscale.md)
* [Simple Schema Sharding Tutorial](mariadb-maxscale-23-08-tutorials/mariadb-maxscale-2308-simple-sharding-with-two-servers.md)

Here are tutorials on monitoring and managing MariaDB MaxScale in cluster environments.

* [REST API Tutorial](mariadb-maxscale-23-08-tutorials/mariadb-maxscale-2308-rest-api-tutorial.md)

### Routers

The routing module is the core of a MariaDB MaxScale service. The router documentation
contains all module specific configuration options and detailed explanations
of their use.

* [Avrorouter](mariadb-maxscale-23-08-routers/mariadb-maxscale-2308-avrorouter.md)
* [Binlogrouter](mariadb-maxscale-23-08-routers/mariadb-maxscale-2308-binlogrouter.md)
* [Cat](mariadb-maxscale-23-08-routers/mariadb-maxscale-2308-cat.md)
* [KafkaCDC](mariadb-maxscale-23-08-routers/mariadb-maxscale-2308-kafkacdc.md)
* [KafkaImporter](mariadb-maxscale-23-08-routers/mariadb-maxscale-2308-kafkaimporter.md)
* [MirrorRouter](mariadb-maxscale-23-08-routers/mariadb-maxscale-2308-mirror.md)
* [Read Connection Router](mariadb-maxscale-23-08-routers/mariadb-maxscale-2308-readconnroute.md)
* [Read Write Split](mariadb-maxscale-23-08-routers/mariadb-maxscale-2308-readwritesplit.md)
* [Schemarouter](mariadb-maxscale-23-08-routers/mariadb-maxscale-2308-schemarouter.md)
* [SmartRouter](mariadb-maxscale-23-08-routers/mariadb-maxscale-2308-smartrouter.md)

### Filters

Here are detailed documents about the filters MariaDB MaxScale offers. They contain configuration guides and example use cases. Before reading these, you should have read the filter tutorial so that you know how they work and how to configure them.

* [Binlog Filter](mariadb-maxscale-23-08-filters/mariadb-maxscale-2308-binlog-filter.md)
* [Cache](mariadb-maxscale-23-08-filters/mariadb-maxscale-2308-cache.md)
* [Comment Filter](mariadb-maxscale-23-08-filters/mariadb-maxscale-2308-comment-filter.md)
* [Consistent Critical Read Filter](mariadb-maxscale-23-08-filters/mariadb-maxscale-2308-consistent-critical-read-filter.md)
* [Hint Filter](mariadb-maxscale-23-08-filters/mariadb-maxscale-2308-hintfilter.md)
* [LDIFilter](https://mariadb.com/kb/en/maxscale-23-08-ldi-filter/)
* [Masking Filter](mariadb-maxscale-23-08-filters/mariadb-maxscale-2308-masking.md)
* [Maxrows Filter](mariadb-maxscale-23-08-filters/mariadb-maxscale-2308-maxrows.md)
* [Named Server Filter](mariadb-maxscale-23-08-filters/mariadb-maxscale-2308-named-server-filter.md)
* [Query Log All](mariadb-maxscale-23-08-filters/mariadb-maxscale-2308-query-log-all-filter.md)
* [Regex Filter](mariadb-maxscale-23-08-filters/mariadb-maxscale-2308-regex-filter.md)
* [Rewrite Filter](mariadb-maxscale-23-08-filters/mariadb-maxscale-2308-rewrite-filter.md)
* [Tee Filter](mariadb-maxscale-23-08-filters/mariadb-maxscale-2308-tee-filter.md)
* [Throttle Filter](mariadb-maxscale-23-08-filters/mariadb-maxscale-2308-throttle.md)
* [Top N Filter](mariadb-maxscale-23-08-filters/mariadb-maxscale-2308-top-filter.md)

### Monitors

Common options for all monitor modules.

* [Monitor Common](mariadb-maxscale-23-08-monitors/mariadb-maxscale-2308-common-monitor-parameters.md)

Module specific documentation.

* [Galera Monitor](mariadb-maxscale-23-08-monitors/mariadb-maxscale-2308-galera-monitor.md)
* [MariaDB Monitor](mariadb-maxscale-23-08-monitors/mariadb-maxscale-2308-mariadb-monitor.md)

### Protocols

Documentation for MaxScale protocol modules.

* [MariaDB](https://mariadb.com/kb/en/maxscale-23-08-mariadb-protocol-module/)
* [Change Data Capture (CDC) Protocol](mariadb-maxscale-23-08-protocols/mariadb-maxscale-2308-change-data-capture-cdc-protocol.md)
* [Change Data Capture (CDC) Users](mariadb-maxscale-23-08-protocols/mariadb-maxscale-2308-change-data-capture-cdc-users.md)
* [NoSQL](mariadb-maxscale-23-08-protocols/mariadb-maxscale-2308-nosql-protocol-module.md)

The MaxScale CDC Connector provides a C++ API for consuming data from a CDC system.

* CDC Connector

### Authenticators

A short description of the authentication module type can be found in the [Authentication Modules](mariadb-maxscale-23-08-authenticators/mariadb-maxscale-2308-authentication-modules.md)
document.

* [MariaDB/MySQL Authenticator](https://mariadb.com/kb/en/mariadbmysql-authenticator/)
* [GSSAPI Authenticator](mariadb-maxscale-23-08-authenticators/mariadb-maxscale-2308-gssapi-client-authenticator.md)
* [PAM Authenticator](mariadb-maxscale-23-08-authenticators/mariadb-maxscale-2308-pam-authenticator.md)
* [Ed25519 Authenticator](mariadb-maxscale-23-08-authenticators/mariadb-maxscale-2308-ed25519-authenticator.md)

CC BY-SA / Gnu FDL

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
