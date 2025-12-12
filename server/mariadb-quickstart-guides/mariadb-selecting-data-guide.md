---
description: >-
  This guide explains the SELECT statement in detail, covering how to retrieve,
  filter, limit, and sort data from your MariaDB database.
---

# Getting Data Guide

This guide explains how to retrieve data from MariaDB using the `SELECT` statement, progressing from basic syntax to more involved queries. Learn to select specific columns, limit results, filter with `WHERE`, sort with `ORDER BY`, join tables, and use various helpful options and functions.

### Setup: Creating and Populating Example Tables

To follow the examples, first create and populate the `books` and `authors` tables:

{% code expandable="true" %}
```sql
CREATE OR REPLACE TABLE books (
    isbn CHAR(20) PRIMARY KEY,
    title VARCHAR(50),
    author_id INT,
    publisher_id INT,
    year_pub CHAR(4),
    description TEXT
);

CREATE OR REPLACE TABLE authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    name_last VARCHAR(50),
    name_first VARCHAR(50),
    country VARCHAR(50)
);

INSERT INTO authors (name_last, name_first, country) VALUES
  ('Kafka', 'Franz', 'Czech Republic'),
  ('Dostoevsky', 'Fyodor', 'Russia');

INSERT INTO books (title, author_id, isbn, year_pub) VALUES
 ('The Trial', 1, '0805210407', '1995'),
 ('The Metamorphosis', 1, '0553213695', '1995'),
 ('America', 2, '0805210644', '1995'), -- Note: Original data had author_id 2 for 'America', Dostoevsky is author_id 2.
 ('Brothers Karamozov', 2, '0553212168', ''),
 ('Crime & Punishment', 2, '0679420290', ''),
 ('Crime & Punishment', 2, '0553211757', ''),
 ('Idiot', 2, '0192834118', ''),
 ('Notes from Underground', 2, '067973452X', '');
```
{% endcode %}

### Basic Data Retrieval

Selecting All Columns:

Use \* to select all columns from a table.

```sql
SELECT * FROM books;
```

**Output (example):**

```
+------------+------------------------+-----------+--------------+----------+-------------+
| isbn       | title                  | author_id | publisher_id | year_pub | description |
+------------+------------------------+-----------+--------------+----------+-------------+
| 0192834118 | Idiot                  |         2 |         NULL |          | NULL        |
| 0553211757 | Crime & Punishment     |         2 |         NULL |          | NULL        |
... (other rows)
| 0805210644 | America                |         2 |         NULL | 1995     | NULL        |
+------------+------------------------+-----------+--------------+----------+-------------+
8 rows in set (0.001 sec)
```

Selecting Specific Columns:

List the column names separated by commas.

```sql
SELECT isbn, title, author_id FROM books;
```

**Output (example):**

```
+------------+------------------------+-----------+
| isbn       | title                  | author_id |
+------------+------------------------+-----------+
| 0192834118 | Idiot                  |         2 |
| 0553211757 | Crime & Punishment     |         2 |
... (other rows)
+------------+------------------------+-----------+
8 rows in set (0.001 sec)
```

**Limiting the Number of Rows with `LIMIT`:**

*   To get the first `N` rows:

    ```sql
    SELECT isbn, title, author_id FROM books LIMIT 5;
    ```

    **Output (example):**

    ```
    +------------+--------------------+-----------+
    | isbn       | title              | author_id |
    +------------+--------------------+-----------+
    | 0192834118 | Idiot              |         2 |
    | 0553211757 | Crime & Punishment |         2 |
    | 0553212168 | Brothers Karamozov |         2 |
    | 0553213695 | The Metamorphosis  |         1 |
    | 0679420290 | Crime & Punishment |         2 |
    +------------+--------------------+-----------+
    5 rows in set (0.001 sec)
    ```
*   To get `N` rows starting from an offset (offset is 0-indexed):SQL

    ```sql
    SELECT isbn, title, author_id FROM books LIMIT 5, 10; -- Skip 5 rows, show next 10 (or fewer if less remain)
    ```

    **Output (example, assuming only 3 more rows exist after offset 5):**

    ```
    +------------+------------------------+-----------+
    | isbn       | title                  | author_id |
    +------------+------------------------+-----------+
    | 067973452X | Notes from Underground |         2 |
    | 0805210407 | The Trial              |         1 |
    | 0805210644 | America                |         2 |
    +------------+------------------------+-----------+
    3 rows in set (0.001 sec)
    ```

### Filtering and Ordering Results

Filtering with `WHERE`:

Use the `WHERE` clause to specify conditions for row selection.

```sql
SELECT isbn, title
FROM books
WHERE author_id = 2
LIMIT 5;
```

**Output (example):**

```
+------------+------------------------+
| isbn       | title                  |
+------------+------------------------+
| 0192834118 | Idiot                  |
| 0553211757 | Crime & Punishment     |
| 0553212168 | Brothers Karamozov     |
| 0679420290 | Crime & Punishment     |
| 067973452X | Notes from Underground |
+------------+------------------------+
5 rows in set (0.000 sec)
```

Ordering with `ORDER BY`:

Use `ORDER BY column_name [ASC|DESC]` to sort the result set.

```sql
SELECT isbn, title
FROM books
WHERE author_id = 2
ORDER BY title ASC
LIMIT 5;
```

**Output (example):**

```
+------------+--------------------+
| isbn       | title              |
+------------+--------------------+
| 0805210644 | America            |
| 0553212168 | Brothers Karamozov |
| 0553211757 | Crime & Punishment |
| 0679420290 | Crime & Punishment |
| 0192834118 | Idiot              |
+------------+--------------------+
5 rows in set (0.001 sec)
```

