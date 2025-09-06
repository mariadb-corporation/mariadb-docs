# PERCENTILE\_CONT

## Syntax

## Description

`PERCENTILE_CONT()` (standing for continuous percentile) is a [window function](./) which returns a value which corresponds to the given fraction in the sort order. If required, it will interpolate between adjacent input items.

Essentially, the following process is followed to find the value to return:

* Get the number of rows in the partition, denoted by N
* RN = p\*(N-1), where p denotes the argument to the PERCENTILE\_CONT function
* Calculate FRN as FRN=floor(RN) and CRN as CRN=ceil(RN)
* Look up rows FRN and CRN
* If (CRN = FRN = RN) then the result is (value of expression from row at RN)
* Otherwise the result is
* (CRN - RN) \* (value of expression for row at FRN) +
* (RN - FRN) \* (value of expression for row at CRN)

The [MEDIAN function](median.md) is a specific case of `PERCENTILE_CONT`, equivalent to `PERCENTILE_CONT(0.5)`.

## Examples

```sql
CREATE TABLE book_rating (name CHAR(30), star_rating TINYINT);

INSERT INTO book_rating VALUES ('Lord of the Ladybirds', 5);
INSERT INTO book_rating VALUES ('Lord of the Ladybirds', 3);
INSERT INTO book_rating VALUES ('Lady of the Flies', 1);
INSERT INTO book_rating VALUES ('Lady of the Flies', 2);
INSERT INTO book_rating VALUES ('Lady of the Flies', 5);

SELECT name, PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY star_rating) 
  OVER (PARTITION BY name) AS pc 
  FROM book_rating;
+-----------------------+--------------+
| name                  | pc           |
+-----------------------+--------------+
| Lord of the Ladybirds | 4.0000000000 |
| Lord of the Ladybirds | 4.0000000000 |
| Lady of the Flies     | 2.0000000000 |
| Lady of the Flies     | 2.0000000000 |
| Lady of the Flies     | 2.0000000000 |
+-----------------------+--------------+

SELECT name, PERCENTILE_CONT(1) WITHIN GROUP (ORDER BY star_rating) 
  OVER (PARTITION BY name) AS pc 
  FROM book_rating;
+-----------------------+--------------+
| name                  | pc           |
+-----------------------+--------------+
| Lord of the Ladybirds | 5.0000000000 |
| Lord of the Ladybirds | 5.0000000000 |
| Lady of the Flies     | 5.0000000000 |
| Lady of the Flies     | 5.0000000000 |
| Lady of the Flies     | 5.0000000000 |
+-----------------------+--------------+

SELECT name, PERCENTILE_CONT(0) WITHIN GROUP (ORDER BY star_rating) 
  OVER (PARTITION BY name) AS pc 
  FROM book_rating;
+-----------------------+--------------+
| name                  | pc           |
+-----------------------+--------------+
| Lord of the Ladybirds | 3.0000000000 |
| Lord of the Ladybirds | 3.0000000000 |
| Lady of the Flies     | 1.0000000000 |
| Lady of the Flies     | 1.0000000000 |
| Lady of the Flies     | 1.0000000000 |
+-----------------------+--------------+

SELECT name, PERCENTILE_CONT(0.6) WITHIN GROUP (ORDER BY star_rating) 
  OVER (PARTITION BY name) AS pc 
  FROM book_rating;
+-----------------------+--------------+
| name                  | pc           |
+-----------------------+--------------+
| Lord of the Ladybirds | 4.2000000000 |
| Lord of the Ladybirds | 4.2000000000 |
| Lady of the Flies     | 2.6000000000 |
| Lady of the Flies     | 2.6000000000 |
| Lady of the Flies     | 2.6000000000 |
+-----------------------+--------------+
```

## See Also

* [MEDIAN()](median.md) - a special case of `PERCENTILE_CONT` equivalent to `PERCENTILE_CONT(0.5)`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
