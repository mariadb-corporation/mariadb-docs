---
description: >-
  A collection of troubleshooting articles specific to Debian and Ubuntu
  deployments, covering upgrade failures, repository conflicts, and migration
  issues.
---

# Installation Issues on Debian and Ubuntu

{% columns %}
{% column %}
{% content-ref url="apt-upgrade-fails-but-the-database-is-running.md" %}
[apt-upgrade-fails-but-the-database-is-running.md](apt-upgrade-fails-but-the-database-is-running.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Solutions for when `apt-get upgrade` hangs or fails because the MariaDB service takes too long to start, triggering a timeout in the init script.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="differences-in-mariadb-in-debian-and-ubuntu.md" %}
[differences-in-mariadb-in-debian-and-ubuntu.md](differences-in-mariadb-in-debian-and-ubuntu.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains the differences between official Debian/Ubuntu repository packages and those from MariaDB.org, particularly regarding library linking and configuration defaults.
{% endcolumn %}
{% endcolumns %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
