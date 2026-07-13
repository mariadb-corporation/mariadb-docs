---
description: Application Development with MariaDB Connector/C
---

# Development

MariaDB Connector/C enables C and C++ applications to establish client connections to MariaDB database products over TLS.

## Build Your Application with Connector/C

When you build a C application, your compiler must link your application with the MariaDB Connector/C shared library.

The following `gcc` ([GNU GCC](https://gcc.gnu.org/)) command demonstrates how to link an application with the MariaDB Connector/C shared library using the `mariadb_config` utility to determine the compiler arguments:

```bash
gcc -o example example.c $(mariadb_config --include --libs)
```

If you are not using the `gcc` compiler, please consult your compiler's manual.

### Header Files

MariaDB Connector/C includes several header files. In some cases, developers might find it useful to inspect the MariaDB Connector/C header files to view the definitions of structures, functions, and constants.

The header files:

* Contain the definitions of structures, functions, and constants.
* Are installed to the `/usr/include/mariadb/` directory by default on Linux for tarball and DEB packages. RPM packages install headers directly to `/usr/include/` instead.

C applications developed using MariaDB Connector/C must include the `mysql.h` header file.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
