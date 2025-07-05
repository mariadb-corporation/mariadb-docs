# list\_add

## Syntax

```
sys.list_add(list,value)
```

## Description

`list_add` is a [stored function](../../../../../../server-usage/stored-routines/stored-functions/) available with the [Sys Schema](../).

It takes a _list_ to be modified and a _value_ to be added to the list, returning the resulting value. This can be used, for example, to add a value to a system variable taking a comma-delimited list of options, such as [sql\_mode](../../../../../../server-management/variables-and-modes/sql-mode.md).

The related function [list\_drop](list_drop.md) can be used to drop a value from a list.

## Examples

```
SELECT @@sql_mode;
+-----------------------------------------------------------------------+
| @@sql_mode                                                            |
+-----------------------------------------------------------------------+
| STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,
NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION |
+-----------------------------------------------------------------------+

SET @@sql_mode = sys.list_add(@@sql_mode, 'NO_ZERO_DATE');

SELECT @@sql_mode;
+-----------------------------------------------------------------------+
| @@sql_mode                                                            |
+-----------------------------------------------------------------------+
| STRICT_TRANS_TABLES,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,
NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION |
+-----------------------------------------------------------------------+
```

## See Also

* [list\_drop](list_drop.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
