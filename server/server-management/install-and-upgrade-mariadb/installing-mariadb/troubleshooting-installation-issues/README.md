---
description: >-
  A guide to diagnosing and resolving common installation and connection
  problems, such as socket errors, permission denied messages, and configuration
  conflicts.
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

# Troubleshooting Installation Issues

{% columns %}
{% column %}
{% content-ref url="error-symbol-mysql_get_server_name-version-libmysqlclient_16-not-defined.md" %}
[error-symbol-mysql_get_server_name-version-libmysqlclient_16-not-defined.md](error-symbol-mysql_get_server_name-version-libmysqlclient_16-not-defined.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Troubleshooting guide for a specific linker error involving `mysql_get_server_name` and `libmysqlclient_16`, typically occurring due to library version mismatches.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installation-issues-on-windows.md" %}
[installation-issues-on-windows.md](installation-issues-on-windows.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Common installation problems on Windows, such as issues with User Account Control (UAC) or unsupported Windows versions, and their solutions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installation-issues-with-php5.md" %}
[installation-issues-with-php5.md](installation-issues-with-php5.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Addresses compatibility issues between MariaDB and older PHP5 client libraries, specifically regarding header and library version mismatches.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installing-on-an-old-linux-version.md" %}
[installing-on-an-old-linux-version.md](installing-on-an-old-linux-version.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Guidance for dealing with glibc or shared library errors when attempting to install modern MariaDB binaries on older Linux distributions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installation-issues-on-debian-and-ubuntu/" %}
[installation-issues-on-debian-and-ubuntu](installation-issues-on-debian-and-ubuntu/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A collection of troubleshooting articles specific to Debian and Ubuntu deployments, covering upgrade failures, repository conflicts, and migration issues.
{% endcolumn %}
{% endcolumns %}
