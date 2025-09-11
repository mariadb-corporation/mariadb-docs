# MaxScale 21.06 Contents

**NOTE** MaxScale 6.4 was renamed to 21.06 in May 2024. Thus, what would have\
been released as 6.4.16 in June, was released as 21.06.16. The purpose of this\
change is to make the versioning scheme used by all MaxScale series\
identical. 21.06 denotes the year and month when the first 6 release was made.\
Anything referring to MaxScale 6 applies to MaxScale 21.06.

### About MariaDB MaxScale

* [About MariaDB MaxScale](mariadb-maxscale-21-06-about/mariadb-maxscale-2106-maxscale-2106-about-mariadb-maxscale.md)
* [Changelog](broken-reference)
* [Limitations](mariadb-maxscale-21-06-about/mariadb-maxscale-2106-maxscale-2106-limitations-and-known-issues-within-mariadb-maxscale.md)

### Getting Started

* [MariaDB MaxScale Installation Guide](mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-installation-guide.md)
* [Building MariaDB MaxScale from Source Code](mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-building-mariadb-maxscale-from-source-code.md)
* [Configuration Guide](mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md)
* [MaxGUI](mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-maxgui-guide.md)

### Upgrading MariaDB MaxScale

* [Upgrading MaxScale](mariadb-maxscale-21-06-upgrading/mariadb-maxscale-2106-maxscale-2106-upgrading-mariadb-maxscale.md)

### Reference

* [MaxCtrl - Command Line Admin Interface](mariadb-maxscale-21-06-reference/mariadb-maxscale-2106-maxscale-2106-maxctrl.md)
* [MaxScale REST API](mariadb-maxscale-21-06-rest-api/mariadb-maxscale-2106-maxscale-2106-rest-api.md)
* [Module Commands](mariadb-maxscale-21-06-reference/mariadb-maxscale-2106-maxscale-2106-module-commands.md)
* [Routing Hints](mariadb-maxscale-21-06-reference/mariadb-maxscale-2106-maxscale-2106-hint-syntax.md)

### Tutorials

The main tutorial for MariaDB MaxScale consist of setting up MariaDB MaxScale for the environment you are using with either a connection-based or a read/write-based configuration.

* [MariaDB MaxScale Tutorial](mariadb-maxscale-21-06-tutorials/mariadb-maxscale-2106-maxscale-2106-setting-up-mariadb-maxscale.md)

These tutorials are for specific use cases and module combinations.

* [Administration Tutorial](mariadb-maxscale-21-06-tutorials/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-administration-tutorial.md)
* [Avro Router Tutorial](mariadb-maxscale-21-06-tutorials/mariadb-maxscale-2106-maxscale-2106-avrorouter-tutorial.md)
* [Connection Routing Tutorial](mariadb-maxscale-21-06-tutorials/mariadb-maxscale-2106-maxscale-2106-connection-routing-with-mariadb-maxscale.md)
* [Filter Tutorial](mariadb-maxscale-21-06-tutorials/mariadb-maxscale-2106-maxscale-2106-filters.md)
* [MariaDB Monitor Failover Tutorial](mariadb-maxscale-21-06-tutorials/mariadb-maxscale-2106-maxscale-2106-automatic-failover-with-mariadb-monitor.md)
* [Read Write Splitting Tutorial](mariadb-maxscale-21-06-tutorials/mariadb-maxscale-2106-maxscale-2106-read-write-splitting-with-mariadb-maxscale.md)
* [Simple Schema Sharding Tutorial](mariadb-maxscale-21-06-tutorials/mariadb-maxscale-2106-maxscale-2106-simple-sharding-with-two-servers.md)

Here are tutorials on monitoring and managing MariaDB MaxScale in cluster environments.

* [REST API Tutorial](mariadb-maxscale-21-06-tutorials/mariadb-maxscale-2106-maxscale-2106-rest-api-tutorial.md)

### Routers

The routing module is the core of a MariaDB MaxScale service. The router documentation\
contains all module specific configuration options and detailed explanations\
of their use.

* [Avrorouter](mariadb-maxscale-21-06-routers/mariadb-maxscale-2106-maxscale-2106-avrorouter.md)
* [Binlogrouter](mariadb-maxscale-21-06-routers/mariadb-maxscale-2106-maxscale-2106-binlogrouter.md)
* [Cat](mariadb-maxscale-21-06-routers/mariadb-maxscale-2106-maxscale-2106-cat.md)
* [KafkaCDC](mariadb-maxscale-21-06-routers/mariadb-maxscale-2106-maxscale-2106-kafkacdc.md)
* [MirrorRouter](mariadb-maxscale-21-06-routers/mariadb-maxscale-2106-maxscale-2106-mirror.md)
* [Read Connection Router](mariadb-maxscale-21-06-routers/mariadb-maxscale-2106-maxscale-2106-readconnroute.md)
* [Read Write Split](mariadb-maxscale-21-06-routers/mariadb-maxscale-2106-maxscale-2106-readwritesplit.md)
* [Schemarouter](mariadb-maxscale-21-06-routers/mariadb-maxscale-2106-maxscale-2106-schemarouter.md)
* [SmartRouter](mariadb-maxscale-21-06-routers/mariadb-maxscale-2106-maxscale-2106-smartrouter.md)

