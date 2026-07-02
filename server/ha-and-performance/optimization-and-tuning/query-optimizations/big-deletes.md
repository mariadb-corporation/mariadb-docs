---
description: >-
  Techniques for deleting large numbers of rows from big tables efficiently.
---

# Big DELETEs

## The problem

How to [DELETE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) lots of rows from a large table? Here is an example of purging items older than 30 days:

```sql
DELETE FROM tbl WHERE 
  ts < CURRENT_DATE() - INTERVAL 30 DAY
```

If there are millions of rows in the table, this statement may take minutes, maybe hours.

Any suggestions on how to speed this up?

## Why it is a problem

* [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/) will lock the table during the entire operation, thereby nothing else can be done with the table.
* [InnoDB](../../../server-usage/storage-engines/innodb/) won't lock the table, but it will chew up a lot of resources, leading to sluggishness.
* InnoDB has to write the undo information to its transaction logs; this significantly increases the I/O required.
* [Replication](../../standard-replication/replication-overview.md), being asynchronous, will effectively be delayed (on Slaves) while the DELETE is running.

## InnoDB and undo

To be ready for a crash, a transactional engine such as InnoDB will record what it is doing to a log file. To make that somewhat less costly, the log file is sequentially written. If the log files you have (there are usually 2) fill up because the delete is really big, then the undo information spills into the actual data blocks, leading to even more I/O.

Deleting in chunks avoids some of this excess overhead.

Limited benchmarking of total delete elapsed time show two observations:

* Total delete time approximately doubles above some 'chunk' size (as opposed to below that threshold). I do not have a formula relating the log file size with the threshold cutoff.
* Chunk size below several hundred rows is slower. This is probably because the overhead of starting/ending each chunk dominates the timing.

Solutions

* PARTITION -- Requires some careful setup, but is excellent for purging a time-base series.
* DELETE in chunks -- Carefully walk through the table N rows at a time.

## PARTITION

The idea here is to have a sliding window of [partitions](../../../server-usage/partitioning-tables/). Let's say you need to purge news articles after 30 days. The "partition key" would be the [datetime](../../../reference/data-types/date-and-time-data-types/datetime.md) (or [timestamp](../../../reference/data-types/date-and-time-data-types/timestamp.md)) that is to be used for purging, and the PARTITIONs would be "range". Every night, a cron job would come along and build a new partition for the next day, and drop the oldest partition.

Dropping a partition is essentially instantaneous, much faster than deleting that many rows. However, you must design the table so that the entire partition can be dropped. That is, you cannot have some items living longer than others.

PARTITION tables have a lot of restrictions, some are rather weird. You can either have no UNIQUE (or PRIMARY) key on the table, or every UNIQUE key must include the partition key. In this use case, the partition key is the datetime. It should not be the first part of the PRIMARY KEY (if you have a PRIMARY KEY).

You can PARTITION InnoDB or MyISAM tables.

Since two news articles could have the same timestamp, you cannot assume the partition key is sufficient for uniqueness of the PRIMARY KEY, so you need to find something else to help with that.

Reference implementation for Partition maintenance

[MariaDB docs on PARTITION](../../../server-usage/partitioning-tables/)

## Deleting in chunks

Although the discussion in this section talks about DELETE, it can be used for any other "chunking", such as, say, UPDATE, or SELECT plus some complex processing.

(This discussion applies to both MyISAM and InnoDB.)

When deleting in chunks, be sure to avoid doing a table scan. The code below is good at that; it scans no more than 1001 rows in any one query. (The 1000 is tunable.)

Assuming you have news articles that need to be purged, and you have a schema something like

```sql
CREATE TABLE tbl
      id INT UNSIGNED NOT NULL AUTO_INCREMENT,
      ts TIMESTAMP,
      ...
      PRIMARY KEY(id)
```

Then, this pseudo-code is a good way to delete the rows older than 30 days:

```sql
@a = 0
   LOOP
      DELETE FROM tbl
         WHERE id BETWEEN @a AND @a+999
           AND ts < DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
      SET @a = @a + 1000
      sleep 1  -- be a nice guy
   UNTIL end of table
```

Notes (Most of these caveats will be covered later):

