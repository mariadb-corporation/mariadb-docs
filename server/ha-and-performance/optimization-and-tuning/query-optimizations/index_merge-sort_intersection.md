# index\_merge sort\_intersection

Prior to [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.3/changes-improvements-in-mariadb-5-3), the `index_merge` access method supported `union`,`sort-union`, and `intersection` operations. Starting from [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.3/changes-improvements-in-mariadb-5-3), the`sort-intersection` operation is also supported. This allows the use of`index_merge` in a broader number of cases.

This feature is disabled by default. To enable it, turn on the optimizer switch `index_merge_sort_intersection` like so:

```sql
SET optimizer_switch='index_merge_sort_intersection=on'
```

## Limitations of index\_merge/intersection

Prior to [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.3/changes-improvements-in-mariadb-5-3), the `index_merge` access method had one intersection strategy called `intersection`. That strategy can only be used when merged index scans produced rowid-ordered streams. In practice this means that an`intersection` could only be constructed from equality (=) conditions.

For example, the following query will use `intersection`:

```sql
MySQL [ontime]> EXPLAIN SELECT AVG(arrdelay) FROM ontime WHERE depdel15=1 AND OriginState ='CA';
+--+-----------+------+-----------+--------------------+--------------------+-------+----+-----+-------------------------------------------------+
|id|select_type|table |type       |possible_keys       |key                 |key_len|ref |rows |Extra                                            |
+--+-----------+------+-----------+--------------------+--------------------+-------+----+-----+-------------------------------------------------+
| 1|SIMPLE     |ontime|index_merge|OriginState,DepDel15|OriginState,DepDel15|3,5    |NULL|76952|Using intersect(OriginState,DepDel15);Using where|
+--+-----------+------+-----------+--------------------+--------------------+-------+----+-----+-------------------------------------------------+
```

but if you replace `OriginState ='CA'` with `OriginState IN ('CA', 'GB')` (which matches the same number of records), then `intersection` is not usable anymore:

```sql
MySQL [ontime]> EXPLAIN SELECT avg(arrdelay) FROM ontime where depdel15=1 and OriginState IN ('CA', 'GB');
+--+-----------+------+----+--------------------+--------+-------+-----+-----+-----------+
|id|select_type|table |type|possible_keys       |key     |key_len|ref  |rows |Extra      |
+--+-----------+------+----+--------------------+--------+-------+-----+-----+-----------+
| 1|SIMPLE     |ontime|ref |OriginState,DepDel15|DepDel15|5      |const|36926|Using where|
+--+-----------+------+----+--------------------+--------+-------+-----+-----+-----------+
```

The latter query would also run 5.x times slower (from 2.2 to 10.8 seconds) in our experiments.

## How index\_merge/sort\_intersection improves the situation

In [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.3/changes-improvements-in-mariadb-5-3), when `index_merge_sort_intersection` is enabled,`index_merge` intersection plans can be constructed from non-equality\
conditions:

```sql
MySQL [ontime]> EXPLAIN SELECT avg(arrdelay) FROM ontime where depdel15=1 and OriginState IN ('CA', 'GB');
+--+-----------+------+-----------+--------------------+--------------------+-------+----+-----+--------------------------------------------------------+
|id|select_type|table |type       |possible_keys       |key                 |key_len|ref |rows |Extra                                                   |
+--+-----------+------+-----------+--------------------+--------------------+-------+----+-----+--------------------------------------------------------+
| 1|SIMPLE     |ontime|index_merge|OriginState,DepDel15|DepDel15,OriginState|5,3    |NULL|60754|Using sort_intersect(DepDel15,OriginState); Using where |
+--+-----------+------+-----------+--------------------+--------------------+-------+----+-----+--------------------------------------------------------+
```

In our tests, this query ran in 3.2 seconds, which is not as good as the case with two equalities, but still much better than 10.8 seconds we were getting without `sort_intersect`.

The `sort_intersect` strategy has higher overhead than `intersect` but is able to handle a broader set of `WHERE` conditions.

![intersect-vs-sort-intersect](../../../.gitbook/assets/intersect-vs-sort-intersect.png)

## When to Use

`index_merge/sort_intersection` works best on tables with lots of records and where intersections are sufficiently large (but still small enough to make a full table scan overkill).

The benefit is expected to be bigger for io-bound loads.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
