---
description: >-
  The MYSQL_JSON plugin provides a JSON data type alias for compatibility,
  ensuring that tables created with the MySQL JSON type can be read by MariaDB.
---

# MYSQL\_JSON

{% hint style="info" %}
The `TYPE_MYSQL_JSON` plugin is available from [MariaDB 10.5.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1057-release-notes).
{% endhint %}

The JSON type in MySQL stores the JSON object in its own native form, while, in MariaDB, the [JSON type](../../data-types/string-data-types/json.md) is a [LONGTEXT](../../data-types/string-data-types/longtext.md). Opening a table with a JSON type created in MySQL results in an error:

```sql
SELECT * FROM mysql_json_table;
ERROR 4161 (HY000): Unknown data type: 'MYSQL_JSON'
```

The `mysql_json` plugin is used to make it easier to upgrade to MariaDB.

## Installing

Installing can be done in a [number of ways](../plugin-overview.md#installing-a-plugin), for example:

```sql
INSTALL SONAME 'type_mysql_json';
```

See [Making MariaDB understand MySQL JSON](https://mariadb.org/making-mariadb-understand-mysql-json/) for a full description.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
