---
description: >-
  The session_connect_attrs table lists connection attributes for the current
  session, offering details about the client library and environment.
---

# Performance Schema session\_connect\_attrs Table

## Description

`session_connect_attrs` is a [Performance Schema](../) table that shows connection attributes for all sessions. The Performance Schema needs to be enabled for the table to be populated.

Applications can pass key/value connection attributes to the server when a connection is made. The `session_connect_attrs` and [session\_account\_connect\_attrs](performance-schema-session_account_connect_attrs-table.md) tables provide access to this information, for all sessions and the current session respectively.

The C API functions [mysql\_options()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_options) and [mysql\_optionsv()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_optionsv) are used for passing connection attributes to the server.

`session_connect_attrs` contains the following columns:

| Column            | Description                                                      |
| ----------------- | ---------------------------------------------------------------- |
| PROCESSLIST\_ID   | Session connection identifier.                                   |
| ATTR\_NAME        | Attribute name.                                                  |
| ATTR\_VALUE       | Attribute value.                                                 |
| ORDINAL\_POSITION | Order in which attribute was added to the connection attributes. |

## Example

Returning the current connection's attributes:

```sql
SELECT * FROM performance_schema.session_connect_attrs WHERE processlist_id=CONNECTION_ID();
+----------------+-----------------+------------------+------------------+
| PROCESSLIST_ID | ATTR_NAME       | ATTR_VALUE       | ORDINAL_POSITION |
+----------------+-----------------+------------------+------------------+
|             45 | _os             | debian-linux-gnu |                0 |
|             45 | _client_name    | libmysql         |                1 |
|             45 | _pid            | 7711             |                2 |
|             45 | _client_version | 10.0.5           |                3 |
|             45 | _platform       | x86_64           |                4 |
|             45 | program_name    | mysql            |                5 |
+----------------+-----------------+------------------+------------------+
```

## Using Other Connectors

### JDBC

Connection attributes values are set using the option [connectionAttributes](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-nodejs/mariadb-connector-node-js-guide).

Example using connection string `jdbc:mariadb://localhost/?connectionAttributes=test:test1,test2:test2Val,test3` :

```sql
SELECT * FROM performance_schema.session_connect_attrs WHERE processlist_id=17;
+----------------+-----------------+---------------------+------------------+
| PROCESSLIST_ID | ATTR_NAME       | ATTR_VALUE          | ORDINAL_POSITION |
+----------------+-----------------+---------------------+------------------+
|             17 | _client_name    | MariaDB Connector/J |                0 |
|             17 | _client_version | 3.1.3               |                1 |
|             17 | _server_host    | localhost           |                2 |
|             17 | _os             | Windows 11          |                3 |
|             17 | _thread         | 1                   |                4 |
|             17 | _java_vendor    | Oracle Corporation  |                5 |
|             17 | _java_version   | 19.0.2              |                6 |
|             17 | test            | test1               |                7 |
|             17 | test2           | test2Val            |                8 |
|             17 | test3           | NULL                |                9 |
+----------------+-----------------+---------------------+------------------+
```

### Node.js

Connection attributes values are set using the option [connectAttributes](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-nodejs/node-js-connection-options).

Example using connection

```javascript
const conn = await mariadb.createConnection({
  host: 'localhost',
  user: 'root',
  connectAttributes: { test: 'test1', test2: 'test2Val', test3: 'f' }
 });
```

```sql
SELECT * FROM performance_schema.session_connect_attrs WHERE processlist_id=30;
+----------------+-----------------+------------------------+------------------+
| PROCESSLIST_ID | ATTR_NAME       | ATTR_VALUE             | ORDINAL_POSITION |
+----------------+-----------------+------------------------+------------------+
|             30 | _client_name    | MariaDB connector/Node |                0 |
|             30 | _client_version | 3.1.1                  |                1 |
|             30 | _server_host    | ::1                    |                2 |
|             30 | _os             | win32                  |                3 |
|             30 | _client_host    | NOSTROMO               |                4 |
|             30 | _node_version   | 18.15.0                |                5 |
|             30 | test            | test1                  |                6 |
|             30 | test2           | test2Val               |                7 |
|             30 | test3           | f                      |                8 |
+----------------+-----------------+------------------------+------------------+
```

### R2DBC

Connection attributes values are set using the option [connectionAttributes](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-r2dbc/mariadb-connector-r2dbc-guide).

Example using connection string `jdbc:mariadb://localhost/?connectionAttributes=test:test1,test2:test2Val,test3`

```java
TreeMap<String, String> connectionAttributes = new TreeMap<>();
    connectionAttributes.put("entry1", "val1");
    connectionAttributes.put("entry2", "val2");

     MariadbConnectionConfiguration conf = MariadbConnectionConfiguration.builder()
             .host("localhost")
             .port(3306) 
             .username("root")
             .connectionAttributes(connectionAttributes)
             .database("test")
             .build();
     MariadbConnectionFactory connFactory = new MariadbConnectionFactory(conf);
     MariadbConnection connection = connFactory.create().block();
```

```sql
SELECT * FROM performance_schema.session_connect_attrs WHERE processlist_id=34;
+----------------+-----------------+--------------------+------------------+
| PROCESSLIST_ID | ATTR_NAME       | ATTR_VALUE         | ORDINAL_POSITION |
+----------------+-----------------+--------------------+------------------+
|             34 | _client_name    | mariadb            |                0 |
|             34 | _client_version | 1.1.4              |                1 |
|             34 | _server_host    | localhost          |                2 |
|             34 | _os             | Windows 11         |                3 |
|             34 | _thread         | 49                 |                4 |
|             34 | _java_vendor    | Oracle Corporation |                5 |
|             34 | _java_version   | 19.0.2             |                6 |
|             34 | entry1          | val1               |                7 |
|             34 | entry2          | val2               |                8 |
+----------------+-----------------+--------------------+------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
