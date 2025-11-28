# Partition Maintenance

## Overview

This article covers:

* Partitioning best practices.
* How to maintain a time-series-partitioned table.
* `AUTO_INCREMENT` secrets.

General partitioning advice, taken from [Rick's RoTs - Rules of Thumb](https://mysql.rjweb.org/doc.php/ricksrots):

1. Don't use [PARTITIONing](./) until you know how and why it will help.
2. Don't use PARTITION unless you will have more than a million rows to handle.
3. No more than 50 PARTITIONs on a table (open, show table status, etc, are impacted).
4. `PARTITION BY RANGE` is the only useful method.

* Subpartitions are not useful.
* The partition field should not be the first field in any key.
* It is okay to have an [AUTO\_INCREMENT](../../reference/data-types/auto_increment.md) as the first part of a compound key, or in a nonunique index.

It is so tempting to believe that PARTITIONing will solve performance problems. But it is so often wrong.

PARTITIONing splits up one table into several smaller tables. But table size is rarely a performance issue. Instead, I/O time and indexes are the issues.

A common fallacy: "Partitioning will make my queries run faster". It won't. Ponder what it takes for a 'point query'. Without partitioning, but with an appropriate index, there is a BTree (the index) to drill down to find the desired row. For a billion rows, this might be 5 levels deep. With partitioning, first the partition is chosen and "opened", then a smaller BTree (of say 4 levels) is drilled down. Well, the savings of the shallower BTree is consumed by having to open the partition. Similarly, if you look at the disk blocks that need to be touched, and which of those are likely to be cached, you come to the conclusion that about the same number of disk hits is likely. Since disk hits are the main cost in a query, Partitioning does not gain any performance (at least for this typical case). The 2D case (below) gives the main contradiction to this discussion.

## Use Cases for PARTITIONing

**Use case #1 -- time series**. Perhaps the most common use case where PARTITIONing shines is in a dataset where "old" data is periodically deleted from the table. RANGE PARTITIONing by day (or other unit of time) lets you do a nearly instantaneous DROP PARTITION plus REORGANIZE PARTITION instead of a much slower DELETE. Much of this blog is focused on this use case. This use case is also discussed in [Big DELETEs](../../ha-and-performance/optimization-and-tuning/query-optimizations/big-deletes.md)

The big win for Case #1: DROP PARTITION is a lot faster than DELETEing a lot of rows.

**Use case #2 -- 2-D index**. INDEXes are inherently one-dimensional. If you need two "ranges" in the WHERE clause, try to migrate one of them to PARTITIONing.

Finding the nearest 10 pizza parlors on a map needs a 2D index. Partition pruning sort of gives a second dimension. See Latitude/Longitude Indexing\
That uses PARTITION BY RANGE(latitude) together with PRIMARY KEY(longitude, ...)

The big win for Case #2: Scanning fewer rows.

**Use case #3 -- hot spot**. This is a bit complicated to explain. Given this combination:

* A table's index is too big to be cached, but the index for one partition is cacheable, and
* The index is randomly accessed, and
* Data ingestion would normally be I/O bound due to updating the index\
  Partitioning can keep all the index "hot" in RAM, thereby avoiding a lot of I/O.

The big win for Case #3: Improving caching to decrease I/O to speed up operations.

## AUTO\_INCREMENT in PARTITION

* For [AUTO\_INCREMENT](../../reference/data-types/auto_increment.md) to work (in any table), it must be the first field in some index. Period. There are no other requirements on indexing it.
* Being the first field in some index lets the engine find the 'next' value when opening the table.
* AUTO\_INCREMENT need not be UNIQUE. What you lose: prevention of explicitly inserting a duplicate id. (This is rarely needed, anyway.)

Examples (where id is AUTO\_INCREMENT):

* PRIMARY KEY (...), INDEX(id)
* PRIMARY KEY (...), UNIQUE(id, partition\_key) -- not useful
* INDEX(id), INDEX(...) (but no UNIQUE keys)
* PRIMARY KEY(id), ... -- works only if id is the partition key (not very useful)

## PARTITION Maintenance for the Time-Series Case

Let's focus on the maintenance task involved in Case #1, as described above.

You have a large table that is growing on one end and being pruned on the other. Examples include news, logs, and other transient information. PARTITION BY RANGE is an excellent vehicle for such a table.

* DROP PARTITION is much faster than DELETE. (This is the big reason for doing this flavor of partitioning.)
* Queries often limit themselves to 'recent' data, thereby taking advantage of "partition pruning".

Depending on the type of data, and how long before it expires, you might have daily or weekly or hourly (etc) partitions.

There is no simple SQL statement to "drop partitions older than 30 days" or "add a new partition for tomorrow". It would be tedious to do this by hand every day.

## High-Level View of the Code

```sql
ALTER TABLE tbl
    DROP PARTITION from20120314;
ALTER TABLE tbl
    REORGANIZE PARTITION future INTO (
        PARTITION from20120415 VALUES LESS THAN (TO_DAYS('2012-04-16')),
        PARTITION future     VALUES LESS THAN MAXVALUE);
```

After which you have...

```sql
CREATE TABLE tbl (
        dt DATETIME NOT NULL,  -- or DATE
        ...
        PRIMARY KEY (..., dt),
        UNIQUE KEY (..., dt),
        ...
    )
    PARTITION BY RANGE (TO_DAYS(dt)) (
        PARTITION START        VALUES LESS THAN (0),
        PARTITION from20120315 VALUES LESS THAN (TO_DAYS('2012-03-16')),
        PARTITION from20120316 VALUES LESS THAN (TO_DAYS('2012-03-17')),
        ...
        PARTITION from20120414 VALUES LESS THAN (TO_DAYS('2012-04-15')),
        PARTITION from20120415 VALUES LESS THAN (TO_DAYS('2012-04-16')),
        PARTITION future       VALUES LESS THAN MAXVALUE
    );
```

## Why?

Perhaps you noticed some odd things in the example. Let me explain them.

* Partition naming: Make them useful.
* from20120415 ... 04-16: Note that the LESS THAN is the next day's date
* The "start" partition: See paragraph below.
* The "future" partition: This is normally empty, but it can catch overflows; more later.
* The range key (dt) must be included in any PRIMARY or UNIQUE key.
* The range key (dt) should be last in any keys it is in -- You have already "pruned" with it; it is almost useless in the index, especially at the beginning.
* DATETIME, etc -- I picked this datatype because it is typical for a time series. Newer MySQL versions allow TIMESTAMP. INT could be used; etc.
* There is an extra day (03-16 thru 04-16): The latest day is only partially full.

Why the bogus "start" partition? If an invalid datetime (Feb 31) were to be used, the datetime would turn into NULL. NULLs are put into the first partition. Since any SELECT could have an invalid date (yeah, this stretching things), the partition pruner always includes the first partition in the resulting set of partitions to search. So, if the SELECT must scan the first partition, it would be slightly more efficient if that partition were empty. Hence the bogus "start" partition. Longer discussion, by The Data Charmer\
5.5 eliminates the bogus check, but only if you switch to a new syntax:

```sql
PARTITION BY RANGE COLUMNS(dt) (
    PARTITION day_20100226 VALUES LESS THAN ('2010-02-27'), ...
```

More on the "future" partition. Sooner or later the cron/EVENT to add tomorrow's partition will fail to run. The worst that could happen is for tomorrow's data to be lost. The easiest way to prevent that is to have a partition ready to catch it, even if this partition is normally always empty.

Having the "future" partition makes the ADD PARTITION script a little more complex. Instead, it needs to take tomorrow's data from "future" and put it into a new partition. This is done with the REORGANIZE command shown. Normally nothing need be moved, and the ALTER takes virtually zero time.

## When to do the ALTERs?

* DROP if the oldest partition is "too old".
* Add 'tomorrow' near the end of today, but don't try to add it twice.
* Do not count partitions -- there are two extra ones. Use the partition names or information\_schema.PARTITIONS.PARTITION\_DESCRIPTION.
* DROP/Add only once in the script. Rerun the script if you need more.
* Run the script more often than necessary. For daily partitions, run the script twice a day, or even hourly. Why? Automatic repair.

## Variants

As I have said many times, in many places, BY RANGE is perhaps the only useful variant. And a time series is the most common use for PARTITIONing.

* (as discussed here) DATETIME/DATE with TO\_DAYS()
* DATETIME/DATE with TO\_DAYS(), but with 7-day intervals
* TIMESTAMP with TO\_DAYS(). (version 5.1.43 or later)
* PARTITION BY RANGE COLUMNS(DATETIME) (5.5.0)
* PARTITION BY RANGE(TIMESTAMP) (version 5.5.15 / 5.6.3)
* PARTITION BY RANGE(TO\_SECONDS()) (5.6.0)
* INT UNSIGNED with constants computed as unix timestamps.
* INT UNSIGNED with constants for some non-time-based series.
* MEDIUMINT UNSIGNED containing an "hour id": FLOOR(FROM\_UNIXTIME(timestamp) / 3600)
* Months, Quarters, etc: Concoct a notation that works.

How many partitions?

* Under, say, 5 partitions -- you get very little of the benefits.
* Over, say, 50 partitions, and you hit inefficiencies elsewhere.
* Certain operations (SHOW TABLE STATUS, opening the table, etc) open every partition.
* [MyISAM](../storage-engines/myisam-storage-engine/), before version 5.6.6, would lock all partitions before pruning!
* Partition pruning does not happen on INSERTs (until Version 5.6.7), so INSERT needs to open all the partitions.
* A possible 2-partition use case: [read.php?24,633179,633179](https://forums.mysql.com/read.php?24,633179,633179)
* 8192 partitions is a hard limit (1024 before [MariaDB 10.0.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1004-release-notes)).
* Before "native partitions" (5.7.6), each partition consumed a chunk of memory.

## Detailed Code

[Reference implementation, in Perl, with demo of daily partitions](https://mysql.rjweb.org/demo_part_maint.pl.txt)

The complexity of the code is in the discovery of the PARTITION names, especially of the oldest and the 'next'.

To run the demo,

* Install Perl and DBIx::DWIW (from CPAN).
* copy the txt file (link above) to demo\_part\_maint.pl
* execute perl demo\_part\_maint.pl to get the rest of the instructions

The program will generate and execute (when needed) either of these:

```sql
ALTER TABLE tbl REORGANIZE PARTITION
        future
   INTO (
        PARTITION from20150606 VALUES LESS THAN (736121),
        PARTITION future VALUES LESS THAN MAXVALUE
   )

   ALTER TABLE tbl
                    DROP PARTITION from20150603
```

## Postlog

[Slides from Percona Amsterdam 2015](https://mysql.rjweb.org/slides/Partition.pdf)

The tips in this document apply to MySQL, MariaDB, and Percona.

* [More on PARTITIONing](https://www.mysqlperformanceblog.com/2010/12/11/mysql-partitioning-can-save-you-or-kill-you/)
* [LinkedIn discussion](https://www.linkedin.com/groups/MySql-Horizontal-partitioning-ProsCons-78638.S.5861525157444595715?qid=0d54d3f9-21d7-43e8-9b75-dbc0270c7236\&trk=groups_guest_most_popular-0-b-ttl\&goback=%2Egmp_78638)
* [Why NOT Partition](https://dba.stackexchange.com/questions/107408/why-not-partition)
* [Geoff Montee's Stored Proc](https://www.geoffmontee.com/automatically-dropping-old-partitions-in-mysql-and-mariadb-part-2/)

Future (as envisioned in 2016):

* MySQL 5.7.6 has "native partitioning for InnoDB".
* FOREIGN KEY support, perhaps in a later 8.0.xx.
* "GLOBAL INDEX" -- this would avoid the need for putting the partition key in every unique index, but make DROP PARTITION costly. This is farther into the future.

MySQL 8.0, released Sep, 2016, not yet GA)

* Only InnoDB tables can be partitioned -- MariaDB is likely to continue maintaining Partitioning on non-InnoDB tables, but Oracle is clearly not.
* Some of the problems having lots of partitions are lessened by the Data-Dictionary-in-a-table.

Native partitioning will give:

* This will improve performance slightly by combining two "handlers" into one.
* Decreased memory usage, especially when using a large number of partitions.

## See Also

Rick James graciously allowed us to use this article in the documentation. [Rick James' site](https://mysql.rjweb.org/) has other useful tips, how-tos, optimizations, and debugging tips. Original source: [partitionmaint](https://mysql.rjweb.org/doc.php/partitionmaint)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
