---
name: mariadb-replace
description: "MariaDB-specific syntax and behavior for REPLACE — why REPLACE is DELETE-then-INSERT (not an upsert/UPDATE), when it triggers (PRIMARY/UNIQUE conflicts only), its data-loss footguns (unlisted columns reset to DEFAULT, AUTO_INCREMENT burned, ON DELETE cascades and DELETE+INSERT triggers fired), the INSERT … ON DUPLICATE KEY UPDATE alternative, REPLACE … RETURNING, the SET and SELECT forms, PARTITION targeting, and the INSERT+DELETE privilege requirement. Use when writing, generating, or reviewing REPLACE statements, or when an upsert is being considered."
---

# REPLACE in MariaDB

*Last updated: 2026-06-24*

This skill covers `REPLACE` and its traps. `REPLACE` is a **MariaDB extension** (not standard SQL) that resolves a `PRIMARY KEY`/`UNIQUE` conflict by **deleting the conflicting row(s) and inserting a new one**. It is *not* an in-place update — that distinction is the source of nearly every `REPLACE` bug.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Anything available in current LTS branches (10.6, 10.11, 11.4, 11.8) is shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| Uses `REPLACE` to mean "upsert / update if it exists" | Use `INSERT … ON DUPLICATE KEY UPDATE`. `REPLACE` deletes the old row and inserts a new one — it does not update in place. The `ON DUPLICATE KEY UPDATE` form is what "upsert" almost always means. See `mariadb-insert` |
| Assumes columns not listed in the `REPLACE` keep their old values (UPDATE-style) | They are **reset to their `DEFAULT`** — because a brand-new row is inserted. A partial `REPLACE` silently wipes the columns you didn't mention. This is the most damaging `REPLACE` footgun |
| Writes `REPLACE … SET counter = counter + 1` expecting to read the old row | The right-hand `counter` resolves to `DEFAULT(counter)`, not the existing row's value — there is no "existing row" in a `REPLACE`. So this means `DEFAULT(counter) + 1` |
| Expects the replaced row to keep its `AUTO_INCREMENT` id | A **new** `AUTO_INCREMENT` value is generated (old row deleted), burning ids and breaking any external references to the old id |
| Assumes `REPLACE` only fires `INSERT` triggers and has no delete side effects | It fires `BEFORE DELETE` → delete → `AFTER DELETE` → then `INSERT` triggers, and it activates `ON DELETE` foreign-key actions (e.g. `ON DELETE CASCADE`) on child tables — so a `REPLACE` can cascade-delete unrelated rows |
| Thinks `REPLACE` matches on any column / the `WHERE`-like condition | It acts **only** on `PRIMARY KEY` or `UNIQUE` index conflicts. With no such index, it's a plain `INSERT`. If a row conflicts on **several** unique keys, **all** matching rows are deleted before the insert |
| Grants only `INSERT` to a user that runs `REPLACE` | `REPLACE` needs **both `INSERT` and `DELETE`** privileges on the table — a direct consequence of the delete-then-insert mechanic |
| Puts an aggregate or multi-row subquery in `RETURNING` | `RETURNING` allows per-row expressions, stored functions, and single-row/single-column subqueries, but **no aggregates** and no multi-row subqueries. Use `ROW_COUNT()` for a count |

## The upsert contrast (read this before using REPLACE)

```sql
-- REPLACE: deletes the existing row #1, inserts a fresh one.
-- → unlisted columns reset to DEFAULT, a new auto_increment id is burned,
--   ON DELETE cascades fire, DELETE+INSERT triggers fire.
REPLACE INTO t (id, name) VALUES (1, 'new');

-- ON DUPLICATE KEY UPDATE: keeps row #1, changes only `name`.
-- → other columns untouched, id preserved, no delete side effects.
INSERT INTO t (id, name) VALUES (1, 'new')
  ON DUPLICATE KEY UPDATE name = VALUE(name);
```

Reach for `REPLACE` only when you genuinely want the row fully replaced (all columns reset, side effects intended). For "insert or update," `ON DUPLICATE KEY UPDATE` is correct.

## Forms

All three forms accept `[LOW_PRIORITY | DELAYED]`, an optional `[INTO]`, an optional `PARTITION (…)`, and an optional trailing `RETURNING`. There is **no `HIGH_PRIORITY`** for `REPLACE`, and `DELAYED` is legacy (a no-op on modern engines).

```sql
-- VALUES form:
REPLACE INTO t [PARTITION (p1)] (col, …) VALUES (expr | DEFAULT, …), (…)
  [RETURNING select_expr [, …]];

-- SET form:
REPLACE INTO t SET col = {expr | DEFAULT}, … [RETURNING …];

-- SELECT form (can copy across databases via db.tbl; source ≠ target):
REPLACE INTO t (col, …) SELECT … [RETURNING …];
```

`REPLACE` cannot be combined with `ON DUPLICATE KEY UPDATE` (they're mutually exclusive duplicate-handling strategies).

## `RETURNING`

```sql
REPLACE INTO t (id, name) VALUES (1, 'new')
  RETURNING id, name, UPPER(name) AS uc;
```

Returns the newly inserted rows. Expressions, virtual columns, `AS` aliases, stored functions, single-value subqueries, and prepared statements are supported; aggregates and multi-row subqueries are not.

## See Also

- **`mariadb-insert`** — `INSERT … ON DUPLICATE KEY UPDATE` (the upsert you usually want), `INSERT IGNORE`, and the shared `RETURNING`/`PARTITION`/priority surface
- **`mariadb-create-table`** — `AUTO_INCREMENT`, `DEFAULT` expressions, and the `PRIMARY KEY`/`UNIQUE` indexes that determine when `REPLACE` fires and which columns reset
- Canonical references (consult only for edge cases not covered here):
  - `server/reference/sql-statements/data-manipulation/changing-deleting-data/replace.md` (~215 lines)
  - `…/replacereturning.md` (~110 lines)
