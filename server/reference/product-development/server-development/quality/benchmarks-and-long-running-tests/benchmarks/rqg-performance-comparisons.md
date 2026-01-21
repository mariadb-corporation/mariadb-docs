# RQG Performance Comparisons

## Performance testing

The `performance/perfrun.pl` executes each query against a set of tw servers\
and reports the outcome.

```
perl performance/perfrun.pl --input-directory=... --dsn1=... --dsn2=... --output-file=... --filter=...
```

* `--input-directory` contains the queries to be run, one query\
  per file. Alternative sources for queries will be made available in the\
  future;
* `--dsn1` and `--dsn2` specify the locations of\
  the two servers being compared in the Perl DBI URL format. If the queries are\
  not fully qualified, the DSNs must contain the database name. The username\
  and the password are also provided via the DSN. For example:

```
--dsn1=dbi:mysql:host=127.0.0.1:port=19300:user=root:database=test \
--dsn2=dbi:mysql:host=127.0.0.1:port=19302:user=root:database=test
```

* `--output-file=...` specifies a file where matching queries\
  will be dumped in a form suitable for follow-up filtering with `perfreport`
* if no `--filter` is specified, all queries from the input will\
  be reported;

## Performance reporting

The `performance/perfreport.pl` script takes an ouput file created by`perfrun` and prints out its contents, possibly applying a filter in the\
process:

```
perl performance/perfreport.pl --input-file=... --filter=...
```

If no `--filter` is specified, all queries present in the input\
file are printed.

## Filters

The queries reported by the system can be filtered out using perl-based\
filtering expressions. A filter can be applied during data collection, at which\
point it determines what information is stored in the output file and at

If you do not specify a filter, it is assumed that you want to output all\
queries.

The following variables can participate in filter expressions:

* Variables from `SHOW SESSION STATUS`, except:
  * variables that are not reset at the start of the query, which\
    includes `Com_*`, `Uptime`, `Opened_files` and the like;
  * variables that relate to the operation of SSL encryption or the query cache;
* Variables from `SHOW GLOBAL STATUS LIKE 'Innodb_%'`

For each MySQL status variable, 4 Perl variables are provided\
— the value of the MySQL variable from each server,\
their absolute difference and their ratio. For example, for the`Innodb_rows_read` MySQL variable, you can use `Innodb_rows_read1`,`Innodb_rows_read2` , `Innodb_rows_read_delta` and`Innodb_rows_read_ratio` in your Perl filter expressions.

In addition to the MySQL status variables, the framework provides the following\
additional variables:

* `$Execution_time{1|2|delta|ratio}` reports the time the query took to run\
  from start to end in seconds. The value is truncated at milliseconds in order\
  to prevent exorbitant performance ratios from being reported on very fast\
  queries;
* `$Temperature` can either be `cold` or `warm` depending on whether the\
  first execution of the query is being processed, or the second.
* `$Query` contains the text of the query, in order to enable filtering such\
  as `$Query !~ m{l_receiptDATE}`

For example, the following command-line option:

```
--filter='($Execution_time1 > 0.1 || $Execution_time2 > 0.1) && $Temperature eq "warm"'
```

Will only process or report queries that took more than 0.1 sec to execute on a\
warm server.

## On-screen Reporting Format

The ASCII on-screen reporting format is as follows:

```
Query: SELECT  l_linenumber FROM lineitem  WHERE l_suppkey  IN ( 10 , 1 ) AND l_shipdate NOT IN ( '1993-06-06' , '1998-02-04' , '1992-01-08' ) AND l_linenumber NOT IN ( 8 , 7 ) AND l_quantity <> 3 AND ( l_orderkey NOT IN ( 1298 , 93 ) OR l_suppkey = 10 ) AND ( l_suppkey BETWEEN 4 AND 10 + 4 OR l_linenumber = 2 AND l_commitDATE BETWEEN '1993-06-27' AND '1993-09-05' AND l_linenumber BETWEEN 3 AND 9 + 9 );
Cache: warm
                                    5.3.0-MariaDB-     5.2.6-MariaDB-          Delta              Ratio
-------------------------------------------------------------------------------------------------------
Execution time                               0.011s            0.004s           -0.007s            0.36
Innodb_buffer_pool_read_requests          2171              1836              -335                 0.85
Handler_read_rnd                           583                 0              -583
Handler_read_next                          583               602                19                 1.03
Innodb_rows_read                          1166               602              -564                 0.52
```

Only variables whose values are different between the two servers are reported.\
In this particular example, the query ran slower on `5.3.0-MariaDB` with warm\
cache and caused twice as many `Innodb_rows_read`.

## On-disk Data Storage Format

The on-disk storage format is `Data::Dumper` objects, wrapped in`<![CDATA[ ... ]]>` tags, without the file being a full-blown XML. The\
serialized representation is created by`GenTest::QueryPerformanceDelta::serialize()` and is read by using `eval()`\
in `performance/perfreport.pl`

## See also:

* [RQG Documentation](https://github.com/RQG/RQG-Documentation/wiki/Category:RandomQueryGenerator)
* [RQG Extensions for MariaDB Features](../../rqg-extensions-for-mariadb.md)
* [Optimizer Quality](../../optimizer-quality.md)
* [QA Tools](../../qa-tools.md)
* [Worklog Quality Checklist Template](../../worklog-quality-checklist-template.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
