---
description: >-
  Learn how to efficiently import data into MariaDB tables from external files
  using the LOAD DATA INFILE statement.
---

# Importing Data Guide

This guide introduces methods and tools for efficiently importing bulk data into MariaDB. Learn to prepare your data, use `LOAD DATA INFILE` and the `mariadb-import` utility, handle common data import challenges, and manage potential constraints.

### Preparing Your Data File

The most common approach for bulk importing is to use a delimited text file.

1. **Export Source Data:** Load your data in its original software (e.g., MS Excel, MS Access) and export it as a delimited text file.
   * **Delimiter:** Use a character not commonly found in your data to separate fields. The pipe symbol (`|`) is often a good choice. Tab () is also common.
   * **Record Separator:** Use line feeds () to separate records.
2. **Align Columns (Recommended for Simplicity):** Ideally, the order and number of columns in your text file should match the target MariaDB table.
   * If the table has extra columns not in your file, they will be filled with their default values (or `NULL`).
   * If your file has extra columns not in the table, you'll need to specify which file columns to load (see "Mapping File Columns to Table Columns" below) or remove them from the text file.
3. **Clean Data:** Remove any header rows or footer information from the text file unless you plan to skip them during import (see `IGNORE N LINES` below).
4. **Upload File:** Transfer the text file to a location accessible by the MariaDB server.
   * Use ASCII mode for FTP transfers to ensure correct line endings.
   * For security, upload data files to non-public directories on the server.

### Using `LOAD DATA INFILE`

The `LOAD DATA INFILE` statement is a powerful SQL command for importing data from text files. Ensure the MariaDB user has the `FILE` privilege.

Basic Syntax:

First, connect to MariaDB using the mariadb client and select your target database:

```sql
USE sales_dept; -- Or your database name
```

Then, load the data:

```sql
LOAD DATA INFILE '/tmp/prospects.txt'
INTO TABLE prospect_contact
FIELDS TERMINATED BY '|';
```

* Replace `/tmp/prospects.txt` with the actual path to your data file on the server. On Windows, paths use forward slashes (e.g., `'C:/tmp/prospects.txt'`).
* `prospect_contact` is the target table. You can also specify `database_name.table_name`.
* `FIELDS TERMINATED BY '|'` specifies the field delimiter. For tab-delimited, use `'\t'`.
* The default record delimiter is the line feed ().

Specifying Line Terminators and Enclosing Characters:

If your file has custom line endings or fields enclosed by characters (e.g., quotes):

```sql
LOAD DATA INFILE '/tmp/prospects.txt'
INTO TABLE prospect_contact
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES STARTING BY '"' TERMINATED BY '"\r\n';
```

* `ENCLOSED BY '"'`: Specifies that fields are enclosed in double quotes.
* `LINES STARTING BY '"'`: Indicates each line starts with a double quote.
* `TERMINATED BY '"\r\n'`: Indicates each line ends with a double quote followed by a Windows-style carriage return and line feed.
* To specify a single quote as an enclosing character, you can escape it or put it within double quotes: `ENCLOSED BY '\''` or `ENCLOSED BY "'"`.

### Handling Duplicate Rows

When importing data, you might encounter records with primary key values that already exist in the target table.

* **Default Behavior:** MariaDB attempts to import all rows. If duplicates are found and the table has a primary or unique key that would be violated, an error occurs, and subsequent rows may not be imported.
*   **`REPLACE`:** If you want new data from the file to overwrite existing rows with the same primary key:SQL

    ```sql
    LOAD DATA INFILE '/tmp/prospects.txt'
    REPLACE INTO TABLE prospect_contact
    FIELDS TERMINATED BY '|';
    ```
*   **`IGNORE`:** If you want to keep existing rows and skip importing duplicate records from the file:SQL

    ```sql
    LOAD DATA INFILE '/tmp/prospects.txt'
    IGNORE INTO TABLE prospect_contact
    FIELDS TERMINATED BY '|';
    ```

### Importing into Live Tables

If the target table is actively being used, importing data can lock it, preventing access.

*   **`LOW_PRIORITY`:** To allow other users to read from the table while the load operation is pending, use `LOW_PRIORITY`. The load will wait until no other clients are reading the table.SQL

    ```sql
    LOAD DATA LOW_PRIORITY INFILE '/tmp/prospects.txt'
    INTO TABLE prospect_contact
    FIELDS TERMINATED BY '|';
    ```

    Without `LOW_PRIORITY` or `CONCURRENT`, the table is typically locked for the duration of the import.

### Advanced `LOAD DATA INFILE` Options

Binary Line Endings:

If your file has Windows CRLF line endings and was uploaded in binary mode, you can specify the hexadecimal value:

```sql
LOAD DATA INFILE '/tmp/prospects.txt'
INTO TABLE prospect_contact
FIELDS TERMINATED BY '|'
LINES TERMINATED BY 0x0d0a; -- 0x0d is carriage return, 0x0a is line feed
```

Note: No quotes around the hexadecimal value.

Skipping Header Lines:

To ignore a certain number of lines at the beginning of the file (e.g., a header row):

SQL

