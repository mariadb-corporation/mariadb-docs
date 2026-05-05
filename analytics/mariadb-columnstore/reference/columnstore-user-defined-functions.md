---
description: >-
  User-defined scalar functions for MariaDB ColumnStore (1.0.10+) require both
  the MariaDB server UDF API and the ColumnStore distributed UDF API to
  execute across PrimProc nodes.
---

# ColumnStore User Defined Functions

## Introduction

MariaDB provides extensibility support through user defined functions (UDFs). For more details on the MariaDB server framework see [User-Defined Functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/user-defined-functions). This documentation applies to MariaDB ColumnStore version 1.0.10 and above.

MariaDB ColumnStore provides scale-out query processing. As such, it requires a separate distributed implementation of each SQL function. This allows for the function application to happen on each PrimProc[^1] server node, providing distributed scale-out performance.

Thus, to fully implement a user defined function for MariaDB ColumnStore requires implementing 2 different APIs:

* **The MariaDB server UDF API** allows utilization on all storage engines, and is the implementation used if applied in the select list.
* **The ColumnStore distributed UDF API** enables distributed execution of `WHERE` clause and `GROUP BY` usage of the function, and is pushed down to PrimProc[^1] nodes for execution where possible.

MariaDB ColumnStore supports user-defined function implementations in C/C++. User-defined aggregate and window functions are not supported in ColumnStore 1.0.

## Developing a User-Defined Function

The development kit can be found under the [utils/udfsdk](https://github.com/mariadb-corporation/mariadb-columnstore-engine/tree/master/utils/udfsdk) directory of the mariadb-columnstore-engine source tree. Developing a UDF requires setting up a development environment and familiarity with c++ development. To set up a ColumnStore development environment, follow the instructions on dependencies in the [ColumnStore server fork](https://github.com/mariadb-corporation/mariadb-columnstore-server) repository.

Three main files need to be modified in order to add a new UDF:

* **udfmysql.cpp:** MariaDB server UDF implementation.
* **udfsdk.h:** Class headers.
* **udfsdk.cpp:** Distributed ColumnStore UDF implementation.

Two reference implementations are provided for guidance on creating your own functions:

* **MCS\_IsNull:** Illustrates a simple single-argument function, providing the ability to return a Boolean if the expression parameter is `NULL`.
* **MCS\_Add:** Illustrates a simple two-argument function that adds two values and return the sum.

It is simplest to copy these and adapt to your needs. There are no system dependencies on the included reference implementations so these can be removed to simplify the class files if preferred.

### MariaDB Server UDF Implementation

Three functions are required to be implemented (for more details see [user-defined-functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/user-defined-functions)):

* **x\_init:** Performs any parameter validation or setup such as memory allocation.
* **x:** Performs the actual function implementation.
* **x\_deinit:** Performs any cleanup tasks such as deallocating memory where 'x' is the function name.

### ColumnStore Distributed UDF Implementation

The function name and class must be registered in order to be recognized and used by the ColumnStore primitives processor (PrimProc). This is done by adding a line to perform the registration in the `UDFSDK::UDFMap()`\_\` function in the file **udfsdk.cpp**:

```c
FuncMap UDFSDK::UDFMap() const
{
	FuncMap fm;
	
	// first: function name
	// second: Function pointer
	// please use lower case for the function name. Because the names might be 
	// case-insensitive in MariaDB depending on the setting. In such case,
	// the function names passed to the interface is always in lower case.
	fm["mcs_add"] = new MCS_add();
	fm["mcs_isnull"] = new MCS_isnull();

	return fm;
}
```

For a new UDF, add a new entry to the FuncMap object, mapping the name to the udf class.

The UDF class should be defined in file **udfsdk.h** and implemented in file **udfsdk.cpp**. It is easiest to adapt the example classes for new instance but each class must implement the `funcexp::Func`\_\` C++ class definition:

* **constructor:** any initialization necessary.
* **destructor:** any de-initialization.
* **getOperationType** performs parameter validation and returns the result data type.
* **getVal** computes and returns the value of the UDF for each given return datatype.

The code changes can be built using `make` within the directory **utils/udfsdk**, this creates the following libraries in the same directory:

* libudf\_mysql.so.1.0.0
* libudfsdk.so.1.0.0

Those libraries contain the compiled code.

### Deploying and Using a UDF

The two libraries created before must be deployed to the **/usr/local/mariadb/columnstore/lib** directory (or equivalent lib directory in a non-root installation), replacing the existing files. Symbolic links in the MariaDB server directory point to these, but should be validated. Run the following as root from the **utils/udfsdk** directory in the build tree (specifying a password to `restartSystem` if needed for a multi-server cluster):

```bash
$ cp libudf_mysql.so.1.0.0 libudfsdk.so.1.0.0 /usr/local/mariadb/columnstore/lib/
$ ls -l /usr/local/mariadb/columnstore/mysql/lib/plugin/libudf_mysql.so
lrwxrwxrwx. 1 root root 56 Jul 19 09:47 /usr/local/mariadb/columnstore/mysql/lib/plugin/libudf_mysql.so -> /usr/local/mariadb/columnstore/lib/libudf_mysql.so.1.0.0
```

Repeat this for each ColumnStore PrimProc[^1] node in the cluster, then restart ColumnStore to make the libraries available.

After restarting the system, the UDF must be registered with the MariaDB server so it can be used:

```sql
$ mcsmysql
    > create function mcs_add returns integer soname 'libudf_mysql.so';
```

The function `mcs_add` can now be used. Verify that it can be used both in the `SELECT` list and `WHERE` clause for correct installation:

```sql
MariaDB [test]> create function mcs_add returns integer soname 'libudf_mysql.so';
Query OK, 0 rows affected (0.01 sec)

MariaDB [test]> create table t1(i1 int, i2 int) engine=columnstore;
Query OK, 0 rows affected (0.58 sec)

MariaDB [test]> insert into t1 values (1,1), (2,2);
Query OK, 2 rows affected (0.24 sec)
Records: 2  Duplicates: 0  Warnings: 0

MariaDB [test]> select i1, i2, mcs_add(i1,i2) sum from t1;
+------+------+------+
| i1   | i2   | sum  |
+------+------+------+
|    1 |    1 |    2 |
|    2 |    2 |    4 |
+------+------+------+
2 rows in set (0.05 sec)

MariaDB [test]> select i1, i2 from t1 where mcs_add(i1,i2) = 4;
+------+------+
| i1   | i2   |
+------+------+
|    2 |    2 |
+------+------+
1 row in set (0.02 sec)
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}

[^1]: PrimProc is the ColumnStore Primitives Processor.
