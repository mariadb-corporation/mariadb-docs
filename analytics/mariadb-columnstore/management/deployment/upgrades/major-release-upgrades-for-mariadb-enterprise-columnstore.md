---
description: >-
  Major-release upgrade procedure for MariaDB Enterprise ColumnStore (CS 5 to
  22.08): full data backup, optional reuse of existing servers, and
  stage-by-stage migration to the new version.
---

# Major Release Upgrades for MariaDB Enterprise ColumnStore

This page provides a major release upgrade procedure for MariaDB Enterprise ColumnStore. A major release upgrade is an upgrade from an older major release to a newer major release, such as an upgrade from MariaDB Enterprise ColumnStore 5 to MariaDB Enterprise ColumnStore 22.08.

### Compatibility

* Enterprise ColumnStore 5
* Enterprise ColumnStore 6
* Enterprise ColumnStore 22.08

### Prerequisites

This procedure assumes that the new Enterprise ColumnStore version will be installed onto new servers.

**To reuse existing servers** for the new Enterprise ColumnStore version, you must adapt the procedure detailed below. After step 1, confirm all data has been backed-up and verify backups. The old version of Enterprise ColumnStore should then be uninstalled, and all Enterprise ColumnStore files should be deleted before continuing with step 2.

### Step 1: Backup/Export Schemas and Data

On the **old ColumnStore cluster**, perform a full backup.

MariaDB recommends backing up the table schemas to a single SQL file and backing up the table data to table-specific CSV files.

1.  For each table, obtain the table's schema by executing the `SHOW CREATE TABLE` [statement](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-create-table):

    ```sql
    SHOW CREATE TABLE DATABASE_NAME.TABLE_NAME\G
    ```

    Backup the table schemas by copying the output to an SQL file. This procedure assumes that the SQL file is named `schema-backup.sql`.
2.  For each table, backup the table data to a CSV file using the `SELECT .. INTO OUTFILE` [statement](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select-into-outfile):

    ```sql
    SELECT * INTO OUTFILE '/path/to/DATABASE_NAME-TABLE_NAME.csv'
    FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    FROM DATABASE_NAME.TABLE_NAME;
    ```
3. Copy the SQL file containing the table schemas and the CSV files containing the table data to the primary node of the new ColumnStore cluster.

### Step 2: Install New Major Release

On the **new ColumnStore cluster**, follow the deployment instructions of the desired topology for the new ColumnStore version.

For deployment instructions, see "[MariaDB Topologies](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies)".

### Step 3: Restore/Import Data

On the **new ColumnStore cluster**, restore the table schemas and data.

1.  Restore the schema backup using [mariadb client](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client):

    ```bash
    mariadb --host HOST --port PORT --user USER --password < schema-backup.sql
    ```

    * `HOST` and `PORT` should refer to the following:
      * If you are connecting with MaxScale as a proxy, they should refer to the host and port of the MaxScale listener
      * If you are connecting directly to a multi-node ColumnStore cluster, they should refer to the host and port of the primary ColumnStore node
      * If you are connecting directly to single-node ColumnStore, they should refer to the host and port of the ColumnStore node
    * When the command is executed, `mariadb` client prompts for the user password
2.  For each table, restore the data from the table's CSV file by executing the [cpimport utility](../../../clients-and-tools/data-import/mariadb-enterprise-columnstore-data-loading-with-cpimport.md) on the primary ColumnStore node:

    ```bash
    sudo cpimport -s ',' \
       DATABASE_NAME \
       TABLE_NAME \
       /path/to/DATABASE_NAME-TABLE_NAME.csv
    ```

### Step 4: Test

On the **new ColumnStore cluster**, verify that the table schemas and data have been restored.

1.  For each table, verify the table's definition by executing the `SHOW CREATE TABLE` statement:

    ```sql
    SHOW CREATE TABLE DATABASE_NAME.TABLE_NAME\G
    ```
2.  For each table, verify the number of rows in the table by executing `SELECT COUNT(*)`:

    ```sql
    SELECT COUNT(*) FROM DATABASE_NAME.TABLE_NAME;
    ```
3.  For each table, verify the data in the table executing the [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) statement.

    If the table is very large, you can limit the number of rows in the result set by adding a `LIMIT` clause:

    ```sql
    SELECT * FROM DATABASE_NAME.TABLE_NAME LIMIT 100;
    ```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
