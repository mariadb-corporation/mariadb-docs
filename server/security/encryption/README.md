---
description: >-
  Enhance MariaDB Server security with encryption. This section covers
  data-at-rest and in-transit encryption, helping you protect sensitive
  information and meet compliance requirements.
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

# Encryption

MariaDB's security architecture distinguishes between data moving across the network (Data-in-Transit) and data stored on disk (Data-at-Rest).

{% columns %}
{% column %}
{% content-ref url="tls-and-cryptography-libraries-used-by-mariadb.md" %}
[tls-and-cryptography-libraries-used-by-mariadb.md](tls-and-cryptography-libraries-used-by-mariadb.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB links to cryptography libraries (OpenSSL, wolfSSL, GnuTLS, Schannel) either statically or dynamically. How to verify the active library and version.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="data-in-transit-encryption/" %}
[data-in-transit-encryption](data-in-transit-encryption/)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
#### Data-in-Transit Encryption

* Protects credentials and query results from "man-in-the-middle" attacks during client-server communication.
* Uses the TLS protocol. It handles the handshake, identity verification, and encryption of the network stream.
* Utilizes Asymmetric Key Pairs (Public/Private keys) and Certificates (PEM/CRT files) managed by libraries like OpenSSL.
* Defined in the `[mariadb]` section using `ssl_cert`, `ssl_key`, and `ssl_ca`.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="data-at-rest-encryption/" %}
[data-at-rest-encryption](data-at-rest-encryption/)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
#### Data-at-Rest Encryption

* Protects physical data files (InnoDB/Aria tables, Redo logs, and Binary logs) if the storage media or backups are stolen.
* Uses Symmetric Encryption (typically AES) managed by specialized Key Management Plugins.
* Uses Symmetric Keys identified by a `Key ID`. These are fetched from a local file, AWS KMS, or HashiCorp Vault.
* Enabled via variables like `innodb_encrypt_tables` and requires a specific plugin (e.g., `file_key_management`) to be loaded.
{% endcolumn %}
{% endcolumns %}



