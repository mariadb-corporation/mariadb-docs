---
name: mariadb-window-functions
description: "MariaDB window functions — ranking (ROW_NUMBER, RANK, DENSE_RANK, PERCENT_RANK, CUME_DIST, NTILE), value navigation (LAG, LEAD, FIRST_VALUE, LAST_VALUE, NTH_VALUE), and ordered-set/inverse-distribution functions (MEDIAN, PERCENTILE_CONT, PERCENTILE_DISC), plus the OVER (PARTITION BY ... ORDER BY ... frame) clause, named windows (WINDOW w AS (...)), and ROWS/RANGE window frames. Use when writing SQL that ranks or paginates rows, computes running totals or moving aggregates, compares a row to its neighbors, or computes percentiles/medians in MariaDB."
---

# MariaDB Window Functions

*Last updated: 2026-07-20*

Catalog of MariaDB's dedicated window functions and the `OVER (...)` clause, with signature and a one-line semantic summary per entry. Any aggregate function (`SUM`, `AVG`, `COUNT`, `MIN`, `MAX`, `STD`, `VARIANCE`, ...) can also run as a window function by adding `OVER (...)` — those aren't re-listed here (see the **`mariadb-aggregate-functions`** skill). `PERCENTILE_CONT` and `PERCENTILE_DISC` use the `WITHIN GROUP (ORDER BY ...)` ordered-set syntax and their canonical doc pages carry no parsable syntax block, so both are **skipped by the catalog extractor** below — see their canonical pages linked in See Also for full syntax and examples. For a function, frame form, or clause not listed here, fall back to the canonical reference at <https://mariadb.com/docs/server/reference/sql-functions/special-functions/window-functions>.

> **Default context:** Assume MariaDB **11.8 LTS** unless the user specifies
> another version. All functions in this category (window functions were
> introduced in 10.2) are available in every current LTS branch (10.6, 10.11,
> 11.4, 11.8); no `*(since X.Y)*` annotations apply here.

## What LLMs Often Miss

| If the agent writes… | Prefer (MariaDB) | Why |
| --- | --- | --- |
| `SELECT * FROM t WHERE ROW_NUMBER() OVER (...) = 1` (or in `HAVING`/`GROUP BY`) | Compute the window function in a subquery or CTE, then filter in the outer query: `SELECT * FROM (SELECT *, ROW_NUMBER() OVER (...) AS rn FROM t) x WHERE rn = 1` | Window functions are evaluated after `WHERE`/`GROUP BY`/`HAVING`, and MariaDB rejects them there outright — server error: "Window function is allowed only in SELECT list and ORDER BY clause" |
| Treating `ROW_NUMBER()`, `RANK()`, and `DENSE_RANK()` as interchangeable for "top N per group" | Pick deliberately: `ROW_NUMBER()` always gives distinct 1..N (arbitrarily breaks ties); `RANK()` gives ties the same value and **skips** subsequent ranks (1,2,2,4); `DENSE_RANK()` gives ties the same value with **no gaps** (1,2,2,3) | Silent correctness bug if the wrong one is picked for tie-heavy data — e.g. "top 2 per partition" behaves differently under `RANK` vs `ROW_NUMBER` when there's a tie for 2nd place |
| `SUM(x) OVER (ORDER BY y)` expecting each row to see the whole partition | With an `ORDER BY` and no explicit frame, the default frame is `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` — a running total, not a partition-wide sum. Add an explicit frame (or drop `ORDER BY`) for a whole-partition aggregate | Classic footgun: `LAST_VALUE(x) OVER (ORDER BY y)` under the default frame returns the **current row's** value (since "last row in frame" = current row), not the partition's actual last row — use an explicit `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING` frame to get the true last value |
| `LAG(col) OVER (PARTITION BY p)` with no `ORDER BY` | `ORDER BY` is mandatory in the `OVER (...)` clause for `LAG`/`LEAD` (and for `RANK`, `DENSE_RANK`, `PERCENT_RANK`, `CUME_DIST`, `PERCENTILE_CONT`, `PERCENTILE_DISC`) — omitting it is an error. Default offset is `1`; default fill value is `NULL`; offset `0` means the current row; negative offsets flip `LAG`↔`LEAD` direction | Doc pages render `ORDER BY` in `[...]` (optional-looking) BNF for these functions, but the server enforces it — `ROW_NUMBER()`, `NTILE()`, `FIRST_VALUE`, `LAST_VALUE`, and `NTH_VALUE` are the ones that genuinely tolerate omitting it |
| `MEDIAN(x) OVER (PARTITION BY p ORDER BY x)` or `PERCENTILE_CONT(0.5) OVER (ORDER BY x)` | Ordering for `MEDIAN`/`PERCENTILE_CONT`/`PERCENTILE_DISC` goes in `WITHIN GROUP (ORDER BY expr)`, not in `OVER (...)`. The `OVER (...)` clause for these three accepts **`PARTITION BY` only** — no `ORDER BY`, no frame: `PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY x) OVER (PARTITION BY p)`. `MEDIAN(x) OVER (...)` is sugar for exactly that with the percentile fixed at `0.5` | Putting `ORDER BY` inside `OVER (...)` for these functions is a parse error, not a silent no-op |
| `... RANGE BETWEEN INTERVAL 1 DAY PRECEDING AND CURRENT ROW` over `ORDER BY a, b` | `RANGE`-type frames with an explicit numeric/interval bound (`n PRECEDING`/`FOLLOWING`) require the window's `ORDER BY` to be exactly **one** sort key — multiple columns are an error. `RANGE` frames also don't support `DATE`/`DATETIME` arithmetic in the bound | Use `ROWS` instead of `RANGE` for multi-column-ordered or date-arithmetic frames |
| `... EXCLUDE CURRENT ROW`, a `GROUPS`-type frame, or `ORDER BY x NULLS LAST` | Not available in MariaDB. `GROUPS` frames and `NULLS FIRST`/`NULLS LAST` aren't even parsed; `EXCLUDE ...` parses but is rejected at runtime ("Frame exclusion is not supported yet") | Don't propose these as drop-in equivalents to standard-SQL frame exclusion — there's no MariaDB workaround beyond restructuring the frame bounds or a `CASE` expression |
| Repeating the same `OVER (PARTITION BY ... ORDER BY ...)` for several window functions in one query | Define it once with `WINDOW w AS (PARTITION BY ... ORDER BY ...)` and reference `OVER w` per function | Also lets MariaDB's optimizer reuse a single sort pass across window functions with identical or prefix-compatible `PARTITION BY`/`ORDER BY` specs — repeating slightly different specs by hand can force extra `filesort` passes |
| `AVG(DISTINCT x) OVER (...)` or `COUNT(DISTINCT x) OVER (...)` | Not supported — `DISTINCT` inside an aggregate function used as a window function is rejected. Deduplicate in a subquery first if you need distinct-value aggregation per window | Aggregate functions gain `OVER (...)` support, not full standard-SQL window-aggregate semantics |

