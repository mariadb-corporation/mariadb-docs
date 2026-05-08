---
description: >-
  mysql_stmt_attr_get retrieves the current value of a prepared statement
  attribute, such as cursor type, prefetch row count, or max-length update
  behavior.
---

# mysql\_stmt\_attr\_get

## Syntax

```c
my_bool mysql_stmt_attr_get(MYSQL_STMT * stmt,
                            enum enum_stmt_attr_type,
                            void * attr);
```

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).
* `enum_stmt_attr_type` - attribute. See below.
* `attr` - pointer to a variable, which will contain the attribute value.

## Description

Gets the current value of a statement attribute. Returns zero on success, non zero on failure.

### Attribute types

The `enum_stmt_attr_type` parameter has the following possible values:

*   `STMT_ATTR_UPDATE_MAX_LENGTH`: Indicates if [mysql\_stmt\_store\_result()](mysql_stmt_store_result.md) will update the max\_length value of MYSQL\_FIELD structures.

    ```c
    my_bool is_update;
    rc= mysql_stmt_attr_get(stmt, STMT_ATTR_UPDATE_MAX_LENGTH, &is_update);
    ```
*   `STMT_ATTR_CURSOR_TYPE`: Cursor type. Possible values are `CURSOR_TYPE_READ_ONLY` or default value `CURSOR_TYPE_NO_CURSOR`.

    ```c
    unsigned long cursor_type;
    rc= mysql_stmt_attr_get(stmt, STMT_ATTR_CURSOR_TYPE, &cursor_type);
    ```
*   `STMT_ATTR_PREFETCH_ROWS`: Number of rows which will be prefetched. The default value is 1.

    ```c
    unsigned long prefetch_rows;
    rc= mysql_stmt_attr_get(stmt, STMT_ATTR_PREFETCH_ROWS, &prefetch_rows);
    ```
*   `STMT_ATTR_PREBIND_PARAMS`: Number of parameters used for [mariadb\_stmt\_execute\_direct()](mariadb_stmt_execute_direct.md)

    ```c
    unsigned int param_count;
    rc= mysql_stmt_attr_get(stmt, STMT_ATTR_PREBIND_PARAMS, ¶m_count);
    ```

{% hint style="info" %}
Setting the number of prefetched rows will work only for read only cursors.
{% endhint %}

## See Also

* [mysql\_stmt\_attr\_set()](mysql_stmt_attr_set.md)


{% @marketo/form formId="4316" %}
