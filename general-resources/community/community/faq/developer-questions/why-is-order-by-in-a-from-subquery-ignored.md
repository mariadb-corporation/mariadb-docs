# Why is ORDER BY in a FROM Subquery Ignored?

Query with ORDER BY in a FROM subquery produces unordered result. Is this a bug?\
Below is an example of this:

```sql
SELECT field1, field2 FROM ( SELECT field1, field2 FROM table1 ORDER BY field2 ) ALIAS
```

returns a result set that is not necessarily ordered by field2. This is not a bug.

A "table" (and subquery in the `FROM` clause too) is - according to the SQL standard - an unordered set of rows. Rows in a table (or in a subquery in the `FROM` clause) do not come in any specific order. That's why the optimizer can ignore the [ORDER BY](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/order-by) clause that you have specified. In fact, the SQL standard does not even allow the `ORDER BY` clause to appear in this subquery (we allow it, because `ORDER BY ... LIMIT ...` changes the result, the set of rows, not only their order).

You need to treat the subquery in the `FROM` clause, as a set of rows in some unspecified and undefined order, and put the `ORDER BY` on the top-level `SELECT`.

Source: [MDEV-3926, Comment by Sergei Golubchik](https://jira.mariadb.org/browse/MDEV-3926?focusedCommentId=28800\&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-28800)

## See also

* [MDEV-3926](https://jira.mariadb.org/browse/MDEV-3926), [MDEV-5007](https://jira.mariadb.org/browse/MDEV-5007), [MDEV-3795](https://jira.mariadb.org/browse/MDEV-3795).
* [SELECT](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select)
* [ORDER BY](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/order-by)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
