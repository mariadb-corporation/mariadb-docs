---
description: >-
  The Information Schema ROUTINES table stores information about stored
  procedures and stored functions, including their definitions and properties.
---

# Information Schema ROUTINES Table

The [Information Schema](../) `ROUTINES` table stores information about [stored procedures](../../../../server-usage/stored-routines/stored-procedures/) and [stored functions](../../../../server-usage/stored-routines/stored-functions/).

It contains the following columns:

| Column                     | Description                                                                                                                                                        |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| SPECIFIC\_NAME             |                                                                                                                                                                    |
| ROUTINE\_CATALOG           | Always def.                                                                                                                                                        |
| ROUTINE\_SCHEMA            | Database name associated with the routine.                                                                                                                         |
| ROUTINE\_NAME              | Name of the routine.                                                                                                                                               |
| ROUTINE\_TYPE              | Whether the routine is a PROCEDURE or a FUNCTION.                                                                                                                  |
| DATA\_TYPE                 | The return value's [data type](../../../data-types/) (for stored functions).                                                                                       |
| CHARACTER\_MAXIMUM\_LENGTH | Maximum length.                                                                                                                                                    |
| CHARACTER\_OCTET\_LENGTH   | Same as the CHARACTER\_MAXIMUM\_LENGTH except for multi-byte [character sets](../../../data-types/string-data-types/character-sets/).                              |
| NUMERIC\_PRECISION         | For numeric types, the precision (number of significant digits) for the column. NULL if not a numeric field.                                                       |
| NUMERIC\_SCALE             | For numeric types, the scale (significant digits to the right of the decimal point). NULL if not a numeric field.                                                  |
| DATETIME\_PRECISION        | Fractional-seconds precision, or NULL if not a [time data type](../../../data-types/date-and-time-data-types/).                                                    |
| CHARACTER\_SET\_NAME       | [Character set](../../../data-types/string-data-types/character-sets/) if a non-binary [string data type](../../../data-types/string-data-types/), otherwise NULL. |
| COLLATION\_NAME            | [Collation](../../../data-types/string-data-types/character-sets/) if a non-binary [string data type](../../../data-types/string-data-types/), otherwise NULL.     |
| DATA\_TYPE                 | The column's [data type](../../../data-types/).                                                                                                                    |
| ROUTINE\_BODY              | Always SQL.                                                                                                                                                        |
| ROUTINE\_DEFINITION        | Definition of the routine.                                                                                                                                         |
| EXTERNAL\_NAME             | Always NULL.                                                                                                                                                       |
| EXTERNAL\_LANGUAGE         | Always SQL.                                                                                                                                                        |
| PARAMETER\_STYLE           | Always SQL.                                                                                                                                                        |
| IS\_DETERMINISTIC          | Whether the routine is deterministic (can produce only one result for a given list of parameters) or not.                                                          |
| SQL\_DATA\_ACCESS          | One of READS SQL DATA, MODIFIES SQL DATA, CONTAINS SQL, or NO SQL.                                                                                                 |
| SQL\_PATH                  | Always NULL.                                                                                                                                                       |
| SECURITY\_TYPE             | INVOKER or DEFINER. Indicates which user's privileges apply to this routine.                                                                                       |
| CREATED                    | Date and time the routine was created.                                                                                                                             |
| LAST\_ALTERED              | Date and time the routine was last changed.                                                                                                                        |
| SQL\_MODE                  | The [SQL\_MODE](../../../../server-management/variables-and-modes/sql_mode.md) at the time the routine was created.                                                |
| ROUTINE\_COMMENT           | Comment associated with the routine.                                                                                                                               |
| DEFINER                    | If the SECURITY\_TYPE is DEFINER, this value indicates which user defined this routine.                                                                            |
| CHARACTER\_SET\_CLIENT     | The [character set](../../../data-types/string-data-types/character-sets/) used by the client that created the routine.                                            |
| COLLATION\_CONNECTION      | The [collation](../../../data-types/string-data-types/character-sets/) (and character set) used by the connection that created the routine.                        |
| DATABASE\_COLLATION        | The default [collation](../../../data-types/string-data-types/character-sets/) (and character set) for the database, at the time the routine was created.          |

It provides information similar to, but more complete, than the [SHOW PROCEDURE STATUS](../../../sql-statements/administrative-sql-statements/show/show-procedure-status.md) and [SHOW FUNCTION STATUS](../../../sql-statements/administrative-sql-statements/show/show-function-status.md) statements.

For information about the parameters accepted by the routine, you can query the [information\_schema.PARAMETERS](information-schema-parameters-table.md) table.

## See also

* [Stored Function Overview](../../../../server-usage/stored-routines/stored-functions/stored-function-overview.md)
* [Stored Procedure Overview](../../../../server-usage/stored-routines/stored-procedures/stored-procedure-overview.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
