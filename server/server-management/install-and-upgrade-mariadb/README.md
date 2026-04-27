---
description: >-
  Learn to install and upgrade MariaDB Server. This section provides detailed
  instructions and best practices for setting up new instances and seamlessly
  upgrading existing ones to newer versions.
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

# Deployment

Deployment includes installing, configuring, upgrading, downgrading, migration from other DBMS[^1]s, and automated deployment options. Here's an overview of what you can find in this section.

{% columns %}
{% column %}
[mariadb-package-repository-setup-and-usage](mariadb-package-repository-setup-and-usage.md "mention")
{% endcolumn %}

{% column %}
* MariaDB Repository Setup Scripts
* MariaDB Foundation Repository Configuration Tool
* Set up RedHat, Ubuntu, Debian, and Suse repositories
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
[deployment-general-installing-and-upgrading-instructions](deployment-general-installing-and-upgrading-instructions/ "mention")
{% endcolumn %}

{% column %}
* Best practices
* Deployment methods
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
[installing-enterprise-server](installing-enterprise-server/ "mention")
{% endcolumn %}

{% column %}
* Customer download token
* Single-node installation
* Multi-node installation (primary/replica)
* Installation with ColumnStore
* Upgrade paths
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
[installing-mariadb](installing-mariadb/ "mention")
{% endcolumn %}

{% column %}
* MariaDB ID
* Installing binary packages (executables)
* Installing from source
* Installing system tables
* Troubleshooting installation issues
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
[configuring-mariadb](configuring-mariadb/ "mention")
{% endcolumn %}

{% column %}
* Option files
* Environment variables
* Advanced configuration options
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
[upgrading](upgrading/ "mention")
{% endcolumn %}

{% column %}
* Upgrade guides
* Upgrade paths
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
[automated-mariadb-deployment-and-administration](../automated-mariadb-deployment-and-administration/ "mention")
{% endcolumn %}

{% column %}
* Automation systems overview
* Ansible
* Puppet
* Containers
* Kubernetes
* Vagrant
{% endcolumn %}
{% endcolumns %}

[^1]: Database Management System. Popular DBMSs include MariaDB, MySQL, Oracle, PostgreSQL, and MongoDB.
