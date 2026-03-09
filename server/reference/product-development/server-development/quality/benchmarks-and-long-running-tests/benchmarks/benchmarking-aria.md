# Benchmarking Aria

We have not yet had time to benchmark [Aria](../../../../../../server-usage/storage-engines/aria/) properly. Here follows some things that have been discussed on the [maria-discuss](https://launchpad.net/~maria-discuss) email list.

## Aria used for internal temporary tables

By default Aria (instead of MyISAM) is used for the internal temporary tables when MEMORY tables overflows to disk or MEMORY tables can't be used (for example when you are using temporary results with BLOB's).\
In most cases Aria should give you better performance than using MyISAM, but this is not always the case.

```
CREATE TABLE `t1` (`id` INT(11) DEFAULT NULL, `tea` TEXT) 
  ENGINE=MyISAM DEFAULT CHARSET=latin1;
INSERT t1 SELECT rand()*2e8, repeat(rand(), rand()*64) FROM t1;
```

Repeat the last row until you get 2097152 rows.

The queries tested

```
Q1: SELECT id, tea from t1 group by left(id,1) order by null;
Q2: SELECT id, count(*), tea from t1 group by left(id,1) order by null;
Q3: SELECT id, tea from t1 group by left(id,2) order by null;
Q4: SELECT id, count(*), tea from t1 group by left(id,2) order by null;
Q5: SELECT id, tea from t1 group by id % 100 order by null;
Q6: SELECT id, count(*), tea from t1 group by id % 100 order by null;
```

Results (times in seconds, lower is better):

| Test | Aria 8K page size | Aria 2K page size | MyISAM |
| ---- | ----------------- | ----------------- | ------ |
| Q1   | 3.08              | 2.41              | 2.17   |
| Q2   | 6.24              | 5.21              | 12.89  |
| Q3   | 4.87              | 4.05              | 4.04   |
| Q4   | 8.20              | 7.04              | 15.14  |
| Q5   | 7.10              | 6.37              | 6.28   |
| Q6   | 10.38             | 9.09              | 17.00  |

The good news is that for common group by queries that is using\
summary functions there is a close to 50 % speedup of using Aria for\
internal temporary tables.

Note that queries Q1,Q3 and Q5 are not typical queries as there is no\
sum functions involved. In this case rows are just written to the tmp\
tables and there is no updates. As soon as there are summary functions\
and updates the new row format in Aria gives a close to 50 % speedup.

The above table also shows how the page size (determined by the [aria\_block\_size](../../../../../../server-usage/storage-engines/aria/aria-system-variables.md#aria_block_size) system variable) affects the performance.\
The reason for the difference is that there is more data to move\
back/from the page cache for inserting of keys. (When reading data we\
are normally not copying pages). The bigger page size however allows\
longer keys and fewer index levels so for bigger data sets the\
different should be smaller. It's possible to in the future optimize\
Aria to not copy pages from the page cache also for index writes and\
then this difference should disappear.

The default page size for Aria is 8K.

If you want to run MariaDB with MyISAM for temporary tables, don't use the configure option '--with-aria-tmp-tables' when building MariaDB.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
