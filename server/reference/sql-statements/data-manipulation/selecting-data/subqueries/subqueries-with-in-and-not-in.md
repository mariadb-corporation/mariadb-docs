# Subqueries with IN and NOT IN

The `IN` operator tests whether a value is a member of a set of values returned by a subquery. It is the most commonly used construct for equality-based subquery comparisons in MariaDB.

While `IN` is logically related to the `ANY` and `SOME` operators, it has distinct semantics and receives specialized treatment from the query optimizer.

## Syntax

```sql
scalar_expression [NOT] IN (subquery)
```

* `scalar_expression`: An expression that evaluates to a single value.
* `subquery`: A subquery that returns a single column.

## Relationship to ANY and SOME

In MariaDB, `IN` is a synonym for `= ANY`.

* `IN` evaluates to `TRUE` if the comparison returns `TRUE` for at least one row produced by the subquery.
* `IN` evaluates to `FALSE` if the subquery returns no rows.

Despite this logical equivalence, the optimizer applies additional transformations to `IN` subqueries (such as semi-joins) that do not always apply to other quantitative `ANY` comparisons like `> ANY` or `<= SOME`.

## Handling NULL Values

The behavior of `IN` and `NOT IN` follows SQL three-valued logic.

* Source Expression is NULL: If the `scalar_expression` is `NULL`, the result is `NULL`.
* Subquery Contains NULL (IN): If no match is found and the subquery contains at least one `NULL`, the result is `NULL`.
* Subquery Contains NULL (NOT IN): If the subquery returns any `NULL` value, `NOT IN` will always evaluate to `NULL` or `FALSE`, never `TRUE`, even if no matching non-null value exists.

{% hint style="warning" %}
Avoid using `NOT IN` if the subquery columns can contain `NULL` values. In such cases, `NOT EXISTS` is generally safer and more predictable.
{% endhint %}

### NOT IN vs. <> ANY

`NOT IN` and `<> ANY` are not synonyms and represent different logical tests:

| OperatorText | Logical MeaningText                                         | ResultText                                                                               |
| ------------ | ----------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `NOT IN`     | "Is this value absent from the entire set?"                 | Returns `TRUE` only if the value matches no rows in the subquery.                        |
| `<> ANY`     | "Is there at least one value in the set that is different?" | Returns `TRUE` if there is at least one row in the subquery that differs from the value. |

## Optimization and Performance

MariaDB treats `IN` subqueries as high-priority candidates for specific optimizations, including:

* Semi-join transformations: Converting the subquery into a join to improve execution speed.
* Subquery materialization: Storing the subquery result in a temporary internal table to avoid repeated execution.
* IN-to-EXISTS rewrites: Converting the predicate based on cost estimates.

## Examples

The following examples use table `sq1` (values: `50`, `100`) and table `sq2` (values: `40`, `50`, `120`).

### Using IN

```sql
SELECT * FROM sq1 WHERE num1 IN (SELECT num2 FROM sq2);
```

Result: `50` (Because `50` exists in both tables).

### Using NOT IN

```sql
SELECT * FROM sq1 WHERE num1 NOT IN (SELECT num2 FROM sq2);
```

Result: `100` (Because `100` is not present in `sq2`).

### NOT IN with NULL Pitfall

```sql
-- sq1 contains 50, 100
SELECT * FROM sq1 WHERE num1 NOT IN (SELECT NULL);
```

Result: Empty set (The condition evaluates to `NULL` for all rows, so no rows are returned).
