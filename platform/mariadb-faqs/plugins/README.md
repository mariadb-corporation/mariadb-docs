# Plugins

* Q: What are plugins in MariaDB and what is their purpose?\
  A: Plugins in MariaDB are modular software components or extensions that can be dynamically loaded into a running MariaDB Server to add new functionalities or modify existing behaviors without needing to recompile or alter the core server code. Their purpose is to provide a flexible and extensible architecture for the database system.
* Q: What is the main benefit of MariaDB's pluggable architecture?\
  A: The primary benefit of MariaDB's plugin architecture is the great flexibility and extensibility it offers. It allows users, third-party developers, and MariaDB itself to add specialized features, support new hardware, integrate MariaDB with other systems, or even introduce entirely new capabilities (like different storage engines or authentication methods). This helps keep the core MariaDB server lean and efficient while enabling a rich and diverse ecosystem of add-on functionalities.
* Q: What types of plugins are commonly available or can be developed for MariaDB?\
  A: MariaDB supports a wide variety of plugin types. Common examples include:
  * **Storage Engine Plugins**: Define data storage and management (e.g., MariaDB ColumnStore, MyRocks, Spider).
  * **Authentication Plugins**: Handle user authentication methods (e.g., plugins for PAM, LDAP, Kerberos, or GSSAPI).
  * **Audit Plugins**: Log database activity for security and compliance (e.g., MariaDB Enterprise Audit Plugin, community audit plugin).
  * **Full-text Parser Plugins**: Enable advanced full-text search for specific languages or data types (e.g., Mroonga for CJK languages).
  * **Information Schema Plugins**: Add virtual tables to the INFORMATION\_SCHEMA database to expose server information.
  * **Daemon Plugins**: Allow execution of background tasks or services within the MariaDB server process.
  * **Encryption Plugins**: Manage data encryption keys (e.g., MariaDB HashiCorp Vault Plugin).
* Q: How are plugins installed and managed within a MariaDB Server instance?\
  A: Plugins in MariaDB can typically be installed using SQL statements like INSTALL PLUGIN 'plugin\_name' SONAME 'shared\_library\_name.so'; or INSTALL SONAME 'shared\_library\_name.so';. Once installed, they can be enabled, disabled, or uninstalled. The SHOW PLUGINS; command is used to list all currently loaded plugins and display their operational status. Configuration of plugins is usually done via system variables.
* Q: Are all MariaDB plugins free to use or open source?\
  A: Many plugins are open source and are included by default with MariaDB Community Server or are available for download from the MariaDB community. However, some advanced plugins, particularly those offering enterprise-grade features, enhanced security, or specific integrations (like the MariaDB Enterprise Audit Plugin or the MariaDB HashiCorp Vault Plugin), may be commercial products and part of MariaDB Enterprise subscriptions offered by MariaDB plc.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
