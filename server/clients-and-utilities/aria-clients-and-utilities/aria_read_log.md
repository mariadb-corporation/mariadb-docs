---
description: >-
  Display and apply records from the Aria transaction log with the
  aria_read_log tool.
---

# aria\_read\_log

`aria_read_log` is a tool for displaying and applying log records from an [Aria](../../server-usage/storage-engines/aria/) [transaction log](../../server-usage/storage-engines/aria/aria-storage-engine.md#aria-log-files).

{% hint style="warning" %}
Aria is compiled without `-DIDENTICAL_PAGES_AFTER_RECOVERY` which means that the table files are not byte-to-byte identical to files created during normal execution. This should be okay, except for test scripts that try to compare files before and after recovery.
{% endhint %}

## Usage

```
aria_read_log OPTIONS
```

As an option, you need to use at least one of `-d` or `-a`.

## Options

The following variables can be set while passed as command line options to `aria_read_log`, or set in the `[aria_read_log]` section in your [my.cnf](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) file.

| Option                         | Description                                                                                                                                                                   |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -a, --apply                    | <p>Apply log to tables.</p><p>Careful — this modifies tables! Make a backup first! </p><p>Displays a lot of information if not run with the <code>--silent</code> option.</p> |
| --character-sets-dir=_name_    | Directory where character sets are.                                                                                                                                           |
| -c, --check                    | Used with the `--display-only` option, check if record is fully readable (for debugging).                                                                                     |
| -?, --help                     | Display help and exit.                                                                                                                                                        |
| -d, --display-only             | Display brief info read from records' header.                                                                                                                                 |
| -e, --end-lsn=#                | Stop applying at this lsn. If end-lsn is used, UNDO operations are not be applied.                                                                                            |
| -h, --aria-log-dir-path=_name_ | Path to the directory where to store transactional log.                                                                                                                       |
| -P, --page-buffer-size=#       | The size of the buffer used for index blocks of Aria tables.                                                                                                                  |
| -l, --print-log-control-file   | Print the content of the `aria_log_control_file`.                                                                                                                             |
| -o, --start-from-lsn=#         | Start reading log from this lsn.                                                                                                                                              |
| -C, --start-from-checkpoint    | Start applying from last checkpoint.                                                                                                                                          |
| -s, --silent                   | Print less information during apply/undo phase.                                                                                                                               |
| -T, --tables-to-redo=_name_    | List of comma-separated tables that we should apply REDO on. Use this if you only want to recover some tables.                                                                |
| -t, --tmpdir=name              | Path for temporary files. Multiple paths can be specified, separated by colon (`:`).                                                                                          |
| --translog-buffer-size=#       | The size of the buffer used for transaction log of Aria tables.                                                                                                               |
| -u, --undo                     | Apply UNDO records to tables. Disable with `--disable-undo`. Defaults to on; use `--skip-undo` to disable.                                                                    |
| -v, --verbose                  | Print more information during apply/undo phase.                                                                                                                               |
| -V, --version                  | Print version and exit.                                                                                                                                                       |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
