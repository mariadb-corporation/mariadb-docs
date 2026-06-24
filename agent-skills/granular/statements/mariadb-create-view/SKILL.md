---
name: mariadb-create-view
description: "MariaDB-specific syntax and behavior for views — CREATE OR REPLACE VIEW vs CREATE VIEW IF NOT EXISTS (mutually exclusive), ALGORITHM = UNDEFINED/MERGE/TEMPTABLE and its effect on updatability and performance, the SQL SECURITY DEFINER default, WITH CASCADED/LOCAL CHECK OPTION, what makes a view updatable/insertable, frozen-at-creation definitions, and ALTER VIEW / DROP VIEW. Use when writing, generating, or reviewing CREATE VIEW / ALTER VIEW / DROP VIEW statements that target MariaDB."
---

# CREATE VIEW in MariaDB

*Last updated: 2026-06-24*

This skill covers the **delta between standard SQL views and MariaDB's** — the view-definition options, updatability rules, and security semantics that trip up generated SQL. It assumes the agent already knows the basic `CREATE VIEW v AS SELECT …` form. The view body is a `SELECT`; for its clauses see `mariadb-select`.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Anything available in current LTS branches (10.6, 10.11, 11.4, 11.8) is shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| `DROP VIEW x; CREATE VIEW x …` to redefine a view | `CREATE OR REPLACE VIEW x AS …` — atomic, no window where the view is missing. (`ALTER VIEW x AS …` also works when it already exists) |
| `CREATE OR REPLACE VIEW IF NOT EXISTS …`, assuming the two combine | Hard error (`ER_WRONG_USAGE`). `OR REPLACE` and `IF NOT EXISTS` are mutually exclusive — pick one |
| Omits `SQL SECURITY`, expecting the caller's privileges to apply | The default is **`SQL SECURITY DEFINER`** — the view executes with the *definer's* privileges, not the invoker's. For caller-privilege semantics you must write `SQL SECURITY INVOKER` explicitly |
| Treats any view as updatable / `INSERT`-able | A view is **not** updatable if its `SELECT` uses an aggregate, `DISTINCT`, `GROUP BY`, `HAVING`, `UNION`, a subquery in the select list, an outer join, references no base table, or refers to one base-table column more than once. `ALGORITHM = TEMPTABLE` is never updatable |
| Sets `ALGORITHM = TEMPTABLE` on a view it then writes through | `TEMPTABLE` views are never updatable; only `MERGE` (or an `UNDEFINED` view the optimizer can merge) can be written through |
| `INSERT`s through a view whose columns are expressions (`col + 1`, `LOWER(col)`, literals) | Insertable views need every column to be a plain base-table column, must include all `NOT NULL`/no-default base columns, and may not repeat a base column. Otherwise `ERROR 1348: Column is not updatable` |
| Bare `WITH CHECK OPTION` on a view built on another view, expecting only the local predicate to be checked | Bare `WITH CHECK OPTION` means **`CASCADED`** (checks this view *and* all underlying views). Use `WITH LOCAL CHECK OPTION` to check only this view's predicate |
| Puts `ORDER BY` inside the view to guarantee output order | The view's `ORDER BY` is **ignored** whenever the outer query has its own `ORDER BY`. Don't rely on in-view ordering — sort in the query that reads the view |
| Expects `SELECT *` in a view to pick up columns added to the base table later | The definition is **frozen at creation**: `SELECT *` is expanded to the columns that existed then. New base-table columns don't appear until you recreate the view |
| Tries to index a view, or `CREATE TEMPORARY VIEW`, or put a subquery in the view's `FROM` | None are allowed. Index the underlying base table; there is no temporary view; a view's `SELECT` can't have a derived table in `FROM` |
| Leaves expression columns unnamed | Every view column needs a unique name — give expressions an alias, or supply an explicit `(column_list)` whose length matches the select list |

## Syntax

```sql
CREATE
    [OR REPLACE]
    [ALGORITHM = {UNDEFINED | MERGE | TEMPTABLE}]
    [DEFINER = { user | CURRENT_USER | role | CURRENT_ROLE }]
    [SQL SECURITY { DEFINER | INVOKER }]
    VIEW [IF NOT EXISTS] view_name [(column_list)]
    AS select_statement
    [WITH [CASCADED | LOCAL] CHECK OPTION];
```

Clause order is fixed (`OR REPLACE` → `ALGORITHM` → `DEFINER` → `SQL SECURITY` → `VIEW`). `DEFINER` accepts a role or `CURRENT_ROLE`, not just a user. `CREATE VIEW` is atomic DDL.

## `ALGORITHM`

| Algorithm | Behavior |
|---|---|
| `MERGE` | The view text is merged into the referencing query. More efficient, and **required for an updatable view**. Not possible if the view uses `GROUP BY`, `HAVING`, `LIMIT`, `DISTINCT`, `UNION`, an aggregate, or a select-list subquery |
| `TEMPTABLE` | The view result is materialized into a temporary table. Never updatable; can release underlying locks earlier |
| `UNDEFINED` (default) | The server chooses, preferring `MERGE` and falling back to a temp table when the shape forbids merging |

## Updatable views and `WITH CHECK OPTION`

When a view is updatable, `WITH CHECK OPTION` rejects writes that would produce rows the view can't see:

```sql
CREATE VIEW active AS SELECT * FROM users WHERE status = 'active' WITH CHECK OPTION;
-- INSERT/UPDATE that sets status <> 'active' → ERROR 1369: CHECK OPTION failed
```

For views layered on views, `LOCAL` checks only this view's predicate; `CASCADED` (the default) also checks every underlying view's predicate.

## `ALTER VIEW` and `DROP VIEW`

```sql
ALTER VIEW view_name [(column_list)] AS select_statement …;   -- same options as CREATE, minus OR REPLACE / IF NOT EXISTS
DROP VIEW [IF EXISTS] view_name [, view_name] … [RESTRICT | CASCADE];
```

- `ALTER VIEW` is equivalent to `CREATE OR REPLACE VIEW` on an existing view.
- In `DROP VIEW`, `RESTRICT` and `CASCADE` are **parsed but ignored** (accepted only for syntax compatibility).
- `DROP VIEW IF EXISTS` downgrades a missing view to a note; in a multi-view drop, existing views are still dropped.

## See Also

- **`mariadb-select`** — the view body is a `SELECT`; the clauses that make a view non-updatable or non-mergeable are all `SELECT` features
- **`mariadb-create-table`** — shares the `CREATE OR REPLACE` / `IF NOT EXISTS` atomic-DDL model and the same mutual-exclusion rule
- **`mariadb-query-optimization`** (topical) — when the `MERGE` vs `TEMPTABLE` choice matters for performance
- **`mariadb-system-versioned-tables`** (topical) — a view adds no row history; put `WITH SYSTEM VERSIONING` on the base table and query it with `FOR SYSTEM_TIME`
- Canonical references on `mariadb.com/docs` (consult only for edge cases not covered here):
  - <https://mariadb.com/docs/server/server-usage/views/create-view>
  - <https://mariadb.com/docs/server/server-usage/views/view-algorithms>
  - <https://mariadb.com/docs/server/server-usage/views/inserting-and-updating-with-views>
  - <https://mariadb.com/docs/server/server-usage/views/alter-view>
  - <https://mariadb.com/docs/server/server-usage/views/drop-view>
