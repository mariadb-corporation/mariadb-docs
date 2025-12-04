# Installing TokuDB

{% include "../../../../.gitbook/includes/tokudb-has-been-deprecated-....md" %}

Note that ha\_tokudb is not included in binaries built with the "old" glibc. Binaries built with glibc 2.14+ do include it.

The following sections detail how to install and enable TokuDB.

## Installing TokuDB

Until MariaDB versions 5.5.39 and 10.0.13, before upgrading TokuDB, the server needed to be cleanly shut down. If the server was not cleanly shut down, TokuDB would fail to start. Since 5.5.40 and 10.0.14, this has no longer been necessary. See [MDEV-6173](https://jira.mariadb.org/browse/MDEV-6173).

TokuDB has been included with MariaDB since [MariaDB 5.5.34](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5534-release-notes) and [MariaDB 10.0.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1006-release-notes) and does not require separate installation. Proceed straight to [Check for Transparent HugePage Support on Linux](installing-tokudb.md#check-for-transparent-hugepage-support-on-linux). For older versions, see the distro-specific instructions below.

### Installing TokuDB on Fedora, RedHat, & CentOS

In [MariaDB 5.5.33](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5533-release-notes), [MariaDB 10.0.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1005-release-notes), and starting from [MariaDB 10.2.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1025-release-notes) TokuDB is in a separate RPM package\
called `MariaDB-tokudb-engine` and is installed as follows:

```
sudo yum install MariaDB-tokudb-engine
```

### Installing TokuDB on Ubuntu & Debian

On Ubuntu, TokuDB is available on the 64-bit versions of Ubuntu 12.10 and\
newer. On Debian, TokuDB is available on the 64-bit versions of Debian 7\
"Wheezy" and newer.

The package is installed as follows:

```
sudo apt-get install mariadb-plugin-tokudb
```

In some earlier versions, from [MariaDB 5.5.33](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5533-release-notes) and [MariaDB 10.0.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1005-release-notes), TokuDB is in a separate package called`mariadb-tokudb-engine-x.x`, where `x.x` is the MariaDB series (`5.5` or`10.0`). The package is installed, for example on `5.5`, as follows:

```
sudo apt-get install mariadb-tokudb-engine-5.5
```

## libjemalloc

TokuDB requires the libjemalloc library (currently version 3.3.0 or greater).

libjemalloc should automatically be installed when using a package manager, and is loaded by restarting MariaDB.

It can be enabled, if not already done, by adding the following to the my.cnf configuration file:

```
[mysqld_safe]

malloc-lib= /path/to/jemalloc
```

If you don't do the above, you will get an error similar to the following one in your error file

```
2018-11-19 18:46:26 0 [ERROR] mysqld: Can't open shared library '/home/my/maria-10.3/mysql-test/var/plugins/ha_tokudb.so' (errno: 2, /usr/lib64/libjemalloc.so.2: cannot allocate memory in static TLS block)
```

## Check for Transparent HugePage Support on Linux

Transparent hugepages is a feature in newer linux kernel versions that causes\
problems for the memory usage tracking calculations in TokuKV and can lead to\
memory overcommit. If you have this feature enabled, TokuKV will not start, and\
you should turn it off.

You can check the status of Transparent Hugepages as follows:

```
cat /sys/kernel/mm/transparent_hugepage/enabled
```

If the path does not exist, Transparent Hugepages are not enabled and you may continue.

Alternatively, the following are returned:

```
always madvise [never]
```

indicating Transparent Hugepages are not enabled and you may continue. If the following is returned:

```
[always] madvise never
```

Transparent Hugepages are enabled, and you will need to disable them.

To disable them, pass "transparent\_hugepage=never" to the kernel in your bootloader (grub, lilo, etc.). For example, for SUSE, add `transparent_hugepage=never` to Optional Kernel Command Line Parameter at the end, such as after "showopts", and press OK. The setting will take effect on the next reboot.

You can also disable with:

```
echo never > /sys/kernel/mm/transparent_hugepage/enabled
echo never > /sys/kernel/mm/transparent_hugepage/defrag
```

On Centos or RedHat you can do:

Add line `GRUB_CMDLINE_LINUX_DEFAULT="transparent_hugepage=never"` to file /etc/default/grub

Update grub (boot loader):

```
grub2-mkconfig -o /boot/grub2/grub.cfg "$@"
```

For more information, see [disable-transparent-hugepages](https://unix.stackexchange.com/questions/99154/disable-transparent-hugepages)

## Enabling TokuDB

Attempting to enable TokuDB while Linux Transparent HugePages are enabled will fail with an error such as:

```
ERROR 1123 (HY000): Can't initialize function 'TokuDB'; Plugin initialization function failed
```

See the section above; [Check for Transparent HugePage Support on Linux](installing-tokudb.md#check-for-transparent-hugepage-support-on-linux).

The [binary log also needs to be enabled](../../../../server-management/server-monitoring-logs/binary-log/activating-the-binary-log.md) before attempting to enable TokuDB. Strictly speaking, the XA code requires two XA-capable storage engines, and this is checked at startup. In practice, this requires InnoDB and the binary log to be active. If it isn't, the following warning are returned and XA features are disabled:

```
Cannot enable tc-log at run-time. XA features of TokuDB are disabled
```

MariaDB's default `my.cnf` files come with a section for\
TokuDB. To enable TokuDB just remove the '#' comment markers from the options\
in the TokuDB section.

A typical TokuDB section looks like the following:

```
# See https://mariadb.com/kb/en/how-to-enable-tokudb-in-mariadb/
# for instructions how to enable TokuDB
#
# See https://mariadb.com/kb/en/tokudb-differences/ for differences
# between TokuDB in MariaDB and TokuDB from http://www.tokutek.com/

plugin-load=ha_tokudb
```

By default, the `plugin-load` option is commented out. Simply un-comment it\
as in the example above.

Don't forget to also enable jemalloc in the config file.

```
[mysqld_safe]
malloc-lib= /path/to/jemalloc
```

With these changes done, you can restart MariaDB to activate TokuDB.

### Enabling TokuDB on Fedora

Instead of putting the TokuDB section in the main `my.cnf` file, it is\
placed in a separate file located at: `/etc/my.cnf.d/tokudb.cnf`

### Enabling TokuDB on Ubuntu & Debian

Instead of putting the TokuDB section in the main `my.cnf` file, it is\
placed in a separate file located at: `/etc/mysql/conf.d/tokudb.cnf`

### Enabling TokuDB Manually From the mysql Command Line

Generally, it is recommended to use one of the above methods to enable the\
TokuDB storage engine, but it is also possible to enable it manually as with\
other plugins. To do so, launch the mysql command-line client and connect to\
MariaDB as a user with the `SUPER` privilege and execute the following\
command:

```
INSTALL SONAME 'ha_tokudb';
```

TokuDB are installed until someone executes [UNINSTALL SONAME](../../../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md).

### Temporarily Enabling TokuDB When Starting MariaDB

If you just want to test TokuDB, you can start the `mysqld` server with TokuDB with the following command:

```
mysqld --plugin-load=ha_tokudb --plugin-dir=/usr/local/mysql/lib/mysql/plugin
```

## See Also

* [Differences between TokuDB from Tokutek.com and the TokuDB version in MariaDB from MariaDB.org](tokudb-differences.md).
* [TokuDB System and Status Variables](tokudb-system-variables.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
