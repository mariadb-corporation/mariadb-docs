---
description: >-
  Complete guide to MariaDB in Docker. Complete resource for container
  deployment, volume management, networking, and environment setup for
  production use.
---

# MariaDB Enterprise Server Docker Official Image Environment Variables

When you start the image, you can adjust the initialization of the MariaDB Server instance by passing one or more environment variables on the docker run command line. Do note that all of the variables below, except `MARIADB_AUTO_UPGRADE`, will have no effect if you start the container with a data directory that already contains a database: any pre-existing database will always be left untouched on container startup.

All tags from `10.6` and above, `MARIADB_*` variables will be used in preference to `MYSQL_*` variables.

One of the following is required: `MARIADB_ROOT_PASSWORD_HASH`, `MARIADB_ROOT_PASSWORD`, `MARIADB_ALLOW_EMPTY_ROOT_PASSWORD`, or `MARIADB_RANDOM_ROOT_PASSWORD` (including `*_FILE` equivalents).

Other environment variables are optional.

## Environment Variables

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

### `MARIADB_USER_HOST`

`%` is the default hostname part of the user created through `MYSQL_USER / MARIADB_USER` in MariaDB. This can be changed to any valid hostname or IP. Setting it to `localhost` restricts user access to only the local machine via the Unix socket.

### `MARIADB_DATABASE / MYSQL_DATABASE`

This variable allows you to specify the name of a database to be created on image startup.

### `MARIADB_USER / MYSQL_USER, MARIADB_PASSWORD_HASH / MARIADB_PASSWORD / MYSQL_PASSWORD`

To create a new user with full access permissions in MariaDB, both `user` and `password` variables are required, along with a designated `database`. This new user will be granted comprehensive privileges (`GRANT ALL`) to the specified `MARIADB_DATABASE`. Note that this method should not be utilized for creating the root superuser, as this user is automatically created with the password provided by the `MARIADB_ROOT_PASSWORD` or `MYSQL_ROOT_PASSWORD` variable.

### `MARIADB_MYSQL_LOCALHOST_USER / MARIADB_MYSQL_LOCALHOST_GRANTS`

Set `MARIADB_MYSQL_LOCALHOST_USER` to a non-empty value to create the `mysql@localhost` database user. This user is useful for health checks and backup scripts. The `mysql@localhost` user gets `USAGE` privileges by default. If more access is needed, additional global privileges can be provided as a comma-separated list. Be cautious when sharing a volume containing MariaDB's unix socket (`/var/run/mysqld` by default) as privileges beyond `USAGE` may pose security risks. This user can also be used with `mariadb-backup`. Refer to `healthcheck.sh` for required privileges for each health check test.

### `MARIADB_HEALTHCHECK_GRANTS`

