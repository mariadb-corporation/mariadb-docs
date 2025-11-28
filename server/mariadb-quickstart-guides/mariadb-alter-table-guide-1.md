---
description: >-
  Essential guide to modifying table structures: add, drop, or change columns;
  manage indexes and default values; and rename tables. Includes key precautions
  for all database operations.
---

# Altering Tables Guide

This guide provides essential instructions for modifying existing table structures. Learn how to add, drop, and change columns, manage indexes and default values, and rename tables, along with key precautions for these operations when working with your database.

### Before You Begin: Backup Your Tables

Before making any structural changes to a table, especially if it contains data, **always create a backup**. The `mariadb-dump` utility is a common and effective tool for this.

Example: Backing up a single table

Suppose you have a database db1 and a table clients. Its initial structure is:

```sql
DESCRIBE clients;
```

```sql
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

To back up the `clients` table from the command-line:

```bash
mariadb-dump --user='your_username' --password='your_password' --add-locks db1 clients > clients.sql
```

* Replace `'your_username'` and `'your_password'` with your actual MariaDB credentials.
* `--add-locks`: Locks the table during the backup and unlocks it afterward.
* `db1 clients`: Specifies the database and then the table.
* `> clients.sql`: Redirects the output to a file named `clients.sql`.

Restoring from a backup

If you need to restore the table:

```bash
mariadb --user='your_username' --password='your_password' db1 < clients.sql
```

This command uses the `mariadb` client to execute the SQL in `clients.sql`, which will typically drop the existing table (if it exists) and recreate it from the backup. Ensure no critical data has been added to the live table since the backup if you intend to overwrite it.

For the examples that follow, we'll assume structural changes are being made, sometimes on an empty table for simplicity, but the backup step is always recommended for tables with data.

### Adding Columns

Use the `ALTER TABLE` statement with the `ADD COLUMN` clause.

Add a column to the end of the table:

To add a status column with a fixed width of two characters:

```sql
ALTER TABLE clients
ADD COLUMN status CHAR(2);
```

Add a column after a specific existing column:

To add address2 (varchar 25) after the address column:

```sql
ALTER TABLE clients
ADD COLUMN address2 VARCHAR(25) AFTER address;
```

**Add a column to the beginning of the table:**

```sql
ALTER TABLE clients
ADD COLUMN new_first_column VARCHAR(50) FIRST;
```

_(Assuming `new_first_column` is the one to be added at the beginning)._

After additions, the table structure might look like (excluding `new_first_column` for consistency with original example flow):

```sql
DESCRIBE clients;
```

```sql
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

### Changing Column Definitions

Use `ALTER TABLE` with `CHANGE` or `MODIFY`.

Change column type (e.g., to ENUM):

The status column name is specified twice even if not changing the name itself when using CHANGE.

```sql
ALTER TABLE clients
CHANGE status status ENUM('AC','IA');
```

Change column name and keep type:

To change status to active while keeping the ENUM definition:

```sql
ALTER TABLE clients
CHANGE status active ENUM('AC','IA');
```

When using `CHANGE`, the current column name is followed by the new column name and the complete type definition.

Modify column type or attributes without renaming:

Use MODIFY if you are only changing the data type or attributes, not the name.

```sql
ALTER TABLE clients
MODIFY address1 VARCHAR(40); -- Assuming 'address1' is an existing column
```

Complex Changes (e.g., ENUM migration with data):

Changing ENUM values in a table with existing data requires careful steps to prevent data loss. This typically involves:

1. Temporarily modifying the ENUM to include both old and new values.
2. Updating existing rows to use the new values.
3. Modifying the ENUM again to remove the old values.

Example of changing `address` to `address1` (40 chars) and preparing `active` ENUM for new values 'yes','no' from 'AC','IA':

```sql
ALTER TABLE clients
    CHANGE address address1 VARCHAR(40),
    MODIFY active ENUM('yes','no','AC','IA'); -- Temporarily include all
```

Then, update the data:

```sql
UPDATE clients
SET active = 'yes'
WHERE active = 'AC';

UPDATE clients
SET active = 'no'
WHERE active = 'IA';
```

Finally, restrict the ENUM to new values:

```sql
ALTER TABLE clients
MODIFY active ENUM('yes','no');
```

### Dropping Columns

To remove a column and its data (this action is permanent and irreversible without a backup):

