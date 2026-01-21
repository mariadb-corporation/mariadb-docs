---
description: >-
  Explore the supported authentication methods in MariaDB MaxScale. Learn how
  authenticators validate clients and backend servers using plugins like Native,
  PAM, GSSAPI, etc.
---

# MaxScale Authentication

## Overview

In MariaDB MaxScale, authenticators perform the following tasks:

* Authenticating clients that connect to MaxScale
* Authenticating connections to back-end MariaDB Enterprise Server and MariaDB Xpand nodes
* Deciding how authentication should be performed

## Authenticators Supported by MaxScale

* [GSSAPI Authenticator](../../reference/maxscale-authenticators/maxscale-gssapi-client-authenticator.md)
* [Native Authenticator](../../reference/maxscale-authenticators/maxscale-mariadb-mysql-authenticator.md)
* [PAM Authenticator](../../reference/maxscale-authenticators/maxscale-pam-authenticator.md)
* [PARSEC Authenticator](../../reference/maxscale-authenticators/maxscale-parsec-authenticator.md)
* [ed25519 Authenticator](../../reference/maxscale-authenticators/maxscale-ed25519-authenticator.md)
