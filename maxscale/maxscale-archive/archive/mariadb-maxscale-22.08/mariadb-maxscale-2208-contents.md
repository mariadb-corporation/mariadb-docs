# MaxScale 22.08 Contents

## MaxScale 22.08 Contents

## Contents

### About MariaDB MaxScale

* [About MariaDB MaxScale](mariadb-maxscale-2208-about/mariadb-maxscale-2208-about-mariadb-maxscale.md)
* [Changelog](https://mariadb.com/kb/en/mariadb-maxscale-2208-maxscale-2208-changelog/)
* [Limitations](mariadb-maxscale-2208-about/mariadb-maxscale-2208-limitations-and-known-issues-within-mariadb-maxscale.md)

### Getting Started

* [MariaDB MaxScale Installation Guide](mariadb-maxscale-2208-getting-started/mariadb-maxscale-2208-mariadb-maxscale-installation-guide.md)
* [Building MariaDB MaxScale from Source Code](mariadb-maxscale-2208-getting-started/mariadb-maxscale-2208-building-mariadb-maxscale-from-source-code.md)
* [Configuration Guide](https://mariadb.com/kb/en/maxscale-2208-getting-started-mariadb-maxscale-configuration-guide/)
* [MaxGUI](mariadb-maxscale-2208-getting-started/mariadb-maxscale-2208-mariadb-maxscale-maxgui-guide.md)

### Upgrading MariaDB MaxScale

* [Upgrading MaxScale](https://mariadb.com/kb/en/upgrading-mariadb-maxscale/)

### Reference

* [MaxCtrl - Command Line Admin Interface](mariadb-maxscale-2208-reference/mariadb-maxscale-2208-maxctrl.md)
* [MaxScale REST API](https://mariadb.com/kb/en/mariadb-maxscale-2208-maxscale-rest-api/)
* [Module Commands](mariadb-maxscale-2208-reference/mariadb-maxscale-2208-module-commands.md)
* [Routing Hints](https://mariadb.com/kb/en/mariadb-maxscale-2208-maxscale-2208-hint-syntax/)

### Tutorials

The main tutorial for MariaDB MaxScale consist of setting up MariaDB MaxScale for the environment you are using with either a connection-based or a read/write-based configuration.

* [MariaDB MaxScale Tutorial](mariadb-maxscale-2208-tutorials/mariadb-maxscale-2208-setting-up-mariadb-maxscale.md)

These tutorials are for specific use cases and module combinations.

* [Administration Tutorial](mariadb-maxscale-2208-tutorials/mariadb-maxscale-2208-mariadb-maxscale-administration-tutorial.md)
* [Avro Router Tutorial](mariadb-maxscale-2208-tutorials/mariadb-maxscale-2208-avrorouter-tutorial.md)
* [Connection Routing Tutorial](mariadb-maxscale-2208-tutorials/mariadb-maxscale-2208-connection-routing-with-mariadb-maxscale.md)
* [Filter Tutorial](mariadb-maxscale-2208-tutorials/mariadb-maxscale-2208-filters.md)
* [MariaDB Monitor Failover Tutorial](mariadb-maxscale-2208-tutorials/mariadb-maxscale-2208-automatic-failover-with-mariadb-monitor.md)
* [Read Write Splitting Tutorial](mariadb-maxscale-2208-tutorials/mariadb-maxscale-2208-read-write-splitting-with-mariadb-maxscale.md)
* [Simple Schema Sharding Tutorial](mariadb-maxscale-2208-tutorials/mariadb-maxscale-2208-simple-sharding-with-two-servers.md)

Here are tutorials on monitoring and managing MariaDB MaxScale in cluster environments.

* [REST API Tutorial](mariadb-maxscale-2208-tutorials/mariadb-maxscale-2208-rest-api-tutorial.md)

### Routers

The routing module is the core of a MariaDB MaxScale service. The router documentation
contains all module specific configuration options and detailed explanations
of their use.

* [Avrorouter](mariadb-maxscale-2208-routers/mariadb-maxscale-2208-avrorouter.md)
* [Binlogrouter](mariadb-maxscale-2208-routers/mariadb-maxscale-2208-binlogrouter.md)
* [Cat](mariadb-maxscale-2208-routers/mariadb-maxscale-2208-cat.md)
* [KafkaCDC](mariadb-maxscale-2208-routers/mariadb-maxscale-2208-kafkacdc.md)
* [KafkaImporter](mariadb-maxscale-2208-routers/mariadb-maxscale-2208-kafkaimporter.md)
* [MirrorRouter](mariadb-maxscale-2208-routers/mariadb-maxscale-2208-mirror.md)
* [Read Connection Router](mariadb-maxscale-2208-routers/mariadb-maxscale-2208-readconnroute.md)
* [Read Write Split](mariadb-maxscale-2208-routers/mariadb-maxscale-2208-readwritesplit.md)
* [Schemarouter](mariadb-maxscale-2208-routers/mariadb-maxscale-2208-schemarouter.md)
* [SmartRouter](mariadb-maxscale-2208-routers/mariadb-maxscale-2208-smartrouter.md)

### Filters

Here are detailed documents about the filters MariaDB MaxScale offers. They contain configuration guides and example use cases. Before reading these, you should have read the filter tutorial so that you know how they work and how to configure them.

* [Binlog Filter](mariadb-maxscale-2208--filters/mariadb-maxscale-2208-binlog-filter.md)
* [Cache](mariadb-maxscale-2208--filters/mariadb-maxscale-2208-cache.md)
* [Comment Filter](mariadb-maxscale-2208--filters/mariadb-maxscale-2208-comment-filter.md)
* [Consistent Critical Read Filter](mariadb-maxscale-2208--filters/mariadb-maxscale-2208-consistent-critical-read-filter.md)
* [Hint Filter](mariadb-maxscale-2208--filters/mariadb-maxscale-2208-hintfilter.md)
* [Insert Stream Filter](mariadb-maxscale-2208--filters/mariadb-maxscale-2208-insert-stream-filter.md)
* [Masking Filter](mariadb-maxscale-2208--filters/mariadb-maxscale-2208-masking.md)
* [Maxrows Filter](mariadb-maxscale-2208--filters/mariadb-maxscale-2208-maxrows.md)
* [Named Server Filter](mariadb-maxscale-2208--filters/mariadb-maxscale-2208-named-server-filter.md)
* [Query Log All](mariadb-maxscale-2208--filters/mariadb-maxscale-2208-query-log-all-filter.md)
* [Regex Filter](mariadb-maxscale-2208--filters/mariadb-maxscale-2208-regex-filter.md)
* [Rewrite Filter](https://mariadb.com/kb/en/rewrite-filter/)
* [Tee Filter](mariadb-maxscale-2208--filters/mariadb-maxscale-2208-tee-filter.md)
* [Throttle Filter](mariadb-maxscale-2208--filters/mariadb-maxscale-2208-throttle.md)
* [Top N Filter](mariadb-maxscale-2208--filters/mariadb-maxscale-2208-top-filter.md)

### Monitors

Common options for all monitor modules.

* [Monitor Common](mariadb-maxscale-2208-monitors/mariadb-maxscale-2208-common-monitor-parameters.md)

Module specific documentation.

* [Aurora Monitor](mariadb-maxscale-2208-monitors/mariadb-maxscale-2208-aurora-monitor.md)
* [ColumnStore Monitor](mariadb-maxscale-2208-monitors/mariadb-maxscale-2208-columnstore-monitor.md)
* [Galera Monitor](mariadb-maxscale-2208-monitors/mariadb-maxscale-2208-galera-monitor.md)
* [MariaDB Monitor](mariadb-maxscale-2208-monitors/mariadb-maxscale-2208-mariadb-monitor.md)

### Protocols

Documentation for MaxScale protocol modules.

* [MariaDB](https://mariadb.com/kb/en/mariadb-protocol-module/)
* [Change Data Capture (CDC) Protocol](mariadb-maxscale-2208-protocols/mariadb-maxscale-2208-change-data-capture-cdc-protocol.md)
* [Change Data Capture (CDC) Users](mariadb-maxscale-2208-protocols/mariadb-maxscale-2208-change-data-capture-cdc-users.md)
* [NoSQL](mariadb-maxscale-2208-protocols/mariadb-maxscale-2208-nosql-protocol-module.md)

The MaxScale CDC Connector provides a C++ API for consuming data from a CDC system.

* [CDC Connector](mariadb-maxscale-2208-connectors/mariadb-maxscale-2208-maxscale-cdc-connector.md)

### Authenticators

A short description of the authentication module type can be found in the [Authentication Modules](https://mariadb.com/kb/en/mariadb-maxscale-2208-maxscale-2208-authentication-modules/)
document.

* [MariaDB/MySQL Authenticator](mariadb-maxscale-2208-authenticators/mariadb-maxscale-2208-mysql-authenticator.md)
* [GSSAPI Authenticator](mariadb-maxscale-2208-authenticators/mariadb-maxscale-2208-gssapi-client-authenticator.md)
* [PAM Authenticator](mariadb-maxscale-2208-authenticators/mariadb-maxscale-2208-pam-authenticator.md)

### Design Documents

* [Plugin development guide](https://mariadb.com/kb/en/mariadb-maxscale-2208-mariadb-maxscale-plugin-development-guide/)

CC BY-SA / Gnu FDL
