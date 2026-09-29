---
description: >-
  Create, assign, query, and reload the Default and Named Audit Filters that control what MariaDB Enterprise Audit writes to the audit log.
---

# Enterprise Audit Filters

Filters are JSON objects that specify what you want MariaDB Enterprise Audit to monitor.

There are two types of filters:

| Audit Filter Type                                                        | Description                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Default Audit Filter](#default-audit-filter) | The Default Audit Filter is used for all user accounts that are not assigned a Named Audit Filter. Only a single Default Audit Filter can be defined in the `mysql.server_audit_filters` system table, and it must be defined with the name default.                                                                                                                     |
| [Named Audit Filters](#named-audit-filters)   | Named Audit Filters must be assigned to specific user accounts. Many Named Audit Filters can be defined in the `mysql.server_audit_filters` system table, and they must be defined with unique names. A Named Audit Filter can be assigned to a user account by inserting the user account details and the filter name into the `mysql.server_audit_users` system table. |

## Default Audit Filter

The Default Audit Filter applies to all user accounts that do not have a specific Named Audit Filter assigned. Only one Default Audit Filter is allowed in the `mysql.server_audit_filters` system table, and it must be named `default`.

### Create a Default Audit Filter

If you want to create a Default Audit Filter, you need to insert the details into the `mysql.server_audit_filters` system table. The name for the Default Audit Filter must be default and the rule should be designed to meet your audit logging requirements.

To create a Default Audit Filter:

1. Confirm that a Default Audit Filter does not already exist:

```sql
SELECT * FROM mysql.server_audit_filters
    WHERE filtername = 'default';
```

2. If a Default Audit Filter already exists, remove it:

```sql
DELETE FROM mysql.server_audit_filters
    WHERE filtername = 'default';
```

3. Insert the details for the new Default Audit Filter into the mysql.server\_audit\_filters system table:

```sql
INSERT INTO mysql.server_audit_filters (filtername, rule)
   VALUES ('default',
      JSON_COMPACT(
         '{
            "connect_event":"ALL",
            "table_event":"WRITE"
         }'
      ));
```

This example Audit Filter configures audit logging for all Connection Events and Write Table Events.

The example passes the JSON object to the [JSON\_COMPACT()](../../sql-functions/special-functions/json-functions/json_compact.md) function, so that the JSON object is compacted prior to being inserted into the system table. This step is recommended, but not required.

4. Reload the Audit Filters by setting the server\_audit\_reload\_filters system variable to `ON`:

```sql
SET GLOBAL server_audit_reload_filters=ON;
```

### Disable Logging with the Default Filter

It is recommended to use the default filter to assure that any user is audited, also if not defined in the `mysql.server_audit_users` system table.

In some special cases you might want audits only to be enabled for the users in `mysql.server_audit_users`. In this case you should use the following default filter to disable logging for all other users.

```sql
INSERT INTO mysql.server_audit_filters (filtername, rule)
   VALUES ('default',
      JSON_COMPACT(
         '{
    "logging": "OFF"
            }'
      ));
```

## Named Audit Filters

Named Audit Filters must be assigned to specific user accounts.

Multiple Named Audit Filters can be defined in the mysql.server\_audit\_filters system table, and they must be defined with unique names. A Named Audit Filter can be assigned to a user account by inserting the user account details and the filter name into the mysql.server\_audit\_users system table.

### Create a Named Audit Filter

To create a Named Audit Filter, insert a row with the Audit Filter's name and the rule into the `mysql.server_audit_filters` system table:

```sql
INSERT INTO mysql.server_audit_filters (filtername, rule)
   VALUES ('reporting',
      JSON_COMPACT(
         '{
            "connect_event": [
               "CONNECT",
               "DISCONNECT"
            ],
            "table_event":[
               "WRITE",
               "CREATE",
               "DROP",
               "RENAME",
               "ALTER"
            ]
         }'
      ));
```

This example Audit Filter is defined with the name reporting, and it configures audit logging for Connection Events and Disconnection Events and for several types of Table Events. This example Audit Filter can be useful for read-only users since it does not log table reads, but it does log table writes and schema changes which are illegitimate activities for a read-only user.

The example passes the JSON object to the `JSON_COMPACT`() function, so that the JSON object is compacted prior to being inserted into the system table. This step is recommended, but not required.

For additional information on how to assign the Audit Filter to a user account, see "[Assign a Named Audit Filter](#assign-a-named-audit-filter)".

### Assign a Named Audit Filter

Named Audit Filters are only active when they are assigned to a specific user account.

To assign a Named Audit Filter to a user account:

1. Insert a row with the user account details and the Audit Filter's name into the `mysql.server_audit_users` system table:

```sql
INSERT INTO mysql.server_audit_users (host, user, filtername)
   VALUES ("%", "reader", "reporting");
```

This example statement assigns the reporting Audit Filter created in "[Create a Named Audit Filter](#create-a-named-audit-filter)" to the `reader@%` user account.

2. Reload the Audit Filters by setting the server\_audit\_reload\_filters system variable to `ON`:

```sql
SET GLOBAL server_audit_reload_filters=ON;
```

MariaDB Enterprise Audit does not track changes to user accounts. If you delete or rename a user account, the change doesn't cascade to the Audit Filter. The Audit Filters must be updated manually.

## System Tables for Audit Filters

There are two system tables for Audit Filters:

<table><thead><tr><th width="247">System Table</th><th>Description</th></tr></thead><tbody><tr><td>mysql.server_audit_filters</td><td>Audit Filter definitions with MariaDB Enterprise Audit</td></tr><tr><td>mysql.server_audit_users</td><td>Audit Filter assignments for user accounts with MariaDB Enterprise Audit.</td></tr></tbody></table>

### Query Audit Filters

You can query Audit Filters by querying the `mysql.server_audit_filters` system table.

The JSON objects can be made more human-readable by passing them to the [JSON\_DETAILED()](../../sql-functions/special-functions/json-functions/json_detailed.md) or [JSON\_LOOSE()](../../sql-functions/special-functions/json-functions/json_loose.md) functions:

```sql
SELECT filtername,
   JSON_DETAILED(rule)
FROM mysql.server_audit_filters\G
```

```json
*************************** 1. row ***************************
         filtername: reporting
JSON_DETAILED(rule): {
    "table_event":
    [
        "WRITE",
        "CREATE",
        "DROP",
        "RENAME",
        "ALTER",

        {
            "log_databases":
            [
                "production",
                "reporting"
            ]
        }
    ]
}
```

### Query User Assignments for Named Audit Filters

You can query user assignments for Named Audit Filters by joining the `mysql.server_audit_filters` and `mysql.server_audit_users` system tables.

The JSON objects can be made more human-readable by passing them to the [JSON\_DETAILED()](../../sql-functions/special-functions/json-functions/json_detailed.md) or [JSON\_LOOSE()](../../sql-functions/special-functions/json-functions/json_loose.md) functions:

```sql
SELECT sau.host, sau.user, saf.filtername,
   JSON_DETAILED(saf.rule)
FROM mysql.server_audit_filters saf
JOIN mysql.server_audit_users sau
   ON saf.filtername = sau.filtername
WHERE saf.filtername != 'default'\G
```

{% code expandable="true" %}
```json
*************************** 1. row ***************************
                   host: %
                   user: reader
             filtername: reporting
JSON_DETAILED(saf.rule): {
    "table_event":
    [
        "WRITE",
        "CREATE",
        "DROP",
        "RENAME",
        "ALTER",

        {
            "log_databases":
            [
                "production",
                "reporting"
            ]
        }
    ]
}
*************************** 2. row ***************************
                   host: %
                   user: writer
             filtername: reporting
JSON_DETAILED(saf.rule): {
    "table_event":
    [
        "WRITE",
        "CREATE",
        "DROP",
        "RENAME",
        "ALTER",

        {
            "log_databases":
            [
                "production",
                "reporting"
            ]
        }
    ]
}
```
{% endcode %}

### Reload Audit Filters and Assignments

MariaDB Enterprise Audit caches its Audit Filters to improve performance. When you change an Audit Filter or an Audit Filter assignment in the system tables, you need to reload the Audit Filters for the changes to take effect.

To reload Audit Filters, set the server\_audit\_reload\_filters system variable to ON with the [SET GLOBAL](../../sql-statements/administrative-sql-statements/set-commands/set.md) statement, which requires the SUPER privilege:

```sql
SET GLOBAL server_audit_reload_filters=ON;
```

When you set the server\_audit\_reload\_filters system variable to ON, MariaDB Enterprise Audit reloads all Audit Filters and assignments to ensure that it is using the latest definitions. Afterward, it sets `server_audit_reload_filters` back to `OFF`.

For additional information on how to use the server\_audit\_reload\_filters system variable, see "[Default Audit Filter](#default-audit-filter)" and "[Named Audit Filters](#named-audit-filters)".

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
