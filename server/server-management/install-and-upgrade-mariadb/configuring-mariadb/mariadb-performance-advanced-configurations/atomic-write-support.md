---
description: >-
  Explains the concept of atomic writes in MariaDB, which improve performance
  and data integrity on SSDs by bypassing the InnoDB doublewrite buffer,
  supported on devices like Fusion-io and Shannon SSDs.
---

# Atomic Write Support

{% hint style="info" %}
For the OS-level meaning of `O_DIRECT` and the other `innodb_flush_method` values mentioned on this page, see [Storage I/O: Buffering and Persistence](../../../../ha-and-performance/optimization-and-tuning/operating-system-optimizations/storage-io-buffering-and-persistence.md).
{% endhint %}

## Partial Write Operations

When Innodb writes to the filesystem, there is generally no guarantee that a given write operation will be complete (not partial) in cases of a poweroff event, or if the operating system crashes at the exact moment a write is being done.

Without detection or prevention of partial writes, the integrity of the database can be compromised after recovery.

## `innodb_doublewrite`--an Imperfect Solution

Since its inception, Innodb has had a mechanism to detect and ignore partial writes via the [InnoDB Doublewrite Buffer](../../../../server-usage/storage-engines/innodb/innodb-doublewrite-buffer.md) (also `innodb_checksum` can be used to detect a partial write).

Doublewrites, controlled by the [innodb\_doublewrite](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md) system variable, comes with its own set of problems. Especially on SSD, writing each page twice can have detrimental effects (write leveling).

## Atomic Write - a Faster Alternative to `innodb_doublewrite`

A better solution is to directly ask the filesystem to provide an atomic (all or nothing) write guarantee. Currently this is only available on [a few SSD cards](atomic-write-support.md#devices-that-support-atomic-writes-with-mariadb).

## Enabling Atomic Writes from [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102)

When starting, [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102) and beyond automatically detects if any of the supported SSD cards are used.

When opening an InnoDB table, there is a check if the tablespace for the table is [on a device that supports atomic writes](atomic-write-support.md#devices-that-support-atomic-writes-with-mariadb) and if yes, it will automatically enable atomic writes for the table. If atomic writes support is not detected, the doublewrite buffer will be used.

One can disable atomic write support for all cards by setting the variable [innodb-use-atomic-writes](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md) to `OFF` in your my.cnf file. It's `ON` by default.

## Enabling Atomic Writes in [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) to [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1)

To use atomic writes instead of the doublewrite buffer, add:

```ini
innodb_use_atomic_writes = 1
```

to the `my.cnf` config file.

Note that atomic writes are only supported on [Fusion-io devices that use the NVMFS file system](fusion-io/fusion-io-introduction.md#atomic-writes) in these versions of MariaDB.

### About innodb\_use\_atomic\_writes (in [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) to [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1))

The following happens when atomic writes are enabled

* if [innodb\_flush\_method](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md) is neither `O_DIRECT`, `ALL_O_DIRECT`, or `O_DIRECT_NO_FSYNC`, it is switched to `O_DIRECT`
* [innodb\_use\_fallocate](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md) is switched `ON` (files are extended using `posix_fallocate` rather than writing zeros behind the end of file)
* Whenever an Innodb datafile is opened, a special `ioctl()` is issued to switch on atomic writes. If the call fails, an error is logged and returned to the caller. This means that if the system tablespace is not located on an atomic write capable device or filesystem, InnoDB/XtraDB will refuse to start.
* if [innodb\_doublewrite](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md) is set to `ON`, `innodb_doublewrite` will be switched `OFF` and a message written to the error log.

Here is a flowchart showing how atomic writes work inside InnoDB:

```mermaid
flowchart TD
    accTitle: InnoDB atomic write support internals
    accDescr {
        Two decision flows. Initialization checks whether innobase_use_atomic_writes
        is set; if so, doublewrite is switched off, the flush method is set to
        O_DIRECT, and posix_fallocate pre-allocates the tablespace, before either
        path continues with the existing flow. Opening a data file issues an ioctl
        to enable atomic writes; success continues normally, while failure on the
        ibdata1 system tablespace stops mysqld from starting, and failure on any
        other file closes it, logs the error, and returns failure to the caller.
    }

    subgraph INIT["Initialization"]
        direction TD
        I0(["MySQL (init)"])
        ID1{"innobase_use_atomic_writes set?"}
        IA["Switch off doublewrite<br/>Set flush method to O_DIRECT<br/>Use posix_fallocate to pre-allocate tablespace"]
        IC(["Continue with existing flow"])
        I0 --> ID1
        ID1 -->|Yes| IA
        ID1 -->|No| IC
        IA --> IC
    end

    subgraph OPEN["Opening a Data File"]
        direction TD
        O0(["MySQL (open data file if innobase_use_atomic_writes set)"])
        OD1{"ioctl to underlying file system succeeds?"}
        OD2{"Is it ibdata1 file?"}
        OC(["Continue with existing flow"])
        OF(["mysqld doesn't start"])
        OE["Close the file, log the error, and return failure to caller"]
        O0 --> OD1
        OD1 -->|Yes| OC
        OD1 -->|No| OD2
        OD2 -->|Yes| OF
        OD2 -->|No| OE
    end

    classDef start fill:#3aa0e6,stroke:#1f6fa8,stroke-width:2px,color:#111;
    classDef decision fill:#f7ca18,stroke:#a97c0c,stroke-width:2px,color:#111;
    classDef action fill:#f0932b,stroke:#b5701d,stroke-width:2px,color:#111;
    classDef terminal fill:#5cb85c,stroke:#2f7d2f,stroke-width:2px,color:#111;
    classDef fail fill:#e6553a,stroke:#a63a26,stroke-width:2px,color:#111;
    class I0,O0 start
    class ID1,OD1,OD2 decision
    class IA,OE action
    class IC,OC terminal
    class OF fail
```

_Initialization checks the atomic-writes setting before continuing, while opening a data file checks the ioctl result, treating a failed ibdata1 open as fatal and any other file as a closable error._

## Devices that Support Atomic Writes with MariaDB

MariaDB currently supports atomic writes on the following devices:

* [Fusion-io devices with the NVMFS file system](fusion-io/fusion-io-introduction.md#atomic-writes) . [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and above.
* [Shannon SSD](https://www.shannon-sys.com). [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102) and above.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
