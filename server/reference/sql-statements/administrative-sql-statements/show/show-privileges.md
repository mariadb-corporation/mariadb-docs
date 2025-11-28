---
description: >-
  List available system privileges. View the context and description for each
  privilege supported by the server.
---

# SHOW PRIVILEGES

## Syntax

```sql
SHOW PRIVILEGES
```

## Description

{% tabs %}
{% tab title="Current" %}
`SHOW PRIVILEGES` shows the list of [system privileges](../../account-management-sql-statements/grant.md) that the MariaDB server supports. The exact list of privileges depends on the version of your server.
{% endtab %}

{% tab title="< 10.5.2 / 10.4.13 / 10.3.23" %}
`SHOW PRIVILEGES` shows the list of [system privileges](../../account-management-sql-statements/grant.md) that the MariaDB server supports. The exact list of privileges depends on the version of your server.

Note that before [MariaDB 10.3.23](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10323-release-notes), [MariaDB 10.4.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-10413-release-notes) and [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1052-release-notes) , the [Delete history](../../account-management-sql-statements/grant.md#table-privileges) privilege displays as `Delete versioning rows` ([MDEV-20382](https://jira.mariadb.org/browse/MDEV-20382)).
{% endtab %}
{% endtabs %}

## Example

{% hint style="info" %}
The output is for MariaDB version from 10.5.9. In previous versions, it might look differently.
{% endhint %}

```sql
SHOW PRIVILEGES;
+--------------------------+---------------------------------------+--------------------------------------------------------------------+
| Privilege                | Context                               | Comment                                                            |
+--------------------------+---------------------------------------+--------------------------------------------------------------------+
| Alter                    | Tables                                | To alter the table                                                 |
| Alter routine            | Functions,Procedures                  | To alter or drop stored functions/procedures                       |
| Create                   | Databases,Tables,Indexes              | To create new databases and tables                                 |
| Create routine           | Databases                             | To use CREATE FUNCTION/PROCEDURE                                   |
| Create temporary tables  | Databases                             | To use CREATE TEMPORARY TABLE                                      |
| Create view              | Tables                                | To create new views                                                |
| Create user              | Server Admin                          | To create new users                                                |
| Delete                   | Tables                                | To delete existing rows                                            |
| Delete history           | Tables                                | To delete versioning table historical rows                         |
| Drop                     | Databases,Tables                      | To drop databases, tables, and views                               |
| Event                    | Server Admin                          | To create, alter, drop and execute events                          |
| Execute                  | Functions,Procedures                  | To execute stored routines                                         |
| File                     | File access on server                 | To read and write files on the server                              |
| Grant option             | Databases,Tables,Functions,Procedures | To give to other users those privileges you possess                |
| Index                    | Tables                                | To create or drop indexes                                          |
| Insert                   | Tables                                | To insert data into tables                                         |
| Lock tables              | Databases                             | To use LOCK TABLES (together with SELECT privilege)                |
| Process                  | Server Admin                          | To view the plain text of currently executing queries              |
| Proxy                    | Server Admin                          | To make proxy user possible                                        |
| References               | Databases,Tables                      | To have references on tables                                       |
| Reload                   | Server Admin                          | To reload or refresh tables, logs and privileges                   |
| Binlog admin             | Server                                | To purge binary logs                                               |
| Binlog monitor           | Server                                | To use SHOW BINLOG STATUS and SHOW BINARY LOG                      |
| Binlog replay            | Server                                | To use BINLOG (generated by mariadb-binlog)                        |
| Replication master admin | Server                                | To monitor connected slaves                                        |
| Replication slave admin  | Server                                | To start/stop slave and apply binlog events                        |
| Slave monitor            | Server                                | To use SHOW SLAVE STATUS and SHOW RELAYLOG EVENTS                  |
| Replication slave        | Server Admin                          | To read binary log events from the master                          |
| Select                   | Tables                                | To retrieve rows from table                                        |
| Show databases           | Server Admin                          | To see all databases with SHOW DATABASES                           |
| Show view                | Tables                                | To see views with SHOW CREATE VIEW                                 |
| Shutdown                 | Server Admin                          | To shut down the server                                            |
| Super                    | Server Admin                          | To use KILL thread, SET GLOBAL, CHANGE MASTER, etc.                |
| Trigger                  | Tables                                | To use triggers                                                    |
| Create tablespace        | Server Admin                          | To create/alter/drop tablespaces                                   |
| Update                   | Tables                                | To update existing rows                                            |
| Set user                 | Server                                | To create views and stored routines with a different definer       |
| Federated admin          | Server                                | To execute the CREATE SERVER, ALTER SERVER, DROP SERVER statements |
| Connection admin         | Server                                | To bypass connection limits and kill other users' connections      |
| Read_only admin          | Server                                | To perform write operations even if @@read_only=ON                 |
| Usage                    | Server Admin                          | No privileges - allow connect only                                 |
+--------------------------+---------------------------------------+--------------------------------------------------------------------+
41 rows in set (0.000 sec)
```

## See Also

* [SHOW CREATE USER](show-create-user.md) shows how the user was created.
* [SHOW GRANTS](show-grants.md) shows the `GRANTS/PRIVILEGES` for a user.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
