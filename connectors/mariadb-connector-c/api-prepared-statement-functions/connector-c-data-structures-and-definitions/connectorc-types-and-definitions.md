---
description: >-
  Connector/C field types and indicator variables used in the MYSQL_BIND
  structure, including all MYSQL_TYPE constants and STMT_INDICATOR values
  defined in mariadb_com.h.
---

# Connector/C Types and Definitions

### Field types

Field types are used in the [MYSQL\_BIND](mysql_bind.md) structure and represent the type of the fields. Field types are defined in `mariadb_com.h`.

* MYSQL\_TYPE\_BIT
* MYSQL\_TYPE\_BLOB
* MYSQL\_TYPE\_DATE
* MYSQL\_TYPE\_DATETIME
* MYSQL\_TYPE\_DECIMAL
* MYSQL\_TYPE\_DOUBLE
* MYSQL\_TYPE\_ENUM
* MYSQL\_TYPE\_FLOAT
* MYSQL\_TYPE\_GEOMETRY
* MYSQL\_TYPE\_INT24
* MYSQL\_TYPE\_JSON
* MYSQL\_TYPE\_LONG
* MYSQL\_TYPE\_LONGLONG
* MYSQL\_TYPE\_LONG\_BLOB
* MYSQL\_TYPE\_MEDIUM\_BLOB
* MYSQL\_TYPE\_NEWDATE
* MYSQL\_TYPE\_NEWDECIMAL
* MYSQL\_TYPE\_NULL
* MYSQL\_TYPE\_SET
* MYSQL\_TYPE\_SHORT
* MYSQL\_TYPE\_STRING
* MYSQL\_TYPE\_TIME
* MYSQL\_TYPE\_TIMESTAMP
* MYSQL\_TYPE\_TINY
* MYSQL\_TYPE\_TINY\_BLOB
* MYSQL\_TYPE\_VARCHAR
* MYSQL\_TYPE\_VAR\_STRING
* MYSQL\_TYPE\_YEAR

### Indicator variables

Indicator variables store supplementary information which will be sent to the server.

|                          |                                                |
| ------------------------ | ---------------------------------------------- |
| STMT\_INDICATOR\_NONE    | no indicator (=0)                              |
| STMT\_INDICATOR\_NTS     | (string) buffer is null/zero terminated string |
| STMT\_INDICATOR\_NULL    | buffer is null                                 |
| STMT\_INDICATOR\_DEFAULT | use columns default value                      |
| STMT\_INDICATOR\_IGNORE  | do not update column value                     |


{% @marketo/form formId="4316" %}