```sql
ALTER TABLE clients
DROP COLUMN client_type;
```

### Managing Default Values

Set a default value for a column:

If most clients are in 'LA', set it as the default for the state column:

```sql
ALTER TABLE clients
ALTER state SET DEFAULT 'LA';
```

Remove a default value from a column:

This reverts the default to its standard (e.g., NULL if nullable, or determined by data type).

```sql
ALTER TABLE clients
ALTER state DROP DEFAULT;
```

This `DROP DEFAULT` does not delete existing data in the column.

### Managing Indexes

Indexes are separate objects from columns. Modifying an indexed column often requires managing its index.

View existing indexes on a table:

The \G displays results in a vertical format, which can be easier to read for wide output.

```sql
SHOW INDEX FROM clients\G
```

Example output:

```sql
*************************** 1. row ***************************
           Table: clients
      Non_unique: 0
        Key_name: PRIMARY
    Seq_in_index: 1
     Column_name: cust_id
       Collation: A
     Cardinality: 0
        Sub_part: NULL
          Packed: NULL
         Comment:
```

Changing an indexed column (e.g., Primary Key):

Attempting to CHANGE a column that is part of a PRIMARY KEY without addressing the key might result in an error like "Multiple primary key defined". The index must be dropped first, then the column changed, and the key re-added.

```sql
ALTER TABLE clients
    DROP PRIMARY KEY,
    CHANGE cust_id client_id INT PRIMARY KEY;
```

The order is important: `DROP PRIMARY KEY` first.

Changing a column with another index type (e.g., UNIQUE):

If cust\_id had a UNIQUE index named cust\_id\_unique\_idx (Key\_name from SHOW INDEX):

```sql
ALTER TABLE clients
    DROP INDEX cust_id_unique_idx, -- Use the actual Key_name
    CHANGE cust_id client_id INT UNIQUE;
```

If the `Key_name` is the same as the `Column_name` (e.g. for a single column `UNIQUE` key defined on `cust_id` where `cust_id` is also its `Key_name`):

```sql
ALTER TABLE clients
    DROP INDEX cust_id, -- If cust_id is the Key_name
    CHANGE cust_id client_id INT UNIQUE;
```

Changing index type and handling duplicates (e.g., INDEX to UNIQUE):

If changing from an index type that allows duplicates (like a plain INDEX) to one that doesn't (UNIQUE), and duplicate data exists, the operation will fail. To force the change and remove duplicates (use with extreme caution):

```sql
ALTER IGNORE TABLE clients
    DROP INDEX cust_id_idx, -- Assuming cust_id_idx is the name of the old INDEX
    CHANGE cust_id client_id INT UNIQUE;
```

The `IGNORE` keyword causes rows with duplicate key values (for the new `UNIQUE` key) to be deleted. Only the first encountered row is kept.

### Renaming and Shifting Tables

Rename a table:

To change the name of clients to client\_addresses:

```sql
RENAME TABLE clients TO client_addresses;
```

Move a table to another database (can be combined with renaming):

To move client\_addresses to a database named db2:

```sql
RENAME TABLE client_addresses TO db2.client_addresses;
```

Re-sort data within a table (MyRocks/Aria, not typically InnoDB):

For some storage engines (excluding InnoDB where tables are ordered by the primary key), you can physically reorder rows. This does not usually apply to InnoDB unless the ORDER BY columns form the primary key.

```sql
ALTER TABLE client_addresses
ORDER BY city, name;
```

After this, `SELECT * FROM client_addresses` (without an `ORDER BY` clause) might return rows in this new physical order, until further data modifications occur.

### Key Considerations

* **Backup First:** Always back up tables before making structural alterations, especially on production systems.
* **Data Integrity:** Be mindful of how changes (e.g., type changes, ENUM modifications, dropping columns) can affect existing data. Test changes in a development environment.
* **Irreversible Actions:** Operations like `DROP COLUMN` or `DROP TABLE` are generally irreversible without restoring from a backup. There's typically no confirmation prompt.
* **Indexes:** Understand that indexes are distinct from columns. Modifying indexed columns often requires separate steps to manage the associated indexes.
* **Performance:** `ALTER TABLE` operations on large tables can be time-consuming and resource-intensive, potentially locking the table and impacting application performance. Plan these operations during maintenance windows if possible.

CC BY-SA / Gnu FDL
