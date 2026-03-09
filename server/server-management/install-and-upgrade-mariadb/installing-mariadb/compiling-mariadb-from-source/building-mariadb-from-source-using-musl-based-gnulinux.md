---
description: >-
  Guide for compiling MariaDB on Alpine Linux or other musl-based systems,
  noting limitations like TokuDB support.
---

# Building MariaDB From Source Using musl-based GNU/Linux

## Instructions on compiling MariaDB on musl-based operating systems (Alpine)

The instructions on this page will help you compile [MariaDB](../../../../clients-and-utilities/mariadb-client/) from source.\
Links to more complete instructions for specific platforms can be found on the [source](./) page.

* First, [get a copy of the MariaDB source](../../../../clients-and-utilities/server-client-software/download/getting-the-mariadb-source-code.md).
* Next, [prepare your system to be able to compile the source](build-environment-setup-for-linux.md).

## Using `cmake`

[MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1) and above is compiled using _`cmake`_. You can configure your\
build simply by running _`cmake`_ using special option, i.e.

```bash
cmake . -DWITHOUT_TOKUDB=1
```

To build and install MariaDB after running _`cmake`_ use

```bash
make
sudo make install
```

Note that building with MariaDB this way will disable `tokuDB`, till `tokuDB` becomes fully supported on `musl`.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
