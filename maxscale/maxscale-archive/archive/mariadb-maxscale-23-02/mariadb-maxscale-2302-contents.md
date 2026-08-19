# MaxScale 23.02 Contents

### About MariaDB MaxScale

* [About MariaDB MaxScale](mariadb-maxscale-23-02-about/mariadb-maxscale-2302-about-mariadb-maxscale.md)
* [Changelog](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/maxscale/23.02/23.02-changelog)
* [Limitations](mariadb-maxscale-23-02-about/mariadb-maxscale-2302-limitations-and-known-issues-within-mariadb-maxscale.md)

### Getting Started

* [MariaDB MaxScale Installation Guide](mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-installation-guide.md)
* [Building MariaDB MaxScale from Source Code](mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-building-mariadb-maxscale-from-source-code.md)
* [Configuration Guide](mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md)
* [MaxGUI](mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-maxgui-guide.md)

### Upgrading MariaDB MaxScale

* [Upgrading MaxScale](mariadb-maxscale-23-02-upgrading/mariadb-maxscale-2302-maxscale-2302-upgrading-mariadb-maxscale.md)

### Reference

* [MaxCtrl - Command Line Admin Interface](mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl.md)
* [MaxScale REST API](mariadb-maxscale-23-02-rest-api/mariadb-maxscale-2302-rest-api.md)
* [Module Commands](mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-module-commands.md)
* [Routing Hints](mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-hint-syntax.md)

### Tutorials

The main tutorial for MariaDB MaxScale consist of setting up MariaDB MaxScale for the environment you are using with either a connection-based or a read/write-based configuration.

* [MariaDB MaxScale Tutorial](mariadb-maxscale-23-02-tutorials/mariadb-maxscale-2302-setting-up-mariadb-maxscale.md)

These tutorials are for specific use cases and module combinations.

* [Administration Tutorial](mariadb-maxscale-23-02-tutorials/mariadb-maxscale-2302-mariadb-maxscale-administration-tutorial.md)
* [Avro Router Tutorial](mariadb-maxscale-23-02-tutorials/mariadb-maxscale-2302-avrorouter-tutorial.md)
* [Connection Routing Tutorial](mariadb-maxscale-23-02-tutorials/mariadb-maxscale-2302-connection-routing-with-mariadb-maxscale.md)
* [Filter Tutorial](mariadb-maxscale-23-02-tutorials/mariadb-maxscale-2302-filters.md)
* [MariaDB Monitor Failover Tutorial](mariadb-maxscale-23-02-tutorials/mariadb-maxscale-2302-automatic-failover-with-mariadb-monitor.md)
* [Read Write Splitting Tutorial](mariadb-maxscale-23-02-tutorials/mariadb-maxscale-2302-read-write-splitting-with-mariadb-maxscale.md)
* [Simple Schema Sharding Tutorial](mariadb-maxscale-23-02-tutorials/mariadb-maxscale-2302-simple-sharding-with-two-servers.md)

Here are tutorials on monitoring and managing MariaDB MaxScale in cluster environments.

* [REST API Tutorial](mariadb-maxscale-23-02-tutorials/mariadb-maxscale-2302-rest-api-tutorial.md)

### Routers

The routing module is the core of a MariaDB MaxScale service. The router documentation
contains all module specific configuration options and detailed explanations
of their use.

* [Avrorouter](mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-avrorouter.md)
* [Binlogrouter](mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-binlogrouter.md)
* [Cat](mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-cat.md)
* [KafkaCDC](mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-kafkacdc.md)
* KafkaImporter
* [MirrorRouter](mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-mirror.md)
* [Read Connection Router](mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-readconnroute.md)
* [Read Write Split](mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-readwritesplit.md)
* [Schemarouter](mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-schemarouter.md)
* [SmartRouter](mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-smartrouter.md)

### Filters

Here are detailed documents about the filters MariaDB MaxScale offers. They contain configuration guides and example use cases. Before reading these, you should have read the filter tutorial so that you know how they work and how to configure them.

* [Binlog Filter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-binlog-filter.md)
* [Cache](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-cache.md)
* [Comment Filter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-comment-filter.md)
* [Consistent Critical Read Filter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-consistent-critical-read-filter.md)
* [Hint Filter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-hintfilter.md)
* [Luafilter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-lua-filter.md)
* [Masking Filter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-masking.md)
* [Maxrows Filter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-maxrows.md)
* [Named Server Filter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-named-server-filter.md)
* [Query Log All](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-query-log-all-filter.md)
* [Regex Filter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-regex-filter.md)
* [Rewrite Filter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-rewrite-filter.md)
* [Tee Filter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-tee-filter.md)
* [Throttle Filter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-throttle.md)
* [Top N Filter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-top-filter.md)
* [Transaction Performance Monitoring Filter](mariadb-maxscale-23-02-filters/mariadb-maxscale-2302-transaction-performance-monitoring-filter.md)

### Monitors

Common options for all monitor modules.

* [Monitor Common](mariadb-maxscale-23-02-monitors/mariadb-maxscale-2302-common-monitor-parameters.md)

Module specific documentation.

* [Galera Monitor](mariadb-maxscale-23-02-monitors/mariadb-maxscale-2302-galera-monitor.md)
* [MariaDB Monitor](mariadb-maxscale-23-02-monitors/mariadb-maxscale-2302-mariadb-monitor.md)

### Protocols

Documentation for MaxScale protocol modules.

* [MariaDB](mariadb-maxscale-23-02-protocols/mariadb-maxscale-2302-maxscale-2302-mariadb-protocol-module.md)
* [Change Data Capture (CDC) Protocol](mariadb-maxscale-23-02-protocols/mariadb-maxscale-2302-change-data-capture-cdc-protocol.md)
* [Change Data Capture (CDC) Users](mariadb-maxscale-23-02-protocols/mariadb-maxscale-2302-change-data-capture-cdc-users.md)
* [NoSQL](mariadb-maxscale-23-02-protocols/mariadb-maxscale-2302-nosql-protocol-module.md)

The MaxScale CDC Connector provides a C++ API for consuming data from a CDC system.

* [CDC Connector](mariadb-maxscale-23-02-connectors/mariadb-maxscale-2302-maxscale-cdc-connector.md)

### Authenticators

A short description of the authentication module type can be found in the [Authentication Modules](mariadb-maxscale-23-02-authenticators/mariadb-maxscale-2302-authentication-modules.md)
document.

* [MariaDB/MySQL Authenticator](mariadb-maxscale-23-02-authenticators/mariadb-maxscale-2302-mysql-authenticator.md)
* [GSSAPI Authenticator](mariadb-maxscale-23-02-authenticators/mariadb-maxscale-2302-gssapi-client-authenticator.md)
* [PAM Authenticator](mariadb-maxscale-23-02-authenticators/mariadb-maxscale-2302-pam-authenticator.md)
* [Ed25519 Authenticator](mariadb-maxscale-23-02-authenticators/mariadb-maxscale-2302-ed25519-authenticator.md)

### Design Documents

* [Plugin development guide](mariadb-maxscale-23-02-design-documents/mariadb-maxscale-2302-mariadb-maxscale-plugin-development-guide.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
