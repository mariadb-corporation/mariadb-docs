---
description: >-
  Restore a single database from a full backup. Learn the procedure to extract
  and recover a specific database schema from a larger backup set.
---

# Individual Database Restores with mariadb-backup from Full Backup

{% include "../../../.gitbook/includes/mariadb-backup-was-previous....md" %}

This method is to solve a flaw with mariadb-backup; it cannot do single database restores from a full backup easily. There is a [blog post that details a way to do this](https://mariadb.com/resources/blog/how-to-restore-a-single-database-from-mariadb-backup/), but it's a manual process which is fine for a few tables but if you have hundreds or even thousands of tables then it would be impossible to do quickly.

We can't just move the data files to the datadir as the tables are not registered in the engines, so the database will error. Currently, the only effective method is to a do full restore in a test database and then dump the database that requires restoring or running a partial backup.

**This has only been tested with InnoDB. Also, if you have stored procedures or triggers then these will need to be deleted and recreated.**

Some of the issues that this method overcomes:

* Tables not registered in the InnoDB engine so will error when you try to select from a table if you move the data files into the datadir
* Tables with foreign keys need to be created without keys, otherwise it will error when you discard the tablespace

### Single Node

Below is the process to perform a single database restore.

Firstly, we will need the table structure from a mariadb-dump backup with the --no-data option. I recommend this is done at least once per day or every six hours via a cronjob. As it is just the structure, it are very fast.

```bash
mariadb-dump -u root -p --all-databases --no-data > nodata.sql
```

Using SED to return only the table structure we require, then use vim or another text editor to make sure nothing is left.

```
sed -n '/Current Database: `DATABASENAME`/, /Current Database:/p' nodata.sql > trimednodata.sql
vim trimednodata.sql
```

Prepare the backup with any incremental-backup-and-restores that you have, and then run the following on the full backup folder using the `--export` option to generate files with .cfg extensions which InnoDB will look for.

```bash
mariadb-backup --prepare --export --target-dir=/media/backups/fullbackupfolder
```

Once we have done these steps, we can then import the table structure. If you have used the `--all-databases` option, then you will need to either use SED or open it in a text editor and export out tables that you require. You will also need to log in to the database and create the database if the dump file doesn't. Run the following command below:

```bash
mysql -u root -p schema_name < nodata.sql
```

Once the structure is in the database, we have now registered the tables to the engine. Next, we will run the following statements in the information\_schema database, to export statements to import/discard table spaces and drop and create foreign keys which we will use later. (edit the `CONSTRAINT_SCHEMA` and `TABLE_SCHEMA` `WHERE` clause to the database you are restoring. Also, add the following lines after your `SELECT` and before the `FROM` to have MariaDB export the files to the OS)

```sql
SELECT ...
INTO OUTFILE '/tmp/filename.SQL'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
FROM ...
```

The following are the statements that we will need later.

```sql
USE information_schema;
SELECT concat("ALTER TABLE ",table_name," DISCARD TABLESPACE;")  AS discard_tablespace
FROM information_schema.tables 
WHERE TABLE_SCHEMA="DATABASENAME";

SELECT concat("ALTER TABLE ",table_name," IMPORT TABLESPACE;") AS import_tablespace
FROM information_schema.tables 
WHERE TABLE_SCHEMA="DATABASENAME";

SELECT 
CONCAT ("ALTER TABLE ", rc.CONSTRAINT_SCHEMA, ".",rc.TABLE_NAME," DROP FOREIGN KEY ", rc.CONSTRAINT_NAME,";") AS drop_keys
FROM REFERENTIAL_CONSTRAINTS AS rc
WHERE CONSTRAINT_SCHEMA = 'DATABASENAME';

SELECT
CONCAT ("ALTER TABLE ", 
KCU.CONSTRAINT_SCHEMA, ".",
KCU.TABLE_NAME," 
ADD CONSTRAINT ", 
KCU.CONSTRAINT_NAME, " 
FOREIGN KEY ", "
(`",KCU.COLUMN_NAME,"`)", " 
REFERENCES `",REFERENCED_TABLE_NAME,"` 
(`",REFERENCED_COLUMN_NAME,"`)" ," 
ON UPDATE " ,(SELECT UPDATE_RULE FROM REFERENTIAL_CONSTRAINTS WHERE CONSTRAINT_NAME = KCU.CONSTRAINT_NAME AND CONSTRAINT_SCHEMA = KCU.CONSTRAINT_SCHEMA)," 
ON DELETE ",(SELECT DELETE_RULE FROM REFERENTIAL_CONSTRAINTS WHERE CONSTRAINT_NAME = KCU.CONSTRAINT_NAME AND CONSTRAINT_SCHEMA = KCU.CONSTRAINT_SCHEMA),";") AS add_keys
FROM KEY_COLUMN_USAGE AS KCU
WHERE KCU.CONSTRAINT_SCHEMA = 'DATABASENAME'
AND KCU.POSITION_IN_UNIQUE_CONSTRAINT >= 0
AND KCU.CONSTRAINT_NAME NOT LIKE 'PRIMARY';
```

Once we have run those statements, and they have been exported to a Linux directory or copied from a GUI interface.

Run the `ALTER DROP KEYS` statements in the database.

```sql
ALTER TABLE schemaname.tablename DROP FOREIGN KEY key_name;
...
```

Once completed, run the `DROP TABLE SPACE` statements in the database:

```sql
ALTER TABLE test DISCARD TABLESPACE;
...
```

Exit out the database and change into the directory of the full backup location. Run the following commands to copy all the `.cfg` and `.ibd` files to the datadir such as _`/var/lib/mysql/testdatabase`_ (change the `datadir` location if needed). Learn more about files that `mariadb-backup` generates with files-created-by-mariadb-backup.

```bash
cp *.cfg /var/lib/mysql
cp *.ibd /var/lib/mysql
```

After moving the files, it is very important that MySQL is the owner of the files, otherwise it won't have access to them and will error when we import the tablespaces.

```bash
sudo chown -R mysql:mysql /var/lib/mysql
```

Run the import table spaces statements in the database.

```sql
ALTER TABLE test IMPORT TABLESPACE;
...
```

Run the add key statements in the database

```sql
ALTER TABLE schmeaname.tablename ADD CONSTRAINT key_name FOREIGN KEY (`column_name`) REFERENCES `foreign_table` (`colum_name`) ON UPDATE NO ACTION ON DELETE NO ACTION;
...
```

We have successfully restored a single database. To test that this has worked, we can do a basic check on some tables.

```sql
USE DATABASE
SELECT * FROM test LIMIT 10;
```

### Replica nodes

If you have a primary-replica set up, it would be best to follow the sets above for the primary node and then either take a full mariadb-dump or take a new full mariadb-backup and restore this to the replica. You can find more information about restoring a replica with mariadb-backup in Setting up a Replica with mariadb-backup

After running the below command, copy to the replica and use the `LESS` linux command to grab the change master statement. Remember to follow this process: Stop replica > restore data > run `CHANGE MASTER` statement > start replica again.

```bash
mariadb-dump -u user -p --single-transaction --master-data=2 > fullbackup.sql
```

Please follow Setting up a Replica with mariadb-backup on restoring a replica with `mariadb-backup`:

```bash
$ mariadb-backup --backup \
   --slave-info --safe-slave-backup \
   --target-dir=/var/mariadb/backup/ \
   --user=mariadb-backup --password=mypassword
```

### Galera Cluster

For this process to work with Galera cluster, we first need to understand that some statements are not replicated across Galera nodes. One of which is the `DISCARD` and `IMPORT` for `ALTER TABLES` statements, and these statements will need to be ran on all nodes. We also need to run the OS level steps on each server as seen below.

Run the `ALTER DROP KEYS` statements on ONE NODE as these are replicated.

```sql
ALTER TABLE schemaname.tablename DROP FOREIGN KEY key_name;
...
```

Once completed, run the `DROP TABLE SPACE` statements on EVERY NODE, as these are not replicated.

```sql
ALTER TABLE test DISCARD TABLESPACE;
...
```

Exit out the database and change into the directory of the full backup location. Run the following commands to copy all the `.cfg` and `.ibd` files to the datadir such as _`/var/lib/mysql/testdatabase`_ (change the `datadir` location if needed). Learn more about files that `mariadb-backup` generates with files-created-by-mariadb-backup. This step needs to be done on all nodes. You will need to copy the backup files to each node, we can use the same backup on all nodes.

```bash
cp *.cfg /var/lib/mysql
cp *.ibd /var/lib/mysql
```

After moving the files, it is very important that MySQL is the owner of the files, otherwise it won't have access to them and will error when we import the tablespaces.

```bash
sudo chown -R mysql:mysql /var/lib/mysql
```

Run the import table spaces statements on EVERY NODE.

```sql
ALTER TABLE test IMPORT TABLESPACE;
...
```

Run the add key statements on ONE NODE.

```sql
ALTER TABLE schmeaname.tablename ADD CONSTRAINT key_name FOREIGN KEY (`column_name`) REFERENCES `foreign_table` (`colum_name`) ON UPDATE NO ACTION ON DELETE NO ACTION;
...
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
