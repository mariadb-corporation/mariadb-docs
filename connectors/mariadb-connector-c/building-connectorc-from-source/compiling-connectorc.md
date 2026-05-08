---
description: >-
  Compile MariaDB Connector/C after configuration using CMake on Windows or
  Unix. Supports Visual Studio builds and GNU make, with both IDE and
  command-line build options.
---

# Compiling Connector/C

After successful configuration, Connector/C can now be compiled.

### Compiling on Windows

If no CMake generator was specified, CMake creates by default build files for Visual Studio.\
You can now either build Connector/C inside Visual Studio

```bash
devenv mariadb_connector_c.sln
```

or via command line

```bash
cmake --build . --config RelWithDebInfo
```

### Compiling on Unix

By default CMake creates build files for GNU make. On some system GNU make is renamed to gmake.\
You can now build Connector/C with

```bash
make
```

or

```bash
cmake --build . --config Release
```


{% @marketo/form formId="4316" %}
