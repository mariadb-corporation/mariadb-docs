---
description: >-
  How to generate a binary tarball from compiled source using `make package`,
  enabling portable distribution.
---

# Creating the MariaDB Binary Tarball

How to generate binary `tar.gz` files.

* [Setup your build environment](https://github.com/mariadb-corporation/docs-server/blob/test/en/Linux_Build_Environment_Setup/README.md).
* [Build binaries](https://kb.askmonty.org/en/generic-build-instructions) with your preferred options/plugins.

If the binaries are already built, you can generate a binary tarball with

```bash
make package
```

Prior to [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5), the following steps were required:

* Use `make_binary_distribution` to generate a binary tar file:

```bash
cd mariadb-source
./scripts/make_binary_distribution
```

This creates a source file with a name like `mariadb-5.3.2-MariaDB-beta-linux-x86_64.tar.gz` in your current directory.

The other option is to use the bakery scripts. In this case you don't have to compile MariaDB source first.

```bash
cd $PACKAGING_WORK
bakery/preheat.sh
cd bakery_{number}
bakery/tarbake51.sh last:1 $MARIA_WORK
bakery/autobake51-bintar.sh mariadb-{version_num}-maria-beta-ourdelta{number}.tar.gz
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
