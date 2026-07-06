---
name: mariadb-aggregate-functions
description: "MariaDB aggregate functions — calculations across a set of rows (typically with GROUP BY or as window functions via OVER()). Covers counting (COUNT, COUNT(DISTINCT)), totals/averages (SUM, AVG), extrema (MIN, MAX), string aggregation (GROUP_CONCAT with DISTINCT/ORDER BY/SEPARATOR/LIMIT), bitwise aggregation (BIT_AND, BIT_OR, BIT_XOR), and the statistical family (STD/STDDEV/STDDEV_POP, STDDEV_SAMP, VARIANCE/VAR_POP, VAR_SAMP). Use when summarizing or rolling up rows in MariaDB. Note aggregates skip NULLs, GROUP_CONCAT silently truncates at group_concat_max_len, and ONLY_FULL_GROUP_BY is not in the default sql_mode."
---

# MariaDB Aggregate Functions

*Last updated: 2026-06-24*

Catalog of every built-in aggregate function in MariaDB, with signature and a one-line semantic summary per entry. For a function not listed here, fall back to the canonical reference at <https://mariadb.com/docs/server/reference/sql-functions/aggregate-functions>. For `GROUP BY`, `HAVING`, `WITH ROLLUP`, and window-function `OVER()` mechanics, see `mariadb-select`.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Functions with a `*(since X.Y)*` annotation are only available from that version onward; everything else is in every current LTS branch (10.6, 10.11, 11.4, 11.8).

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| `COUNT(col)` counts every row, the same as `COUNT(*)` | `COUNT(*)` counts **all rows** (including `NULL`s); `COUNT(expr)` counts only **non-NULL** `expr`; `COUNT(DISTINCT expr)` counts distinct non-NULL values. All three can differ on the same column |
| `SUM`/`AVG`/`MIN`/`MAX` factor `NULL` rows into the result | Every aggregate except `COUNT(*)` **skips `NULL`** rows. `AVG(col)` is sum-of-non-null ÷ count-of-non-null — `NULL`s change the denominator, not just the numerator |
| `SUM`/`AVG` over an empty set returns `0` | On no matching rows, `SUM`, `AVG`, `MIN`, `MAX`, `GROUP_CONCAT`, and the `STDDEV`/`VAR` family return **`NULL`**; only `COUNT` returns `0` |
| `GROUP_CONCAT(...)` returns the full concatenation | Output is silently capped at **`group_concat_max_len` (default 1 MB)** and truncated. A truncation **warning** is raised (not an error) — check `SHOW WARNINGS`, or raise the variable |
| `GROUP_CONCAT` is plain concatenation with no ordering or dedup | It takes `[DISTINCT]`, `ORDER BY`, `SEPARATOR str` (default comma; `SEPARATOR ''` for none), and `LIMIT`, all inside the call: `GROUP_CONCAT(DISTINCT x ORDER BY y SEPARATOR '; ' LIMIT 10)` |
| Selecting non-grouped columns will be rejected (ONLY_FULL_GROUP_BY) | MariaDB's **default `sql_mode` does not include `ONLY_FULL_GROUP_BY`**, so the query runs and returns an **arbitrary** row's value per group — a silent-bug source. Add the column to `GROUP BY`, or enable `ONLY_FULL_GROUP_BY` to make it an error |
| `STDDEV(x)` / `STD(x)` is the sample standard deviation | `STD`, `STDDEV`, and `STDDEV_POP` all return the **population** standard deviation (÷N). For the sample value (÷N−1) use `STDDEV_SAMP`. Likewise `VARIANCE`/`VAR_POP` are population; `VAR_SAMP` is sample |
| Any aggregate works as a window function with `OVER()` | Most do (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`, `BIT_*`, the stats family). But `SUM`/`AVG` **with `DISTINCT`** cannot be window functions, and `JSON_ARRAYAGG`/`JSON_OBJECTAGG` cannot either |
| `MIN(enum_col)` / `MAX(enum_col)` orders by the declared `ENUM` order | `MIN`/`MAX` compare `ENUM`/`SET` by **string value**, not declared position — the result can differ from `ORDER BY enum_col LIMIT 1` |
| `BIT_AND`/`BIT_OR`/`BIT_XOR` work at the column's native width | They always compute at **64-bit** precision and ignore `NULL`s. On an all-`NULL`/empty set they return the identity (`BIT_AND` → all bits set, `BIT_OR`/`BIT_XOR` → 0) |
| Aggregating JSON needs a custom function | Use `JSON_ARRAYAGG` / `JSON_OBJECTAGG` — but they're catalogued under **`mariadb-json-functions`** (they live in the JSON tree), and their output is also bounded by `group_concat_max_len` |

For `COUNT(DISTINCT expr [, expr...])` specifically, note it counts distinct **non-NULL** combinations across the listed expressions.

## Functions

Auto-generated from the canonical `server/reference/sql-functions/aggregate-functions/` pages by `agent-skills/extractor/extract_function_category.py`; regenerate when the doc tree changes. Do not hand-edit between the markers. (The JSON aggregates `JSON_ARRAYAGG`/`JSON_OBJECTAGG` live in the JSON tree — see `mariadb-json-functions`.)

<!-- BEGIN GENERATED -->
<!-- Extracted from server/reference/sql-functions/aggregate-functions -->
<!-- 16 functions, 1 pages skipped on extraction failure -->

### AVG
`AVG([DISTINCT] expr)`  
Returns the average value of expr.

### BIT_AND
`BIT_AND(expr) [over_clause]`  
Returns the bitwise AND of all bits in _expr_.

### BIT_OR
`BIT_OR(expr) [over_clause]`  
Returns the bitwise OR of all bits in `expr`.

### BIT_XOR
`BIT_XOR(expr) [over_clause]`  
Returns the bitwise XOR of all bits in `expr`.

### COUNT
`COUNT(expr)`  
Returns a count of the number of non-NULL values of expr in the rows retrieved by a SELECT statement.

### GROUP_CONCAT
`GROUP_CONCAT(expr)`  
This function returns a string result with the concatenated non-NULL values from a group.

### MAX
`MAX([DISTINCT] expr)`  
Returns the largest, or maximum, value of _`expr`_.

### MIN
`MIN([DISTINCT] expr)`  
Returns the minimum value of _`expr`_.

### STD
`STD(expr)`  
Returns the population standard deviation of _`expr`_.

### STDDEV
`STDDEV(expr)`  
Returns the population standard deviation of _`expr`_.

### STDDEV_POP
`STDDEV_POP(expr)`  
Returns the population standard deviation of _`expr`_ (the square root of VAR_POP()).

### STDDEV_SAMP
`STDDEV_SAMP(expr)`  
Returns the sample standard deviation of `expr` (the square root of VAR_SAMP()).

### SUM
`SUM([DISTINCT] expr)`  
Returns the sum of _`expr`_.

### VARIANCE
`VARIANCE(expr)`  
Returns the population standard variance of `expr`.

### VAR_POP
`VAR_POP(expr)`  
Returns the population standard variance of `expr`.

### VAR_SAMP
`VAR_SAMP(expr)`  
Returns the sample variance of _`expr`_.
<!-- END GENERATED -->

## See Also

- **`mariadb-select`** — `GROUP BY`, `HAVING`, `WITH ROLLUP`, and window-function `OVER()` mechanics; the `ONLY_FULL_GROUP_BY` interaction
- **`mariadb-json-functions`** — `JSON_ARRAYAGG` / `JSON_OBJECTAGG`
- **`mariadb-string-functions`** — non-aggregate string building (`CONCAT`, `CONCAT_WS`)
- Canonical reference on `mariadb.com/docs`: <https://mariadb.com/docs/server/reference/sql-functions/aggregate-functions>
