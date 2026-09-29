---
description: >-
  Reference for the Event Filters, Logging Filter, and Object Filters that make up a MariaDB Enterprise Audit filter rule, with examples.
---

# Enterprise Audit Filter Types

## Event Filters

MariaDB Enterprise Audit supports Event Filters in Audit Filters. Event Filters can be used to configure which Events you want to audit. Each Event refers to a different class of operation.

MariaDB Enterprise Audit defines multiple Event classes that can be used in Event Filters:

* [Audit Config Events](#audit-config-events)
* [Connect Events](#connection-events)
* [Query Events](#query-events)
* [Table Events](#table-events)

The Event classes are described in the sections below. Example audit logs for each Event class are shown in the sections below. For details about the audit log format, see [Audit Log Format](mariadb-enterprise-audit-log-destinations-and-format.md#audit-log-format).

### Audit Config Events

MariaDB Enterprise Audit implements Audit Config Events to help keep track of changes to the audit log configuration.

MariaDB Enterprise Audit logs Audit Config (`AUDIT_CONFIG`) Events in the following situations:

* When one of MariaDB Enterprise Audit's system variables is changed with the [SET GLOBAL](../../sql-statements/administrative-sql-statements/set-commands/set.md) statement, the change is logged.
* When the audit log file is rotated, it is logged.

In the following output, three audit configuration events (`AUDIT_CONFIG`) and one query event (`QUERY`) are shown:

```
20190622 02:10:21,localhost.localdomain,,,0,0,AUDIT_CONFIG,,file_path=server_audit.log,0
20190622 02:10:21,localhost.localdomain,,,0,0,AUDIT_CONFIG,,rotate_size=1000000,0
20190622 02:10:21,localhost.localdomain,,,0,0,AUDIT_CONFIG,,file_rotations=9,0
20190622 02:10:21,localhost.localdomain,root,localhost,8,7,QUERY,mysql,'set global server_audit_logging = on',0
```

{% hint style="success" %}
`AUDIT_CONFIG` events are always logged, so no configuration is required when [audit logging](mariadb-enterprise-audit-installation.md#start-audit-logging) is started.
{% endhint %}

### Connection Events

MariaDB Enterprise Audit implements Connection Events to audit connection attempts, authentication failures, and user account changes that occur due to certain authentication plugins, such as pam.

MariaDB Enterprise Audit logs Connection Events in the following situations:

* When a user successfully connects, it is logged with the `CONNECT` Event sub-class.
* When a user disconnects, it is logged with the `DISCONNECT` Event sub-class.
* When a user fails to connect, it is logged with the `FAILED_CONNECT` Event sub-class.
* When an existing connection authenticates as a different user, it is logged with the `CHANGE_USER` Event sub-class.
* When an authentication plugin changes to a proxy user, it is logged with the `PROXY_CONNECT` Event sub-class.

In the following output, multiple sub-classes of connection events (`CONNECT`, `DISCONNECT`, `FAILED_CONNECT`) are shown:

```sql
20190710 00:05:30,localhost.localdomain,root, localhost,2,0,CONNECT,,,0
20190710 00:05:53,localhost.localdomain,root, localhost,2,0,DISCONNECT,,,0
20190710 00:06:28,localhost.localdomain,unknownuser,localhost,3,0,FAILED_CONNECT,,,1045
20190710 00:06:28,localhost.localdomain,unknownuser, localhost,3,0,DISCONNECT,,,0
```

Starting with MariaDB Enterprise Server 12.3, connection events record the client port alongside the host and append the negotiated TLS version:

```
20260731 09:14:22,mdbe123,root,192.168.1.24:54312,7,0,CONNECT,mysql,,0,TLSv1.3
20260731 09:14:59,mdbe123,root,192.168.1.24:54312,7,0,DISCONNECT,mysql,,0,TLSv1.3
20260731 09:15:03,mdbe123,app,localhost:unavailable,8,0,CONNECT,,,0,
```

The third record is an unencrypted Unix socket connection, so it has no client port and no TLS version.

{% hint style="info" %}
`PROXY_CONNECT` records do not include the TLS version.
{% endhint %}

An **event filter for connection events** can be added to an Audit filter with the `connect_event` key, which supports the following values:

| Value           | Description                                                                                                                                    |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| CONNECT         | Records when the user connects to MariaDB Enterprise Server                                                                                    |
| DISCONNECT      | Records when the user disconnects from MariaDB Enterprise Server                                                                               |
| FAILED\_CONNECT | Records when a user attempts to connect to MariaDB Enterprise Server, but the connection attempt fails due to authentication or similar issues |
| CHANGE\_USER    | Records when a user switches to a different user account                                                                                       |
| PROXY\_CONNECT  | Records proxy user connections.                                                                                                                |
| ALL             | Records all connection Events                                                                                                                  |

This query defines a [Named Audit Filter](mariadb-enterprise-audit-filters.md#named-audit-filters) that specifies connection events:

```sql
INSERT INTO mysql.server_audit_filters (filtername, rule)
   VALUES ('connections',
      JSON_COMPACT(
         '{
            "connect_event": [
               "CONNECT",
               "DISCONNECT"
            ]
         }'
      ));
```

The example passes the JSON object to the [JSON\_COMPACT()](../../sql-functions/special-functions/json-functions/json_compact.md) function, so that the JSON object is compacted prior to being inserted into the system table. This step is recommended, but not required.

### Query Events

MariaDB Enterprise Audit implements Query Events to audit the execution of a specific subset of SQL statements.

MariaDB Enterprise Audit logs Query Events in the following situations:

* When a SQL statement is directly executed, it is logged with the `QUERY` event.

MariaDB Enterprise Audit does not log query events for SQL statements that are indirectly executed. For example, if an SQL statement is executed as part of a view, stored procedure, stored function, or trigger, the query will not be logged. If you want to audit all table accesses, including indirect table accesses, it is recommended to enable audit logging for [Table Events](#table-events) in addition to query events.

This query shows one query event:

```sql
20190710 02:21:07,localhost.localdomain,John,localhost,3,30,QUERY,db1,'SELECT * FROM services WHERE typeid IN (SELECT id FROM services_types WHERE name="consulting")',0
```

An **event filter for query events** can be added to an Audit Filter with the `query_event` key, which supports the following values:

| Value           | Description                                                                                                                                               |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DML             | Records any SQL statements in the Data Manipulation Language subset, including SELECT, INSERT, UPDATE, and DELETE statements.                             |
| DDL             | Records any SQL statements in the Data Definition Language subset, including CREATE TABLE and ALTER TABLE, as well as DROP TABLE and TRUNCATE operations. |
| DCL             | Records any SQL statements in the Data Control Language subset, including GRANT and REVOKE.                                                               |
| DML\_READ       | Records SELECT statements in the Data Manipulation Language subset.                                                                                       |
| DML\_WRITE      | Records any SQL statements for writes in the Data Manipulation Language subset, including INSERT, UPDATE, and DELETE statements.                          |
| DML\_NO\_SELECT | Alias for DML\_WRITE                                                                                                                                      |
| ALL             | Records any SQL statements run by the user.                                                                                                               |

For example, the following query defines a [Named Audit Filter](mariadb-enterprise-audit-filters.md#named-audit-filters) that specifies Query Events:

```sql
INSERT INTO mysql.server_audit_filters (filtername, rule)
   VALUES (
       'queries',
       JSON_COMPACT(
          '{
              "query_event": [
                  "DML",
                  "DDL",
		  "DCL",
		  "DML_NO_SELECT",
		  "DML_WRITE",
		  "DML_READ",
		  "ALL"
              ]
          }'
       )
    );
```

The example passes the JSON object to the [JSON\_COMPACT()](../../sql-functions/special-functions/json-functions/json_compact.md) function, so that the JSON object is compacted prior to being inserted into the system table. This step is recommended, but not required.

{% tabs %}
{% tab title="Current" %}
{% hint style="info" %}
From MariaDB 10.6 / 10.5.12 / 10.4.21:
{% endhint %}

MariaDB Enterprise Audit supports [Object Filters](#object-filters) for Query Events.
{% endtab %}

{% tab title="< 10.6 / 10.5.12 / 10.4.21" %}
{% hint style="info" %}
Before MariaDB 10.6 / 10.5.12 / 10.4.21:
{% endhint %}

MariaDB Enterprise Audit does **not** support [Object Filters](#object-filters) for Query Events.
{% endtab %}
{% endtabs %}

### Table Events

MariaDB Enterprise Audit implements Table Events to audit when a table is accessed or modified.

MariaDB Enterprise Audit logs Table Events in the following situations:

* When an operation reads from a table, it is logged with the `READ` Event sub-class.
* When an operation writes to a table, it is logged with the `WRITE` Event sub-class.
* When an operation creates a table, it is logged with the `CREATE` Event sub-class.
* When an operation drops a table, it is logged with the `DROP` Event sub-class.
* When an operation alters a table, it is logged with the `ALTER` Event sub-class.
* When an operation renames a table, it is logged with the `RENAME` Event sub-class.

Table Events are logged when a table is accessed or modified directly or indirectly by a query. They complement Query Events very well, because the [Query Event](#query-events) causes the raw query to be audit logged, and the Table Event causes all table operations to be audit logged. Both Query Events and Table Events are logged with the query ID, so each Table Event can easily be mapped to its corresponding Query Event. The combination of Query Events and Table Events can be useful when table operations can be hidden by views or triggers.

In the following example output, 6 sub-classes of Table Events are shown:

```sql
20190710 02:21:06,localhost.localdomain,John,localhost,3,25,CREATE,db1,services,
20190710 02:21:06,localhost.localdomain,John,localhost,3,27,READ,db1,services,
20190710 02:21:07,localhost.localdomain,John,localhost,3,29,WRITE,db1,services,
20190710 02:21:27,localhost.localdomain,John,localhost,3,35,ALTER,db1,services,
20190710 02:21:27,localhost.localdomain,John,localhost,3,36,RENAME,db1,services,db1,services_new
20190710 02:21:45,localhost.localdomain,John,localhost,3,38,DROP,db1,services_new,
```

When a query uses the `DELAYED` keyword, it is executed by a system user. In this case, any Table Event associated with the query is written to the audit log with the user set to `DELAYED`. However, the Query Event associated with the query is written to the audit log with the original user:

```sql
20190622 02:10:21,localhost.localdomain,root,localhost,8,5,QUERY,test,'INSERT DELAYED INTO t1 VALUES(1),(2),(3);',0
20190622 02:10:25,localhost.localdomain,root,localhost,2,2,WRITE,test,t1,
20190622 02:10:25,localhost,DELAYED,localhost,2,2,WRITE,test,t1,
```

When your application executes queries with the `DELAYED` keyword, it is recommended to enable audit logging for Query Events in addition to Table Events to ensure that the full details are logged.

If the query cache is enabled, `READ` Table Events may not be audit logged. If MariaDB Enterprise Audit detects that the query cache is enabled during startup, MariaDB Enterprise Audit writes the following message to the MariaDB error log:

```sql
2021-07-23  0:11:26 server_audit: Query cache is enabled with the TABLE events. Some table reads can be veiled.
```

An Event Filter for Table Events can be added to an Audit Filter with the `table_event` key, which supports the following values:

| Value  | Description                                                                                             |
| ------ | ------------------------------------------------------------------------------------------------------- |
| READ   | Records read operations run on table objects, such as from a `SELECT` statement or an `INSERT SELECT`   |
| WRITE  | Records write operations run on table objects, such as `INSERT` or `UPDATE` statements                  |
| CREATE | Records any creation operations run on table objects, such as from a `CREATE TABLE` or `CREATE SERVER`. |
| DROP   | Records any deletion operations run on table objects, such as `DELETE` or `DROP TABLE`.                 |
| ALTER  | Records any modifications made on table objects, such as `ALTER TABLE` or `ALTER USER`.                 |
| RENAME | Records any renaming operations run on table objects, such as `RENAME TABLE`                            |
| ALL    | Records all operations run on table objects                                                             |

For example, the following query defines a [Named Audit Filter](mariadb-enterprise-audit-filters.md#named-audit-filters) that specifies Table Events:

```sql
INSERT INTO mysql.server_audit_filters (filtername, rule)
   VALUES (
       'tables',
       JSON_COMPACT(
           '{
              "table_event": [
                  "WRITE",
                  "CREATE",
                  "DROP",
                  "RENAME",
                  "ALTER"
              ]
           }'
       )
    );
```

The example passes the JSON object to the [JSON\_COMPACT()](../../sql-functions/special-functions/json-functions/json_compact.md) function, so that the JSON object is compacted prior to being inserted into the system table. This step is recommended, but not required.

{% tabs %}
{% tab title="Current" %}
{% hint style="info" %}
From MariaDB 10.6 / 10.5.12 / 10.4.21:
{% endhint %}

MariaDB Enterprise Audit supports [Object Filters](#object-filters) for Table Events.
{% endtab %}

{% tab title="< 10.6 / 10.5.12 / 10.4.21" %}
{% hint style="info" %}
Before MariaDB 10.6 / 10.5.12 / 10.4.21:
{% endhint %}

MariaDB Enterprise Audit does **not** support [Object Filters](#object-filters) for Table Events.
{% endtab %}
{% endtabs %}

## Logging Filter

MariaDB Enterprise Audit supports a special Logging Filter that can be used in Audit Filters to enable or disable audit logging for any users that are assigned the Audit Filter.

The Logging Filter can be added to an Audit Filter with the logging key, which supports the following values:

| Value | Description                                  |
| ----- | -------------------------------------------- |
| ON    | Enables audit logging for this Audit Filter  |
| OFF   | Disables audit logging for this Audit Filter |

For example, the following query defines a [Default Audit Filter](mariadb-enterprise-audit-filters.md#default-audit-filter) that enables logging for all Events for any user account without a [Named Audit Filter](mariadb-enterprise-audit-filters.md#named-audit-filters):

```sql
INSERT INTO mysql.server_audit_filters (filtername, rule)
   VALUES (
       'default',
       JSON_COMPACT(
           '{
              "logging": "ON"
           }'
       )
    );
```

The example passes the JSON object to the [JSON\_COMPACT()](../../sql-functions/special-functions/json-functions/json_compact.md) function, so that the JSON object is compacted prior to being inserted into the system table. This step is recommended, but not required.

## Object Filters

{% hint style="info" %}
Object Filters are available from MariaDB 10.6, 10.5.12, and 10.4.21.
{% endhint %}

Object Filters allow Audit Filters to be limited to specific databases and/or tables. Object Filters can be specified at different scopes:

* An Object Filter can be specified for an entire Audit Filter
* An Object Filter can be specified for a single Event for the Audit Filter

### Object Filter Format

Object Filters are formatted as JSON objects, which are key-value pairs.

For Object Filters, the key in the key-value pair refers to the specific type of Object Filter. The following types of Object Filters are supported:

| Audit Log? | Object Filter Key | Description                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| No         | ignore\_databases | When one or more databases are specified with the `ignore_databases` Object Filter key, the specified databases are not audit-logged. The `ignore_databases` Object Filter key is an alias for the `ignore_tables` Object Filter key, with the table identifier set to the wildcard character (`*`). The ignore\_databases Object Filter key cannot be specified in the same Object Filter as the `log_databases` and `log_tables` Object Filter keys. |
| No         | ignore\_tables    | When one or more tables are specified with the `ignore_tables` Object Filter key, the specified tables will not be audit logged. Table names must be provided in the form _`database.table`_. Wildcard characters (`*`) are allowed. The `ignore_tables` Object Filter key cannot be specified in the same Object Filter as the `log_databases` and `log_tables` Object Filter keys.                                                                   |
| Yes        | log\_databases    | When one or more databases are specified with the `log_databases` Object Filter key, the specified databases will be audit logged, and all other databases will not be audit logged. The `log_databases` Object Filter key is an alias for the `log_tables` Object Filter key, with the table identifier set to the wildcard character (`*`).                                                                                                          |
| Yes        | log\_tables       | When one or more databases are specified with the `log_tables` Object Filter key, the specified tables will be audit logged, and all other tables will not be audit logged. Table names must be provided in the form _`database.table`_. Wildcard characters (`*`) are allowed.                                                                                                                                                                        |

The values in the key-value pair refer to object names.

When the Object Filter only applies to one object, the object name can be specified as a string scalar value in the JSON object:

```json
{"object_filter_key": "object"}
```

When the Object Filter applies to multiple objects, the object names can be specified in a JSON array in the JSON object:

```json
{"object_filter_key": [ "object", "object" ]}
```

In the following example, the Object Filter is designed to audit log the production and reporting databases and to skip audit logging for all other databases and tables:

```json
{"log_tables": ["production.*", "reporting.*"]}
```

And in the following example, the Object Filter is designed to skip audit logging for the production.app\_log table:

```json
{"ignore_tables": "production.app_log"}
```

The Object Filter keys must be specified in different locations in the Audit Filter's JSON object, depending on the desired scope of the Object Filter. The following sections describe how to set Object Filters in more detail.

### Set Object Filters at Event Scope

An Object Filter can be specified for a single Event Filter within an Audit Filter.

Object Filters are supported by the following Events:

* [Query Events](#query-events)
* [Table Events](#table-events)

To create an Object Filter for a single Event Filter, specify the Object Filter's JSON object as part of the JSON object for the Event Filter.

The examples below pass the JSON object to the [JSON\_COMPACT()](../../sql-functions/special-functions/json-functions/json_compact.md) function, so that the JSON object is compacted prior to being inserted into the system table. This step is recommended, but not required.

In the following example, the reporting Audit Filter specifies an Event Filter for Table Events with an embedded Object Filter that includes all tables in the production and reporting databases:

```sql
INSERT INTO mysql.server_audit_filters (filtername, rule)
   VALUES (
       'reporting',
       JSON_COMPACT(
           '{
              "table_event": [
                  "WRITE",
                  "CREATE",
                  "DROP",
                  "RENAME",
                  "ALTER",
                  {
                     "log_tables": [
                        "production.*",
                        "reporting.*"
                     ]
                  }
              ]
           }'
       )
    );
```

### Set Object Filters at Audit Filter Scope

An Object Filter can be specified for an entire Audit Filter.

To create an Object Filter at Audit Filter scope, specify the Object Filter's JSON object as part of the root JSON object for the Audit Filter.

The examples below pass the JSON object to the [JSON\_COMPACT()](../../sql-functions/special-functions/json-functions/json_compact.md) function, so that the JSON object is compacted prior to being inserted into the system table. This step is recommended, but not required.

In the following example, the reporting Audit Filter specifies an Object Filter that includes all tables in the production and reporting databases:

```sql
INSERT INTO mysql.server_audit_filters (filtername, rule)
   VALUES (
       'reporting',
       JSON_COMPACT(
          '{
              "log_tables": [
                  "production.*",
                  "reporting.*"
              ]
          }'
       )
    );
```

When an Object Filter is specified at Audit Filter scope, it can contain embedded Event Filters. The following Event types support Object Filters:

* [Query Events](#query-events)
* [Table Events](#table-events)

In the following example, the reporting Audit Filter has been modified to include Event Filters on specific Query Event sub-classes and Table Event sub-classes:

```sql
INSERT INTO mysql.server_audit_filters (filtername, rule)
   VALUES (
       'reporting',
       JSON_COMPACT(
          '{
              "log_tables": [
                  "production.*",
                  "reporting.*",
                  {
                     "query_event": [
                         "DML",
                         "DDL"
                     ],
                     "table_event": [
                         "WRITE",
                         "CREATE",
                         "DROP",
                         "RENAME",
                         "ALTER"
                     ]
                  }
              ]
          }'
       )
    );
```

### Combine Object Filters at Audit Filter and Event Scope

When an Object Filter is specified at Audit Filter scope with embedded Event Filters, the embedded Event Filters can contain additional Object Filters. When you combine Object Filters at different levels, it is possible to combine Object Filters that are normally incompatible, like tables and ignore\_tables.

To create Object Filters at Audit Filter and Event Type scope, specify the JSON object for the Object Filter at Audit Filter scope as part of the root JSON object for the Audit Filter and specify the JSON object for the Object Filter at Event Type scope as part of the JSON object for the Event Filter.

The examples below pass the JSON object to the [JSON\_COMPACT()](../../sql-functions/special-functions/json-functions/json_compact.md) function, so that the JSON object is compacted prior to being inserted into the system table. This step is recommended, but not required.

In the following example, the reporting Audit Filter specifies an Event Filter for Table Events with an embedded Object Filter that includes all tables in the production and reporting databases, but it excludes Query Events that target specific tables that store Personally Identifiable Information (PII), so that the sensitive information does not appear in the audit log:

```sql
INSERT INTO mysql.server_audit_filters (filtername, rule)
   VALUES (
       'reporting',
       JSON_COMPACT(
          '{
              "log_tables": [
                  "production.*",
                  "reporting.*",
                  {
                     "table_event": [
                         "WRITE",
                         "CREATE",
                         "DROP",
                         "RENAME",
                         "ALTER"
                     ],
                     "query_event": [
                         "DML",
                         "DDL",
                         {
                             "ignore_tables": [
                                 "production.customer_profiles",
                                 "production.customer_addresses"
                             ]
                         }
                     ]
                  }
              ]
          }'
       )
    );
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
