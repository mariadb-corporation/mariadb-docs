# Compile and Using MariaDB with Sanitizers (ASAN, UBSAN, TSAN, MSAN)

## What are Sanitizers?

Sanitizers are open source runtime error detectors developed by Google that are enabled during the compile step. These sanitizers add extra code during compilation that will throw exceptions when certain errors are detected.

Sanitizers find server bugs bug instrumenting the runtime MariaDB during compile time, and performing runtime checks on the executed test. Sanitizers detect a variety of implementation defects:

The sanitizers for clang are:

* [AddressSanitizer (aka ASAN)](https://clang.llvm.org/docs/AddressSanitizer.html)
* [UndefinedBehaviourSanitizer (aka UBSAN)](https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html)
* [ThreadSanitizer (aka TSAN)](https://clang.llvm.org/docs/ThreadSanitizer.html)
* [MemorySanitizer (aka MSAN)](https://clang.llvm.org/docs/MemorySanitizer.html)

## How to Compile MariaDB with Sanitizers

Before using ASAN locally, please ensure that it is installed on the system:

You can use one of the two following build commands:

```
cmake  -DWITH_ASAN=ON /source
```

Additionally, UBSAN, TSAN, and MSAN can be enabled in a similar way:

UBSAN:

```
cmake -DWITH_UBSAN=ON /source
```

TSAN:

```
cmake -DWITH_TSAN=ON /source
```

MSAN:

```
cmake -DWITH_MSAN=ON /source
```

Important to note MSAN requires instrumented c++ and system libraries to have a functioning build per container guide below.

## Buildbot's MSAN container

The time consuming aspect of building with MSAN is having [instrumented system libraries](https://github.com/MariaDB/buildbot/blob/main/ci_build_images/msan.instrumentedlibs.sh). To help with this MariaDB Foundation has built the MSAN container for buildbot, but this is reusable locally.

The MariaDB Buildbot MSAN container, `quay.io/mariadb-foundation/bb-worker/debian12-msan-clang-20` a container with:

* the instrumented libraries required for MSAN
* a very modern clang version
* the latest stable Debian as a base image
* a compiled [rr](https://rr-project.org/) for debugging

The build of this container isn't hard coded to MSAN so it can be used for:

* A general Debian build container
* Using the gcc/g++ of Debian (by removing the CC and CXX environment variables
* Compiling with a latest clang
* Compiling with the ASAN/UBSAN feature available in the latest clang

### Running the MSAN container

First, run the container where your current directory is the source directory:

```
podman run -v $PWD:/source:z \
  --rm \
  -ti \
  --entrypoint bash \
  --mount=type=tmpfs,tmpfs-size=10G,dst=/build \
  --workdir /build \
   quay.io/mariadb-foundation/bb-worker:debian12-msan-clang-20
```

The `/build` options for docker are slighly different as they default to `noexec` and a `root` ownership by default.

```
docker run -v $PWD:/source:z \
  --rm \
  -ti \
  --entrypoint bash \
  --tmpfs /build:size=10G,exec,uid=1000 \
  --workdir /build \
  quay.io/mariadb-foundation/bb-worker:debian12-msan-clang-20
```

The purposes of these, and other options include:

| Command Component                            | Purpose                                                                           | Notes                                                                                   |
| -------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Command Component                            | Purpose                                                                           | Notes                                                                                   |
| podman run / docker run                      | run a container                                                                   | other implementations use docker syntax (or at least close)                          |
| --rm                                         | remove container on termination                                                   |                                                                                         |
| -ti                                          | a tty and a stdin are connected                                                   | for interactive container use                                                           |
| -v "$PWD":/source:z                          | mount current directory as /source inside the container - :z - read selinux label |                                                                                         |
| --mount=type=tmpfs,tmpfs-size=10G,dst=/build | a 10G build directory and mtr under podman                                        | keeps as transient, big enough for some mtr tests                                       |
| --tmpfs /build:size=10G,exec,uid=1000        | a 10G build directory and mtr for docker                                          | keeps as transient, big enough for some mtr tests, exec and uid needed by build/tests   |
| --workdir /build                             | default directory                                                                 |                                                                                         |
| --entrypoint bash                            | Ensure the cmd of buildbot start isn't executed                                   |                                                                                         |
| --cap-add=SYS\_PTRACE                        | capability for tracing used by gdb                                                | for debugging                                                                           |
| Extra options                                |                                                                                   |                                                                                         |
| --name containername                         | useful if running multiple to keep track                                          | Used as a name for a new session in the container (podman exec -ti containername bash)  |
| --shm-size=10g                               | Size of /dev/shm as alternate for mtr tests                                       | Default is unsable 64k, This is large enough for most --big-tests with some parallelism |
| --privileged                                 | Allow rr recording                                                                | Note security impacting, don't run untrusted code as root                               |
| -v $DATADIR:/var/lib/mysql:Z                 | Mount an existing datadir                                                         | For testing against some prepared data                                                  |

Notes:

* docker can be used instead of the lighter weight podman if you so desired.
* /dev/shm is mounted no-exec so it rr recording here cannot be replayed while in that location
* optionally can make /build a filesystem mount to preserve the build.

There are environment variables that affect the cmake configure options and mtr are:

```
CXX=clang++
CC=clang
MSAN_LIBDIR=/msan-libs
CMAKE_GENERATOR=Ninja
MSAN_SYMBOLIZER_PATH=/usr/bin/llvm-symbolizer-20
WSREP_PROVIDER=/usr/lib/galera/libgalera_smm.so
MTR_PARALLEL=auto
ASAN_OPTIONS=quarantine_size_mb=512:atexit=0:detect_invalid_pointer_pairs=3:dump_instruction_bytes=1:allocator_may_return_null=1
UBSAN_OPTIONS=print_stacktrace=1:report_error_type=1
MSAN_OPTIONS=abort_on_error=1:poison_in_dtor=0
```

Note: galera WSREP\_PROVIDER isn't instrumented with any sanitizer

Check the latest version of these running `env`.

### Running an MSAN Build

Once you have started the MSAN container this is how you perform a MSAN build.

The time consuming aspect of building with MSAN is having [instrumented system libraries](https://github.com/MariaDB/buildbot/blob/main/ci_build_images/msan.instrumentedlibs.sh).

All the following instructions are executed within the container - there is a document in /etc/motd that contains the latest information. Start by running the configure stage of `cmake`:

```
cmake \
      -DUPDATE_SUBMODULES=OFF \
      -DWITH_MSAN=ON  \
      -DCMAKE_{EXE,MODULE}_LINKER_FLAGS="-L${MSAN_LIBDIR} -Wl,-rpath=${MSAN_LIBDIR}" \
      -DHAVE_CXX_NEW=1  \
      -DWITH_INNODB_{BZIP2,LZ4,LZMA,LZO,SNAPPY}=OFF \
      -DWITH_ZLIB=bundled  \
      -DWITH_NUMA=NO  \
      -DWITH_SYSTEMD=NO \
      -DHAVE_LIBAIO_H=0    \
      -DCMAKE_DISABLE_FIND_PACKAGE_{URING,LIBAIO}=1  \
      -DPLUGIN_{MROONGA,ROCKSDB,OQGRAPH}=NO  \
      -DWITH_EMBEDDED_SERVER=OFF \
      /source
```

MSAN is a clang only compile options and other compilers will not work.

| CMake Options                                             | Why                                                                                                                                                |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| CMake Options                                             | Why                                                                                                                                                |
| UPDATE\_SUBMODULES=OFF                                    | The source directory is read-only so cannot be updated from within the container                                                                   |
| WITH\_MSAN=ON                                             | Enables MSAN build in compile options                                                                                                              |
| CMAKE\_{EXE,MODULE}\_LINKER\_FLAGS                        | links executables and shared libraries against the instrumented libraries with a rpath so a LD\_LIBRARY\_PATH environment variable isn't required  |
| WITH\_INNODB\_{BZIP2,LZ4,LZMA,LZO,SNAPPY}=OFF             | system libraries for these haven't been MSAN instrumented currently                                                                                |
| HAVE\_CXX\_NEW                                            | Works around a ODR violation                                                                                                                       |
| WITH\_ZLIB=bundled                                        | This hasn't been MSAN instrumented currently                                                                                                       |
| WITH\_NUMA / WITH\_SYSTEMD                                | both uninstrumented                                                                                                                                |
| HAVE\_LIBAIO\_H=0 / CMAKE\_DISABLE\_FIND\_PACKAGE\_LIBAIO | AIO currently not MSAN instrumented                                                                                                                |
| CMAKE\_DISABLE\_FIND\_PACKAGE\_URING=NO                   | Uninstrumented [MDEV-36482](https://jira.mariadb.org/browse/MDEV-36482), and required seccomp adjustment or --privileged to work                   |
| PLUGIN\_OQGRAPH (and PLUGIN\_COLUMNSTORE)                 | Dependency on boost libraries are instrumented                                                                                                     |
| WITH\_EMBEDDED\_SERVER=OFF                                | reduce build time                                                                                                                                  |
| WITH\_DBUG\_TRACE=OFF                                     | reduce runtime overhead if CMAKE\_BUILD\_TYPE=Debug chosen                                                                                         |

Run the build stage:

```
cmake --build . 
...
[100%] Built target mariadbd
[100%] Linking CXX executable mariadb-backup
Creating mariadb-backup link
[100%] Built target mariadb-backup
```

As the MSAN has rpath defined in its compile option there is no need for LD\_LIBRARY\_PATH manipulation.

To run tests:

```
mysql-test/mtr   (usual mtr options)
```

As newer versions occur and improvements happen these instructions may change. Look at the execution on the [buildbot builder](https://buildbot.mariadb.org/#/builders/amd64-debian-11-msan) to see if any changes have been made.

#### Bug Reporting

Use the MSAN in the label when reporting bugs.

Current outstanding MSAN bugs can be found on [JIRA by searching for this label](https://jira.mariadb.org/issues/?jql=labels%20%3D%20MSAN%20and%20status%20!%3D%20Closed).

### Running an combined ASAN and UBSAN Build

The clang implemented instrumentation of the MemoryStanitizer (MSAN) conflicts with the AddressSanitizer (ASAN) and UndefinedBehaviour (UBSAN) mechanisms, however ASAN and UBSAN can be combined into the same build.

After starting the MSAN container the following will configure a combined ASAN and UBSAN build:

```
cmake \
      -DUPDATE_SUBMODULES=OFF \
      -DWITH_ASAN=ON  \
      -DWITH_UBSAN=ON  \
      -DWITH_UNIT_TESTS=OFF \
     /source
```

| CMake Options                                   | Why                                                                                                                                                     |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CMake Options                                   | Why                                                                                                                                                     |
| UPDATE\_SUBMODULES=OFF                          | The source directory is read-only so cannot be updated from within the container                                                                        |
| WITH\_ASAN=ON                                   | Enables ASAN build in compile options                                                                                                                   |
| WITH\_UBSAN=ON                                  | Enables UBSAN build in compile options                                                                                                                  |
| WITH\_UNIT\_TESTS=OFF or PLUGIN\_PERFSCHEMA=OFF | clang is incompatible with performance schema unit tests, at least one must be disabled (ref: [MDEV-22940](https://jira.mariadb.org/browse/MDEV-22940)) |

Build and test run are standard.

Note: list of unfixed [UBSAN issues by MariaDB Corporation Testing](https://github.com/mariadb-corporation/mariadb-qa/blob/master/UBSAN.filter).

#### Bug Reporting

UBSAN bugs are labelled with `UBSAN` and also the short form of the undefined behaviour.

For example in the following output, the `insufficient-object-size` would be used as the additional short form of the label.

```
SUMMARY: UndefinedBehaviorSanitizer: insufficient-object-size /source/sql/item_strfunc.cc:5256:44 
 /source/sql/item_strfunc.cc:5256:44
```

Likewise for ASAN, should use `ASAN` as the label with the short form of the ASAN type from the output.

### Using RR

In the MSAN container there is a build version of the latest rr at the time of the container build.

A recording of the execution can be make with the [mariadb-test-run.pl option --rr](../../../../clients-and-utilities/testing-tools/mariadb-test/mariadb-test-run-pl-options.md). Or alternately you can execute:

```
$ rr record sql/mariadbd ......
```

To replay a recording adjust per the test worker and instance used in the test:

```
$ rr replay mysql-test/var/log/mysqld.1.rr/mariadbd-0/
```

Using curl in the container its possible to save up this directory for another user or developer to use with the same container. This can also be shared with our public ftp server for assistance diagnosing validating a bug report.

## ASAN Options

To run `mariadbd` with instrumentation you have to set the `ASAN_OPTIONS` environment variable before starting `mariadbd` including starting `mariadbd` when running mtr.

```
export ASAN_OPTIONS=abort_on_error=1
```

The above command will abort any instrumented executable if any errors are found, which is good for debugging. If you set abort\_on\_error=0 all server errors are logged to your error log file (mysqld.err).

To catch errors for other processes than the server, you can set more options, like this:

```
export ASAN_OPTIONS=abort_on_error=1:log_path=/tmp/asan
```

If you are seeing an incomplete stack trace for a memory allocation, you may rerun the failing test with

```
export ASAN_OPTIONS=abort_on_error=1:log_path=/tmp/asan:fast_unwind_on_malloc=0
```

To get core dumps of failures:

```
export ASAN_OPTIONS=abort_on_error=1:disable_coredump=0
```

To see all the options (or to check if an executable is instrumented), you may try the following:

```
ASAN_OPTIONS=help=1 extra/perror 0
```

### Using Valgrind

The [MariaDB test system](../../../../clients-and-utilities/testing-tools/mariadb-test/) can use [Valgrind](https://www.valgrind.org) for finding memory leaks and wrong memory accesses. Valgrind is an instrumentation framework for building dynamic analysis tools. If Valgrind is installed on your system, you can simply use [mysql-test-run --valgrind](../../../../clients-and-utilities/testing-tools/mariadb-test/mariadb-test-run-pl-options.md) to run the test under Valgrind.

## See Also

* [Compiling MariaDB for debugging](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/debugging-mariadb/compiling-mariadb-for-debugging)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
