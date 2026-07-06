---
description: >-
  The EXPLAIN Analyzer was an online tool for analyzing and sharing EXPLAIN
  output. It is no longer active.
---

# EXPLAIN Analyzer

{% hint style="warning" %}
The `EXPLAIN` Analyzer is no longer active.
{% endhint %}

The EXPLAIN Analyzer was an online tool for analyzing and optionally sharing the output of both `EXPLAIN` and `EXPLAIN EXTENDED`.

### Using the Analyzer

Using the analyzer is very simple.

In the mariadb client, run `EXPLAIN` on a query and copy the output. For example:

```sql
EXPLAIN SELECT * FROM t1 INNER JOIN t2 INNER JOIN t3 WHERE t1.a=t2.a AND t2.a=t3.a;
+------+-------------+-------+------+---------------+------+---------+------+------+--------------------------------------------------------+
| id   | select_type | table | type | possible_keys | key  | key_len | ref  | rows | Extra                                                  |
+------+-------------+-------+------+---------------+------+---------+------+------+--------------------------------------------------------+
|    1 | SIMPLE      | t1    | ALL  | NULL          | NULL | NULL    | NULL |    3 |                                                        |
|    1 | SIMPLE      | t2    | ALL  | NULL          | NULL | NULL    | NULL |    3 | Using where; Using join buffer (flat, BNL join)        |
|    1 | SIMPLE      | t3    | ALL  | NULL          | NULL | NULL    | NULL |    3 | Using where; Using join buffer (incremental, BNL join) |
+------+-------------+-------+------+---------------+------+---------+------+------+--------------------------------------------------------+
3 rows in set (0.00 sec)
```

1. Paste the output into the [EXPLAIN Analyzer input box](https://mariadb.org/explain_analyzer/analyze/) and click the "Analyze Explain" button.
2. The formatted `EXPLAIN` is shown. You can now click on various part to get more information about them.

#### Some Notes:

* As you can see in the example above, you don't need to chop off the query line or the command prompt.
* To save the EXPLAIN, so you can share it, or just for future reference, click the "Save Explain for analysis and sharing" button and then click the "Analyze Explain" button. You is given a link which leads to your saved `EXPLAIN`. For example, the above explain can be viewed here:
* Some of the elements in the formatted `EXPLAIN` are clickable. Clicking on them will show pop-up help related to that element.

### Clients which integrate with the Explain Analyzer

The Analyzer has an API that client programs can use to send EXPLAINs. If you are a client application developer, see the EXPLAIN Analyzer API page for details.

The following clients have support for the EXPLAIN Analyzer built in:

#### HeidiSQL

[HeidiSQL](https://www.heidisql.com/) has a button when viewing a query that sends the query to the explain analyzer.

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
