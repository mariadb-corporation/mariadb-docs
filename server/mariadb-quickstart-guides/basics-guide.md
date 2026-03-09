---
description: >-
  Complete MariaDB basics guide: connect with mariadb -u/-p/-h, CREATE
  DATABASE/USE, CREATE TABLE with AUTO_INCREMENT, INSERT/SELECT/UPDATE/DELETE
  commands.
---

# Basics Guide

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/G9gr3KMrlccJhmFh3SNT/" %}

The quickstart guide walks you through connecting to a MariaDB server, creating your initial database and table structures, and performing fundamental data operations. It's designed for new users or anyone needing a quick refresher on essential MariaDB commands and basic syntax.

### Connecting to MariaDB Server

To interact with the MariaDB server, use a client program. The default command-line client is `mariadb`.

Connect to MariaDB in monitor mode from the Linux command-line:

```bash
mariadb -u root -p -h localhost
```

Common options:

* `-u username`: Specifies the MariaDB user (e.g., `root`). This is not the OS user.
* `-p`: Prompts for the password. If no password is set, press \[Enter].
* `-h hostname_or_IP`: Specifies the server's hostname or IP address if the client is on a different machine than the server. Often not needed if connecting locally.

If logged into Linux as `root`, you might only need:

```bash
mariadb -p
```

To exit the `mariadb` monitor, type `quit` or `exit` and press \[Enter].

### Creating a Database Structure

First, create and select a database.

```sql
CREATE DATABASE bookstore;
USE bookstore;
```

This creates a database named `bookstore` and sets it as the default for subsequent operations.

Next, create tables to hold data.

```sql
CREATE TABLE books (
    isbn CHAR(20) PRIMARY KEY,
    title VARCHAR(50),
    author_id INT,
    publisher_id INT,
    year_pub CHAR(4),
    description TEXT
);
```

This statement creates a `books` table with six columns:

* `isbn`: `CHAR(20)`, the primary key for unique identification.
* `title`: `VARCHAR(50)`, a variable-width string for the book title.
* `author_id`, `publisher_id`: `INT`, for storing numeric IDs.
* `year_pub`: `CHAR(4)`, a fixed-width string for the publication year.
* `description`: `TEXT`, for longer descriptive text (up to 65,535 bytes).

To view the structure of a created table:

```sql
DESCRIBE books;
```

```sql
+--------------+-------------+------+-----+---------+-------+
| Field        | Type        | Null | Key | Default | Extra |
+--------------+-------------+------+-----+---------+-------+
| isbn         | char(20)    | NO   | PRI | NULL    |       |
| title        | varchar(50) | YES  |     | NULL    |       |
| author_id    | int(11)     | YES  |     | NULL    |       |
| publisher_id | int(11)     | YES  |     | NULL    |       |
| year_pub     | char(4)     | YES  |     | NULL    |       |
| description  | text        | YES  |     | NULL    |       |
+--------------+-------------+------+-----+---------+-------+
```

To modify an existing table, use the `ALTER TABLE` statement (see [ALTER TABLE documentation](../reference/sql-statements/data-definition/alter/alter-table/)). To delete a table and all its data (irreversibly), use `DROP TABLE table_name;` (see [DROP TABLE documentation](../reference/sql-statements/data-definition/drop/drop-table.md)).

Example of another table, `authors`, using `AUTO_INCREMENT` for the primary key:

```sql
CREATE TABLE authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    name_last VARCHAR(50),
    name_first VARCHAR(50),
    country VARCHAR(50)
);
```

The `author_id` will automatically generate a unique number for each new author.

### SQL Syntax Notes

* SQL statements typically end with a semicolon (`;`) or `\G`.
* Statements can span multiple lines; execution occurs after the terminating character and \[Enter].
* To cancel a partially typed statement in the `mariadb` client, enter `\c` and press \[Enter].
* SQL reserved words (e.g., `CREATE`, `SELECT`) are often written in uppercase for readability but are case-insensitive in MariaDB.
* Database and table names are case-sensitive on Linux systems (as they map to directories and files) but generally not on Windows. Column names are case-insensitive.
* Using lowercase for table and column names is a common convention.

### Entering Data

Use the `INSERT` statement (see [INSERT documentation](../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md)) to add new rows to a table.

```sql
INSERT INTO authors (name_last, name_first, country)
VALUES('Kafka', 'Franz', 'Czech Republic');
```

Since `author_id` in the `authors` table is `AUTO_INCREMENT` (see [AUTO\_INCREMENT documentation](../reference/data-types/auto_increment.md)), its value is assigned automatically. If not all columns are being supplied with data, the column names must be listed, followed by their corresponding values in the `VALUES` clause.

To insert data for a book, referencing `author_id` `1` (assuming Kafka's `author_id` became `1`):

```sql
INSERT INTO books (title, author_id, isbn, year_pub)
VALUES('The Castle', '1', '0805211063', '1998');
```

Multiple rows can be inserted with a single `INSERT` statement:

```sql
INSERT INTO books (title, author_id, isbn, year_pub)
VALUES('The Trial', '1', '0805210407', '1995'),
      ('The Metamorphosis', '1', '0553213695', '1995'),
      ('America', '1', '0805210644', '1995');
```

### Retrieving Data

Use the SELECT statement (see SELECT documentation) to query data from tables.

To retrieve all book titles:

```sql
SELECT title FROM books;
```

To limit the number of rows returned (e.g., to 5) using `LIMIT` (see [LIMIT documentation](../reference/sql-statements/data-manipulation/selecting-data/limit.md)):

```sql
SELECT title FROM books LIMIT 5;
```

To retrieve data from multiple tables, use a `JOIN` (see [JOIN documentation](../reference/sql-statements/data-manipulation/selecting-data/joins/join-syntax.md)). This example lists book titles and author last names by joining `books` and `authors` on their common `author_id` column:

```sql
SELECT title, name_last
FROM books
JOIN authors USING (author_id);
```

To filter results, use the `WHERE` clause. This example finds books by 'Kafka' and renames the `title` column<sup>1</sup> in the output to 'Kafka Books' using `AS` (an alias):

```sql
SELECT title AS 'Kafka Books'
FROM books
JOIN authors USING (author_id)
WHERE name_last = 'Kafka';
```

```sql
+-------------------+
| Kafka Books       |
+-------------------+
| The Castle        |
| The Trial         |
| The Metamorphosis |
| America           |
+-------------------+
```

### Changing & Deleting Data

To modify existing data, use the `UPDATE` statement (see [UPDATE documentation](../reference/sql-statements/data-manipulation/changing-deleting-data/update.md)). Always use a `WHERE` clause to specify which rows to update.

```sql
UPDATE books
SET title = 'Amerika'
WHERE isbn = '0805210644';
```

This changes the `title` for the book with the specified `isbn`. Multiple columns can be updated by separating `column = value` assignments with commas within the `SET` clause.

To remove rows from a table, use the `DELETE` statement (see [DELETE documentation](../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md)). Use `WHERE` to specify which rows to delete.

```sql
DELETE FROM books
WHERE author_id = '2034'; -- Assuming '2034' is the author_id to be deleted
```

This deletes all books associated with `author_id` '2034'.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
