---
description: >-
  Compress Aria tables into read-only form that is typically 40 to 70 percent
  smaller with aria_pack.
---

# aria\_pack

`aria_pack` is a tool for compressing [Aria](../../server-usage/storage-engines/aria/) tables. The resulting tables are read-only, and usually about 40% to 70% smaller.

`aria_pack` is run as follows:

```
aria_pack [options] file_name [file_name2...]
```

The file name is the `.MAI` index file. The extension can be omitted, although keeping it permits wildcards, for instance to compress all the files, such as:

```
aria_pack *.MAI
```

`aria_pack` compresses each column separately. This means, when the resulting data is read, only the individual rows and columns required need to be decompressed, allowing for quicker reading.

Once a table has been packed, use [aria\_chk -rq](aria_chk.md) (the quick and recover options) to rebuild its indexes.

## Options

The following variables can be set as command line options to `aria_pack`, or set in the `[ariapack]` section in your [my.cnf](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) file:

| Option                      | Description                                                                                                                        |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| -b, --backup                | Make a backup of the table as _`table_name`_`.OLD`.                                                                                |
| --character-sets-dir=_name_ | Directory where character sets are located.                                                                                        |
| -h, --datadir               | <p>Path for control file (and logs if <code>--logdir</code> is not used). </p><p>This option is available from MariaDB 10.5.3.</p> |
| -#, --debug\[=name]         | Output debug log. Often this is `d:t:o,filename`.                                                                                  |
| -?, --help                  | Display help and exit.                                                                                                             |
| -f, --force                 | Force packing of table even if it gets bigger or if a temporary file exists.                                                       |
| --ignore-control-file       | <p>Ignore the control file. </p><p>This option is available from MariaDB 10.5.3.</p>                                               |
| -j, --join=_name_           | Join all given tables into _name_. All tables must have identical layouts.                                                         |
| --require-control-file      | <p>Abort if the tool cannot find the control file.</p><p>This option is available from MariaDB 10.5.3.</p>                         |
| -s, --silent                | Only write output when an error occurs.                                                                                            |
| -t, --test                  | Don't pack table, only test packing it.                                                                                            |
| -T, --tmpdir=name           | Use temporary directory to store temporary table.                                                                                  |
| -v, --verbose               | Write info about progress and packing result. Use multiple `-v` options for more verbosity.                                        |
| -V, --version               | Output version information and exit.                                                                                               |
| -w, --wait                  | Wait and retry if table is in use.                                                                                                 |

## Unpacking

To unpack a table compressed with aria\_pack, use the [aria\_chk -u](aria_chk.md) option.

## Example

```
> aria_pack /my/data/test/posts
Compressing /my/data/test/posts.MAD: (1690 records)
- Calculating statistics
- Compressing file
37.71%     
> aria_chk -rq --ignore-control-file /my/data/test/posts
- check record delete-chain
- recovering (with keycache) Aria-table '/my/data/test/posts'
Data records: 1690
State updated
```

## See Also

* [FLUSH TABLES FOR EXPORT](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)
* [myisamchk](../myisam-clients-and-utilities/myisamchk.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