## Functions

<!-- BEGIN GENERATED -->
<!-- Extracted from server/reference/sql-functions/special-functions/window-functions -->
<!-- 11 functions, 5 pages skipped on extraction failure -->

### CUME_DIST
`CUME_DIST() OVER (`  
`CUME_DIST()` is a window function that returns the cumulative distribution of a given row.

### DENSE_RANK
`DENSE_RANK() OVER (`  
`DENSE_RANK()` is a window function that displays the number of a given row, starting at one and following the ORDER BY sequence of the window function, with identical values receiving the same result.

### FIRST_VALUE
`FIRST_VALUE(expr) OVER (`  
`FIRST_VALUE` returns the first result from an ordered set, or NULL if no such result exists.

### LAG
`LAG (expr[, offset]) OVER (`  
The `LAG` function accesses data from a previous row according to the `ORDER BY` clause without the need for a self-join.

### LEAD
`LEAD (expr[, offset]) OVER (`  
The `LEAD` function accesses data from a following row in the same result set without the need for a self-join.

### MEDIAN
`MEDIAN(median expression) OVER (`  
`MEDIAN()` is a window function that returns the median value of a range of values.

### NTH_VALUE
`NTH_VALUE (expr[, num_row]) OVER (`  
The `NTH_VALUE` function returns the value evaluated at row number `num_row` of the window frame, starting from 1, or `NULL` if the row does not exist.

### NTILE
`NTILE (expr) OVER (`  
`NTILE()` is a window function that returns an integer indicating which group a given row falls into.

### PERCENT_RANK
`PERCENT_RANK() OVER (`  
`PERCENT_RANK()` is a window function that returns the relative percent rank of a given row.

### RANK
`RANK() OVER (`  
RANK() is a window function that displays the number of a given row, starting at one and following the ORDER BY sequence of the window function, with identical values receiving the same result.

### ROW_NUMBER
`ROW_NUMBER() OVER (`  
`ROW_NUMBER()` is a window function that displays the number of a given row, starting at one and following the ORDER BY sequence of the window function, with identical values receiving different row numbers.
<!-- END GENERATED -->

## See Also

- **`mariadb-aggregate-functions`** — `SUM`, `AVG`, `COUNT`, `MIN`, `MAX`, `STD`/`STDDEV`/`STDDEV_POP`/`STDDEV_SAMP`, `VAR_POP`/`VAR_SAMP`/`VARIANCE`, `BIT_AND`/`BIT_OR`/`BIT_XOR` — all usable as window functions via `OVER (...)`
- **`mariadb-select`** — `SELECT` clause ordering (window functions evaluate after `WHERE`/`GROUP BY`/`HAVING`, before the final `ORDER BY`/`LIMIT`)
- Canonical references on `mariadb.com/docs`:
  - <https://mariadb.com/docs/server/reference/sql-functions/special-functions/window-functions>
  - <https://mariadb.com/docs/server/reference/sql-functions/special-functions/window-functions/window-frames>
  - <https://mariadb.com/docs/server/reference/sql-functions/special-functions/window-functions/percentile_cont>
  - <https://mariadb.com/docs/server/reference/sql-functions/special-functions/window-functions/percentile_disc>
