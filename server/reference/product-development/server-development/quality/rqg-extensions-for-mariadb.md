---
description: >-
  Describes MariaDB-specific enhancements to the Random Query Generator tool for
  testing unique features and syntax.
---

# RQG Extensions for MariaDB

{% include "../../../../.gitbook/includes/this-page-contains-backgrou....md" %}

All recent reasonably stable changes can be found in [our Github repository](https://github.com/MariaDB/randgen). The link points to the master branch; there are other branches created for more specific cases.

While all described changes were made in order to test MariaDB code, many of them are applicable to other MySQL flavors as well.

## Galera Mode <a href="#galera-mode" id="galera-mode"></a>

A set of changes to support running RQG tests with multi-master Galera replication, implemented to test [MariaDB Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/).

The top-level script `runall-new.pl` got a new option `--galera`, which takes a string value. The string can be a combination of `'m'` or `'s'`, where each symbol represents a Galera node. `'m'` stands for `'master'`, and `'s'` stands for `'slave'`.

The new module `GaleraMySQLd.pm` implements cluster initialization and startup. It is only interested in the number of nodes.

Internals are adapted to the multi-master or mixed mode:

* Instead of executing data generation on each started server, it is only executed on the first master.
* Test flow is executed on each master (but not on slaves).
* No result comparison is performed after each query, the flow runs independently, but, in the end, if no other errors were encountered, `runall-new.pl` performs dump comparison in the usual manner.

Also, a sample grammar and data template are provided in `conf/galera`, they are slightly modified versions of `conf/engines/engine_stress.yy` and `engine_stress.zz`, adapted for Galera taking into account its limitations (e.g. no `LOCK`).

_Note: `GaleraMySQLd.pm` has defaults for everything mandatory but `wsrep_provider`. If you run the test with more than 1 node, you need to provide the value on the command line in the usual manner (`--mysqld=--wsrep-provider=...`), otherwise the test fails with the corresponding error message._

So, if you provide the following option:

```
--galera=mms --mysqld=--wsrep-provider=<path to Galera library>
```

3 nodes will be started, and Galera replication will be set up between them; the data will be generated on the first node; the test flow will be executed on the first and second nodes; at the end of the test, data dump from each node will be taken and compared; node vardirs will be placed under `<vardir>/node0`, `<vardir>/node1`, `<vardir>/node2`.

## CheckFieldValue Validator <a href="#checkfieldvalue-validator" id="checkfieldvalue-validator"></a>

A grammar can set requirements on results of a query through a specifically formatted comment. If the validator finds a comment which matches the template, it performs the requested check. The validation is defined in the comment itself: it says which field in which row in the result set should be checked, and provides the condition (currently simple numeric comparisons: `=`, `<`, `>`, `<=`, `>=`).

It allows to do simple verification without implementing a special validator.

Example:

A query in the grammar file

```sql
  SELECT COUNT(*), MAX(`pk`) FROM _table /* Validate 2 > 10 for row all*/;
```

The comment means "Check that the value in field 2 is greater than 10 for all rows" (for this query "all rows" is overkill, it could just as well be "row 1").

Assuming that there is a table with not more than 10 rows, the validator will produce the error:

```
ERROR: For query 'SELECT COUNT(*), MAX(`pk`) FROM `BB` /* Validate 2 > 10 for row 1*/' on row 1 result 10 does not meet the condition > 10
Full row: [1] : 1; [2] : 10;
```

The exit code for this failure is `STATUS_REQUIREMENT_UNMET`.

_Usage example: investigation of the sporadic failure_ [_MDEV-4578_](https://jira.mariadb.org/browse/MDEV-4578)_._

## MariadbGtidCrashSafety Reporter <a href="#mariadbgtidcrashsafety-reporter" id="mariadbgtidcrashsafety-reporter"></a>

The reporter was created to test slave crash-safety with [MariaDB implementation of GTID](../../../../ha-and-performance/standard-replication/gtid.md). It is similar to [SlaveCrashRecovery reporter](rqg-extensions-for-mariadb.md#slavecrashrecovery-reporter), but is adjusted to check GTID-specific aspects:

* It restarts the slave with `--skip-slave-start`, and executes these statements:

```sql
CHANGE MASTER .. MASTER_USE_GTID=current_pos;
STOP SLAVE;
```

So, regardless how the replication was set up initially, after the first crash or restart, it starts using GTID for sure, while the slave is running, and also before a crash and after restart the reporter checks `gtid*` variables and the contents of the system table `mysql.gtid_slave_pos` and verifies basic consistency of the data, e.g. watches that GTID `seq_no` constantly grows.

## SlaveCrashRecovery Reporter <a href="#slavecrashrecovery-reporter" id="slavecrashrecovery-reporter"></a>

The reporter can be used to test crash safety of replication.

It is a periodic reporter, every 30 seconds it kills the slave server using `SIGKILL`, and immediately restarts it on the old data directory, with the same parameters as before. On server restart, the reporter checks that the server and the replication started all right.

The reporter itself does not check consistency of the data, but it can be used together with `ReplicationConsistency` reporter.

It is supposed to be used with `runall-new.pl`, so that the server is started without MTR involvement.

_Usage example: testing of_ [_GTID in MariaDB_](../../../../ha-and-performance/standard-replication/gtid.md)_._

## BinlogConsistency Reporter <a href="#binlogconsistency-reporter" id="binlogconsistency-reporter"></a>

The reporter checks that the contents of the binary log correctly reflects the contents of the server.

After the main test flow is finished, the reporter creates a data dump of the server, stores its binary logs, shuts down the server, starts a new one with the same parameters, but on a clean data directory, replays the binary logs into it, creates a dump of the new server, and compares two dumps.

It is to be used with `runall-new.pl`.

_Usage example: testing of binlog changes in MariaDB 10.0 (e.g._ [_MDEV-181_](https://jira.mariadb.org/browse/MDEV-181)_,_ [_MDEV-232_](https://jira.mariadb.org/browse/MDEV-232)_)_

## CrashRecovery Reporter <a href="#crashrecovery-reporter" id="crashrecovery-reporter"></a>

The idea is very much the same as in the old Recovery reporter: crash the server at the end of the test, restart it and make sure it started all right, and the data is not corrupted. The main difference is that the old reporter restarts the server in a hardcoded pre-defined manner, which limits its use. Instead, CrashRecovery reporter starts the server with the same set of options as the initial one, which imitates a more realistic scenario, and also allows to use it on non-default InnoDB configurations.

It is to be used with `runall-new.pl` .

## LimitRowsExamined Transformer <a href="#limitrowsexamined-transformer" id="limitrowsexamined-transformer"></a>

The transformer was developed for testing the [LIMIT ROWS EXAMINED](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/limit-rows-examined.md) functionality added in MariaDB 5.5. It can be used in the usual way, by providing its name in the `--transformers` list.

The transformer checks whether the original query already contains a `ROWS EXAMINED` clause. If it does not, it adds the clause either after the `LIMIT` clause, or at the end of the query. In any case (even if `ROWS EXAMINED` was already there), the transformer returns the following sequence of statements:

* `FLUSH STATUS`
* \<the query with `ROWS EXAMINED`>
* \<a query which sums up status variables related to examined rows>

The result of the main query is checked to be a subset of the original query's result set. The sum of status variables is checked to be not greater than the limit provided in the `ROWS EXAMINED` clause, plus a margin. The margin is configured in the transformer.

If the result of the transformed query appears not to be a subset of the original result set, `STATUS_LENGTH_MISMATCH` is returned.

If the sum of status variables is greater than the maximum allowed value, `STATUS_REQUIREMENT_UNMET` is returned.

Note: Status values `STATUS_REQUIREMENT_UNMET` and `STATUS_REQUIREMENT_UNMET_SELECT` were added to `Constants.pm`.

## ShowExplain Validator <a href="#showexplain-validator" id="showexplain-validator"></a>

The validator was developed for testing [SHOW EXPLAIN](../../../sql-statements/administrative-sql-statements/show/show-explain.md).

The validator checks that the output of `SHOW EXPLAIN` correlates with the output of traditional `EXPLAIN` executed for the same query. It also tries to filter out known expected mismatches between the produced plans.

## Comparison of VIEW Algorithms <a href="#comparison-of-view-algorithms" id="comparison-of-view-algorithms"></a>

RQG already provided `--views[=<view type>]` option, which means that in addition to the normal data generation, views of the requested types will be added and used in the test flow. However, you could only create views of the same type on servers that you were comparing. Now there are `--views1` and `--views2` options, which work the same way as `--basedir1`/`--basedir2`, `--mysqld1`/`--mysqld2`, etc. The backward compatibility is preserved, so you can still use `--views` which will be applied to both servers unless there is `--views1` or `--views2` to override it.

The change was made in `gentest.pl` and both `runall.pl` and `runall-new.pl`.

_Usage example: testing of MERGE view extension in MariaDB 10.0 (_[_MDEV-3862_](https://jira.mariadb.org/browse/MDEV-3862)_)_

## Multiple Redefining Grammars <a href="#multiple-redefining-grammars" id="multiple-redefining-grammars"></a>

RQG allows to provide `--redefine=<grammar file>` option to override or add rules to the main grammar. Sometimes you have a redefining grammar for a feature, and another redefining grammar for an engine, and yet another redefining grammar for a specific version, and combining them makes the number of grammars to grow uncontrollably. The simple change has been made to allow providing several redefining grammars at once, for instance:

```perl
runall.pl ... --redefine=memory_engine_redefine.yy --redefine=binlog_format_stmt_redefine.yy --redefine=legacy_version_redefine.yy
```

{% hint style="warning" %}
It is better not to allow them to override each other, since the result can be unexpected (that is, they should define different sets of rules).
{% endhint %}

The change was made in `gentest.pl` and both `runall.pl` and `runall-new.pl`.

## Keywords \_basetable and \_view <a href="#new-grammar-keywords-_basetable-and-_view" id="new-grammar-keywords-_basetable-and-_view"></a>

The RQG keyword `_table` means any table or view from the test dataset. Often it's good enough, but sometimes it badly increases the number of erroneous statements. Now tables and views can be differentiated in a grammar depending on what the goal is: `_table` can still be used for both tables and views, while \_basetable will only pick tables, and \_view will only pick views.

Example: If you create the following rule in your grammar:

```sql
alter:
        ALTER TABLE _table ENGINE=MyISAM;
```

When you are running the test with views, you get lots of `ER_WRONG_OBJECT` errors ("is not BASE TABLE"). This is hardly the goal, so you can improve the grammar by changing it to this:

```sql
alter:
        ALTER TABLE _basetable ENGINE=MyISAM;
```

That way, the rule only picks "real" tables. Of course, if you still want to pick views sometimes, as a sanity check that there is no crash or anything, you can make the rule a bit more complicated, but much better tuned than it was:

```sql
alter:
        ALTER TABLE alter_object ENGINE=MyISAM;

alter_object:
        _basetable | _basetable | _basetable | _basetable | _basetable | _view ;
```

## See Also <a href="#see-also" id="see-also"></a>

* [RQG Performance Comparisons](benchmarks-and-long-running-tests/benchmarks/rqg-performance-comparisons.md)
* [RQG Extensions for MariaDB Features](rqg-extensions-for-mariadb.md)
* [Optimizer Quality](optimizer-quality.md)
* [QA Tools](qa-tools.md)
* [Worklog Quality Checklist Template](worklog-quality-checklist-template.md)
