# myisamchk

## myisamchk

myisamchk is a command line tool for checking, repairing and optimizing non-partitioned [MyISAM](../../server-usage/storage-engines/myisam-storage-engine/myisam-overview.md) tables.

myisamchk is run from the command line as follows:

```
myisamchk [OPTIONS] tables[.MYI]
```

The full list of options are listed below. One or more MyISAM tables can be specified. MyISAM tables have an associated .MYI index file, and the table name can either be specified with or without the .MYI extension. Referencing it with the extension allows you to use wildcards, so it's possible to run myisamchk on _all_ the MyISAM tables in the database with `*.MYI`.

The path to the files must also be specified if they're not in the current directory.

{% hint style="danger" %}
myisamchk should not be run while anyone is accessing any of the affected tables. It is also best to make a backup before running.
{% endhint %}

With no options, myisamchk simply checks your table as the default operation.

The following options can be set while passed as command line options to myisamchk, or set with a \[myisamchk] section in your [my.cnf](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) file.

### General Options

| Option                            | Description                                                                                                                                                                                                              |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| -H, --HELP                        | Display help and exit. Options are presented in a single list.
| -?, --help                        | Display help and exit. Options are grouped by type of operation.
| -# options, --debug=options        | Write a debugging log. A typical debug options string is `d:t:o,file_name`. The default is `d:t:o,/tmp/myisamchk.trace`. (Available in debug builds only)
| -t path, --tmpdir=path         | Path for temporary files. Multiple paths can be specified, separated by colon (:) on Unix and semicolon (;) on Windows. They are used in a round-robin fashion. If not set, the TMPDIR environment variable is used. |
| -s, --silent                   | Only print errors. One can use two -s (-ss) to make myisamchk very silent.
| -v, --verbose                  | Print more information. This can be used with --description and --check. Use many -v for more verbosity.
| -V, --version                  | Print version and exit.
| -w, --wait                     | If table is locked, wait instead of returning an error.
| --print-defaults               | Print the program argument list and exit.
| --no-defaults                  | Don't read default options from any option file.
| --defaults-file=filename       | Only read default options from the given file filename, which can be the full path, or the path relative to the current directory.
| --defaults-extra-file=filename | Read the file filename, which can be the full path, or the path relative to the current directory, after the global files are read.
| --defaults-group-suffix=str    | Also read groups with a suffix of str. For example, --defaults-group-suffix=x would read the groups \[myisamchk] and \[myisamchk\_x]

The following variables can also be set by using _--var\_name=value_, for example _--ft\_min\_word\_len=5_

