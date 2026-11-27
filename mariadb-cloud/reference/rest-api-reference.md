---
description: >-
  MariaDB Cloud REST API reference: service provisioning, pricing/billing,
  configuration, user management, backup/restore scheduling, and lifecycle
  operations via swagger docs.
---

# MariaDB Cloud REST API Reference

The easiest way to get started with the API is to use [this swagger Docs](https://apidocs.skysql.com). Just [generate your API key](../security/managing-api-keys.md) , Click `Authorize` and enter `<yourAPI Key>` and try out any of the APIs.

You can use the REST API to Provision, get pricing and billing information, fetch/change service or MariaDB configuration, Manage users and their roles, schedule backups or restores, scale, stop and Delete services.

Please refer to the [API docs](https://apidocs.skysql.com) for examples and a complete list of all the APIs.

The Backup Service API is included in the [MariaDB Cloud API Reference Guide](mariadb-cloud-api-reference-guide/README.md), under the `/skybackup/v1/` endpoints.

## Blocked User-Agent Strings

Requests to the API pass through Cloudflare, which blocks clients that send certain default bot `User-Agent` strings before the request reaches the API gateway. Requests with a `User-Agent` header that starts with `Python-urllib/` (the Python `urllib` default) or `libwww-perl` (the Perl `LWP` default) return HTTP `403` with error code `1010`.

To avoid the error, set a different `User-Agent` header in your requests, or use an HTTP client that sends its own, such as `curl` or the Python `requests` library.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
