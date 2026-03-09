---
description: >-
  This guide outlines the benefits and process of migrating tables from MyISAM
  to InnoDB, highlighting key differences like transaction support and foreign
  keys.
---

# Converting Tables from MyISAM to InnoDB

## The task

You have decided to change one or more tables from [MyISAM](myisam-storage-engine/) to [InnoDB](innodb/). That should be\
as simple as `ALTER TABLE foo ENGINE=InnoDB`. But you have heard that there might\
be some subtle issues.

This describes possible issues that may arise and what to do about them.

_Recommendation._ One way to assist in searching for issues in is to do (at least in \*nix)

```bash
mysqldump --no-data --all-databases >schemas
egrep 'CREATE|PRIMARY' schemas   # Focusing on PRIMARY KEYs
egrep 'CREATE|FULLTEXT' schemas  # Looking for FULLTEXT indexes
egrep 'CREATE|KEY' schemas       # Looking for various combinations of indexes
```

Understanding how the indexes work will help you better understand what might\
run faster or slower in InnoDB.

## INDEX Issues

_(Most of these Recommendations and some of these Facts have exceptions.)_

_Fact._ Every InnoDB table has a PRIMARY KEY. If you do not provide one, then the\
first non-NULL UNIQUE key is used. If that can't be done, then a 6-byte,\
hidden, integer is provided.

_Recommendation._ Look for tables without a PRIMARY KEY. Explicitly specify a\
PRIMARY KEY, even if it's an artificial AUTO\_INCREMENT. This is not an absolute\
requirement, but it is a stronger admonishment for InnoDB than for MyISAM. Some\
day you may need to walk through the table; without an explicit PK, you can't\
do it.

_Fact._ The fields of the PRIMARY KEY are included in each Secondary key.

* Check for redundant indexes with this in mind.

```sql
PRIMARY KEY(id),
INDEX(b), -- effectively the same as INDEX(b, id)
INDEX(b, id) -- effectively the same as INDEX(b)
```

* (Keep one of the INDEXes, not both)
* Note subtle things like

```sql
PRIMARY KEY(id),
UNIQUE(b), -- keep for uniqueness constraint
INDEX(b, id) -- DROP this one
```

* Also, since the PK and the data coexist:

```sql
PRIMARY KEY(id),
INDEX(id, b) -- DROP this one; it adds almost nothing
```

_Contrast._ This feature of MyISAM is not available in InnoDB; the value of\
'id' will start over at 1 for each different value of 'abc':

```sql
id INT UNSIGNED NOT NULL AUTO_INCREMENT,
PRIMARY KEY (abc, id)
```

A way to simulate the MyISAM 'feature' might be something like: What you want\
is this, but it won't work because it is referencing the table twice:

```sql
INSERT INTO foo
    (other, id, ...)
    VALUES
    (123, (SELECT MAX(id)+1 FROM foo WHERE other = 123), ...);
```

Instead, you need some variant on this. (You may already have a BEGIN...COMMIT.)

```sql
BEGIN;
SELECT @id := MAX(id)+1 FROM foo WHERE other = 123 FOR UPDATE;
INSERT INTO foo
    (other, id, ...)
    VALUES
    (123, @id, ...);
COMMIT;
```

Having a transaction is mandatory to prevent another thread from grabbing the\
same id.

