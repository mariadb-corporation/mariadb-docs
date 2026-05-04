---
description: >-
  ssl_ca sets the server-side path to the SSL Certificate Authority file in
  PEM format used by MariaDB Server, including for Galera TLS when
  wsrep_ssl_mode is SERVER or SERVER_X509.
---

# ssl\_ca

## Overview <a href="#overview_h2" id="overview_h2"></a>

CA file in PEM format (check OpenSSL docs, implies --ssl).

## Details

### Parameters

| Command-line          | --ssl\_ca=arg          |
| --------------------- | ---------------------- |
| Configuration file    | Supported              |
| Dynamic               | No                     |
| Scope                 | Global                 |
| Data Type             | VARCHAR                |
| Product Default Value | "" _(an empty string)_ |
