---
description: >-
  Insert multiple rows in a single prepared statement call using column-wise
  binding. This example demonstrates indicator variables and
  STMT_ATTR_ARRAY_SIZE with MariaDB Connector/C.
---

# Bulk Insert (Column-wise Binding)

The following example uses indicator variables and column-wise binding to insert an array of data.

```c
#include <mysql.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

static void show_mysql_error(MYSQL *mysql)
{
  printf("Error(%d) [%s] \"%s\"", mysql_errno(mysql),
                                  mysql_sqlstate(mysql),
                                  mysql_error(mysql));
  exit(-1);
}

static void show_stmt_error(MYSQL_STMT *stmt)
{
  printf("Error(%d) [%s] \"%s\"", mysql_stmt_errno(stmt),
                                  mysql_stmt_sqlstate(stmt),
                                  mysql_stmt_error(stmt));
  exit(-1);
}

int main(int argc, char *argv[])
{
  MYSQL *mysql;
  MYSQL_STMT *stmt;
  MYSQL_BIND bind[3];

  /* Data for insert */
  const char *surnames[]= {"Widenius", "Axmark", "N.N."};
  unsigned long surnames_length[]= {8,6,4};
  const char *forenames[]= {"Monty", "David", "will be replaced by default value"};
  char forename_ind[]= {STMT_INDICATOR_NTS, STMT_INDICATOR_NTS, STMT_INDICATOR_DEFAULT};
  char id_ind[]= {STMT_INDICATOR_NULL, STMT_INDICATOR_NULL, STMT_INDICATOR_NULL};
  unsigned int array_size= 3; 

  mysql= mysql_init(NULL);

  /* connect to MariaDB server */
  if (!mysql_real_connect(mysql, "localhost", "example", "example_pw", 
                          "example_db", 0, "/tmp/mysql.sock", 0))
    show_mysql_error(mysql);

  if (mysql_query(mysql, "DROP TABLE IF EXISTS bulk_example1"))
    show_mysql_error(mysql);

  if (mysql_query(mysql, "CREATE TABLE bulk_example1 (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,"\
                         "forename CHAR(30) NOT NULL DEFAULT 'unknown', surname CHAR(30))"))
    show_mysql_error(mysql);

  stmt= mysql_stmt_init(mysql);
  if (mysql_stmt_prepare(stmt, "INSERT INTO bulk_example1 VALUES (?,?,?)", -1))
    show_stmt_error(stmt);

  memset(bind, 0, sizeof(MYSQL_BIND) * 3);

  /* We autogenerate id's, so all indicators are STMT_INDICATOR_NULL */
  bind[0].u.indicator= id_ind;
  bind[0].buffer_type= MYSQL_TYPE_LONG;

  bind[1].buffer= forenames;
  bind[1].buffer_type= MYSQL_TYPE_STRING;
  bind[1].u.indicator= forename_ind;

  bind[2].buffer_type= MYSQL_TYPE_STRING;
  bind[2].buffer= surnames;
  bind[2].length= &surnames_length;

  /* set array size */
  mysql_stmt_attr_set(stmt, STMT_ATTR_ARRAY_SIZE, &array_size);

  /* bind parameter */
  mysql_stmt_bind_param(stmt, bind);

  /* execute */
  if (mysql_stmt_execute(stmt))
    show_stmt_error(stmt);

  mysql_stmt_close(stmt);
  mysql_close(mysql);
}
```

Now we can check the content of table bulk\_example1:

```sql
MariaDB [example_db]> SELECT id,forename,surname FROM bulk_example1;
+----+----------+----------+
| id | forename | surname  |
+----+----------+----------+
|  1 | Monty    | Widenius |
|  2 | David    | Axmark   |
|  3 | unknown  | N.N.     |
+----+----------+----------+
```


{% @marketo/form formId="4316" %}
