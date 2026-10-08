# Benchmark Builds

When you build for benchmarks, it's important to use consistent compile time settings across different versions and even products (i.e. when comparing MySQL and MariaDB).

MariaDB and MySQL are built using _CMake_. This makes it hard to fine tune settings because when you chose a predefined build configuration (recommended: _RelWithDebInfo_) then other settings like _CFLAGS_ are overwritten by those from the _CMakefile_.

There are more pain points with cmake:

* cmake uses a different install layout than autotools builds
* the OQGraph engine is included by default, but fails often due to mismatching boost libraries
* make install tries to create directories in system locations (/etc/my.cnf.d etc.) which fails as ordinary user
* CMakefiles for different products sometimes use different CFLAGS

So here is my build script that fixes all those things.

```
#!/bin/bash

INSTDIR=${1:?usage: $0 install-dir}

CFLAGS="-O3 -g -fno-omit-frame-pointer -fno-strict-aliasing -DNDEBUG -DDBUG_OFF"
CXXFLAGS="$CFLAGS -felide-constructors"

CMAKE_LAYOUT_OPTS="-DINSTALL_LAYOUT=RPM -DINSTALL_SCRIPTDIR=bin \
-DINSTALL_MYSQLDATADIR=var -DINSTALL_SBINDIR=libexec \
-DINSTALL_SUPPORTFILESDIR=share -DINSTALL_SYSCONFDIR=etc \
-DINSTALL_SYSCONF2DIR=etc/my.cnf.d -DCMAKE_INSTALL_PREFIX=$INSTDIR \
-DMYSQL_DATADIR=$INSTDIR/var"

CMAKE_FEATURE_OPTS="-DWITH_READLINE=1 -DWITHOUT_OQGRAPH_STORAGE_ENGINE=1"

CMAKE_BUILD_OPTS="-DCMAKE_BUILD_TYPE=RelWithDebInfo"

cmake .. $CMAKE_BUILD_OPTS $CMAKE_LAYOUT_OPTS $CMAKE_FEATURE_OPTS \
-DCMAKE_C_FLAGS_RELWITHDEBINFO="$CFLAGS" \
-DCMAKE_CXX_FLAGS_RELWITHDEBINFO="$CXXFLAGS"

make && make install
```

The script shall be run from a subdir of a source tree. i.e.

```
tar xfz mariadb-10.0.7.tar.gz
cd mariadb-10.0.7
mkdir build
cd build
#... run the build script above
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
