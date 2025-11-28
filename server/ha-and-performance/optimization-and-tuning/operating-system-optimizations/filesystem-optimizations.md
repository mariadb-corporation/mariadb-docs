# Filesystem Optimizations

## Suitability of Filesystems

The filesystem is not the most important aspect of MariaDB performance. More important are the available memory (RAM), the drive speed, and the system variable settings (see [Hardware Optimization](../../hardware-optimization.md) and [System Variables](../system-variables/)).

Optimizing the filesystem can, however, make a noticeable difference in some cases. Among the best suited Linux filesystems are ext4, XFS and Btrfs. They are all included in the mainline Linux kernel and are widely supported and available on most Linux distributions.

The following theoretical file size and filesystem size limits apply to those filesystems:

| Limit               | ext4                                       | XFS                                      | Btrfs                                        |
| ------------------- | ------------------------------------------ | ---------------------------------------- | -------------------------------------------- |
| Links               | [ext4](https://en.wikipedia.org/wiki/Ext4) | [XFS](https://en.wikipedia.org/wiki/XFS) | [Btrfs](https://en.wikipedia.org/wiki/Btrfs) |
| Max file size       | 16-256 TB                                  | 8 EB                                     | 16 EB                                        |
| Max filesystem size | 1 EB                                       | 8 EB                                     | 16 EB                                        |

Each has unique characteristics that are worth understanding to get the most from their usage.

## Disabling Access Time

It's unlikely you'll need to record file access time on a database server, and mounting your filesystem with this disabled can give an easy improvement in performance. To do so, use the `noatime` option.

If you want to keep access time for [log files](../../../server-management/server-monitoring-logs/) or other system files, these can be stored on a separate drive.

## Using NFS

Generally, we recommend not to use [NFS](https://en.wikipedia.org/wiki/Network_File_System) (Network File System) with MariaDB, for these reasons:

* MariaDB data and log files on NFS volumes can become locked and unavailable for use. Locking issues may occur in cases where multiple instances of MariaDB access the same data directory, or when MariaDB is shut down improperly, for instance, due to a power outage. In particular, sharing a data directory among MariaDB instances is not recommended.
* Data inconsistencies due to messages received out of order or lost network traffic. To avoid this issue, use TCP with `hard` and `intr` mount options.

Using NFS within a professional SAN[^1] environment or other storage system tends to offer greater reliability than using NFS outside of such an environment. However, NFS within a SAN environment may be slower than directly attached or bus-attached non-rotational storage.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}

[^1]: A Storage Area Network (SAN) is a dedicated high-speed network that connects storage devices to servers, enabling the storage to appear as if it is directly attached to the server's operating system.
