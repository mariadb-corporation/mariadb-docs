---
description: >-
  Fusion-io develops PCIe based NAND flash memory cards and related software
  that can be used to speed up MariaDB databases.
---

# Fusion-io Introduction

The ioDrive branded products can be used as block devices (super-fast disks) or to extend basic DRAM memory. ioDrive is deployed by installing it on an x86 server and then installing the card driver under the operating system. All main line 64-bit operating systems and hypervisors are supported: RHEL, CentOS, SuSe, Debian, OEL etc. and VMware, Microsoft Windows/Server etc. Drivers and their features are constantly developed further.

ioDrive cards support software RAID and you can combine two or more physical cards into one logical drive. Through ioMemory SDK and its APIs, one can integrate and enable more thorough interworking between your own software and the cards - and cut latency.

The key differentiator between a Fusion-io and a legacy SSD/HDD is the following: **A Fusion-io card is connected directly on the system bus (PCIe)**, this enables high data transfer throughput (1.5 GB/s, 3.0 GB/s or 6GB/s) and the fast direct memory access (DMA) method can be used to transfer data. The ATA/SATA protocol stack is omitted and therefore latency is cut short. Fusion-io performance is dependent on server speed: the faster processors and the newer PCIe-bus version you have, the better is the ioDrive performance. Fusion-io memory is non-volatile, in other words, data remains on the card even when the server is powered off.

## Use Cases

1. You can start by using ioDrive for database files that need heavy random access.
2. Whole database on ioDrive.
3. In some cases, Fusion-io devices allow for atomic writes, which allows the server to safely disable the [doublewrite buffer](../../../../../server-usage/storage-engines/innodb/innodb-doublewrite-buffer.md).
4. Use ioDrive as a write-through read cache. This is possible on server level with Fusion-io directCache software or in VMware environments using ioTurbine software or the ioCache bundle product. Reads happen from ioDrive and all writes go directly to your SAN or disk.
5. Highly Available shared storage with ION. Have two different hosts, Fusion-io cards in them and share/replicate data with Fusion-io's ION software.
6. The luxurious Platinum setup: [MariaDB Galera Cluster](https://kb.askmonty.org/en/what-is-mariadb-galera-cluster/) running on Fusion-io SLC cards on several hosts.

## Atomic Writes

Starting with [MariaDB 5.5.31](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5531-release-notes), MariaDB Server supports atomic writes on Fusion-io devices that use the NVMFS (formerly called DirectFS) file system. Unfortunately, NVMFS was never offered under ‘General Availability’, and SanDisk declared that NVMFS would reach end-of-life in December 2015. Therefore, NVMFS support is no longer offered by SanDisk.

MariaDB Server does not currently support atomic writes on Fusion-io devices with any other file systems.

See [atomic write support](../atomic-write-support.md) for more information about MariaDB Server's atomic write support.

## Future Suggested Development

* Extend InnoDB disk cache to be stored on Fusion-io acting as extended memory.

## Settings For Best Performance

Fusion-io memory can be formatted with different sector size of either 512 or 4096 bytes. Bigger sectors are expected to be faster, but only if I/O is done in blocks of 4KB or multiples of that. Speaking of MariaDB: if only InnoDB data files are stored in Fusion-io memory, all I/O is done in blocks of 16K and thus 4K sector size can be used. If the InnoDB redo log (I/O block size: 512 bytes) goes to the same Fusion-io memory, then short sectors should be used.

Note: XtraDB has the experimental feature of an increased InnoDB log block size of 4K. If this is enabled, then both redo log I/O and page I/O in InnoDB will match a sector size of 4K.

As of file systems: currently XFS is expected to yield the best performance with MariaDB. However depending on the exact kernel version and version of XFS code in use, one might be affected by [a bug that severely limits XFS performance in concurrent environments](https://www.mysqlperformanceblog.com/2012/03/15/ext4-vs-xfs-on-ssd/comment-page-1/#comment-903938). This has [been fixed in kernel versions above 3.5](https://github.com/torvalds/linux/commit/507630b29f13a3d8689895618b12015308402e22) or [RHEL6 kernels kernel-2.6.32-358 or later](https://rhn.redhat.com/errata/RHSA-2013-0496.html) (because of [bug 807503 being fixed)](https://bugzilla.redhat.com/show_bug.cgi?id=807503).

For the pitbull machine where I have run such tests, ext4 was faster than xfs for 32 or more threads:

* up to 8 threads xfs was few percent faster (10% on average).
* at 16 threads it was a draw (2036 tps vs. 2070 tps).
* at 32 threads ext4 was 28% faster (2345 tps vs. 1829 tps).
* at 64 threads ext4 was even 47% faster (2362 tps vs. 1601 tps).
* at higher concurrency ext4 lost its bite, but was still constantly better than xfs.

Those numbers are for spinning disks. I guess for Fusion-io memory the XFS numbers will be even worse.

## Example Configuration

![GE-Fusionio-MariaDB](../../../../../.gitbook/assets/GE-Fusionio-MariaDB.png)

## Card Models

There are several card models. ioDrive is older generation, ioDrive2 is newer. SLC sustains more writes. MLC is good enough for normal use.

1. ioDrive2, capacities per card 365GB, 785GB, 1.2TB with MLC. 400GB and 600GB with SLC, performance up to 535000 IOPS & 1.5GB/s bandwidth
2. ioDrive2 Duo, capacities per card 2.4TB MLC and 1.2TB SLC, performance up to 935000 IOPS & 3.0GB/s bandwidth
3. ioDrive, capacities per card 320GB, 640GB MLC and 160GB, 320GB SLC, performance up to 145000 IOPS & 790MB/s bandwidth
4. ioDrive Duo, capacities per card 640GB, 1.28TB MLC and 320GB, 640GB SLC, performance up to 285000 IOPS & 1.5GB/s bandwidth
5. ioDrive Octal, capacities per card 5TB and 10TB MLC, performance up to 1350000 IOPS & 6.7GB/s bandwidth
6. ioFX, a 420GB QDP MLC workstation product, 1.4GB/s bandwidth
7. ioCache, a 600GB MLC card with ioTurbine software bundle that can be used to speed up VMware based virtual hosts.
8. ioScale, 3.2TB card, building block to enable all-flash data center build out in hyperscale web and cloud environments. Product has been developed in co-operation with Facebook.

## Additional Software

* directCache - transforms ioDrive to work as a read cache in your server. Writes go directly to your SAN
* ioTurbine - read cache software for VMware
* ION - transforms ioDrive into a shareable storage
* ioSphere - software to manage and monitor several ioDrives

## See Also

* [FusionIO atomic-series devices](https://www.fusionio.com/products/atomic-series)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
