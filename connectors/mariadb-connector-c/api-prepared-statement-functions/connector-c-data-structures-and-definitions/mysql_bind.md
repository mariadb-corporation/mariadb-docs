---
description: >-
  MYSQL_BIND is the MariaDB Connector/C structure used to bind input parameters
  and output result columns to a prepared statement, with support for array
  binding and indicator variables.
---

# MYSQL\_BIND

The `MYSQL_BIND` structure is used to bind parameters (which will be sent to the server) and result sets (output sent from server to client). The `MYSQL_BIND` structure is bound with [mysql\_stmt\_bind\_param()](../mysql_stmt_bind_param.md) or [mysql\_stmt\_bind\_result()](../mysql_stmt_bind_result.md) to a prepared statement.

### Members of MYSQL\_BIND structure

* `enum enum_field_types` field\_type: Type of the buffer for in- or output. For a complete list of types see the [types and definitions](connectorc-types-and-definitions.md) section.
* `void` buffer: Address of a variable, array or structure used for data transfer.
* `unsigned long` buffer\_length: Size of buffer in bytes.
* `unsigned long *` length: Pointer to a length variable for output or array of length elements for input (array binding).
* `my_bool *` error: Pointer to an error variable for output.
* `my_bool *` is\_null: Pointer to a null indicator for output.
* `char *` u.indicator: Array of indicator variables for input (array binding)
* `my_bool` is\_unsigned: Set when numeric data type is unsigned

### Array binding

Array binding for bulk insert/updates was introduced with Connector/C 3.0 and requires [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102) or above. It allows clients to control the number of rows that will be physically transferred between the server and the client in one logical bind or fetch. This can greatly improve the performance of many applications by trading buffer space for time (network traffic) and is a better and more secure alternative to `LOAD DATA LOCAL INFILE`, especially when the data will be generated within application.

#### Indicator variables

Indicator variables are used to represent special semantics like NULL or DEFAULT values.

|                          |                           |
| ------------------------ | ------------------------- |
| Indicator variable       | Description               |
| STMT\_INDICATOR\_NTS     | String is null terminated |
| STMT\_INDICATOR\_NONE    | No semantics              |
| STMT\_INDICATOR\_NULL    | NULL value                |
| STMT\_INDICATOR\_DEFAULT | Use columns default value |
| STMT\_INDICATOR\_IGNORE  | Skip update of column     |

#### Column wise binding

When using column wise binding (the default) the application binds up to 3 arrays to a column: a data array, a length array and optionally an indicator array.

The number of rows has to be set by calling [mysql\_stmt\_attr\_set()](../mysql_stmt_attr_set.md) with the `STMT_ATTR_ARRAY_SIZE` option:

```c
unsigned int array_size= 100;
  mysql_stmt_attr_set(stmt, STMT_ATTR_ARRAY_SIZE, array_size);
```

Each array contains as many elements as specified in the `array_size` parameter.

![column\_wise\_binding](../../../.gitbook/assets/column_wise_binding.png)

An example for column wise binding can be found [here](../prepared-statement-examples/bulk-insert-column-wise-binding.md).

#### Row wise binding

When using row wise binding the application binds up to 3 elements of a structure to a column: a data element, a length element and an optional indicator element.

The application declares the size of the structure with the `STMT_ATTR_ROW_SIZE` attribute and binds the address of each member in the first element of the array:

```c
unsigned int row_size= sizeof(struct my_data);
mysql_stmt_attr_set(stmt, STMT_ATTR_ROW_SIZE, &row_size);
```

Connector/C can now calculate the address of the data for a particular row and column as`address= bind_address + row_nr * row_size` where rows are numbered from 0 to size of rowset - 1.

If `row_size` is zero, column wise binding will be used instead.

![row\_wise\_binding](../../../.gitbook/assets/row_wise_binding.png)

An example for row wise binding can be found [here](../prepared-statement-examples/bulk-insert-row-wise-binding.md).

{% @marketo/form formId="4316" %}