* It uses the PK instead of the secondary key. This gives much better locality of disk hits, especially for InnoDB.
* You could (should?) do something to avoid walking through recent days but doing nothing. Caution -- the code for this could be costly.
* The 1000 should be tweaked so that the DELETE usually takes under, say, one second.
* No INDEX on ts is needed. (This helps INSERTs a little.)
* If your PRIMARY KEY is compound, the code gets messier.
* This code will not work without a numeric PRIMARY or UNIQUE key.
* Read on, we'll develop messier code to deal with most of these caveats.

If there are big gaps in `id` values (and there will after the first purge), then

```sql
@a = SELECT MIN(id) FROM tbl
   LOOP
      SELECT @z := id FROM tbl WHERE id >= @a ORDER BY id LIMIT 1000,1
      IF @z IS NULL
         EXIT LOOP  -- last chunk
      DELETE FROM tbl
         WHERE id >= @a
           AND id <  @z
           AND ts < DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
      SET @a = @z
      sleep 1  -- be a nice guy, especially in replication
   ENDLOOP
   # Last chunk:
   DELETE FROM tbl
      WHERE id >= @a
        AND ts < DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
```

That code works whether id is numeric or character, and it mostly works even if id is not UNIQUE. With a non-unique key, the risk is that you could be caught in a loop whenever @z==@a. That can be detected and fixed thus:

```sql
...
      SELECT @z := id FROM tbl WHERE id >= @a ORDER BY id LIMIT 1000,1
      IF @z == @a
         SELECT @z := id FROM tbl WHERE id > @a ORDER BY id LIMIT 1
   ...
```

The drawback is that there could be more than 1000 items with a single id. In most practical cases, that is unlikely.

If you do not have a primary (or unique) key defined on the table, and you have an INDEX on ts, then consider

```sql
LOOP
      DELETE FROM tbl
         WHERE ts < DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
         ORDER BY ts   -- to use the index, and to make it deterministic
         LIMIT 1000
   UNTIL no rows deleted
```

This technique is NOT recommended because the LIMIT leads to a warning on replication about it being non-deterministic (discussed below).

## InnoDB chunking recommendation

* Have a 'reasonable' size for [innodb\_log\_file\_size](../../../server-usage/storage-engines/innodb/innodb-system-variables.md).
* Use AUTOCOMMIT=1 for the session doing the deletions.
* Pick about 1000 rows for the chunk size.
* Adjust the row count down if asynchronous replication (Statement Based) causes too much delay on the Slaves or hogs the table too much.

## Iterating through a compound key

To perform the chunked deletes recommended above, you need a way to walk through the PRIMARY KEY. This can be difficult if the PK has more than one column in it.

To efficiently to do compound 'greater than':

Assume that you left off at ($g, $s) (and have handled that row):

```sql
INDEX(Genus, species)
   SELECT/DELETE ...
      WHERE Genus >= '$g' AND ( species  > '$s' OR Genus > '$g' )
      ORDER BY Genus, species
      LIMIT ...
```

Addenda: The above AND/OR works well in older versions of MySQL; this works better in MariaDB and newer versions of MySQL:

```sql
WHERE ( Genus = '$g' AND species  > '$s' ) OR Genus > '$g' )
```

A caution about using @variables for strings. If, instead of '$g', you use @g, you need to be careful to make sure that @g has the same CHARACTER SET and COLLATION as `Genus`, else there could be a charset/collation conversion on the fly that prevents the use of the INDEX. Using the INDEX is vital for performance. It may require a COLLATE clause on SET NAMES and/or the @g in the SELECT.

## Reclaiming the disk space

This is costly. (Switch to the PARTITION solution if practical.)

MyISAM leaves gaps in the table (.MYD file); [OPTIMIZE TABLE](../optimizing-tables/optimize-table.md) will reclaim the freed space after a big delete. But it may take a long time and lock the table.

InnoDB is block-structured, organized in a BTree on the PRIMARY KEY. An isolated deleted row leaves a block less full. A lot of deleted rows can lead to coalescing of adjacent blocks. (Blocks are normally 16KB - see [innodb\_page\_size](../../../server-usage/storage-engines/innodb/innodb-system-variables.md).)

In InnoDB, there is no practical way to reclaim the freed space from ibdata1, other than to reuse the freed blocks eventually.

