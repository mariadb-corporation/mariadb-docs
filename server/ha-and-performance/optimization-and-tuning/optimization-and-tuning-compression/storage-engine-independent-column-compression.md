---
description: >-
  Storage-engine-independent compression for BLOB and TEXT columns,
  independent of the storage engine.
---

# Storage-Engine Independent Column Compression

Storage-engine independent column compression enables [TINYBLOB](../../../reference/data-types/string-data-types/tinyblob.md), [BLOB](../../../reference/data-types/string-data-types/blob.md), [MEDIUMBLOB](../../../reference/data-types/string-data-types/mediumblob.md), [LONGBLOB](../../../reference/data-types/string-data-types/longblob.md), [TINYTEXT](../../../reference/data-types/string-data-types/tinytext.md), [TEXT](../../../reference/data-types/string-data-types/text.md), [MEDIUMTEXT](../../../reference/data-types/string-data-types/mediumtext.md), [LONGTEXT](../../../reference/data-types/string-data-types/longtext.md), [VARCHAR](../../../reference/data-types/string-data-types/varchar.md) and [VARBINARY](../../../reference/data-types/string-data-types/varbinary.md) columns to be compressed.

This is performed by means of a new COMPRESSED [column attribute](../../../reference/sql-statements/data-definition/create/create-table.md#column-and-index-definitions):`COMPRESSED[=<compression_method>]`

Currently the only supported compression method is `zlib`.

### Field Length Compatibility

When using the `COMPRESSED` attribute, note that FIELD LENGTH is reduced by 1; for example, a BLOB has a length of 65535, while BLOB COMPRESSED has 65535-1. See [MDEV-15592](https://jira.mariadb.org/browse/MDEV-15592).

### New System Variables

#### `column_compression_threshold`

* Description: Minimum column data length eligible for compression.
* Command line: `--column-compression-threshold=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `100`
* Range: `0` to `4294967295`

#### `column_compression_zlib_level`

* Description: zlib compression level (1 gives best speed, 9 gives best compression).
* Command line: `--column-compression-zlib-level=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `6`
* Range: `1` to `9`

#### `column_compression_zlib_strategy`

* Description: The strategy parameter is used to tune the compression algorithm. Use the value `DEFAULT_STRATEGY` for normal data, `FILTERED` for data produced by a filter (or predictor), `HUFFMAN_ONLY` to force Huffman encoding only (no string match), or `RLE` to limit match distances to one (run-length encoding). Filtered data consists mostly of small values with a somewhat random distribution. In this case, the compression algorithm is tuned to compress them better. The effect of `FILTERED` is to force more Huffman coding and less string matching; it is somewhat intermediate between `DEFAULT_STRATEGY` and `HUFFMAN_ONLY`. `RLE` is designed to be almost as fast as `HUFFMAN_ONLY`, but give better compression for PNG image data. The strategy parameter only affects the compression ratio but not the correctness of the compressed output even if it is not set appropriately. `FIXED` prevents the use of dynamic Huffman codes, allowing for a simpler decoder for special applications.
* Command line: `--column-compression-zlib-strategy=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `enum`
* Default Value: `DEFAULT_STRATEGY`
* Valid Values: `DEFAULT_STRATEGY`, `FILTERED`, `HUFFMAN_ONLY`, `RLE`, `FIXED`

#### `column_compression_zlib_wrap`

* Description: If set to `1` (`0` is default), generate zlib header and trailer and compute adler32 check value. It can be used with storage engines that don't provide data integrity verification to detect data corruption.
* Command line: `--column-compression-zlib-wrap{=0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

### New Status Variables

#### `Column_compressions`

* Description: Incremented each time field data is compressed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Column_decompressions`

* Description: Incremented each time field data is decompressed.
* Scope: Global, Session
* Data Type: `numeric`

### Limitations

* The only supported method currently is zlib.
* The [CSV](../../../server-usage/storage-engines/csv/) storage engine stores data uncompressed on-disk even if the COMPRESSED attribute is present.
* It is not possible to create indexes over compressed columns.

### Comparison with InnoDB Page Compression

Storage-independent column compression is different to [InnoDB Page Compression](../../../server-usage/storage-engines/innodb/innodb-page-compression.md) in a number of ways.

* It is storage engine independent, while InnoDB page compression applies to InnoDB only.
* By being specific to a column, one can access non-compressed fields without the decompression overhead.
* Only zlib is available, while InnoDB page compression can offer alternative compression algorithms.
* It is not recommended to use multiple forms of compression over the same data.
* It is intended for compressing large blobs, while InnoDB page compression is suitable for a more general case.
* Columns cannot be indexed, while with InnoDB page compression indexes are possible as usual.

### Examples

```sql
CREATE TABLE cmp (i TEXT COMPRESSED);

CREATE TABLE cmp2 (i TEXT COMPRESSED=zlib);
```

### See Also

* [InnoDB Page Compression](../../../server-usage/storage-engines/innodb/innodb-page-compression.md)
* [InnoDB Compressed Row Format](../../../server-usage/storage-engines/innodb/innodb-row-formats/innodb-compressed-row-format.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
