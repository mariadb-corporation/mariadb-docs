# Data Warehousing High Speed Ingestion

## The problem

You are ingesting lots of data. Performance is bottlenecked in the INSERT area.

This will be couched in terms of Data Warehousing, with a huge `Fact` table and Summary (aggregation) tables.

## Overview of solution

* Have a separate staging table.
* Inserts go into `Staging`.
* Normalization and Summarization reads Staging, not Fact.
* After normalizing, the data is copied from Staging to Fact.

`Staging` is one (or more) tables in which the data lives only long enough to be handed off to Normalization, Summary, and the Fact tables.

Since we are probably talking about a billion-row table, shrinking the width of the Fact table by normalizing (as mentioned here). Changing an [INT](../../../reference/data-types/numeric-data-types/int.md) to a [MEDIUMINT](../../../reference/data-types/numeric-data-types/mediumint.md) will save a GB. Replacing a string by an id (normalizing) saves many GB. This helps disk space and cacheability, hence speed.

## Injection speed

Some variations:

* Big dump of data once an hour, versus continual stream of records.
* The input stream could be single-threaded or multi-threaded.
* You might have 3rd party software tying your hands.

Generally the fastest injection rate can be achieved by "staging" the INSERTs in some way, then batch processing the staged records. This blog discusses various techniques for staging and batch processing.

## Normalization

Let's say your Input has a [VARCHAR](../../../reference/data-types/string-data-types/varchar.md) `host_name` column, but you need to turn that into a smaller [MEDIUMINT](../../../reference/data-types/numeric-data-types/mediumint.md) `host_id` in the Fact table. The "Normalization" table, as I call it, looks something like

```sql
CREATE TABLE Hosts (
    host_id  MEDIUMINT UNSIGNED  NOT NULL AUTO_INCREMENT,
    host_name VARCHAR(99) NOT NULL,
    PRIMARY KEY (host_id),      -- for mapping one direction
    INDEX(host_name, host_id)   -- for mapping the other direction
) ENGINE=InnoDB;                -- InnoDB works best for Many:Many mapping table
```

Here's how you can use `Staging` as an efficient way achieve the swap from name to id.

Staging has two fields (for this normalization example):

```sql
host_name VARCHAR(99) NOT NULL,     -- Comes from the insertion process
    host_id  MEDIUMINT UNSIGNED  NULL,  -- NULL to start with; see code below
```

Meawhile, the Fact table has:

```sql
host_id  MEDIUMINT UNSIGNED NOT NULL,
```

SQL #1 (of 2):

```sql
# This should not be in the main transaction, and it should be done with autocommit = ON
    # In fact, it could lead to strange errors if this were part
    #    of the main transaction and it ROLLBACKed.
    INSERT IGNORE INTO Hosts (host_name)
        SELECT DISTINCT s.host_name
            FROM Staging AS s
            LEFT JOIN Hosts AS n  ON n.host_name = s.host_name
            WHERE n.host_id IS NULL;
```

By isolating this as its own transaction, we get it finished in a hurry, thereby minimizing blocking. By saying IGNORE, we don't care if other threads are 'simultaneously' inserting the same host\_names.

There is a subtle reason for the LEFT JOIN. If, instead, it were INSERT IGNORE..SELECT DISTINCT, then the INSERT would preallocate auto\_increment ids for as many rows as the SELECT provides. This is very likely to "burn" a lot of ids, thereby leading to overflowing MEDIUMINT unnecessarily. The LEFT JOIN leads to finding just the new ids that are needed (except for the rare possibility of a 'simultaneous' insert by another thread). More rationale: [Mapping table](../optimization-and-indexes/building-the-best-index-for-a-given-select.md)

SQL #2:

```sql
# Also not in the main transaction, and it should be with autocommit = ON
    # This multi-table UPDATE sets the ids in Staging:
    UPDATE   Hosts AS n
        JOIN Staging AS s  ON s.host_name = n host_name
        SET s.host_id = n.host_id
```

This gets the IDs, whether already existing, set by another thread, or set by SQL #1.

If the size of `Staging` changes depending on the busy versus idle times of the day, this pair of SQL statements has another comforting feature. The more rows in `Staging`, the more efficient the SQL runs, thereby helping compensate for the "busy" times.

The companion [Data Warehouse article](data-warehousing-techniques.md) folds SQL #2 into the INSERT INTO Fact. But you may need host\_id for further normalization steps and/or Summarization steps, so this explicit UPDATE shown here is often better.

## Flip-flop staging

The simple way to stage is to ingest for a while, then batch-process what is in `Staging`. But that leads to new records piling up waiting to be staged. To avoid that issue, have 2 processes:

* one process (or set of processes) for INSERTing into `Staging`;
* one process (or set of processes) to do the batch processing (normalization, summarization).

To keep the processes from stepping on each other, we have a pair of staging tables:

* `Staging` is being INSERTed into;
* `StageProcess` is one being processed for normalization, summarization, and moving to the Fact table.\
  A separate process does the processing, then swaps the tables:

```sql
DROP   TABLE StageProcess;
    CREATE TABLE StageProcess LIKE Staging;
    RENAME TABLE Staging TO tmp, StageProcess TO Staging, tmp TO StageProcess;
```

