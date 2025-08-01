# Building MariaDB MaxScale from Source Code

## Building MariaDB MaxScale from Source Code

## Building MariaDB MaxScale from Source Code

MariaDB MaxScale can be built on any system that meets the requirements. The main\
requirements are as follows:

* CMake version 3.16 or later (Packaging requires CMake 3.25.1 or later)
* GCC version 4.9 or later
* OpenSSL version 1.0.1 or later
* GNUTLS
* Node.js 14 or newer for building MaxCtrl and the GUI (webpack), Node.js 10 or newer for running MaxCtrl
* PAM
* SASL2 (cyrus-sasl)
* SQLite3 version 3.3 or later
* Tcl
* git
* jansson
* libatomic
* libcurl
* libmicrohttpd
* libuuid
* libxml2
* libssh
* pcre2

This is the minimum set of requirements that must be met to build the MaxScale\
core package. Some modules in MaxScale require optional extra dependencies.

* libuuid (binlogrouter)
* boost (binlogrouter)
* Bison 2.7 or later (dbfwfilter)
* Flex 2.5.35 or later (dbfwfilter)
* librdkafka (kafkacdc, kafkaimporter and mirror)
* memcached (storage\_memcached for the cache filter)
* hiredis (storage\_redis for the cache filter)

Some of these dependencies are not available on all operating systems and are\
downloaded automatically during the build step. To skip the building of modules\
that need automatic downloading of the dependencies, use `-DBUNDLE=N` when\
configuring CMake.

### Quickstart

This installs MaxScale as if it was installed from a package. Install `git` before running the following commands.

```
git clone https://github.com/mariadb-corporation/MaxScale
mkdir build
cd build
../MaxScale/BUILD/install_build_deps.sh
cmake ../MaxScale -DCMAKE_INSTALL_PREFIX=/usr
make
sudo make install
sudo ./postinst
```

### Required Packages

For a definitive list of packages, consult the [install\_build\_deps.sh](https://mariadb.com/BUILD/install_build_deps.sh) script.

### Configuring the Build

The tests and other parts of the build can be controlled via CMake arguments.

Here is a small table with the names of the most common parameters and what\
they control. These should all be given as parameters to the -D switch i&#x6E;_&#x4E;AME_=_VALUE_ format (e.g. `-DBUILD_TESTS=Y`).

| Argument Name          | Explanation                                                                                                                                                                |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CMAKE\_INSTALL\_PREFIX | Location where MariaDB MaxScale will be installed to. Set this to /usr if you want MariaDB MaxScale installed into the same place the packages are installed.              |
| BUILD\_TESTS           | Build unit tests                                                                                                                                                           |
| WITH\_SCRIPTS          | Install systemd and init.d scripts                                                                                                                                         |
| PACKAGE                | Enable building of packages                                                                                                                                                |
| TARGET\_COMPONENT      | Which component to install, default is the 'core' package. Other targets are 'experimental', which installs experimental packages and 'all' which installs all components. |
| TARBALL                | Build tar.gz packages, requires PACKAGE=Y                                                                                                                                  |

**Note**: You can look into [defaults.cmake](https://mariadb.com/cmake/defaults.cmake) for a\
list of the CMake variables.

### Running unit tests

To run the MaxScale unit test suite, configure the build with `-DBUILD_TESTS=Y`,\
compile and then run the `make test` command.

## Building MariaDB MaxScale packages

If you wish to build packages, just add `-DPACKAGE=Y` to the CMake invocation\
and build the package with `make package` instead of installing MaxScale with`make install`. This process will create a RPM/DEB package depending on your\
system.

To build a tarball, add `-DTARBALL=Y` to the cmake invokation. This will create\
a _maxscale-x.y.z.tar.gz_ file where _x.y.z_ is the version number.

Some Debian and Ubuntu systems suffer from a bug where `make package` fails\
with errors from dpkg-shlibdeps. This can be fixed by running `make` before`make package` and adding the path to the libmaxscale-common.so library to\
the LD\_LIBRARY\_PATH environment variable.

```
make
LD_LIBRARY_PATH=$PWD/server/core/ make package
```

### Installing optional components

The MaxScale build system is split into multiple components. The main component\
is the `core` MaxScale package which contains MaxScale and all the modules. This\
is the default component that is build, installed and packaged. There is also\
the `experimental` component that contains all experimental modules which are\
not considered as part of the core MaxScale package and are either alpha or beta\
quality modules.

To build the experimental modules along with the MaxScale core components,\
invoke CMake with `-DTARGET_COMPONENT=core,experimental`.

CC BY-SA / Gnu FDL
