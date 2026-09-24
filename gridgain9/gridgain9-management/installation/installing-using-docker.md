---
description: >-
  Run GridGain 9 in Docker containers, including the server and dedicated CLI
  images, and start a cluster with Docker Compose.
---

# Installing Using Docker

## Prerequisites

### Recommended Docker Version

GridGain is tested on the following Docker configuration:

- Docker 26.1.3;
- Docker compose 2.14.2

Docker container environment must follow other system requirements.

### Recommended Operating System

{% include "../../.gitbook/includes/prereqs-os.md" %}

### Recommended Java Version

{% include "../../.gitbook/includes/prereqs-java.md" %}

## Version Lifecycle

The information about versioning and lifecycle of GridGain 9 is available on the [Versioning page](https://www.gridgain.com/versioning-and-support-lifecycle).

## Docker Image Variants

GridGain 9 Docker images are available in several variants based on different JDK versions. The default image tag (`gridgain/gridgain9:9.1`) uses *JDK 25*. If you need a specific JDK version, use the corresponding tag suffix:

| Tag | JDK Version | Support Type |
| --- | --- | --- |
| `9.1` | JDK 25 (default) | LTS |
| `9.1-openjdk21` | JDK 21 | LTS |
| `9.1-openjdk17` | JDK 17 | LTS |
| `9.1-openjdk26` | JDK 26 | STS |

The same variants are available for the CLI image (`gridgain/gridgain9-cli`).

{% hint style="info" %}
GridGain follows the JDK release cadence for short-term support (STS) versions: only the most recent STS image is built and shipped. When the next STS release becomes available, the previous STS image is retired. Long-term support (LTS) images are not affected by this policy.
{% endhint %}

## Running a Node

Run GridGain in a docker container using the `docker run` command. Docker will automatically pull the appropriate GridGain version:

```bash
docker run -d -p 10300:10300 -p 10800:10800 -p 3344:3344 gridgain/gridgain9:9.1
```

{% hint style="info" %}
If you plan to store persistent data, it is recommended to mount a volume for it. Otherwise, data will be deleted when the container is removed.

Consider storing the `/opt/gridgain/work` folder to keep application data and persistent data.
{% endhint %}

This command launches a single GridGain node. After you run the command, you can check if GridGain is running in the container logs.

## Configuring JVM Options

To configure JVM options such as heap size, garbage collection, or Java agents in Docker containers, use the `GRIDGAIN9_EXTRA_JVM_ARGS` environment variable, for example:

```bash
docker run -d \
  -p 10300:10300 -p 10800:10800 -p 3344:3344 \
  -e GRIDGAIN9_EXTRA_JVM_ARGS="-Xms8g -Xmx8g -XX:+UseG1GC" \
  gridgain/gridgain9:9.1
```

## Running a Cluster

You can use the docker-compose file to start an entire cluster in docker. You can download a sample docker-compose file and run a 3-node cluster:

- Download the [docker-compose](../../.gitbook/assets/gg9-quick-start-docker-compose.yml) file.

  {% hint style="info" %}
  Docker compose version 2.23.1 or later is required to use the provided compose file.
  {% endhint %}
- Download the docker image:

  ```bash
  docker pull gridgain/gridgain9:9.1
  ```
- Run the docker compose command.

  ```bash
  docker compose -f docker-compose.yml up -d
  ```

3 nodes will start in docker and will be available from CLI tool that can be run locally. Remember to initialise the cluster from the command line tool before working with it.

## Running CLI Tool in Docker

A dedicated lightweight CLI Docker image is available for managing GridGain 9 clusters. This image is significantly smaller than the full server image and is optimized for cluster administration tasks.

The CLI image includes:

- GridGain 9 CLI tool with all management capabilities;
- Essential utilities: bash, bind-tools (DNS utilities), less (pager), and netcat (network utilities);
- Custom JRE built with all required Java modules;
- Non-root user execution for enhanced security.

### Using the CLI Docker Image

The CLI image can connect to GridGain 9 nodes running in the same Docker network:

```bash
docker run --rm -it --network=gridgain9_default gridgain/gridgain9-cli:9.1
```

This starts the CLI in interactive REPL mode. You can also run one-off commands:

```bash
# Initialize a cluster
docker run --rm --network=gridgain9_default gridgain/gridgain9-cli:9.1 \
  cluster init --url http://node1:10300 --name my-cluster --metastorage-group node1,node2,node3

# Check cluster status
docker run --rm --network=gridgain9_default gridgain/gridgain9-cli:9.1 \
  cluster status --url http://node1:10300

# Run SQL query
docker run --rm --network=gridgain9_default gridgain/gridgain9-cli:9.1 \
  sql --url http://node1:10300 "SELECT * FROM my_table"
```

#### Setting Up an Alias

To simplify CLI commands, you can set up a shell alias:

```bash
alias gridgain-cli='docker run --rm -it --network=gridgain9_default gridgain/gridgain9-cli:9.1'
```

Then use it as:

```bash
gridgain-cli cluster status --url http://node1:10300
```

{% hint style="info" %}
You may need a license file to initialize the cluster. To provide it, mount the license file:

```bash
docker run --rm -it --network=gridgain9_default \
  -v /opt/etc/license.json:/opt/gridgain9cli/license.json \
  gridgain/gridgain9-cli:9.1
```
{% endhint %}

### Using CLI from the Server Image

The full server image also includes the CLI tool. You may want to use it if you only have the server image available.

{% hint style="info" %}
The server image is larger and includes components not needed for CLI operations.
{% endhint %}

- Create a new network with the `network create` command:

  ```bash
  docker network create gridgain-network
  ```
- Add any containers with nodes that are already running to the network:

  ```bash
  docker network connect gridgain-network {container-id}
  ```
- Start the container with the GridGain CLI tool on the same network:

  ```bash
  docker run -it --network=gridgain-network gridgain/gridgain9:9.1 cli
  ```

The CLI will be able to connect to the IP address of the node. If you are not sure what the address is, use the `container inspect` command to check it:

```bash
docker container inspect {container-id}
```

### CLI Tool Work Folder

The CLI tool needs to store some data required for operation as described in the [CLI Tool](../../reference/cli-tool.md) section.

For the dedicated CLI image, data is stored in `/opt/gridgain9cli/work`.

For the server image, data is stored in `/opt/gridgain/work/gridgain9cli`.

You can configure the directory by setting the following environment variables:

- `GRIDGAIN_CLI_WORK_DIR` to configure the directory containing the CLI tool information;
- `GRIDGAIN_WORK_DIR` to configure the GridGain 9 `work` directory, including the CLI tool information;
- `GRIDGAIN_HOME` to configure the home directory of GridGain 9, including all GridGain parameters.

## Software Identification

The GridGain Docker image includes a SWID tag. It is located in `/usr/lib/swidtag/` inside the container.

See [Software Identification](software-identification.md) for details.
