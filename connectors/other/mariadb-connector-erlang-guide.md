---
description: >-
  MySQL/OTP is a native Erlang/OTP client for MariaDB and MySQL databases,
  implementing the MySQL protocol in Erlang with support for transactions,
  SSL, and parameterized queries.
icon: link
---

# Erlang

MySQL/OTP is a driver for connecting Erlang/OTP applications to MySQL and MariaDB databases. It is a native implementation of the MySQL protocol in Erlang.

### MySQL/OTP (Erlang/OTP Client for MariaDB/MySQL)

MySQL/OTP is a native Erlang/OTP client designed for connecting Erlang applications to MySQL and MariaDB databases. It implements the MySQL protocol directly in Erlang, offering robust features for database interaction within an OTP framework.

#### 1. What is MySQL/OTP?

MySQL/OTP acts as a client library, enabling Erlang applications to communicate with MySQL and MariaDB servers. It provides a native Erlang implementation of the MySQL protocol, allowing for efficient and idiomatic database operations within the Erlang/OTP ecosystem.

#### 2. Key Features

* **Mnesia Style Transactions:** Supports nestable transactions that align with Erlang's Mnesia database transaction model.
* **SSL Support:** Secure connections using SSL/TLS.
* **Authentication Methods:** Supports `caching_sha2_password` and `mysql_native_password`.
* **Parametrized Queries:** Utilizes cached unnamed prepared statements for efficient and secure queries.
* **Interruptible Slow Queries:** Allows interrupting slow queries without terminating the connection.
* **Protocol Support:** Implements both the binary protocol (for prepared statements) and the text protocol (for plain queries).

#### 3. Installation

You can add MySQL/OTP as a dependency in your Erlang/OTP project using `erlang.mk`, `rebar` (v2 or v3), or `mix` (for Elixir projects).

**a. Example with `rebar.config` (rebar3):**

Add the following to your `rebar.config` file in the `deps` section:

```erlang
{deps, [
    {mysql, ".*", {git, "https://github.com/mysql-otp/mysql-otp.git", {tag, "2.0.0"}}} % Use the latest stable tag or master
]}.
```

Then run `rebar3 compile` or `rebar3 deps get` to fetch and compile the dependency.

#### 4. Basic Usage

Here are common operations using the `mysql` module:

**a. Connect to the Database:**

Establish a connection to your MariaDB/MySQL server. SSL is optional.

```erlang
% Basic connection
{ok, Pid} = mysql:start_link([{host, "localhost"}, {user, "myuser"}, {password, "mypass"}, {database, "mydb"}]).

% Connection with SSL (example with CA certificate)
% {ok, Pid} = mysql:start_link([{host, "localhost"},
%                                {user, "myuser"},
%                                {password, "mypass"},
%                                {database, "mydb"},
%                                {ssl, [{server_name_indication, disable}, {cacertfile, "/path/to/ca.pem"}]}
%                              ]).
```

Replace `"localhost"`, `"myuser"`, `"mypass"`, and `"mydb"` with your database details.

**b. Execute a SELECT Query (Parameterized):**

```erlang
% Prepared statement with parameters
{ok, ColumnNames, Rows} = mysql:query(Pid, <<"SELECT id, name FROM mytable WHERE status = ?">>, [<<"active">>]),
io:format("Columns: ~p~n", [ColumnNames]),
io:format("Rows: ~p~n", [Rows]).
```

**c. Manipulate Data (INSERT/UPDATE/DELETE):**

```erlang
% Insert data
ok = mysql:query(Pid, "INSERT INTO mytable (col1, col2) VALUES (?, ?)", [<<"value1">>, 123]),
io:format("Insert successful!~n").

% Get info about the last query
LastInsertId = mysql:insert_id(Pid),
AffectedRows = mysql:affected_rows(Pid),
WarningCount = mysql:warning_count(Pid),
io:format("Last Insert ID: ~p, Affected Rows: ~p, Warnings: ~p~n", [LastInsertId, AffectedRows, WarningCount]).
```

**d. Mnesia-style Transaction (Nestable):**

```erlang
% Example of a nested transaction
mysql:transaction(Pid, fun() ->
    ok = mysql:query(Pid, "UPDATE accounts SET balance = balance - 100 WHERE user_id = 1"),
    mysql:transaction(Pid, fun() ->
        ok = mysql:query(Pid, "UPDATE accounts SET balance = balance + 100 WHERE user_id = 2")
    end),
    {atomic, ok} % or {atomic, YourResult}
end).
io:format("Transaction completed.~n").
```

**e. Execute Multiple Queries:**

```erlang
% Example with multiple queries and multiple result sets
{ok, Results} = mysql:query(Pid, "SELECT 1 AS a; SELECT 'hello' AS b;"),
io:format("Multiple Query Results: ~p~n", [Results]).
% Results format: [{[ColumnNames], [Rows]}, {[ColumnNames], [Rows]}]
```

**f. Graceful Timeout Handling:**

You can specify a timeout for queries. If the query exceeds the timeout, it will be interrupted.

```erlang
% Query with a 1000ms (1 second) timeout
{ok, ColumnNames, Rows} = mysql:query(Pid, <<"SELECT SLEEP(5)">>, 1000),
io:format("Query interrupted, result: ~p~n", [Rows]). % SLEEP() typically returns 1 when interrupted
```

**g. Close the Connection:**

Always close the connection when it's no longer needed.

```erlang
mysql:stop(Pid).
io:format("Connection closed.~n").
```

#### Further Resources:

* [MySQL/OTP GitHub Repository](https://github.com/mysql-otp/mysql-otp)
* [Erlang/OTP Documentation](https://www.google.com/search?q=http://erlang.org/doc/man/mysql.html\&authuser=1) (if available on the official Erlang docs)

{% @marketo/form formId="4316" %}
