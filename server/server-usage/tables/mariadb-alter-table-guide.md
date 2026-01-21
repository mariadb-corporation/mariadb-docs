---
description: >-
  Learn how to modify existing table structures using the ALTER TABLE statement,
  including adding, changing, and dropping columns and indexes.
---

# Altering Tables in MariaDB

Despite a MariaDB developer's best planning, occasionally one needs to change the structure or other aspects of tables. This is not very difficult, but some developers are unfamiliar with the syntax for the functions used in MariaDB to accomplish this. And some changes can be very frustrating. In this article we'll explore the ways to alter tables in MariaDB and we'll give some precautions about related potential data problems.

#### Before Beginning

For the examples in this article, we will refer to a database called `db1` containing a table called `clients`. The `clients` table is for keeping track of client names and addresses. To start off, we'll enter a [DESCRIBE](../../reference/sql-statements/administrative-sql-statements/describe.md) statement to see what the table looks like:

```sql
DESCRIBE clients; 

+-------------+-------------+------+-----+---------+-------+
| Field       | Type        | Null | Key | Default | Extra |
+-------------+-------------+------+-----+---------+-------+
| cust_id     | int(11)     |      | PRI | 0       |       |
| name        | varchar(25) | YES  |     | NULL    |       |
| address     | varchar(25) | YES  |     | NULL    |       |
| city        | varchar(25) | YES  |     | NULL    |       |
| state       | char(2)     | YES  |     | NULL    |       |
| zip         | varchar(10) | YES  |     | NULL    |       |
| client_type | varchar(4)  | YES  |     | NULL    |       |
+-------------+-------------+------+-----+---------+-------+
```

This is a very simple table that will hold very little information. However, it's sufficient for the examples here in which we will change several of its columns. Before doing any structural changes to a table in MariaDB, especially if it contains data, one should make a backup of the table to be changed. There are a few ways to do this, but some choices may not be permitted by your web hosting company. Even if your database is on your own server, though, the [mariadb-dump](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) utility is typically the best tool for making and restoring backups in MariaDB, and it's generally permitted by web hosting companies. To backup the clients table with [mariadb-dump](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md), we will enter the following from the command-line:

```bash
mariadb-dump --user='username' --password='password' --add-locks db1 clients > clients.sql
```

As you can see, the username and password are given on the first line. On the next line, the `--add-locks` option is used to lock the table before backing up and to unlock automatically it when the backup is finished. There are many other options in [mariadb-dump](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) that could be used, but for our purposes this one is all that's necessary. Incidentally, this statement can be entered in one line from the shell (i.e., not from the `mariadb` client), or it can be entered on multiple lines as shown here by using the back-slash (i.e., `/`) to let the shell know that more is to follow. On the third line above, the database name is given, followed by the table name. The redirect (i.e., `>`) tells the shell to send the results of the dump to a text file called `clients.sql` in the current directory. A directory path could be put in front of the file name to create the file elsewhere. If the table should need to be restored, the following can be run from the shell:

```bash
mariadb --user='username' --password='password' db1 < clients.sql
```

Notice that this line does not use the `mariadb-dump` utility. It uses the `mariadb` client from the outside, so to speak. When the dump file (`clients.sql`) is read into the database, it will delete the `clients` table and it's data in MariaDB before restoring the backup copy with its data. So be sure that users haven't added data in the interim. In the examples in this article, we are assuming that there isn't any data in the tables yet.

#### Basic Addition and More

In order to add a column to an existing MariaDB table, one would use the [ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table/) statement. To demonstrate, suppose that it has been decided that there should be a column for the client's account status (i.e., active or inactive). To make this change, the following is entered:

```sql
ALTER TABLE clients 
ADD COLUMN status CHAR(2);
```

This will add the column `status` to the end with a fixed width of two characters (i.e., _AC_ for active and _IA_ for inactive). In looking over the table again, it's decided that another field for client apartment numbers or the like needs to be added. That data could be stored in the address column, but it would better for it to be in a separate column. An [ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table/) statement could be entered like above, but it will look tidier if the new column is located right after the address column. To do this, we'll use the `AFTER` option:

```sql
ALTER TABLE clients 
ADD COLUMN address2 VARCHAR(25) 
AFTER address;
```

By the way, to add a column to the first position, you would replace the last line of the SQL statement above to read like this:

```sql
...
FIRST;
```

Before moving on, let's take a look at the table's structure so far:

