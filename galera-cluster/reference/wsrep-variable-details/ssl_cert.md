---
description: >-
  ssl_cert sets the server-side path to the X509 SSL certificate in PEM format
  used by MariaDB Server, including for Galera TLS when wsrep_ssl_mode is
  SERVER or SERVER_X509.
---

# ssl\_cert

## Overview <a href="#overview_h2" id="overview_h2"></a>

X509 cert in PEM format (implies --ssl).

## Details

### Parameters

| Command-line          | --ssl\_cert=arg        |
| --------------------- | ---------------------- |
| Configuration file    | Supported              |
| Dynamic               | No                     |
| Scope                 | Global                 |
| Data Type             | VARCHAR                |
| Product Default Value | "" _(an empty string)_ |
