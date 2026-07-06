---
description: >-
  Provides tailored instructions for upgrading MariaDB on different operating
  systems, including Linux and Windows, and within specific environments like
  Galera Cluster.
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

# Platform Specific Upgrade Guides

{% columns %}
{% column %}
{% content-ref url="upgrading-on-linux/" %}
[upgrading-on-linux](upgrading-on-linux/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Guide to upgrading MariaDB on Linux.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../upgrading-mariadb-on-windows.md" %}
[upgrading-mariadb-on-windows.md](../upgrading-mariadb-on-windows.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Guide to upgrading MariaDB on Windows using the MSI installer, supporting both minor upgrades and major version migrations using the upgrade wizard.
{% endcolumn %}
{% endcolumns %}
