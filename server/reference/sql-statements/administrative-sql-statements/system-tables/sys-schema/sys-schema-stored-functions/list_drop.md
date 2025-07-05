# list\_drop

## Syntax

```
sys.list_drop(list,value)
```

## Description

`list_drop` is a [stored function](../../../../../../server-usage/stored-routines/stored-functions/) available with the [Sys Schema](../).

It takes a _list_ to be modified and a _value_ to be dropped from the list, returning the resulting value. This can be used, for example, to remove a value from a system variable taking a comma-delimited list of options, such as [sql\_mode](../../../../../../server-management/variables-and-modes/sql-mode.md).

The related function [list\_add](list_add.md) can be used to add a value to a list.

## Examples

```
SELECT @@sql_mode;
+-----------------------------------------------------------------------+
| @@sql_mode                                                            |
+-----------------------------------------------------------------------+
| STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,
NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION |
+-----------------------------------------------------------------------+

SET @@sql_mode = sys.list_drop(@@sql_mode, 'NO_ENGINE_SUBSTITUTION');

SELECT @@sql_mode;
+-----------------------------------------------------------------------+
| @@sql_mode                                                            |
+-----------------------------------------------------------------------+
| STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,
NO_AUTO_CREATE_USER |
+-----------------------------------------------------------------------+
```

## See Also

* [list\_add](list_add.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
