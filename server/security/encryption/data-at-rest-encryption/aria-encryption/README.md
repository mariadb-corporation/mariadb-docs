---
description: >-
  Learn about Aria encryption in MariaDB Server for data at rest. This section
  details how to encrypt Aria tablespaces, providing enhanced security for your
  stored data.
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

# Aria Encryption

{% columns %}
{% column %}
{% content-ref url="aria-encryption-overview.md" %}
[aria-encryption-overview.md](aria-encryption-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Introduction to encrypting Aria tables, covering the necessary system variables (aria_encrypt_tables, encrypt_tmp_disk_tables) and how to verify encryption status by inspecting data files.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="aria-enabling-encryption.md" %}
[aria-enabling-encryption.md](aria-enabling-encryption.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Step-by-step guide to enabling encryption for user-created and internal temporary Aria tables, including the requirement to manually rebuild existing tables using ALTER TABLE.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="aria-encryption-keys.md" %}
[aria-encryption-keys.md](aria-encryption-keys.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Details how Aria manages encryption keys (using ID 1 for user tables and ID 2 for temporary tables) and notes limitations regarding key rotation and per-table key assignment.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="aria-disabling-encryption.md" %}
[aria-disabling-encryption.md](aria-disabling-encryption.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Instructions for safely disabling encryption on Aria tables, emphasizing the need to rebuild tables to an unencrypted state before removing key management plugins.
{% endcolumn %}
{% endcolumns %}
