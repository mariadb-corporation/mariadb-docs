---
description: >-
  Explore key management and encryption plugins for MariaDB Server. This section
  details how to manage encryption keys and leverage plugins for robust
  data-at-rest protection.
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

# Key Management and Encryption Plugins

{% columns %}
{% column %}
{% content-ref url="encryption-key-management.md" %}
[encryption-key-management.md](encryption-key-management.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Overview of key management in MariaDB, discussing the need for plugins to manage encryption keys, support for multiple keys (ID 1 for system, ID 2 for temp), and key rotation capabilities.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="file-key-management-encryption-plugin.md" %}
[file-key-management-encryption-plugin.md](file-key-management-encryption-plugin.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Details the File Key Management plugin, which reads encryption keys from a plain-text (or encrypted) file, serving as a simple solution or reference implementation for data-at-rest encryption.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="aws-key-management-encryption-plugin.md" %}
[aws-key-management-encryption-plugin.md](aws-key-management-encryption-plugin.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Introduction to the AWS Key Management plugin, which uses Amazon KMS to generate and store master keys, decrypting them at startup to enable data-at-rest encryption with key rotation support.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="aws-key-management-encryption-plugin-advanced-usage.md" %}
[aws-key-management-encryption-plugin-advanced-usage.md](aws-key-management-encryption-plugin-advanced-usage.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Step-by-step tutorial for setting up the AWS KMS plugin, covering the creation of a Customer Master Key (CMK) in AWS, configuring IAM roles for EC2, and installing the plugin from source.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="aws-key-management-encryption-plugin-setup-guide.md" %}
[aws-key-management-encryption-plugin-setup-guide.md](aws-key-management-encryption-plugin-setup-guide.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Advanced configuration guide for the AWS KMS plugin, detailing how to secure key access using IAM policies, restrict usage by IP address, and implement Multi-Factor Authentication (MFA).
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="hashicorp-key-management-plugin.md" %}
[hashicorp-key-management-plugin.md](hashicorp-key-management-plugin.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Guide to using the HashiCorp Key Management plugin, which integrates MariaDB with HashiCorp Vault for centralized, secure key storage and lifecycle management.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="uninstall-key-management-plugins.md" %}
[uninstall-key-management-plugins.md](uninstall-key-management-plugins.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Final step of removing key management plugins from the configuration once all data and logs have been confirmed as unencrypted.
{% endcolumn %}
{% endcolumns %}
