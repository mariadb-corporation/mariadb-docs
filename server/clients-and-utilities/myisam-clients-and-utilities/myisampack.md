---
description: >-
  Compress MyISAM tables into read-only form that is typically 40 to 70
  percent smaller with myisampack.
---

# myisampack

## myisampack

`myisampack` is a tool for compressing [MyISAM](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/myisam-storage-engine/README.md) tables. The resulting tables\
are read-only, and usually about 40% to 70% smaller. It is run as follows:

```
myisampack [options] file_name [file_name2...]
```

The `file_name` is the `.MYI` index file. The extension can be omitted,\
although keeping it permits wildcards, such as:

```
myisampack *.MYI
```

...to compress all the files.

`myisampack` compresses each column separately, and, when the resulting data\
is read, only the individual rows and columns required need to be decompressed,\
allowing for quicker reading.

Once a table has been packed, use [myisamchk -rq](myisamchk.md) (the quick\
and recover options) to rebuild its indexes.

`myisampack` does not support partitioned tables or vector indexes.

{% hint style="danger" %}
Do not run myisampack if the tables could be updated during the operation, and [skip\_external\_locking](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#skip_external_locking) has been set.
{% endhint %}

### Options

The following variables can be set while passed as command line options to`myisampack`, or set with a `[myisampack]` section in your [my.cnf](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) file.

| Option                    | Description                                                                             |
| ------------------------- | --------------------------------------------------------------------------------------- |
| -b, --backup              | Make a backup of the table as table\_name.OLD.                                          |
| --character-sets-dir=name | Directory where character sets are.                                                     |
| -                         |                                                                                         |
| ## , --debug\[=name]      | Output debug log. Often this is 'd:t:o,filename'.                                       |
| -f, --force               | Force packing of table even if it gets bigger or if tempfile exists.                    |
| -j, --join=name           | Join all given tables into 'new\_table\_name'. All tables must have identical layouts.  |
| -?, --help                | Display help and exit.                                                                  |
| -s, --silent              | Only write output when an error occurs                                                  |
| -T, --tmpdir=name         | Use temporary directory to store temporary table.                                       |
| -t, --test                | Don't pack table, only test packing it.                                                 |
| -v, --verbose             | Write info about progress and packing result. Use multiple -v flags for more verbosity. |
| -V, --version             | Output version information and exit.                                                    |
| -w, --wait                | Wait and retry if table is in use.                                                      |

### Uncompressing

To uncompress a table compressed with `myisampack`, use the [myisamchk -u](myisamchk.md) option.

### Examples

```
> myisampack /var/lib/mysql/test/posts
Compressing /var/lib/mysql/test/posts.MYD: (1680 records)
- Calculating statistics
- Compressing file
37.71%
> myisamchk -rq /var/lib/mysql/test/posts
- check record delete-chain
- recovering (with sort) MyISAM-table '/var/lib/mysql/test/posts'
Data records: 1680
- Fixing index 1
- Fixing index 2
```

### See Also

* [FLUSH TABLES FOR EXPORT](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)
* [myisamchk](myisamchk.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
