---
description: >-
  Inspect histogram data. This function allows viewing the distribution
  statistics stored in a histogram for query optimization analysis.
---

# DECODE\_HISTOGRAM

## Syntax

```sql
DECODE_HISTOGRAM(hist_type,histogram)
```

## Description

Returns a string of comma separated numeric values corresponding to a probability distribution represented by the histogram of type `hist_type` (`SINGLE_PREC_HB` or `DOUBLE_PREC_HB`). The `hist_type` and `histogram` would be commonly used from the [mysql.column\_stats table](../../../system-tables/the-mysql-database-tables/mysql-column_stats-table.md).

See [Histogram Based Statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/histogram-based-statistics.md) for details.

## Examples

```sql
CREATE TABLE origin (
  i INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  v INT UNSIGNED NOT NULL
);

INSERT INTO origin(v) VALUES 
  (1),(2),(3),(4),(5),(10),(20),
  (30),(40),(50),(60),(70),(80),
  (90),(100),(200),(400),(800);

SET histogram_size=10,histogram_type=SINGLE_PREC_HB;

ANALYZE TABLE origin PERSISTENT FOR ALL;
+-------------+---------+----------+-----------------------------------------+
| Table       | Op      | Msg_type | Msg_text                                |
+-------------+---------+----------+-----------------------------------------+
| test.origin | analyze | status   | Engine-independent statistics collected |
| test.origin | analyze | status   | OK                                      |
+-------------+---------+----------+-----------------------------------------+

SELECT db_name,table_name,column_name,hist_type,
  hex(histogram),decode_histogram(hist_type,histogram) 
  FROM mysql.column_stats WHERE db_name='test' and table_name='origin';
+---------+------------+-------------+----------------+----------------------+-------------------------------------------------------------------+
| db_name | table_name | column_name | hist_type      | hex(histogram)       | decode_histogram(hist_type,histogram)                             |
+---------+------------+-------------+----------------+----------------------+-------------------------------------------------------------------+
| test    | origin     | i           | SINGLE_PREC_HB | 0F2D3C5A7887A5C3D2F0 | 0.059,0.118,0.059,0.118,0.118,0.059,0.118,0.118,0.059,0.118,0.059 |
| test    | origin     | v           | SINGLE_PREC_HB | 000001060C0F161C1F7F | 0.000,0.000,0.004,0.020,0.024,0.012,0.027,0.024,0.012,0.376,0.502 |
+---------+------------+-------------+----------------+----------------------+-------------------------------------------------------------------+

SET histogram_size=20,histogram_type=DOUBLE_PREC_HB;

ANALYZE TABLE origin PERSISTENT FOR ALL;
+-------------+---------+----------+-----------------------------------------+
| Table       | Op      | Msg_type | Msg_text                                |
+-------------+---------+----------+-----------------------------------------+
| test.origin | analyze | status   | Engine-independent statistics collected |
| test.origin | analyze | status   | OK                                      |
+-------------+---------+----------+-----------------------------------------+

SELECT db_name,table_name,column_name,
  hist_type,hex(histogram),decode_histogram(hist_type,histogram) 
  FROM mysql.column_stats WHERE db_name='test' and table_name='origin';
+---------+------------+-------------+----------------+------------------------------------------+-----------------------------------------------------------------------------------------+
| db_name | table_name | column_name | hist_type      | hex(histogram)                           | decode_histogram(hist_type,histogram)                                                   |
+---------+------------+-------------+----------------+------------------------------------------+-----------------------------------------------------------------------------------------+
| test    | origin     | i           | DOUBLE_PREC_HB | 0F0F2D2D3C3C5A5A78788787A5A5C3C3D2D2F0F0 | 0.05882,0.11765,0.05882,0.11765,0.11765,0.05882,0.11765,0.11765,0.05882,0.11765,0.05882 |
| test    | origin     | v           | DOUBLE_PREC_HB | 5200F600480116067E0CB30F1B16831CB81FD67F | 0.00125,0.00250,0.00125,0.01877,0.02502,0.01253,0.02502,0.02502,0.01253,0.37546,0.50063 |
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