* `ASC` (ascending) is the default order. `DESC` is for descending order.
* You can order by multiple columns: `ORDER BY col1 ASC, col2 DESC`.
* **Clause Order:** `SELECT ... FROM ... WHERE ... ORDER BY ... LIMIT ...`. MariaDB generally processes `WHERE`, then `ORDER BY`, then `LIMIT`.

### Working with Multiple Tables (JOINs) and Functions

Joining Tables:

Use JOIN to combine rows from two or more tables based on a related column.

```sql
SELECT isbn, title, CONCAT(name_first, ' ', name_last) AS author
FROM books
JOIN authors USING (author_id) -- Assumes 'author_id' column exists in both tables
WHERE name_last = 'Dostoevsky'
ORDER BY title ASC
LIMIT 5;
```

**Output (example):**

```
+------------+--------------------+-------------------+
| isbn       | title              | author            |
+------------+--------------------+-------------------+
| 0805210644 | America            | Fyodor Dostoevsky |
| 0553212168 | Brothers Karamozov | Fyodor Dostoevsky |
| 0553211757 | Crime & Punishment | Fyodor Dostoevsky |
| 0679420290 | Crime & Punishment | Fyodor Dostoevsky |
| 0192834118 | Idiot              | Fyodor Dostoevsky |
+------------+--------------------+-------------------+
5 rows in set (0.00 sec)
```

* Alternative `JOIN` syntax: `... JOIN authors ON books.author_id = authors.author_id ...`. For more on joins, see the [JOIN Syntax documentation](../reference/sql-statements/data-manipulation/selecting-data/joins/join-syntax.md) or a "Basic Joins Guide".
* **`CONCAT(str1, str2, ...)`:** Concatenates strings.
* **`AS alias_name`:** Assigns an alias to an output column.

Pattern Matching with LIKE:

Use LIKE in the WHERE clause for pattern matching. % is a wildcard for zero or more characters.

```sql
SELECT isbn, title, CONCAT(name_first, ' ', name_last) AS author
FROM books
JOIN authors USING (author_id)
WHERE name_last LIKE 'Dostoevsk%'
ORDER BY title ASC
LIMIT 5;
```

**Output (example, same as above if only Dostoevsky matches):**

```
+------------+--------------------+-------------------+
| isbn       | title              | author            |
+------------+--------------------+-------------------+
| 0805210644 | America            | Fyodor Dostoevsky |
| 0553212168 | Brothers Karamozov | Fyodor Dostoevsky |
| 0553211757 | Crime & Punishment | Fyodor Dostoevsky |
| 0679420290 | Crime & Punishment | Fyodor Dostoevsky |
| 0192834118 | Idiot              | Fyodor Dostoevsky |
+------------+--------------------+-------------------+
5 rows in set (0.001 sec)
```

### SELECT Statement Modifiers

Place these modifiers immediately after the `SELECT` keyword.

*   **`ALL` vs `DISTINCT`:**

    * `ALL` (default): Returns all rows that meet the criteria.
    * `DISTINCT`: Returns only unique rows for the selected columns. If multiple identical rows are found for the specified columns, only the first one is displayed.

    ```sql
    SELECT DISTINCT title
    FROM books
    JOIN authors USING (author_id)
    WHERE name_last = 'Dostoevsky'
    ORDER BY title;
    ```

    **Output (example, showing one "Crime & Punishment"):**

    ```
    +------------------------+
    | title                  |
    +------------------------+
    | America                |
    | Brothers Karamozov     |
    | Crime & Punishment     |
    | Idiot                  |
    | Notes from Underground |
    +------------------------+
    ```
*   `HIGH_PRIORITY`:

    Gives the `SELECT` statement higher priority over concurrent data modification statements (use with caution as it can impact write performance).

    SQL

    ```sql
    SELECT DISTINCT HIGH_PRIORITY title
    FROM books
    JOIN authors USING (author_id)
    WHERE name_last = 'Dostoevsky'
    ORDER BY title;
    ```
*   `SQL_CALC_FOUND_ROWS` and `FOUND_ROWS():`

    To find out how many rows a query would have returned without a `LIMIT` clause, use `SQL_CALC_FOUND_ROWS` in your `SELECT` statement, and then execute `SELECT` `FOUND_ROWS()`; immediately after.

    ```sql
    SELECT SQL_CALC_FOUND_ROWS isbn, title
    FROM books
    JOIN authors USING (author_id)
    WHERE name_last = 'Dostoevsky'
    ORDER BY title -- Order before limit to ensure consistent FOUND_ROWS() for a given query logic
    LIMIT 5;
    ```

    **Output (example for the first query):**

    ```
    +------------+------------------------+
    | isbn       | title                  |
    +------------+------------------------+
    | 0805210644 | America                |
    | 0553212168 | Brothers Karamozov     |
    | 0553211757 | Crime & Punishment     |
    | 0679420290 | Crime & Punishment     |
    | 0192834118 | Idiot                  |
    +------------+------------------------+
    5 rows in set (0.001 sec)
    ```

    Then, to get the total count:

    ```sql
    SELECT FOUND_ROWS();
    ```

    **Output (example, if 6 Dostoevsky books in total):**

    ```
    +--------------+
    | FOUND_ROWS() |
    +--------------+
    |            6 |
    +--------------+
    1 row in set (0.000 sec)
    ```

    The value from `FOUND_ROWS()` is temporary and specific to the current session.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