_Recommendation._ Look for such PRIMARY KEYs. If you find such, ponder how\
to change the design. There is no straightforward workaround. However, the\
following may be ok. (Be sure that the datatype for id is big enough since it\
won't start over.):

```sql
id INT UNSIGNED NOT NULL AUTO_INCREMENT,
PRIMARY KEY (abc, id),
UNIQUE(id)
```

_Recommendation._ Keep the PRIMARY KEY short. If you have Secondary keys,\
remember that they include the fields of the PK. A long PK would make the\
Secondary keys bulky. Well, maybe not — if the is a\
lot of overlap in fields. Example: `PRIMARY KEY(a,b,c), INDEX(c,b,a)`\
— no extra bulk.

_Recommendation._ Check AUTO\_INCREMENT sizes.

* BIGINT is almost never needed. It wastes at least 4 bytes per row (versus\
  INT).
* Always use UNSIGNED and NOT NULL.
* MEDIUMINT UNSIGNED (16M max) might suffice instead of INT
* Be sure to be pessimistic — it is painful to ALTER.

_Contrast._ "Vertical Partitioning". This is where you artificially split a\
table to move bulky columns (eg, a BLOB) into another, parallel, table. It is\
beneficial in MyISAM to avoid stepping over the blob when you don't need to\
read it. InnoDB stores BLOB and TEXT differently — 767\
bytes are in the record, the rest is in some other block. So, it may (or may\
not) be worth putting the tables back together. Caution: An InnoDB row is\
limited to 8KB, and the 767 counts against that.

_Fact._ FULLTEXT (prior to [MariaDB 10.0.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.5)) and SPATIAL indexes are not available in InnoDB. Note that MyISAM and InnoDB [FULLTEXT indexes](../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/) use different [stopword](../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/full-text-index-stopwords.md) lists and different system variables.

_Recommendation._ Search for such indexes. Keep such tables in MyISAM.\
Better yet, do Vertical Partitioning (see above) to split out the minimum\
number of columns from InnoDB.

_Fact._ The maximum length of an INDEX is different between the Engines.\
(This change is not likely to hit you, but watch out.) MyISAM allows 1000\
bytes; InnoDB allows 767 bytes, just big enough for a

```sql
VARCHAR(255) CHARACTER SET utf8.

ERROR 1071 (42000): Specified key was too long; max key length is 767 bytes
```

_Fact._ The PRIMARY KEY is included in the data. Hence, SHOW TABLE STATUS\
will show and `Index_length` of 0 bytes (or 16KB) for a table with no\
secondary indexes. Otherwise, `Index_length` is the total size for the\
secondary keys.

_Fact._ The PRIMARY KEY is included in the data. Hence, exact match by PK\
may be a little faster with InnoDB. And, "range" scans by PK are likely to be\
faster.

_Fact._ A lookup by Secondary Key traverses the secondary key's BTree, grabs\
the PRIMARY KEY, then traverses the PK's BTree. Hence, secondary key lookups\
are a little more cumbersome in InnoDB.

_Contrast._ The fields of the PRIMARY KEY are included in each Secondary\
key. This may lead to "Using index" (in the EXPLAIN plan) for InnoDB for cases\
where it did not happen in MyISAM. (This is a slight performance boost, and\
counteracts the double-lookup otherwise needed.) However, when "Using index"\
would be useful on the PRIMARY KEY, MyISAM would do an "index scan", yet InnoDB\
effectively has to do a "table scan".

_Same as MyISAM._ Almost always

```sql
INDEX(a)   -- DROP this one because the other one handles it.
INDEX(a,b)
```

_Contrast._ The data is stored in PK order. This means that "recent" records\
are 'clustered' together at the end. This may give you better 'locality of\
reference' than in MyISAM.

_Same as MyISAM._ The optimizer almost never uses two indexes in a single\
SELECT. (5.1 will occasionally do "index merge".) SELECT in subqueries and\
UNIONs can independently pick indexes.

_Subtle issue._ When you DELETE a row, the AUTO\_INCREMENT id are burned.\
Ditto for REPLACE, which is a DELETE plus an INSERT.

_Very subtle issue._ Replication occurs on COMMIT. If you have multiple\
threads using transactions, the AUTO\_INCREMENTs can arrive at a slave out of\
order. One transaction BEGINs, grabs an id. Then another transaction grabs an\
id but COMMITs before the first finishes.

_Same as MyISAM._ "Prefix" indexing is usually bad in both InnoDB and\
MyISAM. Example: `INDEX(foo(30))`

## Non-INDEX Issues

Disk space for InnoDB is likely to be 2-3 times as much as for MyISAM.

MyISAM and InnoDB use RAM radically differently. If you change all your tables,\
you should make significant adjustments:

* [key\_buffer\_size](myisam-storage-engine/myisam-system-variables.md#key_buffer_size) — small but non-zero; say, 10M;
* [innodb\_buffer\_pool\_size](innodb/innodb-system-variables.md) — 70% of available RAM

InnoDB has essentially no need for CHECK, OPTIMIZE, or ANALYZE. Remove them\
from your maintenance scripts. (No real harm if you keep them.)

Backup scripts may need checking. A MyISAM table can be backed up by copying\
three files. With InnoDB this is only possible if [innodb\_file\_per\_table](innodb/innodb-system-variables.md) is set to 1. Before [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/changes-improvements-in-mariadb-10-0),\
capturing a table or database for copying from production to a development\
environment was not possible. Change to [mysqldump](../../clients-and-utilities/legacy-clients-and-utilities/mysqldump.md). Since [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/changes-improvements-in-mariadb-10-0) a hot copy can be created - see [Backup and restore overview](../backup-and-restore/backup-and-restore-overview.md).

Before [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5), the DATA DIRECTORY [table option](../../reference/sql-statements/data-definition/create/create-table.md#data-directory-index-directory) was not supported for InnoDB. Since [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) it is supported, but only in CREATE TABLE. INDEX DIRECTORY has no effect, since InnoDB does not use separate files for indexes. To better balance the workload through several disks, the paths of some InnoDB log files can also be changed.

Understand autocommit and BEGIN/COMMIT.

* (default) autocommit = 1: In the absence of any BEGIN or COMMIT statements,\
  every statement is a transaction by itself. This is close to the MyISAM\
  behavior, but is not really the best.
* autocommit = 0: COMMIT will close a transaction and start another one. To me,\
  this is kludgy.
* (recommended) BEGIN...COMMIT gives you control over what sequence of\
  operation(s) are to be considered a transaction and "atomic". Include the\
  ROLLBACK statement if you need to undo stuff back to the BEGIN.

Perl's DBIx::DWIW and Java's JDBC have API calls to do BEGIN and COMMIT. These\
are probably better than 'executing' BEGIN and COMMIT.

Test for errors everywhere! Because InnoDB uses row-level locking, it can\
stumble into deadlocks that you are not expecting. The engine will\
automatically ROLLBACK to the BEGIN. The normal recovery is to redo, beginning\
at the BEGIN. Note that this is a strong reason to have BEGINs.

LOCK/UNLOCK TABLES — remove them. Replace them (sort\
of) with BEGIN ... COMMIT. (LOCK will work if [innodb\_table\_locks](innodb/innodb-system-variables.md) is set to 1, but it is less efficient, and\
may have subtle issues.)

In 5.1, ALTER ONLINE TABLE can speed up some operations significantly.\
(Normally ALTER TABLE copies the table over and rebuilds the indexes.)

The "limits" on virtually everything are different between MyISAM and InnoDB.\
Unless you have huge tables, wide rows, lots of indexes, etc, you are unlikely\
to stumble into a different limit.

Mixture of MyISAM and InnoDB? This is OK. But there are caveats.

* RAM settings should be adjusted to accordingly.
* JOINing tables of different Engines works.
* A transaction that affects tables of both types can ROLLBACK InnoDB changes,\
  but will leave MyISAM changes intact.
* Replication: MyISAM statements are replicated when finished; InnoDB\
  statements are held until the COMMIT.

FIXED (vs DYNAMIC) is meaningless in InnoDB.

PARTITION — You can partition MyISAM and InnoDB\
tables. Remember the screwball rule: You must either

* have no UNIQUE (or PRIMARY) keys, or
* have the value you are "partitioning on" in every UNIQUE key.

The former is not advised for InnoDB. The latter is messy if you want an\
AUTO\_INCREMENT.

PRIMARY KEY in PARTITION — Since every key must\
include the field on which you are PARTITIONing, how can AUTO\_INCREMENT work?\
Well, there seems to be a convenient special case:

* This works: PRIMARY KEY(autoinc, partition\_key)
* This does not work for InnoDB: PRIMARY KEY(partition\_key, autoinc)

That is, an AUTO\_INCREMENT will correctly increment, and be unique across all\
PARTITINOs, when it is the first field of the PRIMARY KEY, but not otherwise.

## See Also

Rick James graciously allowed us to use this article in the documentation.

[Rick James' site](https://mysql.rjweb.org/) has other useful tips, how-tos,\
optimizations, and debugging tips.

Original source: [myisam2innodb](https://mysql.rjweb.org/doc.php/myisam2innodb)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
