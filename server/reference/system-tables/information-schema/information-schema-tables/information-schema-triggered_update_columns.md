---
description: >-
  The Information Schema TRIGGERED_UPDATE_COLUMNS table identifies which columns
  are modified by the SET clause of a specific trigger.
---

# Information Schema TRIGGERED\_UPDATE\_COLUMNS

{% hint style="info" %}
This table is available from [MariaDB 12.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/12.2/mariadb-12.2-changes-and-improvements).
{% endhint %}

The [Information Schema](../) `TRIGGERED_UPDATE_COLUMNS` table shows columns specified in [triggers](../../../../server-usage/triggers-events/triggers/) for [update](../../../sql-statements/data-manipulation/changing-deleting-data/update.md) operations.

Columns are displayed only if the user has non-SELECT [privileges](../../../sql-statements/account-management-sql-statements/grant.md) on the columns.

It contains the following columns:

<table><thead><tr><th width="231.86663818359375">Column</th><th>Description</th></tr></thead><tbody><tr><td>TRIGGER_CATALOG</td><td>Always <code>def</code> in MariaDB.</td></tr><tr><td>TRIGGER_SCHEMA</td><td>Name of the database containing the trigger.</td></tr><tr><td>TRIGGER_NAME</td><td>Name of the trigger.</td></tr><tr><td>EVENT_OBJECT_CATALOG</td><td>Always <code>def</code> in MariaDB</td></tr><tr><td>EVENT_OBJECT_SCHEMA</td><td>Name of the database containing the table that the trigger is defined on.</td></tr><tr><td>EVENT_OBJECT_TABLE</td><td>Name of the table that the trigger is defined on.</td></tr><tr><td>EVENT_OBJECT_COLUMN</td><td>Name of the column that the trigger is defined on.</td></tr></tbody></table>

## Examples

<pre class="language-sql"><code class="lang-sql">CREATE TABLE t (a INT, b INT, c INT);
INSERT INTO t VALUES (1, 2, 3);
CREATE TABLE t1 (a_old INT, b_old INT, a_new INT, b_new INT);
CREATE TABLE t2 (a_old INT, b_old INT, a_new INT, b_new INT); 
CREATE TRIGGER trigger_before_update BEFORE UPDATE OF a, b ON t 
  FOR EACH ROW INSERT INTO t1 VALUES (OLD.a, OLD.b, NEW.a, NEW.b);

<strong>SELECT * FROM INFORMATION_SCHEMA.TRIGGERED_UPDATE_COLUMNS\G 
</strong>*************************** 1. row ***************************
 TRIGGER_CATALOG: def 
TRIGGER_SCHEMA: test 
TRIGGER_NAME: trigger_before_update 
EVENT_OBJECT_CATALOG: def 
EVENT_OBJECT_SCHEMA: test 
EVENT_OBJECT_TABLE: t 
EVENT_OBJECT_COLUMN: a 
*************************** 2. row *************************** 
TRIGGER_CATALOG: def 
TRIGGER_SCHEMA: test 
TRIGGER_NAME: trigger_before_update 
EVENT_OBJECT_CATALOG: def 
EVENT_OBJECT_SCHEMA: test 
EVENT_OBJECT_TABLE: t 
EVENT_OBJECT_COLUMN: b
</code></pre>

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
