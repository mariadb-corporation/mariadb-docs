---
description: >-
  innochecksum prints checksums for InnoDB tablespace files and reports
  mismatches, which identify damaged pages after a power outage or a file
  copy.
---

# innochecksum

innochecksum is a tool for printing checksums for InnoDB files.

## Usage

```bash
innochecksum [options] file_name
```

## Description

The tool reads an [InnoDB](../../server-usage/storage-engines/innodb/) tablespace file, calculates the checksum for each page, compares the calculated checksum to the stored checksum, and reports mismatches, which indicate damaged pages. It was originally developed to speed up verifying the integrity of tablespace files after power outages, but can also be used after file copies. Because checksum mismatches causes InnoDB to deliberately shut down a running server, it can be preferable to use innochecksum rather than waiting for a server in production usage to encounter damaged pages.

{% hint style="info" %}
Multiple filenames can be specified by a wildcard (on non-Windows systems only).
{% endhint %}

innochecksum works with compressed pages, and includes options to analyze leaf pages to estimate how fragmented an index is and how much benefit can be gained from defragmentation.

{% hint style="info" %}
innochecksum cannot be used on tablespace files that the server already has open. For such files, you should use [CHECK TABLE](../../reference/sql-statements/table-statements/check-table.md) to check tables within the tablespace. If checksum mismatches are found, you would normally restore the tablespace from backup or start the server and attempt to use [mariadb-dump](../backup-restore-and-import-clients/mariadb-dump.md) to make a backup of the tables within the tablespace.
{% endhint %}

## Options

innochecksum supports the following options. For options that refer to page numbers, the numbers are zero-based.

| Option                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -a, --allow-mismatches=#  | Maximum checksum mismatch allowed before innochecksum terminates. Defaults to `0`, which terminates on the first mismatch.                                                                                                                                                                                                                                                                                                                                                 |
| -c, --count               | Print a count of the number of pages in the file.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -e num, --end-page=#      | End at this page number (0-based).                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -?, --help                | Display help and exits.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -I, --info                | Synonym for --help.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -f, --leaf                | Examine leaf index pages.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -l fn, --log=fn           | Log output to the specified filename _`fn`_.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| -m num, --merge=#         | Leaf page count, in case of a merge, given number of consecutive pages.                                                                                                                                                                                                                                                                                                                                                                                                    |
| -n, --no-check            | Ignore the checksum verification. Before MariaDB 10.6, must be used with the `--write` option.                                                                                                                                                                                                                                                                                                                                                                             |
| -p num, --page=#          | Check only this page number (0-based).                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -D, --page-type-dump=name | Dump the page type info for each page in a tablespace.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -S, --page-type-summary   | Display a count of each page type in a tablespace.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -i, --per-page-details    | Print out detailed information per page.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| -u, --skip-corrupt        | Skip corrupt pages.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -r, --skip-freed-pages    | <p>innochecksum misinterprets freed pages as active, leading to confusion that too many valid pages exist. To avoid this, this option was introduced to avoid freed pages while dumping or printing the summary of the tablespace. </p><p></p><p>This option is available from MariaDB 11.7.2, 11.4.5, 10.6.21, and 10.11.11.</p>                                                                                                                                          |
| -s num, --start-page=#    | Start at this page number (0-based).                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -C, --strict-check=name   | <p>Specify the strict checksum algorithm. One of: <code>crc32</code>, <code>innodb</code>, <code>none</code>. If not specified, validates against <code>innodb</code>, <code>crc32</code> , and <code>none</code>. <code>full_crc32</code> is not supported. See also <a href="../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_checksum_algorithm">innodb_checksum_algorithm</a>. </p><p></p><p>This option was removed in MariaDB 10.6.0.</p> |
| -v, --verbose             | Verbose mode; print a progress indicator every five seconds.                                                                                                                                                                                                                                                                                                                                                                                                               |
| -V, --version             | Display version information and exit.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -w, --write=name          | <p>Rewrite the checksum algorithm. One of <code>crc32</code>, <code>innodb</code>, <code>none</code>. An exclusive lock is obtained during use. Use in conjunction with the <code>-no-check</code> option to rewrite an invalid checksum. </p><p></p><p>This option was removed in MariaDB 10.6.0.</p>                                                                                                                                                                     |

## Examples

Rewriting a CRC32 checksum to replace an invalid checksum:

```bash
innochecksum --no-check --write crc32 tablename.ibd
```

A count of each page type:

```bash
innochecksum --page-type-summary data/mysql/gtid_slave_pos.ibd

File::data/mysql/gtid_slave_pos.ibd
================PAGE TYPE SUMMARY==============
#PAGE_COUNT	PAGE_TYPE
===============================================
       1	Index page
       0	Undo log page
       1	Inode page
       0	Insert buffer free list page
       2	Freshly allocated page
       1	Insert buffer bitmap
       0	System page
       0	Transaction system page
       1	File Space Header
       0	Extent descriptor page
       0	BLOB page
       0	Compressed BLOB page
       0	Page compressed page
       0	Page compressed encrypted page
       0	Other type of page

===============================================
Additional information:
Undo page type: 0 insert, 0 update, 0 other
Undo page state: 0 active, 0 cached, 0 to_free, 0 to_purge, 0 prepared, 0 other
index_id	#pages		#leaf_pages	#recs_per_page	#bytes_per_page
24		1		1		0		0

index_id	page_data_bytes_histgram(empty,...,oversized)
24		1	0	0	0	0	0	0	0	0	0	0	0
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
