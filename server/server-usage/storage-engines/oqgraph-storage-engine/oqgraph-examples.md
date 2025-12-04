---
description: >-
  Practical examples demonstrating how to create OQGRAPH tables and perform
  graph operations like finding shortest paths and leaf nodes.
---

# OQGRAPH Examples

## Creating a Table with origid, destid Only

```sql
CREATE TABLE oq_backing (
  origid INT UNSIGNED NOT NULL, 
  destid INT UNSIGNED NOT NULL,  
  PRIMARY KEY (origid, destid), 
  KEY (destid)
);
```

Some data can be inserted into the backing table to test with later:

```sql
INSERT INTO oq_backing(origid, destid) 
 VALUES (1,2), (2,3), (3,4), (4,5), (2,6), (5,6);
```

Now the read-only [OQGRAPH](./) table is created.

You can use the following syntax:

```sql
CREATE TABLE oq_graph
ENGINE=OQGRAPH 
data_table='oq_backing' origid='origid' destid='destid';
```

## Creating a Table with Weight

For the examples on this page, we'll create a second OQGRAPH table and backing table, this time with `weight` as well.

```sql
CREATE TABLE oq2_backing (
  origid INT UNSIGNED NOT NULL, 
  destid INT UNSIGNED NOT NULL, 
  weight DOUBLE NOT NULL, 
  PRIMARY KEY (origid, destid), 
  KEY (destid)
);
```

```sql
INSERT INTO oq2_backing(origid, destid, weight)  
 VALUES (1,2,1), (2,3,1), (3,4,3), (4,5,1), (2,6,10), (5,6,2);
```

```sql
CREATE TABLE oq2_graph (
  latch VARCHAR(32) NULL,
  origid BIGINT UNSIGNED NULL,
  destid BIGINT UNSIGNED NULL,
  weight DOUBLE NULL,
  seq BIGINT UNSIGNED NULL,
  linkid BIGINT UNSIGNED NULL,
  KEY (latch, origid, destid) USING HASH,
  KEY (latch, destid, origid) USING HASH
) 
ENGINE=OQGRAPH 
data_table='oq2_backing' origid='origid' destid='destid' weight='weight';
```

## Shortest Path

A `latch` value of `'dijkstras'` and an `origid` and `destid` is used for finding the shortest path between two nodes, for example:

```sql
SELECT * FROM oq_graph WHERE latch='breadth_first' AND origid=1 AND destid=6;
+----------+--------+--------+--------+------+--------+
| latch    | origid | destid | weight | seq  | linkid |
+----------+--------+--------+--------+------+--------+
| dijkstras|      1 |      6 |   NULL |    0 |      1 |
| dijkstras|      1 |      6 |      1 |    1 |      2 |
| dijkstras|      1 |      6 |      1 |    2 |      6 |
+----------+--------+--------+--------+------+--------+
```

Note that nodes are uni-directional, so there is no path from node 6 to node 1:

```sql
SELECT * FROM oq_graph WHERE latch='dijkstras' AND origid=6 AND destid=1;
Empty set (0.00 sec)
```

Using the [GROUP\_CONCAT](../../../reference/sql-functions/aggregate-functions/group_concat.md) function can produce more readable results, for example:

```sql
SELECT GROUP_CONCAT(linkid ORDER BY seq) AS path FROM oq_graph 
 WHERE latch='dijkstras' AND origid=1 AND destid=6;
+-------+
| path  |
+-------+
| 1,2,6 |
+-------+
```

Using the table `oq2_graph`, the shortest path is different:

```sql
SELECT GROUP_CONCAT(linkid ORDER BY seq) AS path FROM oq2_graph 
 WHERE latch='dijkstras' AND origid=1 AND destid=6;
+-------------+
| path        |
+-------------+
| 1,2,3,4,5,6 |
+-------------+
```

