---
description: >-
  How to pause and resume mariadb-test-run.pl while a test run is in progress.
---

# Pausing mariadb-test-run.pl

Sometimes you need to work when your computer is busy running [mariadb-test-run.pl](mariadb-test-run-pl-options.md). The mariadb-test-run.pl script allows you to stop it temporarily so you can use\
your computer and then restart the tests when you're ready.

There are two ways to enable this:

1. Command-line: The `--stop-file` and`--stop-keep-alive` options.
2. Environment Variables: If you are calling mariadb-test-run.pl indirectly\
   (i.e from a script or program such as buildbot) you can set`MTR_STOP_FILE` and `MTR_STOP_KEEP_ALIVE`.

### Keep Alive

If you plan on using this feature with other programs, such as buildbot, you should set the `MTR_STOP_KEEP_ALIVE` environment variable or the `--stop-keep-alive` command line option with a value in seconds. This will make the script print messages to whatever program is calling mariadb-test-run.pl at the interval you set to prevent timeouts.

If you are calling mariadb-test-run.pl directly, you do not need to specify a timeout.

### The mariadb-test-run Stop File

The stop file is a temporary file that you create on your system when you want\
to pause the execution of mariadb-test-run. When enabled via the command line or\
environment variable options, mariadb-test-run will periodically check for the\
existence of the file and if it exists it will stop until the file is no longer\
present.

### Examples

Command-line:

```
mariadb-test-run.pl --stop-file="/path/to/stop/file" --stop-keep-alive=120
```

Environment Variables:

```
export MTR_STOP_FILE="/path/to/stop/file"
export MTR_STOP_KEEP_ALIVE=120
mariadb-test-run.pl
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
