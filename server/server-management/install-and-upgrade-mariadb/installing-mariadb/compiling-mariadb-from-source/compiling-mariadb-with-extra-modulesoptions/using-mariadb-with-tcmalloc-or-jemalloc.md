---
description: >-
  Instructions on building and configuring MariaDB to use alternative memory
  allocators like TCMalloc or jemalloc for improved performance and profiling.
---

# Using MariaDB with TCMalloc or jemalloc

Read the [Profiling Memory Usage](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/community/community/bug-tracking/profiling-memory-usage) page for more information on how to debug high memory consumption.

### Using tcmalloc or jemalloc

[TCMalloc](https://goog-perftools.sourceforge.net/doc/tcmalloc.html) is a malloc replacement library optimized for multi-threaded usage. It also features a built-in heap debugger and profiler.

Another malloc replacement that may speed up MariaDB is [jemalloc](https://jemalloc.net/).

The procedures to use one of these libraries with MariaDB are the same. Many other malloc replacement libraries (as well as heap debuggers and profilers) can be used with MariaDB in a similar fashion.

#### Checking the malloc Implementation in Use

If you are unsure which malloc implementation is in use, or if you used one of the procedures explained in this page and you want to verify if it succeeded, you can run this query:

```bash
SHOW GLOBAL VARIABLES LIKE 'version_malloc_library';
```

A value of "system" indicates the system default, which is normally malloc. If another library is used, this query will return the name and version of the library.

#### Building MariaDB with an alternative to malloc

To build [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5) with `TCMalloc`, you need to use the following command

```bash
cmake -DCMAKE_EXE_LINKER_FLAGS='-ltcmalloc'  -DWITH_SAFEMALLOC=OFF
```

To use jemalloc, the option should be `-ljemalloc`.

#### Starting mariadbd-safe with an alternative to malloc

If you want to do this only one time, as a test, you can also start a standard MariaDB server with `TCmalloc` with:

```bash
/usr/sbin/mariadbd-safe --malloc-lib=tcmalloc
```

If you want to configure [mariadbd-safe](../../../../starting-and-stopping-mariadb/mariadbd-safe.md) to use tcmalloc or jemalloc, edit your [configuration file](../../../configuring-mariadb/configuring-mariadb-with-option-files.md), in the `[mariadbd-safe]` group:

```bash
malloc-lib=tcmalloc
```

#### Starting mariadbd with an alternative to malloc

First, locate the library file that needs to be used:

```bash
# jemalloc
find /usr/lib -name "libjemalloc.so.*"
# tcmalloc
find /usr/lib -name "libtcmalloc.so.*"
```

Now pass it to `mariadbd` using the `LD_PRELOAD` variable:

```bash
LD_PRELOAD=/path/to/library mariadbd
```

For example, on OpenSuse 15.4 one would do:

#### Configuring systemd

If you use systemd to run MariaDB, first locate the library as explained above. The locate the service configuration file:

```bash
systemctl status mariadb |grep Loaded
```

Now edit the `mariadb.service` file by adding a line to the `[Service]` group:

```bash
Environment=LD_PRELOAD=<path-to-library>
```

For example:

```ini
[Service]
Environment=LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libjemalloc.so.2
```

Now you should reload the configuration, so that the news setting will take effect, and restart MariaDB:

```bash
systemctl daemon-reload
systemctl restart mariadb
```

#### Dockerfile

If you run [MariaDB on Docker](../../../../automated-mariadb-deployment-and-administration/docker-and-mariadb/) and use an image from a Dockerfile that is publicly available, most probably you have an entrypoint that is a Bash script, which starts `mariadbd` directly. You can edit this Bash script as explained above. Or you can set the `LD_PRELOAD` variable from the Dockerfile:

```bash
ENV LD_PRELOAD=<path-to-library>
```

To find the library file you can run one of these commands while the container is running:

```bash
# jemalloc
docker exec -ti <container-name> find /usr/lib -name "libjemalloc.so.*"
# tcmalloc
docker exec -ti <container-name> find /usr/lib -name "libtcmalloc.so.*"
```

Example:

```bash
docker run -P -d --name mariadb --env LD_PRELOAD="/usr/lib/x86_64-linux-gnu/libjemalloc.so.2" --env MARIADB_ROOT_PASSWORD=Password123! mariadb:latest
```

#### Vagrantfile

Usually [Vagrant](../../../../automated-mariadb-deployment-and-administration/vagrant-and-mariadb/) is used to start a complete system in a virtual machine. If this is your case, you can use one of the methods above, for example you can modify your Vagrantfile to copy a modified version of the `mariadb.service` file into the guest system to configure systemd.

If you use Vagrant with the Docker provider, you can follow the instructions above to modify the Dockerfile.

### Finding memory leaks with jemalloc

jemalloc can provide a report of memory leaks at program exit:

```bash
MALLOC_CONF=prof_leak:true,lg_prof_sample:0,prof_final:true \
LD_PRELOAD=${JEMALLOC_PATH}/lib/libjemalloc.so.2  path-to-mariadbd
```

This will produce something like:

```
<jemalloc>: Leak summary: 267184 bytes, 473 objects, 20 contexts
<jemalloc>: Run jeprof on "jeprof.19678.0.f.heap" for leak detail
```

You can learn more about the memory leaks with jeprof, that is included with jemalloc:

```bash
jeprof --show_bytes path-to-mariadbd jeprof.19678.0.f.heap
```

You can also generate a PDF call graph of the leak:

```bash
jeprof --show_bytes --pdf path-to-mariadbd  jeprof.19678.0.f.heap > /tmp/mariadbd.pdf
```

### See Also

* [Profiling memory usage](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/community/community/bug-tracking/profiling-memory-usage)
* [Debugging a running server on Linux](/broken/spaces/WCInJQ9cmGjq1lsTG91E/pages/KggZ6kWNn0qD0bBBw1kX)
* [Jemalloc leak checking](https://github.com/jemalloc/jemalloc/wiki/Use-Case:-Leak-Checking)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
