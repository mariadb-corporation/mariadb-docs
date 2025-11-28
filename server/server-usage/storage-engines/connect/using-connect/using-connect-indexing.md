# Using CONNECT - Indexing

{% hint style="warning" %}
This storage engine has been deprecated.
{% endhint %}

[Indexing](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/) is one of the main ways to optimize queries. Key columns, in\
particular when they are used to join tables, should be indexed. But what\
should be done for columns that have only few distinct values? If they are\
randomly placed in the table they should not be indexed because reading many\
rows in random order can be slower than reading the entire table sequentially.\
However, if the values are sorted or clustered, indexing can be acceptable\
because [CONNECT](../) indexes store the values in the order they appear into the\
table and this will make retrieving them almost as fast as reading them\
sequentially.

CONNECT provides four indexing types:

1. Standard Indexing
2. Block Indexing
3. Remote Indexing
4. Dynamic Indexing

## Standard Indexing

CONNECT standard indexes are created and used as the ones of other storage engines although they\
have a specific internal format. The CONNECT handler supports the use of standard indexes for most\
of the file based table types.

You can define them in the [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) statement, or either using the CREATE\
INDEX statement or the [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/) statement. In all cases, the index files are\
automatically made. They can be dropped either using the [DROP INDEX](../../../../reference/sql-statements/data-definition/drop/drop-index.md) statement\
or the [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/) statement, and this erases the index files.

Indexes are automatically reconstructed when the table is created, modified by\
INSERT, UPDATE or DELETE commands, or when the SEPINDEX option is changed.\
If you have a lot of changes to do on a table at one moment, you can use table\
locking to prevent indexes to be reconstructed after each statement. The\
indexes are reconstructed when unlocking the table. For instance:

```
LOCK TABLE t1 WRITE;
INSERT INTO t1 VALUES(...);
INSERT INTO t1 VALUES(...);
...
UNLOCK TABLES;
```

If a table was modified by an external application that does not handle indexing, the indexes must be\
reconstructed to prevent returning false or incomplete results. To do this, use the [OPTIMIZE TABLE](../../../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md) command.

For outward tables, index files are not erased when dropping the table. This is\
the same as for the data file and preserves the possibility of several users\
using the same data file via different tables.

Unlike other storage engines, CONNECT constructs the indexes as files that are\
named by default from the data file name, not from the table name, and located\
in the data file directory. Depending on the SEPINDEX table option, indexes are\
saved in a unique file or in separate files (if SEPINDEX is true). For\
instance, if indexes are in separate files, the primary index of the table_dept.dat_ of type DOS is a file named _dept\_PRIMARY.dnx_. This makes\
possible to define several tables on the same data file, with eventual\
different options such as mapped or not mapped, and to share the index files as\
well.

If the index file should have a different name, for instance because several\
tables are created on the same data file with different indexes, specify the\
base index file name with the XFILE\_NAME option.

**Note1:** Indexed columns must be declared NOT NULL; CONNECT doesn't support\
indexes containing null values.

**Note 2:** MRR is used by standard indexing if it is enabled.

**Note 3:** Prefix indexing is not supported. If specified, the CONNECT engine ignores the prefix and builds a whole index.

### Handling index errors

The way CONNECT handles indexing is very specific. All table modifications are\
done regardless of indexing. Only after a table has been modified, or when an`OPTIMIZE TABLE` command is sent are the indexes made. If an error occurs,\
the corresponding index is not made. However, CONNECT being a non-transactional\
engine, it is unable to roll back the changes made to the table. The main\
causes of indexing errors are:

* Trying to index a nullable column. In this case, you can alter the table to\
  declare the column as not nullable or, if the column is nullable indeed, make\
  it not indexed.
* Entering duplicate values in a column indexed by a unique index. In this\
  case, if the index was wrongly declared as unique, alter is declaration to\
  reflect this. If the column should really contain unique values, you must\
  manually remove or update the duplicate values.

In both cases, after correcting the error, remake the indexes with the [OPTIMIZE TABLE](../../../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md) command.

### Index file mapping

