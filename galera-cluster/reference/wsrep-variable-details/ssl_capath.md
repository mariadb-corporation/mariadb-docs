---
description: >-
  ssl_capath sets the server-side path to a directory of SSL Certificate
  Authority files used by MariaDB Server, including for Galera TLS when
  wsrep_ssl_mode is SERVER or SERVER_X509.
---

# ssl\_capath

## Overview <a href="#overview_h2" id="overview_h2"></a>

CA directory (check OpenSSL docs, implies --ssl).

## Details

### Parameters

| Command-line          | --ssl\_capath=arg      |
| --------------------- | ---------------------- |
| Configuration file    | Supported              |
| Dynamic               | No                     |
| Scope                 | Global                 |
| Data Type             | VARCHAR                |
| Product Default Value | "" _(an empty string)_ |
