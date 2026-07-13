---
description: >-
  Data structures and type definitions used by the MariaDB Connector/C
  prepared-statement API, including MYSQL_BIND, MYSQL_STMT, and the associated
  type and indicator constants.
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

# Connector C Data Structures and Definitions

{% columns %}
{% column %}
{% content-ref url="connectorc-types-and-definitions.md" %}
[connectorc-types-and-definitions.md](connectorc-types-and-definitions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Connector/C field types and indicator variables used in the MYSQL_BIND structure, including the MYSQL_TYPE constants and STMT_INDICATOR values defined in `mariadb_com.h`.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql_bind.md" %}
[mysql_bind.md](mysql_bind.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MYSQL_BIND binds input parameters and output result columns to a prepared statement, with support for array binding and indicator variables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql_stmt.md" %}
[mysql_stmt.md](mysql_stmt.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MYSQL_STMT is the handle for a prepared statement, allocated by `mysql_stmt_init()` and released by `mysql_stmt_close()`; all of its members are private.
{% endcolumn %}
{% endcolumns %}
