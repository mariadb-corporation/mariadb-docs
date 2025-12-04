# User-Defined Functions Overview

A user-defined function (UDF) is a historical way to extend MariaDB with a new function that works similar to a native (built-in) MariaDB function such as [ABS( )](../../reference/sql-functions/numeric-functions/abs.md) or [CONCAT( )](../../reference/sql-functions/string-functions/concat.md). It was introduced in 1998 and is generally limited to supporting features that existed at that time.

Statements making use of user-defined functions are not [safe for replication](../../ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication.md).

For an example, see `sql/udf_example.cc` in the source tree. For a collection of existing UDFs go to the [UDF Repository on GitHub](https://github.com/orgs/mysqludf/repositories).

There are alternative ways to add a new function: a native function, which requires modifying and compiling the server source code; a function plugin; or a [stored function](../stored-routines/stored-functions/).

{% @marketo/form formId="4316" %}