The reason is the weight between nodes 2 and 6 is `10` in `oq_graph2`, so the shortest path taking into account `weight` is now across more nodes.

## Possible Destinations

```sql
SELECT GROUP_CONCAT(linkid) AS dests FROM oq_graph WHERE latch='dijkstras' AND origid=2;
+-----------+
| dests     |
+-----------+
| 5,4,6,3,2 |
+-----------+
```

Note that this returns all possible destinations along the path, not just immediate links.

## Leaf Nodes

MariaDB supports the `leaves` latch value. A `latch` value of `'leaves'` and either `origid` or `destid` is used for finding leaf nodes at the beginning or end of a graph.

```sql
INSERT INTO oq_backing(origid, destid)  
 VALUES (1,2), (2,3), (3,5), (4,5), (5,6), (6,7), (6,8), (2,8);
```

For example, to find all reachable nodes from `origid` that only have incoming edges:

```sql
SELECT * FROM oq_graph WHERE latch='leaves' AND origid=2;
+--------+--------+--------+--------+------+--------+
| latch  | origid | destid | weight | seq  | linkid |
+--------+--------+--------+--------+------+--------+
| leaves |      2 |   NULL |      4 |    2 |      7 |
| leaves |      2 |   NULL |      1 |    1 |      8 |
+--------+--------+--------+--------+------+--------+
```

And to find all nodes from which a path can be found to `destid` that only have outgoing edges:

```sql
SELECT * FROM oq_graph WHERE latch='leaves' AND destid=5;
+--------+--------+--------+--------+------+--------+
| latch  | origid | destid | weight | seq  | linkid |
+--------+--------+--------+--------+------+--------+
| leaves |   NULL |      5 |      3 |    2 |      1 |
| leaves |   NULL |      5 |      1 |    1 |      4 |
+--------+--------+--------+--------+------+--------+
```

## Summary of Implemented Latch Commands

| Latch          | Alternative   | additional where clause fields | Graph operation                                                                                                                                              |
| -------------- | ------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| NULL           | (unspecified) | (none)                         | List original data                                                                                                                                           |
| (empty string) | 0             | (none extra)                   | List all vertices in linkid column                                                                                                                           |
| (empty string) | 0             | origid                         | List all first hop vertices from origid in linkid column                                                                                                     |
| dijkstras      | 1             | origid, destid                 | Find shortest path using Dijkstras algorithm between origid and destid, with traversed vertex ids in linkid column                                           |
| dijkstras      | 1             | origid                         | Find all vertices reachable from origid, listed in linkid column, and report sum of weights of vertices on path to given vertex in weight                    |
| dijkstras      | 1             | destid                         | Find all vertices from which a path can be found to destid, listed in linkid column, and report sum of weights of vertices on path to given vertex in weight |
| breadth\_first | 2             | origid                         | List vertices reachable from origid in linkid column                                                                                                         |
| breadth\_first | 2             | destid                         | List vertices from which a path can be found to destid in linkid column                                                                                      |
| breadth\_first | 2             | origid, destid                 | Find shortest path between origid and destid, report in linkid column                                                                                        |
| leaves         | 4             | origid                         | List vertices reachable from origid, that only have incoming edges                                                                                           |
| leaves         | 4             | destid                         | List vertices from which a path can be found to destid, that only have outgoing edges                                                                        |
| leaves         | 4             | origid, destid                 | Not supported, will return an empty result                                                                                                                   |

#### Note

The use of integer latch commands is deprecated and may be phased out in a future release. Currently, numeric values in the strings are interpreted as aliases, and use of an integer column can be optionally allowed, for the latch commands column.

The use of integer latches is controlled using the [oqgraph\_allow\_create\_integer\_latch](../../../ha-and-performance/optimization-and-tuning/system-variables/oqgraph-system-and-status-variables.md#oqgraph_allow_create_integer_latch) system variable.

## See Also

* [OQGRAPH Overview](oqgraph-overview.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
