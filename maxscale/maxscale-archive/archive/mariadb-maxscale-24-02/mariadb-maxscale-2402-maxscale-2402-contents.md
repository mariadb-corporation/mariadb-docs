# MaxScale 24.02 Contents

### About MariaDB MaxScale

* [About MariaDB MaxScale](maxscale-24-02about/mariadb-maxscale-2402-maxscale-2402-about-mariadb-maxscale.md)
* [Changelog](broken-reference/)
* [Limitations](maxscale-24-02about/mariadb-maxscale-2402-maxscale-2402-limitations-and-known-issues-within-mariadb-maxscale.md)

### Getting Started

* [MariaDB MaxScale Installation Guide](maxscale-24-02getting-started/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-installation-guide.md)
* [Building MariaDB MaxScale from Source Code](maxscale-24-02getting-started/mariadb-maxscale-2402-maxscale-2402-building-mariadb-maxscale-from-source-code.md)
* [Configuration Guide](maxscale-24-02getting-started/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-configuration-guide.md)
* [MaxGUI](maxscale-24-02getting-started/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-maxgui-guide.md)

### Upgrading MariaDB MaxScale

* [Upgrading MaxScale](broken-reference/)

### Reference

* [MaxCtrl - Command Line Admin Interface](maxscale-24-02reference/mariadb-maxscale-2402-maxscale-2402-maxctrl.md)
* [MaxScale REST API](maxscale-24-02rest-api/mariadb-maxscale-2402-maxscale-2402-rest-api.md)
* [Module Commands](maxscale-24-02reference/mariadb-maxscale-2402-maxscale-2402-module-commands.md)
* [Routing Hints](maxscale-24-02reference/mariadb-maxscale-2402-maxscale-2402-hint-syntax.md)

### Tutorials

The main tutorial for MariaDB MaxScale consist of setting up MariaDB MaxScale for the environment you are using with either a connection-based or a read/write-based configuration.

* [MariaDB MaxScale Tutorial](maxscale-24-02tutorials/mariadb-maxscale-2402-maxscale-2402-setting-up-mariadb-maxscale.md)

These tutorials are for specific use cases and module combinations.

* [Administration Tutorial](maxscale-24-02tutorials/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-administration-tutorial.md)
* [Avro Router Tutorial](maxscale-24-02tutorials/mariadb-maxscale-2402-maxscale-2402-avrorouter-tutorial.md)
* [Connection Routing Tutorial](maxscale-24-02tutorials/mariadb-maxscale-2402-maxscale-2402-connection-routing-with-mariadb-maxscale.md)
* [Filter Tutorial](maxscale-24-02tutorials/mariadb-maxscale-2402-maxscale-2402-filters.md)
* [MariaDB Monitor Failover Tutorial](maxscale-24-02tutorials/mariadb-maxscale-2402-maxscale-2402-automatic-failover-with-mariadb-monitor.md)
* [Read Write Splitting Tutorial](maxscale-24-02tutorials/mariadb-maxscale-2402-maxscale-2402-read-write-splitting-with-mariadb-maxscale.md)
* [Simple Schema Sharding Tutorial](maxscale-24-02tutorials/mariadb-maxscale-2402-maxscale-2402-simple-sharding-with-two-servers.md)

Here are tutorials on monitoring and managing MariaDB MaxScale in cluster environments.

* [REST API Tutorial](maxscale-24-02tutorials/mariadb-maxscale-2402-maxscale-2402-rest-api-tutorial.md)

### Routers

The routing module is the core of a MariaDB MaxScale service. The router documentation\
contains all module specific configuration options and detailed explanations\
of their use.

* [Avrorouter](maxscale-24-02routers/mariadb-maxscale-2402-maxscale-2402-avrorouter.md)
* [Binlogrouter](maxscale-24-02routers/mariadb-maxscale-2402-maxscale-2402-binlogrouter.md)
* [Cat](maxscale-24-02routers/mariadb-maxscale-2402-maxscale-2402-cat.md)
* [KafkaCDC](maxscale-24-02routers/mariadb-maxscale-2402-maxscale-2402-kafkacdc.md)
* [KafkaImporter](maxscale-24-02routers/mariadb-maxscale-2402-maxscale-2402-kafkaimporter.md)
* [MirrorRouter](maxscale-24-02routers/mariadb-maxscale-2402-maxscale-2402-mirror.md)
* [Read Connection Router](maxscale-24-02routers/mariadb-maxscale-2402-maxscale-2402-readconnroute.md)
* [Read Write Split](maxscale-24-02routers/mariadb-maxscale-2402-maxscale-2402-readwritesplit.md)
* [Schemarouter](maxscale-24-02routers/mariadb-maxscale-2402-maxscale-2402-schemarouter.md)
* [SmartRouter](maxscale-24-02routers/mariadb-maxscale-2402-maxscale-2402-smartrouter.md)

