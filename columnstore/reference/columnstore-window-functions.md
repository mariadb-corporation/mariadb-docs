# ColumnStore Window Functions



1. [Introduction "Introduction"](columnstore-window-functions.md#introduction)
2. [Syntax "Syntax"](columnstore-window-functions.md#syntax)
3. [Supported Functions "Supported Functions"](columnstore-window-functions.md#supported-functions)
4. [Note "Note"](columnstore-window-functions.md#note)
5. [Examples "Examples"](columnstore-window-functions.md#examples)
6. [Example Schema "Example Schema"](columnstore-window-functions.md#example-schema)
7. [Cumulative Sum and Running Max Example "Cumulative Sum and Running Max Example"](columnstore-window-functions.md#cumulative-sum-and-running-max-example)
8. [Partitioned Cumulative Sum and Running Max Example "Partitioned Cumulative Sum and Running Max Example"](columnstore-window-functions.md#partitioned-cumulative-sum-and-running-max-example)
9. [Ranking / Top Results "Ranking / Top Results"](columnstore-window-functions.md#ranking-top-results)
10. [First and Last Values "First and Last Values"](columnstore-window-functions.md#first-and-last-values)
11. [Prior and Next Example "Prior and Next Example"](columnstore-window-functions.md#prior-and-next-example)
12. [Quartiles Example "Quartiles Example"](columnstore-window-functions.md#quartiles-example)
13. [Percentile Example "Percentile Example"](columnstore-window-functions.md#percentile-example)

## Introduction

MariaDB ColumnStore provides support for window functions broadly following the SQL 2003 specification. A window function allows for calculations relating to a window of data surrounding the current row in a result set. This capability provides for simplified queries in support of common business questions such as cumulative totals, rolling averages, and top 10 lists.

Aggregate functions are utilized for window functions however differ in behavior from a group by query because the rows remain ungrouped. This provides support for cumulative sums and rolling averages, for example.

Two key concepts for window functions are Partition and Frame:

* A Partition is a group of rows, or window, that have the same value for a specific column, for example a Partition can be created over a time period such as a quarter or lookup values.
* The Frame for each row is a subset of the row's Partition. The frame typically is dynamic allowing for a sliding frame of rows within the Partition. The Frame determines the range of rows for the windowing function. A Frame could be defined as the last X rows and next Y rows all the way up to the entire Partition.

Window functions are applied after joins, group by, and having clauses are calculated.

## Syntax

A window function is applied in the select clause using the following syntax:

```
function_name ([expression [, expression ... ]]) OVER ( window_definition )
```

where _window\_definition_ is defined as:

```
[ PARTITION BY expression [, ...] ]
[ ORDER BY expression [ ASC | DESC ] [ NULLS { FIRST | LAST } ] [, ...] ]
[ frame_clause ]
```

PARTITION BY:

* Divides the window result set into groups based on one or more expressions.
* An expression may be a constant, column, and non window function expressions.
* A query is not limited to a single partition by clause. Different partition clauses can be used across different window function applications.
* The partition by columns do not need to be in the select list but do need to be available from the query result set.
* If there is no PARTITION BY clause, all rows of the result set define the group.

ORDER BY

* Defines the ordering of values within the partition.
* Can be ordered by multiple keys which may be a constant, column or non window function expression.
* The order by columns do not need to be in the select list but need to be available from the query result set.
* Use of a select column alias from the query is not supported.
* ASC (default) and DESC options allow for ordering ascending or descending.
* NULLS FIRST and NULL\_LAST options specify whether null values come first or last in the ordering sequence. NULLS\_FIRST is the default for ASC order, and NULLS\_LAST is the default for DESC order.

and the optional _frame\_clause_ is defined as:

```
{ RANGE | ROWS } frame_start
{ RANGE | ROWS } BETWEEN frame_start AND frame_end
```

and the optional _frame\_start_ and _frame\_end_ are defined as (value being a numeric expression):

```
UNBOUNDED PRECEDING
value PRECEDING
CURRENT ROW
value FOLLOWING
UNBOUNDED FOLLOWING
```

RANGE/ROWS:

* Defines the windowing clause for calculating the set of rows that the function applies to for calculating a given rows window function result.
* Requires an ORDER BY clause to define the row order for the window.
* ROWS specify the window in physical units, i.e. result set rows and must be a constant or expression evaluating to a positive numeric value.
* RANGE specifies the window as a logical offset. If the expression evaluates to a numeric value then the ORDER BY expression must be a numeric or DATE type. If the expression evaluates to an interval value then the ORDER BY expression must be a DATE data type.
* UNBOUNDED PRECEDING indicates the window starts at the first row of the partition.
* UNBOUNDED FOLLOWING indicates the window ends at the last row of the partition.
* CURRENT ROW specifies the window start or ends at the current row or value.
* If omitted, the default is ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW.

## Supported Functions

| Function                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Function                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| AVG()                             | The average of all input values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| COUNT()                           | Number of input rows.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| CUME\_DIST()                      | Calculates the cumulative distribution, or relative rank, of the current row to other rows in the same partition. Number of peer or preceding rows / number of rows in partition.                                                                                                                                                                                                                                                                                                                                                  |
| DENSE\_RANK()                     | Ranks items in a group leaving no gaps in ranking sequence when there are ties.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| FIRST\_VALUE()                    | The value evaluated at the row that is the first row of the window frame (counting from 1); null if no such row.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| LAG()                             | The value evaluated at the row that is offset rows before the current row within the partition; if there is no such row, instead return default. Both offset and default are evaluated with respect to the current row. If omitted, offset defaults to 1 and default to null. LAG provides access to more than one row of a table at the same time without a self-join. Given a series of rows returned from a query and a position of the cursor, LAG provides access to a row at a given physical offset prior to that position. |
| LAST\_VALUE()                     | The value evaluated at the row that is the last row of the window frame (counting from 1); null if no such row.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| LEAD()                            | Provides access to a row at a given physical offset beyond that position. Returns value evaluated at the row that is offset rows after the current row within the partition; if there is no such row, instead return default. Both offset and default are evaluated with respect to the current row. If omitted, offset defaults to 1 and default to null.                                                                                                                                                                         |
| MAX()                             | Maximum value of expression across all input values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| MEDIAN()                          | An inverse distribution function that assumes a continuous distribution model. It takes a numeric or datetime value and returns the middle value or an interpolated value that would be the middle value once the values are sorted. Nulls are ignored in the calculation. Not available in MariaDB Columnstore 1.1                                                                                                                                                                                                                |
| MIN()                             | Minimum value of expression across all input values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| NTH\_VALUE()                      | The value evaluated at the row that is the nth row of the window frame (counting from 1); null if no such row.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| NTILE()                           | Divides an ordered data set into a number of buckets indicated by expr and assigns the appropriate bucket number to each row. The buckets are numbered 1 through expr. The expr value must resolve to a positive constant for each partition. Integer ranging from 1 to the argument value, dividing the partition as equally as possible.                                                                                                                                                                                         |
| PERCENT\_RANK()                   | Relative rank of the current row: (rank - 1) / (total rows - 1).                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| PERCENTILE\_CONT()                | An inverse distribution function that assumes a continuous distribution model. It takes a percentile value and a sort specification, and returns an interpolated value that would fall into that percentile value with respect to the sort specification. Nulls are ignored in the calculation. Not available in MariaDB Columnstore 1.1                                                                                                                                                                                           |
| PERCENTILE\_DISC()                | An inverse distribution function that assumes a discrete distribution model. It takes a percentile value and a sort specification and returns an element from the set. Nulls are ignored in the calculation. Not available in MariaDB Columnstore 1.1                                                                                                                                                                                                                                                                              |
| RANK()                            | Rank of the current row with gaps; same as row\_number of its first peer.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| REGR\_COUNT(ColumnY, ColumnX)     | The total number of input rows in which both column Y and column X are nonnull                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| REGR\_SLOPE(ColumnY, ColumnX)     | The slope of the least-squares-fit linear equation determined by the (ColumnX, ColumnY) pairs                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| REGR\_INTERCEPT(ColumnY, ColumnX) | The y-intercept of the least-squares-fit linear equation determined by the (ColumnX, ColumnY) pairs                                                                                                                                                                                                                                                                                                                                                                                                                                |
| REGR\_R2(ColumnY, ColumnX)        | Square of the correlation coefficient. correlation coefficient is the regr\_intercept(ColumnY, ColumnX) for linear model                                                                                                                                                                                                                                                                                                                                                                                                           |
| REGR\_SXX(ColumnY, ColumnX)       | REGR\_COUNT(y, x) \* VAR\_POP(x) for non-null pairs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| REGR\_SXY(ColumnY, ColumnX)       | REGR\_COUNT(y, x) \* COVAR\_POP(y, x) for non-null pairs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| REGR\_SYY(ColumnY, ColumnX)       | REGR\_COUNT(y, x) \* VAR\_POP(y) for non-null pairs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ROW\_NUMBER()                     | Number of the current row within its partition, counting from 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| STDDEV() STDDEV\_POP()            | Computes the population standard deviation and returns the square root of the population variance.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| STDDEV\_SAMP()                    | Computes the cumulative sample standard deviation and returns the square root of the sample variance.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| SUM()                             | Sum of expression across all input values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| VARIANCE() VAR\_POP()             | Population variance of the input values (square of the population standard deviation).                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| VAR\_SAMP()                       | Sample variance of the input values (square of the sample standard deviation).                                                                                                                                                                                                                                                                                                                                                                                                                                                     |



## Examples

### Example Schema

The examples are all based on the following simplified sales opportunity table:

```
create table opportunities (
id int,
accountName varchar(20),
name varchar(128),
owner varchar(7),
amount decimal(10,2),
closeDate date,
stageName varchar(11)
) engine=columnstore;
```

Some example values are (thanks to [www.mockaroo.com](https://www.mockaroo.com) for sample data generation):

| id | accountName | name                                               | owner   | amount    | closeDate  | stageName   |
| -- | ----------- | -------------------------------------------------- | ------- | --------- | ---------- | ----------- |
| id | accountName | name                                               | owner   | amount    | closeDate  | stageName   |
| 1  | Browseblab  | Multi-lateral executive function                   | Bob     | 26444.86  | 2016-10-20 | Negotiating |
| 2  | Mita        | Organic demand-driven benchmark                    | Maria   | 477878.41 | 2016-11-28 | ClosedWon   |
| 3  | Miboo       | De-engineered hybrid groupware                     | Olivier | 80181.78  | 2017-01-05 | ClosedWon   |
| 4  | Youbridge   | Enterprise-wide bottom-line Graphic Interface      | Chris   | 946245.29 | 2016-07-02 | ClosedWon   |
| 5  | Skyba       | Reverse-engineered fresh-thinking standardization  | Maria   | 696241.82 | 2017-02-17 | Negotiating |
| 6  | Eayo        | Fundamental well-modulated artificial intelligence | Bob     | 765605.52 | 2016-08-27 | Prospecting |
| 7  | Yotz        | Extended secondary infrastructure                  | Chris   | 319624.20 | 2017-01-06 | ClosedLost  |
| 8  | Oloo        | Configurable web-enabled data-warehouse            | Chris   | 321016.26 | 2017-03-08 | ClosedLost  |
| 9  | Kaymbo      | Multi-lateral web-enabled definition               | Bob     | 690881.01 | 2017-01-02 | Developing  |
| 10 | Rhyloo      | Public-key coherent infrastructure                 | Chris   | 965477.74 | 2016-11-07 | Prospecting |

The schema, sample data, and queries are available as an attachment to this article.

### Cumulative Sum and Running Max Example

Window functions can be used to achieve cumulative / running calculations on a detail report. In this case a won opportunity report for a 7 day period adds columns to show the accumulated won amount as well as the current highest opportunity amount in preceding rows.

```
select owner, 
accountName, 
CloseDate, 
amount, 
sum(amount) over (order by CloseDate rows between unbounded preceding and current row) cumeWon, 
max(amount) over (order by CloseDate rows between unbounded preceding and current row) runningMax
from opportunities 
where stageName='ClosedWon' 
and closeDate >= '2016-10-02' and closeDate <= '2016-10-09' 
order by CloseDate;
```

with example results:

| owner   | accountName  | CloseDate  | amount    | cumeWon    | runningMax |
| ------- | ------------ | ---------- | --------- | ---------- | ---------- |
| owner   | accountName  | CloseDate  | amount    | cumeWon    | runningMax |
| Bill    | Babbleopia   | 2016-10-02 | 437636.47 | 437636.47  | 437636.47  |
| Bill    | Thoughtworks | 2016-10-04 | 146086.51 | 583722.98  | 437636.47  |
| Olivier | Devpulse     | 2016-10-05 | 834235.93 | 1417958.91 | 834235.93  |
| Chris   | Linkbridge   | 2016-10-07 | 539977.45 | 2458738.65 | 834235.93  |
| Olivier | Trupe        | 2016-10-07 | 500802.29 | 1918761.20 | 834235.93  |
| Bill    | Latz         | 2016-10-08 | 857254.87 | 3315993.52 | 857254.87  |
| Chris   | Avamm        | 2016-10-09 | 699566.86 | 4015560.38 | 857254.87  |

### Partitioned Cumulative Sum and Running Max Example

The above example can be partitioned, so that the window functions are over a particular field grouping such as owner and accumulate within that grouping. This is achieved by adding the syntax "partition by " in the window function clause.

```
select owner,  
accountName,  
CloseDate,  
amount,  
sum(amount) over (partition by owner order by CloseDate rows between unbounded preceding and current row) cumeWon,  
max(amount) over (partition by owner order by CloseDate rows between unbounded preceding and current row) runningMax 
from opportunities  
where stageName='ClosedWon' 
and closeDate >= '2016-10-02' and closeDate <= '2016-10-09'  
order by owner, CloseDate;
```

with example results:

| owner   | accountName  | CloseDate  | amount    | cumeWon    | runningMax |
| ------- | ------------ | ---------- | --------- | ---------- | ---------- |
| owner   | accountName  | CloseDate  | amount    | cumeWon    | runningMax |
| Bill    | Babbleopia   | 2016-10-02 | 437636.47 | 437636.47  | 437636.47  |
| Bill    | Thoughtworks | 2016-10-04 | 146086.51 | 583722.98  | 437636.47  |
| Bill    | Latz         | 2016-10-08 | 857254.87 | 1440977.85 | 857254.87  |
| Chris   | Linkbridge   | 2016-10-07 | 539977.45 | 539977.45  | 539977.45  |
| Chris   | Avamm        | 2016-10-09 | 699566.86 | 1239544.31 | 699566.86  |
| Olivier | Devpulse     | 2016-10-05 | 834235.93 | 834235.93  | 834235.93  |
| Olivier | Trupe        | 2016-10-07 | 500802.29 | 1335038.22 | 834235.93  |

### Ranking / Top Results

The rank window function allows for ranking or assigning a numeric order value based on the window function definition. Using the Rank() function will result in the same value for ties / equal values and the next rank value skipped. The Dense\_Rank() function behaves similarly except the next consecutive number is used after a tie rather than skipped. The Row\_Number() function will provide a unique ordering value. The example query shows the Rank() function being applied to rank sales reps by the number of opportunities for Q4 2016.

```
select owner, 
wonCount, 
rank() over (order by wonCount desc) rank 
from (
  select owner, 
  count(*) wonCount 
  from opportunities 
  where stageName='ClosedWon' 
  and closeDate >= '2016-10-01' and closeDate < '2016-12-31'  
  group by owner
) t
order by rank;
```

with example results (note the query is technically incorrect by using closeDate < '2016-12-31' however this creates a tie scenario for illustrative purposes):

| owner   | wonCount | rank |
| ------- | -------- | ---- |
| owner   | wonCount | rank |
| Bill    | 19       | 1    |
| Chris   | 15       | 2    |
| Maria   | 14       | 3    |
| Bob     | 14       | 3    |
| Olivier | 10       | 5    |

If the dense\_rank function is used the rank values would be 1,2,3,3,4 and for the row\_number function the values would be 1,2,3,4,5.

### First and Last Values

The first\_value and last\_value functions allow determining the first and last values of a given range. Combined with a group by this allows summarizing opening and closing values. The example shows a more complex case where detailed information is presented for first and last opportunity by quarter.

```
select a.year, 
a.quarter, 
f.accountName firstAccountName, 
f.owner firstOwner, 
f.amount firstAmount, 
l.accountName lastAccountName, 
l.owner lastOwner, 
l.amount lastAmount 
from (
  select year, 
  quarter, 
  min(firstId) firstId, 
  min(lastId) lastId 
  from (
    select year(closeDate) year, 
    quarter(closeDate) quarter, 
    first_value(id) over (partition by year(closeDate), quarter(closeDate) order by closeDate rows between unbounded preceding and current row) firstId, 
    last_value(id) over (partition by year(closeDate), quarter(closeDate) order by closeDate rows between current row and unbounded following) lastId 
    from opportunities  where stageName='ClosedWon'
  ) t 
  group by year, quarter order by year,quarter
) a 
join opportunities f on a.firstId = f.id 
join opportunities l on a.lastId = l.id 
order by year, quarter;
```

with example results:

| year | quarter | firstAccountName | firstOwner | firstAmount | lastAccountName | lastOwner | lastAmount |
| ---- | ------- | ---------------- | ---------- | ----------- | --------------- | --------- | ---------- |
| year | quarter | firstAccountName | firstOwner | firstAmount | lastAccountName | lastOwner | lastAmount |
| 2016 | 3       | Skidoo           | Bill       | 523295.07   | Skipstorm       | Bill      | 151420.86  |
| 2016 | 4       | Skimia           | Chris      | 961513.59   | Avamm           | Maria     | 112493.65  |
| 2017 | 1       | Yombu            | Bob        | 536875.51   | Skaboo          | Chris     | 270273.08  |

### Prior and Next Example

Sometimes it useful to understand the previous and next values in the context of a given row. The lag and lead window functions provide this capability. By default the offset is one providing the prior or next value but can also be provided to get a larger offset. The example query is a report of opportunities by account name showing the opportunity amount, and the prior and next opportunity amount for that account by close date.

```
select accountName, 
closeDate,  
amount currentOppAmount, 
lag(amount) over (partition by accountName order by closeDate) priorAmount, lead(amount) over (partition by accountName order by closeDate) nextAmount 
from opportunities 
order by accountName, closeDate 
limit 9;
```

with example results:

| accountName | closeDate  | currentOppAmount | priorAmount | nextAmount |
| ----------- | ---------- | ---------------- | ----------- | ---------- |
| accountName | closeDate  | currentOppAmount | priorAmount | nextAmount |
| Abata       | 2016-09-10 | 645098.45        | NULL        | 161086.82  |
| Abata       | 2016-10-14 | 161086.82        | 645098.45   | 350235.75  |
| Abata       | 2016-12-18 | 350235.75        | 161086.82   | 878595.89  |
| Abata       | 2016-12-31 | 878595.89        | 350235.75   | 922322.39  |
| Abata       | 2017-01-21 | 922322.39        | 878595.89   | NULL       |
| Abatz       | 2016-10-19 | 795424.15        | NULL        | NULL       |
| Agimba      | 2016-07-09 | 288974.84        | NULL        | 914461.49  |
| Agimba      | 2016-09-07 | 914461.49        | 288974.84   | 176645.52  |
| Agimba      | 2016-09-20 | 176645.52        | 914461.49   | NULL       |

### Quartiles Example

The NTile window function allows for breaking up a data set into portions assigned a numeric value to each portion of the range. NTile(4) breaks the data up into quartiles (4 sets). The example query produces a report of all opportunities summarizing the quartile boundaries of amount values.

```
select t.quartile, 
min(t.amount) min, 
max(t.amount) max 
from (
  select amount, 
  ntile(4) over (order by amount asc) quartile 
  from opportunities 
  where closeDate >= '2016-10-01' and closeDate <= '2016-12-31'
  ) t 
group by quartile 
order by quartile;
```

With example results:

| quartile | min       | max       |
| -------- | --------- | --------- |
| quartile | min       | max       |
| 1        | 6337.15   | 287634.01 |
| 2        | 288796.14 | 539977.45 |
| 3        | 540070.04 | 748727.51 |
| 4        | 753670.77 | 998864.47 |

### Percentile Example

The percentile functions have a slightly different syntax from other window functions as can be seen in the example below. These functions can be only applied against numeric values. The argument to the function is the percentile to evaluate. Following 'within group' is the sort expression which indicates the sort column and optionally order. Finally after 'over' is an optional partition by clause, for no partition clause use 'over ()'. The example below utilizes the value 0.5 to calculate the median opportunity amount in the rows. The values differ sometimes because percentile\_cont will return the average of the 2 middle rows for an even data set while percentile\_desc returns the first encountered in the sort.

```
select owner,  
accountName,  
CloseDate,  
amount,
percentile_cont(0.5) within group (order by amount) over (partition by owner) pct_cont,
percentile_disc(0.5) within group (order by amount) over (partition by owner) pct_disc
from opportunities  
where stageName='ClosedWon' 
and closeDate >= '2016-10-02' and closeDate <= '2016-10-09'  
order by owner, CloseDate;
```

With example results:

| owner   | accountName  | CloseDate  | amount    | pct\_cont         | pct\_disc |
| ------- | ------------ | ---------- | --------- | ----------------- | --------- |
| owner   | accountName  | CloseDate  | amount    | pct\_cont         | pct\_disc |
| Bill    | Babbleopia   | 2016-10-02 | 437636.47 | 437636.4700000000 | 437636.47 |
| Bill    | Thoughtworks | 2016-10-04 | 146086.51 | 437636.4700000000 | 437636.47 |
| Bill    | Latz         | 2016-10-08 | 857254.87 | 437636.4700000000 | 437636.47 |
| Chris   | Linkbridge   | 2016-10-07 | 539977.45 | 619772.1550000000 | 539977.45 |
| Chris   | Avamm        | 2016-10-09 | 699566.86 | 619772.1550000000 | 539977.45 |
| Olivier | Devpulse     | 2016-10-05 | 834235.93 | 667519.1100000000 | 500802.29 |
| Olivier | Trupe        | 2016-10-07 | 500802.29 | 667519.1100000000 | 500802.29 |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
