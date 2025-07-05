# Importing Data into MariaDB

When a MariaDB developer first creates a MariaDB database for a client, often times the client has already accumulated data in other, simpler applications. Being able to convert data easily to MariaDB is critical. In the previous two articles of this MariaDB series, we explored how to set up a database and how to query one. In this third installment, we will introduce some methods and tools for bulk importing of data into MariaDB. This isn't an overly difficult task, but the processing of large amounts of data can be intimidating for a newcomer and as a result it can be a barrier to getting started with MariaDB. Additionally, for intermediate developers, there are many nuances to consider for a clean import, which is especially important for automating regularly scheduled imports. There are also restraints to deal with that may be imposed on a developer when using a web hosting company.

#### Foreign Data Basics

Clients sometimes give developers raw data in formats created by simple database programs like MS Access ®. Since non-technical clients don't typically understand database concepts, new clients often give me their initial data in Excel spreadsheets. Let's first look at a simple method for importing data. The simplest way to deal with incompatible data in any format is to load it up in its original software and to export it out to a delimited text file. Most applications have the ability to export data to a text format and will allow the user to set the delimiters. We like to use the bar (i.e., `|`, a.k.a. pipe) to separate fields and the line-feed to separate records.

For the examples in this article, we will assume that a fictitious client's data was in Excel and that the exported text file will be named `prospects.txt`. It contains contact information about prospective customers for the client's sales department, located on the client's intranet site. The data is to be imported into a MariaDB table called `prospect_contact`, in a database called `sales_dept`. To make the process simpler, the order and number of columns in MS Excel ® (the format of the data provided by the client) should be the same as the table into which the data is going to be imported. So if prospect\_contact has columns that are not included in the spreadsheet, one would make a copy of the spreadsheet and add the missing columns and leave them blank. If there are columns in the spreadsheet that aren't in `prospect_contact`, one would either add them to the MariaDB table, or, if they're not to be imported, one would delete the extra columns from the spreadsheet. One should also delete any headings and footnotes from the spreadsheet. After this is completed then the data can be exported. Since this is Unix Review, we'll skip how one would export data in Excel and assume that the task was accomplished easily enough using its export wizard.

The next step is to upload the data text file to the client's web site by FTP. It should be uploaded in ASCII mode. Binary mode may send binary hard-returns for row-endings. Also, it's a good security habit to upload data files to non-public directories. Many web hosting companies provide virtual domains with a directory like `/public_html`, which is the document root for the Apache web server; it typically contains the site's web pages. In such a situation, `/` is a virtual root containing logs and other files that are inaccessible to the public. We usually create a directory called `tmp` in the virtual root directory to hold data files temporarily for importing into MariaDB. Once that's done, all that's required is to log into MariaDB with the [mariadb](../../clients-and-utilities/mariadb-client/) client as an administrative user (if not root, then a user with `FILE` privileges), and run the proper SQL statement to import the data.

#### Loading Data Basics

The [LOAD DATA INFILE](../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) statement is the easiest way to import data from a plain text file into MariaDB. Below is what one would enter in the [mariadb](../../clients-and-utilities/mariadb-client/) client to load the data in the file called prospects.txt into the table `prospect_contact`:

```sql
LOAD DATA INFILE '/tmp/prospects.txt'
INTO TABLE prospect_contact
FIELDS TERMINATED BY '|';
```

Before entering the statement above, the MariaDB session would, of course, be switched to the sales\_dept database with a [USE](../../reference/sql-statements/administrative-sql-statements/use-database.md) statement. It is possible, though, to specify the database along with the table name (e.g., `sales_dept.prospect_contact`). If the server is running Windows, the forward slashes are still used for the text file's path, but a drive may need to be specified at the beginning of the path: '`c:/tmp/prospects.txt`'. Notice that the SQL statement above has `|` as the field delimiter. If the delimiter was \[TAB]—which is common—then one would replace `|` with here. A line-feed () isn't specified as the record delimiter since it's assumed. If the rows start and end with something else, though, then they will need to be stated. For instance, suppose the rows in the text file start with a double-quote and end with a double-quote and a Windows hard-return (i.e., a return and a line-feed). The statement would need to read like this:

```sql
LOAD DATA INFILE '/tmp/prospects.txt'
INTO TABLE prospect_contact
FIELDS TERMINATED BY '|'
LINES STARTING BY '"'
TERMINATED BY '"\r\n';
```

Notice that the starting double-quote is inside of single-quotes. If one needs to specify a single-quote as the start of a line, one could either put the one single-quote within double-quotes or one could escape the inner single-quote with a back-slash, thus telling MariaDB that the single-quote that follows is to be taken literally and is not part of the statement, per se:

```sql
...
LINES STARTING BY '\'' 
...
```

#### Duplicate Rows

If the table prospect\_contact already contains some of the records that are about to be imported from prospects.txt (that is to say, records with the same primary key), then a decision should be made as to what MariaDB is to do about the duplicates. The SQL statement, as it stands above, will cause MariaDB to try to import the duplicate records and to create duplicate rows in prospect\_contact for them. If the table's properties are set not to allow duplicates, then MariaDB will kick out errors. To get MariaDB to replace the duplicate existing rows with the ones being imported in, one would add the `REPLACE` just before the `INTO TABLE` clause like this:

