---
description: MyRocks storage engine scans that only use indexes.
---

# MyRocks Index-Only Scans

This article is about [MyRocks](./) and index-only scans on secondary indexes. It applies to MariaDB's MyRocks, Facebook's MyRocks, and other variants.

## Secondary Keys Only

The primary key in MyRocks is always the clustered key, that is, the index record is THE table record and so it's not possible to do "index only" because there isn't anything that is not in the primary key's (Key,Value) pair.

Secondary keys may or may not support index-only scans, depending on the datatypes of the columns that the query is trying to read.

## Background: Mem-Comparable Keys

MyRocks indexes store "mem-comparable keys" (that is, the key values are compared with `memcmp`). For some datatypes, it is easily possible to convert between the column value and its mem-comparable form, while for others the conversion is one-way.

For example, in case-insensitive collations capital and regular letters are considered identical, i.e. 'c' ='C'. For some datatypes, MyRocks stores some extra data which allows it to restore the original value back. (For the `latin1_general_ci` [collation](../../../reference/data-types/string-data-types/character-sets/) and character 'c', for example, it will store one bit which says whether the original value was a small 'c' or a capital letter 'C'). This doesn't work for all datatypes, though.

## Index-Only Support for Various Datatypes

Index-only scans are supported for numeric and date/time datatypes. For CHAR and VAR\[CHAR], it depends on which collation is used, see below for details.

Index-only scans are currently not supported for less frequently used datatypes, like

* [BIT(n)](../../../reference/data-types/numeric-data-types/bit.md)
* [SET(...)](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md)
* [ENUM(...)](../../../reference/data-types/string-data-types/enum.md)\
  It is actually possible to add support for those, feel free to write a patch or at least make a case why a particular datatype is important

## Index-Only Support for Various Collations

As far as Index-only support is concerned, MyRocks distinguishes three kinds of collations:

### 1. Binary (Reversible) Collations

These are `binary`, `latin1_bin`, and `utf8_bin`.

For these collations, it is possible to convert a value back from its mem-comparable form. Hence, one can restore the original value back from its index record, and index-only scans are supported.

### 2. Restorable Collations

These are collations where one can store some extra information which helps to restore the original value.

Criteria (from storage/rocksdb/rdb\_datadic.cc, rdb\_is\_collation\_supported()) are:

* The charset should use 1-byte characters (so, unicode-based collations are not included)
* strxfrm(1 byte) = {one 1-byte weight value always}
* no binary sorting
* PAD attribute

The examples are: `latin1_general_ci`, `latin1_general_cs`, `latin1_swedish_ci`, etc.

Index-only scans are supported for these collations.

### 3. All Other Collations

For these collations, there is no known way to restore the value from its mem-comparable form, and so index-only scans are not supported.

MyRocks needs to fetch the clustered PK record to get the field value.

## Covering Secondary Key Lookups for VARCHARs

TODO: there is also this optimization:

[303](https://github.com/facebook/mysql-5.6/issues/303)[f349c95848e92b5b27b44f0e57194100eb0997e7](https://github.com/facebook/mysql-5.6/commit/f349c95848e92b5b27b44f0e57194100eb0997e7)

document it.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
