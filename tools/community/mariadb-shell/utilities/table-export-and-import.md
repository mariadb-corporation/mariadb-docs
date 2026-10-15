---
description: >-
  Export a MariaDB table to a delimited text file with util.export_table(),
  and load delimited or JSON files into a table in parallel with
  util.import_table().
---

# Table Export and Import

`util.export_table()` writes the rows of one table to a single text file, and `util.import_table()` loads one or more text files into a table. Together they cover data exchange with spreadsheets, other databases, and ETL tools, and they move one table between servers without a full dump.

* `util.export_table()` reads the table with a `SELECT` and writes the rows in a delimited format, such as tab-separated values or CSV. It writes only data, never DDL.
* `util.import_table()` sends the file to the server with `LOAD DATA LOCAL INFILE`. A large file is split into chunks that several connections load at the same time, which is considerably faster than a single `LOAD DATA` statement.

To back up or copy whole schemas with their DDL, use the [dump and load utilities](dump-and-load/) instead.

## Requirements

Both utilities need an open global session. The additional connections they open use the connection options of that session, such as TLS and compression settings.

| Utility | Privileges on the target table | Server setting |
| --- | --- | --- |
| `util.export_table()` | `SELECT` | None |
| `util.import_table()` | `INSERT`; also `DELETE` with `replaceDuplicates` | `local_infile` must be `ON` |

The `local_infile` system variable is `ON` by default in MariaDB Server. If it is off, the import stops before loading anything:

```text
ERROR: The 'local_infile' global system variable must be set to ON in the target server, after the server is verified to be trusted.
ERROR: MYSQLSH 53025: local_infile disabled in server
```

An administrator can enable it with `SET GLOBAL local_infile = ON`, or permanently with `local_infile=ON` in the server option file. You don't need to start the shell with `--local-infile`: the import connections enable the client side of `LOAD DATA LOCAL` themselves, and they only send the files you name.

## Dialects

A dialect is a preset of the five options that describe the file format. You can start from a dialect and override any of its options.

| Dialect | Fields separated by | Enclosed by | Enclosure | Escaped by | Lines end with | Export | Import |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `default` | Tab | Nothing | None | `\` | LF | Yes | Yes |
| `csv` | `,` | `"` | Optional | `\` | CR LF | Yes | Yes |
| `tsv` | Tab | `"` | Optional | `\` | CR LF | Yes | Yes |
| `csv-unix` | `,` | `"` | Every field | `\` | LF | Yes | Yes |
| `csv-rfc-unix` | `,` | `"` | Optional | Nothing; `"` is doubled | LF | Yes | Yes |
| `json` | LF | Nothing | None | Nothing | LF | No | Yes |

The option names behind the columns are `fieldsTerminatedBy`, `fieldsEnclosedBy`, `fieldsOptionallyEnclosed`, `fieldsEscapedBy`, and `linesTerminatedBy`. They mean the same as the matching clauses of `SELECT ... INTO OUTFILE` and `LOAD DATA`.

A few details matter when you exchange files with other tools:

* In every dialect except `csv-rfc-unix`, SQL `NULL` is written as `\N`. `csv-rfc-unix` follows RFC 4180: quotes inside a value are doubled, no backslash escapes are used, and `NULL` is written as the unquoted word `NULL`.
* `csv` and `tsv` use Windows line endings (CR LF). Use `csv-unix` or `csv-rfc-unix` for files with LF line endings.
* `json` expects one JSON document per line and loads each line into one column. `util.export_table()` rejects it with `The 'json' dialect is not supported.`

## Exporting a Table

```python
util.export_table(table, outputUrl[, options])
```

* `table` is `table` or `schema.table`, with backticks where a name needs quoting. Without a schema, the default schema of the global session is used.
* `outputUrl` is the file to write. Its parent directory must exist. An existing file is overwritten. On systems with POSIX permissions, the file is created with mode `rw-r-----`.

