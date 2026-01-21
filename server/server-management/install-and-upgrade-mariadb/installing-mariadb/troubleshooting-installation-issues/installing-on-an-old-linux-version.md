---
description: >-
  Guidance for dealing with glibc or shared library errors when attempting to
  install modern MariaDB binaries on older Linux distributions.
---

# Installing on an Old Linux Version

This article lists some typical errors that may happen when you try to use an incompatible MariaDB binary on a linux system:

The following example errors are from trying to install MariaDB built for SuSE 11.x on a SuSE 9.0 server:

```
> scripts/mysql_install_db
./bin/my_print_defaults: /lib/i686/libc.so.6: 
  version `GLIBC_2.4' not found (required by ./bin/my_print_defaults)
```

and

```
> ./bin/mysqld --skip-grant &
./bin/mysqld: error while loading shared libraries: libwrap.so.0:
cannot open shared object file: No such file or directory
```

If you see either of the above errors, the binary MariaDB package you installed is not compatible with your system.

The options you have are:

* Find another MariaDB package or tar from the [download page](https://downloads.mariadb.org/) that matches your system.
* Alternatively, [download the source](../../../../clients-and-utilities/server-client-software/download/getting-the-mariadb-source-code.md) and [build it](../compiling-mariadb-from-source/generic-build-instructions.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
