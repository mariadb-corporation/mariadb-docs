---
description: >-
  Using FORCE INDEX to make the optimizer use an index instead of a table
  scan.
---

# FORCE INDEX

## Description

Forcing an index to be used is mostly useful when the optimizer decides to do a table scan even if you know that using an index would be better. (The optimizer could decide to do a table scan even if there is an available index when it believes that most or all rows will match and it can avoid the overhead of using the index).

FORCE INDEX works by only considering the given indexes (like with USE\_INDEX) but in addition it tells the optimizer to regard a table scan as something very expensive. However if none of the 'forced' indexes can be used, then a table scan will be used anyway.

FORCE INDEX cannot force an [ignored index](../optimization-and-indexes/ignored-indexes.md) to be used - it will be treated as if it doesn't exist.

## Example

```sql
CREATE INDEX Name ON City (Name);
EXPLAIN SELECT Name,CountryCode FROM City FORCE INDEX (Name)
WHERE name>="A" AND CountryCode >="A";
```

This produces:

```sql
id	select_type	table	type	possible_keys	key	key_len	ref	rows	Extra
1	SIMPLE	City	range	Name	Name	35	NULL	4079	Using where
```

### Index Prefixes

When using index hints (USE, FORCE or IGNORE INDEX), the index name value can also be an unambiguous prefix of an index name.

## See Also

* [Index Hints: How to Force Query Plans](index-hints-how-to-force-query-plans.md) for more details
* [USE INDEX](use-index.md)
* [IGNORE INDEX](ignore-index.md)
* [Ignored Indexes](../optimization-and-indexes/ignored-indexes.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
