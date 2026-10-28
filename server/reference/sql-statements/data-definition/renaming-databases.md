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
mariadb-dump PROD --no-data --no-create-info --routines --triggers --events \
> PROD_routines_triggers_events.sql
```

{% hint style="danger" %}
Do not omit `--no-create-info`. Without it, the dump contains `DROP TABLE IF EXISTS` and `CREATE TABLE` for every table. Restoring that file after the rename drops the moved tables and recreates them empty. `--no-data` does not prevent this.
{% endhint %}
{% endstep %}

{% step %}
**Dump Views.**

`--no-create-info` leaves views out of the previous dump, and `RENAME TABLE` cannot move a view into another database. Dump the views separately, before the rename. This step requires bash, because it reads the view names into an array.

```bash
mapfile -t views < <(mysql -ss -e"SELECT TABLE_NAME FROM INFORMATION_SCHEMA.VIEWS \
WHERE TABLE_SCHEMA = 'PROD'")
[ ${#views[@]} -gt 0 ] && mariadb-dump PROD "${views[@]}" --no-data --skip-triggers \
> PROD_views.sql
```

If `PROD` has no views, the second command does nothing and `PROD_views.sql` is not created, but the command exits with a non-zero status. In that case, skip the views restore in the later restore step.
{% endstep %}

{% step %}
**Generate RENAME TABLE Commands.**

Run the following query to generate a script with the necessary `RENAME TABLE` statements. This is much faster than a full logical dump. Views are excluded, because they cannot be renamed into another database.

```sql
mysql -ss -e"SELECT CONCAT('RENAME TABLE PROD.\`', TABLE_NAME, '\` TO TEST.\`', \
TABLE_NAME, '\`;') FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'PROD' \
AND TABLE_TYPE <> 'VIEW'" > PROD_rename_table.sql
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

Also record the number of rows in every base table. Take these counts now, before the rename, because afterwards the tables are no longer in `PROD`.

```bash
mysql -ss -e"SELECT CONCAT('SELECT ''', TABLE_NAME, ''', COUNT(*) FROM \`', \
TABLE_NAME, '\`;') FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'PROD' \
AND TABLE_TYPE IN ('BASE TABLE', 'SYSTEM VERSIONED')" > count_rows.sql
mysql -ss PROD < count_rows.sql > PROD_row_counts.txt
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

{% hint style="warning" %}
A table that has triggers cannot be renamed into another database. The rename fails with "Trigger in wrong schema". If the script fails partway, the tables before it have already been moved to `TEST`, so check the list of triggers from the previous steps before you run the script.
{% endhint %}

```bash
mysql TEST < PROD_rename_table.sql
```
{% endstep %}

{% step %}
**Restore Logical Objects.**

After the rename script completes, restore the triggers, routines, and events into the new database. Restore the views last.

```bash
mysql TEST < PROD_routines_triggers_events.sql
mysql TEST < PROD_views.sql
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

Then compare the row counts with the counts you took before the rename. Any difference means that rows were lost, so do not drop `PROD`.

```bash
mysql -ss TEST < count_rows.sql > TEST_row_counts.txt
diff PROD_row_counts.txt TEST_row_counts.txt && echo "Row counts match"
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

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
