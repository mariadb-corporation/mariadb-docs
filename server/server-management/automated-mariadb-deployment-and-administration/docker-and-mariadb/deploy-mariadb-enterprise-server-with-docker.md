---
description: >-
  Instructions for deploying MariaDB Enterprise Server using the official
  enterprise Docker images, including handling license keys and entitlements.
---

# Deploy MariaDB Enterprise Server with Docker

MariaDB Corporation provides Docker images for MariaDB Enterprise Server in the [MariaDB Enterprise Docker Registry](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md).

Docker provides multiple benefits:

* Docker is an open platform for developing, shipping, and running applications that allows you to separate your applications from your infrastructure.
* Docker images are portable. A Docker image can be deployed in a Docker container on any system using the Docker platform, regardless of the host operating system.
* Docker containers are isolated from the host operating system and from other Docker containers.

If you want to deploy MariaDB Enterprise Server without Docker, alternative deployment methods are available.

## Use Cases

MariaDB Enterprise Server can be deployed with Docker to support use cases that require software to be rapidly deployed on existing infrastructure, such as:

* Continuously create and destroy automated testing environments as part of a continuous integration (CI) pipeline
* Create a small test environment on a local workstation
* Create multiple isolated test environments on the same host
* Deployment alongside related containers using Docker Compose

## Compatibility

The following products and versions can be deployed using the MariaDB Enterprise Docker Registry:

* MariaDB Enterprise Server 11.8
* MariaDB Enterprise Server 11.4
* MariaDB Enterprise Server 10.6

For details about which storage engines and plugins are supported in the images for each version, see "[MariaDB Enterprise Docker Registry](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md)".

## Deploy Enterprise Server in a Docker Container

To deploy MariaDB Enterprise Server in a Docker container, follow the instructions below.

### Step 1: Retrieve Customer Download Token

MariaDB Corporation requires customers to authenticate when logging in to the MariaDB Enterprise Docker Registry. A customer-specific Customer Download Token must be provided as the password.

Customer Download Tokens are available through the MariaDB Customer Portal.

To retrieve the customer download token for your account:

1. Navigate to the Customer Download Token at the MariaDB Customer Portal.
2. Log in using your MariaDB ID.
3. Copy the Customer Download Token to use as the password when logging in to the MariaDB Enterprise Docker Registry.

### Step 2: Log In to Docker Registry

Log in to the MariaDB Enterprise Docker Registry by executing `docker login`:

```bash
$ docker login docker.mariadb.com
```

When prompted, enter the login details:

* As the user name, enter the email address associated with your MariaDB ID.
* As the password, enter your Customer Download Token.

The login details will be saved.

Confirm the login details were saved by checking the /.docker/config.json file for a JSON object named "docker.mariadb.com" inside an "auths" parent JSON object:

```bash
$ cat ~/.docker/config.json
```

```json
{
   "auths": {
      "docker.mariadb.com": {
         "auth": "<auth_hash>"
      }
   }
}
```

### Step 3: Choose an Image Tag

The `enterprise-server` repository in the MariaDB Enterprise Docker Registry contains images for different MariaDB Enterprise Server releases using specific tags. Before continuing, you will need to decide which tag to use.

To deploy a container using the most recent image for the latest MariaDB Enterprise Server release series (currently 11.8), use the `latest` tag.

For additional information, see "[MariaDB Enterprise Docker Registry: Tags](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md#tags)".

### Step 4: Pull Docker Image

Pull the Docker image with the chosen tag by executing `docker pull`:

```bash
docker pull docker.mariadb.com/enterprise-server:latest
```

```
latest: Pulling from enterprise-server
5d87d5506868: Pull complete
Digest: sha256:68795ca747901e3402e30dab71d6d8bc72bce727db3b9e4888979468be77d250
Status: Downloaded newer image for docker.mariadb.com/enterprise-server:latest
docker.mariadb.com/enterprise-server:latest
```

Confirm the Docker image has been pulled by executing `docker images`:

```bash
docker images \
   --filter=reference='docker.mariadb.com/enterprise-server'
```

```
REPOSITORY                             TAG       IMAGE ID       CREATED        SIZE
docker.mariadb.com/enterprise-server   latest    dd17291aa340   3 months ago   451MB
```

### Step 5: Create a Container

Create a container using the pulled Docker image by executing `docker run`:

```bash
docker run --detach \
   --name mariadb-es-latest \
   --env MARIADB_ROOT_PASSWORD='YourSecurePassword123!' \
   --publish '3307:3306/tcp' \
   docker.mariadb.com/enterprise-server:latest \
   --log-bin=mariadb-bin \
   <other mariadbd command-line options>
```

```
3082ab69e565be21c6157bb5a3d8c849ec03a2c51576778ac417a8a3aa9e7537
```

* Configure the container and set the root password using environment variables by setting the `--env` command-line option.
* Configure TCP port bindings for the container by setting the `--publish` or `--publish-all` command-line options.
* Configure MariaDB Enterprise Server by setting mariadbd command-line options.

Confirm the container is running by executing `docker ps`:

```bash
docker ps \
   --all \
   --filter ancestor='docker.mariadb.com/enterprise-server:latest'
```

```
CONTAINER ID   IMAGE                                         COMMAND                  CREATED          STATUS                      PORTS      NAMES
3082ab69e565   docker.mariadb.com/enterprise-server:latest   "/es-entrypoint.sh -…"   12 seconds ago   Up 11 seconds               3306/tcp   mariadb-es-latest
```

By default, Docker uses Docker bridge networking for new containers. For details on how to use host networking for new containers, see "Create a Container with Host Networking".

### Step 6: Connect to Container

Connect to the container by executing MariaDB Client on the container using docker exec:

```bash
docker exec --interactive --tty \
   mariadb-es-latest \
   mariadb \
   --user=root \
   --password
```

Confirm the container is using the correct version of MariaDB Enterprise Server by querying the version system variable with the SHOW GLOBAL VARIABLES statement:

```sql
SHOW GLOBAL VARIABLES
   LIKE 'version'\G
```

```
*************************** 1. row ***************************
Variable_name: version
        Value: 11.8.3-1-MariaDB-enterprise-log
```

Exit the container using `exit`:

```bash
exit
```

```
Bye
```

### Step 7: Stop Container

Stop a Docker container using `docker stop`:

```bash
docker stop mariadb-es-latest
```

```
mariadb-es-latest
```

Confirm the container is stopped by executing `docker ps`:

```bash
docker ps \
   --all \
   --filter ancestor='docker.mariadb.com/enterprise-server:latest'
```

```
CONTAINER ID   IMAGE                                         COMMAND                  CREATED         STATUS                            PORTS       NAMES
3082ab69e565   docker.mariadb.com/enterprise-server:latest   "/es-entrypoint.sh -…"   2 minutes ago   Exited (143) About a minute ago               mariadb-es-latest
```

### Step 8: Remove Container

Remove a Docker container using `docker rm`:

```bash
docker rm mariadb-es-latest
```

```
mariadb-es-latest
```

Confirm the container is removed by executing docker ps:

```bash
docker ps \
   --all \
   --filter ancestor='docker.mariadb.com/enterprise-server:latest'
```

```
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