The following routers are only available in MaxScale Enterprise.

* [Diff](/broken/pages/bereh4MkASVoNSKMQwFa)

### Filters

Here are detailed documents about the filters MariaDB MaxScale offers. They contain configuration guides and example use cases. Before reading these, you should have read the filter tutorial so that you know how they work and how to configure them.

* [Binlog Filter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-binlog-filter.md)
* [Cache](maxscale-24-02filters/mariadb-maxscale-2402-cache.md)
* [Comment Filter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-comment-filter.md)
* [Consistent Critical Read Filter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-consistent-critical-read-filter.md)
* [Hint Filter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-hintfilter.md)
* [LDIFilter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-ldi-filter.md)
* [Luafilter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-lua-filter.md)
* [Masking Filter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-masking.md)
* [Maxrows Filter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-maxrows.md)
* [Named Server Filter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-named-server-filter.md)
* [Query Log All](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-query-log-all-filter.md)
* [Regex Filter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-regex-filter.md)
* [Rewrite Filter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-rewrite-filter.md)
* [Tee Filter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-tee-filter.md)
* [Throttle Filter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-throttle.md)
* [Top N Filter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-top-filter.md)
* [Transaction Performance Monitoring Filter](maxscale-24-02filters/mariadb-maxscale-2402-maxscale-2402-transaction-performance-monitoring-filter.md)

The following filters are only available in MaxScale Enterprise.

* [Wcar](broken-reference/)

### Monitors

Common options for all monitor modules.

* [Monitor Common](maxscale-24-02monitors/mariadb-maxscale-2402-maxscale-2402-common-monitor-parameters.md)

Module specific documentation.

* [Galera Monitor](maxscale-24-02monitors/mariadb-maxscale-2402-maxscale-2402-galera-monitor.md)
* [MariaDB Monitor](maxscale-24-02monitors/mariadb-maxscale-2402-maxscale-2402-mariadb-monitor.md)

### Protocols

Documentation for MaxScale protocol modules.

* [MariaDB](maxscale-24-02protocols/mariadb-maxscale-2402-maxscale-2402-mariadb-protocol-module.md)
* [Change Data Capture (CDC) Protocol](maxscale-24-02protocols/mariadb-maxscale-2402-maxscale-2402-change-data-capture-cdc-protocol.md)
* [Change Data Capture (CDC) Users](maxscale-24-02protocols/mariadb-maxscale-2402-maxscale-2402-change-data-capture-cdc-users.md)
* [NoSQL](maxscale-24-02protocols/mariadb-maxscale-2402-maxscale-2402-nosql-protocol-module.md)

The MaxScale CDC Connector provides a C++ API for consuming data from a CDC system.

* [CDC Connector](maxscale-24-02connectors/mariadb-maxscale-2402-maxscale-2402-maxscale-cdc-connector.md)

### Authenticators

A short description of the authentication module type can be found in the [Authentication Modules](maxscale-24-02authenticators/mariadb-maxscale-2402-maxscale-2402-authentication-modules.md)\
document.

* [MariaDB/MySQL Authenticator](maxscale-24-02authenticators/mariadb-maxscale-2402-maxscale-2402-mariadbmysql-authenticator.md)
* [GSSAPI Authenticator](maxscale-24-02authenticators/mariadb-maxscale-2402-maxscale-2402-gssapi-client-authenticator.md)
* [PAM Authenticator](maxscale-24-02authenticators/mariadb-maxscale-2402-maxscale-2402-pam-authenticator.md)
* [Ed25519 Authenticator](../mariadb-maxscale-23-02/mariadb-maxscale-23-02-authenticators/mariadb-maxscale-2302-ed25519-authenticator.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
