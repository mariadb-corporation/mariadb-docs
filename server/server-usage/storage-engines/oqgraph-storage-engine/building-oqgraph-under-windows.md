---
description: >-
  Specific instructions and prerequisites for building the OQGRAPH storage
  engine on Windows systems using Visual Studio.
---

# Building OQGRAPH Under Windows

OQGRAPH v3 can be built on Windows. This has been tested using Windows 7, Microsoft Visual Studio Express 2010 (32-bit), Microsoft Windows 64-bit Platform SDK 7.1 (64-bit), the Boost library >= 1.55 and Judy 1.0.5.

#### Note

Other recent versions of Boost, Judy or MSVC may work but these combinations have not been tested.

* Download the source package for Boost 1.55 from the Boost project website, [www.boost.org](https://www.boost.org)
* Download the source package for Judy 1.05 via
* Follow the documented instructions for building under Windows from the command line: [Building\_MariaDB\_on\_Windows](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/compiling-mariadb-from-source/building_mariadb_on_windows.md)
  * Ensure that the following variable is set to CMAKE: `JUDY_ROOT=path\to\judy\unzipped`
  * See also comments in `storage/oqgraph/cmake/FindJudy.cmake`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