To accelerate the indexing process, CONNECT makes an index structure in memory from the index\
file. This can be done by reading the index file or using it as if it was in memory by “file mapping”. On\
enabled versions, file mapping is used according to the boolean [connect\_indx\_map](../connect-system-variables.md#connect_indx_map) system variable. Set it to 0 (file read) or 1 (file mapping).

## Block Indexing

To accelerate input/output, CONNECT uses when possible a read/write mode by blocks of n rows, n\
being the value given in the BLOCK \_ SIZE option of the Create Table, or a default value depending on\
the table type. This is automatic for fixed files ([FIX](../connect-table-types/connect-table-types-data-files.md#dos-and-fix-table-types), [BIN](../connect-table-types/connect-table-types-data-files.md#bin-table-type), [DBF](../connect-table-types/connect-table-types-data-files.md#dbf-type) or [VEC](../connect-table-types/connect-table-types-data-files.md#vec-table-type-vector)), but must be specified for\
variable files ([DOS](../connect-table-types/connect-table-types-data-files.md#dos-and-fix-table-types) , [CSV](../connect-table-types/connect-table-types-data-files.md#csv-and-fmt-table-types) or [FMT](../connect-table-types/connect-table-types-data-files.md#fmt-type) ).

For blocked tables, further optimization can be achieved if the data values for some columns are\
“clustered” meaning that they are not evenly scattered in the table but grouped in some consecutive\
rows. Block indexing permits to skip blocks in which no rows fulfill a conditional predicate without\
having even to read the block. This is true in particular for sorted columns.

You indicate this when creating the table by using the DISTRIB =d column option. The enum value d can\
be _scattered_, _clustered_, or _sorted_. In general only one column can be sorted. Block indexing is used\
only for clustered and sorted columns.

### Difference between standard indexing and block indexing

* Block indexing is internally handled by CONNECT while reading sequentially a table data. This\
  means in particular that when standard indexing is used on a table, block indexing is not used.
* In a query, only one standard index can be used. However, block indexing can combine the\
  restrictions coming from a where clause implying several clustered/sorted columns.
* The block index files are faster to make and much smaller than standard index files.

### Notes for this Release:

* On all operations that create or modify a table, CONNECT automatically calculates or recalculates\
  and saves the mini/maxi or bitmap values for each block, enabling it to skip block containing no\
  acceptable values. In the case where the optimize file does not correspond anymore to the table,\
  because it has been accidentally destroyed, or because some column definitions have been altered,\
  you can use the OPTIMIZE TABLE command to reconstruct the optimization file.
* Sorted column special processing is currently restricted to ascending sort. Column sorted in\
  descending order must be flagged as clustered. Improper sorting is not checked in Update or Insert\
  operations but is flagged when optimizing the table.
* Block indexing can be done in two ways. Keeping the min/max values existing for each block, or\
  keeping a bitmap allowing knowing what column distinct values are met in each blocks. This\
  second ways often gives a better optimization, except for sorted columns for which both are\
  equivalent. The bitmap approach can be done only on columns having not too many distinct\
  values. This is estimated by the MAX \_ DIST option value associated to the column when creating the\
  table. Bitmap block indexing are used if this number is not greater than the MAXBMP setting for\
  the database.
* CONNECT cannot perform block indexing on case insensitive character columns. To force block\
  indexing on a character column, specify its charset as not case insensitive, for instance as binary.\
  However this will also apply to all other clauses, this column being now case sensitive.

## Remote Indexing

Remote indexing is specific to the [MYSQL](../connect-table-types/connect-mysql-table-type-accessing-mysqlmariadb-tables.md) table type. It is equivalent to what the [FEDERATED](../../federatedx-storage-engine/)\
storage does. A MYSQL table does not support indexes per se. Because access to the table is handled\
remotely, it is the remote table that supports the indexes. What the MYSQL table does is just to add a WHERE clause to the [SELECT](../../../../reference/sql-statements/data-manipulation/selecting-data/select.md) command sent to the remote server allowing the remote server to use\
indexing when applicable.\
Note however that because CONNECT adds when possible all or part of the where clause of the\
original query, this happens often even if the remote indexed column is not declared locally indexed.\
The only, but very important, case a column should be locally declared indexed is when it is used to\
join tables. Otherwise, the required where clause would not be added to the sent SELECT query.

See [Indexing of MYSQL tables](../connect-table-types/connect-mysql-table-type-accessing-mysqlmariadb-tables.md) for more.

## Dynamic Indexing

An indexed created as “dynamic” is a standard index which, in some cases, can be reconstructed for a\
specific query. This happens in particular for some queries where two tables are joined by an indexed\
key column. If the “from” table is big and the “to” big table reduced in size because of a where clause,\
it can be worthwhile to reconstruct the index on this reduced table.

Because of the time added by reconstructing the index, this is valuable only if the time gained by\
reducing the index size if more than this reconstruction time. This is why this should not be done if the\
“from” table is small because there will not be enough row joining to compensate for the additional time.\
Otherwise, the gain of using a dynamic index is:

* Indexing time is a little faster if the index is smaller.
* The join process will return only the rows fulfilling the where clause.
* Because the table is read sequentially when reconstructing the index there no need for MRR.
* Constructing the index can be faster if the table is reduced by block indexing.
* While constructing the index, CONNECT also stores in memory the values of other used columns.

This last point is particularly important. It means that after the index is reconstructed, the join is done\
on a temporary memory table.

Unfortunately, storage engines being called independently by MariaDB for each table, CONNECT has\
no global information to decide when it is good to use dynamic indexing. This is why you should use it\
only on cases where you see that some important join queries take a very long time and only on\
columns used for joining the table. How to declare an index to be dynamic is by using the Boolean\
DYNAM index option. For instance, the query:

```
SELECT d.diag, COUNT(*) cnt FROM diag d, patients p WHERE d.pnb =
p.pnb AND ageyears < 17 AND county = 30 AND drg <> 11 AND d.diag
BETWEEN 4296 AND 9434 GROUP BY d.diag ORDER BY cnt DESC;
```

Such a query joining the diag table to the patients table may last a very long time if the tables are big.\
To declare the primary key on the pnb column of the patients table to be dynamic:

```
ALTER TABLE patients DROP PRIMARY KEY;
ALTER TABLE patients ADD PRIMARY KEY (pnb) COMMENT 'DYNAMIC' dynam=1;
```

Note 1: The comment is not mandatory here but useful to see that the index is dynamic if you use the [SHOW INDEX](../../../../reference/sql-statements/administrative-sql-statements/show/show-index.md) command.

Note 2: There is currently no way to just change the DYNAM option without dropping and adding the\
index. This is unfortunate because it takes time.

## Virtual Indexing

It applies only to the virtual tables of type [VIR](../connect-table-types/connect-table-types-vir.md) and must be made on a column specifying `SPECIAL=ROWID` or `SPECIAL=ROWNUM`.

<sub>_This page is licensed: GPLv2_</sub>

{% @marketo/form formId="4316" %}
