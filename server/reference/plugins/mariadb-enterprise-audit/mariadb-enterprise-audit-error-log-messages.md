---
description: >-
  Messages that MariaDB Enterprise Audit writes to the MariaDB error log when it loads, starts or stops logging, or rejects invalid filters.
---

# Enterprise Audit Error Log Messages

MariaDB Enterprise Audit writes messages to the MariaDB Error Log in various scenarios. Some of the scenarios and log messages are described below.

## Load Plugin

When MariaDB Enterprise Server loads the plugin for MariaDB Enterprise Audit, MariaDB Enterprise Audit writes the following message in the MariaDB error log:

```
2021-08-03 21:07:03 server_audit: MariaDB Audit Plugin version 2.0.3 STARTED.
```

For additional information, see "[Load the Audit Plugin](mariadb-enterprise-audit-installation.md#load-the-audit-plugin)".

## Unload Plugin

When MariaDB Enterprise Server unloads the plugin for MariaDB Enterprise Audit, MariaDB Enterprise Audit writes the following message in the MariaDB error log:

```
2021-08-02 23:54:59 server_audit: STOPPED
```

The plugin is unloaded when MariaDB Enterprise Server is shutdown, so this message is most commonly written to the MariaDB error log during the shutdown process.

## Start Audit Logging to File

When audit logging is started and it is directed to a file, MariaDB Enterprise Audit writes the following message in the MariaDB error log:

{% code overflow="wrap" %}
```log
2021-08-03 21:39:42 server_audit: logging started to the file server_audit.log.
```
{% endcode %}

If a custom [audit log path](mariadb-enterprise-audit-log-destinations-and-format.md#audit-log-path) is configured, then the message will refer to the custom path.

For additional information, see "[Start Audit Logging](mariadb-enterprise-audit-installation.md#start-audit-logging)" and "[Audit Logging to File](mariadb-enterprise-audit-log-destinations-and-format.md#audit-logging-to-file)".

## Start Audit Logging to Syslog

When audit logging is started and it is directed to syslog, MariaDB Enterprise Audit writes the following message in the MariaDB error log:

```log
2021-08-03 22:02:45 server_audit: logging started to the syslog.
```

For additional information, see "[Start Audit Logging](mariadb-enterprise-audit-installation.md#start-audit-logging)" and "[Audit Logging to Syslog](mariadb-enterprise-audit-log-destinations-and-format.md#audit-logging-to-system-log)".

## Stop Audit Logging

When audit logging is stopped, MariaDB Enterprise Audit writes the following message in the MariaDB error log:

```log
2021-08-03 21:39:50 server_audit: logging was stopped.
```

## Change Audit Logging to File

When audit logging is changed to a file, MariaDB Enterprise Audit writes the following message in the MariaDB error log:

```log
2021-08-03 22:03:31 server_audit: Output was redirected to 'file'
```

For additional information, see "[Audit Logging to File](mariadb-enterprise-audit-log-destinations-and-format.md#audit-logging-to-file)".

## Change Audit Logging to Syslog

When audit logging is changed to syslog, MariaDB Enterprise Audit writes the following message in the MariaDB error log:

```log
2021-08-03 22:01:22 server_audit: Output was redirected to 'syslog'
```

For additional information, see [Audit Logging to System Log](mariadb-enterprise-audit-log-destinations-and-format.md#audit-logging-to-system-log).

## Change File Name for Audit Logging

When the file name for audit logging is changed, MariaDB Enterprise Audit writes the following message in the MariaDB error log:

```log
2021-08-03 22:05:17 server_audit: Log file name was changed to 'mariadb-enterprise-audit.log'.
```

For additional information, see "[Audit Log Path](mariadb-enterprise-audit-log-destinations-and-format.md#audit-log-path)".

## Reload Invalid Audit Filters

When the Audit Filters are reloaded and one or more of the Audit Filters are invalid, MariaDB Enterprise Audit writes the following message in the MariaDB error log:

```sql
2021-08-03 21:51:55 server_audit: Unknown filter function tables.
2021-08-03 21:51:55 server_audit: Can't parse filter's 'production' definition { "tables": "production.*" }.
2021-08-03 21:51:55 server_audit: can't load filters - old filters are saved.
```

For additional information, see "[Reload Audit Filters and Assignments](mariadb-enterprise-audit-filters.md#reload-audit-filters-and-assignments)".

## Conflict with the Query Cache

If the query cache is enabled, `READ` Table Events may not be audit logged. If MariaDB Enterprise Audit detects during startup that the query cache is enabled, MariaDB Enterprise Audit writes the following message to the MariaDB error log:

```log
2021-08-03 21:07:03 server_audit: Query cache is enabled with the TABLE events. Some table reads can be veiled.
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