```sql
DESCRIBE clients;

+-------------+-------------+------+-----+---------+-------+
| Field       | Type        | Null | Key | Default | Extra |
+-------------+-------------+------+-----+---------+-------+
| cust_id     | int(11)     |      | PRI | 0       |       |
| name        | varchar(25) | YES  |     | NULL    |       |
| address     | varchar(25) | YES  |     | NULL    |       |
| address2    | varchar(25) | YES  |     | NULL    |       |
| city        | varchar(25) | YES  |     | NULL    |       |
| state       | char(2)     | YES  |     | NULL    |       |
| zip         | varchar(10) | YES  |     | NULL    |       |
| client_type | varchar(4)  | YES  |     | NULL    |       |
| status      | char(2)     | YES  |     | NULL    |       |
+-------------+-------------+------+-----+---------+-------+
```

#### Changing One's Mind

After looking over the above table display, it's decided that it might be better if the status column has the choices of 'AC' and 'IA' enumerated. To make this change, we'll enter the following SQL statement:

```sql
ALTER TABLE clients 
CHANGE status status ENUM('AC','IA');
```

Notice that the column name status is specified twice. Although the column name isn't being changed, it still must be respecified. To change the column name (from `status` to `active`), while leaving the enumerated list the same, we specify the new column name in the second position:

```sql
ALTER TABLE clients
CHANGE status active ENUM('AC','IA');
```

Here we have the current column name and then the new column name, along with the data type specifications (i.e., `ENUM`), even though the result is only a name change. With the `CHANGE` clause everything must be stated, even items that are not to be changed.

In checking the table structure again, more changes are decided on: The column address is to be renamed to address1 and changed to forty characters wide. Also, the enumeration of active is to have 'yes' and 'no' choices. The problem with changing enumerations is that data can be clobbered in the change if one isn't careful. We've glossed over this possibility before because we are assuming that clients is empty. Let's take a look at how the modifications suggested could be made with the table containing data:

```sql
ALTER TABLE clients
CHANGE address address1 VARCHAR(40),
MODIFY active ENUM('yes','NO','AC','IA');

UPDATE clients
SET active = 'yes'
WHERE active = 'AC';

UPDATE clients
SET active = 'NO'
WHERE active = 'IA';

ALTER TABLE clients
MODIFY active ENUM('yes','NO');
```

The first SQL statement above changes address and modifies active in preparation for the transition. Notice the use of a `MODIFY` clause. It works the same as `CHANGE`, but it is only used for changing data types and not column names. Therefore, the column name isn't respecified. Notice also that there is a comma after the CHANGE clause. You can string several `CHANGE` and `MODIFY` clauses together with comma separators. We've enumerated both the new choices and the old ones to be able to migrate the data. The two [UPDATE](../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) statements are designed to adjust the data accordingly and the last [ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table/) statement is to remove the old enumerated choices for the status column.

In talking to the boss, we find out that the `client_type` column isn't going to be used. So we enter the following in MariaDB:

```sql
ALTER TABLE clients
DROP client_type;
```

This deletes `client_type` and its data, but not the whole table, obviously. Nevertheless, it is a permanent and non-reversible action; there won't be a confirmation request when using the mariadb client. This is how it is with all MariaDB DROP statements and clauses. So be sure that you want to delete an element and its data before using a `DROP.` As mentioned earlier, be sure that you have a backup of your tables before doing any structured changes.

#### The Default

You may have noticed that the results of the [DESCRIBE](../../reference/sql-statements/administrative-sql-statements/describe.md) statements shown before have a heading called 'Default' and just about all of the fields have a default value of NULL. This means that there are no default values and a null value is allowed and are used if a value isn't specified when a row is created. To be able to specify a default value other than NULL, an [ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table/) statement can be entered with a `SET` clause. Suppose we're located in Louisiana and we want a default value of 'LA' for state since that's where our clients are usually located. We would enter the following to set the default:

```sql
ALTER TABLE clients
ALTER state SET DEFAULT 'LA';
```

Notice that the second line starts with `ALTER` and not `CHANGE`. If we change our mind about having a default value for state, we would enter the following to reset it back to NULL (or whatever the initial default value would be based on the data type):

```sql
ALTER TABLE clients
ALTER state DROP DEFAULT;
```

This particular `DROP` doesn't delete data, by the way.

#### Indexes

One of the most irritating tasks in making changes to a table for newcomers is dealing with indexes. If they try to rename a column that is indexed by only using an [ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table/) statement like we used earlier, they will get a frustrating and confusing error message:

```sql
ALTER TABLE clients
CHANGE cust_id client_id INT
PRIMARY KEY;
 
ERROR 1068: Multiple primary key defined
```

