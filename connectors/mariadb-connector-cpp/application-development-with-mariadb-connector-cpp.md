---
description: >-
  C++ applications built with MariaDB Connector/C++ use the sql namespace
  classes for connections, prepared statements, and result sets to interact
  with MariaDB databases.
---

# Application Development with MariaDB Connector/C++

MariaDB Connector/C++ enables C++ applications to establish client connections to MariaDB database products over TLS.

## Build Your Application with Connector/C++

When you build a C++ application, your compiler must link your application with the MariaDB Connector/C++ shared library.

The following g++ ([GNU GCC](https://gcc.gnu.org/)) command demonstrates how to link an application with the MariaDB Connector/C++ shared library using the -lmariadbcpp argument:

```bash
$ g++ -o example example.cpp -std=c++11 -lmariadbcpp
```

If you are not using the g++ compiler, please consult your compiler's manual.

## Header Files

MariaDB Connector/C++ includes several header files. In some cases, developers might find it useful to inspect the MariaDB Connector/C++ header files to view the definitions of classes, functions, and methods.

The header files:

* Contain the definitions of classes, functions, and methods in the `sql` namespace.
* Are installed to the `/usr/include/mariadb/conncpp/` directory by default on Linux.

C++ applications developed using MariaDB Connector/C++ must include the `conncpp.hpp` header file.

When a C++ application includes `conncpp.hpp`, the application will automatically include other header files that are included by `conncpp.hpp`:

* `CallableStatement.hpp`
* `Connection.hpp`
* `DatabaseMetaData.hpp`
* `Driver.hpp`
* `DriverManager.hpp`
* `Exception.hpp`
* `jdbccompat.hpp`
* `ParameterMetaData.hpp`
* `PreparedStatement.hpp`
* `ResultSet.hpp`
* `ResultSetMetaData.hpp`
* `Savepoint.hpp`
* `SQLString.hpp`
* `Statement.hpp`
* `Types.hpp`
* `Warning.hpp`

## Classes

MariaDB Connector/C++ implements many different classes.

Most C++ applications developed using MariaDB Connector/C++ will use some of the following classes:

| Class                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| sql::Connection        | Establish a connection to a MariaDB database product. A Connection can be closed by calling close(), or there is an implicit close when using a smart pointer.                                                                                                                                                                                                                                                                                                                                                        |
| sql::DatabaseMetaData  | Provides detailed information about the database metadata, such as database name, version, schemas, tables, columns, procedures, and support for various features.                                                                                                                                                                                                                                                                                                                                                    |
| sql::Driver            | Implements the non-static connect() method, which is a [connection method](connect-with-mariadb-connectorcpp.md).                                                                                                                                                                                                                                                                                                                                                                                                     |
| sql::DriverManager     | Implements the static getConnection() method, which is a [connection method](connect-with-mariadb-connectorcpp.md).                                                                                                                                                                                                                                                                                                                                                                                                   |
| sql::PreparedStatement | Execute a query that contains variable text. Prepared statements can be used to sanitize input. Therefore, using prepared statements reduces the risk of SQL injection attacks. A PreparedStatement can be closed by calling close(), or there is an implicit close when using a smart pointer. By default, the connector will use client-side prepared statements. To use server-side prepared statements, set the useServerPrepStmts [optional connection parameter](connect-with-mariadb-connectorcpp.md) to true. |
| sql::ResultSet         | Fetch query results. A ResultSet can be closed by calling close(), or there is an implicit close when using a smart pointer.                                                                                                                                                                                                                                                                                                                                                                                          |
| sql::ResultSetMetaData | Provides detailed information about a result set, such as schema name, table name, column names and types, and column attributes; whether a column is auto increment, and nullable.                                                                                                                                                                                                                                                                                                                                   |
| sql::Statement         | Execute a query that does not contain variable text. A Statement can be closed by calling close(), or there is an implicit close when using a smart pointer.                                                                                                                                                                                                                                                                                                                                                          |

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>


{% @marketo/form formId="4316" %}
