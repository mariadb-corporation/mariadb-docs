---
description: >-
  Install GridGain MCP Server from the ZIP download package or run it as a container image, and run it by hand for a first test.
---

# Installing MCP Server

GridGain MCP Server is a separate download. You do not install it into a GridGain node.
You can run it from the download package or as a container image.

You do not start the server yourself in everyday use.
Your assistant starts it when needed and stops it when the session ends.
The commands on this page show how to run the server by hand, which is useful for the first test.

## Installing From the Download Package

The package is a ZIP archive named `gridgain-mcp-<version>.zip`.
It requires Java 17 or later.

1. Unpack the archive.
2. Check the contents of the unpacked folder:

   | Item | Description |
   | ---- | ----------- |
   | `gridgain-mcp-<version>.jar` | The server. It needs the `libs` folder next to it. |
   | `libs/` | The libraries that the server loads. Keep this folder next to the JAR file. If you move the JAR file, move this folder with it. |
   | `standalone/gridgain-mcp-<version>.jar` | The same server as a single JAR file. It does not need the `libs` folder, so you can copy it anywhere. |
   | `licenses/` | The license notices of the third-party libraries. |
   | `gridgain-eula.txt` | The license agreement that governs the download. |
   | `swidtag/` | The software identification tag for asset management tools. |

3. Start the server:

   ```shell
   java -jar gridgain-mcp-<version>.jar
   ```

The server waits for requests from an assistant on standard input and does not print anything on its own.
Press `Ctrl+C` to stop it.
To check that the server can reach your cluster, use the [connection check](operations.md#checking-the-connection) instead.

{% hint style="info" %}
If you start the JAR file without its `libs` folder, the server fails with `NoClassDefFoundError`. Use the single JAR from the `standalone` folder if you want to keep one file.
{% endhint %}

## Installing as a Container Image

The image name is `gridgain/mcp`. One image tag works on both `linux/amd64` and `linux/arm64`.

```shell
docker run -i --rm gridgain/mcp:<version>
```

Use both options:

- `-i` keeps standard input open. The server talks to the assistant through it, and without it the server stops at once.
- `--rm` removes the container when the session ends.

The image does not publish any ports, and the server runs as a non-root user (user ID 10000).
Everything you put after the image name goes to the server as its own arguments.

You set the server through environment variables, as described in [Configuring MCP Server](configuration.md).
With Docker, pass them with the `-e` option.

### Reaching the Cluster From a Container

By default, the server connects to `localhost`. Inside a container, that is the container itself and not your machine.
Set `GRIDGAIN_HOST` to the address of your cluster. If the cluster runs on the same machine as Docker:

- On Docker Desktop, use the host name `host.docker.internal`.
- On Linux, add `--add-host=host.docker.internal:host-gateway` to the `docker run` command, or use `--network host`.

### Using Certificates

The server opens its trust store and key store files, so they must be available inside the container:

- Mount the folder with the stores as read-only.
- Make the files readable by user ID 10000.
- Set the store path settings to the path inside the container, not the path on your machine.

### Keeping the Audit Log

In the container image, the server writes the [audit log](operations.md#audit-log) under `/opt/gridgain-mcp/.gridgain8/mcp/logs`.
When you run the JAR file, the log is in your home folder by default, as described in [Operating MCP Server](operations.md#audit-log).
Without a volume, you lose the log when you remove the container.
To keep it, mount a folder from your machine at this path.
The folder must belong to user ID 10000 and be closed to the group and to other users, such as mode `0700`.
Otherwise, the server does not start.

If no volume is mounted, the container prints a warning to standard error and starts anyway.

### Example

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

The `-e` options without a value, such as `-e GRIDGAIN_PASSWORD`, take the value from the environment of the `docker` command.
This keeps passwords out of the command line.

## Next Steps

- [Connect your assistant to the server](agent-hosts.md)
- [Configure the server](configuration.md)
