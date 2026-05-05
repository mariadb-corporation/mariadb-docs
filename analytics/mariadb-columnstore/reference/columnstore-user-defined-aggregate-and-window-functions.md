---
description: >-
  User-defined aggregate and window functions for MariaDB ColumnStore 1.1 and
  later using a C++ SDK, with distributed execution across PrimProc nodes;
  examples include median and SSQ.
---

# ColumnStore User Defined Aggregate and Window Functions

## Introduction

Starting with MariaDB ColumnStore 1.1, the ability to create and use user-defined aggregate and window functions is supported in addition to scalar functions. With Columnstore 1.2, multiple parameters are supported. A C++ SDK is provided, as well as 3 reference examples that provide additional functions that may be of general use:

* **median—mathematical median**, equivalent to percentile\_cont(0.5).
* **avg\_mode—mathematical mode**, i.e., the most frequent value in the set.
* **SSQ—sum of squares**, i.e., the sum of each number squared in the set.

Similar to built-in functions, the SDK supports distributed aggregate execution, where much of the calculation is scaled out across PrimProc[^1] nodes.

## Using User-Defined Aggregate Functions

The reference examples above are included in the standard build of MariaDB ColumnStore. They can be used by registering them as user-defined aggregate functions. The same can be done for new functions, assuming the instance has the updated libraries included.

From a `mcsmysql` prompt:

```sql
CREATE AGGREGATE FUNCTION median RETURNS REAL soname 'libudf_mysql.so';
CREATE AGGREGATE FUNCTION avg_mode RETURNS REAL soname 'libudf_mysql.so';
CREATE AGGREGATE FUNCTION ssq RETURNS REAL soname 'libudf_mysql.so';
```

After this, they may be used in the same way as any other aggregate or window function, like `SUM`:

```sql
SELECT grade, 
AVG(loan_amnt) AVG, 
MEDIAN(loan_amnt) median 
FROM loanstats 
GROUP BY grade 
ORDER BY grade;
```

## Developing a New Function

This requires a MariaDB ColumnStore source tree and the necessary tools to compile C/C++ code. The SDK and reference examples are available in the `utils/udfsdk` directory of the source tree. It contains the SDK documentation, which is also available here:

* [1.2.x UDAF SDK Guide "1.2.x UDAF SDK Guide"](https://github.com/mariadb-corporation/mariadb-columnstore-engine/blob/master/utils/udfsdk/udfsdk.h)

## Limitations

* The implementation of the median and `avg_mode` functions will scale in memory consumption to the size of the set of unique values in the aggregation.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}

[^1]: PrimProc is the ColumnStore Primitives Processor.
