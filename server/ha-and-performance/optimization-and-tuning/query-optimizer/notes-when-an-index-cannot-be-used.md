# Notes When an Index Cannot Be Used

**MariaDB starting with** [**10.6.16**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-16-release-notes)

This is a new note added in 10.6.16.

## Warning About Incompatible Index Comparison

A frequent mistake database developers make is to compare an indexed column with another column that is not compatible with the indexed column. For example, comparing string columns with number columns, or using incompatible character sets or collations.

Because of this we have introduced notes (low severity warnings) when an indexed column cannot use the index to lookup rows.

The warnings are of different types:

If one compares an indexed column with a value of a different type one, will get a warning like the following:

```
Note   1105    Cannot use key `PRIMARY` part[0] for lookup: `test`.`t1`.`id` of 
  type `char` = "1" of type `bigint`
```

If one compares indexed character columns with a value of an incompatible collation, one will get a warning like the following:

```
Note   1105    Cannot use key `s2` part[0] for lookup: `test`.`t1`.`s2` of 
  collation `latin1_swedish_ci` = "'a' collate latin1_german1_ci" of collation `latin1_german1_ci`
```

Note that in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106) to [MariaDB 11.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113) we will use the error 1105 (Unknown error), as we cannot add an new error code in a GA version. In [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/what-is-mariadb-114) we will change this to be a unique error code.

## Enabling the Note

By default, the warning is only shown when executing [EXPLAIN](../../../reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain.md) on a query.\
To enable for all queries, use the option/server variable:

```
In config file:
--note-verbosity=all

As a server variable:
@@note_verbosity="all";
```

[note\_verbosity](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#note_verbosity) describes with note categories one want to get notes for. Be aware that if the old [sql\_notes](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sql_notes) variable is 0, one will not get any notes.

It can have one or many of the following options:

| Option         | Description                                                    |
| -------------- | -------------------------------------------------------------- |
| basic          | All old notes.                                                 |
| unusable\_keys | Give warnings for unusable keys for SELECT, DELETE and UPDATE. |
| explain        | Give warnings about unusable keys for EXPLAIN.                 |

One can also set `note_verbosity` to the value of `all` to set all options.

## Enabling Warnings and Notes for the Slow Query Log

One can get the note about incompatible keys also in the slow query log by adding the option `warnings` in the `log_slow_verbosity` option/variable. It will automatically be enabled if one uses `log_slow_verbosity=all`.

```
In config file:
--log-slow-verbosity=warnings

As a server variable:
@@log_slow_verbosity="all";
```

## See Also

* [Type conversions](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/sql-functions/string-functions/type-conversion.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
