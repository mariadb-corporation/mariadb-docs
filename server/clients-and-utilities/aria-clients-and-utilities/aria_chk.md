# aria\_chk

`aria_chk` is used to check, repair, optimize, sort and get information about [Aria](../../server-usage/storage-engines/aria/aria-storage-engine.md) tables.

With the MariaDB server, you can use [CHECK TABLE](../../reference/sql-statements/table-statements/check-table.md),[REPAIR TABLE](../../reference/sql-statements/table-statements/repair-table.md) and [OPTIMIZE TABLE](../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md) to do\
similar things.

{% hint style="danger" %}
Note: `aria_chk` should not be used when MariaDB is running. MariaDB Server assumes that no one is changing the tables it's using.
{% endhint %}

## Usage

```
aria_chk [OPTIONS] aria_tables[.MAI]
```

Aria table information is stored in 2 files: the `.MAI` file contains base\
table information and the index and the `.MAD` file contains the data.`aria_chk` takes one or more `.MAI` files as arguments.

The following groups are read from the my.cnf files:

* `[maria_chk]`
* `[aria_chk]`

## Options and Variables

### **Global Options**

The following options to handle option files may be given as the first\
argument:

| Option                  | Description                                      |
| ----------------------- | ------------------------------------------------ |
| --print-defaults        | Print the program argument list and exit.        |
| --no-defaults           | Don't read default options from any option file. |
| --defaults-file=#       | Only read default options from the given file #. |
| --defaults-extra-file=# | Read this file after the global files are read.  |

### **Main Arguments**

| Option                 | Description                                                                                                                                                            |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -#, --debug=...        | Output debug log. Often this is `d:t:o,filename`.                                                                                                                      |
| -H, --HELP             | Display this help and exit.                                                                                                                                            |
| -?, --help             | Display this help and exit.                                                                                                                                            |
| --datadir=path         | Path for control file (and logs if the `--logdir` option is not used).                                                                                                 |
| --ignore-control-file  | <p>Don't open the control file. </p><p>Use this only if you are sure the tables are not used by another program.</p>                                                   |
| --logdir=path          | Path for log files.                                                                                                                                                    |
| --require-control-file | Abort if we can't find/read the `maria_log_control` file.                                                                                                              |
| -s, --silent           | Only print errors. You can use two `-s` options to make `aria_chk` very silent.                                                                                        |
| -t, --tmpdir=path      | Path for temporary files. Multiple paths can be specified, separated by colon (`:`) on Unix or semicolon (`;`) on Windows. They are used in a round-robin fashion. |
| -v, --verbose          | Print more information. This can be used with `--description` and `--check`. Use many `-v` options for more verbosity.                                                 |
| -V, --version          | Print version and exit.                                                                                                                                                |
| -w, --wait             | Wait if table is locked.                                                                                                                                               |

### **Check Options**

**`-`**`-check` is the default action for `aria_chk`:

| Option                   | Description                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -c, --check              | Check table for errors.                                                                                                                                                                                                                                                                                                                                       |
| -e, --extend-check       | Check the table _very_ throughly. Only use this in extreme cases, as `aria_chk` should normally be able to find out if the table is okay, even without this switch.                                                                                                                                                                                           |
| -F, --fast               | Check only tables that haven't been closed properly.                                                                                                                                                                                                                                                                                                          |
| -C, --check-only-changed | Check only tables that have changed since last check.                                                                                                                                                                                                                                                                                                         |
| -f, --force              | Restart with `-r` if there are any errors in the table. States is updated as with `--update-state`.                                                                                                                                                                                                                                                      |
| -i, --information        | Print statistics information about table that is checked.                                                                                                                                                                                                                                                                                                     |
| -m, --medium-check       | Faster than extend-check, and finds 99.99% of all errors. Should be good enough for most cases.                                                                                                                                                                                                                                                               |
| -U, --update-state       | Mark tables as crashed if any errors were found and clean if check didn't find any errors but table was marked as 'not clean' before. This allows one to get rid of warnings like 'table not properly closed'. If table was updated, update also the timestamp for when the check was made. This option is on by default! Use --skip-update-state to disable. |
| -T, --read-only          | Don't mark table as checked.                                                                                                                                                                                                                                                                                                                                  |

### **Recover (Repair) Options** 

When using `--recover` or `--safe-recover'` , these options are available:

