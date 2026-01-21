---
description: >-
  Tutorial on using Docker Compose to orchestrate a full LAMP stack (Linux,
  Apache, MariaDB, PHP) environment.
---

# Setting Up a LAMP Stack with Docker Compose

Docker Compose is a tool that allows one to declare which Docker containers should run, and which relationships should exist between them. It follows the **infrastructure as code** approach, just like most automation software and Docker itself.

For information about installing Docker Compose, see [Install Docker Compose](https://docs.docker.com/compose/install/) in Docker documentation.

## The `docker-compose.yml` File

When using Docker Compose, the Docker infrastructure must be described in a YAML file called `docker-compose.yml`.

Let's see an example:

```yaml
version: "3"

services:
  web:
    image: "apache:${PHP_VERSION}"
    restart: 'always'
    depends_on:
      - mariadb
    restart: 'always'
    ports:
      - '8080:80'
    links:
      - mariadb
  mariadb:
    image: "mariadb:${MARIADB_VERSION}"
    restart: 'always'
    volumes: 
      - "/var/lib/mysql/data:${MARIADB_DATA_DIR}"
      - "/var/lib/mysql/logs:${MARIADB_LOG_DIR}"
      - /var/docker/mariadb/conf:/etc/mysql
    environment:
      MYSQL_ROOT_PASSWORD: "${MYSQL_ROOT_PASSWORD}"
      MYSQL_DATABASE: "${MYSQL_DATABASE}"
      MYSQL_USER: "${MYSQL_USER}"
      MYSQL_PASSWORD: "${MYSQL_PASSWORD}"
```

In the first line we declare that we are using version 3 of the Docker compose language.

Then we have the list of services, namely the `web` and the `mariadb` services.

Let's see the properties of the services:

| Property      | Description                                                                                                                             |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `port`        | Maps the 8080 container port to the 80 host system port; useful for development, allows browser connection to containerized web server. |
| `links`       | Declares container connectivity, ensuring that the container can connect to `mariadb`. The hostname is the container name.              |
| `depends_on`  | Specifies that `mariadb` must start before `web`, ensuring the application can connect once MariaDB is ready.                           |
| `restart`     | Ensures containers restart automatically if they crash (`restart: always`).                                                             |
| `volumes`     | Creates accessible directories for containers on the host system, facilitating data persistence even if a container is destroyed.       |
| `environment` | Sets environment variables within the container, crucial for defining MariaDB root credentials.                                         |

### About Volumes

It is good practice to create volumes for:

* The [data directory](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir), so we don't lose data when a container is created or replaced, perhaps to upgrade MariaDB.
* The directory where we put all the logs, if it is not the datadir.
* The directory containing all configuration files (for development environments), so we can edit those files with the editor installed in the host system. Normally no editor is installed in containers. In production we don't need to do this, because we can copy files from a repository located in the host system to the containers.

Note that Docker Compose variables are just placeholders for values. Compose does not support assignment, conditionals or loops.

### Using Variables

In the above example you can see several variables, like `${MARIADB_VERSION}`. Before executing the file, Docker Compose will replace this syntax with the `MARIADB_VERSION` variable.

Variables allow making Docker Compose files more re-usable: in this case, we can use any MariaDB image version without modifying the Docker Compose file.

The most common way to pass variables is to write them into a file. This has the benefit of allowing us to version the variable file along with the Docker Compose file. It uses the same syntax you would use in BASH:

```bash
PHP_VERSION=8.0
MARIADB_VERSION=10.6
...
```

For bigger setups, it could make sense to use different environment files for different services. To do so, we need to specify the file to use in the Compose file:

```yaml
services:
  web:
    env_file:
      - web-variables.env
...
```

## Docker Compose Commands

Docker Compose is operated using `docker-compose`. Here we'll see the most common commands. For more commands and for more information about the commands mentioned here, see the documentation.

Docker Compose assumes that the Composer file is located in the current directory and it's called `docker-compose.yml`. To use a different file, the `-f <filename>` parameter must be specified.

| Command                              | Description                                                                                            |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `docker-compose pull`                | Pulls the necessary images.                                                                            |
| `docker-compose up --no-recreate`    | Creates containers only if they do not already exist.                                                  |
| `docker-compose up`                  | Creates containers if they don't exist and recreates them if their image or configuration has changed. |
| `docker-compose up --force-recreate` | Recreates containers in all cases.                                                                     |
| `docker-compose up --no-start`       | Creates containers without starting them.                                                              |
| `docker-compose restart`             | Restarts containers without recreating them.                                                           |
| `docker-compose kill <service>`      | Kills a specific container by sending it a SIGKILL signal.                                             |
| `docker-compose rm -f <service>`     | Instantly removes a running container.                                                                 |
| `docker-compose down`                | Tears down all containers, networks, and volumes created by the Compose file.                          |

## Docker Compose Resources and References

* [Overview of Docker Compose](https://docs.docker.com/compose/) in the Docker documentation.
* [Compose file](https://docs.docker.com/compose/compose-file/) in the Docker documentation.
* [Docker Compose](https://github.com/docker/compose) on GitHub.

Further information about the concepts explained in this page can be found in Docker documentation:

* [Environment variables in Compose](https://docs.docker.com/compose/environment-variables/).
* [Overview of docker-compose CLI](https://docs.docker.com/compose/reference/overview/).
* [Compose command-line reference](https://docs.docker.com/compose/reference/).

Content initially contributed by [Vettabase Ltd](https://vettabase.com/).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
