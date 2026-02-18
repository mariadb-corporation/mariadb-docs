---
description: >-
  Secure MariaDB Server data in transit with encryption. This section covers
  configuring SSL/TLS to protect communication between clients and the database,
  ensuring confidentiality and integrity.
---

# Data-in-Transit Encryption

Protect your data as it moves across the network with Data-in-Transit Encryption. By leveraging the TLS (Transport Layer Security) protocol, MariaDB ensures that credentials, queries, and result sets are encrypted between the client and server. This prevents "man-in-the-middle" attacks and unauthorized eavesdropping on sensitive information.

This guide covers the essentials of securing your network traffic—from configuring SSL certificates and private keys to enforcing secure connections for all users. Secure your communications layer to maintain data integrity and confidentiality in any environment.

{% columns %}
{% column %}
{% content-ref url="secure-connections-overview.md" %}
[secure-connections-overview.md](secure-connections-overview.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Conceptual overview of data-in-transit encryption in MariaDB, discussing supported TLS libraries (OpenSSL, wolfSSL), protocol versions (`tls_version`), and certificate verification.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="securing-connections-for-client-and-server.md" %}
[securing-connections-for-client-and-server.md](securing-connections-for-client-and-server.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Complete MariaDB security guide. Complete resource for user management, access control, SSL/TLS encryption, and audit policies with comprehensive examples.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="replication-with-secure-connections.md" %}
[replication-with-secure-connections.md](replication-with-secure-connections.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
A guide to securing replication traffic between primary and replica servers, covering the use of `CHANGE MASTER TO` options (e.g., `MASTER_SSL`) and mutual authentication.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="data-in-transit-encryption-enabling-tls-on-mariadb-server.md" %}
[data-in-transit-encryption-enabling-tls-on-mariadb-server.md](data-in-transit-encryption-enabling-tls-on-mariadb-server.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Step-by-step instructions for configuring MariaDB Server to use TLS by setting system variables like `ssl_cert`, `ssl_key`, and `ssl_ca` in the configuration file.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="certificate-creation-with-openssl.md" %}
[certificate-creation-with-openssl.md](certificate-creation-with-openssl.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Complete OpenSSL TLS certificate guide: generate CA key/cert and server key/CSR, sign X509 with openssl x509 -CA/-CAkey, and verify certificates.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="ssltls-system-variables.md" %}
[ssltls-system-variables.md](ssltls-system-variables.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Reference list of system variables related to TLS configuration, such as `ssl_cipher`, `ssl_crl`, and `have_ssl`, used to manage and monitor encryption settings.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="using-tlsv13.md" %}
[using-tlsv13.md](using-tlsv13.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}

{% endcolumn %}
{% endcolumns %}
