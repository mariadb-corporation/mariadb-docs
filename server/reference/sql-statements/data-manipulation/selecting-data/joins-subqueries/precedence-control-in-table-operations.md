---
description: >-
  Control the execution order of UNION, EXCEPT, and INTERSECT operations. Learn
  how to use parentheses to define explicit operation priority.
---

# Precedence Control in Table Operations

You can control the ordering of execution on table operations using parentheses.

## Syntax

```sql
(  expression )
[ORDER BY [column[, column...]]]
[LIMIT {[offset,] row_count | row_count OFFSET offset}]
```

## Description

Using parentheses in your SQL allows you to control the order of execution for [SELECT](../select.md) statements and [Table Value Constructor](../../../../sql-structure/sql-language-structure/table-value-constructors.md), including [UNION](union.md), [EXCEPT](except.md), and [INTERSECT](intersect.md) operations. MariaDB executes the parenthetical expression before the rest of the statement. You can then use [ORDER BY](../order-by.md) and [LIMIT](../limit.md) clauses the further organize the result-set.

**Note**: In practice, the Optimizer may rearrange the exact order in which MariaDB executes different parts of the statement. When it calculates the result-set, however, it returns values as though the parenthetical expression were executed first.

## Example

```sql
CREATE TABLE test.t1 (num INT);

INSERT INTO test.t1 VALUES (1),(2),(3);

(SELECT * FROM test.t1 
 UNION 
 VALUES (10)) 
INTERSECT 
VALUES (1),(3),(10),(11);
+------+
| num  |
+------+
|    1 |
|    3 |
|   10 |
+------+

((SELECT * FROM test.t1 
  UNION 
  VALUES (10)) 
 INTERSECT 
 VALUES (1),(3),(10),(11)) 
ORDER BY 1 DESC;
+------+
| num  |
+------+
|   10 |
|    3 |
|    1 |
+------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
