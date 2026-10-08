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

A better solution is to directly ask the filesystem to provide an atomic (all or nothing) write guarantee. This is only available on [a few SSD cards](atomic-write-support.md#devices-that-support-atomic-writes-with-mariadb).

## Enabling Atomic Writes

MariaDB automatically detects if any of the supported SSD cards are used.

When opening an InnoDB table, there is a check if the tablespace for the table is [on a device that supports atomic writes](atomic-write-support.md#devices-that-support-atomic-writes-with-mariadb) and if yes, it will automatically enable atomic writes for the table. If atomic writes support is not detected, the doublewrite buffer will be used.

One can disable atomic write support for all cards by setting the variable [innodb-use-atomic-writes](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md) to `OFF` in your my.cnf file. It's `ON` by default.

How InnoDB uses atomic writes:

* When a data file is on a device that supports atomic writes, InnoDB skips the [doublewrite buffer](../../../../server-usage/storage-engines/innodb/innodb-doublewrite-buffer.md) for that tablespace. Other tablespaces still use it.
* On Linux and other Unix-like systems, if atomic writes may be available, InnoDB forces [innodb\_flush\_method](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_flush_method) to `O_DIRECT`.
* On Windows, single-sector writes are always atomic, so InnoDB uses atomic writes for a data file when the InnoDB page size equals the device's physical sector size.

## Devices that Support Atomic Writes with MariaDB

MariaDB supports atomic writes on the following devices:

* [Fusion-io devices with the NVMFS file system](fusion-io/fusion-io-introduction.md#atomic-writes).
* [Shannon SSD](https://www.shannon-sys.com).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
