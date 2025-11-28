# MariaDB Server Docker Official Image Environment Variables

When you start the image, you can adjust the initialization of the MariaDB Server instance by passing one or more environment variables on the docker run command line. Do note that all of the variables below, except `MARIADB_AUTO_UPGRADE`, will have no effect if you start the container with a data directory that already contains a database: any pre-existing database will always be left untouched on container startup.

All tags from `10.6` and above, `MARIADB_*` variables will be used in preference to `MYSQL_*` variables.

One of the following is required: `MARIADB_ROOT_PASSWORD_HASH`, `MARIADB_ROOT_PASSWORD`, `MARIADB_ALLOW_EMPTY_ROOT_PASSWORD`, or `MARIADB_RANDOM_ROOT_PASSWORD` (including `*_FILE` equivalents).

Other environment variables are optional.

### `MARIADB_ROOT_PASSWORD_HASH / MARIADB_ROOT_PASSWORD / MYSQL_ROOT_PASSWORD`

This specifies the password that will be set for the MariaDB root superuser account.

### `MARIADB_ALLOW_EMPTY_ROOT_PASSWORD / MYSQL_ALLOW_EMPTY_PASSWORD`

Set to a non-empty value, like `1`, to allow the container to be started with a blank password for the root user. 

{% hint style="warning" %}
Setting this variable to yes is not recommended unless you really know what you are doing, since this will leave your MariaDB instance completely unprotected, allowing anyone to gain complete superuser access.
{% endhint %}

### `MARIADB_RANDOM_ROOT_PASSWORD / MYSQL_RANDOM_ROOT_PASSWORD`

Define a non-empty value, such as "yes," to auto-generate a random initial password for the root user. The password will be output to stdout, prefixed with "GENERATED ROOT PASSWORD: ...".

### `MARIADB_ROOT_HOST / MYSQL_ROOT_HOST`

`%` is the default hostname part of the root user in MariaDB. This can be changed to any valid hostname. Setting it to `localhost` restricts root access to only the local machine via the Unix socket.

### `MARIADB_DATABASE / MYSQL_DATABASE`

This variable allows you to specify the name of a database to be created on image startup.

### `MARIADB_USER / MYSQL_USER, MARIADB_PASSWORD_HASH / MARIADB_PASSWORD / MYSQL_PASSWORD`

To create a new user with full access permissions in MariaDB, both `user` and `password` variables are required, along with a designated `database`. This new user will be granted comprehensive privileges (`GRANT ALL`) to the specified `MARIADB_DATABASE`. Note that this method should not be utilized for creating the root superuser, as this user is automatically created with the password provided by the `MARIADB_ROOT_PASSWORD` or `MYSQL_ROOT_PASSWORD` variable.

### `MARIADB_MYSQL_LOCALHOST_USER / MARIADB_MYSQL_LOCALHOST_GRANTS`

Set `MARIADB_MYSQL_LOCALHOST_USER` to a non-empty value to create the `mysql@localhost` database user. This user is useful for health checks and backup scripts. The `mysql@localhost` user gets `USAGE` privileges by default. If more access is needed, additional global privileges can be provided as a comma-separated list. Be cautious when sharing a volume containing MariaDB's unix socket (`/var/run/mysqld` by default) as privileges beyond `USAGE` may pose security risks. This user can also be used with `mariadb-backup`. Refer to `healthcheck.sh` for required privileges for each health check test.

### `MARIADB_HEALTHCHECK_GRANTS`

Set `MARIADB_HEALTHCHECK_GRANTS` to the grants required to be given to the `healthcheck@localhost`, `healthcheck@127.0.0.1`, `healthcheck@::1`, users. When not specified the default grant is [USAGE](../../../reference/sql-statements/account-management-sql-statements/grant.md#the-usage-privilege).

The main value used here will be `[REPLICA MONITOR](../../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#replica-monitor) for the [healthcheck --replication](using-healthcheck-sh.md) test.`

### `MARIADB_INITDB_SKIP_TZINFO / MYSQL_INITDB_SKIP_TZINFO`

By default, the entrypoint script automatically loads the timezone data needed for the `CONVERT_TZ()` function. If it is not needed, any non-empty value disables timezone loading.

### `MARIADB_AUTO_UPGRADE / MARIADB_DISABLE_UPGRADE_BACKUP`

Set `MARIADB_AUTO_UPGRADE` to a non-empty value to have the entrypoint check whether [mariadb-upgrade](../../../clients-and-utilities/deployment-tools/mariadb-upgrade.md) needs to run, and if so, run the upgrade before starting the MariaDB server.

Before the upgrade, a backup of the system database is created in the top of the datadir with the name `system_mysql_backup_*.sql.zst`. This backup process can be disabled by setting `MARIADB_DISABLE_UPGRADE_BACKUP` to a non-empty value.

If `MARIADB_AUTO_UPGRADE` is set, and the `.my-healthcheck.cnf` file is missing, the `healthcheck` users are recreated if they don't exist, `MARIADB_HEALTHCHECK_GRANTS` grants are given, the passwords of the `healthcheck` users are reset to a random value and the `.my-healthcheck.cnf` file is recreated with the new password populated.

### `MARIADB_MASTER_HOST`

When specified, the container will connect to this host and replicate from it.

### `MARIADB_REPLICATION_USER / MARIADB_REPLICATION_PASSWORD_HASH / MARIADB_REPLICATION_PASSWORD`

When `MARIADB_MASTER_HOST` is defined, `MARIADB_REPLICATION_USER` and `MARIADB_REPLICATION_PASSWORD` will be used to connect to the master. When not specified, the `MARIADB_REPLICATION_USER` will be created with the `REPLICATION REPLICA` grants needed for a client to initiate replication.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
