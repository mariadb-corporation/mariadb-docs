---
description: >-
  Reference keywords for date arithmetic. These units, such as DAY, HOUR, and
  MINUTE, specify the interval type used in functions like DATE_ADD and EXTRACT.
---

# Date and Time Units

The `INTERVAL` keyword can be used to add or subtract a time interval of time to a [DATETIME](../../data-types/date-and-time-data-types/datetime.md), [DATE](../../data-types/date-and-time-data-types/date.md) or [TIME](../../data-types/date-and-time-data-types/time.md) value.

The syntax is:

```sql
INTERVAL time_quantity time_unit
```

For example, the `SECOND` unit is used below by the [DATE\_ADD()](date_add.md) function:

```sql
SELECT '2008-12-31 23:59:59' + INTERVAL 1 SECOND;
+-------------------------------------------+
| '2008-12-31 23:59:59' + INTERVAL 1 SECOND |
+-------------------------------------------+
| 2009-01-01 00:00:00                       |
+-------------------------------------------+
```

The following units are valid:

| Unit                | Description                             |
| ------------------- | --------------------------------------- |
| MICROSECOND         | Microseconds                            |
| SECOND              | Seconds                                 |
| MINUTE              | Minutes                                 |
| HOUR                | Hours                                   |
| DAY                 | Days                                    |
| WEEK                | Weeks                                   |
| MONTH               | Months                                  |
| QUARTER             | Quarters                                |
| YEAR                | Years                                   |
| SECOND\_MICROSECOND | Seconds.Microseconds                    |
| MINUTE\_MICROSECOND | Minutes.Seconds.Microseconds            |
| MINUTE\_SECOND      | Minutes.Seconds                         |
| HOUR\_MICROSECOND   | Hours.Minutes.Seconds.Microseconds      |
| HOUR\_SECOND        | Hours.Minutes.Seconds                   |
| HOUR\_MINUTE        | Hours.Minutes                           |
| DAY\_MICROSECOND    | Days Hours.Minutes.Seconds.Microseconds |
| DAY\_SECOND         | Days Hours.Minutes.Seconds              |
| DAY\_MINUTE         | Days Hours.Minutes                      |
| DAY\_HOUR           | Days Hours                              |
| YEAR\_MONTH         | Years-Months                            |

The time units containing an underscore are composite; that is, they consist of multiple base time units. For base time units, `time_quantity` is an integer number. For composite units, the quantity must be expressed as a string with multiple integer numbers separated by any punctuation character.

Example of composite units:

```sql
INTERVAL '2:2' YEAR_MONTH
INTERVAL '1:30:30' HOUR_SECOND
INTERVAL '1!30!30' HOUR_SECOND -- same as above
```

Time units can be used in the following contexts:

* after a [+](../../sql-structure/operators/arithmetic-operators/addition-operator.md) or a [-](../../sql-statements/data-manipulation/selecting-data/joins-subqueries/minus.md) operator;
* with the following `DATE` or `TIME` functions: [ADDDATE()](adddate.md), [SUBDATE()](subdate.md), [DATE\_ADD()](date_add.md), [DATE\_SUB()](date_sub.md), [TIMESTAMPADD()](timestampadd.md), [TIMESTAMPDIFF()](timestampdiff.md), [EXTRACT()](extract.md);
* in the `ON SCHEDULE` clause of [CREATE EVENT](../../sql-statements/data-definition/create/create-event.md) and [ALTER EVENT](../../../server-usage/triggers-events/event-scheduler/alter-event.md);
* when defining a [partitioning](../../sql-statements/data-definition/create/create-table.md#partitions) `BY SYSTEM_TIME` .

## See Also

* [Date and time literals](../../sql-structure/sql-language-structure/date-and-time-literals.md)
* [Operator Precedence](../../sql-structure/operators/operator-precedence.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
