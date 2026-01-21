---
description: Calculate the difference between two months.
---

# MONTHS\_BETWEEN

`MONTHS_BETWEEN` returns the number of months between dates two dates. If the first date given is later than the second date, the result is positive; otherwise, the result is negative. If both dates are the same days of the month, or both are last days of months, the result is always an integer. Otherwise, the fractional portion of the result based on a 31-day month is calculated, and considered the difference in time components between the dates.

The following example calculates the months between two dates:

```sql
SELECT MONTHS_BETWEEN
       (TO_DATE('02-02-1995','MM-DD-YYYY'),
        TO_DATE('01-01-1995','MM-DD-YYYY') 
       );
```

The result is `1.03225806`.
