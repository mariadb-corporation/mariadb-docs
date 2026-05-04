---
description: >-
  ssl_key sets the server-side path to the X509 SSL private key in PEM format
  used by MariaDB Server, including for Galera TLS when wsrep_ssl_mode is
  SERVER or SERVER_X509.
---

# ssl\_key

## Overview <a href="#overview_h2" id="overview_h2"></a>

X509 key in PEM format (implies --ssl).

## Details

### Parameters

| Command-line          | --ssl\_key=arg         |
| --------------------- | ---------------------- |
| Configuration file    | Supported              |
| Dynamic               | No                     |
| Scope                 | Global                 |
| Data Type             | VARCHAR                |
| Product Default Value | "" _(an empty string)_ |
