---
description: >-
  Learn how to configure and use Bloom filters in MyRocks to speed up point
  lookups by probabilistically determining if a key exists in a data file.
---

# MyRocks Bloom Filters

Bloom filters are used to reduce read amplification. Bloom filters can be set on a per-column family basis (see [myrocks-column-families](myrocks-column-families.md)).

## Bloom Filter Parameters

* How many bits to use
* whole\_key\_filtering=true/false
* Whether the bloom filter is for the entire key or for the prefix. In case of a prefix, you need to look at the index definition and compute the desired prefix length.

### Computing Prefix Length

* It's 4 bytes for `index_nr`
* Then, for fixed-size columns (integer, date\[time], decimal) it is key\_length as shown by `EXPLAIN`. For VARCHAR columns, determining the length is tricky (It depends on the values stored in the table. Note that MyRocks encodes VARCHARs with "Variable-Length Space-Padded Encoding" format).

## Configuring Bloom Filter

To enable 10-bit bloom filter for 8-byte prefix length for column family "cf1", put this into my.cnf:

```
rocksdb_override_cf_options='cf1={block_based_table_factory={filter_policy=bloomfilter:10:false;whole_key_filtering=0;};prefix_extractor=capped:8};'
```

and restart the server.

Check if the column family actually uses the bloom filter:

```sql
SELECT * 
FROM information_schema.rocksdb_cf_options 
WHERE 
  cf_name='cf1' AND
  option_type IN ('TABLE_FACTORY::FILTER_POLICY','PREFIX_EXTRACTOR');
```

```
+---------+------------------------------+----------------------------+
| CF_NAME | OPTION_TYPE                  | VALUE                      |
+---------+------------------------------+----------------------------+
| cf1     | PREFIX_EXTRACTOR             | rocksdb.CappedPrefix.8     |
| cf1     | TABLE_FACTORY::FILTER_POLICY | rocksdb.BuiltinBloomFilter |
+---------+------------------------------+----------------------------+
```

## Checking if Bloom Filter is Useful

Watch these status variables:

```sql
SHOW status LIKE '%bloom%';
+-------------------------------------+-------+
| Variable_name                       | Value |
+-------------------------------------+-------+
| Rocksdb_bloom_filter_prefix_checked | 1     |
| Rocksdb_bloom_filter_prefix_useful  | 0     |
| Rocksdb_bloom_filter_useful         | 0     |
+-------------------------------------+-------+
```

Other useful variables are:

* `rocksdb_force_flush_memtable_now` - bloom filter is only used when reading data from disk. If you are doing testing, flush the data to disk first.
* `rocksdb_skip_bloom_filter_on_read` - skip using the bloom filter (default is FALSE).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
