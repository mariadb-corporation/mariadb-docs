# ALTER SEQUENCE

### Syntax

```sql
ALTER SEQUENCE [IF EXISTS] sequence_name
[AS { TINYINT | SMALLINT | |MEDIUMINT | INT | INTEGER | BIGINT } [SIGNED | UNSIGNED]]
[ INCREMENT [ BY | = ] number ]
[ MINVALUE [=] number | NO MINVALUE | NOMINVALUE ]
[ MAXVALUE [=] number | NO MAXVALUE | NOMAXVALUE ]
[ START [ WITH | = ] number ] [ CACHE [=] number ] [ [ NO ] CYCLE ]
[ RESTART [[WITH | =] number]
```

`ALTER SEQUENCE` allows one to change any values for a `SEQUENCE` created with [CREATE SEQUENCE](create-sequence.md).

The options for `ALTER SEQUENCE` can be given in any order.

### Description

`ALTER SEQUENCE` changes the parameters of an existing sequence generator. Any parameters not specifically set in the `ALTER SEQUENCE` command retain their prior settings.

`ALTER SEQUENCE` requires the [ALTER privilege](../../sql-statements/account-management-sql-statements/grant.md).

#### Options to `ALTER SEQUENCE`

| Option    | Default value                                                | Description                                                                                                                                                                 |
| --------- | ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| INCREMENT | 1                                                            | Increment to use for values. May be negative.                                                                                                                               |
| MINVALUE  | 1 if INCREMENT > 0 and -9223372036854775807 if INCREMENT < 0 | Minimum value for the sequence.                                                                                                                                             |
| MAXVALUE  | 9223372036854775806 if INCREMENT > 0 and -1 if INCREMENT < 0 | Max value for sequence.                                                                                                                                                     |
| START     | MINVALUE if INCREMENT > 0 and MAX\_VALUE if INCREMENT< 0     | First value that the sequence will generate.                                                                                                                                |
| CACHE     | 1000                                                         | Number of values that should be cached. 0 if no CACHE. The underlying table will be updated first time a new sequence number is generated and each time the cache runs out. |
| CYCLE     | 0 (= NO CYCLE)                                               | 1 if the sequence should start again from MINVALUE                                                                                                                          |

The optional clause `RESTART [ WITH restart ]` sets the next value for the sequence. This is equivalent to calling the [SETVAL()](sequence-functions/setval.md) function with the `is_used` argument as `0`. The specified value will be returned by the next call of `nextval`. Using `RESTART` with no restart value is equivalent to supplying the start value that was recorded by [CREATE SEQUENCE](create-sequence.md) or last set by `ALTER SEQUENCE START WITH`.

`ALTER SEQUENCE` does not allow to change the sequence so that it's inconsistent:

```sql
CREATE SEQUENCE s1;
ALTER SEQUENCE s1 MINVALUE 10;
ERROR 4061 (HY000): Sequence 'test.t1' values are conflicting

ALTER SEQUENCE s1 MINVALUE 10 RESTART 10;
ERROR 4061 (HY000): Sequence 'test.t1' values are conflicting

ALTER SEQUENCE s1 MINVALUE 10 START 10 RESTART 10;
```

#### INSERT

To allow `SEQUENCE` objects to be backed up by old tools, like [mariadb-dump](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md), one can use `SELECT` to read the current state of a `SEQUENCE` object and use an `INSERT` to update the `SEQUENCE` object. `INSERT` is only allowed if all fields are specified:

```sql
CREATE SEQUENCE s1;
INSERT INTO s1 VALUES(1000,10,2000,1005,1,1000,0,0);
SELECT * FROM s1;

+------------+-----------+-----------+-------+-----------+-------+-------+-------+
| next_value | min_value | max_value | start | increment | cache | cycle | round |
+------------+-----------+-----------+-------+-----------+-------+-------+-------+
|       1000 |        10 |      2000 |  1005 |         1 |  1000 |     0 |     0 |
+------------+-----------+-----------+-------+-----------+-------+-------+-------+

SHOW CREATE SEQUENCE s1;
+-------+--------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                 |
+-------+--------------------------------------------------------------------------------------------------------------+
| s1    | CREATE SEQUENCE `s1` start with 1005 minvalue 10 maxvalue 2000 increment by 1 cache 1000 nocycle ENGINE=Aria |
+-------+--------------------------------------------------------------------------------------------------------------+
```

#### Notes

`ALTER SEQUENCE` will instantly affect all future `SEQUENCE` operations. This is in contrast to some other databases where the changes requested by `ALTER SEQUENCE` will not be seen until the sequence cache has run out.

`ALTER SEQUENCE` will take a full table lock of the sequence object during its (brief) operation. This ensures that `ALTER SEQUENCE` is replicated correctly. If you only want to set the next sequence value to a higher value than current, then you should use [SETVAL()](sequence-functions/setval.md) instead, as this is not blocking.

If you want to change the storage engine or sequence comment, or rename the sequence, you can use [ALTER TABLE](../../sql-statements/data-definition/alter/alter-table/) for this.

### See Also

* [Sequence Overview](sequence-overview.md)
* [CREATE SEQUENCE](create-sequence.md)
* [DROP SEQUENCE](drop-sequence.md)
* [NEXT VALUE FOR](sequence-functions/next-value-for-sequence_name.md)
* [PREVIOUS VALUE FOR](sequence-functions/previous-value-for-sequence_name.md)
* [SETVAL()](sequence-functions/setval.md). Set next value for the sequence.
* [AUTO INCREMENT](../../data-types/auto_increment.md)
* [ALTER TABLE](../../sql-statements/data-definition/alter/alter-table/)
* [Information Schema SEQUENCES Table](../../system-tables/information-schema/information-schema-tables/information-schema-sequences-table.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
