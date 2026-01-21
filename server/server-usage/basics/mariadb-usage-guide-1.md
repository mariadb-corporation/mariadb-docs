---
description: >-
  A beginner-friendly primer on using the mariadb command-line client to log in,
  create databases, and execute basic SQL commands.
---

# A MariaDB Primer

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/G9gr3KMrlccJhmFh3SNT/" %}

This primer is designed to teach you the basics of getting information into and out of an existing MariaDB database using the [mariadb](../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) command-line client program. It's not a complete reference and will not touch on any advanced topics. It is just a quick jump-start into using MariaDB.

#### Logging into MariaDB

Log into your MariaDB server from the command-line like so:

```bash
mariadb -u user_name -p -h ip_address db_name
```

Replace _user\_name_ with your database username. Replace _ip\_address_ with the host name or address of your server. If you're accessing MariaDB from the same server you're logged into, then don't include `-h` and the _ip\_address_. Replace _db\_name_ with the name of the database you want to access (such as _test_, which sometimes comes already created for testing purposes - note that Windows does not create this database, and some setups may also have removed the `test` database by running [mariadb-secure-installation](../../clients-and-utilities/deployment-tools/mariadb-secure-installation.md), in which case you can leave the _db\_name_ out).

When prompted to enter your password, enter it. If your login is successful you should see something that looks similar to this:

```bash
MariaDB [test]>
```

This is where you will enter in all of your SQL statements. More about those later. For now, let's look at the components of the prompt: The "MariaDB" part means you that you are connected to a MariaDB database server. The word between the brackets is the name of your default database, the _test_ database in this example.

#### The Basics of a Database

To make changes to a database or to retrieve data, you will need to enter an SQL statement. SQL stands for Structured Query Language. An SQL statement that requests data is called a query. Databases store information in tables. They're are similar to spreadsheets, but much more efficient at managing data.

Note that the _test_ database may not contain any data yet. If you want to follow along with the primer, copy and paste the following into the [mariadb](../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) client. This will create the tables we will use and add some data to them. Don't worry about understanding them yet; we'll get to that later.

```sql
CREATE DATABASE IF NOT EXISTS test;

USE test;

CREATE TABLE IF NOT EXISTS books (
  BookID INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
  Title VARCHAR(100) NOT NULL, 
  SeriesID INT, AuthorID INT);

CREATE TABLE IF NOT EXISTS authors 
(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT);

CREATE TABLE IF NOT EXISTS series 
(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT);

INSERT INTO books (Title,SeriesID,AuthorID) 
VALUES('The Fellowship of the Ring',1,1), 
      ('The Two Towers',1,1), ('The Return of the King',1,1),  
      ('The Sum of All Men',2,2), ('Brotherhood of the Wolf',2,2), 
      ('Wizardborn',2,2), ('The Hobbbit',0,1);
```

Notice the semi-colons used above. The [mariadb](../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) client lets you enter very complex SQL statements over multiple lines. It won't send an SQL statement until you type a semi-colon and hit \[Enter].

Let's look at what you've done so far. Enter the following:

```sql
SHOW TABLES;

+----------------+
| Tables_in_test |
+----------------+
| authors        |
| books          |
| series         |
+----------------+
3 rows in set (0.00 sec)
```

Notice that this displays a list of the tables in the database. If you didn't already have tables in your `test` database, your results should look the same as above. Let's now enter the following to get information about one of these tables:

```sql
DESCRIBE books;

+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| BookID   | int(11)      | NO   | PRI | NULL    | auto_increment |
| Title    | varchar(100) | NO   |     | NULL    |                |
| SeriesID | int(11)      | YES  |     | NULL    |                |
| AuthorID | int(11)      | YES  |     | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
```

The main bit of information of interest to us is the _Field_ column. The other columns provide useful information about the structure and type of data in the database, but the _Field_ column gives us the names, which is needed to retrieve data from the table.

Let's retrieve data from the `books` table. We'll do so by executing a [SELECT](../../reference/sql-statements/data-manipulation/selecting-data/select.md) statement like so:

```sql
SELECT * FROM books;

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

This SQL statement or query asks the database to show us all of the data in the `books` table. The wildcard ('`*`') character indicates to select all columns.

#### Inserting Data

Suppose now that we want to add another book to this table. We'll add the book, _Lair of Bones_. To insert data into a table, you would use the [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statement. To insert information on a book, we would enter something like this:

```sql
INSERT INTO books (Title, SeriesID, AuthorID)
VALUES ("Lair of Bones", 2, 2);

Query OK, 1 row affected (0.00 sec)
```

Notice that we put a list of columns in parentheses after the name of the table, then we enter the keyword `VALUES` followed by a list of values in parentheses--in the same order as the columns were listed. We could put the columns in a different order, as long as the values are in the same order as we list the columns. Notice the message that was returned indicates that the execution of the SQL statement went fine and one row was entered.

Execute the following SQL statement again and see what results are returned:

```sql
SELECT * FROM books;
```

You should see the data you just entered on the last row of the results. In looking at the data for the other books, suppose we notice that the title of the seventh book is spelled wrong. It should be spelled _The Hobbit_, not _The Hobbbit_. We will need to update the data for that row.

#### Modifying Data

To change data in a table, you will use the [UPDATE](../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) statement. Let's change the spelling of the book mentioned above. To do this, enter the following:

```sql
UPDATE books 
SET Title = "The Hobbit" 
WHERE BookID = 7;

Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0
```

Notice the syntax of this SQL statement. The `SET` clause is where you list the columns and the values to set them. The `WHERE` clause says that you want to update only rows in which the `BookID` column has a value of `7`, of which there are only one. You can see from the message it returned that one row matched the `WHERE` clause and one row was changed. There are no warnings because everything went fine. Execute the [SELECT](../../reference/sql-statements/data-manipulation/selecting-data/select.md) from earlier to see that the data changed.

As you can see, using MariaDB isn't very difficult. You just have to understand the syntax of SQL since it doesn't allow for typing mistakes or things in the wrong order or other deviations.

#### See Also

* [MariaDB Basics](./)

{% include "../../.gitbook/includes/license-cc-by-sa-gnu-fdl.md" %}

{% @marketo/form formId="4316" %}