```sql
LOAD DATA INFILE '/tmp/prospects.txt'
REPLACE INTO TABLE prospect_contact
FIELDS TERMINATED BY '|'
LINES STARTING BY '"'
TERMINATED BY '"\n';
```

To import only records for prospects that are not already in prospect\_contact, one would substitute REPLACE with the `IGNORE` flag. This instructs MariaDB to ignore records read from the text file that already exist in the table.

#### Live Data

For importing data into a table while it's in use, table access needs to be addressed. If access to the table by other users may not be interrupted, then a `LOW_PRIORITY` flag can be added to the [LOAD DATA INFILE](../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) statement. This tells MariaDB that the loading of this data is a low priority. One would only need to change the first line of the SQL statement above to set its priority to low:

```sql
LOAD DATA LOW_PRIORITY INFILE '/tmp/prospects.txt'
...
```

If the `LOW_PRIORITY` flag isn't included, the table will be locked temporarily during the import and other users will be prevented from accessing it.

#### Being Difficult

I mentioned earlier that uploading of the text file should not be done in binary mode so as to avoid the difficulties associated with Windows line endings. If this is unavoidable, however, there is an easy way to import binary row-endings with MariaDB. One would just specify the appropriate hexadecimals for a carriage-return combined with a line-feed (i.e., `CRLF`) as the value of `TERMINATED BY`:

```sql
...
TERMINATED BY 0x0d0a;
```

Notice that there are intentionally no quotes around the binary value. If there were, MariaDB would take the value for text and not a binary code. The semi-colon is not part of the value; it's the SQL statement terminator.

Earlier we also stated that the first row in the spreadsheet containing the column headings should be deleted before exporting to avoid the difficulty of importing the headings as a record. It's actually pretty easy to tell MariaDB to just skip the top line. One would add the following line to the very end of the [LOAD DATA INFILE](../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) statement:

```sql
...
IGNORE 1 LINES;
```

The number of lines for MariaDB to ignore can, of course, be more than one.

Another difficulty arises when some Windows application wizards export data with each field surrounded by double-quotes, as well as around the start and end of records. This can be a problem when a field contains a double-quote. To deal with this, some applications use back-slash () to escape embedded double-quotes, to indicate that a particular double-quote is not a field ending but part of the field's content. However, some applications will use a different character (like a pound-sign) to escape embedded quotes. This can cause problems if MariaDB isn't prepared for the odd escape-character. MariaDB will think the escape character is actually text and the embedded quote-mark, although it's escaped, is a field ending. The unenclosed text that follows will be imported into the next column and the remaining columns will be one column off, leaving the last column not imported. As maddening as this can be, it's quite manageable in MariaDB by adding an `ENCLOSED BY` and an `ESCAPED BY` clause:

```sql
LOAD DATA LOW_PRIORITY INFILE '/tmp/prospects.txt'
REPLACE INTO TABLE prospect_contact
FIELDS TERMINATED BY '"'
ENCLOSED BY '"' ESCAPED BY '#'
LINES STARTING BY '"'
TERMINATED BY '"\n'
IGNORE 1 LINES;
```

In the _Foreign Data Basics_ section above, we said that the columns in the spreadsheet should be put in the same order and quantity as the receiving table. This really isn't necessary if MariaDB is cued in as to what it should expect. To illustrate, let's assume that prospect\_contact has four columns in the following order: `row_id`, `name_first`, `name_last`, `telephone`. Whereas, the spreadsheet has only three columns, differently named, in this order: `Last Name`, `First Name`, `Telephone`. If the spreadsheet isn't adjusted, then the SQL statement will need to be changed to tell MariaDB the field order:

```sql
LOAD DATA LOW_PRIORITY INFILE '/tmp/prospects.txt'
REPLACE INTO TABLE sales_dept.prospect_contact
FIELDS TERMINATED BY 0x09
ENCLOSED BY '"' ESCAPED BY '#'
TERMINATED BY 0x0d0a
IGNORE 1 LINES
(name_last, name_first, telephone);
```

This SQL statement tells MariaDB the name of each table column associated with each spreadsheet column in the order that they appear in the text file. From there it will naturally insert the data into the appropriate columns in the table. As for columns that are missing like row\_id, MariaDB will fill in those fields with the default value if one has been supplied in the table's properties. If not, it will leave the field as NULL. Incidentally, we slipped in the binary `[TAB] (0x09)` as a field delimiter.

#### mariadb-import

For some clients and for certain situations it may be of value to be able to import data into MariaDB without using the [mariadb](../../clients-and-utilities/mariadb-client/) client. This could be necessary when constructing a shell script to import text files on an automated, regular schedule. To accomplish this, the [mariadb-import](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-import.md) (`mysqlimport` before [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105)) utility may be used as it encompasses the [LOAD DATA INFILE](../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) statement and can easily be run from a script. So if one wants to enter the involved SQL statement at the end of the last section above, the following could be entered from the command-line (i.e., not in the [mariadb](../../clients-and-utilities/mariadb-client/) client):

