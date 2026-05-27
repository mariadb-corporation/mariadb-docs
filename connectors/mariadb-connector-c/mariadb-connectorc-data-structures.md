---
description: >-
  Reference for the public data structures in MariaDB Connector/C, including
  MYSQL, MYSQL_RES, MYSQL_STMT, MYSQL_FIELD, MYSQL_BIND, and MYSQL_TIME with
  all member definitions.
---

# MariaDB Connector/C Data Structures

This page describes the public data structures used by MariaDB Connector/C.

### MYSQL

The `MYSQL` structure represents one database connection and is used by most of MariaDB Connector/C's API functions. The MYSQL structure needs to be allocated and initialized by the [mysql\_init()](api-functions/mysql_init.md) API function. It will be released by the [mysql\_close()](api-functions/mysql_close.md) function.

{% hint style="info" %}
The `MYSQL` structure should be considered as opaque; copying or changing values of its members might produce unexpected results, errors or program crashes.
{% endhint %}

### MYSQL\_RES

The `MYSQL_RES` structure represents a result set which contains data and metadata information. It will be returned by the [mysql\_use\_result()](api-functions/mysql_use_result.md), [mysql\_store\_result()](api-functions/mysql_store_result.md) and [mysql\_stmt\_result\_metadata()](api-prepared-statement-functions/mysql_stmt_result_metadata.md) API functions and needs to be released by [mysql\_free\_result()](api-functions/mysql_free_result.md).

{% hint style="info" %}
The `MYSQL_RES` structure should be considered as opaque; copying or changing values of its members might produce unexpected results, errors or program crashes.
{% endhint %}

### MYSQL\_ROW

`MYSQL_ROW` represents an array of character pointers, pointing to the columns of the actual data row.\
Data will be received by the [mysql\_fetch\_row()](api-functions/mysql_fetch_row.md) function. The size of the array is the number of columns for the current row.

{% hint style="info" %}
After freeing the result set with [mysql\_free\_result()](api-functions/mysql_free_result.md) `MYSQL_ROW` becomes invalid.
{% endhint %}

### MYSQL\_STMT

The `MYSQL_STMT` structure represents a prepared statement handle and is used by MariaDB Connector/C's prepared statement API functions. The MYSQL\_STMT structure needs to be allocated and initialized by the [mysql\_stmt\_init()](api-prepared-statement-functions/mysql_stmt_init.md) function and needs to be released by the [mysql\_stmt\_close()](api-prepared-statement-functions/mysql_stmt_close.md) function.

{% hint style="info" %}
The `MYSQL_STMT` structure should be considered as opaque; copying or changing values of its members might produce unexpected results, errors or program crashes.
{% endhint %}

### MYSQL\_FIELD

The `MYSQL_FIELD` structure describes the metadata of a column. It can be obtained by the [mysql\_fetch\_field()](api-functions/mysql_fetch_field.md) function.

It has the following members:

|                         |                    |                                             |
| ----------------------- | ------------------ | ------------------------------------------- |
| char \*                 | name               | The name of the column                      |
| unsigned int            | name\_length       | The length of column name                   |
| char \*                 | org\_name          | The original name of the column             |
| unsigned int            | org\_name\_length  | The length of original column name          |
| char \*                 | table              | The name of the table                       |
| unsigned int            | table\_length      | The length of table name                    |
| char \*                 | org\_table         | The original name of the table              |
| unsigned int            | org\_table\_length | The length of original table name           |
| char \*                 | db                 | The name of the database (schema)           |
| unsigned int            | db\_length         | The length of database name                 |
| char \*                 | catalog            | The catalog name (always 'def')             |
| unsigned int            | catalog\_length    | The length of catalog name                  |
| char \*                 | def                | default value                               |
| unsigned int            | def\_length        | The length of default value                 |
| unsigned int            | length             | The length (width) of the column definition |
| unsigned int            | max\_length        | The maximum length of the column value      |
| unsigned int            | flags              | Flags                                       |
| unsigned int            | decimals           | Number of decimals                          |
| enum enum\_field\_types | type               | Field type                                  |

### MYSQL\_BIND

The `MYSQL_BIND` structure is used to provide parameters for prepared statements or to receive output column value from prepared statements.

|                         |                 |                                                                     |
| ----------------------- | --------------- | ------------------------------------------------------------------- |
| unsigned long \*        | length          | Pointer for the length of the buffer (not used for parameters). The length is ignored for numeric and fixed size data types, as the buffer_type value determines the size of the data. |
| my\_bool \*             | is\_nulll       | Pointer which indicates if column is NULL (not used for parameters) |
| my\_bool \*             | error           | Pointer which indicates if an error occurred                        |
| void \*                 | buffer          | Data buffer which contains or receives data                         |
| char \*                 | u.indicator     | Array of indicator variables for bulk operation parameter           |
| unsigned long           | buffer\_length  | Length of buffer                                                    |
| enum enum\_field\_types | buffer\_type    | [Buffer type](mariadb-connectorc-types-and-definitions.md)          |
| unsigned long           | length\_value   | Used if length pointer is NULL                                      |
| my\_bool                | error\_value    | Used if error pointer is NULL                                       |
| my\_bool                | is\_null\_value | Used if is\_null pointer is NULL                                    |
| my\_bool                | is\_unsigned    | Set if integer type is unsigned                                     |
| my\_bool                | is\_null\_value | Used if value is NULL                                               |

### MYSQL\_TIME

The `MYSQL_TIME` structure is used for date and time values in prepared statements. It has the following members:

|                                   |              |                                    |
| --------------------------------- | ------------ | ---------------------------------- |
| unsigned int                      | year         | Year                               |
| unsigned int                      | month        | Month                              |
| unsigned int                      | day          | Day                                |
| unsigned int                      | hour         | Hour                               |
| unsigned int                      | minute       | Minute                             |
| unsigned int                      | second       | Second                             |
| unsigned long                     | second\_part | Fractional seconds (max. 6 digits) |
| my\_bool                          | neg          | Negative value                     |
| enum enum\_mysql\_timestamp\_type | time\_type   | Type                               |


{% @marketo/form formId="4316" %}
