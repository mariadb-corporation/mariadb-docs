---
description: >-
  This guide offers conventions and practical tips for designing SQL queries
  that are easier to read, understand, and debug.
---

# Basic SQL Debugging Guide

This guide offers conventions and practical tips for designing SQL queries that are easier to read, understand, and debug. Learn about effectively using whitespace, choosing meaningful aliases, correctly placing `JOIN` conditions, and strategies for identifying and resolving common syntax errors.

Following a few conventions makes finding errors in queries a lot easier, especially when asking for help from people who might know SQL but know nothing about your particular schema. A query easy to read is a query easy to debug.

### Using Whitespace

A query that is hard to read is hard to debug. Whitespace is free; use new lines and indentation to make queries easy to read, particularly when constructing a query inside a scripting language where variables might be interspersed.

Example: Hard-to-read query with a syntax error

Can you find the error quickly in this?

```sql
SELECT u.id, u.name, alliance.ally FROM users u JOIN alliance ON (u.id=alliance.userId) JOIN team ON (alliance.teamId=team.teamId WHERE team.teamName='Legionnaires' AND u.online=1 AND ((u.subscription='paid' AND u.paymentStatus='current') OR u.subscription='free') ORDER BY u.name;
```

**Same query with better whitespace:**

Code snippet

```sql
SELECT
    u.id,
    u.name,
    alliance.ally
FROM
    users u
    JOIN alliance ON (u.id = alliance.userId)
    JOIN team ON (alliance.teamId = team.teamId  -- Error: Missing ')'
WHERE
    team.teamName = 'Legionnaires'
    AND u.online = 1
    AND (
        (u.subscription = 'paid' AND u.paymentStatus = 'current')
        OR
        u.subscription = 'free'
    )
ORDER BY
    u.name;
```

The missing closing parenthesis `)` after `team.teamId` in the second `JOIN` condition is much easier to spot with clear formatting. The exact style (commas before or after selected items, tabs vs. spaces) is less important than overall legibility.

### Table and Field Aliases

Aliases rename tables and fields within a query, useful for long names or when required (e.g., self-joins, some subqueries). Poorly chosen aliases, however, can hinder debugging. Aliases should ideally reflect the original table name.

**Bad Example (arbitrary aliases):**

Code snippet

```sql
SELECT *
FROM
    financial_reportQ_1 AS a
    JOIN sales_renderings AS b ON (a.salesGroup = b.groupId)
    JOIN sales_agents AS c ON (b.groupId = c.group)
WHERE
    b.totalSales > 10000
    AND c.id != a.clientId;
```

As the query grows, it's hard to remember what `a`, `b`, or `c` refer to without looking back.

**Better Example (meaningful aliases):**

To correct the SQL code, it should be properly formatted and structured:

```sql
SELECT *
FROM financial_report_Q_1 AS frq1
JOIN sales_renderings AS sr ON frq1.salesGroup = sr.groupId
JOIN sales_agents AS sa ON sr.groupId = sa.group
WHERE sr.totalSales > 10000
AND sa.id != frq1.clientId;
```

This query selects all data from `financial_report_Q_1` and joins `sales_renderings` and `sales_agents` using specified conditions. It filters for total sales greater than 10,000 and excludes records where the sales agent's ID matches

````sql

Using initials or recognizable abbreviations (e.g., `frq1` for `financial_report_Q_1`) makes the query more understandable.

## Placing JOIN Conditions

The `ON` clause of a `JOIN` should specify the conditions that link the tables. Avoid using it for filtering rows that belong in the `WHERE` clause. Conversely, avoid placing all join logic in the `WHERE` clause (as common with older, implicit join syntax).

**Bad Example (join condition mixed in `WHERE`):**

```sql
SELECT *
FROM
    family,
    relationships
WHERE
    family.personId = relationships.personId -- Join condition
    AND relationships.relation = 'father';   -- Filtering condition
````

It's unclear how `family` and `relationships` are linked without parsing the entire `WHERE` clause.

**Better Example (clear separation):**

```sql
SELECT *
FROM
    family
    JOIN relationships ON (family.personId = relationships.personId) -- Join condition
WHERE
    relationships.relation = 'father'; -- Filtering condition
```

The table relationship is obvious in the `JOIN ... ON` clause. The `WHERE` clause is reserved for filtering the result set. Always use explicit `JOIN` keywords (`INNER JOIN`, `LEFT JOIN`, etc.) instead of commas for joining tables, and do not mix these styles.

### Finding Syntax Errors

MariaDB's error messages usually point to where the parser got confused. Check the query around the indicated point.

Interpreting the "Empty Error"

An error like ERROR 1064: ... syntax to use near '' at line 1 can be tricky. The empty ' ' often means the parser reached the end of the statement while expecting more tokens.

*   Check for missing closing characters like quotes `'` or parentheses `)`.SQL

    ```sql
    SELECT * FROM someTable WHERE field = 'value -- Missing closing quote
    ```
*   Look for incomplete clauses, often indicated by a trailing comma.SQL

    ```sql
    SELECT * FROM someTable WHERE field = 1 GROUP BY id, -- Incomplete GROUP BY
    ```

Checking for Reserved Keywords

If an identifier (table name, column name, alias) is a MariaDB reserved word, it must be enclosed in backticks (\`) to avoid ambiguity.

```sql
SELECT * FROM actionTable WHERE `DELETE` = 1; -- `DELETE` is a reserved word
```

A text editor with SQL syntax highlighting can help spot these. Common identifiers that are also keywords include:

* `DESC` (often for "description", but means "descending" in `ORDER BY`)
* `DATE`, `TIME`, `TIMESTAMP` (data types)
* `ORDER` (used in sales contexts, but is an SQL clause)

It's a good practice to quote any identifier that is also a keyword, even if MariaDB might allow some unquoted in certain contexts.

Version-Specific Syntax

SQL syntax evolves. Features and syntax available in newer MariaDB versions might not work in older ones, and vice-versa (though less common).

* **New syntax in old versions:** Web hosts may run older MariaDB versions. A query working on your newer local setup might fail in an older production environment.
  * Subqueries (e.g., `WHERE someId IN (SELECT id FROM ...))` were added in MySQL 4.1.
  * Early `JOIN` syntax did not always allow an `ON` clause.
* **Old syntax in new versions:** Sometimes, changes in operator precedence or syntax deprecation can cause issues. For example, the precedence of the comma operator relative to `JOIN` changed in MySQL 5.0. A query like `SELECT * FROM a, b JOIN c ON a.x = c.x;` that worked before might fail or produce different results.

Always check the MariaDB server version you are targeting and consult the manual for that version to ensure syntax compatibility. The manual usually indicates when specific syntax features became available.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