This may not seem like the shortest way to do it, but has these features:

* The DROP + CREATE might be faster than TRUNCATE, which is the desired effect.
* The RENAME is atomic, so the INSERT process(es) never find that `Staging` is missing.

A variant on the 2-table flip-flop is to have a separate `Staging` table for each Insertion process. The Processing process would run around to each Staging in turn.

A variant on that would be to have a separate processing process for each Insertion process.

The choice depends on which is faster (insertion or processing). There are tradeoffs; a single processing thread avoids some locks, but lacks some parallelism.

## Engine choice

`Fact` table -- [InnoDB](../../../server-usage/storage-engines/innodb/), if for no other reason than that a system crash would not need a REPAIR TABLE. (REPAIRing a billion-row [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/) table can take hours or days.)

Normalization tables -- InnoDB, primarily because it can be done efficiently with 2 indexes, whereas, MyISAM would need 4 to achieve the same efficiency.

`Staging` -- Lots of options here.

* If you have multiple Inserters and a single Staging table, InnoDB is desirable due to row-level, not table-level, locking.
* MEMORY may be the fastest and it avoids I/O. This is good for a single staging table.
* For multiple Inserters, a separate Staging table for each Inserter is desired.
* For multiple Inserters into a single Staging table, InnoDB may be faster. (MEMORY does table-level locking.)
* With one non-InnoDB Staging table per Inserter, using an explicit LOCK TABLE avoids repeated implicit locks on each INSERT.
* But, if you are doing LOCK TABLE and the Processing thread is separate, an UNLOCK is necessary periodically to let the RENAME grab the table.
* "Batch INSERTs" (100-1000 rows per SQL) eliminates much of the issues of the above bullet items.

Confused? Lost? There are enough variations in applications that make it impractical to predict what is best. Or, simply good enough. Your ingestion rate may be low enough that you don't hit the brick walls that I am helping you avoid.

Should you do "CREATE TEMPORARY TABLE"? Probably not. Consider `Staging` as part of the data flow, not to be DROPped.

## Summarization

This is mostly covered here: [Summary Tables](data-warehousing-summary-tables.md)\
Summarize from the Staging table instead of the Fact table.

## Replication Issues

Row Based Replication (RBR) is probably the best option.

The following allows you to keep more of the Ingestion process in the Master, thereby not bogging down the Slave(s) with writes to the Staging table.

* RBR
* `Staging` is in a separate database
* That database is not replicated (binlog-ignore-db on Master)
* In the Processing steps, USE that database, reach into the main db via syntax like "MainDb.Hosts". (Otherwise, the binlog-ignore-db does the wrong thing.)

That way

* Writes to `Staging` are not replicated.
* Normalization sends only the few updates to the normalization tables.
* Summarization sends only the updates to the summary tables.
* Flip-flop does not replicate the DROP, CREATE or RENAME.

## Sharding

You could possibly spread the data you are trying ingest across multiple machines in a predictable way (sharding on hash, range, etc). Running "reports" on a sharded Fact table is a challenge unto itself. On the other hand, Summary Tables rarely get too big to manage on a single machine.

For now, Sharding is beyond the scope of this blog.

## Push me vs pull me

I have implicitly assumed the data is being pushed into the database. If, instead, you are "pulling" data from some source(s), then there are some different considerations.

Case 1: An hourly upload; run via cron

1. Grab the upload, parse it
2. Put it into the Staging table
3. Normalize -- each SQL in its own transaction (autocommit)
4. BEGIN
5. Summarize
6. Copy from Staging to Fact.
7. COMMIT

If you need parallelism in Summarization, you will have to sacrifice the transactional integrity of steps 4-7.

Caution: If these steps add up to more than an hour, you are in deep dodo.

Case 2: You are polling for the data

It is probably reasonable to have multiple processes doing this, so it will be detailed about locking.

1. Create a Staging table for this polling processor.\
   Loop:
2. With some locked mechanism, decide which 'thing' to poll.
3. Poll for the data, pull it in, parse it. (Potentially polling and parsing are significantly costly)
4. Put it into the process-specific Staging table
5. Normalize -- each SQL in its own transaction (autocommit)
6. BEGIN
7. Summarize
8. Copy from Staging to Fact.
9. COMMIT
10. Declare that you are finished with this 'thing' (see step 1)\
    EndLoop.

iblog\_file\_size should be larger than the change in the STATUS "Innodb\_os\_log\_written" across the BEGIN...COMMIT transaction (for either Case).

## See also

* [companion Data Warehouse blog](data-warehousing-techniques.md)
* [companion Summary Table blog](data-warehousing-summary-tables.md)
* [a forum thread that prodded me into writing this blog](https://forums.mysql.com/read.php?106,623744)
* [StackExchange discussion](https://dba.stackexchange.com/a/108726/1876)

Rick James graciously allowed us to use this article in the documentation.

[Rick James' site](https://mysql.rjweb.org/) has other useful tips, how-tos,\
optimizations, and debugging tips.

Original source: [staging\_table](https://mysql.rjweb.org/doc.php/staging_table)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
