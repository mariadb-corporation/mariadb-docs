---
description: >-
  Explains how to generate RPM packages from the MariaDB source code using CMake
  with the `-DRPM` flag.
---

# Building RPM Packages From Source

To generate RPM packages from the build, supply the `-DRPM=xxx` flag to `CMake`, where the value `xxx` is the name of the distribution you're building for. For example, centos7 or rocky8 or fedora39 or sles15.

What these do are controlled in the following CMake files:

* `cmake/cpack_rpm.cmake`
* `cmake/build_configurations/mysql_release.cmake`
* `cmake/mariadb_connector_c.cmake`

To build the packages you should execute:

```
$ umask 0022
$ cmake --build . --target package
```

## See Also

* [About the MariaDB RPM Files](../binary-packages/rpm/about-the-mariadb-rpm-files.md)
* [Building MariaDB on CentOS](source-building-mariadb-on-centos.md)
* [Installing MariaDB RPM Files](../binary-packages/rpm/)
* [MariaDB RPM Packages](../../../../clients-and-utilities/server-client-software/download/mariadb-rpm-packages.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
