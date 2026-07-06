---
description: >-
  The rowid filtering optimization, which pre-filters rowids to reduce
  expensive row lookups.
---

# Rowid Filtering Optimization

The target use case for rowid filtering is as follows:

* a table uses ref access on index IDX1
* but it also has a fairly restrictive range predicate on another index IDX2.

In this case, it is advantageous to:

* Do an index-only scan on index IDX2 and collect rowids of index records into a data structure that allows filtering (let's call it $FILTER).
* When doing ref access on IDX1, check $FILTER before reading the full record.

## Example

Consider a query

```sql
SELECT ...
FROM orders JOIN lineitem ON o_orderkey=l_orderkey
WHERE
  l_shipdate BETWEEN '1997-01-01' AND '1997-01-31' AND
  o_totalprice between 200000 and 230000;
```

Suppose the condition on `l_shipdate` is very restrictive, which means lineitem table should go first in the join order. Then, the optimizer can use `o_orderkey=l_orderkey` equality to do an index lookup to get the order the line item is from. On the other hand `o_totalprice between ...` can also be rather selective.

With filtering, the query plan would be:

```sql
*************************** 1. row ***************************
           id: 1
  select_type: SIMPLE
        table: lineitem
         type: range
possible_keys: PRIMARY,i_l_shipdate,i_l_orderkey,i_l_orderkey_quantity
          key: i_l_shipdate
      key_len: 4
          ref: NULL
         rows: 98
        Extra: Using index condition
*************************** 2. row ***************************
           id: 1
  select_type: SIMPLE
        table: orders
         type: eq_ref|filter
possible_keys: PRIMARY,i_o_totalprice
          key: PRIMARY|i_o_totalprice
      key_len: 4|9
          ref: dbt3_s001.lineitem.l_orderkey
         rows: 1 (5%)
        Extra: Using where; Using rowid filter
```

Note that table `orders` has "Using rowid filter". The `type` column has `"|filter"`, the `key` column shows the index that is used to construct the filter. `rows` column shows the expected filter selectivity, it is 5%.

ANALYZE FORMAT=JSON output for table orders will show

```json
"table": {
      "table_name": "orders",
      "access_type": "eq_ref",
      "possible_keys": ["PRIMARY", "i_o_totalprice"],
      "key": "PRIMARY",
      "key_length": "4",
      "used_key_parts": ["o_orderkey"],
      "ref": ["dbt3_s001.lineitem.l_orderkey"],
      "rowid_filter": {
        "range": {
          "key": "i_o_totalprice",
          "used_key_parts": ["o_totalprice"]
        },
        "rows": 69,
        "selectivity_pct": 4.6,
        "r_rows": 71,
        "r_selectivity_pct": 10.417,
        "r_buffer_size": 53,
        "r_filling_time_ms": 0.0716
      }
```

Note the `rowid_filter` element. It has a `range` element inside it. `selectivity_pct` is the expected selectivity, accompanied by the `r_selectivity_pct` showing the actual observed selectivity.

## Details

* The optimizer makes a cost-based decision about when the filter should be used.
* The filter data structure is currently an ordered array of rowids. (a Bloom filter would be better here and will probably be introduced in the future versions).
* The optimization needs to be supported by the storage engine. At the moment, it is supported by [InnoDB](../../../server-usage/storage-engines/innodb/) and [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/). It is not supported in [partitioned tables](../../../server-usage/partitioning-tables/).

## Limitations

* Rowid Filtering can't be used with a backward-ordered index scan. When the optimizer needs to execute an ORDER BY ... DESC query and decides to handle it with a backward-ordered index scan, it will disable Rowid Filtering.

## Control

Rowid filtering can be switched on/off using `rowid_filter` flag in the [optimizer\_switch](../system-variables/server-system-variables.md#optimizer_switch) variable. By default, the optimization is enabled.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
