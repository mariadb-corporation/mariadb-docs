---
description: >-
  Explains the necessity of initializing system tables (using
  mariadb-install-db) after installation and troubleshooting startup issues
  related to missing tables.
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

# Installing System Tables

{% columns %}
{% column %}
{% content-ref url="installing-system-tables-on-unix.md" %}
[installing-system-tables-on-unix.md](installing-system-tables-on-unix.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Instructions for running the `mariadb-install-db` script on Unix-like systems to initialize the MariaDB data directory and system tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-install-db-exe.md" %}
[mariadb-install-db-exe.md](mariadb-install-db-exe.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Details the use of `mariadb-install-db.exe` on Windows to create new database instances, set the root password, and register Windows services.
{% endcolumn %}
{% endcolumns %}
