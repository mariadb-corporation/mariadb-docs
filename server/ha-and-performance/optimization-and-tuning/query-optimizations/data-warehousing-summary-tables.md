# Data Warehousing Summary Tables

## Preface

This document discusses the creation and maintenance of "Summary Tables". It is a companion to the document on [Data Warehousing Techniques](data-warehousing-techniques.md).

The basic terminology ("Fact Table", "[Normalization](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/database-theory/database-normalization)", etc) is covered in that document.

## Summary tables for data warehouse "reports"

Summary tables are a performance necessity for large tables. MariaDB and MySQL do not provide any automated way to create such, so I am providing techniques here.

(Other vendors provide something similar with "materialized views".)

When you have millions or billions of rows, it takes a long time to summarize the data to present counts, totals, averages, etc, in a size that is readily digestible by humans. By computing and saving subtotals as the data comes in, one can make "reports" run much faster. (I have seen 10x to 1000x speedups.) The subtotals go into a "summary table". This document guides you on efficiency in both creating and using such tables.

## General structure of a summary table

A summary table includes two sets of columns:

* Main KEY: date + some dimension(s)
* Subtotals: COUNT(\*), SUM(...), ...; but not AVG()

The "date" might be a DATE (a 3-byte native datatype), or an hour, or some other time interval. A 3-byte MEDIUMINT UNSIGNED 'hour' can be derived from a DATETIME or TIMESTAMP via

```sql
FLOOR(UNIX_TIMESTAMP(dt) / 3600)
   FROM_UNIXTIME(hour * 3600)
```

The "dimensions" (a DW term) are some of the columns of the "Fact" table. Examples: Country, Make, Product, Category, Host Non-dimension examples: Sales, Quantity, TimeSpent

There would be one or more indexes, usually starting with some dimensions and ending with the date field. By ending with the date, one can efficiently get a range of days/weeks/etc. even when each row summarizes only one day.

There will typically be a "few" summary tables. Often one summary table can serve multiple purposes sufficiently efficiently.

As a rule of thumb, a summary table will have one-tenth the number of rows as the Fact table. (This number is very loose.)

## Example

Let's talk about a large chain of car dealerships.\
The Fact table has all the sales with columns such as\
datetime, salesman\_id, city, price, customer\_id, make, model, model\_year.\
One Summary table might focus on sales:

```sql
PRIMARY KEY(city, datetime),
   Aggregations: ct, sum_price
   
   # Core of INSERT..SELECT:
   DATE(datetime) AS DATE, city, COUNT(*) AS ct, SUM(price) AS sum_price
   
   # Reporting average price FOR last month, broken down BY city:
   SELECT city,
          SUM(sum_price) / SUM(ct) AS 'AveragePrice'
      FROM SalesSummary
      WHERE datetime BETWEEN ...
      GROUP BY city;
   
   # Monthly sales, nationwide, FROM same summary TABLE:
   SELECT MONTH(datetime) AS 'Month',
          SUM(ct)         AS 'TotalSalesCount'
          SUM(sum_price)  AS 'TotalDollars'
      FROM SalesSummary
      WHERE datetime BETWEEN ...
      GROUP BY MONTH(datetime);
   # This might benefit FROM a secondary INDEX(datetime)
```

## When to augment the summary table(s)?

"Augment" in this section means to add new rows into the summary table or increment the counts in existing rows.

Plan A: "While inserting" rows into the Fact table, augment the summary table(s). This is simple, and workable for a smaller DW database (under 10 Fact table rows per second). For larger DW databases, Plan A likely to be too costly to be practical.

Plan B: "Periodically", via cron or an EVENT.

Plan C: "As needed". That is, when someone asks for a report, the code first updates the summary tables that will be needed.

Plan D: "Hybrid" of B and C. C, by itself, can led to long delays for the report. By also doing B, those delays can be kept low.

