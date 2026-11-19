---
description: >-
  Reference for the environment variables that configure the MariaDB Community
  Server Docker Official Image and the MariaDB Enterprise Server Docker images
  when a container initializes.
---

# MariaDB Docker Image Environment Variables

This page applies to two families of images:

* The MariaDB Community Server Docker Official Image, `mariadb` on Docker Hub
* The MariaDB Enterprise Server images, `docker.mariadb.com/enterprise-server` in the [MariaDB Enterprise Docker Registry](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md)

Both families support each variable on this page unless its section says otherwise.

When you start the image, you can adjust the initialization of the MariaDB Server instance by passing one or more environment variables on the docker run command line. Do note that all of the variables below, except `MARIADB_AUTO_UPGRADE`, will have no effect if you start the container with a data directory that already contains a database: any pre-existing database will always be left untouched on container startup.

All tags from `10.6` and above, `MARIADB_*` variables will be used in preference to `MYSQL_*` variables.

One of the following is required: `MARIADB_ROOT_PASSWORD_HASH`, `MARIADB_ROOT_PASSWORD`, `MARIADB_ALLOW_EMPTY_ROOT_PASSWORD`, or `MARIADB_RANDOM_ROOT_PASSWORD` (including `*_FILE` equivalents). Enterprise Server images that support them also accept [`MARIADB_UNIX_SOCKET_AUTHENTICATION`](#mariadb_unix_socket_authentication) or [`MARIADB_ROOT_TLS_CLIENT_AUTH`](#mariadb_root_tls_client_auth) instead.

Other environment variables are optional.

## Password Policy in the Enterprise Server Images

The MariaDB Enterprise Server images enable the [simple\_password\_check](../../../reference/plugins/password-validation-plugins/simple-password-check-plugin.md) plugin. Every password that the environment variables set must be at least 8 characters long and contain at least one digit, one uppercase letter, one lowercase letter, and one special character. If a password doesn't meet these requirements, initialization fails and the container exits. For the same reason, setting `MARIADB_ALLOW_EMPTY_ROOT_PASSWORD` makes the container exit. Setting [`MARIADB_ROOT_TLS_CLIENT_AUTH`](#mariadb_root_tls_client_auth) turns the policy off.

The Community Server image doesn't enable a password validation plugin.

## Environment Variables

### `MARIADB_ROOT_PASSWORD_HASH / MARIADB_ROOT_PASSWORD / MYSQL_ROOT_PASSWORD`

This specifies the password that will be set for the MariaDB root superuser account.

### `MARIADB_ALLOW_EMPTY_ROOT_PASSWORD / MYSQL_ALLOW_EMPTY_PASSWORD`

Set to a non-empty value, like `1`, to allow the container to be started with a blank password for the root user.

{% hint style="warning" %}
Setting this variable to yes is not recommended unless you really know what you are doing, since this will leave your MariaDB instance completely unprotected, allowing anyone to gain complete superuser access.
{% endhint %}

{% hint style="info" %}
In the MariaDB Enterprise Server images, setting this variable makes initialization fail and the container exit, because the [password policy](#password-policy-in-the-enterprise-server-images) rejects an empty password.
{% endhint %}

### `MARIADB_RANDOM_ROOT_PASSWORD / MYSQL_RANDOM_ROOT_PASSWORD`

Define a non-empty value, such as "yes," to auto-generate a random initial password for the root user. The password will be output to stdout, prefixed with "GENERATED ROOT PASSWORD: ...".

### `MARIADB_ROOT_HOST / MYSQL_ROOT_HOST`

`%` is the default hostname part of the root user in MariaDB. This can be changed to any valid hostname. Setting it to `localhost` restricts root access to only the local machine via the Unix socket.

### `MARIADB_USER_HOST`

**Applies to:** MariaDB Community Server image only

`%` is the default hostname part of the user created through `MYSQL_USER / MARIADB_USER` in MariaDB. This can be changed to any valid hostname or IP. Setting it to `localhost` restricts user access to only the local machine via the Unix socket.

### `MARIADB_DATABASE / MYSQL_DATABASE`

This variable allows you to specify the name of a database to be created on image startup.

### `MARIADB_USER / MYSQL_USER, MARIADB_PASSWORD_HASH / MARIADB_PASSWORD / MYSQL_PASSWORD`

To create a new user with full access permissions in MariaDB, both `user` and `password` variables are required, along with a designated `database`. This new user will be granted comprehensive privileges (`GRANT ALL`) to the specified `MARIADB_DATABASE`. Note that this method should not be utilized for creating the root superuser, as this user is automatically created with the password provided by the `MARIADB_ROOT_PASSWORD` or `MYSQL_ROOT_PASSWORD` variable.

### `MARIADB_MYSQL_LOCALHOST_USER / MARIADB_MYSQL_LOCALHOST_GRANTS`

Set `MARIADB_MYSQL_LOCALHOST_USER` to a non-empty value to create the `mysql@localhost` database user. This user is useful for health checks and backup scripts. The `mysql@localhost` user gets `USAGE` privileges by default. If more access is needed, additional global privileges can be provided as a comma-separated list. Be cautious when sharing a volume containing MariaDB's unix socket (`/var/run/mysqld` by default) as privileges beyond `USAGE` may pose security risks. This user can also be used with `mariadb-backup`. Refer to `healthcheck.sh` for required privileges for each health check test.

### `MARIADB_HEALTHCHECK_GRANTS`

Set `MARIADB_HEALTHCHECK_GRANTS` to the grants required to be given to the `healthcheck@localhost`, `healthcheck@127.0.0.1`, `healthcheck@::1`, users. When not specified the default grant is [USAGE](../../../reference/sql-statements/account-management-sql-statements/grant.md#the-usage-privilege).

The main value used here will be [`REPLICA MONITOR`](../../../reference/sql-statements/account-management-sql-statements/grant.md#replica-monitor) for the [`healthcheck --replication`](using-healthcheck-sh.md) test.

### `MARIADB_INITDB_SKIP_TZINFO / MYSQL_INITDB_SKIP_TZINFO`

By default, the entrypoint script automatically loads the timezone data needed for the `CONVERT_TZ()` function. If it is not needed, any non-empty value disables timezone loading.

### `MARIADB_AUTO_UPGRADE / MARIADB_DISABLE_UPGRADE_BACKUP`

Set `MARIADB_AUTO_UPGRADE` to a non-empty value to have the entrypoint check whether [mariadb-upgrade](../../../clients-and-utilities/deployment-tools/mariadb-upgrade.md) needs to run, and if so, run the upgrade before starting the MariaDB server.

Before the upgrade, a backup of the system database is created in the top of the datadir with the name `system_mysql_backup_*.sql.zst`. This backup process can be disabled by setting `MARIADB_DISABLE_UPGRADE_BACKUP` to a non-empty value.

If `MARIADB_AUTO_UPGRADE` is set, and the `.my-healthcheck.cnf` file is missing, the `healthcheck` users are recreated if they don't exist, `MARIADB_HEALTHCHECK_GRANTS` grants are given, the passwords of the `healthcheck` users are reset to a random value and the `.my-healthcheck.cnf` file is recreated with the new password populated.

### `MARIADB_MASTER_HOST / MARIADB_MASTER_PORT`

When `MARIADB_MASTER_HOST` is specified, the container will connect to this host and replicate from it. `MARIADB_MASTER_PORT` sets the port to connect to, and defaults to `3306`.

### `MARIADB_REPLICATION_USER / MARIADB_REPLICATION_PASSWORD_HASH / MARIADB_REPLICATION_PASSWORD`

When `MARIADB_MASTER_HOST` is defined, `MARIADB_REPLICATION_USER` and `MARIADB_REPLICATION_PASSWORD` will be used to connect to the master. When not specified, the `MARIADB_REPLICATION_USER` will be created with the `REPLICATION REPLICA` grants needed for a client to initiate replication.

### `MARIADB_UNIX_SOCKET_AUTHENTICATION`

**Applies to:** MariaDB Enterprise Server images 10.6.25-22, 11.4.10-8, 11.8.6-4, 12.3.3-1, and later

When set to a non-empty value, such as `1`, the container creates two administrative accounts, `root@localhost` and `mysql@localhost`, that have all privileges and authenticate only with [Unix socket authentication](../../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md). Each account can connect only from inside the container, as the operating system user of the same name. Commands that you run with `docker exec` run as the `mysql` operating system user, so connect with `mariadb -u mysql`. No `root` account is created for other hosts.

This variable can't be combined with any of the `MARIADB_ROOT_PASSWORD*` variables.

### `MARIADB_ROOT_TLS_CLIENT_AUTH`

**Applies to:** MariaDB Enterprise Server images 12.3.3-1 and later

When set to a true value (`1`, `true`, `yes`, or `on`, case-insensitive), the `root` user is created with an X.509 `REQUIRE` clause and no password, so it authenticates with a TLS client certificate instead of a password. The option alone satisfies the requirement to specify a root password option.

The account is created for `MARIADB_ROOT_HOST`: nothing is created for `root` when `MARIADB_ROOT_HOST` is empty or `localhost`. The `root@localhost` account has no password, so it can still connect from inside the container without a certificate.

Because the password validation plugins refuse passwordless accounts, the container starts the server with `simple_password_check` and `cracklib_password_check` disabled when this option is set. They stay disabled for the running server, so the [password policy](#password-policy-in-the-enterprise-server-images) doesn't apply to any account.

### `MARIADB_ROOT_TLS_SUBJECT / MARIADB_ROOT_TLS_ISSUER`

**Applies to:** MariaDB Enterprise Server images 12.3.3-1 and later

The certificate subject and issuer that the `root` user's client certificate must have, in OpenSSL one-line format (for example, `/CN=root` or `/CN=my-ca`). They are used only when `MARIADB_ROOT_TLS_CLIENT_AUTH` is enabled, and can be combined. If neither is set, the account is created with `REQUIRE X509`.

### `SKIP_INIT_WSREP_OFF`

**Applies to:** MariaDB Enterprise Server images 10.6.25-22, 11.4.10-8, 11.8.6-4, 12.3.3-1, and later

By default, the temporary server used for initialization is started with Galera Cluster replication explicitly turned off (`--wsrep_on=OFF`). If this variable is set to any non-empty value, that flag is omitted, allowing the temporary server to start with wsrep enabled.

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
  -e MARIADB_ROOT_PASSWORD="YourStrongPassword123!" \
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
      - MARIADB_ROOT_PASSWORD=YourStrongPassword123!
```

## Using `_FILE` Environment Variables for Secrets

When running Docker containers, it is a security best practice to avoid passing sensitive information, like database passwords, directly as plain-text environment variables. The MariaDB container images allow you to securely read secrets from mounted files by appending `_FILE` to the standard environment variable name. 

### List of supported `_FILE` Environment Variables

The `_FILE` variables follow the same image support as the variables they replace.

| Name | Description |
| --- | --- |
| `MYSQL_ROOT_HOST_FILE` | Path to a file containing the host from which the root user is allowed to connect. |
| `MARIADB_ROOT_HOST_FILE` | Path to a file containing the host from which the root user is allowed to connect. |
| `MYSQL_DATABASE_FILE` | Path to a file containing the name of a database to be created on initialization. |
| `MARIADB_DATABASE_FILE` | Path to a file containing the name of a database to be created on initialization. |
| `MYSQL_USER_FILE` | Path to a file containing the username for a new user to be created on initialization. |
| `MARIADB_USER_FILE` | Path to a file containing the username for a new user to be created on initialization. |
| `MARIADB_USER_HOST_FILE` | Path to a file containing the host part of the user created on initialization. Community Server image only. |
| `MYSQL_PASSWORD_FILE` | Path to a file containing the password for the user defined by `MYSQL_USER`. |
| `MARIADB_PASSWORD_FILE` | Path to a file containing the password for the user defined by `MARIADB_USER`. |
| `MYSQL_ROOT_PASSWORD_FILE` | Path to a file containing the password for the root database user. |
| `MARIADB_ROOT_PASSWORD_FILE` | Path to a file containing the password for the root database user. |
| `MARIADB_PASSWORD_HASH_FILE` | Path to a file containing the hashed password for the created standard user. |
| `MARIADB_ROOT_PASSWORD_HASH_FILE` | Path to a file containing the hashed password for the root database user. |
| `MARIADB_UNIX_SOCKET_AUTHENTICATION_FILE` | Path to a file containing a value to enable/disable Unix socket authentication. Enterprise Server images only. |
| `MARIADB_ROOT_TLS_CLIENT_AUTH_FILE` | Path to a file containing a value to enable TLS client authentication for the root user. Enterprise Server images only. |
| `MARIADB_ROOT_TLS_SUBJECT_FILE` | Path to a file containing the certificate subject required for the root user. Enterprise Server images only. |
| `MARIADB_ROOT_TLS_ISSUER_FILE` | Path to a file containing the certificate issuer required for the root user. Enterprise Server images only. |
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
