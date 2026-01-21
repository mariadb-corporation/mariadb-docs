---
description: >-
  Instructions for cross-compiling MariaDB for different architectures,
  including using Buildroot and CMake toolchain files.
---

# Cross-compiling MariaDB

## Buildroot

[Buildroot](https://buildroot.org/downloads/manual/manual.html#_user_guide) is a way to cross compile MariaDB and other packages into a root filesystem. In the menuconfig you need to enable "Enable C++ Support" first under "Toolchain". After C++ is enabled MariaDB is an option under "Target Packages" ->"Libraries" -> "Databases" -> "mysql support" -> "mysql variant" -> "mariadb". Also enable the "mariadb server" below the "mysql support" option.

## Details

To cross-compile with `cmake` you will need a `toolchain` file. See, for example, [here](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html?highlight=linker#cross-compiling-for-linux). Besides `cmake` specific variables it should have, at least

```bash
SET(STACK_DIRECTION -1)
  SET(HAVE_IB_GCC_ATOMIC_BUILTINS 1)
```

with appropriate values for your target architecture. Normally these MariaDB configuration settings are detected by running a small test program, and it cannot be done when cross-compiling.

Note that during the build few helper tools are compiled and then immediately used to generate more source files for this very build. When cross-compiling these tools naturally should be built for the host architecture, not for the target architecture. Do it like this (assuming you're in the mariadb source tree):

```bash
$ mkdir host
$ cd host
$ cmake ..
$ make import_executables
$ cd ..
```

Now the helpers are built and you can cross-compile:

```bash
$ mkdir target
$ cd target
$ cmake .. -DCMAKE_TOOLCHAIN_FILE=/path/to/toolchain/file.cmake -DIMPORT_EXECUTABLES=../host/import_executables.cmake
$ make
```

Here you invoke `cmake`, specifying the path to your toolchain file and the path to the `import_executables.cmake` that you have just built on the previous step. Of course, you can also specify any other cmake parameters that could be necessary for this build, for example, enable or disable specific storage engines.

See also [msg02911.html](https://lists.launchpad.net/maria-discuss/msg02911.html)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
