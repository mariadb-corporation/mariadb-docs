---
description: >-
  Secure MariaDB Server data at rest with encryption. This section details how
  to protect your sensitive information stored on disk, ensuring data
  confidentiality and compliance.
---

# Data-at-Rest Encryption

{% columns %}
{% column %}
{% content-ref url="data-at-rest-encryption-tde-fundamentals.md" %}
[data-at-rest-encryption-tde-fundamentals.md](data-at-rest-encryption-tde-fundamentals.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The fundamentals of MariaDB data-at-rest encryption (Transparent Data Encryption, TDE), which encrypts files on storage.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="managing-binary-log-encryption.md" %}
[managing-binary-log-encryption.md](managing-binary-log-encryption.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to encrypt binary logs and relay logs so on-disk data modifications are only accessible through the server.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="aria-encryption/" %}
[aria-encryption](aria-encryption/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about Aria encryption in MariaDB Server for data at rest. This section details how to encrypt Aria tablespaces, providing enhanced security for your stored data.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-encryption/" %}
[innodb-encryption](innodb-encryption/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about InnoDB encryption for data at rest. This section details how to encrypt InnoDB tablespaces, ensuring strong data security and compliance for your mission-critical applications.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="key-management-and-encryption-plugins/" %}
[key-management-and-encryption-plugins](key-management-and-encryption-plugins/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore key management and encryption plugins for MariaDB Server. This section details how to manage encryption keys and leverage plugins for robust data-at-rest protection.
{% endcolumn %}
{% endcolumns %}
