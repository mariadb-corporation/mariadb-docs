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
{% content-ref url="{connectors}/mariadb-connector-odbc/mariadb-connector-odbc-guide" %}
[mariadb-connector-odbc-guide.md]({connectors}/mariadb-connector-odbc/mariadb-connector-odbc-guide)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Connector/ODBC setup guide: Windows ODBC Administrator, `odbcinst.ini`/`odbc.ini` configuration, `isql` DSN testing, and DSN-less connection strings.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-odbc/building-mariadb-connectorodbc-from-source" %}
[building-mariadb-connectorodbc-from-source.md]({connectors}/mariadb-connector-odbc/building-mariadb-connectorodbc-from-source)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Compile MariaDB Connector/ODBC from the GitHub source repository on Linux or Windows, with step-by-step dependency installation for cmake, UnixODBC, and optional OpenSSL TLS support.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-odbc/creating-a-data-source-with-mariadb-connectorodbc" %}
[creating-a-data-source-with-mariadb-connectorodbc.md]({connectors}/mariadb-connector-odbc/creating-a-data-source-with-mariadb-connectorodbc)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Create a data source with MariaDB Connector/ODBC on Windows using ODBC Data Source Administrator, or on Linux by configuring UnixODBC with a driver entry and DSN for MariaDB Server.
{% endcolumn %}
{% endcolumns %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
