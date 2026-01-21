# Optimizer Debugging With GDB

Some useful things for debugging optimizer code.

## Useful Print Functions

* `dbug_print_item()` prints the contents of an `Item` object into a buffer and returns pointer to it.
* `dbug_print_sel_arg()` prints an individual `SEL_ARG` object (NOT the whole graph or tree) and returns pointer to the buffer holding the printout.
* `dbug_print_table_row` prints the current row buffer of the given table.
* There are more `dbug_print_XX` functions for various data structures

## Printing the Optimizer Trace

The optimizer trace is collected as plain text.\
One can print the contents of the trace collected so far as follows:

```bash
printf "%s\n", thd->opt_trace->current_trace->current_json->output.str.Ptr
```

Starting from 11.0, there is `dbug_print_opt_trace()` function which one call from gdb.

## Printing Current Partial Join Prefix

`best_access_path()` is a function that adds another table to the join prefix.

When in or around that function, the following can be useful:

A macro to print the join prefix already constructed:

```bash
define bap_print_prefix
  set $i=0
  while ($i < idx)
    p join->positions[$i++].table->table->alias.Ptr
  end
end
```

## Other Settings

* May need to set [innodb\_fatal\_semaphore\_wait\_threshold](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/storage-engines/innodb/innodb-system-variables.md#innodb_fatal_semaphore_wait_threshold) to be high enough?

## Other development topics

### mtr tests

In order to get innodb to have stable statistics, use this in the test:

```
--source include/innodb_stable_estimates.inc
```

Also consider `set global innodb_max_purge_lag_wait=0;`\
(TODO: how these two compare?)

### Coding guidelines

Run this to get your patch auto-formatted according to our coding style in `.clang-format` :

```bash
git diff -U0 --no-color --relative HEAD^ | clang-format-diff -p1 -i
```

## See Also

* [How to collect large optimizer traces](mariadb-internals-documentation-optimizer-trace/how-to-collect-large-optimizer-traces.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
