---
description: >-
  The Information Schema SEQUENCES table provides metadata about sequence
  objects, including their minimum, maximum, and current values.
---

# Information Schema SEQUENCES Table

{% hint style="info" %}
This table is available as of MariaDB [11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/what-is-mariadb-115).
{% endhint %}

The [Information Schema](../) `SEQUENCES` table stores information about [sequences](../../../sql-structure/sequences/) on the server.

It contains the following columns. See [CREATE SEQUENCE](../../../sql-structure/sequences/create-sequence.md) for details.

| Column                    | Description                                       |
| ------------------------- | ------------------------------------------------- |
| SEQUENCE\_CATALOG         | Catalog name                                      |
| SEQUENCE\_SCHEMA          | Database name                                     |
| SEQUENCE\_NAME            | Sequence name                                     |
| DATA\_TYPE                | Data type, for example BIGINT or TINYINT UNSIGNED |
| NUMERIC\_PRECISION        |                                                   |
| NUMERIC\_PRECISION\_RADIX |                                                   |
| NUMERIC\_SCALE            |                                                   |
| START\_VALUE              |                                                   |
| MINIMUM\_VALUE            |                                                   |
| MAXIMUM\_VALUE            |                                                   |
| INCREMENT                 |                                                   |
| CYCLE\_OPTION             | 1 if the CYCLE OPTION is set, otherwise 0         |

## Example

```sql
CREATE SEQUENCE s START WITH 100 INCREMENT BY 10;

SELECT * FROM INFORMATION_SCHEMA.SEQUENCES\G
*************************** 1. row ***************************
       SEQUENCE_CATALOG: def
        SEQUENCE_SCHEMA: test
          SEQUENCE_NAME: s
              DATA_TYPE: bigint
      NUMERIC_PRECISION: 64
NUMERIC_PRECISION_RADIX: 2
          NUMERIC_SCALE: 0
            START_VALUE: 100
          MINIMUM_VALUE: 1
          MAXIMUM_VALUE: 9223372036854775806
              INCREMENT: 10
           CYCLE_OPTION: 0
```

## See Also

* [Sequence Overview](../../../sql-structure/sequences/sequence-overview.md)
* [CREATE SEQUENCE](../../../sql-structure/sequences/create-sequence.md)
* [ALTER SEQUENCE](../../../sql-structure/sequences/alter-sequence.md)
* [DROP SEQUENCE](../../../sql-structure/sequences/drop-sequence.md)
* [NEXT VALUE FOR](../../../sql-structure/sequences/sequence-functions/next-value-for-sequence_name.md)
* [PREVIOUS VALUE FOR](../../../sql-structure/sequences/sequence-functions/previous-value-for-sequence_name.md)
* [SETVAL()](../../../sql-structure/sequences/sequence-functions/setval.md). Set next value for the sequence.
* [AUTO INCREMENT](../../../data-types/auto_increment.md)
* [Sequence Storage Engine](../../../../server-usage/storage-engines/sequence-storage-engine.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
