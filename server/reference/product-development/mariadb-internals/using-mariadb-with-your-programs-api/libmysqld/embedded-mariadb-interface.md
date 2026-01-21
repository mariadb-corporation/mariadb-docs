---
description: >-
  Detailed guide on the C API functions and requirements for initializing,
  using, and terminating the embedded MariaDB server library.
---

# Embedded MariaDB Interface

{% include "../../../../../.gitbook/includes/this-page-contains-backgrou....md" %}

The embedded MariaDB server, `libmysqld` has the identical interface as the [C client library](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c)`libmysqclient`.

The normal usage of the embedded server is to use the normal `mysql.h` include file in your application and link with `libmysqld` instead of `libmysqlclient`.

The intention is that one should be able to move from a server/client version of MariaDB to a single server version of MariaDB by just changing which library you link with.

This means that the embedded C client API only changes when the normal C API changes, usually only between major releases.

The only major change required in your application if you are going to use the embedded server is that you have to call the following functions from your application:

```c
int mysql_library_init(int argc, char **argv, char **groups)
void mysql_library_end(void);
```

This is also safe to do when using the standard C library.

## Notes

* libmysqld.so has many more exported symbols than the C library to allow one to expose and use more parts of MariaDB. In normal applications one should not use them, as they may change between every release.
* The embedded server library and related test binaries are no longer part of binary tarball release archives.

## See Also

* [mysql\_library\_init](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_library_init)
* [mariadb client with MariaDB embedded](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/clients-and-utilities/mariadb-embedded.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
