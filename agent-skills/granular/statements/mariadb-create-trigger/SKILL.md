---
name: mariadb-create-trigger
description: "MariaDB-specific syntax and behavior for CREATE TRIGGER — OR REPLACE, DEFINER, IF NOT EXISTS, multiple trigger_events in one statement with INSERTING/UPDATING/DELETING predicates (since 12.0), multiple triggers per action-time/event ordered with FOLLOWS/PRECEDES, OLD/NEW row-reference rules, the no-ALTER-TRIGGER gotcha, and restrictions on modifying tables already touched by the firing statement. Use when writing, generating, or reviewing CREATE TRIGGER statements that target MariaDB."
---

# CREATE TRIGGER in MariaDB

*Last updated: 2026-07-20*

This skill covers the **delta between standard SQL triggers and MariaDB's**. It assumes the agent already knows the standard trigger model (fires `BEFORE`/`AFTER` a row-level DML event, `OLD`/`NEW` row aliases). Everything below documents MariaDB-specific grammar, ordering of multiple triggers, restrictions, and the most common LLM traps.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Anything available in current LTS branches (10.6, 10.11, 11.4, 11.8) is shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / suggests… | …prefer the MariaDB form |
|---|---|
| `ALTER TRIGGER … RENAME TO …` or any `ALTER TRIGGER` | **There is no `ALTER TRIGGER` statement in MariaDB.** To change a trigger, use `CREATE OR REPLACE TRIGGER` (if only the body/options change) or `DROP TRIGGER` + `CREATE TRIGGER` (to rename — trigger names can't be renamed in place) |
| Assuming a table can only have one `BEFORE INSERT` trigger | MariaDB has always allowed **multiple triggers for the same action time + event** on one table, ordered with `FOLLOWS`/`PRECEDES`. If neither is given, the new trigger is appended last for that action/event |
| One `CREATE TRIGGER` per event, e.g. three separate triggers for `INSERT`, `UPDATE`, `DELETE` doing the same thing | *(since 12.0)* A single trigger can fire on multiple events: `BEFORE INSERT OR UPDATE OR DELETE ON t FOR EACH ROW …`, using `INSERTING`/`UPDATING`/`DELETING` predicates in the body to branch. Older versions (all current LTS lines) require one event per trigger |
| `NEW.col` in a `DELETE` trigger, or `OLD.col` in an `INSERT` trigger | Only `NEW.col` exists in `INSERT` (no old row); only `OLD.col` exists in `DELETE` (no new row); `UPDATE` triggers have both |
| `SET NEW.col = value` inside an `AFTER` trigger to change the row | Has **no effect** in `AFTER` — the row change already happened. Move the assignment to a `BEFORE` trigger |
| `CREATE DEFINER=... SQL SECURITY DEFINER TRIGGER …` | `SQL SECURITY` is **not valid trigger syntax** (unlike views/procedures/functions) — triggers always execute with the `DEFINER`'s privileges. Just omit it |
| A trigger body that does `COMMIT;`, `ROLLBACK;`, or `START TRANSACTION;` | **Not permitted** — triggers can't perform explicit or implicit commits/rollbacks; they always run inside the invoking statement's transaction |
| A trigger on one table that writes back to a table the firing statement is already reading/writing | Raises `ER_CANT_UPDATE_USED_TABLE_IN_SF_OR_TRG` — a trigger cannot modify a table the outer statement has already opened. Design around it (e.g. use a different table, or restructure the statement) |
| `CREATE TRIGGER … ON some_view FOR EACH ROW …` or `ON temp_table` | Triggers can only be attached to **permanent base tables** — not views, not `TEMPORARY` tables |
| Multi-statement trigger body pasted straight into the client without changing the delimiter | The body's own `;` terminates the statement early in the CLI client. Wrap with `DELIMITER //` … `END; //` … `DELIMITER ;` |

## Syntax

```sql
CREATE [OR REPLACE]
    [DEFINER = { user | CURRENT_USER | role | CURRENT_ROLE }]
    TRIGGER [IF NOT EXISTS]
            trigger_name trigger_time {trigger_event [OR trigger_event] ...}
    ON tbl_name FOR EACH ROW
    [{ FOLLOWS | PRECEDES } other_trigger_name]
    trigger_stmt

trigger_time: BEFORE | AFTER
trigger_event: INSERT | UPDATE [OF column_name [, column_name] ...] | DELETE
```

- `tbl_name` must be a permanent base table — not a view, not a `TEMPORARY` table.
- Requires the **`TRIGGER`** privilege on `tbl_name` (plus `SET USER`/`SUPER` to use a `DEFINER` other than the current user).
- `DEFINER` defaults to `CURRENT_USER` when omitted.
- Multi-statement bodies need `BEGIN … END`; use the `DELIMITER` client command to type them interactively.
- There is **no `ALTER TRIGGER`**. Modify via `CREATE OR REPLACE TRIGGER`, or `DROP TRIGGER` + recreate.

## Multiple Trigger Events in One Statement *(since 12.0)*

A single `CREATE TRIGGER` can react to more than one DML event by chaining `trigger_event` with `OR`:

```sql
CREATE TRIGGER t1_b_any BEFORE INSERT OR UPDATE OR DELETE ON t1 FOR EACH ROW
BEGIN
  IF INSERTING THEN
    INSERT INTO t2 VALUES (NEW.a, 'INSERTING');
  ELSEIF UPDATING THEN
    INSERT INTO t2 VALUES (NEW.a, 'UPDATING');
  ELSEIF DELETING THEN
    INSERT INTO t2 VALUES (OLD.a, 'DELETING');
  END IF;
END;
```

`INSERTING`, `UPDATING`, `DELETING` are boolean predicates usable inside the body to branch on which event fired. On MariaDB versions before 12.0 (including all current 10.x/11.x LTS lines), only a single `trigger_event` is allowed per trigger — write three separate triggers instead, one per event.

## Multiple Triggers per Action Time + Event — `FOLLOWS`/`PRECEDES`

Unlike the single-event-per-trigger constraint above, **having more than one trigger for the same `trigger_time` + `trigger_event` combination on a table has always been supported** in MariaDB (this predates the 10.6 baseline — no version gate applies). Use `FOLLOWS`/`PRECEDES` to control firing order:

```sql
CREATE TRIGGER tr1_bi BEFORE INSERT ON t1 FOR EACH ROW SET @a := 1;
CREATE TRIGGER tr2_bi BEFORE INSERT ON t1 FOR EACH ROW FOLLOWS tr1_bi SET @a := 2;
CREATE TRIGGER tr0_bi BEFORE INSERT ON t1 FOR EACH ROW PRECEDES tr1_bi SET @a := 0;
```

- `FOLLOWS other_trigger` places the new trigger immediately after `other_trigger` in the firing order.
- `PRECEDES other_trigger` places it immediately before.
- Omitting both appends the new trigger last for that action time + event.
- Verify the actual order via `ACTION_ORDER` in `INFORMATION_SCHEMA.TRIGGERS`:

  ```sql
  SELECT trigger_name, action_order FROM information_schema.triggers
    WHERE event_object_table = 't1';
  ```

## `OLD` / `NEW` Row References

| Event | Available references |
|---|---|
| `INSERT` | `NEW.col` only (no prior row) |
| `UPDATE` | Both `OLD.col` (pre-update) and `NEW.col` (post-update) |
| `DELETE` | `OLD.col` only (row is gone after) |

- `OLD.col` is always **read-only**.
- `NEW.col` is readable everywhere, and in a **`BEFORE`** trigger it can be assigned with `SET NEW.col = value` to change what actually gets written. In an `AFTER` trigger, assigning `NEW.col` is a no-op — the row is already committed to storage.
- Neither `OLD` nor `NEW` can reference **generated columns**.
- `OLD`/`NEW` are MariaDB extensions to standard SQL trigger syntax, and are not case-sensitive.

## Restrictions

Triggers inherit **both** the stored-routine and stored-function limitation sets, plus their own:

- Cannot be defined on a `TEMPORARY` table or a view — permanent base tables only.
- Cannot return a result set (a bare `SELECT` is rejected; `SELECT ... INTO` is fine).
- No explicit or implicit `COMMIT`/`ROLLBACK`/`START TRANSACTION` inside the body.
- Cannot modify a table that the invoking statement has already opened for read or write (`ER_CANT_UPDATE_USED_TABLE_IN_SF_OR_TRG`).
- No `PREPARE`/`EXECUTE`/`DEALLOCATE PREPARE` (no dynamic SQL).
- Not activated by foreign-key cascade actions (`ON DELETE CASCADE`, etc.) or by `TRUNCATE TABLE`.
- Standard `FOR EACH STATEMENT` triggers are not supported — MariaDB triggers are always row-level (`FOR EACH ROW` is mandatory in the grammar).
- If called indirectly (a trigger calling a stored procedure via `CALL`), the called routine inherits the trigger's restrictions — e.g. it still can't `COMMIT` or return a result set.

## Trigger Firing on Compound Statements

- `LOAD DATA INFILE` / `LOAD XML` fire `INSERT` triggers per row.
- `REPLACE` fires, in order: `BEFORE INSERT`, then (only if a row is actually deleted) `BEFORE DELETE`/`AFTER DELETE`, then `AFTER INSERT`.
- `INSERT ... ON DUPLICATE KEY UPDATE` fires `BEFORE INSERT`, then (if the row already exists) `BEFORE UPDATE`/`AFTER UPDATE` instead of the insert path.
- `DROP TABLE`, `TRUNCATE TABLE`, and dropping a partition do **not** fire `DELETE` triggers.

## Examples

```sql
-- OR REPLACE avoids the "trigger already exists" error on redeploy
CREATE OR REPLACE DEFINER=`app_user`@`%` TRIGGER trg_limit_population
  BEFORE UPDATE ON country_stats FOR EACH ROW
BEGIN
  IF NEW.population < 1 THEN
    SET NEW.population = 1;
  ELSEIF NEW.population > 2000000000 THEN
    SET NEW.population = 2000000000;
  END IF;
END;
```

```sql
-- IF NOT EXISTS: idempotent create, warns instead of erroring if present
CREATE TRIGGER IF NOT EXISTS increment_animal
  AFTER INSERT ON animals FOR EACH ROW
  UPDATE animal_count SET animal_count.animals = animal_count.animals + 1;
```

## See Also

- **`mariadb-create-procedure`** / **`mariadb-create-function`** — shared stored-routine restriction surface (no result sets from functions, no dynamic SQL, `DELIMITER` gotcha)
- Canonical references on `mariadb.com/docs`:
  - <https://mariadb.com/docs/server/server-usage/triggers-events/triggers/create-trigger>
  - <https://mariadb.com/docs/server/server-usage/triggers-events/triggers/trigger-overview>
  - <https://mariadb.com/docs/server/server-usage/triggers-events/triggers/trigger-limitations>
  - <https://mariadb.com/docs/server/server-usage/triggers-events/triggers/triggers-and-implicit-locks>
  - <https://mariadb.com/docs/server/reference/sql-statements/data-definition/drop/drop-trigger>
