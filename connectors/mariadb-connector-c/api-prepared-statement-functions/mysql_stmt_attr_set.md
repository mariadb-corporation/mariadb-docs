---
description: >-
  mysql_stmt_attr_set configures a prepared statement attribute on a
  Connector/C statement handle; supported attributes include cursor type,
  prefetch rows, and bulk-insert array size.
---

# mysql\_stmt\_attr\_set

## Syntax

```c
my_bool mysql_stmt_attr_set(MYSQL_STMT * stmt,
                            enum enum_stmt_attr_type,
                            const void * attr);
```

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).
* `enum_stmt_attr_type` - the attribute that you want to set. See below.
* `attr` - the value to assign to the attribute

## Description

Used to modify the behavior of a prepared statement. This function may be called multiple times to set several attributes. Returns zero on success, non-zero on failure.

### Attribute types

The `enum_stmt_attr_type` attribute can have one of the following values:

* `STMT_ATTR_UPDATE_MAX_LENGTH` If set to 1, [mysql\_stmt\_store\_result()](mysql_stmt_store_result.md) will update the max\_length value of MYSQL\_FIELD structures.

```c
my_bool update= 1;
rc= mysql_stmt_attr_set(stmt, STMT_ATTR_UPDATE_MAX_LENGTH, &update);
```

* `STMT_ATTR_CURSOR_TYPE`: cursor type when [mysql\_stmt\_execute()](mysql_stmt_execute.md) is invoked. Possible values are CURSOR\_TYPE\_READ\_ONLY or default value CURSOR\_TYPE\_NO\_CURSOR.

```c
unsigned long cursor_type= CURSOR_TYPE_READ_ONLY;
rc= mysql_stmt_attr_set(stmt, STMT_ATTR_CURSOR_TYPE, &cursor_type);
```

* `STMT_ATTR_PREFETCH_ROWS`: number of rows which will be prefetched. The default value is 1.

```c
unsigned long rows=4;
rc= mysql_stmt_attr_set(stmt, STMT_ATTR_PREFETCH_ROWS, &rows);
```

* `STMT_ATTR_PREBIND_PARAMS`: number of parameter markers when using [mariadb\_stmt\_execute\_direct()](mariadb_stmt_execute_direct.md). If the statement handle is reused it will be reset automatically to the state after mysql\_stmt\_init(). This option was added in Connector/C 3.0

```c
unsigned int params= 5;
rc= mysql_stmt_attr_set(stmt, STMT_ATTR_PREBIND_PARAMS, ¶ms);
```

* `STMT_ATTR_ARRAY_SIZE`: number of array elements. This option was added in Connector/C 3.0 and requires [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102) or later

```c
unsigned int array_size= 5;
rc= mysql_stmt_attr_set(stmt, STMT_ATTR_ARRAY_SIZE, &array_size);
```

* `STMT_ATTR_ROW_SIZE`: specifies size of a structure for row wise binding. This length must include space for all of the bound parameters and any padding of the structure or buffer to ensure that when the address of a bound parameter is incremented with the specified length, the result will point to the beginning of the same parameter in the next set of parameters. When using the sizeof operator in ANSI C, this behavior is guaranteed.\
  If the value is zero column-wise binding will be used (default).\
  This option was added in Connector/C 3.0 and requires [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102) or later

```c
size_t row_size= sizeof(struct st_customer);
rc= mysql_stmt_attr_set(stmt, STMT_ATTR_ROW_SIZE, &array_size);
```

{% hint style="info" %}
* If you use the `MYSQL_STMT_ATTR_CURSOR_TYPE` option with `MYSQL_CURSOR_TYPE_READ_ONLY`, a cursor is opened for the statement when you invoke [mysql\_stmt\_execute()](mysql_stmt_execute.md). If there is already an open cursor from a previous [mysql\_stmt\_execute()](mysql_stmt_execute.md) call, it closes the cursor before opening a new one. [mysql\_stmt\_reset()](mysql_stmt_reset.md) also closes any open cursor before preparing the statement for re-execution.
* If you open a cursor for a prepared statement, it is unnecessary to call [mysql\_stmt\_store\_result()](mysql_stmt_store_result.md).
* [mysql\_stmt\_free\_result()](mysql_stmt_free_result.md) closes any open cursor.
{% endhint %}

## See Also

* [mariadb\_stmt\_execute\_direct()](mariadb_stmt_execute_direct.md)
* [mysql\_stmt\_attr\_get()](mysql_stmt_attr_get.md)

{% @marketo/form formId="4316" %}
