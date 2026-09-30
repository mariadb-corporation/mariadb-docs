---
description: >-
  The MariaDB Enterprise Audit plugin logs detailed data access and
  configuration changes, offering advanced filtering to meet security and
  compliance requirements.
---

# MariaDB Enterprise Audit

## Overview

While application design specifications and database configurations may intend specific limitations to be placed around access to data, audit mechanisms help confirm the effectiveness of these controls.

MariaDB Enterprise Audit is a plugin that logs data access and database operations.

Audit mechanisms are most effective when they produce a manageable quantity of output. MariaDB Enterprise Audit includes advanced filtering features to enable narrowly defining which information is logged.

Where audit mechanisms may only be effective when control parameters can also be audited, MariaDB Enterprise Audit implements logging of configuration changes.

{% hint style="danger" %}
**Plugin Conflict (**[MENT-316](https://jira.mariadb.org/browse/MENT-316)**)**

The MariaDB Enterprise Audit plugin (`server_audit2.so`) is incompatible with the older server\_audit.so (`v1`) plugin. Running both can cause server instability or deadlocks.

_If you are a new user: You can continue reading._

_If you are migrating: You must remove the old `v1` plugin. Go directly to_ [_Upgrading to Enterprise Audit_](mariadb-enterprise-audit-upgrades.md) _for complete instructions._
{% endhint %}

## Configuration Overview

MariaDB Enterprise Audit is installed and loaded by default. If you are unsure whether it is loaded on your system, you can [confirm that the plugin is loaded](mariadb-enterprise-audit-installation.md#confirm-the-audit-plugin-is-loaded).

To use MariaDB Enterprise Audit, the plugin must be configured: Administrators must define [Audit Filters](mariadb-enterprise-audit-filters.md) to configure what MariaDB Enterprise Audit writes to the audit log.

MariaDB Enterprise Audit supports two types of Audit Filters:

| Audit Filter Type                                                        | Used For                                                                                         |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| [Default Audit Filter](mariadb-enterprise-audit-filters.md#default-audit-filter) | The Default Audit Filter is used for any user account that is not assigned a Named Audit Filter. |
| [Named Audit Filters](mariadb-enterprise-audit-filters.md#named-audit-filters)   | Named Audit Filters are assigned to specific user accounts.                                      |

Administrators can define Audit Filters to audit log activity using multiple types of filters:

| Filter Type                                                   | Used For                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Event Filters](mariadb-enterprise-audit-filter-types.md#event-filters)    | Event Filters are used to enable or disable audit logging for specific types of operations performed by the user accounts assigned to the Audit Filter.                                                                                                                                                      |
| [Logging Filters](mariadb-enterprise-audit-filter-types.md#logging-filter) | Logging Filters are used to enable or disable audit logging for the user accounts assigned to the Audit Filter.                                                                                                                                                                                              |
| [Object Filters](mariadb-enterprise-audit-filter-types.md#object-filters)  | Object Filters are used to enable or disable audit logging for specific databases or tables accessed by the user accounts assigned to the Audit Filter. Support for Object Filters was added in MariaDB Enterprise Server 10.6. Support for Object Filters was backported to ES 10.4.21-13 and ES 10.5.12-8. |

Administrators must [start audit logging](mariadb-enterprise-audit-installation.md#start-audit-logging).

## General Operation

MariaDB Enterprise Audit performs audit logging during typical operations of MariaDB Enterprise Server:

* When a user connects, fails to connect, or disconnects, MariaDB Enterprise Audit will write a message to the audit log if the Audit Filter specifies the specific type of [Connect Event](mariadb-enterprise-audit-filter-types.md#connection-events).
* When a user executes a query, MariaDB Enterprise Audit will write a message to the audit log if the Audit Filter specifies the specific type of [Query Event](mariadb-enterprise-audit-filter-types.md#query-events) and if the queried objects are not excluded by [Object Filters](mariadb-enterprise-audit-filter-types.md#object-filters).
* When a query accesses a table, MariaDB Enterprise Audit will write a message to the audit log if the Audit Filter specifies the specific type of Table Event and if the table is not excluded by [Object Filters](mariadb-enterprise-audit-filter-types.md#object-filters).
* When a query modifies the MariaDB Enterprise Audit configuration, MariaDB Enterprise Audit will write a message to the audit log if the Audit Filter specifies the [Audit Config Event](mariadb-enterprise-audit-filter-types.md#audit-config-events).
* When a user's [Audit Filter](mariadb-enterprise-audit-filter-types.md#logging-filter) contains a Logging Filter that disables audit logging, all audit logging for the user's activity will be skipped.

MariaDB Enterprise Audit writes audit log messages either to a dedicated [audit log file or to the system log (syslog)](mariadb-enterprise-audit-log-destinations-and-format.md#audit-log-destinations), depending on configuration.

Audit log messages that correspond to a query are logged when the query completes. If a query is executed in a transaction, the audit log messages that correspond to the query are logged when the individual query completes, not when the transaction completes. If the query fails, the audit log message is logged at time of failure.

## Audit Log Considerations

Care must be taken when logging data for audit to maintain alignment to business requirements. Concerns include:

* Queries should not be logged for tables containing Personally Identifiable Information (PII) or Sensitive PII (SPII) such as passwords, since audit log data is written unencrypted. Consider using [Object Filters](mariadb-enterprise-audit-filter-types.md#object-filters) to exclude sensitive information from the audit log.
* Backup of audit data should be performed at least as frequently as database backups.
* Audit log data on database servers could be tampered with if the database server is compromised. Consider secure transmission of log data to a hardened and remote logging server.
* Where audit data is mission-critical, it should be subject to controls, data protection, data retention, and highly-available storage as are used for other mission-critical data.

## In This Section

{% columns %}
{% column %}
{% content-ref url="mariadb-enterprise-audit-installation.md" %}
[mariadb-enterprise-audit-installation.md](mariadb-enterprise-audit-installation.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Verify and load the MariaDB Enterprise Audit plugin, start audit logging, forbid its uninstallation, and understand its server startup behavior.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-enterprise-audit-filters.md" %}
[mariadb-enterprise-audit-filters.md](mariadb-enterprise-audit-filters.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Create, assign, query, and reload the Default and Named Audit Filters that control what MariaDB Enterprise Audit writes to the audit log.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-enterprise-audit-filter-types.md" %}
[mariadb-enterprise-audit-filter-types.md](mariadb-enterprise-audit-filter-types.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Reference for the Event Filters, Logging Filter, and Object Filters that make up a MariaDB Enterprise Audit filter rule, with examples.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-enterprise-audit-log-destinations-and-format.md" %}
[mariadb-enterprise-audit-log-destinations-and-format.md](mariadb-enterprise-audit-log-destinations-and-format.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Send MariaDB Enterprise Audit output to a file or to syslog, configure log path and rotation, and parse the audit log record format.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-enterprise-audit-error-log-messages.md" %}
[mariadb-enterprise-audit-error-log-messages.md](mariadb-enterprise-audit-error-log-messages.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Messages that MariaDB Enterprise Audit writes to the MariaDB error log when it loads, starts or stops logging, or rejects invalid filters.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-enterprise-audit-upgrades.md" %}
[mariadb-enterprise-audit-upgrades.md](mariadb-enterprise-audit-upgrades.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Uninstall the v1 MariaDB Audit Plugin and migrate its settings, filters, and user lists to MariaDB Enterprise Audit (v2).
{% endcolumn %}
{% endcolumns %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
