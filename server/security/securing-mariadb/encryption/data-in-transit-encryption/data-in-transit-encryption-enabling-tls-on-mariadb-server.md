---
description: >-
  Step-by-step instructions for configuring MariaDB Server to use TLS by setting
  system variables like ssl_cert, ssl_key, and ssl_ca in the configuration file.
---

# Enabling TLS on MariaDB Server

## Overview

MariaDB Server supports data-in-transit encryption, which secures data transmitted over the network. The server and the clients encrypt data using the Transport Layer Security (TLS) protocol, which is a newer version of the Secure Socket Layer (SSL) protocol.

TLS must be manually enabled on the server, which is what this page describes.

## Enabling TLS

{% stepper %}
{% step %}
### Acquire an X509 certificate and a private key for the server.

If it is a test or development server, self-signed certificates and keys should be sufficient.
{% endstep %}

{% step %}
### Determine which system variables and  you need to configure.

Mandatory [system variables and options](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md) for TLS include:

| System Variable/Option                           | Description             |
| ------------------------------------------------ | ----------------------- |
| [ssl\_cert](ssltls-system-variables.md#ssl_cert) | X509 cert in PEM format |
| [ssl\_key](ssltls-system-variables.md#ssl_key)   | X509 key in PEM format  |
| [ssl\_ca](ssltls-system-variables.md#ssl_ca)     | JCA file in PEM format  |

Other useful system variables and options for TLS include:

| System Variable/Option                                                                                                                                    | Description                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [require\_secure\_transport](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#require_secure_transport) | When this option is enabled, connections attempted using insecure transport are rejected. Secure transports are SSL/TLS, Unix sockets, and named pipes. |
| [ssl\_capath](ssltls-system-variables.md#ssl_capath)                                                                                                      | CA directory                                                                                                                                            |
| [ssl\_cipher](ssltls-system-variables.md#ssl_cipher)                                                                                                      | SSL cipher to use                                                                                                                                       |
| [ssl\_crl](ssltls-system-variables.md#ssl_crl)                                                                                                            | CRL file in PEM format                                                                                                                                  |
| [ssl\_crlpath](ssltls-system-variables.md#ssl_crlpath)                                                                                                    | CRL directory                                                                                                                                           |
| [tls\_version](ssltls-system-variables.md#tls_version)                                                                                                    | TLS protocol version for secure connections                                                                                                             |
{% endstep %}

{% step %}
### Choose a configuration file in which to configure your system variables and options.

It is not recommended to make changes to one of the bundled configuration files. Instead, we recommend to [create a custom configuration file](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#including-option-files) in one of the directories included by the main configuration file (for instance, my.cnf). Configuration files in included directories are read in alphabetical order. If you want your custom configuration file to override the bundled configuration files, it is a good idea to prefix the custom configuration file's name with a string that will be sorted last, such as `z-`. Examples:

* RHEL, CentOS, Rocky Linux, and SLES: `/etc/my.cnf.d/z-custom-my.cnf`
* Debian and Ubuntu: `/etc/mysql/mariadb.conf.d/z-custom-my.cnf`&#x20;
* macOS: `/opt/homebrew/etc/z-custom-my.cnf`
{% endstep %}

{% step %}
### Set your system variables and options in the configuration file.

They need to be set in a group that is read by [MariaDB Server](https://github.com/mariadb-corporation/docs-server/blob/test/en/mariadb-enterprise-server/README.md), such as `[mariadb]` , `[server]`, or `[client-server]`:

```ini
[mariadb]
ssl_cert = /certs/server-cert.pem
ssl_key = /certs/server-key.pem
ssl_ca = /certs/ca-cert.pem
```
{% endstep %}

{% step %}
### Restart the server.

On most Linux systems, run this command:

```bash
sudo systemctl restart mariadb
```

On macOS, run this command:

```bash
brew services restart mariadb
```
{% endstep %}

{% step %}
### Connect to the server.

Start a client like [mariadb](../../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) (see [this page](../../../../mariadb-quickstart-guides/mariadb-connecting-guide.md) for connection options):

```bash
$ sudo mariadb
```
{% endstep %}

{% step %}
### Verify that TLS is enabled.

```sql
SHOW GLOBAL VARIABLES LIKE 'have_ssl';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| have_ssl      | YES   |
+---------------+-------+
```
{% endstep %}
{% endstepper %}

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
