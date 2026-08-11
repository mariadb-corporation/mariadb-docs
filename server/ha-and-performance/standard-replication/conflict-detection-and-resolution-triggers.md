---
description: >-
  Resolve row-based replication conflicts directly on the replica with Conflict
  Detection and Resolution (CDR) triggers, available in MariaDB Enterprise
  Server 12.3.
hidden: true
---

# Conflict Detection and Resolution (CDR) Triggers

{% hint style="warning" %}
CDR triggers are available beginning with **MariaDB Enterprise Server 12.3** and are a **beta feature**. Read [Limitations and Beta Caveats](conflict-detection-and-resolution-triggers.md#limitations-and-beta-caveats) before deploying CDR triggers on a production replica. Behavior outside the supported configuration is unspecified and may change.
{% endhint %}

{% hint style="info" %}
The terms _master_ and _slave_ have historically been used in replication, and MariaDB has begun the process of adding _primary_ and _replica_ synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.
{% endhint %}

Replica data can diverge from the primary in three ways:

1. **Direct local writes to the replica** — for example, an ETL job or a manual administrative fix.
2. **Multi-writer topologies** — such as [ring](multi-master-ring-replication.md) or bidirectional replication, where every server legitimately accepts writes.
3. **Operational drift** — left behind by skipped events, imperfect restores, or past failovers.

In every case the replication stream itself remains correct — the divergence enters alongside it, and surfaces only when a later event touches a row that no longer matches. CDR triggers let the replica resolve that moment according to a policy you define, instead of stopping replication.

## Overview

In [row-based replication](../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md) (RBR), the replica applies the row events recorded in the primary's binary log. Each event carries a _before-image_ (the row as it existed on the primary) and/or an _after-image_ (the row as the primary changed it). The applier locates the matching row on the replica and performs the same insert, update, or delete.

A **conflict** occurs when the replica's local data has diverged from what the primary's event expects:

* The primary inserts a row whose key **already exists** on the replica.
* The primary updates or deletes a row that is **missing** on the replica.
* The primary updates or deletes a row that exists on the replica but **holds different values**.

By default, these divergences raise a hard applier error (duplicate key, record not found, and so on) and **stop the SQL thread**, requiring an operator to intervene manually or skip the event.

Conflict Detection and Resolution (CDR) Triggers let you encode the resolution policy as SQL, on the replica. When a conflict is detected, the applier diverts the failing row event into a user-defined trigger. Inside the trigger you decide, per row, whether to overwrite, merge, ignore, or deliberately halt.

## Enabling CDR Triggers

CDR triggers fire only on the replica's SQL (applier) thread, and they operate on row-based replication events.

### Primary-Side Configuration

The only requirement on the primary is that it logs changes in row format with full row images, so that the replica receives the before- and after-images CDR triggers depend on:

```ini
[mariadbd]
binlog_format    = ROW
binlog_row_image = FULL
```

No other CDR-specific configuration is needed on the primary, and CDR triggers do **not** need to exist on the primary. (`STATEMENT` and `MIXED` binary log formats do not carry the row images CDR requires, so they are not supported for this feature.)

### Replica-Side Configuration

CDR triggers are gated by the same global system variable that controls [running triggers on the replica for row-based events](running-triggers-on-the-replica-for-row-based-events.md), [slave\_run\_triggers\_for\_rbr](replication-and-binary-log-system-variables.md#slave_run_triggers_for_rbr). There is no separate CDR switch. For CDR conflict handling, set the variable to `YES` while the SQL thread is stopped:

```sql
STOP REPLICA;
SET @@global.slave_run_triggers_for_rbr = YES;
START REPLICA;
```

Changing `slave_run_triggers_for_rbr` requires a privilege that permits setting this global variable, such as [SUPER](../../reference/sql-statements/account-management-sql-statements/grant.md#super) or the corresponding fine-grained global-variable grant.

## The Five Conflict Types

A CDR trigger is bound to **one** conflict type. The type names encode _what the primary did_ and _what the replica's local state implies_. The examples below use the table `t1 (a INT PRIMARY KEY, b INT, c CHAR(255))`, already in sync on both servers.

* **`INSERT_INSERT`**
  * Primary's operation: `INSERT`
  * Replica's local state: a row with the same key already exists
  * Typical underlying error: duplicate key

  ```sql
  -- On the replica (local write):
  INSERT INTO t1 VALUES (7, 1, 'local row');

  -- On the primary (replicated to the replica afterwards):
  INSERT INTO t1 VALUES (7, 2, 'primary row');
  -- The replicated insert collides with the replica's key 7
  ```
* **`UPDATE_UPDATE`**
  * Primary's operation: `UPDATE`
  * Replica's local state: the row exists but its values differ
  * Typical underlying error: before-image mismatch

  ```sql
  -- Both servers hold (7, 300, 'in sync')

  -- On the replica (local write):
  UPDATE t1 SET b = 900 WHERE a = 7;

  -- On the primary (replicated to the replica afterwards):
  UPDATE t1 SET b = 500 WHERE a = 7;
  -- The event's before-image says b = 300; the replica finds b = 900
  ```
* **`DELETE_UPDATE`**
  * Primary's operation: `DELETE`
  * Replica's local state: the row exists but has been changed locally
  * Typical underlying error: before-image mismatch

  ```sql
  -- Both servers hold (7, 300, 'in sync')

  -- On the replica (local write):
  UPDATE t1 SET b = 900 WHERE a = 7;

  -- On the primary (replicated to the replica afterwards):
  DELETE FROM t1 WHERE a = 7;
  -- The event's before-image says b = 300; the replica finds b = 900
  ```
* **`UPDATE_DELETE`**
  * Primary's operation: `UPDATE`
  * Replica's local state: the row is missing (already deleted locally)
  * Typical underlying error: record not found

  ```sql
  -- On the replica (local write):
  DELETE FROM t1 WHERE a = 7;

  -- On the primary (replicated to the replica afterwards):
  UPDATE t1 SET b = 500 WHERE a = 7;
  -- The replica has no row with key 7 to update
  ```
* **`DELETE_DELETE`**
  * Primary's operation: `DELETE`
  * Replica's local state: the row is missing (already deleted locally)
  * Typical underlying error: record not found

  ```sql
  -- On the replica (local write):
  DELETE FROM t1 WHERE a = 7;

  -- On the primary (replicated to the replica afterwards):
  DELETE FROM t1 WHERE a = 7;
  -- The replica has no row with key 7 to delete
  ```

## Syntax

```sql
CREATE TRIGGER <trigger_name>
    FOR CONFLICT <conflict_type>
    ON <table_name>
    FOR EACH ROW
    <trigger_body>;
```

`<conflict_type>` is one of `INSERT_INSERT`, `UPDATE_UPDATE`, `DELETE_UPDATE`, `UPDATE_DELETE`, `DELETE_DELETE`.

A conflict trigger has **no** `BEFORE`/`AFTER` timing keyword — the `FOR CONFLICT` clause replaces it. The trigger fires only at conflict time, on the applier thread. A single `CREATE TRIGGER` statement binds to exactly one conflict type: conflict types cannot be chained with `OR`, and a conflict type cannot be combined with the regular `INSERT`/`UPDATE`/`DELETE` trigger events. To handle several conflict types on the same table, create a separate trigger for each.

Example skeleton:

```sql
DELIMITER //
CREATE TRIGGER cdr_upd_upd FOR CONFLICT UPDATE_UPDATE ON t1
FOR EACH ROW
BEGIN
    -- resolution logic here
END//
DELIMITER ;
```

## Row Accessors: NEW, OLD, and ORG

CDR triggers introduce a third row accessor, `ORG`, alongside the familiar `NEW` and `OLD`:

| Accessor | Represents                                                                                     | Writable |
| -------- | ---------------------------------------------------------------------------------------------- | -------- |
| `NEW`    | The **resolution image** — the row you want the replica to end up with.                        | Yes      |
| `OLD`    | The replica's **current local row** (its actual stored state).                                 | No       |
| `ORG`    | The primary's **before-image** from the replication event — the state the primary expected.    | No       |

`ORG` is the key to conflict resolution: it lets the trigger compare what the primary believed (`ORG`) against what the replica actually has (`OLD`), and construct what should result (`NEW`).

### Accessor Availability per Conflict Type

Some images do not logically exist for certain conflicts, so the parser **rejects** triggers that reference an unavailable accessor at `CREATE TRIGGER` time:

| Conflict type   | `NEW` | `OLD`                    | `ORG`                              |
| --------------- | ----- | ------------------------ | ---------------------------------- |
| `INSERT_INSERT` | Yes   | Yes                      | No (an insert has no before-image) |
| `UPDATE_UPDATE` | Yes   | Yes                      | Yes                                |
| `DELETE_UPDATE` | Yes   | Yes                      | Yes                                |
| `UPDATE_DELETE` | Yes   | No (row missing locally) | Yes                                |
| `DELETE_DELETE` | Yes   | No (row missing locally) | Yes                                |

Violations produce an error when the trigger is created:

```sql
-- ORG referenced in INSERT_INSERT:
CREATE TRIGGER trg1 FOR CONFLICT INSERT_INSERT ON t1
  FOR EACH ROW SET NEW.b = ORG.a;
-- ERROR 1363 (HY000): There is no ORG row in on INSERT_INSERT trigger

-- OLD referenced in a *_DELETE conflict:
CREATE TRIGGER trg1 FOR CONFLICT UPDATE_DELETE ON t1
  FOR EACH ROW SET NEW.b = OLD.a;
-- ERROR 1363 (HY000): There is no OLD row in on UPDATE_DELETE trigger

-- Attempting to assign to a read-only accessor:
CREATE TRIGGER trg1 FOR CONFLICT UPDATE_UPDATE ON t1
  FOR EACH ROW SET ORG.b = NEW.a;
-- ERROR 1362 (HY000): Updating of ORG row is not allowed in trigger
```

## The Four Resolution Outcomes

Inside the trigger body, you choose one of four outcomes. A CDR trigger is not a general-purpose stored program for arbitrary DML against the conflicting table — these four outcomes are the supported ways to act on it.

### Resolve by Assigning NEW (Apply the Row)

Set columns on `NEW` and let the trigger return normally. The applier writes your `NEW` image to the table:

* For `INSERT_INSERT`, `UPDATE_UPDATE`, `DELETE_UPDATE`: the existing local row is overwritten with `NEW`.
* For `UPDATE_DELETE`, `DELETE_DELETE`: a new row is inserted from `NEW`.

```sql
-- UPDATE_UPDATE: primary wins, keep an audit note
CREATE TRIGGER cdr_uu FOR CONFLICT UPDATE_UPDATE ON t1
FOR EACH ROW
  SET NEW.c = 'resolved: primary wins';
```

### Do Nothing — Let the Default Operation Apply

If you do **not** assign `NEW` and return normally, the applier performs the operation's natural default for that conflict:

| Conflict        | Default action when `NEW` is left untouched                 |
| --------------- | ----------------------------------------------------------- |
| `INSERT_INSERT` | Overwrite the existing row with the primary's image.        |
| `UPDATE_UPDATE` | Overwrite the local row with the primary's image.           |
| `DELETE_UPDATE` | Delete the local row.                                       |
| `UPDATE_DELETE` | Insert the primary's row.                                   |
| `DELETE_DELETE` | No operation (the row is already absent).                   |

### Skip the Event — SIGNAL SQLSTATE '02TRG'

Raising the special SQLSTATE `02TRG` tells the applier to **gracefully ignore** this row event and continue replication. The table is left unmodified (the replica keeps `OLD`, or stays empty for a `*_DELETE` conflict). The SQL thread does **not** stop, and the replica's GTID position advances past the event.

```sql
CREATE TRIGGER cdr_skip FOR CONFLICT UPDATE_UPDATE ON t1
FOR EACH ROW
  SIGNAL SQLSTATE '02TRG';   -- keep the local row, drop the primary's change
```

`02TRG` is a "no data in trigger" subclass of the standard `02` ("no data") SQLSTATE class and is intentionally treated as _not an error_.

### Halt Deliberately — SIGNAL SQLSTATE '51CDR'

When a conflict is genuinely unresolvable by policy, raise SQLSTATE `51CDR` with a custom error number to **stop the SQL thread on purpose**:

```sql
CREATE TRIGGER cdr_halt FOR CONFLICT DELETE_DELETE ON t1
FOR EACH ROW
  SIGNAL SQLSTATE '51CDR' SET MYSQL_ERRNO = 9001;
```

The SQL thread stops with the error number you supplied (`9001` above), letting an operator investigate. After fixing the underlying data, run `START REPLICA` to resume.

Any other unhandled error raised inside the trigger also stops the SQL thread, but `51CDR` is the intentional, documented way to do so.

## Resolving Missing-Row Conflicts: the NEW Primary Key Sentinel

For `UPDATE_DELETE` and `DELETE_DELETE` the row is physically missing on the replica, so there is no `OLD`. The applier hands the trigger a blank `NEW` image with its **primary key set to `NULL`** as a sentinel, and interprets the trigger's result as follows:

* If, after the trigger runs, `NEW`'s primary key is still `NULL`, the applier treats it as "no resolution row" and performs the default action (insert the primary's row for `UPDATE_DELETE`, no-op for `DELETE_DELETE`).
* If the trigger **populates `NEW`'s primary key** (making it non-`NULL`), the applier applies `NEW` to the table.

Because `OLD` is unavailable, source the key (and any other values) from `ORG`, the primary's before-image:

```sql
DELIMITER //
CREATE TRIGGER cdr_dd FOR CONFLICT DELETE_DELETE ON t1
FOR EACH ROW
BEGIN
    -- Re-create the row the primary tried to delete, from its before-image
    SET NEW.a = ORG.a;          -- setting the PK signals "apply this row"
    SET NEW.b = ORG.b;
    SET NEW.c = 'del_del: re-materialized';
END//
DELIMITER ;
```

If you instead leave `NEW.a` untouched, the conflict resolves as a no-op and the row stays absent.

## The Before-Image Consistency Check

When a table has CDR triggers and an `UPDATE` or `DELETE` row event is applied, the applier locates the target row by primary key and compares the primary's before-image (`ORG`) against the row it actually found. A mismatch in the non-key columns means the replica's copy has diverged from what the primary expected, and is treated as a conflict.

What happens next depends on whether the mismatch is eligible to be routed to a CDR trigger:

* **Eligible → the trigger handles it.** The mismatch is delivered to your `UPDATE_UPDATE` trigger (for `UPDATE`) or `DELETE_UPDATE` trigger (for `DELETE`), exactly like the other conflict types.
* **Not eligible → the applier raises the consistency error and stops the SQL thread**, so an operator can reconcile rather than silently applying changes on top of unexpectedly diverged data:

```
ERROR 6001: Before image of replicated record does not match the slave local record
```

A mismatch is eligible for trigger routing only when all of these hold:

* the table has a **primary key**;
* the replica's [slave\_parallel\_mode](replication-and-binary-log-system-variables.md#slave_parallel_mode) is `optimistic` or a more conservative setting (`conservative`, `minimal`, `none`); and
* the row event is not currently being applied as an optimistic speculative attempt. (This case is transient: the transaction rolls back and retries non-speculatively, and on retry the conflict is delivered to the trigger.)

So even on a table that has CDR triggers, error 6001 can still appear when the table lacks a primary key, or when the replica runs a parallel mode more aggressive than `optimistic`. This is why the recommended beta configuration keeps the replica at `optimistic` or below — see [Limitations and Beta Caveats](conflict-detection-and-resolution-triggers.md#limitations-and-beta-caveats).

This check only exists when CDR triggers are present on the table. It is suppressed entirely when [slave\_exec\_mode](replication-and-binary-log-system-variables.md#slave_exec_mode) is `IDEMPOTENT` — but `IDEMPOTENT` mode is itself outside the supported beta configuration.

## Worked Example

The following demonstrates all five conflict types with a mix of resolutions.

```sql
-- ===== On the replica =====
STOP REPLICA;
SET @@global.slave_run_triggers_for_rbr = YES;
START REPLICA;

-- Table (created on the primary, replicated):
--   CREATE TABLE t1 (a INT PRIMARY KEY, b INT UNIQUE, c CHAR(255)) ENGINE=InnoDB;

DELIMITER //

-- 1) INSERT_INSERT: primary wins for a=10, keep local for a=11
CREATE TRIGGER cdr_ins_ins FOR CONFLICT INSERT_INSERT ON t1
FOR EACH ROW
BEGIN
    IF NEW.a = 10 THEN
        SET NEW.c = 'ins_ins: updated to NEW';   -- apply primary's image (+ tweak)
    ELSEIF NEW.a = 11 THEN
        SIGNAL SQLSTATE '02TRG';                 -- keep local row
    END IF;
END//

-- 2) UPDATE_DELETE: re-insert the row the primary updated (missing locally)
CREATE TRIGGER cdr_upd_del FOR CONFLICT UPDATE_DELETE ON t1
FOR EACH ROW
BEGIN
    IF NEW.a = 20 THEN
        SET NEW.b = ORG.b + 1000;
        SET NEW.c = 'upd_del: inserted NEW';
    ELSEIF NEW.a = 21 THEN
        SIGNAL SQLSTATE '02TRG';                 -- leave the row absent
    END IF;
END//

-- 3) DELETE_UPDATE: delete / keep / convert to update
CREATE TRIGGER cdr_del_upd FOR CONFLICT DELETE_UPDATE ON t1
FOR EACH ROW
BEGIN
    IF OLD.a = 30 THEN
        BEGIN END;                               -- default: delete the local row
    ELSEIF OLD.a = 31 THEN
        SIGNAL SQLSTATE '02TRG';                 -- keep the locally-updated row
    ELSEIF OLD.a = 32 THEN
        SET NEW.a = OLD.a;                       -- non-NULL PK => convert to UPDATE
        SET NEW.b = OLD.b;
        SET NEW.c = 'del_upd: updated to NEW';
    END IF;
END//

-- 4) UPDATE_UPDATE: primary wins for a=40, keep local for a=41
CREATE TRIGGER cdr_upd_upd FOR CONFLICT UPDATE_UPDATE ON t1
FOR EACH ROW
BEGIN
    IF NEW.a = 40 THEN
        SET NEW.c = 'upd_upd: updated to NEW';
    ELSEIF NEW.a = 41 THEN
        SIGNAL SQLSTATE '02TRG';
    END IF;
END//

-- 5) DELETE_DELETE: no-op / skip / re-materialize / deliberate halt
CREATE TRIGGER cdr_del_del FOR CONFLICT DELETE_DELETE ON t1
FOR EACH ROW
BEGIN
    IF ORG.a = 50 THEN
        BEGIN END;                               -- default no-op
    ELSEIF ORG.a = 51 THEN
        SIGNAL SQLSTATE '02TRG';                 -- skip
    ELSEIF ORG.a = 52 THEN
        SET NEW.a = ORG.a;                       -- re-create the row
        SET NEW.b = ORG.b;
        SET NEW.c = 'del_del: assigned to NEW';
    ELSEIF ORG.a = 53 THEN
        SIGNAL SQLSTATE '51CDR' SET MYSQL_ERRNO = 9001;  -- stop SQL thread
    END IF;
END//

DELIMITER ;
```

## Operational Notes

* **One trigger per conflict type per table.** Define separate triggers for the conflict types you want to handle. Conflict types you don't define fall back to the normal applier behavior (hard error, SQL thread stops).
* **Define triggers on servers that act as replicas.** A server that only acts as a primary does not need CDR triggers. In [ring replication](multi-master-ring-replication.md), every server replicates from another, so every server should define them. A CDR trigger created on the primary and replicated does not resolve conflicts there — the trigger only fires on a replica's applier thread.
* **You can write to other tables.** The `NEW`/`OLD`/`ORG` accessors act on the conflicting table, but the trigger body may run DML against other tables (for example, an audit or exception log). Keep this lightweight — it runs inline on the applier thread.
* **Monitor the SQL thread.** A `51CDR` halt, an unhandled trigger error, or a before-image mismatch (error 6001) stops the SQL thread. Watch `Last_SQL_Errno` and `Last_SQL_Error` in [SHOW REPLICA STATUS](../../reference/sql-statements/administrative-sql-statements/show/show-replica-status.md).
* **The [Executed\_triggers](../optimization-and-tuning/system-variables/server-status-variables.md#executed_triggers) status variable** increments for each trigger invocation (CDR triggers included), which is useful for confirming the feature is firing.

## Limitations and Beta Caveats

CDR triggers are **beta**. The current implementation is validated only within the configuration below. Outside it, behavior is unsupported, unspecified, or known-incomplete:

| Area                                | Current state in beta                                                                                                                                             |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Row image format                    | Supported **only** with `binlog_row_image = FULL`. Other row-image settings are not supported.                                                                     |
| System-versioned tables             | **Not supported.** Do not create CDR triggers on tables with [system versioning](../../reference/sql-structure/temporal-tables/system-versioned-tables.md).       |
| Parallel replication mode           | Supported up to and including `slave_parallel_mode = optimistic` (that is, `none`, `minimal`, `conservative`, `optimistic`). `aggressive` is **not supported**.    |
| `slave_exec_mode = IDEMPOTENT`      | Behavior in combination with `IDEMPOTENT` is **unspecified**. `IDEMPOTENT` also disables the before-image consistency check.                                       |
| Multiple triggers per conflict type | Creating more than one CDR trigger for the same conflict type on the same table is not prevented, but the effect is **unspecified**.                               |
| Coexistence with regular RBR triggers | A CDR trigger alongside a normal replica-side RBR trigger on the same table is intended to work but **may produce unexpected results**. Test thoroughly.          |
| Mixing with multi-event triggers    | A single `CREATE TRIGGER` statement is either a CDR trigger or a regular trigger, never both — see below.                                                          |

### No Mixing of CDR and Regular Trigger Syntax

MariaDB supports defining a single regular trigger that fires on more than one event by chaining events with `OR` ([MDEV-10164](https://jira.mariadb.org/browse/MDEV-10164)). CDR triggers and this multi-event syntax are mutually exclusive within a single `CREATE TRIGGER` statement:

* A CDR trigger binds to exactly **one** conflict type — `FOR CONFLICT INSERT_INSERT OR UPDATE_UPDATE` is rejected.
* A conflict type cannot be mixed with regular events in the same statement — `FOR CONFLICT` combined with `INSERT`, `UPDATE`, or `DELETE` is rejected.
* The `FOR CONFLICT` clause replaces the `BEFORE`/`AFTER` timing keyword entirely; a regular trigger cannot carry a `FOR CONFLICT` clause.

### Recommended Beta Configuration

```ini
[mariadbd]
binlog_row_image    = FULL
# On the replica, keep parallel mode at optimistic or below:
slave_parallel_mode = optimistic
# Do not use IDEMPOTENT exec mode with CDR triggers:
slave_exec_mode     = STRICT
```

Validate CDR triggers in a staging environment that mirrors your production topology before enabling them on a production replica, and watch the SQL thread closely during the initial rollout.

## See Also

* [Running Triggers on the Replica for Row-based Events](running-triggers-on-the-replica-for-row-based-events.md)
* [Replication and Binary Log System Variables](replication-and-binary-log-system-variables.md)
* [Trigger Overview](../../server-usage/triggers-events/triggers/trigger-overview.md)
* [Parallel Replication](parallel-replication.md)
* [Multi-Master Ring Replication](multi-master-ring-replication.md)

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