Set `MARIADB_HEALTHCHECK_GRANTS` to the grants required to be given to the `healthcheck@localhost`, `healthcheck@127.0.0.1`, `healthcheck@::1`, users. When not specified the default grant is [USAGE](../../../reference/sql-statements/account-management-sql-statements/grant.md#the-usage-privilege).

The main value used here will be `[REPLICA MONITOR](../../../reference/sql-statements/account-management-sql-statements/grant.md#replica-monitor)` for the `[healthcheck --replication](using-healthcheck-sh.md)` test.

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

## Timezone Configuration

By default, the container operates in the Coordinated Universal Time (UTC) timezone. To configure a specific timezone for the container's operating system and internal processes, utilize the `TZ` environment variable.

### Supported Values

The `TZ` variable accepts standard tz database (IANA) timezone identifiers. Examples include `America/New_York`, `Europe/London`, or `Asia/Tokyo`.

### Usage Examples

**Using `docker run`**

You can specify the timezone when starting the container via the command line interface using the `-e` flag:

```bash
docker run -d \
  --name database-container \
  -e TZ="America/New_York" \
  -e MARIADB_ROOT_PASSWORD="your_strong_password" \
  docker.mariadb.com/enterprise-server:11.8
```

**Using `docker-compose.yml`**

For deployments managed by Docker Compose, declare the `TZ` variable within the `environment` mapping of your service definition:

```yaml
services:
  db:
    image: docker.mariadb.com/enterprise-server:11.8
    environment:
      - TZ=America/New_York
      - MARIADB_ROOT_PASSWORD=your_strong_password
```

## Using `_FILE` Environment Variables for Secrets

When running Docker containers, it is a security best practice to avoid passing sensitive information, like database passwords, directly as plain-text environment variables. The MariaDB container images allow you to securely read secrets from mounted files by appending `_FILE` to the standard environment variable name. 

### List of supported `_FILE` Environment Variables

| Name | Description |
| --- | --- |
| `MYSQL_ROOT_HOST_FILE` | Path to a file containing the host from which the root user is allowed to connect. |
| `MARIADB_ROOT_HOST_FILE` | Path to a file containing the host from which the root user is allowed to connect. |
| `MYSQL_DATABASE_FILE` | Path to a file containing the name of a database to be created on initialization. |
| `MARIADB_DATABASE_FILE` | Path to a file containing the name of a database to be created on initialization. |
| `MYSQL_USER_FILE` | Path to a file containing the username for a new user to be created on initialization. |
| `MARIADB_USER_FILE` | Path to a file containing the username for a new user to be created on initialization. |
| `MYSQL_PASSWORD_FILE` | Path to a file containing the password for the user defined by `MYSQL_USER`. |
| `MARIADB_PASSWORD_FILE` | Path to a file containing the password for the user defined by `MARIADB_USER`. |
| `MYSQL_ROOT_PASSWORD_FILE` | Path to a file containing the password for the root database user. |
| `MARIADB_ROOT_PASSWORD_FILE` | Path to a file containing the password for the root database user. |
| `MARIADB_PASSWORD_HASH_FILE` | Path to a file containing the hashed password for the created standard user. |
| `MARIADB_ROOT_PASSWORD_HASH_FILE` | Path to a file containing the hashed password for the root database user. |
| `MARIADB_UNIX_SOCKET_AUTHENTICATION_FILE` | Path to a file containing a value to enable/disable Unix socket authentication. |
| `MARIADB_REPLICATION_USER_FILE` | Path to a file containing the username to be used for setting up replication. |
| `MARIADB_REPLICATION_PASSWORD_FILE` | Path to a file containing the password for the replication user. |
| `MARIADB_REPLICATION_PASSWORD_HASH_FILE` | Path to a file containing the hashed password for the replication user. |
| `MARIADB_MASTER_HOST_FILE` | Path to a file containing the hostname or IP address of the replication master. |
| `MARIADB_MASTER_PORT_FILE` | Path to a file containing the port number of the replication master. |

### Example

Here is how to set up your MariaDB root password using the `MARIADB_ROOT_PASSWORD_FILE` environment variable.

#### Step 1: Create the Secret File

First, create a local file on your host machine that contains your desired environment variable. In this example, we will create a file named `mariadb_root_password_secret` containing the password `MariaDB11!`.

```bash
echo -n "MariaDB11!" > mariadb_root_password_secret
```

{% hint style="tip" %}
Using the `-n` flag with `echo` is highly recommended, as it ensures no hidden newline characters are accidentally appended to your password!
{% endhint %}

#### Step 2: Start the MariaDB Container

Next, run the container. You need to mount the local secret file into the container and set the environment variable to point to that newly mounted path.

```bash
docker run -d \
  -v "$(pwd)/mariadb_root_password_secret:/run/secrets/root_password" \
  -e MARIADB_ROOT_PASSWORD_FILE=/run/secrets/root_password \
  docker.mariadb.com/enterprise-server:11.8
```

**Understanding the flags:**
* **`-v "$(pwd)/..."`**: This volume mount takes your local file (`mariadb_root_password_secret`) and securely maps it inside the container to `/run/secrets/root_password`.
* **`-e MARIADB_ROOT_PASSWORD_FILE=...`**: This instructs the MariaDB initialization script to look inside `/run/secrets/root_password` and use its contents as the root password.

#### Step 3: Verify the Connection

Once the container is up and running, you can test the connection to ensure the password was applied correctly. 

Grab your container ID (with `docker ps`) and use `docker exec` to start an interactive database session using the password you defined in Step 1:

```bash
docker exec -it <container_id> mariadb -u root -p'MariaDB11!'
```

If the secret was read successfully, you will be authenticated and greeted by the MariaDB:

```
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 5
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}