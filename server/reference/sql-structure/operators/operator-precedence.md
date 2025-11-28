---
description: >-
  Understand operator precedence in MariaDB Server SQL. This section details the
  order in which operators are evaluated within expressions, crucial for writing
  accurate and predictable queries.
---

# Operator Precedence

The precedence is the order in which the SQL operators are evaluated.

The following list shows the SQL operator precedence. **Operators that appear first in the list have a higher precedence.** Operators which are listed together have the same precedence.

* [INTERVAL](comparison-operators/interval.md)
* [BINARY](../../data-types/string-data-types/binary.md), [COLLATE](../../data-types/string-data-types/character-sets/setting-character-sets-and-collations.md#literals)
* [!](logical-operators/not.md)
* [-](../../sql-statements/data-manipulation/selecting-data/joins-subqueries/minus.md) (unary minus), [bitwise not](../../sql-functions/secondary-functions/bit-functions-and-operators/bitwise-not.md) (unary bit inversion)
* `||` (string concatenation)
* [^](../../sql-functions/aggregate-functions/bit_xor.md) (bitwise XOR)
* [\*](arithmetic-operators/multiplication-operator.md), [/](arithmetic-operators/division-operator.md), [DIV](../../sql-functions/numeric-functions/div.md), [%](arithmetic-operators/modulo-operator.md), [MOD](../../sql-functions/numeric-functions/mod.md) (multiplication, division, modulo)
* [-](arithmetic-operators/subtraction-operator.md), [+](arithmetic-operators/addition-operator.md) (subtraction, addition)
* [<<](../../sql-functions/secondary-functions/bit-functions-and-operators/shift-left.md), [>>](../../sql-functions/secondary-functions/bit-functions-and-operators/shift-right.md)
* [&](../../sql-functions/aggregate-functions/bit_and.md) (bitwise AND)
* [|](../../sql-functions/aggregate-functions/bit_or.md) (bitwise OR)
* [LIKE](../../sql-functions/string-functions/like.md), [REGEXP](../../sql-functions/string-functions/regular-expressions-functions/regexp.md), [IN](comparison-operators/in.md)
* [BETWEEN](comparison-operators/between-and.md)
* [=](comparison-operators/equal.md) (comparison), [<=>](comparison-operators/null-safe-equal.md), [>=](comparison-operators/greater-than-or-equal.md), [>](comparison-operators/greater-than.md), [<=](comparison-operators/less-than-or-equal.md), [<](comparison-operators/less-than.md), [<>](comparison-operators/not-equal.md), [!=](comparison-operators/not-equal.md), [IS](comparison-operators/is.md)
* [NOT](logical-operators/not.md)
* [&&](logical-operators/and.md), [AND](logical-operators/and.md)
* [XOR](logical-operators/xor.md)
* [||](logical-operators/or.md) (logical or), [OR](logical-operators/or.md)
* [=](assignment-operators/assignment-operators-assignment-operator.md) (assignment), [:=](assignment-operators/assignment-operator.md)

{% hint style="warning" %}
Functions precedence is always higher than operators precedence.
{% endhint %}

If the `HIGH_NOT_PRECEDENCE` [SQL\_MODE](../../../server-management/variables-and-modes/sql_mode.md) is set, `NOT` has the same precedence as `!`.

The `||` operator's precedence, as well as its meaning, depends on the `PIPES_AS_CONCAT` [SQL\_MODE](../../../server-management/variables-and-modes/sql_mode.md) flag: if it is on, `||` can be used to concatenate strings (like the [CONCAT()](../../sql-functions/string-functions/concat.md) function) and has a higher precedence.

The `=` operator's precedence depends on the context - it is higher when `=` is used as a comparison operator.

[Parentheses](../../sql-functions/secondary-functions/bit-functions-and-operators/parentheses.md) can be used to modify the operators precedence in an expression.

## Short-Circuit Evaluation

The `AND`, `OR`, `&&` and `||` operators support short-circuit evaluation. This means that, in some cases, the expression on the right of those operators is not evaluated, because its result cannot affect the result. In the following cases, short-circuit evaluation is used and `x()` is not evaluated:

* `FALSE AND x()`
* `FALSE && x()`
* `TRUE OR x()`
* `TRUE || x()`
* `NULL BETWEEN x() AND x()`

Note however that the short-circuit evaluation does _not_ apply to `NULL AND x()`. Also, `BETWEEN`'s right operands are not evaluated if the left operand is `NULL`, but in all other cases all the operands are evaluated.

This is a speed optimization. Also, since functions can have side-effects, this behavior can be used to choose whether execute them or not using a concise syntax:

```sql
SELECT some_function() OR log_error();
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
