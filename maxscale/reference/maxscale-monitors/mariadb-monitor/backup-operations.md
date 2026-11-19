---
description: >-
  How MariaDB Monitor rebuilds servers, creates backups, and restores them
  with mariadb-backup over SSH, and the prerequisites for these operations.
---

# MaxScale MariaDB Monitor Backup Operations

MariaDB Monitor can rebuild a server and create and restore backups. This page describes these operations and what they need.

Backup operations manipulate the contents of a MariaDB Server, saving it or
overwriting it. MariaDB-Monitor supports three backup operations:

1. `rebuild-server`: Replace the contents of a database server with the
   contents of another. Launched with the `async-rebuild-server` command.
2. `create-backup`: Copy the contents of a database server to a storage
   location. Launched with the `async-create-backup` command.
3. `restore-from-backup`: Overwrite the contents of a database server with a
   backup. Launched with the `async-restore-from-backup` command.

These operations do not modify server config files, only files in the data
directory (typically _/var/lib/mysql_) are affected.

All of these operations are monitor commands and best launched with MaxCtrl.
The operations are asynchronous, which means MaxCtrl won't wait for the
operation to complete and instead immediately returns "OK". To see the current
status of an operation, either check MaxScale log or use the
fetch-cmd-result-command
(e.g. `maxctrl call command mariadbmon fetch-cmd-result MyMonitor`).

Because these operations are always run asynchronously, the MaxCtrl command name
is prefixed with `async-` (for example, `async-rebuild-server`). The unprefixed
name (for example, `rebuild-server`) is the operation's name as it appears in
the MaxScale log and in `fetch-cmd-result` output; it is not a separate command
you can run.

