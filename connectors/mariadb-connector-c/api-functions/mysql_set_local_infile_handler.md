---
description: >-
  mysql_set_local_infile_handler registers custom callback functions for init,
  read, end, and error phases of a LOAD DATA LOCAL INFILE operation in MariaDB
  Connector/C.
---

# mysql\_set\_local\_infile\_handler

## Name

mysql\_set\_local\_infile\_handler - Registers callback functions for LOAD DATA LOCAL INFILE

## Syntax

```c
#include <mysql.h>

void STDCALL mysql_set_local_infile_handler(MYSQL *conn,
        int (*local_infile_init)(void **, const char *, void *),
        int (*local_infile_read)(void *, char *, uint),
        void (*local_infile_end)(void *),
        int (*local_infile_error)(void *, char *, uint),
        void *userdata);
```

## Description

Registers four callback functions which will be called if a LOAD DATA LOCAL INFILE command will be executed.

The initialization function accepts 3 parameters and returns zero on success, nonzero on error. It allocates an handle, which will be passed to read, end and error functions:

`int init(void **handle, const char *filename, void *userdata)`

The read function is called repeatedly to read data chunks from file into buffer. The amount of bytes is limited by parameer buffer\_len. The function returns the number of bytes which were read from the file:

`int mysql_local_infile_read(void *handle, char * buffer, unsigned int buffer_len)`

The end function will be called after the read function returned zero (no more bytes to read). To prevent leaking of resources, the file must be closed and handle must be freed inside this function:

`void end(void *handle);`

The error function is called to get an error message in case init, read or end functions returned an error.

`error(void *handler, char *error_buf, unsigned int error_buf_len);`

## Parameters

* `mysql` - mysql handle, which was previously allocated by [mysql\_init()](https://github.com/mariadb-corporation/mariadb-connector-c/wiki/mysql_init)
* `local_infile_init` - initialization function, e.g. for opening the file
* `local_infile_read` - read function
* `local_infile_end` - terminating function, e.g. for closing the file
* `local_infile_error` - error function
* `userdata` - a buffer which will be passed to all callback function

## See Also

* [mysql\_set\_local\_infile\_default()](mysql_set_local_infile_default.md)

\\
