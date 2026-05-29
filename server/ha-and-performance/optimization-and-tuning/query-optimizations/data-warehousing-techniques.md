# Data Warehousing Techniques

## Preface

This document discusses techniques for improving performance for data-warehouse-like tables in MariaDB and MySQL.

* How to load large tables.
* [Normalization](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/database-theory/database-normalization).
* Developing 'summary tables' to make 'reports' efficient.
* Purging old data.

Details on summary tables is covered in the companion document: [Summary Tables](data-warehousing-summary-tables.md).

## Terminology

This list mirrors "Data Warehouse" terminology.

* Fact table -- The one huge table with the 'raw' data.
* Summary table -- a redundant table of summarized data that could -- use for efficiency
* Dimension -- columns that identify aspects of the dataset (region, country, user, SKU, zipcode, ...)
* Normalization table (dimension table) -- mapping between strings an ids; used for space and speed.
* Normalization -- The process of building the mapping ('New York City' <-> 123)

## Fact table

Techniques that should be applied to the huge Fact table.

* id INT/BIGINT UNSIGNED NOT NULL AUTO\_INCREMENT
* PRIMARY KEY (id)
* Probably no other INDEXes
* Accessed only via id
* All VARCHARs are "normalized"; ids are stored instead
* ENGINE = InnoDB
* All "reports" use summary tables, not the Fact table
* Summary tables may be populated from ranges of id (other techniques described below)

There are exceptions where the Fact table must be accessed to retrieve multiple rows. However, you should minimize the number of INDEXes on the table because they are likely to be costly on INSERT.

## Why keep the Fact table?

Once you have built the Summary table(s), there is not much need for the Fact table. One option that you should seriously consider is to not have a Fact table. Or, at least, you could purge old data from it sooner than you purge the Summary tables. Maybe even keep the Summary tables forever.

Case 1: You need to find the raw data involved in some event. But how will you find those row(s)? This is where a secondary index may be required.

If a secondary index is bigger than can be cached in RAM, and if the column(s) being indexed is random, then each row inserted may cause a disk hit to update the index. This limits insert speed to something like 100 rows per second (on ordinary disks). Multiple random indexes slow down insertion further. RAID striping and/or SSDs speed up insertion. Write caching helps, but only for bursts.

Case 2: You need some event, but you did not plan ahead with the optimal INDEX. Well, if the data is PARTITIONed on date, so even if you have a clue of when the event occurred, "partition pruning" will keep the query from being too terribly slow.

Case 3: Over time, the application is likely to need new 'reports', which may lead to a new Summary table. At this point, it would be handy to scan through the old data to fill up the new table.

Case 4: You find a flaw in the summarization, and need to rebuild an existing Summary table.

Cases 3 and 4 both need the "raw" data. But they don't necessarily need the data sitting in a database table. It could be in the pre-database format (such as log files). So, consider not building the Fact table, but simply keep the raw data, compressed, on some file system.

## Batching the load of the Fact table

When talking about billions of rows in the Fact table, it is essentially mandatory that you "batch" the inserts. There are two main ways:

* INSERT INTO Fact (.,.,.) VALUES (.,.,.), (.,.,.), ...; -- "Batch insert"
* LOAD DATA ...;

A third way is to INSERT or LOAD into a Staging table, then

* INSERT INTO Fact SELECT \* FROM Staging;\
  This INSERT..SELECT allows you to do other things, such as normalization. More later.

## Batched INSERT Statement

Chunk size should usually be 100-1000 rows.

* 100-1000 an insert will run 10 times as fast as single-row inserts.
* Beyond 100, you may be interfering replication and SELECTs.
* Beyond 1000, you are into diminishing returns -- virtually no further performance gains.
* Don't go past, say, 1MB for the constructed INSERT statement. This deals with packet sizes, etc. (1MB is unlikely to be hit for a Fact table.)\
  Decide whether your application should lean toward the 100 or the 1000.

If your data is coming in continually, and you are adding a batching layer, let's do some math. Compute your ingestion rate -- R rows per second.

* If R < 10 (= 1M/day = 300M/year) -- single-row INSERTs would probably work fine (that is, batching is optional)
* If R < 100 (3B records per year) -- secondary indexes on Fact table may be ok
* If R < 1000 (100M records/day) -- avoid secondary indexes on Fact table.
* If R > 1000 -- Batching may not work.\
  Decide how long (S seconds) you can stall loading the data in order to collect a batch of rows.
* If S < 0.1s -- May not be able to keep up

If batching seems viable, then design the batching layer to gather for S seconds or 100-1000 rows, whichever comes first.

(Note: Similar math applies to rapid UPDATEs of a table.)

## Normalization (Dimension) table

Normalization is important in Data Warehouse applications because it significantly cuts down on the disk footprint and improves performance. There are other reasons for normalizing, but space is the important one for DW.

Here is a typical pattern for a Dimension table:

```sql
CREATE TABLE Emails (
        email_id MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,  -- don't make bigger than needed
        email VARCHAR(...) NOT NULL,
        PRIMARY KEY (email),  -- for looking up one way
        INDEX(email_id)  -- for looking up the other way (UNIQUE is not needed)
    ) ENGINE = InnoDB;  -- to get clustering
```

Notes:

* MEDIUMINT is 3 bytes with UNSIGNED range of 0..16M; pick SMALLINT, INT, etc, based on a conservative estimate of how many 'foo's you will eventually have.
* datatype sizes
* There may be more than one VARCHAR in the table. Example: For cities, you might have City and Country.
* InnoDB is better than MyISAM because of way the two keys are structured.
* The secondary key is effectively (email\_id, email), hence 'covering' for certain queries.
* It is OK to not specify an AUTO\_INCREMENT to be UNIQUE.

## Batched normalization

I bring this up as a separate topic because of some of the subtle issues that can happen.

You may be tempted to do

```sql
INSERT IGNORE INTO Foos
        SELECT DISTINCT foo FROM Staging;  -- not wise
```

It has the problem of "burning" AUTO\_INCREMENT ids. This is because MariaDB pre-allocates ids before getting to "IGNORE". That could rapidly increase the AUTO\_INCREMENT values beyond what you expected.

Better is this...

```sql
INSERT IGNORE INTO Foos
        SELECT DISTINCT foo
            FROM Staging
            LEFT JOIN Foos ON Foos.foo = Staging.foo
            WHERE Foos.foo_id IS NULL;
```

Notes:

* The LEFT JOIN .. IS NULL finds the `foo`s that are not yet in Foos.
* This INSERT..SELECT must not be done inside the transaction with the rest of the processing. Otherwise, you add to deadlock risks, leading to burned ids.
* IGNORE is used in case you are doing the INSERT from multiple processes simultaneously.

Once that INSERT is done, this will find all the foo\_ids it needs:

```sql
INSERT INTO Fact (..., foo_id, ...)
        SELECT ..., Foos.foo_id, ...
            FROM Staging
            JOIN Foos ON Foos.foo = Staging.foo;
```

An advantage of "Batched Normalization" is that you can summarize directly from the Staging table. Two approaches:

Case 1: PRIMARY KEY (dy, foo) and summarization is in lock step with, say, changes in `dy`.

* This approach can have troubles if new data arrives after you have summarized the day's data.

```sql
INSERT INTO Summary (dy, foo, ct, blah_total)
        SELECT  DATE(dt) AS dy, foo,
                COUNT(*) AS ct, SUM(blah) AS blah_total)
            FROM Staging
            GROUP BY 1, 2;
```

Case 2: (dy, foo) is a non-UNIQUE INDEX.

* Same code as Case 1.
* By having the index be non-UNIQUE, delayed data simply shows up as extra rows.
* You need to take care to avoid summarizing the data twice. (The id on the Fact table may be a good tool for that.)

Case 3: PRIMARY KEY (dy, foo) and summarization can happen anytime.

```sql
INSERT INTO Summary (dy, foo, ct, blah_total)
        ON DUPLICATE KEY UPDATE
            ct = ct + VALUE(ct),
            blah_total = blah_total + VALUE(bt)
        SELECT  DATE(dt) AS dy, foo,
                COUNT(*) AS ct, SUM(blah) AS bt)
            FROM Staging
            GROUP BY 1, 2;
```

## Too many choices?

This document lists a number of ways to do things. Your situation may lead to one approach being more/less acceptable. But, if you are thinking "Just tell me what to do!", then here:

* Batch load the raw data into a temporary table (`Staging`).
* Normalize from `Staging` -- use code in Case 3.
* INSERT .. SELECT to move the data from `Staging` into the Fact table
* Summarize from `Staging` to Summary table(s) via IODKU (Insert ... On Duplicate Key Update).
* Drop the Staging

Those techniques should perform well and scale well in most cases. As you develop your situation, you may discover why I described alternative solutions.

## Purging old data

Typically the Fact table is PARTITION BY RANGE (10-60 ranges of days/weeks/etc) and needs purging (DROP PARTITION) periodically. This discusses a safe/clean way to design the partitioning and do the DROPs: Purging PARTITIONs

## Master / slave

For "read scaling", backup, and failover, use master-slave replication or something fancier. Do ingestion only on a single active master; it replicate to the slave(s). Generate reports on the slave(s).

## Sharding

"Sharding" is the splitting of data across multiple servers. (In contrast, [replication](../../standard-replication/replication-overview.md) and [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) have the same data on all servers, requiring all data to be written to all servers.)

With the non-sharding techniques described here, terabyte(s) of data can be handled by a single machine. Tens of terabytes probably requires sharding.

Sharding is beyond the scope of this document.

## How fast? How big?