The following session exports a table as tab-separated values, then exports the Brazilian customers as a fully quoted CSV file:

```text
MariaDB localhost:3306 ssl  Py > util.export_table("shop.customers", "/exports/customers.tsv")
...
Rows written: 20003
Bytes written: 1.11 MB

The dump can be loaded using:
util.import_table("/exports/customers.tsv", {
    "characterSet": "utf8mb4",
    "schema": "shop",
    "table": "customers"
})
MariaDB localhost:3306 ssl  Py > util.export_table("shop.customers", "/exports/customers_br.csv", {"dialect": "csv-unix", "where": "country = 'BR'"})
```

The first lines of the CSV file:

```text
"1","Ana Lima","ana@example.com","BR","2026-01-12",\N
"6","Customer 3","c3@example.com","BR","2026-01-04",\N
```

At the end of every export, the utility prints the `util.import_table()` call that loads the file back with the matching options. Keep it with the file.

Binary columns, such as `BLOB` and `BINARY`, are written in Base64. The printed import call then contains the `columns` and `decodeColumns` options that decode them. Because of the encoding, a binary value can't be larger than about 74 percent of `max_allowed_packet` on the server that imports it.

### Export Options

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `where` | string | Not set | A SQL condition that selects the rows to export, without the `WHERE` keyword. |
| `partitions` | list of strings | Not set | Export only these partitions. MariaDB Server doesn't allow partition selection on system-versioned tables, so the option is refused for them. |
| `dialect` | string | `default` | One of `default`, `csv`, `tsv`, `csv-unix`, `csv-rfc-unix`. See [Dialects](#dialects). |
| `fieldsTerminatedBy` | string | Tab | String between fields. Overrides the dialect. |
| `fieldsEnclosedBy` | character | Empty | Character that encloses values. Overrides the dialect. |
| `fieldsOptionallyEnclosed` | Boolean | `false` | If `true`, only string values are enclosed. If `false`, every value is enclosed by `fieldsEnclosedBy`. |
| `fieldsEscapedBy` | character | `\` | Escape character. Overrides the dialect. |
| `linesTerminatedBy` | string | LF | String at the end of each row. Overrides the dialect. |
| `compression` | string | `none` | `none`, `gzip`, or `zstd`. You can add a level, such as `"zstd;level=8"`. |
| `defaultCharacterSet` | string | `utf8mb4` | Character set of the export session, and therefore of the file. |
| `maxRate` | string | `"0"` | Maximum read throughput in bytes per second, with the suffixes `k`, `M`, and `G`. `"0"` means no limit. |
| `showProgress` | Boolean | `true` on a terminal | Show progress information. |

The export can write to Amazon S3, OCI Object Storage, or Azure Blob Storage instead of a local file. For the storage options, such as `s3BucketName`, see [Object Storage](dump-and-load/object-storage.md).

## Importing Files

```python
util.import_table(urls[, options])
```

`urls` is a file path or a list of paths. A path can contain the wildcards `*` and `?` to select several files. All selected files must contain rows for the same table. Files whose names end in `.gz` or `.zst` are decompressed while they are read.

The target table must exist. If you don't give `table`, the file name without its extension is used, and if you don't give `schema`, the default schema of the global session is used.

### Parallel Import

How the work is divided depends on the input:

* **One file.** The utility scans the file for row boundaries and cuts it into chunks of about `bytesPerChunk` bytes. Up to `threads` connections load chunks at the same time, each with its own `LOAD DATA` statement. The number of connections never exceeds the number of chunks. This also works for compressed files, which are decompressed while they are scanned.
* **Several files.** Each file is loaded as one unit, and up to `threads` files are loaded at the same time. `bytesPerChunk` can't be used in this case.
* **Files that can't be split.** A file can only be cut into chunks when its line terminator is not empty and differs from its field terminator. Otherwise, such as with the `json` dialect, the file is loaded by one connection.

Use `maxBytesPerTransaction` to split each chunk further into several `LOAD DATA` statements. This keeps each transaction smaller than `max_binlog_cache_size` on servers with binary logging, which otherwise fail large loads with error 1197.

Tables that use a storage engine with table-level locks, such as MyISAM, are loaded one chunk at a time, regardless of `threads`.

### Session Settings of the Import Connections

Each import connection prepares its session before it loads data:

* It clears `sql_mode`.
* It sets the character set with `SET NAMES` when you give `characterSet`.
* It sets `foreign_key_checks = 0` and `check_constraint_checks = 0`, so rows load in any order and rows that violate a `CHECK` constraint are kept.
* It sets the transaction isolation level to `READ UNCOMMITTED`.
* On MariaDB Server, it keeps `unique_checks` on unless `replaceDuplicates` is `true`. With duplicate keys in a file, InnoDB's bulk insert path can otherwise drop rows that are not duplicates. With `replaceDuplicates`, `unique_checks` is set to `0`.

Use `sessionInitSql` to run additional statements in each import connection, for example to set `time_zone`.

### Example: Parallel Import of a Large File

The following call loads the file exported above into an empty copy of the table with four connections and 200 KB chunks:

```text
MariaDB localhost:3306 ssl  Py > util.import_table("/exports/customers.tsv", {"schema": "shop", "table": "customers_copy", "threads": 4, "bytesPerChunk": "200k"})
Importing from file '/exports/customers.tsv' to table `shop`.`customers_copy` in MariaDB Server at localhost:3306 using 4 threads
Parallel load data...
[Worker000]: customers.tsv: Records: 3854  Deleted: 0  Skipped: 0  Warnings: 0
[Worker003]: customers.tsv: Records: 3793  Deleted: 0  Skipped: 0  Warnings: 0
...
Parallel load data - done
File '/exports/customers.tsv' (1.11 MB) was imported in 0.1152 sec at 1.11 MB/s
Total rows affected in shop.customers_copy: Records: 20003  Deleted: 0  Skipped: 0  Warnings: 0
```

### Example: Transforming Values While Loading

A supplier delivers a price list with a header line, prices in cents, and dates in day/month/year order:

{% code title="products.csv" %}
```text
sku,product,price_cents,added
A-100,Desk lamp,2599,05/01/2026
A-101,Office chair,14900,17/02/2026
A-102,"Cable, USB-C",899,28/03/2026
```
{% endcode %}

The target table stores the price in a `DECIMAL` column and the date in a `DATE` column:

```sql
CREATE TABLE shop.products (
  sku     VARCHAR(10) PRIMARY KEY,
  product VARCHAR(50),
  price   DECIMAL(8,2),
  added   DATE
);
```

`columns` maps the fields of the file, in order, to table columns. An integer in the list reads that field into a user variable instead: `1` becomes `@1`. `decodeColumns` then sets table columns from SQL expressions over those variables. `skipRows` skips the header line:

```python
util.import_table("/imports/products.csv", {
    "schema": "shop",
    "table": "products",
    "dialect": "csv-unix",
    "fieldsOptionallyEnclosed": True,
    "skipRows": 1,
    "columns": ["sku", "product", 1, 2],
    "decodeColumns": {
        "price": "@1 / 100",
        "added": "STR_TO_DATE(@2, '%d/%m/%Y')"
    }
})
```

The result:

```text
MariaDB localhost:3306 ssl  SQL > SELECT * FROM shop.products;
+-------+--------------+--------+------------+
| sku   | product      | price  | added      |
+-------+--------------+--------+------------+
| A-100 | Desk lamp    |  25.99 | 2026-01-05 |
| A-101 | Office chair | 149.00 | 2026-02-17 |
| A-102 | Cable, USB-C |   8.99 | 2026-03-28 |
+-------+--------------+--------+------------+
```

`decodeColumns` also accepts the shorthand values `"UNHEX"` and `"FROM_BASE64"`. With a shorthand, list the column by name in `columns`, and the utility decodes the field with that function. This is the form that `util.export_table()` prints for binary columns:

```python
{"columns": ["id", "name", "body"], "decodeColumns": {"body": "FROM_BASE64"}}
```

### Example: JSON Lines and Multiple Files

Load a file with one JSON document per line into the `doc` column of a table:

```python
util.import_table("/imports/items.json", {"schema": "shop", "table": "items", "dialect": "json", "columns": ["doc"]})
```

Load all parts of a split export with two connections:

```sh
mariadb-shell root@localhost -- util import-table "/imports/part_*.tsv" --schema=shop --table=customers_copy --threads=2
```

Quote the wildcard so that your operating system shell passes it to MariaDB Shell unexpanded.

### Duplicate Keys

By default, rows whose primary key or unique key already exists in the table are skipped, and each one is reported as a warning. The summary line shows them under `Skipped`. Set `replaceDuplicates` to `true` to replace the existing rows instead.

### Import Options

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `schema` | string | Default schema of the session | Schema of the target table. |
| `table` | string | File name without its extension | Target table. |
| `columns` | list of strings and integers | Not set | Field-to-column mapping, in file order. A non-negative integer `n` reads the field into the user variable `@n`. |
| `decodeColumns` | dictionary | Not set | Maps a column name to a SQL expression, or to the shorthand `"UNHEX"` or `"FROM_BASE64"`. Requires `columns`. |
| `dialect` | string | `default` | One of `default`, `csv`, `tsv`, `json`, `csv-unix`, `csv-rfc-unix`. See [Dialects](#dialects). |
| `fieldsTerminatedBy` | string | Tab | String between fields. Overrides the dialect. |
| `fieldsEnclosedBy` | character | Empty | Character that encloses values. Overrides the dialect. |
| `fieldsOptionallyEnclosed` | Boolean | `false` | Set to `true` when only some values are enclosed. |
| `fieldsEscapedBy` | character | `\` | Escape character. Overrides the dialect. |
| `linesTerminatedBy` | string | LF | String at the end of each row. Overrides the dialect. |
| `skipRows` | integer | `0` | Number of lines to skip at the start of each file, such as a header line. |
| `replaceDuplicates` | Boolean | `false` | Replace existing rows that have the same primary or unique key, instead of skipping the new rows. |
| `threads` | integer | `8` | Maximum number of connections that load data at the same time. |
| `bytesPerChunk` | string | `"50M"` | Approximate chunk size for a single file, with the suffixes `k`, `M`, and `G`. The minimum is `"131072"`. Not allowed with several files. |
| `maxBytesPerTransaction` | string | Not set | Maximum number of bytes loaded by one `LOAD DATA` statement. The minimum is `"4096"`. |
| `maxRate` | string | `"0"` | Maximum send throughput per connection, in bytes per second, with the suffixes `k`, `M`, and `G`. `"0"` means no limit. |
| `characterSet` | string | Not set | Character set of the file. `"binary"` means no conversion. Without it, the server uses `character_set_database`. |
| `sessionInitSql` | list of strings | `[]` | Statements to run in each import connection before it loads data. |
| `showProgress` | Boolean | `true` on a terminal | Show progress information. |

The import can read files from Amazon S3, OCI Object Storage, or Azure Blob Storage instead of the local file system. For the storage options, see [Object Storage](dump-and-load/object-storage.md).

## Running from the Command Line

Both utilities support [command line integration](../using-mariadb-shell/command-line-integration.md). Options become `--name=value` arguments, in camelCase or kebab-case:

```sh
mariadb-shell root@localhost -- util export-table shop.customers /exports/customers.csv --dialect=csv-unix --show-progress=false
mariadb-shell root@localhost -- util import-table /exports/customers.csv --schema=shop --table=customers_copy --dialect=csv-unix --replace-duplicates=true
```
