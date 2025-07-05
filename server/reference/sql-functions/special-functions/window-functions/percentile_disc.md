
# PERCENTILE_DISC

## Syntax



## Description


`PERCENTILE_DISC()` (standing for discrete percentile) is a [window function](README.md) which returns the first value in the set whose ordered position is the same or more than the specified fraction.


Essentially, the following process is followed to find the value to return:


* Get the number of rows in the partition.
* Walk through the partition, in order, until finding the first row with [CUME_DIST()](cume_dist.md) >= function_argument.


## Examples


```
CREATE TABLE book_rating (name CHAR(30), star_rating TINYINT);

INSERT INTO book_rating VALUES ('Lord of the Ladybirds', 5);
INSERT INTO book_rating VALUES ('Lord of the Ladybirds', 3);
INSERT INTO book_rating VALUES ('Lady of the Flies', 1);
INSERT INTO book_rating VALUES ('Lady of the Flies', 2);
INSERT INTO book_rating VALUES ('Lady of the Flies', 5);

SELECT name, PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY star_rating)
  OVER (PARTITION BY name) AS pc FROM book_rating;
+-----------------------+------+
| name                  | pc   |
+-----------------------+------+
| Lord of the Ladybirds |    3 |
| Lord of the Ladybirds |    3 |
| Lady of the Flies     |    2 |
| Lady of the Flies     |    2 |
| Lady of the Flies     |    2 |
+-----------------------+------+
5 rows in set (0.000 sec)

SELECT name, PERCENTILE_DISC(0) WITHIN GROUP (ORDER BY star_rating) 
 OVER (PARTITION BY name) AS pc FROM book_rating;
+-----------------------+------+
| name                  | pc   |
+-----------------------+------+
| Lord of the Ladybirds |    3 |
| Lord of the Ladybirds |    3 |
| Lady of the Flies     |    1 |
| Lady of the Flies     |    1 |
| Lady of the Flies     |    1 |
+-----------------------+------+
5 rows in set (0.000 sec)

SELECT name, PERCENTILE_DISC(1) WITHIN GROUP (ORDER BY star_rating) 
  OVER (PARTITION BY name) AS pc FROM book_rating;
+-----------------------+------+
| name                  | pc   |
+-----------------------+------+
| Lord of the Ladybirds |    5 |
| Lord of the Ladybirds |    5 |
| Lady of the Flies     |    5 |
| Lady of the Flies     |    5 |
| Lady of the Flies     |    5 |
+-----------------------+------+
5 rows in set (0.000 sec)

SELECT name, PERCENTILE_DISC(0.6) WITHIN GROUP (ORDER BY star_rating) 
  OVER (PARTITION BY name) AS pc FROM book_rating;
+-----------------------+------+
| name                  | pc   |
+-----------------------+------+
| Lord of the Ladybirds |    5 |
| Lord of the Ladybirds |    5 |
| Lady of the Flies     |    2 |
| Lady of the Flies     |    2 |
| Lady of the Flies     |    2 |
+-----------------------+------
```

## See Also


* [CUME_DIST()](cume_dist.md)


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
