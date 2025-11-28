# SETVAL

## Syntax

```sql
SETVAL(sequence_name, next_value, [is_used, [round]])
```

## Description

Set the next value to be returned for a `SEQUENCE`.

This function is compatible with PostgreSQL syntax, extended with the `round` argument.

If the `is_used` argument is not given or is `1` or `true`, then the next used value will one after the given value. If `is_used` is `0` or `false` then the next generated value will be the given value.

If `round` is used then it will set the `round` value (or the internal cycle count, starting at zero) for the sequence. If `round` is not used, it's assumed to be 0.

`next_value` must be an integer literal.

For `SEQUENCE` tables defined with `CYCLE` (see [CREATE SEQUENCE](../create-sequence.md)) one should use both `next_value` and `round` to define the next value. In this case the current sequence value is defined to be `round`, `next_value`.

The result returned by `SETVAL()` is `next_value` or NULL if the given `next_value` and `round` is smaller than the current value.

`SETVAL()` will not set the `SEQUENCE` value to a something that is less than its current value. This is needed to ensure that `SETVAL()` is replication-safe. If you want to set the `SEQUENCE` to a smaller number, use [ALTER SEQUENCE](../alter-sequence.md).

If `CYCLE` is used, first `round` and then `next_value` are compared to see if the value is bigger than the current value.

Internally, in the MariaDB server, `SETVAL()` is used to inform replicas that a `SEQUENCE` has changed value. The replica may get`SETVAL()` statements out of order, but this is ok as only the biggest one will have an effect.

`SETVAL` requires the [INSERT privilege](../../../sql-statements/account-management-sql-statements/grant.md).

## Examples

```sql
SELECT setval(foo, 42);           -- Next nextval will return 43
SELECT setval(foo, 42, TRUE);     -- Same as above
SELECT setval(foo, 42, FALSE);    -- Next nextval will return 42
```

`SETVAL` setting higher and lower values on a sequence with an increment of 10:

```sql
SELECT NEXTVAL(s);
+------------+
| NEXTVAL(s) |
+------------+
|         50 |
+------------+

SELECT SETVAL(s, 100);
+----------------+
| SETVAL(s, 100) |
+----------------+
|            100 |
+----------------+

SELECT NEXTVAL(s);
+------------+
| NEXTVAL(s) |
+------------+
|        110 |
+------------+

SELECT SETVAL(s, 50);
+---------------+
| SETVAL(s, 50) |
+---------------+
|          NULL |
+---------------+

SELECT NEXTVAL(s);
+------------+
| NEXTVAL(s) |
+------------+
|        120 |
+------------+
```

Example demonstrating `round`:

```sql
CREATE OR REPLACE SEQUENCE s1
  START WITH 1
  MINVALUE 1
  MAXVALUE 99
  INCREMENT BY 1 
  CACHE 20 
  CYCLE;

SELECT SETVAL(s1, 99, 1, 0);
+----------------------+
| SETVAL(s1, 99, 1, 0) |
+----------------------+
|                   99 |
+----------------------+

SELECT NEXTVAL(s1);
+-------------+
| NEXTVAL(s1) |
+-------------+
|           1 |
+-------------+
```

The following statement returns `NULL`, as the given `next_value` and `round` is smaller than the current value:

```sql
SELECT SETVAL(s1, 99, 1, 0);
+----------------------+
| SETVAL(s1, 99, 1, 0) |
+----------------------+
|                 NULL |
+----------------------+

SELECT NEXTVAL(s1);
+-------------+
| NEXTVAL(s1) |
+-------------+
|           2 |
+-------------+
```

Increasing the round from zero to 1 allows `next_value` to be returned:

```sql
SELECT SETVAL(s1, 99, 1, 1);
+----------------------+
| SETVAL(s1, 99, 1, 1) |
+----------------------+
|                   99 |
+----------------------+

SELECT NEXTVAL(s1);
+-------------+
| NEXTVAL(s1) |
+-------------+
|           1 |
+-------------+
```

## See Also

* [Sequence Overview](../sequence-overview.md)
* [ALTER SEQUENCE](../alter-sequence.md)
* [CREATE SEQUENCE](../create-sequence.md)
* [NEXT VALUE FOR](next-value-for-sequence_name.md)
* [PREVIOUS VALUE FOR](previous-value-for-sequence_name.md)
* [Information Schema SEQUENCES Table](../../../system-tables/information-schema/information-schema-tables/information-schema-sequences-table.md)
* [Error 4084: Sequence has run out](../../../error-codes/mariadb-error-codes-4000-to-4099/e4084.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