If they're typing this column change from memory, they will wear themselves out trying different deviations thinking that they remembered the syntax wrong. What most newcomers to MariaDB don't seem to realize is that the index is separate from the indexed column. To illustrate, let's take a look at the index for clients by using the [SHOW INDEX](../../reference/sql-statements/administrative-sql-statements/show/show-index.md) statement:

```sql
SHOW INDEX FROM clients\G

*************************** 1. row ***************************
           TABLE: clients
      Non_unique: 0
        Key_name: PRIMARY
    Seq_in_index: 1
     Column_name: cust_id
       Collation: A
     Cardinality: 0
        Sub_part: NULL
          Packed: NULL
         Comment:
1 row in set (0.00 sec)
```

The text above shows that behind the scenes there is an index associated with `cust_id`. The column `cust_id` is not the index. Incidentally, the G at the end of the [SHOW INDEX](../../reference/sql-statements/administrative-sql-statements/show/show-index.md) statement is to display the results in portrait instead of landscape format. Before the name of an indexed column can be changed, the index related to it must be eliminated. The index is not automatically changed or deleted. Therefore, in the example above, MariaDB thinks that the developer is trying to create another primary key index. So, a `DROP` clause for the index must be entered first and then a `CHANGE` for the column name can be made along with the establishing of a new index:

```sql
ALTER TABLE clients
DROP PRIMARY KEY,
CHANGE cust_id
client_id INT PRIMARY KEY;
```

The order of these clauses is necessary. The index must be dropped before the column can be renamed. The syntax here is for a `PRIMARY KEY`. There are other types of indexes, of course. To change a column that has an index type other than a `PRIMARY KEY`. Assuming for a moment that `cust_id` has a `UNIQUE` index, this is what we would enter to change its name:

```sql
ALTER TABLE clients
DROP UNIQUE cust_id
CHANGE cust_id
client_id INT UNIQUE;
```

Although the index type can be changed easily, MariaDB won't permit you to do so when there are duplicate rows of data and when going from an index that allows duplicates (e.g., `INDEX`) to one that doesn't (e.g., `UNIQUE`). If you actually do want to eliminate the duplicates, though, you can add the `IGNORE` flag to force the duplicates to be deleted:

```sql
ALTER IGNORE TABLE clients
DROP INDEX cust_id
CHANGE cust_id
client_id INT UNIQUE;
```

In this example, we're not only changing the indexed column's name, but we're also changing the index type from `INDEX` to `UNIQUE`. And, again, the `IGNORE` flag tells MariaDB to ignore any records with duplicate values for `cust_id`.

#### Renaming & Shifting Tables

The previous sections covered how to make changes to columns in a table. Sometimes you may want to rename a table. To change the name of the `clients` table to client\_addresses we enter this:

```sql
RENAME TABLE clients 
TO client_addresses;
```

The RENAME TABLE statement will also allows a table to be moved to another database just by adding the receiving database's name in front of the new table name, separated by a dot. Of course, you can move a table without renaming it. To move the newly named `client_addresses` table to the database db2, we enter this:

```sql
RENAME TABLE client_addresses
TO db2.client_addresses;
```

Finally, with tables that contain data (excluding [InnoDB](../storage-engines/innodb/) tables), occasionally it's desirable to resort the data within the table. Although the [ORDER BY](../../reference/sql-statements/data-manipulation/selecting-data/select.md#order-by) clause in a [SELECT](../../reference/sql-statements/data-manipulation/selecting-data/select.md) statement can do this on the fly as needed, sometimes developers want to do this somewhat permanently to the data within the table based on a particular column or columns. It can be done by entering the following:

```sql
ALTER TABLE client_addresses
ORDER BY city, name;
```

Notice that we're sorting by the city first and then by the client's name. Now when the developer enters a [SELECT](../../reference/sql-statements/data-manipulation/selecting-data/select.md) statement without an [ORDER BY](../../reference/sql-statements/data-manipulation/selecting-data/select.md#order-by) clause, the results are already ordered by the default of city and then name, at least until more data is added to the table.

This is not applicable to [InnoDB](../storage-engines/innodb/) tables, the default, which are ordered according to the clustered index, unless the primary key is defined on the specific columns.

#### Summation

Good planning is certainly important in developing a MariaDB database. However, as you can see, MariaDB is malleable enough that it can be reshaped without much trouble. Just be sure to make a backup before restructuring a table and be sure to check your work and the data when you're finished. With all of this in mind, you should feel comfortable in creating tables since they don't have to be perfect from the beginning.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
