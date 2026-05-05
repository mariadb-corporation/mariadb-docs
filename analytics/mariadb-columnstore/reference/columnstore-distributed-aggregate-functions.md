---
description: >-
  MariaDB ColumnStore distributed aggregate functions usable in SELECT,
  HAVING, and ORDER BY: AVG, COUNT, MAX, MIN, CORR, COVAR_POP, COVAR_SAMP, and
  other statistical aggregates.
---

# ColumnStore Distributed Aggregate Functions

## Functions

MariaDB ColumnStore supports the following aggregate functions, these can be used in the `SELECT`, `HAVING`, and `ORDER BY` clauses of the SQL statement.

| Function                           | Description                                                                                                              |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| AVG(\[DISTINCT] column)            | Average value of a numeric (INT variations, NUMERIC, DECIMAL) column                                                     |
| CORR (ColumnY, ColumnX)            | The correlation coefficient for non-null pairs in a group.                                                               |
| COUNT (\*, \[DISTINCT] column)     | The number of rows returned by a query or grouping. All datatypes are supported                                          |
| COVAR\_POP (ColumnY, ColumnX)      | The population covariance for non-null pairs in a group.                                                                 |
| COVAR\_SAMP (ColumnY, ColumnX)     | The sample covariance for non-null pairs in a group.                                                                     |
| MAX (\[DISTINCT] column)           | The maximum value of a column. All datatypes are supported.                                                              |
| MIN (\[DISTINCT] column)           | The maximum value of a column. All datatypes are supported.                                                              |
| REGR\_AVGX (ColumnY, ColumnX)      | Average of the independent variable (sum(ColumnX)/N), where N is number of rows processed by the query                   |
| REGR\_AVGY (ColumnY, ColumnX)      | Average of the dependent variable (sum(ColumnY)/N), where N is number of rows processed by the query                     |
| REGR\_COUNT (ColumnY, ColumnX)     | The total number of input rows in which both column Y and column X are nonnull                                           |
| REGR\_INTERCEPT (ColumnY, ColumnX) | The y-intercept of the least-squares-fit linear equation determined by the (ColumnX, ColumnY) pairs                      |
| REGR\_R2(ColumnY, ColumnX)         | Square of the correlation coefficient. correlation coefficient is the regr\_intercept(ColumnY, ColumnX) for linear model |
| REGR\_SLOPE(ColumnY, ColumnX)      | The slope of the least-squares-fit linear equation determined by the (ColumnX, ColumnY) pairs                            |
| REGR\_SXX(ColumnY, ColumnX)        | REGR\_COUNT(y, x) \* VAR\_POP(x) for non-null pairs.                                                                     |
| REGR\_SXY(ColumnY, ColumnX)        | REGR\_COUNT(y, x) \* COVAR\_POP(y, x) for non-null pairs.                                                                |
| REGR\_SYY(ColumnY, ColumnX)        | REGR\_COUNT(y, x) \* VAR\_POP(y) for non-null pairs.                                                                     |
| STD(), STDDEV(), STDDEV\_POP()     | The population standard deviation of a numeric (INT variations, NUMERIC, DECIMAL) column                                 |
| STDDEV\_SAMP()                     | The sample standard deviation of a numeric (INT variations, NUMERIC, DECIMAL) column                                     |
| SUM(\[DISTINCT] column)            | The sum of a numeric (INT variations, NUMERIC, DECIMAL) column                                                           |
| VARIANCE(), VAR\_POP()             | The population standard variance of a numeric (INT variations, NUMERIC, DECIMAL) column                                  |
| VAR\_SAMP()                        | The population standard variance of a numeric (INT variations, NUMERIC, DECIMAL) column                                  |

{% hint style="info" %}
Regression functions (`REGR_AVGX` to `REGR_YY`), `CORR`, `COVAR_POP` and `COVAR_SAMP` are supported for version 1.2.0 and higher
{% endhint %}

## Example

An example group by query using aggregate functions is:

```sql
SELECT year(o_orderdate) order_year, 
AVG(o_totalprice) avg_totalprice, 
MAX(o_totalprice) max_totalprice, 
COUNT(*) order_count 
FROM orders 
GROUP BY order_year 
ORDER BY order_year;
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