The only option with [innodb\_file\_per\_table = 0](../../../server-usage/storage-engines/innodb/innodb-system-variables.md) is to dump ALL tables, remove ibdata\*, restart, and reload. That is rarely worth the effort and time.

InnoDB, even with innodb\_file\_per\_table = 1, won't give space back to the OS, but at least it is only one table to rebuild with. In this case, something like this should work:

```sql
CREATE TABLE new LIKE main;
   INSERT INTO new SELECT * FROM main;  -- This could take a long time
   RENAME TABLE main TO old, new TO main;   -- Atomic swap
   DROP TABLE old;   -- Space freed up here
```

You do need enough disk space for both copies. You must not write to the table during the process.

## Deleting more than half a table

The following technique can be used for any combination of

* Deleting a large portion of the table more efficiently
* Add PARTITIONing
* Converting to [innodb\_file\_per\_table = ON](../../../server-usage/storage-engines/innodb/innodb-system-variables.md)
* Defragmenting

This can be done by chunking, or (if practical) all at once:

```sql
-- Optional:  SET GLOBAL innodb_file_per_table = ON;
   CREATE TABLE New LIKE Main;
   -- Optional:  ALTER TABLE New ADD PARTITION BY RANGE ...;
   -- Do this INSERT..SELECT all at once, or with chunking:
   INSERT INTO New
      SELECT * FROM Main
         WHERE ...;  -- just the rows you want to keep
   RENAME TABLE main TO Old, New TO Main;
   DROP TABLE Old;   -- Space freed up here
```

Notes:

* You do need enough disk space for both copies.
* You must not write to the table during the process. (Changes to Main may not be reflected in New.)

## Non-deterministic replication

Any UPDATE, DELETE, etc with LIMIT that is replicated to slaves (via [Statement Based Replication](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md)) _may_ cause inconsistencies between the Master and Slaves. This is because the actual order of the records discovered for updating/deleting may be different on the slave, thereby leading to a different subset being modified. To be safe, add ORDER BY to such statements. Moreover, be sure the ORDER BY is deterministic -- that is, the fields/expressions in the ORDER BY are unique.

An example of an ORDER BY that does not quite work: Assume there are multiple rows for each 'date':

```sql
DELETE * FROM tbl ORDER BY date LIMIT 111
```

Given that id is the PRIMARY KEY (or UNIQUE), this will be safe:

```sql
DELETE * FROM tbl ORDER BY date, id LIMIT 111
```

Unfortunately, even with the ORDER BY, MySQL has a deficiency that leads to a bogus warning in mysqld.err. See Spurious "Statement is not safe to log in statement format." warnings

Some of the above code avoids this spurious warning by doing

```sql
SELECT @z := ... LIMIT 1000,1;  -- not replicated
   DELETE ... BETWEEN @a AND @z;   -- deterministic
```

That pair of statements guarantees no more than 1000 rows are touched, not the whole table.

## Replication and KILL

If you KILL a DELETE (or any? query) on the master in the middle of its execution, what will be replicated?

If it is InnoDB, the query should be rolled back. (Exceptions??)

In MyISAM, rows are DELETEd as the statement is executed, and there is no provision for ROLLBACK. Some of the rows will be deleted, some won't. You probably have no clue of how much was deleted. In a single server, simply run the delete again. The delete is put into the binlog, but with error 1317. Since replication is supposed to keep the master and slave in sync, and since it has no clue of how to do that, replication stops and waits for manual intervention. In a HA (High Available) system using replication, this is a minor disaster. Meanwhile, you need to go to each slave(s) and verify that it is stuck for this reason, then do

```sql
SET GLOBAL SQL_SLAVE_SKIP_COUNTER = 1;
   START SLAVE;
```

Then (presumably) re-executing the DELETE will finish the aborted task.

(That is yet another reason to move all your tables [from MyISAM to InnoDB](../../../server-usage/storage-engines/converting-tables-from-myisam-to-innodb.md).)

## SBR vs RBR; Galera

TBD -- "Row Based Replication" may impact this discussion.

## Postlog

The tips in this document apply to MySQL, MariaDB, and Percona.

## See also

Rick James graciously allowed us to use this article in the documentation.

[Rick James' site](https://mysql.rjweb.org/) has other useful tips, how-tos,\
optimizations, and debugging tips.

Original source: [deletebig](https://mysql.rjweb.org/doc.php/deletebig)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
