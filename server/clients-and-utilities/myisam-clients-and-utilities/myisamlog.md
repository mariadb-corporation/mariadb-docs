---
description: >-
  Process and display the contents of a MyISAM log file with the myisamlog
  utility.
---

# myisamlog

`myisamlog` processes and returns the contents of a [MyISAM log file](../../server-management/server-monitoring-logs/myisam-log.md).

Invoke `myisamlog` like this:

```
shell> myisamlog [options] [log_file [tbl_name] ...]
shell> isamlog [options] [log_file [tbl_name] ...]
```

The default operation is update (`-u`). If a recovery is done (`-r`), all\
writes and possibly updates and deletes are done and errors are only counted.\
The default log file name is `myisam.log` for `myisamlog` and `isam.log`\
for `isamlog` if no `log_file` argument is given. If tables are named on\
the command line, only those tables are updated.

`myisamlog` supports the following options:

| Option                           | Description                                                                                                                                       |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| -?, -I                           | Display a help message and exit.                                                                                                                  |
| -c N                             | Execute only N commands.                                                                                                                          |
| -f N                             | Specify the maximum number of open files.                                                                                                         |
| -i                               | Display extra information before exiting.                                                                                                         |
| -o offset                        | Specify the starting offset.                                                                                                                      |
| -p N                             | Remove N components from path.                                                                                                                    |
| -r                               | Perform a recovery operation.                                                                                                                     |
| -R record\_pos\_file record\_pos | Specify record position file and record position.                                                                                                 |
| -u                               | Displays update operations.                                                                                                                       |
| -v                               | Verbose mode. Print more output about what the program does. This option can be given multiple times (-vv, -vvv) to produce more and more output. |
| -w write\_file                   | Specify the write file.                                                                                                                           |
| -V                               | Display version information.                                                                                                                      |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
