---
description: >-
  Data manipulation language (DML) commands supported by GridGain 9: DELETE,
  INSERT, MERGE, and UPDATE, with their syntax and parameters.
---

# Data Manipulation Language (DML)

This section walks you through all data manipulation language (DML) commands supported by GridGain 9.

## DELETE

Deletes data from a table.

```bnf
DELETE FROM qualified_table_name
  [ [ AS ] alias ]
  [ WHERE booleanExpression ]
  [ LIMIT count ]
```

<!-- Diagram(
Terminal('DELETE FROM'),
NonTerminal('qualified_table_name', {href:'./grammar-reference/#qualified_table_name'}),
Optional(
Sequence(
Optional('AS'),
NonTerminal('alias'),
)
),
Optional(
Sequence(
NonTerminal('WHERE'),
Terminal('booleanExpression')
)
),
Optional(
Sequence(
Terminal('LIMIT'),
NonTerminal('count')
)
)
) -->

### Parameters

- `alias` - an SQL alias for an expression or value.
- `booleanExpression` - an SQL expression that returns a boolean value. Only the records for which `TRUE` was returned will be deleted. If not specified, all records are deleted.
- `count` - the maximum number of rows to delete. Accepts an integer literal or a query parameter.

{% hint style="warning" %}
When more rows match the `WHERE` expression than are specified in the `LIMIT`, there is no guarantee for which matching rows are deleted. For example, if 8 rows match the query and the `LIMIT` is 3, any 3 of the matching rows will be deleted. The statement then returns the number of rows deleted.
{% endhint %}

```sql
DELETE FROM Person WHERE city = 'New York' LIMIT 3;
```

## INSERT

Inserts data into a table.

```bnf
INSERT INTO qualified_table_name [ column_list ] query
```

<!-- Diagram(
Terminal('INSERT INTO'),
NonTerminal('qualified_table_name', {href:'./grammar-reference/#qualified_table_name'}),
Optional(
NonTerminal('column_list', {href:'./grammar-reference/#column_list'}),
),
NonTerminal('query', {href:'./grammar-reference/#query'})
) -->

## MERGE

Merges data into a table.

```bnf
MERGE INTO qualified_table_name [ [ AS ] alias ]
  USING qualified_table_name ON booleanExpression
  [ WHEN MATCHED THEN UPDATE SET assign [, assign]... ]
  [ WHEN NOT MATCHED THEN INSERT VALUES ( value [, value]... ) ]
```

<!-- Diagram(
Terminal('MERGE INTO'),
NonTerminal('qualified_table_name', {href:'./grammar-reference/#qualified_table_name'}),
Optional(
Sequence(
Optional('AS'),
NonTerminal('alias'),
)
),
Terminal('USING'),
NonTerminal('qualified_table_name', {href:'./grammar-reference/#qualified_table_name'}),
Terminal('ON'),
NonTerminal('booleanExpression'),
End({type:'complex'})
)

Diagram(
Start({type:'complex'}),
Optional(
Sequence(
NonTerminal('WHEN MATCHED THEN UPDATE SET'),
OneOrMore(Sequence(Terminal('assign', {href:'./grammar-reference/#assign'})
),
Terminal(',')
))),
Optional(
Sequence(
NonTerminal('WHEN NOT MATCHED THEN INSERT VALUES'),
NonTerminal('('),
OneOrMore(Sequence(Terminal('value')
),
Terminal(',')
),
NonTerminal(')'),
))) -->

{% hint style="info" %}
At least of the `WHEN MATCHED` and `WHEN NOT MATCHED` clauses must be present.
{% endhint %}

### Parameters

- `alias` - an SQL alias for an expression or value.
- `booleanExpression` - an SQL expression that returns a boolean value. If `TRUE` is returned, the `WHEN MATCHED` clause is executed, otherwise the `WHEN NOT MATCHED` is executed.
- `value` - arbitrary value that will be inserted into the table during the operation.

## UPDATE

Updates data in a table.

```bnf
UPDATE qualified_table_name
  SET assign [, assign]...
  [ WHERE booleanExpression ]
```

<!-- Diagram(
Terminal('UPDATE'),
NonTerminal('qualified_table_name', {href:'./grammar-reference/#qualified_table_name'}),
Terminal('SET'),
OneOrMore(Sequence(Terminal('assign', {href:'./grammar-reference/#assign'})
),
Terminal(',')
),
Optional(
Sequence(
Terminal('WHERE'),
NonTerminal('booleanExpression')
)
)
) -->

### Parameters

- `booleanExpression` - an SQL expression that returns a boolean value. Only the records for which `TRUE` was returned will be updated. If not specified, all records will be updated.
