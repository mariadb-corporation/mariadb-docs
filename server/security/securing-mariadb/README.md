---
description: >-
  Overview of security best practices for MariaDB, covering privilege
  separation, mandatory access control (SELinux), and vulnerability tracking.
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

# Securing MariaDB

{% columns %}
{% column %}
{% content-ref url="running-mariadbd-as-root.md" %}
[running-mariadbd-as-root.md](running-mariadbd-as-root.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Understand the implications of running MariaDB Server as root. This section highlights security risks and provides guidance on configuring MariaDB Server to operate with less privileged user accounts.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="selinux.md" %}
[selinux.md](selinux.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Secure MariaDB Server with SELinux. This section guides you through configuring SELinux policies to enhance the security posture of your MariaDB deployments on Linux systems.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="security.md" %}
[security.md](security.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This is is the master list of CVEs fixed across all versions of MariaDB.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="security-vulnerabilities-in-oracle-mysql-that-did-not-exist-in-mariadb.md" %}
[security-vulnerabilities-in-oracle-mysql-that-did-not-exist-in-mariadb.md](security-vulnerabilities-in-oracle-mysql-that-did-not-exist-in-mariadb.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This page lists all CVEs that were fixed in MySQL and mentioned in Oracle CPU Advisories, but that — to the best of our knowledge — were never present in MariaDB.
{% endcolumn %}
{% endcolumns %}
