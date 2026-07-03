---
description: >-
  Learn about InnoDB encryption for data at rest. This section details how to
  encrypt InnoDB tablespaces, ensuring strong data security and compliance for
  your mission-critical applications.
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

# InnoDB Encryption

{% columns %}
{% column %}
{% content-ref url="innodb-encryption-overview.md" %}
[innodb-encryption-overview.md](innodb-encryption-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Introduction to InnoDB's encryption architecture, explaining how data is encrypted/decrypted during disk I/O, the role of the buffer pool (where data is unencrypted), and how to verify encryption stat
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-enabling-encryption.md" %}
[innodb-enabling-encryption.md](innodb-enabling-encryption.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Step-by-step guide to enabling encryption for InnoDB, covering the configuration of innodb_encrypt_tables for automatic encryption and the use of ENCRYPTED=YES table options for per-table encryption.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-encryption-keys.md" %}
[innodb-encryption-keys.md](innodb-encryption-keys.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How InnoDB manages encryption keys using 32-bit integer IDs, including the default key ID (innodb_default_encryption_key_id), assigning specific keys to tables, and the process of key rotation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="disabling-innodb-encryption.md" %}
[disabling-innodb-encryption.md](disabling-innodb-encryption.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Instructions for safely disabling encryption on InnoDB tables, emphasizing the critical need to decrypt all tablespaces and redo logs using background threads or ALTER TABLE.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-background-encryption-threads.md" %}
[innodb-background-encryption-threads.md](innodb-background-encryption-threads.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Details the operation of background threads (configured via innodb_encryption_threads) which handle key rotation, and the encryption/decryption of tablespaces when global settings.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-encryption-troubleshooting.md" %}
[innodb-encryption-troubleshooting.md](innodb-encryption-troubleshooting.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Solutions for common issues such as Error 1005 (Wrong create options) when configuring encryption, and handling cases where encryption key IDs are set for unencrypted tables.
{% endcolumn %}
{% endcolumns %}
