---
description: >-
  Install GridGain MCP Server from the ZIP download package or run it as a container image, and run it manually for a first test.
---

# Installing MCP Server

{% hint style="warning" %}
MCP Server is available only with GridGain Ultimate Edition.
{% endhint %}

GridGain MCP Server is a separate download, available from the [GridGain download page](https://www.gridgain.com/resources/download).
The GridGain Ultimate Edition package also contains the server as a single JAR file in its `mcp` folder.

{% hint style="info" %}
You do not install the server into a GridGain node, and you do not run it manually in everyday use.
Your assistant starts the server when needed and stops it when the session ends.
{% endhint %}

## Installing From the Download Package

After you download the archive, unpack it and start the server:

```shell
java -jar gridgain-mcp-<version>.jar
```

The server then waits for requests from an assistant on standard input and does not do anything on its own.

To check that the server can reach your cluster, use the [connection check](operations.md#checking-the-connection) operation.

By default, the server writes the audit log to `~/.gridgain8/mcp/logs/audit.log` in your home folder.

{% hint style="info" %}
The `gridgain-mcp-<version>.jar` file needs the `libs` folder next to it. If you move the JAR file, move the folder with it.
To keep one file, use `standalone/gridgain-mcp-<version>.jar`, which does not need the `libs` folder.
{% endhint %}

## Installing as a Container Image

To run the server in Docker, get the `gridgain/mcp` image. The image works on both the `linux/amd64` and `linux/arm64` platforms.

The following command starts the server:

```shell
docker run -i --rm gridgain/mcp:<version>
```

Make sure to use both options:

- `-i` keeps standard input open. The server talks to the assistant through it, and without it the server stops at once.
- `--rm` removes the container when the session ends.

Unlike the JAR file, the container prints a warning to standard error at once if no volume is mounted for the audit log.
See [Keeping the Audit Log](#keeping-the-audit-log).

The image does not publish any ports by default, and the server runs as user ID 10000, not as root.

You configure the server through environment variables, as described in [Configuring MCP Server](configuration.md).
With Docker, pass them with the `-e` option.

### Reaching the Cluster From a Container

By default, the server connects to `localhost`. Inside a container, that is the container itself and not your machine.
Set `GRIDGAIN_HOST` to the address of your cluster. If the cluster runs on the same machine as Docker:

- On Docker Desktop, use the host name `host.docker.internal`.
- On Linux, add `--add-host=host.docker.internal:host-gateway` to the `docker run` command, or use `--network host`.

### Using Certificates

The server opens its own trust store and key store files, so they must be available inside the container:

- Mount the folder with the stores as read-only.
- Make the files readable by user ID 10000.
- Set the store path settings to the path inside the container, not the path on your machine.

### Keeping the Audit Log

In the container image, the server writes the [audit log](operations.md#audit-log) under `/opt/gridgain-mcp/.gridgain8/mcp/logs`.
Without a volume, you lose the log when you remove the container. To keep it, mount a folder from your machine at this path.

The folder must belong to the user that the container runs as, and be closed to the group and to other users, such as mode `0700`.
This user is user ID 10000, unless you choose another one with `docker run --user`.
Otherwise, the server does not start.

### Example

The following command connects the server to a cluster over TLS and mounts folders for the certificates and the audit log:

```shell
docker run -i --rm \
  -e GRIDGAIN_HOST=host.docker.internal \
  -e GRIDGAIN_USERNAME=mcp_reader \
  -e GRIDGAIN_PASSWORD \
  -e GRIDGAIN_SSL_MODE=REQUIRED \
  -e GRIDGAIN_SSL_TRUSTSTORE_PATH=/etc/gridgain-mcp/certs/truststore.jks \
  -e GRIDGAIN_SSL_TRUSTSTORE_PASSWORD \
  -v /path/to/stores:/etc/gridgain-mcp/certs:ro \
  -v /path/to/audit:/opt/gridgain-mcp/.gridgain8/mcp/logs \
  gridgain/mcp:<version>
```

An `-e` option without a value, such as `-e GRIDGAIN_PASSWORD`, takes the value from the environment of the `docker` command.
This keeps passwords out of the command line.

## Next Steps

- [Connect your assistant to the server](agent-hosts.md)
- [Configure the server](configuration.md)
