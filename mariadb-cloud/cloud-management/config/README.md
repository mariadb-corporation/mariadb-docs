---
description: >-
  This section guides you through viewing, modifying, and applying configuration
  settings for your MariaDB Cloud database services, ensuring optimal
  performance and compliance.
icon: database
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
---

# Configuring Database Servers

Database server configuration, including system variables, is managed through the Configuration Manager.

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

## **Access to Configuration Manager**

To access the Configuration Manager interface:

1. Log in to the [Portal](https://app.skysql.com/dashboard).
2. Select <kbd>Settings</kbd> in the sidebar.
3. Select <kbd>Configuration Manager</kbd>.

After selecting Configuration Manager, you will be sent to Saved Configuration page, where you can view, create, and manage configuration templates for various MariaDB cloud topologies.

## **What is Configurable?**

Available configuration parameters differ by cloud database topology.

{% content-ref url="mariadb-serverless-single-node.md" %}
[mariadb-serverless-single-node.md](mariadb-serverless-single-node.md)
{% endcontent-ref %}

{% content-ref url="mariadb-server-single-node.md" %}
[mariadb-server-single-node.md](mariadb-server-single-node.md)
{% endcontent-ref %}

{% content-ref url="mariadb-server-with-replica-s.md" %}
[mariadb-server-with-replica-s.md](mariadb-server-with-replica-s.md)
{% endcontent-ref %}

{% content-ref url="maxscale.md" %}
[maxscale.md](maxscale.md)
{% endcontent-ref %}
