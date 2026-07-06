---
description: >-
  MariaDB enhancements to the mariadb-test (mysqltest) framework.
---

# New Features for mysqltest in MariaDB

{% hint style="info" %}
Note that not all MariaDB-enhancements are listed on this page. See [mariadb-test and mariadb-test-embedded](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/using-mariadb-with-your-programs-api/libmysqld/mariadb-test-and-mariadb-test-embedded.md) for a full set of options.
{% endhint %}

## Startup Option --connect-timeout

```
--connect-timeout=N
```

This can be used to set the MYSQL\_OPT\_CONNECT\_TIMEOUT parameter of\
mysql\_options, to change the number of seconds before an unsuccessful\
connection attempt times out.

## Test Commands for Handling Warnings During Prepare Statements

* `enable_prepare_warnings;`
* `disable_prepare_warnings;`

Normally, when running with the prepared statement protocol with warnings\
enabled and executing a statement that returns a result set (like SELECT),\
warnings that occur during the execute phase are shown, but warnings that occur\
during the prepare phase are ''not'' shown. The reason for this is that some\
warnings are returned both during prepare and execute; if both copies of\
warnings were shown, then test cases would show different number of warnings\
between prepared statement execution and normal execution (where there is no\
prepare phase).

The `enable_prepare_warnings` command changes this so that\
warnings from both the prepare and execute phase are shown, regardless of\
whether the statement produces a result set in the execute phase. The`disable_prepare_warnings` command reverts to the default\
behaviour.

These commands only have effect when running with the prepared statement\
protocol (--ps-protocol) _and_ with warnings enabled\
(enable\_warnings). Furthermore, they only have effects for statements that\
return a result set (as for statements without result sets, warnings from are\
always shown when warnings are enabled).

The `replace_regex` command supports paired delimiters (like in perl, etc). If the first non-space character in the `replace_regex` argument is one of `(`, `[`, `{`, `<`, then the pattern should end with `)`, `]`, `}`, `>` accordingly. The replacement string can use its own pair of delimiters, not necessarily the same as the pattern. If the first non-space character in the `replace_regex` argument is not one of the above, then it should also separate the pattern and the replacement string and it should end the replacement string. Backslash can be used to escape the current terminating character as usual. The examples below demonstrate valid usage of `replace_regex`:

```
--replace_regex (/some/path)</another/path>
--replace_regex !/foo/bar!foobar!
--replace_regex {pat\}tern}/replace\/ment/i
```

## Dumping "exec" output on errors only

Sometimes it is only interesting to see the output of a utility to stdout/stderr, if utility failed. In case of success, the output might be unpredictable, and contain timestamps, startup messages etc. mariadb-backup can be a good example of such utility.

mysqltest in MariaDB can helps in this situation. In the example below, the output of $XTRABACKUP is suppressed, however if `exec` fails, stdout and stderr both is dumped , to aid diagnostics:

```
--disable_result_log
exec $XTRABACKUP  --param1 --param2  # Note, do not use output redirection here
--enable_result_log
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
