---
description: >-
  Stored Aggregate Functions allow users to create custom aggregate functions
  that process a sequence of rows and return a single summary result.
---

# Stored Aggregate Functions

[Aggregate functions](../../../reference/sql-functions/aggregate-functions/) are functions that are computed over a sequence of rows and return one result for the sequence of rows.

Creating a custom aggregate function is done using the [CREATE FUNCTION](../../../reference/sql-statements/data-definition/create/create-function.md) statement with two main differences:

* The addition of the AGGREGATE keyword, so `CREATE AGGREGATE FUNCTION`
* The `FETCH GROUP NEXT ROW` instruction inside the loop
* Oracle PL/SQL compatibility using SQL/PL is provided

## Standard Syntax

```sql
CREATE AGGREGATE FUNCTION function_name (parameters) RETURNS return_type
BEGIN
      ALL types of declarations
      DECLARE CONTINUE HANDLER FOR NOT FOUND RETURN return_val;
      LOOP
           FETCH GROUP NEXT ROW; // fetches next row FROM TABLE
           other instructions
      END LOOP;
END
```

Stored aggregate functions were a [2016 Google Summer of Code](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/community/contributing-participating/google-summers-of-code/google-summer-of-code-2016) project by Varun Gupta.

### Using SQL/PL

```sql
SET sql_mode=Oracle;
DELIMITER //

CREATE AGGREGATE FUNCTION function_name (parameters) RETURN return_type
   declarations
BEGIN
   LOOP
      FETCH GROUP NEXT ROW; -- fetches next row from table
      -- other instructions

   END LOOP;
EXCEPTION
   WHEN NO_DATA_FOUND THEN
      RETURN return_val;
END //

DELIMITER ;
```

## Examples

First a simplified example:

```sql
CREATE TABLE marks(stud_id INT, grade_count INT);

INSERT INTO marks VALUES (1,6), (2,4), (3,7), (4,5), (5,8);

SELECT * FROM marks;
+---------+-------------+
| stud_id | grade_count |
+---------+-------------+
|       1 |           6 |
|       2 |           4 |
|       3 |           7 |
|       4 |           5 |
|       5 |           8 |
+---------+-------------+

DELIMITER //
CREATE AGGREGATE FUNCTION IF NOT EXISTS aggregate_count(x INT) RETURNS INT
BEGIN
 DECLARE count_students INT DEFAULT 0;
 DECLARE CONTINUE HANDLER FOR NOT FOUND
 RETURN count_students;
      LOOP
          FETCH GROUP NEXT ROW;
          IF x  THEN
            SET count_students = count_students+1;
          END IF;
      END LOOP;
END //
DELIMITER ;
```

A non-trivial example that cannot easily be rewritten using existing functions:

```sql
DELIMITER //
CREATE AGGREGATE FUNCTION medi_int(x INT) RETURNS DOUBLE
BEGIN
  DECLARE CONTINUE HANDLER FOR NOT FOUND
    BEGIN
      DECLARE res DOUBLE;
      DECLARE cnt INT DEFAULT (SELECT COUNT(*) FROM tt);
      DECLARE lim INT DEFAULT (cnt-1) DIV 2;
      IF cnt % 2 = 0 THEN
        SET res = (SELECT AVG(a) FROM (SELECT a FROM tt ORDER BY a LIMIT lim,2) ttt);
      ELSE
        SET res = (SELECT a FROM tt ORDER BY a LIMIT lim,1);
      END IF;
      DROP TEMPORARY TABLE tt;
      RETURN res;
    END;
  CREATE TEMPORARY TABLE tt (a INT);
  LOOP
    FETCH GROUP NEXT ROW;
    INSERT INTO tt VALUES (x);
  END LOOP;
END //
DELIMITER ;
```

### SQL/PL Example

This uses the same marks table as created above.

```sql
SET sql_mode=Oracle;
DELIMITER //

CREATE AGGREGATE FUNCTION aggregate_count(x INT) RETURN INT AS count_students INT DEFAULT 0;
BEGIN
   LOOP
      FETCH GROUP NEXT ROW;
      IF x  THEN
        SET count_students := count_students+1;
      END IF;
   END LOOP;
EXCEPTION
   WHEN NO_DATA_FOUND THEN
      RETURN count_students;
END aggregate_count //
DELIMITER ;

SELECT aggregate_count(stud_id) FROM marks;
```

## See Also

* [Stored Function Overview](stored-function-overview.md)
* [CREATE FUNCTION](../../../reference/sql-statements/data-definition/create/create-function.md)
* [SHOW CREATE FUNCTION](../../../reference/sql-statements/administrative-sql-statements/show/show-create-function.md)
* [DROP FUNCTION](drop-function.md)
* [Stored Routine Privileges](stored-routine-privileges.md)
* [SHOW FUNCTION STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-function-status.md)
* [Information Schema ROUTINES Table](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-routines-table.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
