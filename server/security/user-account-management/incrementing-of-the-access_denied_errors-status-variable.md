---
description: >-
  Describes the conditions that trigger the `access_denied_errors` status
  variable, such as failed logins, invalid privileges, or missing SSL
  requirements, aiding in security monitoring.
---

# Incrementing of the access\_denied\_errors Status Variable

The [access\_denied\_errors](../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#access_denied_errors) status variable is incremented when someone tries to access something they do not have rights to.

This happens in the following cases:

* When accessing a database, table, or column that the user does not have rights to access. The error is sent to the client.
* When a login fails because of the wrong user/password, etc. The error is printed to the general log.
* When the require\_secure\_transport option is enabled on the server, and the user has not used a secure transport. The error is sent to the client.
* Users try to change to a database/schema they do not have access to. A warning is written to the error log if log\_warnings > 1.
* Users try to use a `SHOW` command to access an object they do not have rights to see. The error is sent to the client.
* Users access something that requires global access, like "CREATE SERVER". The error is sent to the client.

Login failures can be found in the [general log](../../server-management/server-monitoring-logs/general-query-log.md). Errors that are sent to the client can be found by using the [SQL Error Log Plugin](../../server-management/server-monitoring-logs/sql-error-log-plugin.md). The plugin captures all errors sent to the client. Starting from [MariaDB 10.11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-5-release-notes), it can also optionally capture all warnings sent to the client.

### See Also

* [Troubleshooting Connection Issues](../../mariadb-quickstart-guides/mariadb-connection-troubleshooting-guide.md)
* [GRANT](../../reference/sql-statements/account-management-sql-statements/grant.md)
* [Error 1045: Access denied for user (using password)](../../reference/error-codes/mariadb-error-codes-1000-to-1099/e1045.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
