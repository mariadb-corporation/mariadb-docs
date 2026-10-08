---
description: >-
  Boolean literals: TRUE and FALSE as synonyms for 1 and 0.
---

# Boolean Literals

In MariaDB, `FALSE` is a synonym of `0` and `TRUE` is a synonym of `1`. These constants are case insensitive, so `TRUE`, `True`, and `true` are equivalent.

These terms are not synonyms of `0` and `1` when used with the [IS](../operators/comparison-operators/is.md) operator. So, for example, `10 IS TRUE` returns `1`, while `10 = TRUE` returns `0` (because 1 != 10).

The `IS` operator accepts a third constant exists: `UNKNOWN`. It is always a synonym of [NULL](../../data-types/null-values.md).

`TRUE` and `FALSE` are [reserved words](reserved-words.md), while `UNKNOWN` is not.

## See Also

* [BOOLEAN](../../data-types/numeric-data-types/boolean.md) type

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
