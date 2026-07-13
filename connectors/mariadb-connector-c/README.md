---
description: >-
  The MariaDB Connector/C is used to connect applications developed in C/C++ to
  MariaDB and MySQL databases. MariaDB Connector/C is LGPLv2.1 licensed.
icon: link
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# Connector/C

MariaDB Connector/C is the C client library for connecting C/C++ applications to MariaDB and MySQL databases. It is LGPLv2.1 licensed.

{% columns %}
{% column %}
{% content-ref url="mariadb-connector-c-guide.md" %}
[mariadb-connector-c-guide.md](mariadb-connector-c-guide.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete Connector/C reference: Windows MSI install, Linux packages (yum/apt/zypper), MariaDB-shared/devel libraries, and option file configuration.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="install-mariadb-connector-c.md" %}
[install-mariadb-connector-c.md](install-mariadb-connector-c.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Install MariaDB Connector/C on Linux, Windows, and macOS, with configuration and verification steps for production use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="configuring-mariadb-connectorc-with-option-files.md" %}
[configuring-mariadb-connectorc-with-option-files.md](configuring-mariadb-connectorc-with-option-files.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/C reads connection settings from option files such as `my.cnf`, supporting default and custom file locations, option groups, and a full set of client options.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-binlogreplication-api-reference/README.md" %}
[mariadb-binlogreplication-api-reference](mariadb-binlogreplication-api-reference/README.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/C binlog and replication API reference, documenting the functions used to consume binary log events from a MariaDB server as a replication client.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-connectorc-data-structures.md" %}
[mariadb-connectorc-data-structures.md](mariadb-connectorc-data-structures.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Reference for the public data structures in MariaDB Connector/C, including MYSQL, MYSQL_RES, MYSQL_STMT, MYSQL_FIELD, MYSQL_BIND, and MYSQL_TIME with all member definitions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-connectorc-plugins.md" %}
[mariadb-connectorc-plugins.md](mariadb-connectorc-plugins.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/C supports loadable and built-in plugins across four categories: connection, pvio, I/O, and authentication, including remote_io and multiple auth methods.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-connectorc-types-and-definitions.md" %}
[mariadb-connectorc-types-and-definitions.md](mariadb-connectorc-types-and-definitions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Reference for MariaDB Connector/C types and definitions, including enumeration constants for field types, statement options, cursor types, indicator types, field flags, and server status.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="building-connectorc-from-source/README.md" %}
[building-connectorc-from-source](building-connectorc-from-source/README.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Build MariaDB Connector/C from source: download the package from MariaDB downloads or get the latest development version from the Connector/C GitHub repository.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="api-functions/README.md" %}
[api-functions](api-functions/README.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Detailed documentation on the MariaDB Connector/C API functions for connecting, querying, and managing data in C applications.
{% endcolumn %}
{% endcolumns %}
