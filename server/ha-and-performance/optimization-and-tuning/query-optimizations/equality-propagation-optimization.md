# Equality propagation optimization

## Basic idea

Consider a query with a WHERE clause:

```sql
WHERE col1=col2 AND ...
```

the WHERE clause will compute to true only if `col1=col2`. This means that in the rest of the WHERE clause occurrences of `col1` can be substituted with `col2` (with some limitations which are discussed in the next section). This allows the optimizer to infer additional restrictions.

For example:

```sql
WHERE col1=col2 AND col1=123
```

allows to infer a new equality: `col2=123`

```sql
WHERE col1=col2 AND col1 < 10
```

allows to infer that `col2<10`.

## Identity and comparison substitution

There are some limitations to where one can do the substitution, though.

The first and obvious example is the string datatype and collations. Most commonly-used collations in SQL are "case-insensitive", that is `'A'='a'`. Also, most collations have a "PAD SPACE" attribute, which means that comparison ignores the spaces at the end of the value, `'a'='a '`.

Now, consider a query:

```sql
INSERT INTO t1 (col1, col2) VALUES ('ab', 'ab   ');
SELECT * FROM t1 WHERE col1=col2 AND LENGTH(col1)=2
```

Here, `col1=col2`, the values are "equal". At the same time `LENGTH(col1)=2`, while `LENGTH(col2)=4`, which means one can't perform the substitution for the argument of LENGTH(...).

It's not only collations. There are similar phenomena when equality compares columns of different datatypes. The exact criteria of when thy happen are rather convoluted.

The take-away is: **sometimes, X=Y does not mean that one can replace any reference to X with Y**.\
What one CAN do is still replace the occurrence in the comparisons `<`, `>`, `>=`, `<=`, etc.

This is how we get two kinds of substitution:

* Identity substitution: X=Y, and any occurrence of X can be replaced with Y.
* Comparison substitution: X=Y, and an occurrence of X in a comparison (X\<Z) can be replaced with Y (Y\<Z).

## Place in query optimization

(A draft description):\
Let's look at how Equality Propagation is integrated with the rest of the query optimization process.

* First, multiple-equalities are built (TODO example from optimizer trace)
  * If multiple-equality includes a constant, fields are substituted with a constant if possible.
* From this point, all optimizations like range optimization, ref access, etc make use of multiple equalities: when they see a reference to `tableX.columnY` somewhere, they also look at all the columns that tableX.columnY is equal to.
* After the join order is picked, the optimizer walks through the WHERE clause and substitutes each field reference with the "best" one - the one that can be checked as soon as possible.
  * Then, the parts of the WHERE condition are attached to the tables where they can be checked.

### Interplay with ORDER BY optimization

Consider a query:

```sql
SELECT ... FROM ... WHERE col1=col2 ORDER BY col2
```

Suppose, there is an `INDEX(col1)`. MariaDB optimizer is able to figure out that it can use an index on `col1` (or sort by the value of `col1`) in order to resolve `ORDER BY col2`.

## Optimizer trace

Look at these elements:

* `condition_processing`
* `attaching_conditions_to_tables`

## More details

Equality propagation doesn't just happen at the top of the WHERE clause. It is done "at all levels" where a level is:

* A top level of the WHERE clause.
* If the WHERE clause has an OR clause, each branch of the OR clause.
* The top level of any ON expression
* (the same as above about OR-levels)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
