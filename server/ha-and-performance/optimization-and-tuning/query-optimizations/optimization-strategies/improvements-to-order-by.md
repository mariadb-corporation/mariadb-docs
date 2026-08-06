# Improvements to ORDER BY Optimization

## Available tuning for ORDER BY with small LIMIT

* In 2024, fix for [MDEV-34720](https://jira.mariadb.org/browse/MDEV-34720) has added [optimizer\_join\_limit\_pref\_ratio optimization](../optimizer_join_limit_pref_ratio-optimization.md) into MariaDB starting from 10.6. It allows one to enable extra optimization for ORDER BY with small LIMIT.

## Older optimizations

MariaDB brought several improvements to the [ORDER BY](../../../../reference/sql-statements/data-manipulation/selecting-data/order-by.md) optimizer.

The fixes were made as a response to complaints by MariaDB customers, so they fix real-world optimization problems. The fixes are a bit hard to describe (as the `ORDER BY` optimizer is complicated), but here's a short description:

The [ORDER BY](../../../../reference/sql-statements/data-manipulation/selecting-data/order-by.md) optimizer:

* Doesn’t make stupid choices when several multi-part keys and potential range accesses are present ([MDEV-6402](https://jira.mariadb.org/browse/MDEV-6402)).
  * This also fixes [MySQL Bug#12113](https://bugs.mysql.com/bug.php?id=12113).
* Always uses “range” and (not full “index” scan) when it switches to an index to satisfy `ORDER BY … LIMIT` ([MDEV-6657](https://jira.mariadb.org/browse/MDEV-6657)).
* Tries hard to be smart and use cost/number of records estimates from other parts of the optimizer ([MDEV-6384](https://jira.mariadb.org/browse/MDEV-6384), [MDEV-465](https://jira.mariadb.org/browse/MDEV-465)).
  * This change also fixes [MySQL Bug#36817](https://bugs.mysql.com/bug.php?id=36817).
* Takes full advantage of InnoDB’s Extended Keys feature when checking if filesort() can be skipped ([MDEV-6796](https://jira.mariadb.org/browse/MDEV-6796)).

## Extra optimizations

* The [ORDER BY](../../../../reference/sql-statements/data-manipulation/selecting-data/order-by.md) optimizer takes multiple-equalities into account ([MDEV-8989](https://jira.mariadb.org/browse/MDEV-8989)). This optimization is enabled by default.

## Comparison with MySQL 5.7

In [MySQL 5.7 changelog](https://mysqlserverteam.com/whats-new-in-mysql-5-7-generally-available/), one can find this passage:

Make switching of index due to small limit cost-based ([WL#6986](https://askmonty.org/worklog/?tid=6986)) : We have made
the decision in make\_join\_select() of whether to switch to a new index in order to
support "ORDER BY ... LIMIT N" cost-based. This work fixes Bug#73837.

MariaDB is not using Oracle's fix (we believe `make_join_select` is not the right place to do ORDER BY optimization), but the effect is the same.

## See Also

* Blog post [MariaDB 10.1: Better query optimization for ORDER BY … LIMIT](https://s.petrunia.net/blog/?p=103)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