### Filters

Here are detailed documents about the filters MariaDB MaxScale offers. They contain configuration guides and example use cases. Before reading these, you should have read the filter tutorial so that you know how they work and how to configure them.

* [Binlog Filter](mariadb-maxscale-21-06-filters/mariadb-maxscale-2106-maxscale-2106-binlog-filter.md)
* [Cache](mariadb-maxscale-21-06-filters/mariadb-maxscale-2106-cache.md)
* [Consistent Critical Read Filter](mariadb-maxscale-21-06-filters/mariadb-maxscale-2106-maxscale-2106-consistent-critical-read-filter.md)
* [Database Firewall Filter](mariadb-maxscale-21-06-filters/mariadb-maxscale-2106-maxscale-2106-database-firewall-filter.md)
* [Hint Filter](mariadb-maxscale-21-06-filters/mariadb-maxscale-2106-maxscale-2106-hintfilter.md)
* [Insert Stream Filter](mariadb-maxscale-21-06-filters/mariadb-maxscale-2106-maxscale-2106-insert-stream-filter.md)
* [Luafilter](mariadb-maxscale-21-06-filters/mariadb-maxscale-2106-maxscale-2106-lua-filter.md)
* [Masking Filter](mariadb-maxscale-21-06-filters/mariadb-maxscale-2106-maxscale-2106-masking.md)
* [Maxrows Filter](mariadb-maxscale-21-06-filters/mariadb-maxscale-2106-maxscale-2106-maxrows.md)
* [Named Server Filter](mariadb-maxscale-21-06-filters/mariadb-maxscale-2106-maxscale-2106-named-server-filter.md)
* [Query Log All](mariadb-maxscale-21-06-filters/mariadb-maxscale-2106-maxscale-2106-query-log-all-filter.md)
* [Regex Filter](mariadb-maxscale-21-06-filters/mariadb-maxscale-2106-maxscale-2106-regex-filter.md)
* [Tee Filter](mariadb-maxscale-21-06-filters/mariadb-maxscale-2106-maxscale-2106-tee-filter.md)
* [Throttle Filter](mariadb-maxscale-21-06-filters/mariadb-maxscale-2106-maxscale-2106-throttle.md)
* [Top N Filter](mariadb-maxscale-21-06-filters/mariadb-maxscale-2106-maxscale-2106-top-filter.md)
* [Transaction Performance Monitoring Filter](mariadb-maxscale-21-06-filters/mariadb-maxscale-2106-maxscale-2106-transaction-performance-monitoring-filter.md)

### Monitors

Common options for all monitor modules.

* [Monitor Common](mariadb-maxscale-2106-maxscale-21-06-monitors/mariadb-maxscale-2106-maxscale-2106-common-monitor-parameters.md)

Module specific documentation.

* [Aurora Monitor](mariadb-maxscale-2106-maxscale-21-06-monitors/mariadb-maxscale-2106-maxscale-2106-aurora-monitor.md)
* [ColumnStore Monitor](mariadb-maxscale-2106-maxscale-21-06-monitors/mariadb-maxscale-2106-maxscale-2106-columnstore-monitor.md)
* [Galera Monitor](mariadb-maxscale-2106-maxscale-21-06-monitors/mariadb-maxscale-2106-maxscale-2106-galera-monitor.md)
* [MariaDB Monitor](mariadb-maxscale-2106-maxscale-21-06-monitors/mariadb-maxscale-2106-maxscale-2106-mariadb-monitor.md)

### Protocols

Documentation for MaxScale protocol modules.

* [MariaDB](mariadb-maxscale-21-06-protocols/mariadb-maxscale-2106-maxscale-2106-mariadb-protocol-module.md)
* [Change Data Capture (CDC) Protocol](mariadb-maxscale-21-06-protocols/mariadb-maxscale-2106-maxscale-2106-change-data-capture-cdc-protocol.md)
* [Change Data Capture (CDC) Users](mariadb-maxscale-21-06-protocols/mariadb-maxscale-2106-maxscale-2106-change-data-capture-cdc-users.md)
* [NoSQL](mariadb-maxscale-21-06-protocols/mariadb-maxscale-2106-maxscale-2106-nosql-protocol-module.md)

The MaxScale CDC Connector provides a C++ API for consuming data from a CDC system.

* [CDC Connector](mariadb-maxscale-21-06-connectors/mariadb-maxscale-2106-maxscale-2106-maxscale-cdc-connector.md)

### Authenticators

A short description of the authentication module type can be found in the [Authentication Modules](mariadb-maxscale-21-06-authenticators/mariadb-maxscale-2106-maxscale-2106-authentication-modules.md)\
document.

* [MariaDB/MySQL Authenticator](mariadb-maxscale-21-06-authenticators/mariadb-maxscale-2106-maxscale-2106-mariadbmysql-authenticator.md)
* [GSSAPI Authenticator](mariadb-maxscale-21-06-authenticators/mariadb-maxscale-2106-maxscale-2106-gssapi-client-authenticator.md)
* [PAM Authenticator](mariadb-maxscale-21-06-authenticators/mariadb-maxscale-2106-maxscale-2106-pam-authenticator.md)

### Design Documents

* [Plugin development guide](mariadb-maxscale-21-06-design-documents/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-plugin-development-guide.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
