# Assignment Operator (:=)

## Syntax

```bnf
var_name := expr
```

## Description

Assignment operator for assigning a value. The value on the right is assigned to the variable on left.

Unlike the [= operator](assignment-operators-assignment-operator.md), `:=` can always be used to assign a value to a variable.

This operator works with both [user-defined variables](../../sql-language-structure/user-defined-variables.md) and [local variables](../../../sql-statements/programmatic-compound-statements/declare-variable.md).

When assigning the same value to several variables, [LAST\_VALUE()](../../../sql-functions/secondary-functions/information-functions/last_value.md) can be useful.

## Examples

```sql
SELECT @x := 10;
+----------+
| @x := 10 |
+----------+
|       10 |
+----------+

SELECT @x, @y := @x;
+------+----------+
| @x   | @y := @x |
+------+----------+
|   10 |       10 |
+------+----------+
```

## See Also

* [Operator Precedence](../operator-precedence.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
