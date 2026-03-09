# Deploy MaxScale with Docker

## Overview

This guide explains how to deploy MariaDB MaxScale using the official Docker image available via the MariaDB Enterprise Registry. MaxScale is a database proxy that offers load balancing, high availability, and security between MariaDB database servers and your applications.

## Prerequisites

Before deploying MaxScale with Docker, ensure the following requirements are met:

* Docker installed and running on your system
* A MariaDB Enterprise subscription
* Your MariaDB Enterprise token and account credentials

## Authenticate to the MariaDB Enterprise Registry

MariaDB Docker images are stored in the private MariaDB Enterprise Docker Registry. To retrieve MaxScale Docker images, you must first authenticate with the MariaDB Enterprise Registry using the Customer Download Token.&#x20;

### **Obtain Customer Download Token**

1. Log in to the [MariaDB Customer Portal](https://id.mariadb.com/).
2. Locate your **Customer Download Token**.
3. Copy the token to use for authentication when logging in to Docker.

As a best practice, ensure that your token is stored securely.

### Log in to Docker Registry

For authentication, use your **Customer Download Token** to the MariaDB Enterprise Registry:

```
echo "<ENTERPRISE_TOKEN>" | docker login docker.mariadb.com -u <your-mariadb.id-email> --password-stdin
```

Replace:

* `<ENTERPRISE_TOKEN>` with your **Customer Download Token**.
* `<your-mariadb.id-email>` with the email associated with your MariaDB account.

## Available Image Tags

The following tags are available for MaxScale Docker image:

| Tag       | Description                    |
| --------- | ------------------------------ |
| `latest`  | Latest stable MaxScale release |
| `25.01`   | MaxScale 25.01.x series        |
| `25.01.1` | MaxScale version 25.01.1       |
| `25.01.2` | MaxScale version 25.01.2       |

Select the appropriate Docker image tag from the `maxscale` repository.

## Pull the MaxScale Image

Pull the `latest` MaxScale image using `docker pull`:

```
docker pull docker.mariadb.com/maxscale:latest
```

Or pull a specific version:

```
docker pull docker.mariadb.com/maxscale:25.01.1
```

## Run MaxScale in a Container

### Basic Example

The default setup of MaxScale, which just activates the REST API, is used by this command:

```
docker run -d -p 8989:8989 --name mxs docker.mariadb.com/maxscale:latest
```

### Quick Start Example

For a quick start that includes database proxy port access:

```
## Authenticate, pull, and run in one sequence
echo "<ENTERPRISE_TOKEN>" | docker login docker.mariadb.com -u <your-mariadb.id-email> --password-stdin
docker pull docker.mariadb.com/maxscale:latest
docker run -d -p 3306:3306 -p 8989:8989 --name mxs docker.mariadb.com/maxscale:latest
```

## Configure MaxScale

MaxScale must be configured to define backend servers, monitoring, routing services, and listeners. For production deployments, you can either use the default basic configuration or provide a custom configuration file.

### Default Configuration

The REST API, which listens on port 8989, is the only feature enabled by the container's minimum default configuration. The default login credentials are:

* Username: `admin`
* Password: `mariadb`

#### Basic Container Setup

Run MaxScale with default configuration using `docker run`:

```
docker run -d -p 3306:3306 -p 8989:8989 --name mxs docker.mariadb.com/maxscale:latest
```

**Parameters**:

* `-d`: Run container in detached mode
* `--name mxs`: Container name "mxs"
* `-p 3306:3306`: Map database proxy port
* `-p 8989:8989`: Map REST API port

After launching the container, test the REST API `using curl`:

{% code fullWidth="true" %}
```
curl -u admin:mariadb http://localhost:8989/v1/maxscale
```
{% endcode %}

### Using a Custom Configuration File

Before starting the container:

1. Create a directory on your system to store the configuration file.
2. Place `your-maxscale.cnf` file in this directory.
3. The container will mount this directory in order to enable persistent configuration.

Create a custom MaxScale configuration file and mount it into the container:

```
docker run -d -p 8989:8989 --name mxs -v /path/to/your-maxscale.cnf:/etc/maxscale.cnf.d/custom.cnf docker.mariadb.com/maxscale:latest
```

### Overriding the Default Configuration

If you need to modify the maxscale section, override the main configuration file:

{% code fullWidth="true" %}
```
docker run -d -p 8989:8989 --name mxs -v /path/to/your-maxscale.cnf:/etc/maxscale.cnf.d docker.mariadb.com/maxscale:latest
```
{% endcode %}

## Access the Container

To access the running the container's shell:

```
docker exec -it mxs bash
```

## Verify MaxScale is Running

After starting the container, verify that MaxScale is running correctly. Check the container status by executing the below command:

```
docker ps --filter "name=mxs"
```

## Managing the Container

### Stop the Container

To stop the running container, use:

```
docker stop mxs
```

### Remove the Container

Delete the container after use with the following command:

```
docker rm mxs
```
