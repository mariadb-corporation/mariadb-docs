---
description: >-
  Tasks.cpp is a complete MariaDB Connector/C++ sample demonstrating CRUD
  operations, with setup instructions, compilation steps, and command-line
  usage for a task management database.
---

# MariaDB Connector/C++ Sample Application

Tasks.cpp is a complete sample application that demonstrates `CRUD` (`Create, Read, Update, Delete`) operations using the MariaDB Connector/C++.

## Setup

The tasks.cpp sample application depends on a database, `todo` and the table task.,

Create the example database and table:

```sql
CREATE DATABASE IF NOT EXISTS todo;

CREATE TABLE todo.tasks (
   id INT AUTO_INCREMENT PRIMARY KEY,
   description VARCHAR(200),
   completed BOOLEAN DEFAULT FALSE);
```

Create a user `db_user` with privileges to execute the tasks of the sample application:

```sql
CREATE USER IF NOT EXISTS db_user@192.0.2.1
   IDENTIFIED BY 'db_user_password';

GRANT ALL PRIVILEGES ON todo.* TO db_user@192.0.2.1;
```

Within the tasks.cpp file, navigate to the `main` method, and add the database connection values:

```sql
sql::SQLString url("jdbc:mariadb://192.0.2.1:3306/todo");
sql::Properties properties({{"user", "db_user"}, {"password", "db_user_password"}});
```

```sql
sql::SQLString url("jdbc:mariadb://example.skysql.net:5509/todo");
sql::Properties properties({
      {"user", "db_user"},
      {"password", "db_user_password"},
      {"autocommit", "false"},
      {"useTls", "true"},
      {"tlsCert", "classpath:static/skysql_chain.pem"}
   });
```

## Compiling

After adding the connection details to the tasks.cpp file, build the sample application:

```bash
$ g++ -o tasks tasks.cpp -std=c++11 -lmariadbcpp
```

## Usage

The sample application supports `CRUD` (`Create, Read, Update, Delete`) operations.

### Create

Create a new task record:

```bash
$ ./tasks addTask 'New Task Description'
```

### Read

Read all task records:

```bash
$ ./tasks showTasks
```

If the task got added, the preceding command lists the task:

```bash
id = 1, description = New Task Description, completed = 0
```

### Update

Update an existing task record:

```bash
$ ./tasks updateTaskStatus 1 1
```

If the task got updated, the ./tasks showTasks command lists the updated task:

```bash
id = 1, description = New Task Description, completed = 1
```

### Delete

Delete a task record:

```bash
$ ./tasks deleteTask 1
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
