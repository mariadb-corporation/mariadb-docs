---
description: >-
  Instructions for setting up the build environment on macOS, including
  installing dependencies via Homebrew and configuring CMake.
---

# Build Environment Setup for macOS

## Prelude

Building MariaDB on macOS relies on the Apple-provided toolchain and Homebrew for dependencies.

You can install the toolchain without XCode (suggested, unless you have XCode installed already) with:

```
xcode-select --install
```

Homebrew is a package manager for macOS which you can install from [https://brew.sh](https://brew.sh/)

## Install Dependencies

First, install the upstream dependencies, then clone MariaDB.

```
brew install bison byacc cmake git gnutls libxml2 m4 openssl pcre pcre2 zlib zstd
```

Second, clone MariaDB from the GitHub repository: see the [Getting the MariaDB Source Code](../../../../clients-and-utilities/server-client-software/download/getting-the-mariadb-source-code.md) page for options.

## Set Up the Environment

CMake should find the dependencies automatically, but we may need to set several environment variables to explicitly point at locations of dependencies installed by Homebrew to avoid conflicts with system-native versions that aren't suitable for building MariaDB. In the worst case scenario, use the following (but you can try building MariaDB first by skipping to the "Run CMake" section below to see if these are necessary in your setup):

```
# Homebrew location
export HOMEBREW_BASE_DIR=""
if [ $(uname -m) = "x86_64" ]; then
  export HOMEBREW_BASE_DIR="/usr/local"
else
  export HOMEBREW_BASE_DIR="/opt/homebrew"
fi

# LLVM and Clang
export CXX=$HOMEBREW_BASE_DIR/opt/llvm/bin/clang++
export CC=$HOMEBREW_BASE_DIR/opt/llvm/bin/clang
export PATH="$HOMEBREW_BASE_DIR/opt/llvm/bin:$PATH"
export CPPFLAGS="-I$HOMEBREW_BASE_DIR/opt/llvm/include"
export LDFLAGS="-L$HOMEBREW_BASE_DIR/opt/llvm/lib"
export LDFLAGS="$LDFLAGS -L$HOMEBREW_BASE_DIR/opt/llvm/lib/c++"
export LDFLAGS="$LDFLAGS -Wl,-rpath,$HOMEBREW_BASE_DIR/opt/llvm/lib/c++"
export LDFLAGS="$LDFLAGS -L$HOMEBREW_BASE_DIR/opt/llvm/lib"

# zlib, libxml2
export CPPFLAGS="$CPPFLAGS -I$HOMEBREW_BASE_DIR/opt/libxml2/include -I$HOMEBREW_BASE_DIR/opt/zlib/include"
export CPPFLAGS="$CPPFLAGS -I$HOMEBREW_BASE_DIR/opt/libxml2/include"
export CPPFLAGS="$CPPFLAGS -I$HOMEBREW_BASE_DIR/opt/zlib/include"
export LDFLAGS="$LDFLAGS -L$HOMEBREW_BASE_DIR/opt/libxml2/lib -L$HOMEBREW_BASE_DIR/opt/zlib/lib"
export LDFLAGS="$LDFLAGS -L$HOMEBREW_BASE_DIR/opt/zlib/lib"
export PATH="$HOMEBREW_BASE_DIR/opt/libxml2/bin:$PATH"

# pkgconfig
export PKG_CONFIG_PATH="$HOMEBREW_BASE_DIR/opt/libxml2/lib/pkgconfig:$HOMEBREW_BASE_DIR/opt/zlib/lib/pkgconfig"

# libunwind
export LDFLAGS="$LDFLAGS -L$HOMEBREW_BASE_DIR/opt/llvm/lib/unwind -lunwind"

# bison
export PATH="$HOMEBREW_BASE_DIR/opt/bison/bin:$PATH"
```

The installation location of Homebrew depends on the processor type. Apple Silicon macs will have Homebrew in `/opt/homebrew` while Intel macs will have Homebrew in `/usr/local`.

## Run CMake

By default, macOS uses a case-insensitive filesystem. When building, we can't create a `build` subdirectory because `BUILD` already exists, and all the CMake output will end up mixed in with `BUILD`. Instead, create a `mariadb-build` directory as that is unique. `cd` into `mariadb-build` and, from there, run CMake with the following flags:

```
mkdir mariadb-build
cd mariadb-build
cmake .. \
        -DENABLE_GCOV=OFF \
        -DCMAKE_C_FLAGS=-fno-color-diagnostics \
        -DCMAKE_CXX_FLAGS=-fno-color-diagnostics \
        -DCMAKE_COLOR_MAKEFILE=OFF \
        -DCMAKE_VERBOSE_MAKEFILE=OFF \
        -DCMAKE_BUILD_TYPE=Debug \
        -DCMAKE_EXPORT_COMPILE_COMMANDS=ON \
        -DMYSQL_MAINTAINER_MODE=OFF \
        -DPLUGIN_ARCHIVE=NO \
        -DPLUGIN_MROONGA=NO \
        -DPLUGIN_CONNECT=NO \
        -DPLUGIN_SPIDER=NO \
        -DPLUGIN_ROCKSDB=NO \
        -DPLUGIN_OQGRAPH=NO \
        -DPLUGIN_TOKUDB=NO \
        -DWITH_ASAN=OFF \
        -DWITH_MSAN=OFF \
        -DWITH_SAFEMALLOC=ON \
        -DWITH_MARIABACKUP=OFF \
        -DWITH_EMBEDDED_SERVER=OFF \
        -DWITH_UNIT_TESTS=OFF \
        -DCONC_WITH_UNITTEST=OFF \
        -DWITH_WSREP=OFF \
        -DWITHOUT_DYNAMIC_PLUGINS=0 \
        -DWITH_SSL=bundled \
        -DWITH_PCRE=bundled \
        -G Ninja
```

(You can vary the values of these flags depending on what you need to do.)

{% hint style="info" %}
To install Ninja, run `brew install ninja` in Terminal.
{% endhint %}

If `CMake` runs successfully, you can then run the build itself:

```
cmake --build . --parallel 8
```

This produces a `mariadbd` binary at `mariadb-build/sql`.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