To perform backup operations, MaxScale requires ssh-access on all affected
machines. The _ssh\_user_ and _ssh\_keyfile_-settings define the SSH credentials
MaxScale uses to access the servers. MaxScale must be able to run commands with
_sudo_ on both the source and target servers. See [settings](README.md#settings) and
[sudoers.d configuration](#sudoers.d-configuration) below
for more information.

The following tools need to be installed on the backends:

1. mariadb-backup. Backs up and restores MariaDB Server contents. Installed e.g.
   with `yum install MariaDB-backup`. See
   [mariadb-backup documentation](../../../../server/server-usage/backup-and-restore/mariadb-backup)
   for more information.
2. pigz. Compresses and decompresses the backup stream. Installed e.g. with`yum install pigz`.
3. socat. Streams data from one machine to another. Is likely already
   installed. If not, can be installed e.g. with `yum install socat`.

mariadb-backup needs server credentials to log in and authenticate to the
MariaDB Server being copied from. For this, MaxScale uses the monitor user.
The monitor user may thus require additional privileges. See
[mariadb-backup documentation](../../../../server/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview.md#authentication-and-privileges)
for more details.

## Rebuild server

The rebuild server-operation replaces the contents of a database server with the
contents of another server. The source server is effectively cloned and all data
on the target server is lost. This is useful when a replica server has diverged
from the primary server, or when adding a new server to the cluster.
MaxScale performs this operation by running mariadb-backup on both the
source and target servers.

Run this operation with the `async-rebuild-server` command. In the MaxScale log
and in `fetch-cmd-result` output it is referred to by its operation name,
`rebuild-server`.

### Prerequisites

**Verify SSH Connectivity**

The async rebuild server operation requires SSH to be correctly configured
between the MaxScale host and all the database servers. Before starting a
rebuild operation, it is important to ensure that MaxScale can interact with the
database servers over SSH without generating any unwanted or additional output
during login or logout. The rebuild process may encounter a non-specific issue
or fail without a descriptive error message due to interference from shell
configuration files (such as `.bashrc`, `.profile`, etc.) on the database
servers that print text during login.

Hence, before using the async rebuild server feature, verify that SSH output is
clean by running the following command on the MaxScale host:

```
ssh -i /home/maxscale/.ssh/<private_key_filename> root@<db_host_ip> hostname
```

The output must contain only the hostname of the database server without any
additional text, lines, or errors. Example of correct output:

```
dbserver01
```

If any additional text or unwanted output appears in the output (from `.bashrc`,
`/etc/profile`, or any custom login scripts), the async rebuild server operation
may fail without providing a clear descriptive error message.

**Verify Backup User Privileges**

The MariaDB monitor user (specified by `user` and `password` parameters) must
have sufficient privileges to run `mariadb-backup` command locally on both the
source and target database nodes via SSH before starting the rebuild operation.

Before launching the operation, run the following command to verify that the
monitor user can perform a backup manually on the database server:

```
/usr/bin/mariabackup \
  --user=<monitor_user> \
  --password=<password> \
  --backup \
  --safe-slave-backup \
  --target-dir=<backup_directory>
```

The command should run without errors and create a backup in the specified
directory.

In the event the command fails with authentication errors, you may need to grant
privileges for `mariadbmon`@`%` and `mariadbmon`@`localhost`, as the backup
command may connect locally. For example:

```
-- For remote connections
GRANT RELOAD, PROCESS, FILE, SHOW DATABASES, SUPER, BINLOG MONITOR, EVENT, CONNECTION ADMIN, SLAVE MONITOR, REPLICATION MASTER ADMIN, REPLICATION SLAVE ADMIN ON *.* TO 'mariadbmon'@'%' IDENTIFIED BY 'password';

-- For local connections during backup
GRANT RELOAD, PROCESS, LOCK TABLES, BINLOG MONITOR ON *.* TO 'mariadbmon'@'localhost' IDENTIFIED BY 'password';
```

Once the privileges are granted, you can run the test command again to verify it
works properly.

### Rebuild Operation Steps

When launched, the rebuild operation proceeds as below. If any step fails, the
operation is stopped and the target server will be left in an unspecified state.

1. Log in to both servers with ssh and check that the tools listed above are
   present (e.g. `mariadb-backup -v` should succeed).
2. Check that the port used for transferring the backup is free on the source
   server. If not, kill the process holding it. This requires running `lsof` and
   `kill`.
3. Test the connection by streaming a short message from the source host to the
   target.
4. Launch `mariadb-backup` on the source machine, compress the stream and listen
   for an incoming connection. This is performed with the following command:
   `mariadb-backup --backup --safe-slave-backup --stream=xbstream --parallel=1 | pigz -c | socat - TCP-LISTEN:<port>`
   **Note**: MaxScale uses the `user` and `password` parameters specified in the
   monitor configuration to authenticate to MariaDB. Before initiating the async
   rebuild server process, ensure this user has the sufficient privileges on
   both the source and target servers. See
   the [Verify Backup User Privileges](backup-operations.md#prerequisites) section
   for details and example grant statements.
5. Ask the target server what its data directory is (`select @@datadir;`). Stop
   MariaDB Server on the target machine and delete all contents of the data
   directory.
6. On the target machine, connect to the source machine, read the backup stream,
   decompress it and write to the data directory. This is performed with a command
   like `socat -u TCP:<host>:<port> STDOUT | pigz -dc | mbstream -x`. This step can
   take a long time if there is much data to transfer.
7. Check that the data directory on the target machine is not empty,
   i.e. that the transfer at least appears to have succeeded.
8. Prepare the backup on the target server with a command like:
   `mariadb-backup --use-memory=1G --prepare`. This step can also take some time
   if the source server performs writes during data transfer.
9. On the target server, change ownership of datadir contents to the
   mysql-user and start MariaDB-server.
10. Read `gtid` from the data directory. Have the target server start replicating
    from the primary if it is not one already.

The rebuild-operation is a monitor module command and takes four arguments:

1. Monitor name, e.g. MyMonitor.
2. Target server name, e.g. MyTargetServer.
3. Source server name, e.g. MySourceServer. This parameter is optional.
   If not specified, the monitor prefers to autoselect an up-to-date replica
   server to avoid increasing load on the primary server. Due to the`--safe-slave-backup`-option, the replica will stop
   replicating until the backup data has been transferred.
4. Data directory on target server. This parameter is optional. If not
   specified, the monitor will ask the target server. If the target server is
   not running, the monitor will assume /var/lib/mysql. Thus, this only needs to be
   defined with non-standard directory setups.

The following example rebuilds MyTargetServer with contents of MySourceServer.

```
maxctrl call command mariadbmon async-rebuild-server MyMonitor MyTargetServer MySourceServer
```

The following example uses a custom data directory on the target.

```
maxctrl call command mariadbmon async-rebuild-server MyMonitor MyTargetServer MySourceServer /my_datadir
```

The operation does not launch if the target server is already replicating or if
the source server is not a primary or replica.

Steps 6 and 8 can take a long time depending on the size of the database and if
writes are ongoing. During these steps, the monitor will continue monitoring the
cluster normally. After each monitor tick the monitor checks if the
rebuild-operation can proceed. No other monitor operations, either manual or
automatic, can run until the rebuild completes.

### Rebuild server with key-value arguments

In addition to traditional argument passing, rebuild-server supports
key-value arguments. The supported arguments are:

| argument | type    | default            | description                       |
|----------|---------|--------------------|-----------------------------------|
| monitor  | monitor | none (mandatory)   | Monitor name                      |
| target   | server  | none (mandatory)   | Which server to rebuild           |
| source   | server  | empty (autoselect) | Which server to copy data from    |
| datadir  | string  | empty (autodetect) | Data directory on target server   |
| dry_run  | boolean | false              | If true, only check preconditions |

The *dry_run*-argument causes the monitor to only check if preconditions for
rebuild are met on the source and target servers. It checks that SSH-
connections can be established and that required tools are present on the
servers. No permanent changes are done.

The following example checks if MyServer1 can be rebuilt from the contents
of MyServer2.
```
$ maxctrl call command mariadbmon async-rebuild-server monitor=MyMonitor target=MyServer1 source=MyServer2 dry_run=true
OK
$ maxctrl call command mariadbmon fetch-cmd-result MyMonitor
"rebuild-server completed successfully."
```

## Create backup

The create backup-operation copies the contents of a database server to the
backup storage. The source server is not modified but may slow down during
backup creation. MaxScale performs this operation by running
mariadb-backup on both the source and storage servers. The storage location is
defined by the _backup\_storage\_address_ and _backup\_storage\_path_ settings.
Normal ssh-settings are used to access the storage server. The backup storage
machine does not need to have a MariaDB Server installed.

Run this operation with the `async-create-backup` command. In the MaxScale log
and in `fetch-cmd-result` output it is referred to by its operation name,
`create-backup`.

Backup creation runs somewhat similar to rebuild-server. The main difference
is that the backup data is simply saved to a directory and not prepared or
used to start a MariaDB Server. If any step fails, the operation is stopped
and the backup storage directory will be left in an unspecified state.

1. Init. See rebuild-server.
2. Check listen port on the backup storage machine. See rebuild-server.
3. Check that the backup storage main directory exists. Check that it does not
   contain a backup with the same name as the one being created. Create the final
   backup directory.
4. Test the connection by streaming a short message from the source host to the
   backup storage.
5. Serve backup on source. Similar to rebuild-server step 4.
6. Transfer backup directly to the final storage directory. Similar to
   rebuild-server step 5.
7. Check that the copied backup data looks ok.

Backup creation is a monitor module command and takes three
arguments: the monitor name, source server name and backup name. Backup name
defines the subdirectory where the backup is saved and should be a valid
directory name. The command

```
maxctrl call command mariadbmon async-create-backup MyMonitor MySourceServer wednesday_161122
```

would save the backup of MySourceServer to
`<backup_storage_path>/wednesday_161122` on the host defined in
_backup\_storage\_address_. _ssh\_user_ needs to have read and write access
to the main storage directory. The source server must be a primary or replica.

Similar to rebuild-server, the monitor will continue monitoring the servers
while the backup is transferred.

### Create backup with key-value arguments

In addition to traditional argument passing, create-backup supports
key-value arguments. The supported arguments are:

| argument | type    | default          | description                       |
|----------|---------|------------------|-----------------------------------|
| monitor  | monitor | none (mandatory) | Monitor name                      |
| source   | server  | none (mandatory) | Which server to copy data from    |
| bu_name  | string  | none (mandatory) | Backup name                       |
| dry_run  | boolean | false            | If true, only check preconditions |

The *dry_run*-argument causes the monitor to only check if preconditions for
backup creation are met on the source server and backup storage. It checks
that SSH-connections can be established and that required tools are present.
The backup storage must also not yet have a backup with the given name.
No permanent changes are done.

The following example checks that MyServer1 can be backed up.
```
$ maxctrl call command mariadbmon async-create-backup monitor=MyMonitor source=MyServer1 bu_name=mybackup2 dry_run=true
OK
$ maxctrl call command mariadbmon fetch-cmd-result MyMonitor
"create-backup completed successfully."
```

## Restore from backup

The restore-operation is the reverse of create-backup. It overwrites the
contents of an existing MariaDB Server with a backup from the backup storage.
The backup is not removed and can be used again. MaxScale performs this
operation by transferring the backup contents as a tar archive and overwriting
the target server data directory. The backup storage is defined in monitor
settings similar to create-backup.

Run this operation with the `async-restore-from-backup` command. In the MaxScale
log and in `fetch-cmd-result` output it is referred to by its operation name,
`restore-from-backup`.

The restore-operation runs somewhat similar to rebuild-server. The main
difference is that the backup data is copied with _tar_ instead of mariadb-backup.
If any step fails, the operation is stopped and the target server will be
left in an unspecified state.

1. Init. See rebuild-server.
2. Check listen port on the target machine. See rebuild-server.
3. Check that the backup storage main directory exists and that it contains
   a backup with the name requested.
4. Test the connection by streaming a short message from the backup storage to
   the target machine.
5. On the backup storage machine, compress the backup with tar and serve it
   with socat, listening for an incoming connection. This is performed with
   a command like `tar -zc -C <backup_dir> . | socat - TCP-LISTEN:<port>`.
6. Ask the target server what its data directory is (`select @@datadir;`). Stop
   MariaDB Server on the target machine and delete all contents of the data
   directory.
7. On the target machine, connect to the source machine, read the backup stream,
   decompress it and write to the data directory. This is performed with a command
   like `socat -u TCP:<host>:<port> STDOUT | sudo tar -xz -C /var/lib/mysql/`.
   This step can take a long time if there is much data to transfer.
8. From here on, the operation proceeds as from rebuild-server step 7.

Server restoration is a monitor module command and takes four arguments.

1. Monitor name, e.g. MyMonitor.
2. Target server name, e.g. MyNewServer.
3. Backup name. This parameter defines the subdirectory where the backup is
   read from and should be an existing directory on the backup storage host.
4. Data directory on target server. This parameter is optional. If not
   specified, the monitor will ask the target server. If the target server is
   not running, the monitor will assume /var/lib/mysql. Thus, this only needs to be
   defined with non-standard directory setups.

The command

```
maxctrl call command mariadbmon async-restore-from-backup MyMonitor MyTargetServer wednesday_161122
```

would erase the contents of MyTargetServer and replace them with the backup
contained in
`<backup_storage_path>/wednesday_161122` on the host defined in
_backup\_storage\_address_. _ssh\_user_ needs to have read access
to the main storage directory and the backup. The target server must not be
a primary or replica.

The following example uses a custom data directory on the target.

```
maxctrl call command mariadbmon async-restore-from-backup MyMonitor MyTargetServer wednesday_161122 /my_datadir
```

Similar to rebuild-server, the monitor will continue monitoring the servers
while the backup is transferred and prepared.

### Restore from backup with key-value arguments

In addition to traditional argument passing, restore-from-backup supports
key-value arguments. The supported arguments are:

| argument | type    | default            | description                       |
|----------|---------|--------------------|-----------------------------------|
| monitor  | monitor | none (mandatory)   | Monitor name                      |
| target   | server  | none (mandatory)   | Which server to rebuild           |
| bu_name  | string  | none (mandatory)   | Backup name                       |
| datadir  | string  | empty (autodetect) | Data directory on target server   |
| dry_run  | boolean | false              | If true, only check preconditions |

The *dry_run*-argument causes the monitor to only check if preconditions for
restore are met on the target server and backup storage. It checks
that SSH-connections can be established and that required tools are present.
The backup storage must also have a backup with the given name. No permanent
changes are done.

The following example checks if MyServer1 can be restored.
```
$ maxctrl call command mariadbmon async-restore-from-backup monitor=MyMonitor target=MyServer2 bu_name=mybackup2 dry_run=true
OK
$ maxctrl call command mariadbmon fetch-cmd-result MyMonitor
"restore-from-backup completed successfully."
```
call command mariadbmon async-create-backup monitor=MariaDB-Monitor source=server1 dry_run=true bu_name=bu1

## List backups

The *list-backups* command lists currently available backups in the backup
storage.
```
$ maxctrl call command mariadbmon list-backups monitor=MariaDB-Monitor
{
    "backups": [
        "bu1",
        "bu2",
        "bu3"
    ]
}
```

## Settings for Backup operations

The following settings control this feature:

* [`ssh_user`](mariadb-monitor-settings.md#ssh_user)
* [`ssh_keyfile`](mariadb-monitor-settings.md#ssh_keyfile)
* [`ssh_check_host_key`](mariadb-monitor-settings.md#ssh_check_host_key)
* [`ssh_timeout`](mariadb-monitor-settings.md#ssh_timeout)
* [`ssh_port`](mariadb-monitor-settings.md#ssh_port)
* [`rebuild_port`](mariadb-monitor-settings.md#rebuild_port)
* [`mariadb_backup_use_memory`](mariadb-monitor-settings.md#mariadb_backup_use_memory)
* [`mariadb_backup_parallel`](mariadb-monitor-settings.md#mariadb_backup_parallel)
* [`backup_storage_address`](mariadb-monitor-settings.md#backup_storage_address)
* [`backup_storage_path`](mariadb-monitor-settings.md#backup_storage_path)

## sudoers.d configuration

If giving MaxScale general sudo-access is out of the question, MaxScale must be
allowed to run the specific commands required by the backup operations. This can
be achieved by creating a file with the commands in the`/etc/sudoers.d`
-directory. In the example below, the user _johnny_ is given the power to run
commands as root. The contents of the file may need to be tweaked due to changes
in install locations.

```
johnny ALL= NOPASSWD: /bin/systemctl stop mariadb
johnny ALL= NOPASSWD: /bin/systemctl start mariadb
johnny ALL= NOPASSWD: /usr/sbin/lsof
johnny ALL= NOPASSWD: /bin/kill
johnny ALL= NOPASSWD: /bin/du
johnny ALL= NOPASSWD: /usr/bin/mariabackup
johnny ALL= NOPASSWD: /usr/bin/mariadb-backup
johnny ALL= NOPASSWD: /bin/mbstream
johnny ALL= NOPASSWD: /bin/rm -rf /var/lib/mysql/*
johnny ALL= NOPASSWD: /bin/chown -R mysql\:mysql /var/lib/mysql
johnny ALL= NOPASSWD: /bin/cat /var/lib/mysql/xtrabackup_binlog_info
johnny ALL= NOPASSWD: /bin/cat /var/lib/mysql/mariadb_backup_binlog_info
johnny ALL= NOPASSWD: /bin/tar -xz -C /var/lib/mysql/
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
