# mariadb-dumpslow

{% hint style="info" %}
Previously, the client was called `mysqldumpslow`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.
{% endhint %}

`mariadb-dumpslow` is a tool to examine the [slow query log](../../server-management/server-monitoring-logs/slow-query-log/).

It parses the slow query log files, printing a summary result. Normally, `mariadb-dumpslow` groups queries that are similar, except for the particular values of number and string data values. It “abstracts” these values to N and ´S´ when displaying summary output. The `-a` and `-n` options can be used to modify value abstracting behavior.

## Usage

```bash
mariadb-dumpslow [ options... ] [ logs... ]
```

## Options

#### `-a`

Don't abstract all numbers to N and strings to 'S'.

#### `-d`, `--debug`

Debug mode.

#### `-g`` `_`pattern`_

Grep: only consider statements that include this string _pattern_.

#### `--help`

Display help.

#### `-h`` `_`hostname`_

_Hostname_ of db server for -slow.log filename (can be a wildcard). The Default is `''`, that is, match all hosts.

#### `-i`` `_`name`_

Name of server instance (if using mysql.server startup script).

#### `-l`

Don't subtract lock time from total time.

#### `-j`, `--json`

Stores the dumped data in JSON format. Available from MariaDB 12.1.

#### `-n`` `_`number`_

Abstract numbers with at least this _number_ of digits within names.

#### `-r`

Reverse the sort order (largest last instead of first).

#### `-s`` `_`order`_

What to sort by (`aa`, `ae`, `al`, `ar`, `at`, `a`, `c`, `e`, `l`, `r`, `t`). The default is `at` . The meaning of the abbreviations is:

* `aa` – average rows affected
* `ae` – aggregated number of rows examined
* `al` – average lock time
* `ar` – average rows sent
* `at` – average query time
* `a` – rows affected
* `c` – count
* `e` – rows examined
* `l` – lock time
* `r` – rows sent
* `t` – query time:

#### `-t`` `_`number`_

Just show the top _number of queries_.

#### `-v`, `--verbose`

Verbose mode.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
