# Subqueries in a FROM Clause (Derived Tables)

Although [subqueries](./) are more commonly placed in a WHERE clause, they can also form part of the FROM clause. Such subqueries are commonly called derived tables.

If a subquery is used in this way, you must also use an AS clause to name the result of the subquery.

## ORACLE mode

**MariaDB starting with** [**10.6.0**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.0)

{% tabs %}
{% tab title="Current" %}
[Anonymous subqueries in a FROM clause](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle#simple-syntax-compatibility) (no AS clause) are permitted in [ORACLE mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle).
{% endtab %}

{% tab title="< 10.6" %}
[Anonymous subqueries in a FROM clause](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/subqueries/broken-reference/README.md) (no `AS` clause) are **not** permitted in [ORACLE mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle).
{% endtab %}
{% endtabs %}

## Correlation Column List

**MariaDB starting with** [**11.7.0**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-11-7-rolling-releases/mariadb-11-7-0-release-notes)

{% tabs %}
{% tab title="Current" %}
It is possible to assign column names in the derived table name syntax element.
{% endtab %}

{% tab title="< 11.7" %}
It is **not** possible to assign column names in the derived table name syntax element.
{% endtab %}
{% endtabs %}

## Examples

```sql
CREATE TABLE student (name CHAR(10), test CHAR(10), score TINYINT); 

INSERT INTO student VALUES 
  ('Chun', 'SQL', 75), ('Chun', 'Tuning', 73), 
  ('Esben', 'SQL', 43), ('Esben', 'Tuning', 31), 
  ('Kaolin', 'SQL', 56), ('Kaolin', 'Tuning', 88), 
  ('Tatiana', 'SQL', 87), ('Tatiana', 'Tuning', 83);
```

Assume that, given the data above, you want to return the average total for all students. In other words, the average of Chun's 148 (75+73), Esben's 74 (43+31), etc.

You cannot do the following:

```sql
SELECT AVG(SUM(score)) FROM student GROUP BY name;
ERROR 1111 (HY000): Invalid use of group function
```

A subquery in the FROM clause is however permitted:

```sql
SELECT AVG(sq_sum) FROM (SELECT SUM(score) AS sq_sum FROM student GROUP BY name) AS t;
+-------------+
| AVG(sq_sum) |
+-------------+
|    134.0000 |
+-------------+
```

The following is permitted:

```sql
SELECT * FROM (SELECT 1 FROM DUAL), (SELECT 2 FROM DUAL);
```

In this example, the second column of the derived table `dt` is used both within (`WHERE` c2 > 0), and outside, (`WHERE` a2 > 10), the specification. Both conditions apply to t1.c2.

```sql
CREATE OR REPLACE TABLE t1(c1 INT, c2 INT, c3 INT);

SELECT a1, a2 FROM (SELECT c1, c2, c3 FROM t1 WHERE c2 > 0) AS dt (a1, a2, a3);
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
