---
description: >-
  A guide to installing MariaDB from pre-compiled binary tarballs on Linux,
  allowing for flexible installation paths and multiple versions.
---

# Installing MariaDB Binary Tarballs

Binary tarballs (bintars) are compressed tar archives that contain pre-compiled executables, libraries, and other deployment dependencies. They can usually be installed on any modern Linux distribution.

MariaDB Binary tarballs are named following the pattern: `mariadb-VERSION-OS.tar.gz`. Be sure to [download](https://mariadb.org/download) the correct version for your machine.

{% hint style="warning" %}
Some older binary tarballs are marked _'(GLIBC\_2.14)'_ or _'(requires GLIBC\_2.14+)'_. These binaries are built the same as the others, but on a newer build host, and they require GLIBC 2.14 or higher. Use the other binaries for machines with older versions of GLIBC installed. Run `ldd --version` to see which version is running on your distribution.\
Others are marked `systemd`, which are for systems with `systemd` and GLIBC 2.19 or higher.
{% endhint %}

### Benefits of Binary Tarballs

Binary tarballs provide multiple benefits:

* They are highly OS independent. As long as you get the `bintar` for the architecture, GLIBC version, and if you are using `systemd` or not, the `bintar` should work almost anywhere.
* You do not need to be root to use them.
  * They can be installed by anyone to any path, including one's home directory.
* You can have [any number of different MariaDB installations](../../../starting-and-stopping-mariadb/running-multiple-mariadb-server-processes.md) on the same machine. This is often desired during upgrades when one wants to have the old installation running until switching to the new one.
* You can use them on systems for which MariaDB does not support native packages.

### Installing binary tarballs

To install the [binaries](https://downloads.mariadb.org), unpack the distribution into the directory of your choice and run the [mariadb-install-db](../installing-system-tables-mariadb-install-db/) script.

In the example below, we install MariaDB in the `/usr/local/mysql` directory (this is the default location for MariaDB for many platforms). However, any other directory should work too.

We install the binary with a symlink to the original name. This is done so that you can easily change MariaDB versions just by moving the symlink to point to another directory.

### Ensure You Use the Correct my.cnf Files

MariaDB searches for the configuration files '`/etc/my.cnf`' (on some systems '`/etc/mysql/my.cnf`') and '`~/.my.cnf`'. If you have an old `my.cnf` file (maybe from a system installation of MariaDB or MySQL), you need to take care that you don't accidentally use the old one with your new binary .tar installation.

The normal solution for this is to ignore the `my.cnf` file in `/etc` when you use the programs in the tar file.

This is done by [creating your own .my.cnf file](../../configuring-mariadb/configuring-mariadb-with-option-files.md) in your home directory and telling [mariadb-install-db](../../../../clients-and-utilities/deployment-tools/mariadb-install-db.md),[mysqld\_safe](../../../../clients-and-utilities/legacy-clients-and-utilities/mariadbd_safe.md), and possibly [mariadb (the command-line client utility)](../../../../clients-and-utilities/mariadb-client/) to **only** use this one with the option '`--defaults-file=~/.my.cnf`'. Note that this has to be the first option for the above commands!

### Installing MariaDB as root in /usr/local/mysql

If you have root access to the system, you probably want to install MariaDB under the user and group 'mysql' (to keep compatibility with MySQL installations):

```bash
groupadd mysql
useradd -g mysql mysql
cd /usr/local
tar -zxvpf /path-to/mariadb-VERSION-OS.tar.gz
ln -s mariadb-VERSION-OS mysql
cd mysql
./scripts/mariadb-install-db --user=mysql
chown -R root .
chown -R mysql data
```

The symlinking with `ln -s` is recommended as it makes it easy to install many MariaDB versions at the same time (for easy testing, upgrading, downgrading, etc).

If you are installing MariaDB to replace MySQL, then you can leave out the call to `mariadb-install-db`. Instead, shut down MySQL. MariaDB should find the path to the data directory from your old `/etc/my.cnf` file (path may vary depending on your system).

To start mariadbd, you should now do:

```bash
./bin/mariadbd-safe --user=mysql &
or
./bin/mariadbd-safe --defaults-file=~/.my.cnf --user=mysql &
```

To test the connection, modify your $PATH so you can invoke clients such as [mariadb](../../../../clients-and-utilities/mariadb-client/), [mariadb-dump](../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md), etc.

```bash
export PATH=$PATH:/usr/local/mysql/bin/
```

You may want to modify your .bashrc or .bash\_profile to make it permanent.

### Installing MariaDB as Not root in Any Directory

Below, change /usr/local to the directory of your choice.

```bash
cd /usr/local
gunzip < /path-to/mariadb-VERSION-OS.tar.gz | tar xf -
ln -s mariadb-VERSION-OS mysql
cd mysql
./scripts/mariadb-install-db --defaults-file=~/.my.cnf
```

If you have problems with the above gunzip command line, you can instead, if you have gnu tar, do:

```bash
tar xfz /path-to/mariadb-VERSION-OS.tar.gz
```

To start mariadbd, you should now do:

```bash
./bin/mariadbd-safe --defaults-file=~/.my.cnf &
```

### Auto Start of mariadbd

You can get mariadbd (the MariaDB server) to autostart by copying the file `mysql.server` file to the right place.

```bash
cp support-files/mysql.server /etc/init.d/mysql.server
```

The exact place depends on your system. The `mysql.server` file contains instructions on how to use and fine tune it.

For systemd installation, the mariadb.service file will need to be copied from the `support-files/systemd` folder to the `/usr/lib/systemd/system/` folder.

```bash
cp support-files/systemd/mariadb.service /usr/lib/systemd/system/mariadb.service
```

Note that, by default, the `/usr/` directory is write protected by systemd, though, so when having the data directory in `/usr/local/mysql/data` as per the instructions above, you also need to make that directory writable. You can do so by adding an extra service include file:

```bash
mkdir /etc/systemd/system/mariadb.service.d/

cat > /etc/systemd/system/mariadb.service.d/datadir.conf <<EOF
[Service]
ReadWritePaths=/usr/local/mysql/data
EOF

systemctl daemon-reload
```

After this, you can start the service using this command:

```bash
systemctl start mariadb.service
```

Stop the service with this command:

```bash
systemctl stop mariadb.service
```

Please refer to the [systemd](../../../starting-and-stopping-mariadb/systemd.md) page for further information.

### Post Installation

After this, remember to set proper passwords for all accounts accessible from untrusted sources, to avoid exposing the host to security risks!

Also consider using the [mysql.server](../../../starting-and-stopping-mariadb/mysql-server.md) to [start MariaDB automatically](../../../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md) when your system boots.

On systems using systemd, instead, enable automatic startup during system boot with this command:

```bash
systemctl enable mariadb.service
```

For details on the exact steps used to build the binaries, see the [compiling MariaDB section](../compiling-mariadb-from-source/).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
