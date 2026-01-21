---
description: >-
  Use aggregate functions over windows. Standard aggregates like SUM and AVG can
  be used with an OVER clause to calculate running totals and moving averages.
---

# Aggregate Functions as Window Functions

It is possible to use [aggregate functions](../../aggregate-functions/) as window functions. An aggregate function used as a window function must have the `OVER` clause. For example, here's [COUNT()](../../aggregate-functions/count.md) used as a window function:

```sql
SELECT COUNT(*) OVER (ORDER BY column) FROM table;
```

MariaDB currently allows these aggregate functions to be used as window functions:

* [AVG](../../aggregate-functions/avg.md)
* [BIT\_AND](../../aggregate-functions/bit_and.md)
* [BIT\_OR](../../aggregate-functions/bit_or.md)
* [BIT\_XOR](../../aggregate-functions/bit_xor.md)
* [COUNT](../../aggregate-functions/count.md)
* [MAX](../../aggregate-functions/max.md)
* [MIN](../../aggregate-functions/min.md)
* [STD](../../aggregate-functions/std.md)
* [STDDEV](../../aggregate-functions/stddev.md)
* [STDDEV\_POP](../../aggregate-functions/stddev_pop.md)
* [STDDEV\_SAMP](../../aggregate-functions/stddev_samp.md)
* [SUM](../../aggregate-functions/sum.md)
* [VAR\_POP](../../aggregate-functions/var_pop.md)
* [VAR\_SAMP](../../aggregate-functions/var_samp.md)
* [VARIANCE](../../aggregate-functions/variance.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
