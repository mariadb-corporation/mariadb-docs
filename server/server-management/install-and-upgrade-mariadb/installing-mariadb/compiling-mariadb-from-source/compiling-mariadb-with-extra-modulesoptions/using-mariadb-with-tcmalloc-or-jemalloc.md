---
description: >-
  Instructions on building and configuring MariaDB to use alternative memory
  allocators like TCMalloc or jemalloc for improved performance and profiling.
---

# Using MariaDB with TCMalloc or jemalloc

{% hint style="info" %}
Read the [Profiling Memory Usage](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/community/community/bug-tracking/profiling-memory-usage) page for more information on how to debug high memory consumption.
{% endhint %}

## Using tcmalloc or jemalloc

[TCMalloc](https://goog-perftools.sourceforge.net/doc/tcmalloc.html) is a malloc replacement library optimized for multi-threaded usage. It features a built-in heap debugger and profiler. Another malloc replacement that can speed up MariaDB is [jemalloc](https://jemalloc.net/).

The procedures to use one of these libraries with MariaDB are the same. Many other malloc replacement libraries (as well as heap debuggers and profilers) can be used with MariaDB in a similar fashion.

## Prerequisites

`jemalloc` is a powerhouse for reducing memory fragmentation and improving concurrency, but it isn't a "one-size-fits-all" drop-in for every environment. Its availability and stability depend heavily on how the operating system handles memory pages and how MariaDB was compiled.

### Operating System Availability

* Linux: Jemalloc is most at home here. Most major distributions (Ubuntu, Debian, CentOS/RHEL, Arch) include it in their official repositories (`libjemalloc2` or `jemalloc`). It is the standard recommendation for high-traffic MariaDB setups on Linux.
* Windows: Jemalloc does not have the same "native" presence on Windows. While the `jemalloc` source code can technically be compiled for Windows using MSVC or MinGW, MariaDB for Windows is almost exclusively used with the default Windows system allocator. Most DBAs do not use `jemalloc` on Windows production servers.
* FreeBSD: This is the "birthplace" of `jemalloc` – it replaced the system malloc in FreeBSD back in 2005. If you are running MariaDB on FreeBSD, you are likely using `jemalloc` by default at the OS level.

### Hardware and Architecture Hurdles

One of the most common "hidden" failures occurs on non-x86 architectures:

* Raspberry Pi (ARM): On newer devices like the Raspberry Pi 5, `jemalloc` often fails to start with the error: `<jemalloc>: Unsupported system page size`. This happens because `jemalloc` is frequently compiled assuming a 4KB page size, while many ARM kernels now use 16KB or 64KB pages for better performance.
* Cloud Instances: Small instances (like AWS `t2.micro`) can sometimes behave unpredictably with `jemalloc` if they lack sufficient swap space or if the memory overhead of the `jemalloc` metadata conflicts with the tiny RAM footprint.

### Compatibility Matrix Summary

| **Platform**    | **Jemalloc Support** | **Typical Usage**                                    |
| --------------- | -------------------- | ---------------------------------------------------- |
| Linux (x86\_64) | Excellent            | Highly recommended; installed via `apt` or `yum`.    |
| FreeBSD         | Native               | It is the system default.                            |
| Windows         | Poor/Partial         | Rarely used; usually requires custom builds.         |
| ARM (RPi/M1/M2) | Conditional          | Depends on the kernel page size (4KB vs 16KB).       |
| Solaris/Illumos | Experimental         | Possible but lacks the robust testing seen on Linux. |

### Check if it's Ready to Use

Before trying to force it via `LD_PRELOAD`, check if the library even exists on your system paths:

```bash
# On Debian/Ubuntu
find /usr/lib -name "libjemalloc.so.*"

# On RHEL/CentOS
find /usr/lib64 -name "libjemalloc.so.*"
```

If these commands return nothing, you need to install the package first (`sudo apt install libjemalloc2` or `sudo dnf install jemalloc`).

### Why Use it

The main reason to switch isn't just speed, but fragmentation. Standard `malloc` can leave small gaps of unused memory that the OS can't reclaim, leading to "memory bloat" where MariaDB appears to use 10GB of RAM even if the data only needs 6GB. Jemalloc is much better at packing these allocations tightly.

## Checking the malloc Implementation in Use

To check which `malloc` implementation is used, run this query:

```bash
SHOW GLOBAL VARIABLES LIKE 'version_malloc_library';
+------------------------+--------+
| Variable_name          | Value  |
+------------------------+--------+
| version_malloc_library | system |
+------------------------+--------+
```

A value of `system` indicates the system default, which is normally `malloc`. If another library is used, the name and version of the library is shown.

## Building MariaDB With an Alternative to malloc

To build MariaDB with `TCMalloc`, you need to use the following command:

```bash
cmake -DCMAKE_EXE_LINKER_FLAGS='-ltcmalloc'  -DWITH_SAFEMALLOC=OFF
```

To use `jemalloc`, specify `-ljemalloc` instead of `-ltcmalloc`.

## Starting mariadbd-safe With an Alternative to malloc

Start a standard MariaDB server with `TCmalloc` like this:

```bash
/usr/sbin/mariadbd-safe --malloc-lib=tcmalloc
```

To configure [mariadbd-safe](../../../../starting-and-stopping-mariadb/mariadbd-safe.md) to use `tcmalloc` or `jemalloc`, add this to your [configuration file](../../../configuring-mariadb/configuring-mariadb-with-option-files.md):

```ini
[mariadbd-safe]
malloc-lib=tcmalloc
```

## Starting mariadbd With an Alternative to malloc

Locate the library file that needs to be used:

```bash
# jemalloc
find /usr/lib -name "libjemalloc.so.*"
# tcmalloc
find /usr/lib -name "libtcmalloc.so.*"
```

Pass that library file to `mariadbd` using the `LD_PRELOAD` variable:

```bash
LD_PRELOAD=/path/to/library mariadbd
```

## Configuring systemd

If you use `systemd` to run MariaDB, locate the library as explained above, then locate the service configuration file:

```bash
systemctl status mariadb | grep Loaded
```

Edit the `mariadb.service` file by adding a line to the `[Service]` group:

```bash
[Service]
Environment=LD_PRELOAD=<path-to-library>
```

For example, add this:

```ini
[Service]
Environment=LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libjemalloc.so.2
```

Reload the configuration for the news setting to take effect, and restart MariaDB:

```bash
systemctl daemon-reload
systemctl restart mariadb
```

## Dockerfile

If you run [MariaDB on Docker](../../../../automated-mariadb-deployment-and-administration/docker-and-mariadb/) and use an image from a Dockerfile that is publicly available, most probably you have an entry point that is a bash script, which starts `mariadbd` directly. Edit that bash script, or set the `LD_PRELOAD` variable from the Dockerfile:

```bash
ENV LD_PRELOAD=<path-to-library>
```

To find the library file, run one of these commands while the container is running:

```bash
# jemalloc
docker exec -ti <container-name> find /usr/lib -name "libjemalloc.so.*"
# tcmalloc
docker exec -ti <container-name> find /usr/lib -name "libtcmalloc.so.*"
```

Example:

{% code overflow="wrap" %}
```bash
docker run -P -d --name mariadb --env LD_PRELOAD="/usr/lib/x86_64-linux-gnu/libjemalloc.so.2" --env MARIADB_ROOT_PASSWORD=Password123! mariadb:latest
```
{% endcode %}

## Vagrantfile

Usually [Vagrant](../../../../automated-mariadb-deployment-and-administration/vagrant-and-mariadb/) is used to start a complete system in a virtual machine. In that case, you can use one of the methods above, for example you can modify your Vagrantfile to copy a modified version of the `mariadb.service` file to the guest system to configure systemd.

If you use Vagrant with the Docker provider, you can follow the instructions above to modify the Dockerfile.

## Making jemalloc Persistent

To make MariaDB use `jemalloc` persistently, set it up like this. These instructions work on Linux using `systemd` and running on an x86 architecture.

### Steps

{% stepper %}
{% step %}
### Identify the jemalloc library path.

Identify the `jemalloc` library path, to find the exact location of the `jemalloc` shared library on your system:

```bash
find /usr -name "libjemalloc.so.*"
```

Take a note of the output path. Typically, it is something like `/usr/lib64/libjemalloc.so.2`.
{% endstep %}

{% step %}
### Create or edit the MariaDB Systemd override file.

This is the crucial step for persistence. Use `systemctl edit` to manage the override file:

```bash
sudo systemctl edit mariadb
```

If an override file already exists for MariaDB, it opens in the editor. If not, the editor creates a new, empty file, typically at `/etc/systemd/system/mariadb.service.d/override.conf`. Add the following content to the file:

```ini
[Service] 
Environment="LD_PRELOAD=/usr/lib64/libjemalloc.so.2"
```

Replace `/usr/lib64/libjemalloc.so.2` with the actual path you noted in step 1. Save the file and exit the editor.
{% endstep %}

{% step %}
### Restart services and MariaDB.

```bash
sudo systemctl daemon-reexec 
sudo systemctl daemon-reload 
sudo systemctl restart mariadb
```
{% endstep %}

{% step %}
### Reboot the computer, and verify that jemalloc is used.

You can verify this on various levels.

MariaDB:

```bash
mariadb -e "SHOW GLOBAL VARIABLES LIKE 'version_malloc_library';"
+------------------------+------------------------------------------------------------+ 
| Variable_name          | Value                                                      | 
+------------------------+------------------------------------------------------------+ 
| version_malloc_library | jemalloc 5.2.1-0-gea6b3e973b477b8061e0076bb257dbd7f3faa756 | 
+------------------------+------------------------------------------------------------+
```

Operating system:

```bash
sudo cat /proc/$MARIADB_PID/environ | tr '\0' '\n' | grep LD_PRELOAD
LD_PRELOAD=/usr/lib64/libjemalloc.so.2
```

Operating system processes:

```bash
sudo cat /proc/$MARIADB_PID/maps | grep jemalloc
7f6981c00000-7f6981c06000 r--p 00000000 fd:00 50981369 /usr/lib64/libjemalloc.so.2 
7f6981c06000-7f6981c76000 r-xp 00006000 fd:00 50981369 /usr/lib64/libjemalloc.so.2 
7f6981c76000-7f6981c81000 r--p 00076000 fd:00 50981369 /usr/lib64/libjemalloc.so.2 
7f6981c81000-7f6981c87000 r--p 00080000 fd:00 50981369 /usr/lib64/libjemalloc.so.2 
7f6981c87000-7f6981c88000 rw-p 00086000 fd:00 50981369 /usr/lib64/libjemalloc.so.2
```
{% endstep %}
{% endstepper %}

### Notes

`systemctl edit` creates a separate configuration file (`/etc/systemd/system/mariadb.service.d/override.conf`). `systemd` always prioritizes settings in  override files over the main service file (`/usr/lib/systemd/system/mariadb.service`).

When upgrading MariaDB, the package manager only replaces or updates the main service file. Your custom override file in `/etc/systemd/system/mariadb.service.d/` remains untouched, thus preserving your `jemalloc` configuration.

`systemd` reads all its service configurations, including override files, on system start. This means the `LD_PRELOAD` environment variable is set for MariaDB automatically each time the service starts, making the change persistent across reboots.

## Finding memory leaks with jemalloc

`jemalloc` provides a report of memory leaks at program exit:

```bash
MALLOC_CONF=prof_leak:true,lg_prof_sample:0,prof_final:true \
LD_PRELOAD=${JEMALLOC_PATH}/lib/libjemalloc.so.2  path-to-mariadbd
```

This produces output like this:

```
<jemalloc>: Leak summary: 267184 bytes, 473 objects, 20 contexts
<jemalloc>: Run jeprof on "jeprof.19678.0.f.heap" for leak detail
```

You can learn more about the memory leaks with `jeprof`, which is shipped with jemalloc:

```bash
jeprof --show_bytes path-to-mariadbd jeprof.19678.0.f.heap
```

You can also generate a PDF call graph of the leak:

```bash
jeprof --show_bytes --pdf path-to-mariadbd  jeprof.19678.0.f.heap > /tmp/mariadbd.pdf
```

## See Also

* [Profiling memory usage](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/community/community/bug-tracking/profiling-memory-usage)
* [Jemalloc leak checking](https://github.com/jemalloc/jemalloc/wiki/Use-Case:-Leak-Checking)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
