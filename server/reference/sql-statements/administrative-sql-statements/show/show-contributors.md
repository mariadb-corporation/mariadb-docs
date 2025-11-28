---
description: >-
  List financial contributors to the MariaDB Foundation. View the names and
  contributions of companies and individuals supporting the project.
---

# SHOW CONTRIBUTORS

## Syntax

```sql
SHOW CONTRIBUTORS
```

## Description

The `SHOW CONTRIBUTORS` statement displays information about the companies and people who financially contribute to MariaDB. For each contributor, it displays `Name`, `Location`, and `Comment` values. All columns are encoded as `latin1`.

It displays all [members and sponsors of the MariaDB Foundation](https://mariadb.org/en/supporters) as well as other financial contributors.

## Example

```sql
SHOW CONTRIBUTORS;
+---------------------+-------------------------------+-------------------------------------------------------------+
| Name                | Location                      | Comment                                                     |
+---------------------+-------------------------------+-------------------------------------------------------------+
| Alibaba Cloud       | https://www.alibabacloud.com/ | Platinum Sponsor of the MariaDB Foundation                  |
| Tencent Cloud       | https://cloud.tencent.com     | Platinum Sponsor of the MariaDB Foundation                  |
| Microsoft           | https://microsoft.com/        | Platinum Sponsor of the MariaDB Foundation                  |
| MariaDB Corporation | https://mariadb.com           | Founding member, Platinum Sponsor of the MariaDB Foundation |
| ServiceNow          | https://servicenow.com        | Platinum Sponsor of the MariaDB Foundation                  |
| Intel               | https://www.intel.com         | Platinum Sponsor of the MariaDB Foundation                  |
| SIT                 | https://sit.org               | Platinum Sponsor of the MariaDB Foundation                  |
| Visma               | https://visma.com             | Gold Sponsor of the MariaDB Foundation                      |
| DBS                 | https://dbs.com               | Gold Sponsor of the MariaDB Foundation                      |
| IBM                 | https://www.ibm.com           | Gold Sponsor of the MariaDB Foundation                      |
| Automattic          | https://automattic.com        | Silver Sponsor of the MariaDB Foundation                    |
| Percona             | https://www.percona.com/      | Sponsor of the MariaDB Foundation                           |
| Galera Cluster      | https://galeracluster.com     | Sponsor of the MariaDB Foundation                           |
| Google              | USA                           | Sponsoring encryption, parallel replication and GTID        |
| Facebook            | USA                           | Sponsoring non-blocking API, LIMIT ROWS EXAMINED etc        |
| Ronald Bradford     | Brisbane, Australia           | EFF contribution for UC2006 Auction                         |
| Sheeri Kritzer      | Boston, Mass. USA             | EFF contribution for UC2006 Auction                         |
| Mark Shuttleworth   | London, UK.                   | EFF contribution for UC2006 Auction                         |
+---------------------+-------------------------------+-------------------------------------------------------------+
```

## See Also

* [Log of MariaDB contributors](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/community/contributing-participating/log-of-mariadb-contributions).
* [SHOW AUTHORS](show-authors.md) list the authors of MariaDB (including documentation, QA etc).
* [MariaDB Foundation page on contributing financially](https://mariadb.org/donate/).

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
