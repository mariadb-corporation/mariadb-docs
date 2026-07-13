---
description: >-
  Learn about MariaDB R2DBC Connector for Java. This guide covers reactive,
  non-blocking database operations, setup, and integrating with Spring Data
  R2DBC for efficient data access.
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

# Connector/R2DBC

MariaDB Connector/R2DBC is the reactive, non-blocking R2DBC driver for connecting Java applications to MariaDB and MySQL databases. It can be used with the native R2DBC API or with the Spring Data framework.

{% columns %}
{% column %}
{% content-ref url="mariadb-connector-r2dbc-guide.md" %}
[mariadb-connector-r2dbc-guide.md](mariadb-connector-r2dbc-guide.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/R2DBC enables Java applications to connect to MariaDB using the non-blocking R2DBC API, with a native R2DBC implementation and Spring Data R2DBC framework integration.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-connector-r2dbc-connection-parameters.md" %}
[mariadb-connector-r2dbc-connection-parameters.md](mariadb-connector-r2dbc-connection-parameters.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/R2DBC connection parameters cover SSL mode, authentication plugins, autocommit, transaction replay, timezone handling, and prepared statement options.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="using-the-native-r2dbc-api-of-mariadb-connector-r2dbc/README.md" %}
[using-the-native-r2dbc-api-of-mariadb-connector-r2dbc](using-the-native-r2dbc-api-of-mariadb-connector-r2dbc/README.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Use MariaDB Connector/R2DBC directly through the native R2DBC API for reactive, non-blocking database operations with fine-grained control over data access in Java applications.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="using-the-spring-data-framework-with-mariadb-connector-r2dbc/README.md" %}
[using-the-spring-data-framework-with-mariadb-connector-r2dbc](using-the-spring-data-framework-with-mariadb-connector-r2dbc/README.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Integrate MariaDB Connector/R2DBC with the Spring Data framework for reactive, non-blocking data access using Spring Data R2DBC in modern Java applications.
{% endcolumn %}
{% endcolumns %}
