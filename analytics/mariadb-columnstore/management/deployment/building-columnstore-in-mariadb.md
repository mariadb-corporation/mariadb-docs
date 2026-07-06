---
description: >-
  Build MariaDB ColumnStore from source for development and debugging. Check out
  the MariaDB server source with submodules, then build and install ColumnStore
  with the bootstrap_mcs.sh script.
---

# Building ColumnStore from Source

This page describes how to build MariaDB ColumnStore from source, for development and debugging.

{% hint style="info" %}
ColumnStore is not built on its own. It is a storage engine that lives inside the MariaDB server source tree as a git submodule at `storage/columnstore/columnstore`, so you build it as part of MariaDB server.
{% endhint %}

## Supported Distributions

The build script supports the following Linux distributions:

* Ubuntu 20.04, 22.04, and 24.04
* Debian 11 and 12
* Rocky Linux 8 and 9

{% hint style="info" %}
The authoritative, up-to-date list of supported distributions is defined in `build/bootstrap_mcs.sh` (the `DISTRO_OPTIONS` array). Check the script if you are on a newer release.
{% endhint %}

## Get the Source Code

Clone the MariaDB server repository. Use SSH:

```bash
git clone git@github.com:MariaDB/server.git
```

Or HTTPS:

```bash
git clone https://github.com/MariaDB/server.git
```

The server repository contains many git submodules, including ColumnStore. Check them out:

```bash
cd server
git submodule update --init --recursive
```

This also checks out the ColumnStore source at `storage/columnstore/columnstore`.

To build a specific ColumnStore branch, check it out in the submodule:

```bash
cd storage/columnstore/columnstore
git checkout <columnstore-branch>
git config --global --add safe.directory "$(pwd)"
```

{% hint style="info" %}
If you do not have developer access to the ColumnStore repository and want to contribute, fork it and update the submodule's `origin` remote to point at your fork.
{% endhint %}

## Build and Install

The `bootstrap_mcs.sh` script builds and installs ColumnStore into your system. Run it from the ColumnStore submodule directory:

```bash
cd server/storage/columnstore/columnstore
sudo build/bootstrap_mcs.sh --install-deps
```

The `--install-deps` flag installs the build dependencies before compiling.

To select the build type, pass `--build-type` with `Debug` or `RelWithDebInfo`:

```bash
sudo build/bootstrap_mcs.sh --install-deps --build-type Debug
```

## Build Native OS Packages

To build native OS packages (`.rpm` or `.deb`) instead of installing directly, add `--build-packages`:

```bash
cd server/storage/columnstore/columnstore
sudo build/bootstrap_mcs.sh --install-deps --build-packages
```

The resulting packages are written to the build directory.

{% hint style="info" %}
Packages are built for the operating system you are running on. For example, running `--build-packages` on Rocky Linux produces RPMs for Rocky Linux.
{% endhint %}

For the full list of options, run the script with `--help` or read `build/bootstrap_mcs.sh` directly.