With the techniques described here, you may be able to achieve the following performance numbers. I say "may" because every data warehouse situation is different, and you may require performance-hurting deviations from what I describe here. I give multiple options for some aspects; these may cover some of your deviations.

One big performance killer is UUID/GUID keys. Since they are very 'random', updates of them (at scale) are limited to 1 row = 1 disk hit. Plain disks can handle only 100 hits/second. RAID and/or SSD can increase that to something like 1000 hits/sec. Huge amounts of RAM (for caching the random index) are a costly solution. It is possible to turn type-1 UUIDs into roughly-chronological keys, thereby mittigating the performance problems if the UUIDs are written/read with some chronological clustering. UUID discussion

Hardware, etc:

* Single SATA drive: 100 IOPs (Input/Output operations per second)
* RAID with N physical drives -- 100\*N IOPs (roughly)
* SSD -- 5 times as fast as rotating media (in this context)
* Batch INSERT -- 100-1000 rows is 10 times as fast as INSERTing 1 row at a time (see above)
* Purge "old" data -- Do not use DELETE or TRUNCATE, design so you can use DROP PARTITION (see above)
* Think of each INDEX (except the PRIMARY KEY on InnoDB) as a separate table
* Consider access patterns of each table/index: random vs at-the-end vs something in between

"Count the disk hits" -- back-of-envelope performance analysis

* Random accesses to a table/index -- count each as a disk hit.
* At-the-end accesses (INSERT chronologically or with AUTO\_INCREMENT; range SELECT) -- count as zero hits.
* In between (hot/popular ids, etc) -- count as something in between
* For INSERTs, do the analysis on each index; add them up.
* For SELECTs, do the analysis on the one index used, plus the table. (Use of 2 indexes is rare.)\
  Insert cost, based on datatype of first column in an index:
* AUTO\_INCREMENT -- essentially 0 IOPs
* DATETIME, TIMESTAMP -- essentially 0 for 'current' times
* UUID/GUID -- 1 per insert (terrible)
* Others -- depends on their patterns\
  SELECT cost gets a little tricky:
* Range on PRIMARY KEY -- think of it as getting 100 rows per disk hit.
* IN on PRIMARY KEY -- 1 disk hit per item in IN
* "=" -- 1 hit (for 1 row)
* Secondary key -- First compute the hits for the index, then...
* Think of each row as needing 1 disk hit.
* However, if the rows are likely to be 'near' each other (based on the PRIMARY KEY), then it could be < 1 disk hit/row.

More on Count the Disk Hits

## How fast?

Look at your data; compute raw rows per second (or hour or day or year). There are about 30M seconds in a year; 86,400 seconds per day. Inserting 30 rows per second becomes a billion rows per year.

10 rows per second is about all you can expect from an ordinary machine (after allowing for various overheads). If you have less than that, you don't have many worries, but still you should probably create Summary tables. If more than 10/sec, then batching, etc, becomes vital. Even on spiffy hardware, 100/sec is about all you can expect without utilizing the techniques here.

## Not so fast?

Let's say your insert rate is only one-tenth of your disk IOPs (eg, 10 rows/sec vs 100 IOPs). Also, let's say your data is not "bursty"; that is, the data comes in somewhat soothly throughout the day.

Note that 10 rows/sec (300M/year) implies maybe 30GB for data + indexes + normalization tables + summary tables for 1 year. I would call this "not so big".

Still, the [normalization](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/database-theory/database-normalization) and summarization are important. Normalization keeps the data from being, say, twice as big. Summarization speeds up the reports by orders of magnitude.

Let's design and analyse a "simple ingestion scheme" for 10 rows/second, without 'batching'.

```sql
# Normalize:
    $foo_id = SELECT foo_id FROM Foos WHERE foo = $foo;
    IF NO $foo_id, THEN
        INSERT IGNORE INTO Foos ...

    # Inserts:
    BEGIN;
        INSERT INTO Fact ...;
        INSERT INTO Summary ... ON DUPLICATE KEY UPDATE ...;
    COMMIT;
    # (plus code TO deal WITH errors ON INSERTs OR COMMIT)
```

Depending on the number and randomness of your indexes, etc, 10 Fact rows may (or may not) take less than 100 IOPs.

Also, note that as the data grows over time, random indexes will become less and less likely to be cached. That is, even if runs fine with 1 year's worth of data, it may be in trouble with 2 year's worth.

For those reasons, I started this discussion with a wide margin (10 rows versus 100 IOPs).

## References

* [sec. 3.3.2: Dimensional Model and "Star schema"](https://www.redbooks.ibm.com/redbooks/pdfs/sg247138.pdf)
* Summary Tables

## See also

Rick James graciously allowed us to use this article in the documentation.

[Rick James' site](https://mysql.rjweb.org/) has other useful tips, how-tos,\
optimizations, and debugging tips.

Original source: [datawarehouse](https://mysql.rjweb.org/doc.php/datawarehouse)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
