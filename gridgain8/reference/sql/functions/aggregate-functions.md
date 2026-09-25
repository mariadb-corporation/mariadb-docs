---
description: >-
  Reference of the SQL aggregate functions supported by GridGain — AVG, BIT_AND,
  BIT_OR, COUNT, GROUP_CONCAT, MAX, MIN, SUM, and statistical aggregates.
---

# Aggregate Functions

{% hint style="info" %}
Aggregates are allowed only in SELECT statements.
{% endhint %}

## AVG

### Description

Computes and returns the average (mean) value of the specified parameter for the selected table rows. If no rows are selected, the result is `NULL`. The returned value is of the same data type as the specified parameter.

```sql
AVG ([DISTINCT] expression)
```

### Parameters

- `expression` - any valid numeric expression
- `DISTINCT` - an optional keyword; if present, the function averages unique values only

### Example

Calculate the average players' age:

```sql
SELECT AVG(age) "AverageAge" FROM Players;
```

## BIT_AND

### Description

Returns the bitwise AND of all non-null values. If no rows are selected, the result is `NULL`. A logical AND operation is performed on each pair of corresponding bits of two binary expressions of equal length. In each pair, it returns 1 if the first bit is 1 AND the second bit is 1. Else, it returns 0.

```sql
BIT_AND (expression)
```

### Parameters

`expression` - the input data

## BIT_OR

### Description

Return the bitwise OR of all non-null values. If no rows are selected, the result is `NULL`. A logical OR operation is performed on each pair of corresponding bits of two binary expressions of equal length. In each pair, the result is 1 if the first bit is 1 OR the second bit is 1 OR both bits are 1. Otherwise, the result is 0.

```sql
BIT_OR (expression)
```

### Parameters

`expression` - the input data

## COUNT

### Description

Counts all entries or all non-null values. Returns a long. If no entries are selected, the result is `0`.

```sql
COUNT (* | [DISTINCT] expression)
```

### Example

Calculate the number of players in each city:

```sql
SELECT city_id, COUNT(*) FROM Players GROUP BY city_id;
```

## FIRSTVALUE

### Description

Returns the value of `expression1` associated with the smallest value of `expression2` for each group defined by the `group by` expression in the query.

```sql
FIRSTVALUE ([DISTINCT] <expression1>, <expression2>)
```

This function can only be used with colocated data; you have to use the `colocated` flag when executing the query.

The collocated hint can be set as follows:

- `SqlFieldsQuery.collocated = true` if you use [GridGain SQL API](../../../gridgain8-usage/sql/sql-api.md) to execute queries
- [JDBC connection string parameter]({connectors}/sql/jdbc/jdbc-driver#parameters)
- [ODBC connection string argument]({connectors}/sql/odbc/connection-string-dsn#supported-arguments)

### Example

Return the youngest person for each Company from the Person table and group them by Company ID:

```sql
select company_id, firstvalue(name, age) as youngest from person group by company_id;
```

## GROUP_CONCAT

### Description

Concatenates strings with a separator. The default separator is ',' (without whitespace). Returns a string. If no entries are selected, the result is `NULL`.

```sql
GROUP_CONCAT([DISTINCT] expression || [expression || [expression ...]]
  [ORDER BY expression [ASC|DESC], [[ORDER BY expression [ASC|DESC]]]
  [SEPARATOR expression])
```

`Expression` can be a concatenation of columns and strings with the `||` operator; for example: `column1 || "=" || column2`.

### Parameters

- `DISTINCT` - filters the result set for unique sets of expressions
- `expression` - specifies an expression that may be a column name, a result of another function, or a math operation
- `ORDER BY` - orders rows by expression
- `SEPARATOR` - overrides a string separator; by default, the separator character is the comma ','

{% hint style="info" %}
The `DISTINCT` and `ORDER BY` expressions inside the GROUP_CONCAT function are only supported if you group the results by the primary or affinity key (i.e., use `GROUP BY`). Moreover, you have declare that your data is colocated by specifying the `collocated=true` property in the connection string or by calling `SqlFieldsQuery.setCollocated(true)` if you use the [Java API](https://www.gridgain.com/sdk/8.10/javadoc/org/apache/ignite/cache/query/SqlFieldsQuery.html#setCollocated-boolean-).
{% endhint %}

### Example

Group all players' names in one row:

```sql
SELECT GROUP_CONCAT(name ORDER BY id SEPARATOR ', ') FROM Players;
```

## LASTVALUE

### Description

Returns the value of `expression1` associated with the largest value of `expression2` for each group defined by the `group by` expression.

```sql
LASTVALUE ([DISTINCT] <expression1>, <expression2>)
```

This function can only be used with colocated data and you have to use the `collocated` flag when executing the query.

The colocated hint can be set as follows:

- `SqlFieldsQuery.collocated=true` if you use [GridGain SQL API](../../../gridgain8-usage/sql/sql-api.md) to execute queries
- [JDBC connection string parameter]({connectors}/sql/jdbc/jdbc-driver#parameters)
- [ODBC connection string argument]({connectors}/sql/odbc/connection-string-dsn#supported-arguments)

### Example

Return the oldest person for each Company from the Person table and group them by Company ID:

```sql
select company_id, lastvalue(name, age) as oldest from person group by company_id;
```

## MAX

### Description

Returns the highest value for the specified parameter. If no entries are selected, the result is `NULL`. The returned value is of the same data type as the parameter.

```sql
MAX (expression)
```

### Parameters

`expression` - may be a column name, a result of another function, or a math operation

### Example

Return the height of the tallest player:

```sql
SELECT MAX(height) FROM Players;
```

## MIN

### Description

Returns the lowest value for the specified parameter. If no entries are selected, the result is `NULL`. The returned value is of the same data type as the parameter.

```sql
MIN (expression)
```

### Parameters

`expression` - may be a column name, a result of another function, or a math operation

### Example

Return the age of the youngest player:

```sql
SELECT MIN(age) FROM Players;
```

## SUM

### Description

Returns the sum of all values of a parameter. If no entries are selected, the result is `NULL`. The data type of the returned value depends on the parameter data type.

```sql
SUM ([DISTINCT] expression)
```

### Parameters

- `DISTINCT` - sum up unique values only
- `expression` - may be a column name, a result of another function, or a math operation

### Example

Get the total number of goals scored by all players:

```sql
SELECT SUM(goal) FROM Players;
```

## STDDEV_POP

### Description

Returns the standard deviation value for a population (`double`). If no entries are selected, the result is `NULL`.

```sql
STDDEV_POP ([DISTINCT] expression)
```

### Parameters

- `DISTINCT` - calculate for unique values only
- `expression` - may be a column name, etc.; see [Microsoft language manual](https://learn.microsoft.com/en-us/azure/databricks/sql/language-manual/functions/stddev_pop)

### Example

Calculate the standard deviation for players' age:

```sql
SELECT STDDEV_POP(age) from Players;
```

## STDDEV_SAMP

### Description

Calculates the standard deviation for a sample (`double`). If no entries are selected, the result is `NULL`.

```sql
STDDEV_SAMP ([DISTINCT] expression)
```

### Parameters

- `DISTINCT` - calculate for unique values only
- `expression` - may be a column name, etc.; see [Microsoft language manual](https://stackoverflow.com/questions/62660321/stddev-pop-vs-stddev-samp)

### Example

Calculate the sample standard deviation for players' age:

```sql
SELECT STDDEV_SAMP(age) from Players;
```

## VAR_POP

### Description

Calculates the *variance* (square of the standard deviation) for a population. It returns a `double`. If no entries are selected, the result is `NULL`.

```sql
VAR_POP ([DISTINCT] expression)
```

### Parameters

- `DISTINCT` - calculate for unique values only
- `expression` - may be a column name, etc.; see [Microsoft language manual](https://learn.microsoft.com/en-us/azure/databricks/sql/language-manual/functions/var_pop)

### Example

Calculate the variance of players' age:

```sql
SELECT VAR_POP (age) from Players;
```

## VAR_SAMP

### Description

Calculates the *variance* (square of the standard deviation) for a sample. It returns a `double`. If no entries are selected, the result is `NULL`.

```sql
VAR_SAMP ([DISTINCT] expression)
```

### Parameters

- `DISTINCT` - calculate for unique values only
- `expression` - may be a column name, etc.; see [Microsoft language manual](https://learn.microsoft.com/en-us/azure/databricks/sql/language-manual/functions/var_samp)

### Example

Calculate the variance of players' age:

```sql
SELECT VAR_SAMP(age) FROM Players;
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
