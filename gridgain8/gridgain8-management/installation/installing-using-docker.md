---
description: >-
  How to run GridGain in Docker: pulling the image, running in-memory and
  persistent clusters, providing configuration and license files, and enabling modules.
---

# Installing Using Docker

## Considerations

### In-memory vs. Persistent Cluster

When deploying a persistent GridGain cluster, you should always mount a persistent volume or local directory.
If you do not use a persistent volume, GridGain stores the data in the container's file system.
It means that the data is erased when you remove the container.
To save the data in a permanent location, [mount a persistent volume](#running-persistent-cluster).

### Networking

By default, GridGain docker image exposes the following ports: 11211, 47100, 47500, 49112.
You can expose more ports as needed by adding `-p <port>` to the `docker run` command.
For example, to connect a thin client to the node running inside a docker container, open port 10800:

```shell
docker run -d -p 10800:10800 \
-e LICENCE_URL=http://myserver/license.xml \
gridgain/enterprise
```

## Downloading GridGain Docker Image

Assuming that you already have Docker installed on your machine, you can pull and run the GridGain Docker image using the following commands.

Open a command shell and use the following command to pull the GridGain Docker image.

```shell
docker pull \
gridgain/enterprise
```

{% hint style="info" %}
Starting with version 8.8.21, docker images do not include a licence. You must specify the valid licence URL with the `LICENCE_URL` parameter.
{% endhint %}

By default, the latest version is downloaded but you can download a specific version too.

```shell
# Pull a specific GridGain version
docker pull gridgain/enterprise:8.10
```

For GridGain Ultimate Edition, use `gridgain/ultimate`.

## Running In-Memory Cluster

Run GridGain in a docker container using the `docker run` command.

```shell
docker run -d \
-e LICENCE_URL=http://myserver/license.xml \
gridgain/enterprise
```

This command launches a single GridGain node.

To run a specific version of GridGain, use the following command:

```shell
docker run -d \
-e LICENCE_URL=http://myserver/license.xml \
gridgain/enterprise:8.10
```

After you run the command, you can check if GridGain is running in the container logs.

## Running Persistent Cluster

If you use [Native Persistence](../../architecture/storage/native-persistence.md), GridGain stores the user data under the default work directory (`{IGNITE_HOME}/work`) in the file system of the container.
This directory is erased if you restart the docker container.
To avoid this, you can:

- Use a persistent volume to store the data; or
- Mount a local directory

These two options are described in the following sections.

### Using Persistent Volume

To create a persistent volume, run the following command:

```shell
docker volume create persistence-volume
```

We mount this volume to a specific directory when running the GridGain docker image.
This directory will have to be passed to GridGain.
You can do this in two ways:

- By using the `IGNITE_WORK_DIR` system property;
- In the [node configuration file](../../architecture/storage/native-persistence.md#enabling-persistent-storage).

The following command launches the GridGain Docker image and passes the work directory to GridGain:

```shell
docker run -d \
  -v persistence-volume:/persistence \
  -e IGNITE_WORK_DIR=/persistence \
  -e LICENCE_URL=http://myserver/license.xml \
  gridgain/enterprise
```

The following command passes a configuration file from your file system to the docker image:

```shell
docker run -d \
  -v /local/dir/config.xml:/config-file.xml \
  -e CONFIG_URI=/config-file.xml \
  -e LICENCE_URL=http://myserver/license.xml \
  gridgain/enterprise
```

### Using Local Directory

Instead of creating a volume, you can mount a local directory to the container in which the GridGain image is running and use this directory to store persistent data.
When restarting the container with the same command, GridGain loads the data from the directory.

```shell
mkdir work_dir

docker run -d \
  -v ${PWD}/work_dir:/persistence \
  -e IGNITE_WORK_DIR=/persistence \
  -e LICENCE_URL=http://myserver/license.xml \
  gridgain/enterprise
```

The `-v` option mounts a local directory under the `/persistence` path in the container.
The `-e IGNITE_WORK_DIR=/persistence` option tells GridGain to use this folder as the work directory.

## Providing Configuration File

When you run the image, it starts a node with the default configuration file. You can pass a custom configuration file by using the `CONFIG_URI` environment variable:

```shell
docker run -d \
  -e CONFIG_URI=http://myserver/config.xml \
  -e LICENCE_URL=http://myserver/license.xml \
gridgain/enterprise
```

You can also use a file from your local file system.
Mount the file first under a specific path inside the container by using the `-v` option.
Then, use this path in the `CONFIG_URI` option:

```shell
docker run -d \
  -v /local/dir/config.xml:/config-file.xml \
  -e CONFIG_URI=/config-file.xml \
  -e LICENCE_URL=http://myserver/license.xml \
  gridgain/enterprise
```

## Deploying User Libraries

When starting, a node adds all libraries found in the `{IGNITE_HOME}/libs` directory to the classpath (ignoring the "optional" directory).
If you want to deploy user libraries, you can mount a directory from your local machine to a path in the `/opt/gridgain/libs/` in the container by using the `-v` option.

The following command mounts a directory on your machine to `libs/user_libs` in the container.
All files located in the directory are added to the classpath of the node.

```shell
docker run -d \
  -v /local_path/to/dir_with_libs/:/opt/gridgain/libs/user_libs \
  -e LICENCE_URL=http://myserver/license.xml \
  gridgain/enterprise
```

Another option is to use the `EXTERNAL_LIBS` variable if your libraries are available via an URL.

```shell
docker run -d \
  -e "EXTERNAL_LIBS=http://url_to_your_jar" \
  -e LICENCE_URL=http://myserver/license.xml \
  gridgain/enterprise
```

## Providing License File

If you use GridGain Enterprise or Ultimate Edition, you need to provide your license file when launching nodes.
The license file can be specified using the 'LICENCE_URL' variable.

```shell
docker run -d \
  -e LICENCE_URL=http://myserver/license.xml  \
  gridgain/enterprise:8.10
```

If you license file is stored locally, use the following syntax:

```shell
docker run -d -v {absolute_path}/gridgain-license.xml:/opt/gridgain/gridgain-license.xml \
 -e "OPTION_LIBS=ignite-rest-http,control-center-agent" \
 gridgain/ultimate:8.10
```

## Enabling Modules

To enable specific [modules](../../gridgain8-usage/setup.md#enabling-modules), specify their names in the `OPTION_LIBS` system variable as follows:

```shell
docker run -d \
  -e "OPTION_LIBS=ignite-rest-http,ignite-aws" \
  -e LICENCE_URL=http://myserver/license.xml \
  gridgain/enterprise
```

By default, GridGain Docker image starts with the following modules enabled:

- ignite-log4j,
- ignite-spring,
- ignite-indexing,
- ignite-opencensus.

## Environment Variables

The following parameters can be passed as environment variables in the docker container:

| Parameter Name | Description | Default |
|---|---|---|
| `CONFIG_URI` | URL to the GridGain configuration file (can also be relative to the META-INF folder on the class path). The downloaded configuration file is saved to `./ignite-config.xml` | N/A |
| `OPTION_LIBS` | A list of [modules](../../gridgain8-usage/setup.md#enabling-modules) that will be enabled for the node. | ignite-log4j, ignite-spring, ignite-indexing |
| `JVM_OPTS` | JVM arguments passed to the GridGain instance. | N/A |
| `EXTERNAL_LIBS` | A list of URL's to external libraries. Refer to [Deploying User Libraries](#deploying-user-libraries). | N/A |
| `LICENCE_URL` | URL to the licence file. A licence is required when you run the GridGain Ultimate or Enterprise Editions. | N/A |

## Software Identification

The GridGain Docker image includes a SWID tag. It is located at `/opt/gridgain/swid/gridgain.swidtag` inside the Docker container.

See [Software Identification](../software-identification.md) for details.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
