# User-Defined Functions Calling Sequences

The functions described in [Creating User-defined Functions](creating-user-defined-functions.md) are expanded on this page. They are declared as follows:

## Simple Functions

### x()

If x() returns an integer, it is declared as follows:

```
long long x(UDF_INIT *initid, UDF_ARGS *args,
              char *is_null, char *error);
```

If x() returns a string (DECIMAL functions also return string values), it is declared as follows:

```
char *x(UDF_INIT *initid, UDF_ARGS *args,
          char *result, unsigned long *length,
          char *is_null, char *error);
```

If x() returns a real, it is declared as follows:

```
double x(UDF_INIT *initid, UDF_ARGS *args,
              char *is_null, char *error);
```

### x\_init()

```
my_bool x_init(UDF_INIT *initid, UDF_ARGS *args, char *message);
```

### x\_deinit()

```
void x_deinit(UDF_INIT *initid);
```

### Description

_initid_ is a parameter passed to all three functions that points to a _UDF\_INIT_ structure, used for communicating information between the functions. Its structure members are:

* my\_bool maybe\_null
  * maybe\_null should be set to 1 if x\_init can return a NULL value, Defaults to 1 if any arguments are declared maybe\_null.
* unsigned int decimals
  * Number of decimals after the decimal point. The default, if an explicit number of decimals is passed in the arguments to the main function, is the maximum number of decimals, so if 9.5, 9.55 and 9.555 are passed to the function, the default would be three (based on 9.555, the maximum). If there are no explicit number of decimals, the default is set to 31, or one more than the maximum for the DOUBLE, FLOAT and DECIMAL types. This default can be changed in the function to suit the actual calculation.
* unsigned int max\_length
  * Maximum length of the result. For integers, the default is 21. For strings, the length of the longest argument. For reals, the default is 13 plus the number of decimals indicated by initid->decimals. The length includes any signs or decimal points. Can also be set to 65KB or 16MB in order to return a BLOB. The memory remains unallocated, but this is used to decide on the data type to use if the data needs to be temporarily stored.
* char \*ptr
  * A pointer for use as required by the function. Commonly, initid->ptr is used to communicate allocated memory, with x\_init() allocating the memory and assigning it to this pointer, x() using it, and x\_deinit() de-allocating it.
* my\_bool const\_item
  * Should be set to 1 in x\_init() if x() always returns the same value, otherwise 0.

## Aggregate Functions

### x\_clear()

_x\_clear()_ is a required function for aggregate functions, and is declared as follows:

```
void x_clear(UDF_INIT *initid, char *is_null, char *error);
```

It is called when the summary results need to be reset, that is at the beginning of each new group. but also to reset the values when there were no matching rows.

_is\_null_ is set to point to CHAR(0) before calling x\_clear().

In the case of an error, you can store the value to which the error argument points (a single-byte variable, not a string buffer) in the variable.

### x\_reset()

_x\_reset()_ is declared as follows:

```
void x_reset(UDF_INIT *initid, UDF_ARGS *args,
               char *is_null, char *error);
```

It is called on finding the first row in a new group. Should reset the summary variables, and then use _UDF\_ARGS_ as the first value in the group's internal summary value. The function is not required if the UDF interface uses _x\_clear()_.

### x\_add()

_x\_add()_ is declared as follows:

```
void x_add(UDF_INIT *initid, UDF_ARGS *args,
             char *is_null, char *error);
```

It is called for all rows belonging to the same group, and should be used to add the value in _UDF\_ARGS_ to the internal summary variable.

### x\_remove()

_x\_remove()_ was added in [MariaDB 10.4](../../security/user-account-management/authentication-from-mariadb-10-4.md) and is declared as follows (same as _x\_add()_):

```
void x_remove(UDF_INIT* initid, UDF_ARGS* args,
               char* is_null, char *error );
```

It adds more efficient support of aggregate UDFs as [window functions](../../reference/sql-functions/special-functions/window-functions/). _x\_remove()_ should "subtract" the row (reverse _x\_add()_). In [MariaDB 10.4](../../security/user-account-management/authentication-from-mariadb-10-4.md) aggregate UDFs will work as WINDOW functions without _x\_remove()_ but it will not be so efficient.

If _x\_remove()_ supported (defined) detected automatically.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
