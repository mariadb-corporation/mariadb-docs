# Container Backup and Restoration

MariaDB databases in containers need backup and restore like their non-container equivalents.

## Logical Backups

In this section, we will assume that the MariaDB container has been created as follows:

```bash
$ docker volume create mariadb_data
$ docker volume create mariadb_backup
$ docker run --rm \
  -v mariadb_data:/var/lib/mysql \
  -v mariadb_backup:/backup \
  mariadb \
  chown -R mysql:mysql /var/lib/mysql /backup
$ docker run -d --name mariadb \
  -v mariadb_data:/var/lib/mysql \
  -v mariadb_backup:/backup \
  -e MARIADB_ROOT_PASSWORD='MariaDB11!' \
  <mariadb-image>
```

### Backup

[mariadb-dump](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) is in the Docker Official Image and can be used as follows:

```bash
$ docker exec mariadb \
  sh -c 'mariadb-dump --all-databases -u root -p"$MARIADB_ROOT_PASSWORD" > backup/db.sql'
```

### Restoring Data from Dump Files

For restoring data, you can use the following `docker exec` command:

```bash
$ docker exec mariadb \
  sh -c 'mariadb -u root -p"$MARIADB_ROOT_PASSWORD" < backup/db.sql'
```

## Physical Backups

[mariadb-backup](../../../server-usage/backup-and-restore/mariadb-backup/) is in the Docker Official Image.

### Backup

mariadb-backup can create a backup as follows:

To perform a backup using [mariadb-backup](../../../server-usage/backup-and-restore/mariadb-backup/), a second container is started that shares the original container's data directory. An additional volume for the backup needs to be included in the second backup instance. Authentication against the MariaDB database instance is required to successfully complete the backup. In the example below, a `mysql@localhost` user is used with the MariaDB server's Unix socket shared with the backup container.

Note: Privileges listed here are for 10.5+. For an exact list, see [mariadb-backup: Authentication and Privileges](../../../server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview.md#authentication-and-privileges).

```bash
$ docker volume create mariadb_data
$ docker volume create mariadb_backup
$ docker run --rm \
  -v mariadb_data:/var/lib/mysql \
  -v mariadb_backup:/backup \
  mariadb \
  chown -R mysql:mysql /var/lib/mysql /backup
$ docker run -d --name mariadb \
  -v mariadb_data:/var/lib/mysql \
  -v mariadb_backup:/backup \
  -e MARIADB_ROOT_PASSWORD='MariaDB11!' \
  -e MARIADB_MYSQL_LOCALHOST_USER=1 \
  -e MARIADB_MYSQL_LOCALHOST_GRANTS='RELOAD, PROCESS, LOCK TABLES, BINLOG MONITOR' \
  <mariadb-image>
```

mariadb-backup will run as the `mysql` user in the container, so the permissions on `/backup` will need to ensure that it can be written to by this user:

```bash
$ docker exec --user mysql mariadb mariadb-backup --backup --target-dir=backup
```

### Restore

These steps restore the backup made with mariadb-backup.

At some point before doing the restore, the backup needs to be prepared. The prepare must be done with the same MariaDB version that performed the backup. Perform the prepare like this:

```bash
$ docker run --rm \
  --name mariadb-restore \
  -v mariadb_backup:/backup \
  <mariadb-image> \
  mariadb-backup --prepare --target-dir=backup
```

Now that the image is prepared, start the container with both the data and the backup volumes and restore the backup. The data directory must be empty to perform this action:

```bash
$ docker volume create mariadb_restore
$ docker run --rm \
   -v mariadb_restore:/var/lib/mysql \
   --name mariadb-restore-change-permissions \
  <mariadb-image> \
  chown mysql: /var/lib/mysql
$ docker run --rm \
  --name mariadb-restore \
  -v mariadb_restore:/var/lib/mysql \
  -v mariadb_backup:/backup \
  --user mysql \
  <mariadb-image> \
  mariadb-backup --copy-back --target-dir=backup
```

With `mariadb_restore` volume containing the restored backup, start normally as this is an initialized data directory. At this point a later version of `<mariadb-image>` container can be used:

```bash
$ docker run -d --name mariadb \
  -v mariadb_restore:/var/lib/mysql \
  -e MARIADB_AUTO_UPGRADE=1 \
  -e MARIADB_ROOT_PASSWORD='MariaDB11!' \
  <mariadb-image>
```

On the environment variables here:

* [MARIADB\_AUTO\_UPGRADE](mariadb-server-docker-official-image-environment-variables.md#mariadb_auto_upgrade-mariadb_disable_upgrade_backup) here in addition to upgrading the system tables ensures there is a [healthcheck user](using-healthcheck-sh.md).
* `MARIADB_ROOT_PASSWORD` is a convenience if any scripts, like logical backup above, use the environment variable. This environment variable is not strictly required.

For further information on mariadb-backup, see [mariadb-backup Overview](../../../server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
