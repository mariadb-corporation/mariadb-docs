# Primary Keys with Nullable Columns

MariaDB deals with primary keys over nullable columns according to the SQL standards.

Take the following table structure:

```sql
CREATE TABLE t1(
  c1 INT NOT NULL AUTO_INCREMENT, 
  c2 INT NULL DEFAULT NULL, 
  PRIMARY KEY(c1,c2)
);
```

Column c2 is part of a primary key, and thus it cannot be [NULL](../../../reference/data-types/null-values.md).

Before [MariaDB 10.1.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.7), MariaDB (as well as versions of MySQL before MySQL 5.7) would silently convert it into a NOT NULL column with a default value of _0_.

Since [MariaDB 10.1.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.7), the column is converted to NOT NULL, but without a default value. If we then attempt to insert a record without explicitly setting _c2_, a warning (or, in strict mode, an error), will be thrown, for example:

```sql
INSERT INTO t1() VALUES();
Query OK, 1 row affected, 1 warning (0.00 sec)
Warning (Code 1364): Field 'c2' doesn't have a default value

SELECT * FROM t1;
+----+----+
| c1 | c2 |
+----+----+
|  1 |  0 |
+----+----+
```

MySQL, since 5.7, will abort such a CREATE TABLE with an error.

The [MariaDB 10.1.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.7) behavior adheres to the SQL 2003 standard.

SQL-2003, Part II, “Foundation” says:

\*\*11.7 \*\***Syntax Rules**

…

_5) If the specifies PRIMARY KEY, then for each in the explicit or implicit for which NOT NULL is not specified, NOT NULL is implicit in the ._

Essentially this means that all PRIMARY KEY columns are automatically converted to NOT NULL. Furthermore:

**11.5 General Rules**

…

_3) When a site S is set to its default value,_

…

_b) If the data descriptor for the site includes a , then S is set to the value specified by that ._

…

_e) Otherwise, S is set to the null value._

There is no concept of “no default value” in the standard. Instead, a column always has an implicit default value of NULL. On insertion it might however fail the NOT NULL constraint. MariaDB and MySQL instead mark such a column as “not having a default value”. The end result is the same — a value must be specified explicitly or an INSERT will fail.

MariaDB since 10.1.7 behaves in a standard compatible manner — being part of a PRIMARY KEY, the nullable column gets an automatic NOT NULL constraint, on insertion one must specify a value for such a column. MariaDB before 10.1.7 was automatically assigning a default value of 0 — this behavior was non-standard. Issuing an error at CREATE TABLE time is also non-standard.

## See Also

* [MDEV-12248](https://jira.mariadb.org/browse/MDEV-12248) describes an edge-case that may result in replication problems when replicating from a master server before this change to a slave server after this change.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
