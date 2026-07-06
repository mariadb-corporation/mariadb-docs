---
description: >-
  Using IGNORE INDEX to tell the optimizer not to consider specific indexes.
---

# IGNORE INDEX

## Syntax

```bnf
IGNORE INDEX [{FOR {JOIN|ORDER BY|GROUP BY}] ([index_list])
```

## Description

You can tell the optimizer to not consider a particular index with the IGNORE INDEX option.

The benefit of using IGNORE\_INDEX instead of [USE\_INDEX](use-index.md) is that it will not disable a new index which you may add later.

Also see [Ignored Indexes](../optimization-and-indexes/ignored-indexes.md) for an option to specify in the index definition that indexes should be ignored.

### Index Prefixes

When using index hints (USE, FORCE or IGNORE INDEX), the index name value can also be an unambiguous prefix of an index name.

## Example

This is used after the table name in the FROM clause:

```sql
CREATE INDEX Name ON City (Name);
CREATE INDEX CountryCode ON City (Countrycode);
EXPLAIN SELECT Name FROM City IGNORE INDEX (Name)
WHERE name="Helsingborg" AND countrycode="SWE";
```

This produces:

```
id	select_type	table	type	possible_keys	key	key_len	ref	rows	Extra
1	SIMPLE	City	ref	CountryCode	CountryCode	3	const	14	Using where
```

## See Also

* See [Index Hints: How to Force Query Plans](index-hints-how-to-force-query-plans.md) for more details
* [USE INDEX](use-index.md)
* [FORCE INDEX](force-index.md)
* [Ignored Indexes](../optimization-and-indexes/ignored-indexes.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
