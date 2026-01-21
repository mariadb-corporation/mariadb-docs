---
description: >-
  A beginner-friendly primer on using the mariadb command-line client to log in,
  create databases, and execute basic SQL commands.
---

# A MariaDB Primer Guide

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/G9gr3KMrlccJhmFh3SNT/" %}

This primer offers a quick jump-start for beginners using an existing MariaDB database via the `mariadb` command-line client. Learn how to log in, understand basic database concepts, and perform essential SQL operations like creating tables, inserting data, and retrieving or modifying records.

### Logging into MariaDB

To begin, log into your MariaDB server from your system's command-line:

```bash
mariadb -u user_name -p -h ip_address db_name
```

* Replace `user_name` with your MariaDB username.
* Replace `ip_address` with the hostname or IP address of your MariaDB server. If you are accessing MariaDB from the same server you're logged into (i.e., locally), you can usually omit the `-h ip_address` part.
* Replace `db_name` with the name of the database you wish to access (e.g., `test`). Some setups may have a `test` database by default; others might not, or it might have been removed (e.g., by `mariadb-secure-installation`). If unsure, or if you want to connect without selecting a specific database initially, you can omit `db_name`.

You will be prompted to enter your password. If your login is successful, you will see a prompt similar to this:

```bash
MariaDB [test]>
```

The "MariaDB" indicates you are connected to a MariaDB server. The name within the brackets (e.g., `test`) is your current default database. If no database was specified or successfully connected to, it might show `[(none)]`.

### Understanding Database Basics and Setup

SQL (Structured Query Language): This is the language used to interact with MariaDB. An SQL statement that requests data is called a query.

Tables: Databases store information in tables, which are structured like spreadsheets with rows and columns, but are much more efficient for data management.

Example Setup:

If the test database is empty or doesn't exist, you can run the following SQL statements to create and populate tables for the examples in this primer. Copy and paste these into the mariadb client prompt.

{% code expandable="true" %}
```sql
CREATE DATABASE IF NOT EXISTS test;
USE test;

CREATE TABLE IF NOT EXISTS books (
  BookID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  Title VARCHAR(100) NOT NULL,
  SeriesID INT,
  AuthorID INT
);

CREATE TABLE IF NOT EXISTS authors (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT
  -- You would typically add more columns like name, etc.
);

CREATE TABLE IF NOT EXISTS series (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT
  -- You would typically add more columns like series_name, etc.
);

INSERT INTO books (Title, SeriesID, AuthorID) VALUES
  ('The Fellowship of the Ring', 1, 1),
  ('The Two Towers', 1, 1),
  ('The Return of the King', 1, 1),
  ('The Sum of All Men', 2, 2),
  ('Brotherhood of the Wolf', 2, 2),
  ('Wizardborn', 2, 2),
  ('The Hobbbit', 0, 1); -- Note: "Hobbbit" is intentionally misspelled for a later example
```
{% endcode %}

* **Semicolons (`;`):** The `mariadb` client allows complex SQL statements over multiple lines. It sends the statement to the server for execution only after you type a semicolon (`;`) and press \[Enter].

### Exploring Your Database Structure

Listing Tables:

To see the tables in your current database:

```sql
SHOW TABLES;
```

**Output (example):**

```
+----------------+
| Tables_in_test |
+----------------+
| authors        |
| books          |
| series         |
+----------------+
3 rows in set (0.00 sec)
```

Describing a Table:

To get information about the columns in a table (like their names and types):

```sql
DESCRIBE books;
```

**Output (example):**

```
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| BookID   | int(11)      | NO   | PRI | NULL    | auto_increment |
| Title    | varchar(100) | NO   |     | NULL    |                |
| SeriesID | int(11)      | YES  |     | NULL    |                |
| AuthorID | int(11)      | YES  |     | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
```

The `Field` column lists the column names, which you'll need to retrieve specific data.

### Retrieving Data (SELECT)

To retrieve data from a table, use the `SELECT` statement.

```sql
SELECT * FROM books;
```

* The asterisk (`*`) is a wildcard meaning "all columns." **Output (example):**

```
+--------+----------------------------+----------+----------+
| BookID | Title                      | SeriesID | AuthorID |
+--------+----------------------------+----------+----------+
|      1 | The Fellowship of the Ring |        1 |        1 |
|      2 | The Two Towers             |        1 |        1 |
|      3 | The Return of the King     |        1 |        1 |
|      4 | The Sum of All Men         |        2 |        2 |
|      5 | Brotherhood of the Wolf    |        2 |        2 |
|      6 | Wizardborn                 |        2 |        2 |
|      7 | The Hobbbit                |        0 |        1 |
+--------+----------------------------+----------+----------+
7 rows in set (0.00 sec)
```

### Adding Data (INSERT)

To add new rows to a table, use the `INSERT` statement.

```sql
INSERT INTO books (Title, SeriesID, AuthorID)
VALUES ("Lair of Bones", 2, 2);
```

* After `INSERT INTO table_name`, list the columns you are providing data for in parentheses.
* The `VALUES` keyword is followed by a list of values in parentheses, in the same order as the listed columns. **Output:**

```sql
Query OK, 1 row affected (0.00 sec)
```

You can run `SELECT * FROM books;` again to see the newly added row.

### Modifying Data (UPDATE)

To change existing data in a table, use the `UPDATE` statement. Let's correct the spelling of "The Hobbbit".

```sql
UPDATE books
SET Title = "The Hobbit"
WHERE BookID = 7;
```

* `SET Title = "The Hobbit"` specifies the column to change and its new value.
* `WHERE BookID = 7` is crucial; it specifies _which row(s)_ to update. Without a `WHERE` clause, `UPDATE` would change _all_ rows in the table. **Output:**

```
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0
```

Run `SELECT * FROM books WHERE BookID = 7;` to see the correction.

Using MariaDB involves understanding SQL syntax. It doesn't allow for typing mistakes or clauses in the wrong order, but with practice, it becomes straightforward.

### See Also

* [MariaDB Basics](basics-guide.md)

{% @marketo/form formId="4316" %}
