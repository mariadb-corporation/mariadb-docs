# mariadb\_field\_attr

## Syntax

```bnf
#include <mysql.h>

int *mariadb_field_attr(MARIADB_CONST_STRING *attr,
                        const MYSQL_FIELD *field,
                        enum mariadb_field_attr_t type)
```

## Parameter

* `attr`: A pointer which returns extended metadata information
* `field`: Specifies the field which contains extended metadata information
* `type:` Specifies type of metadata information. Supported types are `MARIADB_FIELD_METADATA_DATA_TYPE_NAME` and `MARIADB_FIELD_METADATA_FORMAT_NAME`.

## Description

Returns extended metadata information for pluggable field types like JSON and GEOMETRY.

## Return Value

Returns zero on success or non zero if the field doesn't provide extended metadata information.

### Notes

* Pluggable field type support is available in MariaDB server version 10.5.2 and later.
* To check if the server supports pluggable field types, check the extended server capabilities which can be obtained by api function [mariadb\_get\_info()](mariadb_get_info.md).

## Example

```sql
#include <mysql.h>

int display_extended_field_attribute(MYSQL *mysql)
{
  MYSQL_RES *result;
  MYSQL_FIELD *fields;

  if (mysql_query(mysql, "CREATE TEMPORARY TABLE t1 (a POINT)"))
    return 1;

  if (mysql_query(mysql, "SELECT a FROM t1"))
    return 1;

  if (!(result= mysql_store_result(mysql)))
    return 1;

  if ((fields= mysql_fetch_fields(result)))
  {
    MARIADB_CONST_STRING field_attr;

    if (!mariadb_field_attr(&field_attr, &fields[0],
                            MARIADB_FIELD_ATTR_DATA_TYPE_NAME))
    {
      printf("Extended field attribute: %s\n", field_attr.str);
    }
  }
  mysql_free_result(result);
  return 0;
}
```

## History

`mariadb_field_attr` was added in MariaDB Connector/C 3.1.8.

## See Also

* [mysql\_store\_result()](mysql_store_result.md)
* [mysql\_use\_result()](mysql_use_result.md)
* [mariadb\_get\_info()](mariadb_get_infov.md)
* [mysql\_fetch\_fields()](mysql_fetch_fields.md)
