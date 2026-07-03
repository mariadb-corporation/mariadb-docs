---
description: Guide to upgrading MariaDB on Linux.
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

# Upgrading on Linux

{% columns %}
{% column %}
{% content-ref url="../../upgrading-between-major-mariadb-versions.md" %}
[../../upgrading-between-major-mariadb-versions.md](../../upgrading-between-major-mariadb-versions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Upgrade between major MariaDB versions, which is normally straightforward thanks to backward-compatible data files, connection protocol, and replication.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../upgrading-between-minor-versions-on-linux.md" %}
[../../upgrading-between-minor-versions-on-linux.md](../../upgrading-between-minor-versions-on-linux.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Step-by-step minor version upgrade (e.g., 11.4.4 to 11.4.5) for MariaDB Community Server on Linux using YUM, APT, or ZYpp — backup, stop, upgrade packages, restart, and run mariadb-upgrade.
{% endcolumn %}
{% endcolumns %}