| Variable                                                                                                                                  | Default Value     |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| decode\_bits                                                                                                                              | 9                 |
| ft\_max\_word\_len                                                                                                                        | version-dependent |
| ft\_min\_word\_len                                                                                                                        | 4                 |
| ft\_stopword\_file                                                                                                                        | built-in list     |
| key\_buffer\_size                                                                                                                         | 1044480           |
| key\_cache\_block\_size                                                                                                                   | 1024              |
| myisam\_block\_size                                                                                                                       | 1024              |
| [myisam\_sort\_buffer\_size](../../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#myisam_sort_buffer_size) | 134216704         |
| myisam\_sort\_key\_blocks                                                                                                                 | 16                |
| read\_buffer\_size                                                                                                                        | 262136            |
| sort\_buffer\_size                                                                                                                        | 134216704         |
| sort\_key\_blocks                                                                                                                         | 16                |
| stats\_method                                                                                                                             | nulls\_unequal    |
| write\_buffer\_size                                                                                                                       | 262136            |

### Checking Tables

If no option is provided, myisamchk will perform a check table. It is possible to check [MyISAM](../../server-usage/storage-engines/myisam-storage-engine/myisam-overview.md) tables without shutting down or restricting access to the server by using [CHECK TABLE](../../reference/sql-statements/table-statements/check-table.md) instead.

The following check options are available:

| Option                   | Description                                                                                                                                                                                                                                                       |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -c, --check              | Check table for errors. This is the default operation if you specify no option that selects an operation type explicitly.                                                                                                                                         |
| -e, --extend-check       | Check the table VERY thoroughly. Only use this in extreme cases as it may be slow, and myisamchk should normally be able to find out if the table has errors even without this switch. Increasing the key\_buffer\_size can help speed the process up.             |
| -F, --fast               | Check only tables that haven't been closed properly.                                                                                                                                                                                                              |
| -C, --check-only-changed | Check only tables that have changed since last check.                                                                                                                                                                                                             |
| -f, --force              | Restart with '-r' (recover) if there are any errors in the table. States is updated as with '--update-state'.                                                                                                                                                |
| -i, --information        | Print statistics information about the table that is checked.                                                                                                                                                                                                     |
| -m, --medium-check       | Faster than extend-check, but only finds 99.99% of all errors. Should be good enough for most cases.                                                                                                                                                              |
| -U --update-state        | Mark tables as crashed if you find any errors. This should be used to get the full benefit of the --check-only-changed option, but you shouldn´t use this option if the mariadbd server is using the table and you are running it with external locking disabled. |
| -T, --read-only          | Don't mark table as checked. This is useful if you use myisamchk to check a table that is in use by some other application that does not use locking, such as mariadbd when run with external locking disabled.                                                   |

### Repairing Tables

It is also possible to repair [MyISAM](../../server-usage/storage-engines/myisam-storage-engine/myisam-overview.md) tables by using [REPAIR TABLE](../../reference/sql-statements/table-statements/repair-table.md).

The following repair options are available, and are applicable when using '-r' or '-o':

| Option                               | Description                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -B, --backup                         | Make a backup of the .MYD file as 'filename-time.BAK'.                                                                                                                                                                                                                                                                                                                              |
| --correct-checksum                   | Correct the checksum information for table.                                                                                                                                                                                                                                                                                                                                         |
| -D len, --data-file-length=#         | Max length of data file (when recreating data file when it's full).                                                                                                                                                                                                                                                                                                                 |
| -e, --extend-check                   | Try to recover every possible row from the data file. Normally this will also find a lot of garbage rows; Don't use this option if you are not totally desperate.                                                                                                                                                                                                                   |
| -f, --force                          | Overwrite old temporary files. Add another --force to avoid 'myisam\_sort\_buffer\_size is too small' errors. In this case we will attempt to do the repair with the given [myisam\_sort\_buffer\_size](../../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#myisam_sort_buffer_size) and dynamically allocate as many management buffers as needed. |
| -k val, --keys-used=#                | Specify which keys to update. The value is a bit mask of which keys to use. Each binary bit corresponds to a table index, with the first index being bit 0. 0 disables all index updates, useful for faster inserts. Deactivated indexes can be reactivated by using myisamchk -r.                                                                                                  |
| --create-missing-keys                | Create missing keys. This assumes that the data file is correct and that the number of rows stored in the index file is correct. Enables --quick                                                                                                                                                                                                                                    |
| --max-record-length=#                | Skip rows larger than this if myisamchk can't allocate memory to hold them.                                                                                                                                                                                                                                                                                                         |
| -r, --recover                        | Can fix almost anything except unique keys that aren't unique (a rare occurrence). Usually this is the best option to try first. Increase [myisam\_sort\_buffer\_size](../../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#myisam_sort_buffer_size) for better performance.                                                                         |
| -n, --sort-recover                   | Forces recovering with sorting even if the temporary file would be very large.                                                                                                                                                                                                                                                                                                      |
| -p, --parallel-recover               | Uses the same technique as '-r' and '-n', but creates all the keys in parallel, in different threads.                                                                                                                                                                                                                                                                               |
| -o, --safe-recover                   | Uses old recovery method; Slower than '-r' but uses less disk space and can handle a couple of cases where '-r' reports that it can't fix the data file. Increase key\_buffer\_size for better performance.                                                                                                                                                                         |
| --character-sets-dir=directory\_name | Directory where the [character sets](../../reference/data-types/string-data-types/character-sets/) are installed.                                                                                                                                                                                                                                                                   |
| --set-collation=name                 | Change the collation (and by implication, the [character set](../../reference/data-types/string-data-types/character-sets/)) used by the index.                                                                                                                                                                                                                                     |
| -q, --quick                          | Faster repair by not modifying the data file. One can give a second '-q' to force myisamchk to modify the original datafile in case of duplicate keys. NOTE: Tables where the data file is corrupted can't be fixed with this option.                                                                                                                                               |
| -u, --unpack                         | Unpack file packed with myisampack.                                                                                                                                                                                                                                                                                                                                                 |

### Other Actions

| Option                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -a, --analyze                              | Analyze distribution of keys. Will make some joins faster as the join optimizer can better choose the order in which to join the tables and which indexes to use. You can check the calculated distribution by using '--description --verbose table\_name' or [SHOW INDEX FROM table\_name](../../reference/sql-statements/administrative-sql-statements/show/show-index.md).                                                                                 |
| --stats\_method=name                       | Specifies how index statistics collection code should treat NULLs. Possible values of name are "nulls\_unequal" (default), "nulls\_equal" (emulate MySQL 4.0 behavior), and "nulls\_ignored".                                                                                                                                                                                                                                                                 |
| -d, --description                          | Print some descriptive information about the table. Specifying the --verbose option once or twice produces additional information.                                                                                                                                                                                                                                                                                                                            |
| -A \[value], --set-auto-increment\[=value] | Force auto\_increment to start at this or higher value. If no value is given, then sets the next auto\_increment value to the highest used value for the auto key + 1.                                                                                                                                                                                                                                                                                        |
| -S, --sort-index                           | Sort the index tree blocks in high-low order. This optimizes seeks and makes table scans that use indexes faster.                                                                                                                                                                                                                                                                                                                                             |
| -R index\_num, --sort-records=#            | Sort records according to the given index (as specified by the index number). This makes your data much more localized and may speed up range-based SELECTs and ORDER BYs using this index. It may be VERY slow to do a sort the first time! To see the index numbers, [SHOW INDEX](../../reference/sql-statements/administrative-sql-statements/show/show-index.md) displays table indexes in the same order that myisamchk sees them. The first index is 1. |
| -b offset, --block-search=offset           | Find the record to which a block at the given offset belongs.                                                                                                                                                                                                                                                                                                                                                                                                 |

For more, see [Memory and Disk Use With myisamchk](memory-and-disk-use-with-myisamchk.md).

### Examples

Check all the MyISAM tables in the current directory:

```
myisamchk *.MYI
```

If you are not in the database directory, you can check all the tables there by specifying the path to the directory:

```
myisamchk /path/to/database_dir/*.MYI
```

Check all tables in all databases by specifying a wildcard with the path to the MariaDB data directory:

```
myisamchk /path/to/datadir/*/*.MYI
```

The recommended way to quickly check all MyISAM tables:

```
myisamchk --silent --fast /path/to/datadir/*/*.MYI
```

Check all MyISAM tables and repair any that are corrupted:

```
myisamchk --silent --force --fast --update-state \
  --key_buffer_size=64M --sort_buffer_size=64M \
  --read_buffer_size=1M --write_buffer_size=1M \
/path/to/datadir/*/*.MYI
```

### See Also

* [Memory and Disk Use With myisamchk](memory-and-disk-use-with-myisamchk.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
