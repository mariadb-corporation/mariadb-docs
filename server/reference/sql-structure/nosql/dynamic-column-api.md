---
description: >-
  The client-side API for reading and writing dynamic-column blobs, as an
  alternative to the in-server dynamic-column functions.
---

# Dynamic Column API

This page describes the client-side API for reading and writing [Dynamic Columns](dynamic-columns.md) blobs.

Normally, you should use [Dynamic column functions](dynamic-columns.md#dynamic-columns-functions) which are run inside the MariaDB server and allow one to access Dynamic Columns content without any client-side libraries.

If you need to read/write dynamic column blobs **on the client** for some reason, this API enables that.

## Where to get it

The API is a part of `libmysql` C client library. In order to use it, you need to include this header file and link against `libmysql`:

```c
#include <mysql/ma_dyncol.h>
```

## Data structures

### DYNAMIC\_COLUMN

`DYNAMIC_COLUMN` represents a packed dynamic column blob. It is essentially a string-with-length and is defined as follows:

```c
/* A generic-purpose arbitrary-length string defined in MySQL Client API */
typedef struct st_dynamic_string
{
  char *str;
  size_t length,max_length,alloc_increment;
} DYNAMIC_STRING;

...

typedef DYNAMIC_STRING DYNAMIC_COLUMN;
```

### DYNAMIC\_COLUMN\_VALUE

Dynamic columns blobs store {name, value} pairs. The `DYNAMIC_COLUMN_VALUE` structure is used to represent the value in accessible form.

```c
struct st_dynamic_column_value
{
  DYNAMIC_COLUMN_TYPE type;
  union
  {
    long long long_value;
    unsigned long long ulong_value;
    double double_value;
    struct {
      MYSQL_LEX_STRING value;
      CHARSET_INFO *charset;
    } string;
    struct {
      decimal_digit_t buffer[DECIMAL_BUFF_LENGTH];
      decimal_t value;
    } decimal;
    MYSQL_TIME time_value;
  } x;
};
typedef struct st_dynamic_column_value DYNAMIC_COLUMN_VALUE;
```

Every value has a type, which is determined by the `type` member.

| Type               | Structure field                              |
| ------------------ | -------------------------------------------- |
| DYN\_COL\_NULL     | -                                            |
| DYN\_COL\_INT      | value.x.long\_value                          |
| DYN\_COL\_UINT     | value.x.ulong\_value                         |
| DYN\_COL\_DOUBLE   | value.x.double\_value                        |
| DYN\_COL\_STRING   | value.x.string.value, value.x.string.charset |
| DYN\_COL\_DECIMAL  | value.x.decimal.value                        |
| DYN\_COL\_DATETIME | value.x.time\_value                          |
| DYN\_COL\_DATE     | value.x.time\_value                          |
| DYN\_COL\_TIME     | value.x.time\_value                          |
| DYN\_COL\_DYNCOL   | value.x.string.value                         |

#### Notes

* Values with type `DYN_COL_NULL` do not ever occur in dynamic columns blobs.
* Type `DYN_COL_DYNCOL` means that the value is a packed dynamic blob. This is how nested dynamic columns are done.
* Before storing a value to `value.x.decimal.value`, you must call `mariadb_dyncol_prepare_decimal()` to initialize the space for storage.

### enum\_dyncol\_func\_result

`enum enum_dyncol_func_result` is used as return value.

| Value | Name                         | Comments                                                             |
| ----- | ---------------------------- | -------------------------------------------------------------------- |
| 0     | ER\_DYNCOL\_OK               | OK                                                                   |
| 0     | ER\_DYNCOL\_NO               | (the same as ER\_DYNCOL\_OK but for functions which return a YES/NO) |
| 1     | ER\_DYNCOL\_YES              | `YES` response or success                                            |
| 2     | ER\_DYNCOL\_TRUNCATED        | Operation succeeded but the data was truncated                       |
| -1    | ER\_DYNCOL\_FORMAT           | Wrong format of the encoded string                                   |
| -2    | ER\_DYNCOL\_LIMIT            | A limit of implementation reached                                    |
| -3    | ER\_DYNCOL\_RESOURCE         | Out of resources                                                     |
| -4    | ER\_DYNCOL\_DATA             | Incorrect input data                                                 |
| -5    | ER\_DYNCOL\_UNKNOWN\_CHARSET | Unknown character set                                                |

Result codes that are less than zero represent error conditions.

## Function reference

Functions come in pairs:

* `xxx_num()` operates on the old (pre-MariaDB-10.0.1) dynamic column blob format, where columns were identified by numbers.
* `xxx_named()` can operate on both old or new data format. If it modifies the blob, it converts it to the new data format.

You should use `xxx_named()` functions, unless you need to keep the data compatible with MariaDB versions before 10.0.1.

### mariadb\_dyncol\_init <a href="#mariadb_dyncol_init" id="mariadb_dyncol_init"></a>

First, define mariadb\_dyncol\_init(A) memset((A), 0, sizeof(\*(A))). It is the correct initialization for an empty packed dynamic blob.

### mariadb\_dyncol\_free <a href="#mariadb_dyncol_free" id="mariadb_dyncol_free"></a>

Copy where str is IN. Packed dynamic blob which memory should be freed.

```c
void mariadb_dyncol_free(DYNAMIC_COLUMN *str);
```

### mariadb\_dyncol\_create\_many

Create a packed dynamic blob from arrays of values and names.

```c
enum enum_dyncol_func_result
mariadb_dyncol_create_many(DYNAMIC_COLUMN *str,
                           uint column_count,
                           uint *column_numbers,
                           DYNAMIC_COLUMN_VALUE *values,
                           my_bool new_string);
enum enum_dyncol_func_result
mariadb_dyncol_create_many_named(DYNAMIC_COLUMN *str,
                                 uint column_count,
                                 MYSQL_LEX_STRING *column_keys,
                                 DYNAMIC_COLUMN_VALUE *values,
                                 my_bool new_string);
```

Here are the names and values:

| Name            | Value | Comments                                                            |
| --------------- | ----- | ------------------------------------------------------------------- |
| str             | OUT   | Packed dynamic blob will be put here                                |
| column\_count   | IN    | Number of columns                                                   |
| column\_numbers | IN    | Column numbers array (old format)                                   |
| column\_keys    | IN    | Column names array (new format)                                     |
| values          | IN    | Column values array                                                 |
| new\_string     | IN    | If TRUE then the str will be reinitialized (not freed) before usage |

### mariadb\_dyncol\_update\_many

Add or update columns in a dynamic columns blob. To delete a column, update its value to a "non-value" of type `DYN_COL_NULL` :

```c
enum enum_dyncol_func_result
mariadb_dyncol_update_many(DYNAMIC_COLUMN *str,
                           uint column_count,
                           uint *column_numbers,
                           DYNAMIC_COLUMN_VALUE *values);
enum enum_dyncol_func_result
mariadb_dyncol_update_many_named(DYNAMIC_COLUMN *str,
                                 uint column_count,
                                 MYSQL_LEX_STRING *column_keys,
                                 DYNAMIC_COLUMN_VALUE *values);
```

| Name            | Value  | Comments                              |
| --------------- | ------ | ------------------------------------- |
| str             | IN/OUT | Dynamic columns blob to be modified   |
| column\_count   | IN     | Number of columns in following arrays |
| column\_numbers | IN     | Column numbers array (old format)     |
| column\_keys    | IN     | Column names array (new format)       |
| values          | IN     | Column values array                   |

### mariadb\_dyncol\_exists

Check if column with given names exist in the blob:

```c
enum enum_dyncol_func_result
mariadb_dyncol_exists(DYNAMIC_COLUMN *str, uint column_number);
enum enum_dyncol_func_result
mariadb_dyncol_exists_named(DYNAMIC_COLUMN *str, MYSQL_LEX_STRING *column_key);
```

| Name           | Value | Comments                      |
| -------------- | ----- | ----------------------------- |
| str            | IN    | Packed dynamic columns string |
| column\_number | IN    | Column number (old format)    |
| column\_key    | IN    | Column name (new format)      |

The function returns `YES`, or `NO` or Error code.

### mariadb\_dyncol\_column\_count

Get the number of columns in a dynamic column blob:

```c
enum enum_dyncol_func_result
mariadb_dyncol_column_count(DYNAMIC_COLUMN *str, uint *column_count);
```

| Name          | Value | Comments                                                 |
| ------------- | ----- | -------------------------------------------------------- |
| str           | IN    | Packed dynamic columns string                            |
| column\_count | OUT   | Number of not NULL columns in the dynamic columns string |

### mariadb\_dyncol\_list

List columns in a dynamic column blob:

```c
enum enum_dyncol_func_result
mariadb_dyncol_list(DYNAMIC_COLUMN *str, uint *column_count, uint **column_numbers);
enum enum_dyncol_func_result
mariadb_dyncol_list_named(DYNAMIC_COLUMN *str, uint *column_count,
                          MYSQL_LEX_STRING **column_keys);
```

|                 |     |                                                                  |
| --------------- | --- | ---------------------------------------------------------------- |
| str             | IN  | Packed dynamic columns string                                    |
| column\_count   | OUT | Number of columns in following arrays                            |
| column\_numbers | OUT | Column numbers array (old format). Caller should free this array |
| column\_keys    | OUT | Column names array (new format). Caller should free this array   |

### mariadb\_dyncol\_get

Get a value of one column:

```c
enum enum_dyncol_func_result
mariadb_dyncol_get(DYNAMIC_COLUMN *org, uint column_number,
                   DYNAMIC_COLUMN_VALUE *value);
enum enum_dyncol_func_result
mariadb_dyncol_get_named(DYNAMIC_COLUMN *str, MYSQL_LEX_STRING *column_key,
                         DYNAMIC_COLUMN_VALUE *value);
```

| Name           | Value | Comments                          |
| -------------- | ----- | --------------------------------- |
| str            | IN    | Packed dynamic columns string     |
| column\_number | IN    | Column numbers array (old format) |
| column\_key    | IN    | Column names array (new format)   |
| value          | OUT   | Value of the column               |

If the column is not found, `NULL` is returned as the value of the column.

### mariadb\_dyncol\_unpack

Get the value of all columns:

```c
enum enum_dyncol_func_result
mariadb_dyncol_unpack(DYNAMIC_COLUMN *str,
                      uint *column_count,
                      MYSQL_LEX_STRING **column_keys,
                      DYNAMIC_COLUMN_VALUE **values);
```

| Name          | Value | Comments                                               |
| ------------- | ----- | ------------------------------------------------------ |
| str           | IN    | Packed dynamic columns string to unpack                |
| column\_count | OUT   | Number of columns in following arrays                  |
| column\_keys  | OUT   | Column names array (should be free by caller)          |
| values        | OUT   | Values of the columns array (should be free by caller) |

### mariadb\_dyncol\_has\_names

Check whether the dynamic columns blob uses the new data format (the one where columns are identified by names):

```c
my_bool mariadb_dyncol_has_names(DYNAMIC_COLUMN *str);
```

| Name | Value | Comments                      |
| ---- | ----- | ----------------------------- |
| str  | IN    | Packed dynamic columns string |

### mariadb\_dyncol\_check

Check whether the dynamic column blob has the correct data format:

```c
enum enum_dyncol_func_result
mariadb_dyncol_check(DYNAMIC_COLUMN *str);
```

| Name | Value | Comments                      |
| ---- | ----- | ----------------------------- |
| str  | IN    | Packed dynamic columns string |

### mariadb\_dyncol\_json

Get contents of a dynamic columns blob in a JSON form:

```c
enum enum_dyncol_func_result
mariadb_dyncol_json(DYNAMIC_COLUMN *str, DYNAMIC_STRING *json);
```

| Name | Value | Comments                      |
| ---- | ----- | ----------------------------- |
| str  | IN    | Packed dynamic columns string |
| json | OUT   | JSON representation           |

### mariadb\_dyncol\_val\_TYPE

Get the dynamic column value as one of the base types:

```c
enum enum_dyncol_func_result
mariadb_dyncol_val_str(DYNAMIC_STRING *str, DYNAMIC_COLUMN_VALUE *val,
                       CHARSET_INFO *cs, my_bool quote);
enum enum_dyncol_func_result
mariadb_dyncol_val_long(longlong *ll, DYNAMIC_COLUMN_VALUE *val);
enum enum_dyncol_func_result
mariadb_dyncol_val_double(double *dbl, DYNAMIC_COLUMN_VALUE *val);
```

| Name             | Value | Comments            |
| ---------------- | ----- | ------------------- |
| str or ll or dbl | OUT   | value of the column |
| val              | IN    | Value               |

### mariadb\_dyncol\_prepare\_decimal

Initialize `DYNAMIC_COLUMN_VALUE` before setting the value of `value.x.decimal.value`:

```c
void mariadb_dyncol_prepare_decimal(DYNAMIC_COLUMN_VALUE *value);
```

| Name  | Value | Comments            |
| ----- | ----- | ------------------- |
| value | OUT   | Value of the column |

This function links `value.x.decimal.value` to `value.x.decimal.buffer`.

### mariadb\_dyncol\_value\_init

Initialize a `DYNAMIC_COLUMN_VALUE` structure to a safe default:

```c
#define mariadb_dyncol_value_init(V) (V)->type= DYN_COL_NULL
```

### mariadb\_dyncol\_column\_cmp\_named

Compare two column names (column names are compared with memcmp()):

```c
int mariadb_dyncol_column_cmp_named(const MYSQL_LEX_STRING *s1,
                                    const MYSQL_LEX_STRING *s2);
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
