# PREVIOUS VALUE FOR

## Syntax

```sql
PREVIOUS VALUE FOR sequence_name
```

or

```sql
LASTVAL(sequence_name)
```

or in Oracle mode ([SQL\_MODE=ORACLE](../../../../server-management/variables-and-modes/sql_mode.md))

```sql
sequence_name.currval
```

`PREVIOUS VALUE FOR` is IBM DB2 syntax while `LASTVAL()` is PostgreSQL syntax.

## Description

Gets the most recent value in the current connection generated from a sequence.

* If the sequence has not yet been used by the connection, `PREVIOUS VALUE FOR` returns `NULL` (the same thing applies with a new connection which doesn't see a last value for an existing sequence).
* If a `SEQUENCE` has been dropped and re-created then it's treated as a new `SEQUENCE` and `PREVIOUS VALUE FOR` will return `NULL`.
* Returns `NULL` if the sequence is complete.
* [FLUSH TABLES](../../../sql-statements/administrative-sql-statements/flush-commands/flush.md) has no effect on `PREVIOUS VALUE FOR`.
* Previous values for all used sequences are stored per connection until connection ends.
* `PREVIOUS VALUE FOR` requires the [SELECT privilege](../../../sql-statements/account-management-sql-statements/grant.md).

## Examples

```sql
CREATE SEQUENCE s START WITH 100 INCREMENT BY 10;

SELECT PREVIOUS VALUE FOR s;
+----------------------+
| PREVIOUS VALUE FOR s |
+----------------------+
|                 NULL |
+----------------------+

# The function works for sequences only, if the table is used an error is generated
SELECT PREVIOUS VALUE FOR t;
ERROR 4089 (42S02): 'test.t' is not a SEQUENCE

# Call the NEXT VALUE FOR s:
SELECT NEXT VALUE FOR s;
+------------------+
| NEXT VALUE FOR s |
+------------------+
|              100 |
+------------------+

SELECT PREVIOUS VALUE FOR s;
+----------------------+
| PREVIOUS VALUE FOR s |
+----------------------+
|                  100 |
+----------------------+
```

Now try to start the new connection and check that the last value is still `NULL`, before updating the value in the new connection after the output of the new connection gets current value (110 in the example below). Note that first connection cannot see this change and the result of last value still remains the same (100 in the example above).

```sql
$ .mysql -uroot test -e"SELECT PREVIOUS VALUE FOR s; SELECT NEXT VALUE FOR s; SELECT PREVIOUS VALUE FOR s;"
+----------------------+
| PREVIOUS VALUE FOR s |
+----------------------+
|                 NULL |
+----------------------+
+------------------+
| NEXT VALUE FOR s |
+------------------+
|              110 |
+------------------+
+----------------------+
| PREVIOUS VALUE FOR s |
+----------------------+
|                  110 |
+----------------------+
```

Returns `NULL` if the sequence has run out:

```sql
CREATE OR REPLACE SEQUENCE s MAXVALUE=2;

SELECT NEXTVAL(s), LASTVAL(s);
+------------+------------+
| NEXTVAL(s) | LASTVAL(s) |
+------------+------------+
|          1 |          1 |
+------------+------------+

SELECT NEXTVAL(s), LASTVAL(s);
+------------+------------+
| NEXTVAL(s) | LASTVAL(s) |
+------------+------------+
|          2 |          2 |
+------------+------------+

SELECT NEXTVAL(s), LASTVAL(s);
ERROR 4084 (HY000): Sequence 'test.s' has run out

SELECT LASTVAL(s);
+------------+
| LASTVAL(s) |
+------------+
|       NULL |
+------------+
```

## See Also

* [Sequence Overview](../sequence-overview.md)
* [CREATE SEQUENCE](../create-sequence.md)
* [ALTER SEQUENCE](../alter-sequence.md)
* [NEXT VALUE FOR](next-value-for-sequence_name.md)
* [SETVAL()](setval.md). Set next value for the sequence.
* [AUTO\_INCREMENT](../../../data-types/auto_increment.md)
* [Information Schema SEQUENCES Table](../../../system-tables/information-schema/information-schema-tables/information-schema-sequences-table.md)
* [Error 4084: Sequence has run out](../../../error-codes/mariadb-error-codes-4000-to-4099/e4084.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
