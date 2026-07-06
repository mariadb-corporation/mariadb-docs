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

{% columns %}
{% column %}
{% content-ref url="mariadb-5533-debian-and-ubuntu-installation-issues.md" %}
[mariadb-5533-debian-and-ubuntu-installation-issues.md](mariadb-5533-debian-and-ubuntu-installation-issues.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Specific instructions for resolving dependency breakage that occurred with the release of MariaDB 5.5.33 on Debian and Ubuntu systems.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-debian-live-images.md" %}
[mariadb-debian-live-images.md](mariadb-debian-live-images.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Information about using MariaDB Debian Live images for testing and offline installation, including boot options and default credentials.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="moving-from-mysql-to-mariadb-in-debian-9.md" %}
[moving-from-mysql-to-mariadb-in-debian-9.md](moving-from-mysql-to-mariadb-in-debian-9.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A guide on migrating from MySQL 5.5 to MariaDB 10.1 during an operating system upgrade to Debian 9 (Stretch).
{% endcolumn %}
{% endcolumns %}
