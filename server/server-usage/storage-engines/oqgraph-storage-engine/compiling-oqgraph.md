---
description: >-
  Learn about the dependencies and build steps required to compile the OQGRAPH
  storage engine from source.
---

# Compiling OQGRAPH

To compile OQGraph v2 you need to have the boost library with the versions not earlier than 1.40 and not later than 1.55 and gcc version not earlier than 4.5.

#### Note

OQGraph v3 compiles fine with the newer boost libraries, but it additionally needs the Judy library installed.

When all build prerequisites are met, OQGraph is enabled and compiled automatically. To enable or disable OQGRAPH explicitly, see the generic [plugin build instructions](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/compiling-mariadb-from-source/compiling-mariadb-with-extra-modulesoptions/specifying-which-plugins-to-build.md).

### Finding Out Why OQGRAPH Didn't Compile

If OQGRAPH gets compiled properly, there should be a file like:

```bash
storage/oqgraph/ha_oqgraph.so
```

If this is not the case, then you can find out if there is any modules missing that are required by OQGRAPH by doing:

```bash
cmake . -LAH | grep -i oqgraph
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
