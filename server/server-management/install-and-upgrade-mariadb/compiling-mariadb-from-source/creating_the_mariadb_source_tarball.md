---
description: >-
  Explains how to generate a source tarball from the MariaDB build environment
  using `automake` and `make dist`.
---

# Creating the MariaDB Source Tarball

How to create a source tar.gz file.

First [Setup your build environment](build-environment-setup-for-linux.md).

Then use automake/configure/make to generate the tar file:

```bash
BUILD/autorun.sh
./configure --with-plugin-xtradb
make dist
```

This creates a source file with a name like `mysql-5.3.2-MariaDB-beta.tar.gz`

See also [the generic build instructions](generic-build-instructions.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
