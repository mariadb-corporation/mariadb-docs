---
description: Quickstart Guide for MySQL/OTP (Erlang/OTP Client)
---

# Erlang Guide

***

MySQL/OTP is the native Erlang/OTP client for connecting Erlang applications to MariaDB and MySQL databases, offering a direct implementation of the MySQL protocol.

#### 1. Installation

Add MySQL/OTP as a dependency in your `rebar.config` file (for rebar3 projects):

Erlang

```erlang
{deps, [
    {mysql, ".*", {git, "https://github.com/mysql-otp/mysql-otp.git", {tag, "2.0.0"}}} % Use the latest stable tag
]}.
```

Then, run `rebar3 compile`.

#### 2. Basic Usage

Here are essential steps for connecting and interacting with your database:

**a. Connect:**

Erlang

```erlang
{ok, Pid} = mysql:start_link([{host, "localhost"}, {user, "myuser"}, {password, "mypass"}, {database, "mydb"}]).
```

Replace placeholder values with your actual database credentials.

**b. Execute Query:**

Erlang

```erlang
% Select data
{ok, ColumnNames, Rows} = mysql:query(Pid, <<"SELECT id, name FROM mytable WHERE status = ?">>, [<<"active">>]).

% Insert data
ok = mysql:query(Pid, "INSERT INTO mytable (col1, col2) VALUES (?, ?)", [<<"value1">>, 123]).
```

**c. Close Connection:**

Erlang

```erlang
mysql:stop(Pid).
```

#### Further Resources:

* [MySQL/OTP GitHub Repository](https://github.com/mysql-otp/mysql-otp)
* [Erlang/OTP Documentation](https://www.google.com/search?q=http://erlang.org/doc/man/mysql.html\&authuser=1)

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
