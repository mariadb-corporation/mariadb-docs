---
description: >-
  Complete healthcheck.sh Docker reference: --connect, --innodb_initialized,
  --replication_* checks, .my-healthcheck.cnf config, and environment variables.
---

# Using Healthcheck

## Using Healthcheck.sh

The healthcheck.sh script is part of the Docker Official Images of MariaDB Server. The script is part of the [repository of the Docker Official Image of MariaDB Server](https://github.com/MariaDB/mariadb-docker/blob/master/healthcheck.sh).

The script processes a number of argument and tests, together, in strict order. Arguments pertaining to a test must occur before the test name. If a test fails, no further processing is performed. Both arguments and tests begin with a double-hyphen.

By default, (since 2023-06-27), official images will create `healthcheck@localhost`, `healthcheck@127.0.0.1`, `healthcheck@::1` users with a random password and USAGE privileges. [MARIADB\_HEALTHCHECK\_GRANTS](mariadb-server-docker-official-image-environment-variables.md#mariadb_healthcheck_grants) can be used for `--replication` where additional grants are required. This is stored in `.my-healthcheck.cnf` in the datadir of the container and passed as the `--defaults-extra-file` to the healthcheck.sh script if it exists. The `.my-healthcheck.cnf` also sets `protocol=tcp` for the `mariadb` so `--connect` is effectively there on all tests.

The [MARIADB\_AUTO\_UPGRADE=1](mariadb-server-docker-official-image-environment-variables.md#mariadb_auto_upgrade-mariadb_disable_upgrade_backup) will regenerate the `.my-healthcheck.cnf` file if missing and recreate the healthcheck users of the database with a new random password. The current port configuration of the MariaDB container is written into this file.

The [MARIADB\_MYSQL\_LOCALHOST\_USER=1, MARIADB\_MYSQL\_LOCALHOST\_GRANTS](mariadb-server-docker-official-image-environment-variables.md#mariadb_mysql_localhost_user-mariadb_mysql_localhost_grants) environment variables can also be used, but with the creation of the healthcheck user, these are backwards compatible.

## Compose File Example

An example of a compose file that uses the healthcheck.sh to determine a healthy service as a dependency before starting a WordPress service:

```
version: "3"
services:
  mariadb:
    image: mariadb:lts
    environment:
      - MARIADB_DATABASE=testdb
      - MARIADB_USER=testuser
      - MARIADB_PASSWORD=password
      - MARIADB_RANDOM_ROOT_PASSWORD=1
    healthcheck:
      test: ["CMD", "healthcheck.sh", "--connect", "--innodb_initialized"]
      start_period: 10s
      interval: 10s
      timeout: 5s
      retries: 3
  wordpress:
    image: wordpress
    environment:
      - WORDPRESS_DB_HOST=mariadb
      - WORDPRESS_DB_NAME=testdb
      - WORDPRESS_DB_USER=testuser
      - WORDPRESS_DB_PASSWORD=password
    depends_on:
      mariadb:
        condition: service_healthy
```

## Tests

The various health check flags used for monitoring the status and readiness of a MariaDB server.

| Health Check Flag             | Description                                                                                                                                                                                                                                                                                                                                                                                                                    | Required Privileges                                                              |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| `--connect`                   | Active when an external user can connect to the TCP port of MariaDB Server. This strictly tests the TCP connection, not authentication.                                                                                                                                                                                                                                                                                        |                                                                                  |
| `--innodb_initialized`        | True when InnoDB has completed initializing, including any rollback or crash recovery.                                                                                                                                                                                                                                                                                                                                         | The connecting user must have `USAGE` privileges.                                |
| `--innodb_buffer_pool_loaded` | Indicates that the previously saved buffer pool dump has been completely loaded, meaning the server has a hot cache ready for use.                                                                                                                                                                                                                                                                                             | The connecting user must have `USAGE` privileges.                                |
| `--galera_online`             | Indicates that the Galera node is online (based on the `wsrep_local_state` variable). This includes states like "joining" and "donor" where it cannot serve SQL queries.                                                                                                                                                                                                                                                       | The connecting user must have `USAGE` privileges.                                |
| `--replication`               | Tests a replica based on the `--replication_*` parameters. All subtests must pass: \<ul>\<li>io: The IO thread is running.\</li>\<li>sql: The SQL thread is running.\</li>\<li>seconds\_behind\_master: The replica is less than a specified number of seconds behind the primary.\</li>\<li>sql\_remaining\_delay: The delayed replica is less than a specified number of seconds behind the primary's execution.\</li>\</ul> | `REPLICATION_CLIENT` (before MariaDB 10.5) or `REPLICA MONITOR` (MariaDB 10.5+). |
| `--mariadbupgrade`            | Indicates that MariaDB is upgraded to the current version.                                                                                                                                                                                                                                                                                                                                                                     |                                                                                  |

## Parameters

To customize the health checks described previously, you can use the following parameters:

| Parameter                                                                                                                                       | Description                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `--replication_all`                                                                                                                             | Checks all replication sources.                                                                                      |
| `--replication_name=n`                                                                                                                          | Sets the multisource connection name to be tested. This unsets `--replication_all`.                                  |
| `--replication_io`                                                                                                                              | Checks if the replication IO thread is running.                                                                      |
| `--replication_sql`                                                                                                                             | Checks if the replication SQL thread is running.                                                                     |
| `--replication_seconds_behind_master=n`                                                                                                         | Checks if the replication delay is less than or equal to `n` seconds.                                                |
| `--replication_sql_remaining_delay=n`                                                                                                           | Checks if the remaining SQL delay is less than or equal to `n` seconds.                                              |
| `--su=n`                                                                                                                                        | Changes to the specified user (`n`). Can only be used once from the default `root` user.                             |
| `--su-mysql`                                                                                                                                    | Changes to the `mysql` unix user. Respawns the script, resetting all parameters, so it should be the first argument. |
| `--datadir=n`                                                                                                                                   | Specifies the data directory location (`n`) for the `--mariadbupgrade` test.                                         |
| <p><code>--no-defaults</code><br><code>--defaults-file</code><br><code>--defaults-extra-file</code><br><code>--defaults-group-suffix</code></p> | These parameters are passed to the `mariadb` shell for all tests except `--mariadbupgrade`.                          |

## Examples

```bash
healthcheck.sh --su-mysql --connect --innodb_initialized
```

Switch to `mysql` user, and check if can connect and the innodb is initialized.

```bash
healthcheck.sh --su-mysql --connect --replication_io --replication_sql --replication_seconds_behind_master=600  --replication_sql_remaining_delay=30 ----replication_name=archive --replication --replication_seconds_behind_master=10  --replication_name=channel1 --replication
```

Switch to `mysql` user, check if connections can be made. For the replication channel `archive`, ensure IO and SQL threads are running, the seconds behind master is less than `600` seconds, and the SQL remaining delay is less than `30` seconds. For the `channel1`, the seconds behind master is limited to `10` seconds maximum.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
