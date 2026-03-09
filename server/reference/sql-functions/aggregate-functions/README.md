---
description: >-
  Perform calculations on multiple rows to return a single value. Includes
  standard SQL functions like SUM, AVG, COUNT, MIN, and MAX, often used with
  GROUP BY.
---

# Aggregate Functions

{% columns %}
{% column %}
{% content-ref url="../../../server-usage/stored-routines/stored-functions/stored-aggregate-functions.md" %}
[stored-aggregate-functions.md](../../../server-usage/stored-routines/stored-functions/stored-aggregate-functions.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Stored Aggregate Functions allow users to create custom aggregate functions that process a sequence of rows and return a single summary result. This page provides a general overview.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="avg.md" %}
[avg.md](avg.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Calculate the average value. This function computes the arithmetic mean of a numeric expression, ignoring `NULL` values.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="bit_and.md" %}
[bit\_and.md](bit_and.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Perform a bitwise `AND` operation. This function returns the result of performing a bitwise `AND` on all values in a given expression.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="bit_or.md" %}
[bit\_or.md](bit_or.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Perform a bitwise `OR` operation. This function returns the result of performing a bitwise `OR` on all values in a given expression.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="bit_xor.md" %}
[bit\_xor.md](bit_xor.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Perform a bitwise `XOR` operation. This function returns the result of performing a bitwise `XOR` on all values in a given expression.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="count-distinct.md" %}
[count-distinct.md](count-distinct.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Count unique values. This function returns the number of distinct, non-`NULL` values found in the specified column or expression.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="count.md" %}
[count.md](count.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Complete `COUNT()` function reference: `COUNT(*`) and `COUNT(expr)` syntax, `COUNT(DISTINCT)` usage, `GROUP BY` aggregation, and `OVER(PARTITION BY)` window syntax.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="group_concat.md" %}
[group\_concat.md](group_concat.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Complete `GROUP_CONCAT` reference for MariaDB. Complete function guide with syntax, parameters, return values, and usage examples for production use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../special-functions/json-functions/json_arrayagg.md" %}
[json\_arrayagg.md](../special-functions/json-functions/json_arrayagg.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Aggregate values into a JSON array. This function aggregates a result set column into a single JSON array.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../special-functions/json-functions/json_objectagg.md" %}
[json\_objectagg.md](../special-functions/json-functions/json_objectagg.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Aggregate key-value pairs into a JSON object. This function aggregates two columns or expressions into a single JSON object.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="max.md" %}
[max.md](max.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Find the maximum value. This function returns the highest value in a set of values, applicable to numbers, strings, and dates.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="min.md" %}
[min.md](min.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Find the minimum value. This function returns the lowest value in a set of values, applicable to numbers, strings, and dates.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="std.md" %}
[std.md](std.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Calculate population standard deviation. This function returns the square root of the population variance. It is a synonym for `STDDEV_POP()`.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="stddev.md" %}
[stddev.md](stddev.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Calculate population standard deviation. This function is a synonym for `STD()` and `STDDEV_POP()`, returning the square root of the population variance.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="stddev_pop.md" %}
[stddev\_pop.md](stddev_pop.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Calculate population standard deviation. This function computes the standard deviation assuming the set of values represents the entire population.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="stddev_samp.md" %}
[stddev\_samp.md](stddev_samp.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Calculate sample standard deviation. This function computes the standard deviation assuming the set of values represents a sample of the population.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sum.md" %}
[sum.md](sum.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Calculate the total sum. This function returns the sum of all values in a numeric expression, ignoring `NULL` values.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="var_pop.md" %}
[var\_pop.md](var_pop.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Calculate population variance. This function computes the statistical variance for a set of values assumed to be the entire population.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="var_samp.md" %}
[var\_samp.md](var_samp.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Calculate sample variance. This function computes the statistical variance for a set of values assumed to be a sample of the population.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="variance.md" %}
[variance.md](variance.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Calculate population variance. This function is a synonym for VAR\_POP() and returns the variance of a set of values.
{% endcolumn %}
{% endcolumns %}
