# ColumnStore SELECT

The `SELECT` statement is used to query the database and display table data. You can add many clauses to filter the data.

## Syntax

```sql
SELECT
[ALL | DISTINCT ]
    select_expr [, select_expr ...]
    [ FROM table_references
      [WHERE where_condition]
      [GROUP BY {col_name | expr | POSITION} [ASC | DESC], ... [WITH ROLLUP]]
      [HAVING where_condition]
      [ORDER BY {col_name | expr | POSITION} [ASC | DESC], ...]
      [LIMIT {[offset,] ROW_COUNT | ROW_COUNT OFFSET OFFSET}]
      [PROCEDURE procedure_name(argument_list)]
      [INTO OUTFILE 'file_name' [CHARACTER SET charset_name] [export_options]
         | INTO DUMPFILE 'file_name' | INTO var_name [, var_name] ]
export_options:
    [{FIELDS | COLUMNS}
        [TERMINATED BY 'string']
        [[OPTIONALLY] ENCLOSED BY 'char']
        [ESCAPED BY 'char']
    ]
    [LINES
        [STARTING BY 'string']
        [TERMINATED BY 'string']
    ]
```



## Projection List (SELECT)

If the same column needs to be referenced more than once in the projection list, a unique name is required for each column using a column alias. The total length of the name of a column, inclusive of the length of functions, in the projection list must be 64 characters or less.

## WHERE

The `WHERE` clause filters data retrieval based on criteria. Note that _`column_alias`_ cannot be used in the `WHERE` clause. The following statement returns rows in the region table where the region = ‘ASIA’:

```sql
SELECT * FROM region WHERE name = ’ASIA’;
```

## GROUP BY

`GROUP BY` groups data based on values in one or more specific columns. The following statement returns rows from the _lineitem_ table where /orderkey_is less than 1 000 000 and groups them by the quantity._

```sql
SELECT quantity, COUNT(*) FROM lineitem WHERE orderkey < 1000000 GROUP BY quantity;
```

## HAVING

`HAVING` is used in combination with the `GROUP BY` clause. It can be used in a `SELECT` statement to filter the records that a `GROUP BY` returns. The following statement returns shipping dates, and the respective quantity where the quantity is 2500 or more.

```sql
SELECT shipdate, COUNT(*) FROM lineitem GROUP BYshipdate HAVING COUNT(*) >= 2500;
```

## ORDER BY

The `ORDER BY` clause presents results in a specific order. Note that the `ORDER BY` clause represents a statement that is post-processed by MariaDB. The following statement returns an ordered _quantity_ column from the _lineitem_ table.

```sql
SELECT quantity FROM lineitem WHERE orderkey < 1000000 ORDER BY quantity;
```

The following statement returns an ordered _shipmode_ column from the _lineitem_ table.

```sql
SELECT shipmode FROM lineitem WHERE orderkey < 1000000 ORDER BY 1;
```

**NOTE:** When `ORDER BY` is used in an inner query and `LIMIT` on an outer query, `LIMIT` is applied first and then `ORDER BY` is applied when returning results.

## UNION

Used to combine the result from multiple `SELECT` statements into a single result set. The `UNION` or `UNION DISTINCT` clause returns query results from multiple queries into one display and discards duplicate results. The `UNION ALL` clause displays query results from multiple queries and does not discard the duplicates. The following statement returns the _`p_name`_ rows in the _part_ table and the _partno_ table and discards the duplicate results:

```sql
SELECT p_name FROM part UNION SELECT p_name FROM  partno;
```

The following statement returns all the _`p_name` rows_ in the _part_ table and the _partno_ table:

```sql
SELECT p_name FROM part UNION ALL SELECT p_name FROM  partno;
```

## LIMIT

A limit is used to constrain the number of rows returned by the `SELECT` statement. `LIMIT` can have up to two arguments. `LIMIT` must contain a row count and may optionally contain an offset of the first row to return (the initial row is 0).

The following statement returns 5 customer keys from the customer table:

```sql
SELECT custkey FROM customer LIMIT 5;
```

The following statement returns 5 customer keys from the customer table beginning at offset 1000:

```sql
SELECT custkey FROM customer LIMIT 1000,5;
```

{% hint style="info" %}
When `LIMIT` is used in a nested query, and the inner query contains an `ORDER BY` clause, `LIMIT` is applied before   `ORDER BY` is applied.
{% endhint %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
