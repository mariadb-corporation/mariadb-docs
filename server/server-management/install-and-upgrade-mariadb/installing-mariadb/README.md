---
description: >-
  Learn how to install MariaDB Server on various platforms. This section
  provides detailed guides and considerations for setting up your database
  environment, from simple installations to complex deploy
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

# Installing Community Server

{% columns %}
{% column %}
{% content-ref url="mariadb-id-sign-up.md" %}
[mariadb-id-sign-up.md](mariadb-id-sign-up.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Information on creating a free MariaDB ID account to access software downloads, including binary packages and repositories.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="binary-packages/" %}
[binary-packages](binary-packages/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Provides details on using MariaDB binary packages (tarballs, RPMs, DEBs) for installation, including repository configuration scripts.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installing-system-tables-mariadb-install-db/" %}
[installing-system-tables-mariadb-install-db](installing-system-tables-mariadb-install-db/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains the necessity of initializing system tables (using mariadb-install-db) after installation and troubleshooting startup issues related to missing tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="troubleshooting-installation-issues/" %}
[troubleshooting-installation-issues](troubleshooting-installation-issues/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A guide to diagnosing and resolving common installation and connection problems, such as socket errors, permission denied messages, and configuration conflicts.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installing-mariadb-on-ibm-cloud.md" %}
[installing-mariadb-on-ibm-cloud.md](installing-mariadb-on-ibm-cloud.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Step-by-step instructions for deploying MariaDB on IBM Cloud Kubernetes Service, including provisioning clusters and configuring storage.
{% endcolumn %}
{% endcolumns %}
