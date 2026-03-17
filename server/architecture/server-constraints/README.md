---
description: >-
  Understand MariaDB Server's architectural constraints. This section details
  limitations & design considerations, helping you optimize your database 
  deployments for maximum efficiency and scalability.
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
---

# Server Constraints

{% columns %}
{% column %}
{% content-ref url="server-constraints-overview.md" %}
[server-constraints-overview.md](server-constraints-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Provides a high-level overview of how MariaDB Server enforces data integrity through various architectural constraint types.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="auto_increment-constraints.md" %}
[auto\_increment-constraints.md](auto_increment-constraints.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains the limitations and behavior of `AUTO_INCREMENT` columns, including how they handle maximum values and gaps in sequences.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="foreign-key-constraints.md" %}
[foreign-key-constraints.md](foreign-key-constraints.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Details the requirements and limitations for defining foreign keys to ensure referential integrity between tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="not-null-constraints.md" %}
[not-null-constraints.md](not-null-constraints.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Describes how `NOT NULL` constraints prevent `NULL` values from being stored in specific columns.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="primary-key-constraints.md" %}
[primary-key-constraints.md](primary-key-constraints.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Outlines the rules for primary keys, which uniquely identify each record in a table and cannot contain `NULL` values.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="unique-constraints-with-mariadb-enterprise-server.md" %}
[unique-constraints-with-mariadb-enterprise-server.md](unique-constraints-with-mariadb-enterprise-server.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains the specific implementation and considerations for unique constraints when using MariaDB Enterprise Server.
{% endcolumn %}
{% endcolumns %}

