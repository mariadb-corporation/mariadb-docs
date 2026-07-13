---
description: >-
  MariaDB Connector/ODBC guide: installation, configuration, query execution,
  and integration, with examples.
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

# Connector/ODBC

MariaDB Connector/ODBC is the ODBC driver for connecting ODBC-based applications to MariaDB and MySQL databases. It is built on MariaDB Connector/C.

{% columns %}
{% column %}
{% content-ref url="mariadb-connector-odbc-guide.md" %}
[mariadb-connector-odbc-guide.md](mariadb-connector-odbc-guide.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Connector/ODBC setup guide: Windows ODBC Administrator, `odbcinst.ini`/`odbc.ini` configuration, `isql` DSN testing, and DSN-less connection strings.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="building-mariadb-connectorodbc-from-source.md" %}
[building-mariadb-connectorodbc-from-source.md](building-mariadb-connectorodbc-from-source.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Compile MariaDB Connector/ODBC from the GitHub source repository on Linux or Windows, with step-by-step dependency installation for cmake, UnixODBC, and optional OpenSSL TLS support.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="creating-a-data-source-with-mariadb-connectorodbc.md" %}
[creating-a-data-source-with-mariadb-connectorodbc.md](creating-a-data-source-with-mariadb-connectorodbc.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Create a data source with MariaDB Connector/ODBC on Windows using ODBC Data Source Administrator, or on Linux by configuring UnixODBC with a driver entry and DSN for MariaDB Server.
{% endcolumn %}
{% endcolumns %}
