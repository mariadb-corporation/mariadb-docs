# Creating User-Defined Functions

[User-defined functions](./) allow MariaDB to be extended with a new function that works like a native (built-in) MariaDB function such as [ABS()](../../reference/sql-functions/numeric-functions/abs.md) or [CONCAT()](../../reference/sql-functions/string-functions/concat.md). It was introduced in 1998 and is generally limited to supporting features that existed at that time. There are alternative ways to add a new function: a native function, which requires modifying and compiling the server source code; a [function plugin](../../reference/plugins/); or a [stored function](../stored-routines/stored-functions/).

Statements making use of user-defined functions are not [safe for replication](../../ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication.md).

Functions are written in C or C++, and to make use of them, the operating system must support dynamic loading.

Each new SQL function requires corresponding functions written in C/C++. In the list below, at least the main function - x() - and one other, are required. _x_ should be replaced by the name of the function you are creating.

All functions need to be thread-safe, so not global or static variables that change can be allocated. Memory is allocated in _x\_init()/ and freed i&#x6E;_x\_deinit()_._

## Simple Functions

### x()

Required for all UDFs; this is where the results are calculated.

| C/C++ type | SQL type                                                            |
| ---------- | ------------------------------------------------------------------- |
| char \*    | [STRING](../../reference/data-types/string-data-types/)             |
| long long  | [INTEGER](../../reference/data-types/numeric-data-types/integer.md) |
| double     | [REAL](../../reference/data-types/numeric-data-types/)              |

DECIMAL functions return string values, and so should be written accordingly. It is not possible to create ROW functions.

### x\_init()

Initialization function for x(). Can be used for the following:

* Check the number of arguments to X() (the SQL equivalent).
* Verify the argument types, or to force arguments to be of a particular type after the function is called.
* Specify whether the result can be NULL.
* Specify the maximum result length.
* For REAL functions, specify the maximum number of decimals for the result.
* Allocate any required memory.

### x\_deinit()

De-initialization function for x(). Used to de-allocate memory that was allocated in x\_init().

### Description

Each time the SQL function _X()_ is called:

* MariaDB will first call the C/C++ initialization function, x\_init(), assuming it exists. All setup are performed, and if it returns an error, the SQL statement is aborted and no further functions are called.
* If there is no x\_init() function, or it has been called and did not return an error, x() is then called once per row.
* After all rows have finished processing, x\_deinit() is called, if present, to clean up by de-allocating any memory that was allocated in x\_init().
* See [User-defined Functions Calling Sequences](user-defined-functions-calling-sequences.md) for more details on the functions.

## Aggregate Functions

The following functions are required for aggregate functions, such as [AVG()](../../reference/sql-functions/aggregate-functions/avg.md) and [SUM()](../../reference/sql-functions/aggregate-functions/sum.md). When using [CREATE FUNCTION](create-function-udf.md), the [AGGREGATE](create-function-udf.md#aggregate) keyword is required.

### x\_clear()

Used to reset the current aggregate, but without inserting the argument as the initial aggregate value for the new group.

### x\_add()

Used to add the argument to the current aggregate.

### x\_remove()

Starting from [MariaDB 10.4](../../server-management/install-and-upgrade-mariadb/upgrading/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-10-4-to-mariadb-10-5.md), improves the support of [window functions](../../reference/sql-functions/special-functions/window-functions/) (so it is not obligatory to add it) and should remove the argument from the current aggregate.

### Description

Each time the aggregate SQL function _X()_ is called:

* MariaDB will first call the C/C++ initialization function, x\_init(), assuming it exists. All setup are performed, and if it returns an error, the SQL statement is aborted and no further functions are called.
* If there is no x\_init() function, or it has been called and did not return an error, x() is then called once per row.
* After all rows have finished processing, x\_deinit() is called, if present, to clean up by de-allocating any memory that was allocated in x\_init().
* MariaDB will first call the C/C++ initialization function, x\_init(), assuming it exists. All setup are performed, and if it returns an error, the SQL statement is aborted and no further functions are called.
* The table is sorted according to the [GROUP BY](../../reference/sql-statements/data-manipulation/selecting-data/group-by.md) expression.
* x\_clear() is called for the first row of each new group.
* x\_add() is called once per row for each row in the same group.
* x() is called when the group changes, or after the last row, to get the aggregate result.
* The latter three steps are repeated until all rows have been processed.
* After all rows have finished processing, x\_deinit() is called, if present, to clean up by de-allocating any memory that was allocated in x\_init().

## Examples

For an example, see `sql/udf_example.cc` in the source tree. For a collection of existing UDFs see [mysqludf](https://github.com/mysqludf).

## See Also

* [Stored Functions](../stored-routines/stored-functions/)
* [Stored Aggregate Functions](../stored-routines/stored-functions/stored-aggregate-functions.md)
* [User-defined Functions Calling Sequences](user-defined-functions-calling-sequences.md)
* [allow-suspicious-udfs](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-allow-suspicious-udfs)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
