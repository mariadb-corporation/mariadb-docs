---
description: >-
  Learn the supported methods for renaming a database. Since RENAME DATABASE is
  not available, this guide outlines safe workarounds like dumping and reloading
  or moving tables.
---

# Renaming Databases

There is no `RENAME DATABASE` statement. To rename a database, use one of the following procedures.

## Using RENAME TABLE

{% hint style="danger" %}
Use this procedure only if your tables have neither triggers nor views or events.
{% endhint %}

To move your tables from a database named db1 to one named db2, run these statements:

```sql
CREATE DATABASE db2;
# Do this for every table in database db1
RENAME TABLE db1.t TO db2.t;
# When no table is left in database db1, optionally drop it
DROP DATABASE db1;
```

{% hint style="warning" %}
Privileges are neither dropped for `db1`, nor are they "copied" to `db2`. Use [SHOW PRIVILEGES](../administrative-sql-statements/show/show-privileges.md) to see which privileges are related to `db1`, then [apply those privileges](../account-management-sql-statements/grant.md) to `db2`.
{% endhint %}

## Renaming Databases Manually

To overcome the limitations of the previous procedure, you can do the following.

In the following steps, the source database is named `PROD` , and the destination database `TEST`.

* **Full Backup and Restore**: If restoring to a different server, use [mariadb-backup](../../../server-usage/backup-and-restore/mariadb-backup/) to create a full backup, then restore it to the intended server. (This step is optional. It is not necessary if your renamed database is to reside on the same computer.)

{% stepper %}
{% step %}
**Dump Logical Objects.**

`RENAME TABLE` does not work for triggers, events, and routines. You need to dump these logical objects separately.

```bash
mariadb-dump PROD --no-data --routines --triggers --events \
> PROD_routines_triggers_events.sql
```
{% endstep %}

{% step %}
**Generate RENAME TABLE Commands.**

Run the following query to generate a script with the necessary `RENAME TABLE` statements. This is much faster than a full logical dump.

```sql
mysql -ss -e"SELECT CONCAT('RENAME TABLE PROD.', TABLE_NAME, ' TO TEST.', \
TABLE_NAME, ';') FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'PROD'" \
> PROD_rename_table.sql
```
{% endstep %}

{% step %}
**List all Existing Objects.**

```sql
SELECT TABLE_SCHEMA, TABLE_NAME FROM INFORMATION_SCHEMA.TABLES 
       WHERE TABLE_SCHEMA = 'PROD';
SELECT EVENT_SCHEMA, EVENT_NAME FROM INFORMATION_SCHEMA.EVENTS 
       WHERE EVENT_SCHEMA = 'PROD';
SELECT ROUTINE_SCHEMA, ROUTINE_NAME FROM INFORMATION_SCHEMA.ROUTINES 
       WHERE ROUTINE_SCHEMA = 'PROD';
SELECT TRIGGER_SCHEMA, TRIGGER_NAME FROM INFORMATION_SCHEMA.TRIGGERS 
 WHERE TRIGGER_SCHEMA = 'PROD';
```
{% endstep %}

{% step %}
**Create the new Database.**

```sql
CREATE DATABASE TEST;
```
{% endstep %}

{% step %}
**Run the rename\_table Script.**

```bash
mysql TEST < PROD_rename_table.sql
```
{% endstep %}

{% step %}
**Restore Logical Objects.**

After the rename script completes, restore the triggers, routines, and events into the new database.

```bash
mysql TEST < PROD_routines_triggers_events.sql
```
{% endstep %}

{% step %}
**Verify all Objects are Restored.**

Verify that all objects have been correctly moved to the new `TEST` database.

```sql
SELECT TABLE_SCHEMA, TABLE_NAME FROM INFORMATION_SCHEMA.TABLES 
       WHERE TABLE_SCHEMA = 'TEST';
SELECT EVENT_SCHEMA, EVENT_NAME FROM INFORMATION_SCHEMA.EVENTS 
       WHERE EVENT_SCHEMA = 'TEST';
SELECT ROUTINE_SCHEMA, ROUTINE_NAME FROM INFORMATION_SCHEMA.ROUTINES 
       WHERE ROUTINE_SCHEMA = 'TEST';
SELECT TRIGGER_SCHEMA, TRIGGER_NAME FROM INFORMATION_SCHEMA.TRIGGERS 
       WHERE TRIGGER_SCHEMA = 'TEST';
```
{% endstep %}

{% step %}
**Cleanup.**

Once you have confirmed everything looks good, you can drop the old `PROD` database.

{% hint style="warning" %}
Privileges are neither dropped for `PROD`, nor are they "copied" to `TEST`. Use [SHOW PRIVILEGES](../administrative-sql-statements/show/show-privileges.md) to see which privileges are related to `PROD`, then [apply those privileges](../account-management-sql-statements/grant.md) to `TEST`.
{% endhint %}
{% endstep %}
{% endstepper %}
