---
description: >-
  How to authenticate with and pull images from the private MariaDB Enterprise
  Docker Registry.
---

# MariaDB Enterprise Docker Registry for MariaDB Enterprise Server

MariaDB Corporation provides the MariaDB Enterprise Docker Registry. The MariaDB Enterprise Docker Registry provides Docker images for MariaDB Enterprise Server.

This page contains reference material for the MariaDB Enterprise Docker Registry.

The reference material on this page applies to MariaDB Enterprise Server 10.6 and later.

## Details

Docker is an open platform for developing, shipping, and running applications that allows you to separate your applications from your infrastructure.

MariaDB Corporation provides the MariaDB Enterprise Docker Registry. The MariaDB Enterprise Docker Registry provides Docker images for MariaDB Enterprise Server.

For examples that show how to use the Docker images in the MariaDB Enterprise Docker Registry for MariaDB Enterprise Server, see [Examples](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md#examples).

Other details are listed in the sections below.

* [Versions](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md#versions)
* [Storage Engines](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md#storage-engines)
* [Plugins](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md#plugins)
* [Repositories](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md#repositories)
* [Tags](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md#tags)

### Versions

The MariaDB Enterprise Docker Registry provides Docker images for **MariaDB Enterprise Server 10.6 and later**.

### Storage Engines

The Docker images for MariaDB Enterprise Server include all storage engines that are installed with MariaDB Enterprise Server by default. The following storage engines are currently included:

* [Aria](../../../server-usage/storage-engines/aria/)
* [CSV](../../../server-usage/storage-engines/csv/)
* [InnoDB](../../../server-usage/storage-engines/innodb/)
* [MEMORY](../../../server-usage/storage-engines/memory-storage-engine.md)
* [MRG\_MYISAM](../../../server-usage/storage-engines/merge.md)
* [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/)

You can check which storage engines are installed by connecting to the Docker container and executing the [SHOW ENGINES](../../../reference/sql-statements/administrative-sql-statements/show/show-engines.md) statement.

### Plugins

The Docker images for MariaDB Enterprise Server include all plugins that are installed with MariaDB Enterprise Server by default.

You can check which plugins are installed by connecting to the Docker container and executing the [SHOW PLUGINS](../../../reference/sql-statements/administrative-sql-statements/show/show-plugins.md) statement.

The container contains shared libraries for additional plugins that can be installed with the [INSTALL SONAME](../../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) statement or the [--plugin-load-add](../../starting-and-stopping-mariadb/mariadbd-options.md#plugin-load-add) command-line option. You can check which plugins are available by querying the [information\_schema.ALL\_PLUGINS](../../../reference/system-tables/information-schema/information-schema-tables/all-plugins-table-information-schema.md) table:

```sql
SELECT PLUGIN_NAME, PLUGIN_VERSION, PLUGIN_LIBRARY
FROM information_schema.ALL_PLUGINS
WHERE PLUGIN_STATUS = 'NOT INSTALLED';
```

```
+---------------------------+----------------+------------------------+
| PLUGIN_NAME               | PLUGIN_VERSION | PLUGIN_LIBRARY         |
+---------------------------+----------------+------------------------+
| pam                       | 1.0            | auth_pam_v1.so         |
| LOCALES                   | 1.0            | locales.so             |
| BLACKHOLE                 | 1.0            | ha_blackhole.so        |
| SQL_ERROR_LOG             | 1.0            | sql_errlog.so          |
| METADATA_LOCK_INFO        | 0.1            | metadata_lock_info.so  |
| pam                       | 2.0            | auth_pam.so            |
| SERVER_AUDIT              | 1.4            | server_audit.so        |
| file_key_management       | 1.0            | file_key_management.so |
| QUERY_RESPONSE_TIME       | 1.0            | query_response_time.so |
| QUERY_RESPONSE_TIME_AUDIT | 1.0            | query_response_time.so |
+---------------------------+----------------+------------------------+
```

### Repositories

The MariaDB Enterprise Docker Registry contains a single repository, which provides images for MariaDB Enterprise Server:

* `enterprise-server`

### Tags

The `enterprise-server` repository in the MariaDB Enterprise Docker Registry contains images for different MariaDB Enterprise Server releases using specific tags:

| Type of release?        | Tags                                                                                                  | Description                                                                                                                                                                                                                                                                                       |
| ----------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Latest release series   | <ul><li><code>latest</code></li></ul>                                                                 | This tag refers to the most recent image for the latest MariaDB Enterprise Server release series, which is currently MariaDB Enterprise Server 11.8.                                                                                                                                              |
| Specific release series | <ul><li><code>11.8</code></li><li><code>11.4</code></li><li><code>10.6</code></li></ul>               | These tags refer to the images for the most recent minor release of each specific MariaDB Enterprise Server release series.                                                                                                                                                                       |
| Specific minor release  | <ul><li><code>11.8.3-1</code></li><li><code>11.4.8-5</code></li><li><code>10.6.23-19</code></li></ul> | These tags refer to images for specific MariaDB Enterprise Server minor releases. The listed tags are examples of minor releases. For a full list of minor releases, see [MariaDB Enterprise Server All Releases](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/all-releases). |

## Examples

* [Connect to Container with Docker Bridge Networking](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md#connect-to-container-with-docker-bridge-networking)
* [Connect to Container with Host Networking](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md#connect-to-container-with-host-networking)
* [Create a Container with Docker Bridge Networking](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md#create-a-container-with-docker-bridge-networking)
* [Create a Container with Host Networking](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md#create-a-container-with-host-networking)
* [Environment Variables](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md#environment-variables)
* [Inspect Container](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md#inspect-container)
* [Log In to Docker Registry](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md#log-in-to-docker-registry)
* [Obtain a Shell in Container](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md#obtain-a-shell-in-container)
* [Pull Docker Image](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md#pull-docker-image)
* [Remove Container](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md#remove-container)
* [Stop Container](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md#stop-container)
* [View Container Logs](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md#view-container-logs)

### Connect to Container with Docker Bridge Networking

To connect to a Docker container that uses Docker bridge networking, execute [MariaDB Client](../../../clients-and-utilities/mariadb-client/) on the container using [`docker exec`](https://docs.docker.com/engine/reference/commandline/exec/):

```bash
docker exec --interactive --tty \
   mariadb-es-11.4 \
   mariadb \
   --user=root \
   --password
```

To confirm the client is connected to the Docker container and the container is using the correct version of MariaDB Enterprise Server, query the [version](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#version) system variable with the [SHOW GLOBAL VARIABLES](../../../reference/sql-statements/administrative-sql-statements/show/show-variables.md) statement:

```sql
SHOW GLOBAL VARIABLES
   LIKE 'version'\G
```

```
*************************** 1. row ***************************
Variable_name: version
        Value: 11.4.5-3-MariaDB-enterprise-log
```

To exit the container, use `exit`:

```bash
exit
```

```
Bye
```

The example above shows how to connect to a Docker container using MariaDB Client on the container, but you can also connect using MariaDB Client on the host using TCP/IP. You can [inspect the Docker container](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md#inspect-container) to find the container's IP address and TCP port bindings.

### Connect to Container with Host Networking

To connect to a Docker container that uses host networking, execute [MariaDB Client](../../../clients-and-utilities/mariadb-client/) on the host node and specify the host's IP address and the container's port:

```bash
mariadb --host=192.0.2.1 \
   --port=3307 \
   --user=root \
   --password
```

To confirm the client is connected to the Docker container and the container is using the correct version of MariaDB Enterprise Server, query the [version](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#version) system variable with the [SHOW GLOBAL VARIABLES](../../../reference/sql-statements/administrative-sql-statements/show/show-variables.md) statement:

```sql
SHOW GLOBAL VARIABLES
   LIKE 'version'\G
```

```
*************************** 1. row ***************************
Variable_name: version
        Value: 11.8.3-1-MariaDB-enterprise-log
```

To exit the container, use `exit`:

```bash
exit
```

```
Bye
```

### Create a Container with Docker Bridge Networking

By default, Docker containers use Docker bridge networking. To make connecting to the container easier, Docker can use port bindings to publish the container's TCP ports to the host.

To create a Docker container using Docker bridge networking, execute [`docker run`](https://docs.docker.com/engine/reference/commandline/run/):

```bash
docker run --detach \
   --name mariadb-es-11.8 \
   --env MARIADB_ROOT_PASSWORD='Password123!' \
   --publish '3307:3306/tcp' \
   docker.mariadb.com/enterprise-server:11.8 \
   --log-bin=mariadb-bin \
   <other mariadbd command-line options>
```

```
3082ab69e565be21c6157bb5a3d8c849ec03a2c51576778ac417a8a3aa9e7537
```

* Configure the container using [environment variables](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md#environment-variables) by setting the `--env` command-line option.
* Configure TCP port bindings for the container by setting the `--publish` or `--publish-all` command-line options.
* Configure MariaDB Enterprise Server by setting [mariadbd command-line options](../../starting-and-stopping-mariadb/mariadbd-options.md).

To confirm the Docker container is running, execute [`docker ps`](https://docs.docker.com/engine/reference/commandline/ps/):

```bash
docker ps \
   --all \
   --filter ancestor='docker.mariadb.com/enterprise-server:11.8'
```

```
CONTAINER ID   IMAGE                                         COMMAND                  CREATED          STATUS                      PORTS      NAMES
3082ab69e565   docker.mariadb.com/enterprise-server:11.8   "/es-entrypoint.sh -…"   12 seconds ago   Up 11 seconds               3306/tcp   mariadb-es-11.8
```

### Create a Container with Host Networking

A Docker container can be configured to use the host operating system's network.

To create a Docker container using host networking, execute [`docker run`](https://docs.docker.com/engine/reference/commandline/run/) and specify the `--network host` option:

```bash
docker run --detach \
   --network host \
   --name mariadb-es-11.8 \
   --env MARIADB_ROOT_PASSWORD='Password123!' \
   docker.mariadb.com/enterprise-server:11.8 \
   --port=3307 \
   --log-bin=mariadb-bin \
   <other mariadbd command-line options>
```

```
3082ab69e565be21c6157bb5a3d8c849ec03a2c51576778ac417a8a3aa9e7537
```

* Configure the container using [environment variables](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md#environment-variables) by setting the `--env` command-line option.
* Configure the port for MariaDB Enterprise Server by setting the [--port](../../../server-usage/connecting/mariadb-connecting-guide-1.md#port) command-line option.
* Configure MariaDB Enterprise Server by setting [mariadbd command-line options](../../starting-and-stopping-mariadb/mariadbd-options.md).

To confirm the Docker container is running, execute [`docker ps`](https://docs.docker.com/engine/reference/commandline/ps/):

```bash
docker ps \
   --all \
   --filter ancestor='docker.mariadb.com/enterprise-server:11.8'
```

### Environment Variables

A Docker container can be configured to perform the following tasks using environment variables:

* Create a custom database
* Create a custom database user account with a custom password
* Initialize the timezone tables
* Set the host for the `root` database user
* Set the password for the `root` database user

The following table contains details about the environment variables that are supported:

| Environment Variable         | Description                                                                                                                                                                                                                                                                                                                                                                                           | Default    | Allowed Values                                                                              |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------------------------------------------------------------------------------------------- |
| `MARIADB_DATABASE`           | When the `MARIADB_DATABASE` environment variable is set to a valid database name, create the specified database if it does not already exist.                                                                                                                                                                                                                                                         | No default | Any valid database name                                                                     |
| `MARIADB_INITDB_SKIP_TZINFO` | By default, the entrypoint script automatically loads the timezone data needed for the `CONVERT_TZ()` function. If it is not needed, any non-empty value disables timezone loading.                                                                                                                                                                                                                   | No default | <ul><li><code>0</code></li><li><code>1</code></li></ul>                                     |
| `MARIADB_PASSWORD`           | When the `MARIADB_USER` and `MARIADB_PASSWORD` environment variables are both set, create a user account with the specified user name and password.                                                                                                                                                                                                                                                   | No default | Any valid password                                                                          |
| `MARIADB_ROOT_HOST`          | When the `MARIADB_ROOT_HOST` environment variable is set to a valid hostname, the `root` user account will be restricted to logins from that hostname.                                                                                                                                                                                                                                                | `%`        | Any valid hostname                                                                          |
| `MARIADB_ROOT_PASSWORD`      | When the `MARIADB_ROOT_PASSWORD` environment variable is set to `RANDOM`, a random password is generated for the `root` user account. When the `MARIADB_ROOT_PASSWORD` environment variable is set to `EMPTY`, the `root` user account uses an empty password. When the `MARIADB_ROOT_PASSWORD` environment variable is set to a valid password, the `root` user account uses the specified password. | No default | <ul><li><code>RANDOM</code></li><li><code>EMPTY</code></li><li>Any valid password</li></ul> |
| `MARIADB_USER`               | When the `MARIADB_USER` and `MARIADB_PASSWORD` environment variables are both set, create a user account with the specified user name and password.                                                                                                                                                                                                                                                   | No default | Any valid user name                                                                         |

To create a Docker container using environment variables, execute [`docker run`](https://docs.docker.com/engine/reference/commandline/run/), environment variables and specify each environment variable using the `--env` option:

```bash
docker run --detach \
   --network host \
   --name mariadb-es-11.8 \
   --env MARIADB_ROOT_PASSWORD='Password123!' \
   docker.mariadb.com/enterprise-server:11.8
```

```
3082ab69e565be21c6157bb5a3d8c849ec03a2c51576778ac417a8a3aa9e7537
```

### Inspect Container

A Docker contained can be inspected to find out internal details about the container, such as the following details:

* IP addresses
* MAC addresses
* Port bindings

To inspect all internal details about a Docker container, execute [`docker inspect`](https://docs.docker.com/engine/reference/commandline/inspect/):

```bash
docker inspect mariadb-es-11.8
```

```json
[
    {
        "Id": "d784a193ad828cbd3db10dfbef3e3b7274465fa587453c3f6e2e27703b361173",
        "Created": "2021-10-13T20:25:04.994759266Z",
        "Path": "docker-entrypoint.sh",
        "Args": [
            "--log-bin=mariadb-bin"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 33714,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2021-10-13T20:25:05.32049779Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        ..
    }
]
```

To inspect a specific internal detail about a Docker container, execute [`docker inspect`](https://docs.docker.com/engine/reference/commandline/inspect/) and specify a filter using the `--format` option. Some examples are shown below.

To inspect the container's IP address:

```bash
docker inspect \
   --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' \
   mariadb-es-11.8
```

```
172.17.0.3
```

To inspect the container's TCP port bindings:

```bash
docker inspect \
   --format='{{range $p, $conf := .NetworkSettings.Ports}}Container port: {{$p}} -> Host port: {{(index $conf 0).HostPort}} {{end}}' \
   mariadb-es-11.8
```

```
Container port: 3306/tcp -> Host port: 3307
```

### Log In to Docker Registry

To log in to the MariaDB Enterprise Docker Registry, execute [`docker login`](https://docs.docker.com/engine/reference/commandline/login/):

```bash
docker login docker.mariadb.com
```

When prompted, enter the login details:

* As the user name, enter the email address associated with your [MariaDB ID](https://id.mariadb.com/).
* As the password, enter your [Customer Download Token](../../install-and-upgrade-mariadb/installing-enterprise-server/token.md).

The login details will be saved.

To confirm the login details were saved, check the `~/.docker/config.json` file for a JSON object named `"docker.mariadb.com"` inside an `"auths"` parent JSON object:

```bash
cat ~/.docker/config.json
{
   "auths": {
      "docker.mariadb.com": {
         "auth": "<auth_hash>"
      }
   }
}
```

### Obtain a Shell in Container

To obtain a shell in the Docker container, execute the shell on the container using [`docker exec`](https://docs.docker.com/engine/reference/commandline/exec/):

```bash
docker exec --interactive --tty \
   mariadb-es-11.8 \
   bash
```

### Pull Docker Image

To pull a Docker image with the [appropriate tag](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md#tags), execute [`docker pull`](https://docs.docker.com/engine/reference/commandline/pull/):

```bash
docker pull docker.mariadb.com/enterprise-server:11.8
```

```
11.8: Pulling from enterprise-server
5d87d5506868: Pull complete
Digest: sha256:68795ca747901e3402e30dab71d6d8bc72bce727db3b9e4888979468be77d250
Status: Downloaded newer image for docker.mariadb.com/enterprise-server:11.8
docker.mariadb.com/enterprise-server:11.8
```

To confirm the Docker image has been pulled, execute [`docker images`](https://docs.docker.com/engine/reference/commandline/images/):

```bash
docker images \
   --filter=reference='docker.mariadb.com/enterprise-server'
```

```
REPOSITORY                             TAG       IMAGE ID       CREATED        SIZE
docker.mariadb.com/enterprise-server   11.8      dd17291aa340   3 months ago   451MB
```

### Remove Container

To remove a Docker container, execute [`docker rm`](https://docs.docker.com/engine/reference/commandline/rm/):

```bash
docker rm mariadb-es-11.8
```

```
mariadb-es-11.8
```

To confirm the container is removed, execute [`docker ps`](https://docs.docker.com/engine/reference/commandline/ps/):

```bash
docker ps \
   --all \
   --filter ancestor='docker.mariadb.com/enterprise-server:11.8'
```

```
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

### Stop Container

To stop a Docker container, execute [`docker stop`](https://docs.docker.com/engine/reference/commandline/stop/):

```bash
docker stop mariadb-es-11.8
```

```
mariadb-es-11.8
```

To confirm the container is stopped, execute [`docker ps`](https://docs.docker.com/engine/reference/commandline/ps/):

```bash
docker ps \
   --all \
   --filter ancestor='docker.mariadb.com/enterprise-server:11.8'
```

```
CONTAINER ID   IMAGE                                         COMMAND                  CREATED         STATUS                            PORTS       NAMES
3082ab69e565   docker.mariadb.com/enterprise-server:11.8   "/es-entrypoint.sh -…"   2 minutes ago   Exited (143) About a minute ago               mariadb-es-11.8
```

### View Container Logs

To view the logs in the Docker container, execute [`docker logs`](https://docs.docker.com/engine/reference/commandline/logs/):

```bash
docker logs mariadb-es-11.8
```