```sql
mariadb-import --user='marie_dyer' --password='angelle1207' \
--fields-terminated-by=0x09 --lines-terminated-by=0x0d0a \
--replace --low-priority --fields-enclosed-by='"' \
 --fields-escaped-by='#' --ignore-lines='1' --verbose \
--columns='name_last, name_first, telephone' \
sales_dept '/tmp/prospect_contact.txt'
```

Although this statement is written over several lines here, it either has to be on the same line when entered or a space followed by a back-slash has to be entered at the end of each line (as seen here) to indicate that more follows. Since the above is entered at the command-line prompt, the user isn't logged into MariaDB. Therefore the first line contains the user name and password for [mariadb-import](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-import.md) to give to MariaDB. The password itself is optional, but the directive `--password` (without the equal sign) isn't. If the password value is not given in the statement, then the user will be prompted for it. Notice that the order of directives doesn't matter after the initial command, except that the database and file name go last. Regarding the file name, its prefix must be the same as the table—the dot and the extension are ignored. This requires that `prospects.txt` be renamed to `prospect_contact.txt`. If the file isn't renamed, then MariaDB would create a new table called prospects and the `--replace` option would be pointless. After the file name, incidentally, one could list more text files, separated by a space, to process using [mariadb-import](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-import.md). We've added the `--verbose` directive so as to be able to see what's going on. One probably would leave this out in an automated script. By the way, `--low-priority` and `--ignore-lines` are available.

#### Web Hosting Restraints

Some web hosting companies do not allow the use of [LOAD DATA INFILE](../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) or [mariadb-import](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-import.md) statements due to security vulnerabilities in these statements for them. To get around this, some extra steps are necessary to avoid having to manually enter the data one row at a time. First, one needs to have MariaDB installed on one's local workstation. For simplicity, we'll assume this is done and is running Linux on the main partition and MS Windows® on an extra partition. Recapping the on-going example of this article based on these new circumstances, one would boot up into Windows and start MS Excel®, load the client's spreadsheet into it and then run the export wizard as before—saving the file prospects.txt to the 'My Documents' directory. Then one would reboot into Linux and mount the Windows partition and copy the data text file to `/tmp` in Linux, locally. Next one would log into the local (not the client's) MariaDB server and import the text file using a [LOAD DATA INFILE](../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) as we've extensively outline above. From there one would exit MariaDB and export the data out of MariaDB using the [mariadb-dump](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) utility locally, from the command-line like this:

```bash
mariadb-dump --user='root' --password='geronimo' sales_dept prospect_contact > /tmp/prospects.sql
```

This creates an interesting text file complete with all of the SQL commands necessary to insert the data back into MariaDB one record, one [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) at a time. When you run [mariadb-import](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-import.md), it's very educational to open up it in a text editor to see what it generates.

After creating this table dump, one would upload the resulting file (in ASCII mode) to the `/tmp` directory on the client's web server. From the command prompt on the client's server one would enter the following:

```bash
mariadb --user='marie_dyer' --password='angelle12107' sales_dept < '/tmp/prospects.sql'
```

This line along with the [mariadb-dump](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) line show above are simple approaches. Like the Windows application wizard, with mariadb-dump one can specify the format of the output file and several other factors. One important factor related to the scenario used in this article is the [CREATE TABLE](../../reference/sql-statements/data-definition/create/create-table.md) statement that will be embedded in the [mariadb-dump](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) output file. This will fail and kick out an error because of the existing table prospect\_contact in the client's database. To limit the output to only [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statements and no [CREATE TABLE](../../reference/sql-statements/data-definition/create/create-table.md) statements, the [mariadb-dump](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) line would look like this:

```bash
mariadb-dump -u marie_dyer -p --no-create-info sales_dept prospect_contact > /tmp/prospects.sql
```

Notice that we've used acceptable abbreviations for the user name and the password directives. Since the password was given here, the user will be prompted for it.

The [mariadb-dump](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) utility usually works pretty well. However, one feature it's lacking at this time is a `REPLACE` flag as is found in the [LOAD DATA INFILE](../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) statement and with the [mariadb-import](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-import.md) tool. So if a record already exists in the `prospect_contact`, it won't be imported. Instead it will kick out an error message and stop at that record, which can be a mess if one has imported several hundred rows and have several hundred more to go. One easy fix for this is to open up `prospects.sql` in a text editor and do a search on the word `INSERT` and replace it with `REPLACE`. The syntax of both of these statements are the same, fortunately. So one would only need to replace the keyword for new records to be inserted and for existing records to be replaced.

#### Concluding Observations and Admissions

It's always amazing to me how much can be involved in the simplest of statements in MariaDB. MariaDB is deceptively powerful and feature rich. One can keep the statements pretty minimal or one can develop a fairly detailed, single statement to allow for accuracy of action. There are many other aspects of importing data into MariaDB that we did not address—in particular dealing with utilities. We also didn't talk about the Perl modules that could be used to convert data files. These can be useful in scripting imports. There are many ways in which one can handle importing data. Hopefully, this article has presented most of the basics and pertinent advanced details that may be of use to most MariaDB developers.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