| Option                   | Description                                                                                                                                                                                                                                    |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -B, --backup             | Make a backup of the `.MAD` file as _`filename`_`-time.BAK'`.                                                                                                                                                                                  |
| --correct-checksum       | Correct checksum information for table.                                                                                                                                                                                                        |
| -D, --data-file-length=# | Max length of data file (when recreating data file when it's full).                                                                                                                                                                            |
| -e, --extend-check       | Try to recover every possible row from the data file Normally this will also find a lot of garbage rows; Don't use this option if you are not totally desperate.                                                                               |
| -f, --force              | Overwrite old temporary files.                                                                                                                                                                                                                 |
| -k, --keys-used=#        | Tell MariaDB to update only some specific keys. # is a bit mask of which keys to use. This can be used to get faster inserts.                                                                                                                  |
| --max-record-length=#    | Skip rows bigger than this if `aria_chk` can't allocate memory to hold it.                                                                                                                                                                     |
| -r, --recover            | Can fix almost anything except unique keys that aren't unique.                                                                                                                                                                                 |
| -n, --sort-recover       | Forces recovering with sorting even if the temporary file would be very big.                                                                                                                                                                   |
| -p, --parallel-recover   | Uses the same technique as `-r` and `-n` , but creates all the keys in parallel, in different threads.                                                                                                                                         |
| -o, --safe-recover       | Uses an old recovery method, which is slower than using `-r` but can handle a couple of cases where `-r` reports that it can't fix the data file.                                                                                              |
| --transaction-log        | Log repair command to transaction log. This is needed if one wants to use the `maria_read_log` option to repeat the repair.                                                                                                                    |
| --character-sets-dir=... | Directory where character sets are.                                                                                                                                                                                                            |
| --set-collation=name     | Change the collation used by the index.                                                                                                                                                                                                        |
| -q, --quick              | <p>Faster repair by not modifying the data file. One can give a second '-q' to force aria_chk to modify the original datafile in case of duplicate keys. </p><p>Note: Tables with a corrupted ´ data file can't be fixed with this option.</p> |
| -u, --unpack             | Unpack file packed with [aria\_pack](aria_pack.md).                                                                                                                                                                                            |

### **Other Options**

| Option                            | Description                                                                                                                                                                                                                                                                                                                          |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| -a, --analyze                     | Analyze distribution of keys. Will make some joins in MariaDB faster. You can check the calculated distribution by using `--description --verbose`` `_`table_name`_'.                                                                                                                                                                |
| --stats\_method=name              | Specifies how index statistics collection code should treat NULLs. Possible values of name are "nulls\_unequal" (default for 4.1/5.0), "nulls\_equal" (emulate 4.0), and "nulls\_ignored".                                                                                                                                           |
| -d, --description                 | Prints some information about table.                                                                                                                                                                                                                                                                                                 |
| -A, --set-auto-increment\[=value] | Force auto\_increment to start at this or higher value If no value is given, then sets the next auto\_increment value to the highest used value for the auto key + 1.                                                                                                                                                                |
| -S, --sort-index                  | Sort index blocks. This speeds up 'read-next' in applications.                                                                                                                                                                                                                                                                       |
| -R, --sort-records=#              | Sort records according to an index. This makes your data much more localized and may speed up things (It may be VERY slow to do a sort the first time!).                                                                                                                                                                             |
| -b, --block-search=#              | Find a record, a block at given offset belongs to.                                                                                                                                                                                                                                                                                   |
| -z, --zerofill                    | Remove transaction id's from the data and index files and fills empty space in the data and index files with zeroes. Zerofilling makes it possible to move the table from one system to another without the server having to do an automatic zerofill. It also allows one to compress the tables better if one want to archive them. |
| --zerofill-keep-lsn               | Like --zerofill but does not zero out LSN of data/index pages.                                                                                                                                                                                                                                                                       |

### **Variables**

| Option              | Description                                                                               |
| ------------------- | ----------------------------------------------------------------------------------------- |
| page\_buffer\_size  | Size of page buffer. Used by `--safe-repair`.                                             |
| read\_buffer\_size  | Read buffer size for sequential reads during scanning.                                    |
| write\_buffer\_size | Write buffer size for sequential writes during repair of fixed size or dynamic size rows. |
| sort\_buffer\_size  | Size of sort buffer. Used by `--recover`.                                                 |
| sort\_key\_blocks   | Internal buffer for sorting keys. Do not use!                                             |

## Examples

The main usage of `aria_chk` is a fast check of all Aria tables in your system. This is faster than doing it in MariaDB, as you can allocate all free memory to the buffers.

Assuming you have a bit more than 2G free memory, the following commands, run in the MariaDB data directory, check all your tables and repairs only those that have an error:

```
aria_chk --check --sort_order --force --sort_buffer_size=1G */*.MAI
```

To optimize all your tables, run this command (the `--zerofill` option is used here to fill up empty space with `\0` which can speed up compressed backups):

```
aria_chk --analyze --sort-index --page_buffer_size=1G --zerofill */*.MAI
```

In case you have a serious problem and have to use `--safe-recover`, run this command:

```
aria_chk --safe-recover --zerofill --page_buffer_size=2G */*.MAI
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