Plan E: (This is not advised.) "Rebuild" the entire summary table from the entire Fact table. The cost of this is prohibitive for large tables. However, Plan E may be needed when you decide to change the columns of a Summary Table, or discover a flaw in the computations.\
To lessen the impact of an entire build, adapt the chunking techniques in [Deleting in chunks](big-deletes.md#deleting_in_chunks) .

Plan F: "Staging table". This is primarily for very high speed ingestion. It is mentioned briefly in this blog, and discussed more thoroughly in the companion blog: High Speed Ingestion

## Summarizing while Inserting (one row at a time)

```sql
INSERT INTO Fact ...;
    INSERT INTO Summary (..., ct, foo, ...) VALUES (..., 1, foo, ...)
        ON DUPLICATE KEY UPDATE ct = ct+1, sum_foo = sum_foo + VALUES(foo), ...;
```

IODKU (Insert On Duplicate Key Update) will update an existing row or create a new row. It knows which to do based on the Summary table's PRIMARY KEY.

Caution: This approach is costly, and will not scale to an ingestion rate of over, say, 10 rows per second (Or maybe 50/second on SSDs). More discussion later.

## Summarizing periodically vs as-needed

If your reports need to be up-to-the-second, you need "as needed" or "hybrid". If your reports have less urgency (eg, weekly reports that don't include 'today'), then "periodically" might be best.

For a daily summaries, augmenting the summary tables could be done right after midnight. But, beware of data coming "late".

For both "periodic" and "as needed", you need a definitive way of keeping track of where you "left off".

Case 1: You insert into the Fact table first and it has an AUTO\_INCREMENT id: Grab MAX(id) as the upper bound for summarizing and put it either into some other secure place (an extra table), or put it into the row(s) in the Summary table as you insert them. (Caveat: AUTO\_INCREMENT ids do not work well in multi-master, including Galera, setups.)

Case 2: If you are using a 'staging' table, there is no issue. (More on staging tables later.)

## Summarizing while batch inserting

This applies to multi-row (batch) INSERT and LOAD DATA.

The Fact table needs an AUTO\_INCREMENT id, and you need to be able to find the exact range of ids inserted. (This may be impractical in any multi-master setup.)

Then perform bulk summarization using

```sql
FROM Fact
   WHERE id BETWEEN min_id AND max_id
```

## Summarizing when using a staging table

Load the data (via INSERTs or \[LOAD DATA) en masse into a "staging table". Then perform batch summarization from the Staging table. And batch copy from the Staging table to the Fact table. Note that the Staging table is handy for batching "normalization" during ingestion.\
See also \[[data-warehousing-high-speed-ingestion|High Speed Ingestion](../../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md)

## Summary table: PK or not?

Let's say your summary table has a DATE, `dy`, and a dimension, `foo`. The question is: Should (foo, dy) be the PRIMARY KEY? Or a non-UNIQUE index?

Case 1: PRIMARY KEY (foo, dy) and summarization is in lock step with, say, changes in `dy`.

This case is clean and simple -- until you get to endcases. How will you handle the case of data arriving 'late'? Maybe you will need to recalculate some chunks of data? If so, how?

Case 2: (foo, dy) is a non-UNIQUE INDEX.

This case is clean and simple, but it can clutter the summary table because multiple rows can occur for a given (foo, dy) pair. The report will always have to [SUM()](../../../reference/sql-functions/aggregate-functions/sum.md) up values because it cannot assume there is only one row, even when it is reporting on a single `foo` for a single `dy`. This forced-SUM is not really bad -- you should do it anyway; that way all your reports are written with one pattern.

Case 3: PRIMARY KEY (foo, dy) and summarization can happen anytime.

Since you should be using InnoDB, there needs to be an explicit PRIMARY KEY.\
One approach when you do not have a 'natural' PK is this:

```sql
id INT UNSIGNED AUTO_INCREMENT NOT NULL,
   ...
   PRIMARY KEY(foo, dy, id),  -- `id` added to make unique
   INDEX(id)                  -- sufficient to keep AUTO_INCREMENT happy
```

This case pushes the complexity onto the summarization by doing a IODKU.

Advice? Avoid Case 1; too messy. Case 2 is ok if the extra rows are not too common. Case 3 may be the closest to "once size fits all".

## Averages, etc.

When summarizing, include `COUNT(*) AS ct and SUM(foo) AS sum_foo`. When reporting, the "average" is computed as SUM(sum\_foo) / SUM(ct). That is mathematically correct.

Exception... Let's say you are looking at weather temperatures. And you monitoring station gets the temp periodically, but unreliably. That is, the number of readings for a day varies. Further, you decide that the easiest way to compensate for the inconsistency is to do something like: Compute the avg temp for each day, then average those across the month (or other timeframe).

Formula for Standard Deviation:

```sql
SQRT( SUM(sum_foo2)/SUM(ct) - POWER(SUM(sum_foo)/SUM(ct), 2) )
```

Where sum\_foo2 is SUM(foo \* foo) from the summary table. sum\_foo and sum\_foo2 should be FLOAT. FLOAT gives you about 7 significant digits, which is more than enough for things like average and standard deviation. FLOAT occupies 4 bytes. DOUBLE would give you more precision, but occupies 8 bytes. INT and BIGINT are not practical because they may lead to complaints about overflow.

## Staging table

The idea here is to first load a set of Fact records into a "staging table", with the following characteristics (at least):

* The table is repeatedly populated and truncated
* Inserts could be individual or batched, and from one or many clients
* SELECTs will be table scans, so no indexes needed
* Inserting will be fast (InnoDB may be the fastest)
* Normalization can be done in bulk, hence efficiently
* Copying to the Fact table will be fast
* Summarization can be done in bulk, hence efficiently
* "Bursty" ingestion is smoothed by this process
* Flip-flop a pair of Staging tables

If you have bulk inserts (Batch INSERT or LOAD DATA) then consider doing the normalization and summarization immediately after each bulk insert.

More details: High Speed Ingestion

## Extreme design

Here is a more complex way to design the system, with the goal of even more scaling.

* Use master-slave setup: ingest into master; report from slave(s).
* Feed ingestion through a staging table (as described above)
* Single-source of data: ENGINE=MEMORY; multiple sources: InnoDB
* [binlog\_format = ROW](../../standard-replication/replication-and-binary-log-system-variables.md)
* Use [binlog\_ignore\_db](../../standard-replication/replication-and-binary-log-system-variables.md) to avoid replicating staging -- necessitating putting it in a separate database.
* Do the summarization from Staging
* Load Fact via INSERT INTO Fact ... SELECT FROM Staging ...

Explanation and comments:

* ROW + ignore\_db avoids replicating Staging, yet replicates the INSERTs based on it. Hence, it lightens the write load on the Slaves
* If using MEMORY, remember that it is volatile -- recover from a crash by starting the ingestion over.
* To aid with debugging, TRUNCATE or re-CREATE Staging at the start of the next cycle.
* Staging needs no indexes -- all operations read all rows from it.

Stats on the system that this 'extreme design' came from: Fact Table: 450GB, 100M rows/day (batch of 4M/hour), 60 day retention (60+24 partitions), 75B/row, 7 summary tables, under 10 minutes to ingest and summarize the hourly batch. The INSERT..SELECT handled over 20K rows/sec going into the Fact table.\
Spinning drives (not SSD) with RAID-10.

## "Left Off"

One technique involves summarizing some of the data, then recording where you "left off", so that next time, you can start there. There are some subtle issues with "left off" that you should be cautious of.

If you use a DATETIME or TIMESTAMP as "left off", beware of multiple rows with the same value.

* Plan A: Use a compound "left off" (eg, TIMESTAMP + ID). This is messy, error prone, etc.
* Plan B: WHERE ts >= $left\_off AND ts < $max\_ts -- avoids dups, but has other problems (below)
* Separate threads could COMMIT TIMESTAMPs out of order.

If you use an AUTO\_INCREMENT as "left off" beware of:

* In InnoDB, separate threads could COMMIT ids in the 'wrong' order.
* Multi-master (including Galera and InnoDB Cluster), could lead to ordering issues.

So, nothing works, at least not in a multi-threaded environment?

If you can live with an occasional hiccup (skipped record), then maybe this is 'not a problem' for you.

The "Flip-Flop Staging" is a safe alternative, optionally combined with the "Extreme Design".

## Flip-flop staging

If you have many threads simultaneously INSERTing into one staging table, then here is an efficient way to handle a large load: Have a process that flips that staging table with another, identical, staging table, and performs bulk normalization, Fact insertion, and bulk summarization.

The flipping step uses a fast, atomic, RENAME.

Here is a sketch of the code:

```sql
# Prep FOR flip:
    CREATE TABLE new LIKE Staging;

    # Swap (flip) Staging tables:
    RENAME TABLE Staging TO old, new TO Staging;

    # Normalize new `foo`s:
    # (autocommit = 1)
    INSERT IGNORE INTO Foos SELECT fpp FROM old LEFT JOIN Foos ...

    # Prep FOR possible deadlocks, etc
    WHILE...
    START TRANSACTION;

    # ADD TO Fact:
    INSERT INTO Fact ... FROM old JOIN Foos ...

    # Summarize:
    INSERT INTO Summary ... FROM old ... GROUP BY ...

    COMMIT;
    end-WHILE

    # Cleanup:
    DROP TABLE old;
```

Meanwhile, ingestion can continue writing to `Staging`. The ingestion INSERTs will conflict with the RENAME, but will be resolved gracefully and silently and quickly.

How fast should you flip-flop? Probably the best scheme is to

* Have a job that flip-flops in a tight loop (no delay, or a small delay, between iterations), and
* Have a CRON that serves only as a "keep-alive" to restart the job if it dies.

If Staging is 'big', an iteration will take longer, but run more efficiently. Hence, it is self-regulating.

In a [Galera](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/) (or InnoDB Cluster?) environment, each node could be receiving input. If can afford to loose a few rows, have `Staging` be a non-replicated MEMORY table. Otherwise, have one `Staging` per node and be InnoDB; it will be more secure, but slower and not without problems. In particular, if a node dies completely, you somehow need to process its `Staging` table.

## Multiple summary tables

* Look at the reports you will need.
* Design a summary table for each.
* Then look at the summary tables -- you are likely to find some similarities.
* Merge similar ones.

To look at what a report needs, look at the WHERE clause that would provide the data. Some examples, assuming data about service records for automobiles: The GROUP BY to gives a clue of what the report might be about.

1. WHERE make = ? AND model\_year = ? GROUP BY service\_date, service\_type
2. WHERE make = ? AND model = ? GROUP BY service\_date, service\_type
3. WHERE service\_type = ? GROUP BY make, model, service\_date
4. WHERE service\_date between ? and ? GROUP BY make, model, model\_year

You need to allow for 'ad hoc' queries? Well, look at all the ad hoc queries -- they all have a date range, plus nail down one or two other things. (I rarely see something as ugly as '%CL%' for nailing down another dimension.) So, start by thinking of date plus one or two other dimensions as the 'key' into a new summary table. Then comes the question of what data might be desired -- counts, sums, etc. Eventually you have a small set of summary tables. Then build a front end to allow them to pick only from those possibilities. It should encourage use of the existing summary tables, not be truly 'open ended'.

Later, another 'requirement' may surface. So, build another summary table. Of course, it may take a day to initially populate it.

## Games on summary tables

Does one ever need to summarize a summary table? Yes, but only in extreme situations. Usually a 'weekly' report can be derived from a 'daily' summary table; building a separate weekly summary table not being worth the effort.

Would one ever PARTITION a Summary Table? Yes, in extreme situations, such as the table being large, and

* Need to purge old data (unlikely), or
* Recent' data is usually requested, and the index(es) fail to prevent table scans (rare). ("Partition pruning" to the rescue.)

## See also

Rick James graciously allowed us to use this article in the documentation.

[Rick James' site](https://mysql.rjweb.org/) has other useful tips, how-tos,\
optimizations, and debugging tips.

Original source: [summarytables](https://mysql.rjweb.org/doc.php/summarytables)

Examples

* [1876](https://dba.stackexchange.com/a/144723/1876)
* [1766831](https://stackoverflow.com/a/39403194/1766831)
* [1766831](https://stackoverflow.com/a/40310314/1766831)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
