---
description: >-
  Explore temporal tables in MariaDB Server. This section details how to manage
  data with system-versioning and application-time periods, enabling historical
  data tracking and time-aware queries.
---

# Temporal Tables

{% columns %}
{% column %}
{% content-ref url="application-time-periods.md" %}
[application-time-periods.md](application-time-periods.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Application-time period tables define a time period between two temporal columns, for application-level data versioning.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="bitemporal-tables.md" %}
[bitemporal-tables.md](bitemporal-tables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Bitemporal tables combine system-versioning and application-time periods, versioning data at both levels.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="system-versioned-tables.md" %}
[system-versioned-tables.md](system-versioned-tables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete system-versioned tables: WITH SYSTEM VERSIONING syntax, FOR SYSTEM_TIME AS OF/BETWEEN/ALL queries, and ROW_START/ROW_END columns.
{% endcolumn %}
{% endcolumns %}