```sql
LOAD DATA INFILE '/tmp/prospects.txt'
INTO TABLE prospect_contact
FIELDS TERMINATED BY '|'
IGNORE 1 LINES; -- Skips the first line
```

Handling Escaped Characters:

If fields are enclosed by quotes and contain embedded quotes that are escaped by a special character (e.g., # instead of the default backslash \\):

```sql
LOAD DATA INFILE '/tmp/prospects.txt'
INTO TABLE prospect_contact
FIELDS TERMINATED BY '|'
    ENCLOSED BY '"'
    ESCAPED BY '#'
IGNORE 1 LINES;
```

Mapping File Columns to Table Columns:

If the order or number of columns in your text file differs from the target table, you can specify the column mapping at the end of the LOAD DATA INFILE statement.

Assume prospect\_contact table has: (row\_id INT AUTO\_INCREMENT, name\_first VARCHAR, name\_last VARCHAR, telephone VARCHAR).

And prospects.txt has columns in order: Last Name, First Name, Telephone.

```sql
LOAD DATA INFILE '/tmp/prospects.txt'
INTO TABLE prospect_contact
FIELDS TERMINATED BY '|' -- Or your actual delimiter, e.g., 0x09 for tab
ENCLOSED BY '"'
ESCAPED BY '#'
IGNORE 1 LINES
(name_last, name_first, telephone);
```

* MariaDB will map data from the file's first column to `name_last`, second to `name_first`, and third to `telephone`.
* The `row_id` column in the table, not being specified in the list, will be filled by its default mechanism (e.g., `AUTO_INCREMENT` or `DEFAULT` value, or `NULL`).

### Using the `mariadb-import` Utility

The `mariadb-import` utility (known as `mysqlimport` before MariaDB 10.5) is a command-line program that acts as a wrapper for `LOAD DATA INFILE`. It's useful for scripting imports.

**Syntax:**

```bash
mariadb-import --user='your_username' --password='your_password' \
    --fields-terminated-by='|' --lines-terminated-by='\r\n' \
    --replace --low-priority --fields-enclosed-by='"' \
    --fields-escaped-by='#' --ignore-lines='1' --verbose \
    --columns='name_last,name_first,telephone' \
    sales_dept '/tmp/prospect_contact.txt'
```

* This command is run from the system shell, not within the `mariadb` client.
* Lines are continued with `\` for readability here; it can be a single line.
* `--password`: If the password value is omitted, you'll be prompted.
* The database name (`sales_dept`) is specified before the file path.
* **File Naming:** `mariadb-import` expects the text file's name (without extension) to match the target table name (e.g., `prospect_contact.txt` for table `prospect_contact`). If your file is `prospects.txt` and table is `prospect_contact`, you might need to rename the file or import into a temporary table named `prospects` first.
* `--verbose`: Shows progress information.
* You can list multiple text files to import into correspondingly named tables.

### Dealing with Web Hosting Restraints

Some web hosts disable `LOAD DATA INFILE` or `mariadb-import` for security reasons. A workaround involves using `mariadb-dump`:

1. **Prepare Data Locally:** Prepare your delimited text file (e.g., `prospects.txt`).
2. **Local Import:** If you have a local MariaDB server, import the text file into a local table (e.g., `local_db.prospect_contact`) using `LOAD DATA INFILE` as described above.
3.  **Local Export with `mariadb-dump`:** Export the data from your local table into an SQL file containing `INSERT` statements.

    ```bash
    mariadb-dump --user='local_user' --password='local_pass' --no-create-info local_db prospect_contact > /tmp/prospects.sql
    ```

    * `--no-create-info` (or `-t`): Prevents the `CREATE TABLE` statement from being included, outputting only `INSERT` statements. This is useful if the table already exists on the remote server.
4. **Upload SQL File:** Upload the generated `.sql` file (e.g., `prospects.sql`) to your web server (in ASCII mode).
5.  **Remote Import of SQL File:** Log into your remote server's shell and import the SQL file using the `mariadb` client:

    ```bash
    mariadb --user='remote_user' --password='remote_pass' remote_sales_dept < /tmp/prospects.sql
    ```

Handling Duplicates with mariadb-dump Output:

mariadb-dump does not have a REPLACE flag like LOAD DATA INFILE. If the target table might contain duplicates:

* Open the `.sql` file generated by `mariadb-dump` in a text editor.
* Perform a search and replace operation to change all occurrences of `INSERT INTO` to `REPLACE INTO`. The syntax for `INSERT` and `REPLACE` (for the data values part) is similar enough that this often works. Test thoroughly.

### Key Considerations

* **Flexibility:** MariaDB provides powerful and flexible options for data importing. Understanding the details of `LOAD DATA INFILE` and `mariadb-import` can save significant effort.
* **Data Validation:** While these tools are efficient for bulk loading, they may not perform extensive data validation beyond basic type compatibility. Cleanse and validate your data as much as possible before importing.
* **Character Sets:** Ensure your data file's character set is compatible with the target table's character set to avoid data corruption. You can specify character sets in `LOAD DATA INFILE`.
* **Other Tools/Methods:** For very complex transformations or ETL (Extract, Transform, Load) processes, dedicated ETL tools or scripting languages (e.g., Python, Perl with database modules) might be more suitable, though they are beyond the scope of this guide.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
