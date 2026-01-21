---
description: >-
  Explains the limitations in providing Source RPMs (SRPMs) for certain
  platforms due to CMake version requirements and build system dependencies.
---

# Why Source RPMs (SRPMs) Aren't Packaged For Some Platforms

MariaDB source RPMs (SRPMs) are not packaged on all platforms for which MariaDB RPMs are packaged.

The reason is that MariaDB's build process relies heavily on [cmake](https://cmake.org) for a lot of things. In this specific case, MariaDB's build process relies on [CMake CPack Package Generators](https://gitlab.kitware.com/cmake/community/wikis/doc/cpack/PackageGenerators) to build RPMs. The specific package generator that it uses to build RPMs is called [CPackRPM](https://cmake.org/cmake/help/v3.10/module/CPackRPM.html).

Support for source RPMs in [CPackRPM](https://cmake.org/cmake/help/v3.10/module/CPackRPM.html) became usable with MariaDB's build system starting from around [cmake 3.10](https://cmake.org/cmake/help/v3.10/release/3.10.html). This means that we do not produce source RPMs on platforms where the installed [cmake](https://cmake.org) version is older than that.

See also [Building MariaDB from a Source RPM](../../compiling-mariadb-from-source/building-mariadb-from-a-source-rpm.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
