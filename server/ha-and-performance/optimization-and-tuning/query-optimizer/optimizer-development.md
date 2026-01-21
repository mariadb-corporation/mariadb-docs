# Optimizer Development

Notes about Optimizer Development

## mysql-test

### InnoDB Estimates are unstable

This is caused by background statistics update. It may cause the numbers in EXPLAIN output to be off-by-one. It may also cause different query plans to be picked on different runs (See e.g. [MDEV-32901](https://jira.mariadb.org/browse/MDEV-32901) for details)

On a per-table basis, one can use `STATS_AUTO_RECALC=0` as table parameter.

On a per-file basis, one can use this include:

```
--source mysql-test/include/innodb_stable_estimates.inc
```

### Run mtr with Optimizer Trace enabled

TODO

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
