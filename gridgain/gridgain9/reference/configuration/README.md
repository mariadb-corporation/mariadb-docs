---
description: >-
  How GridGain 9 cluster and node configuration is structured, stored in HOCON
  or JSON, and updated from the CLI at startup and during runtime.
---

# Cluster and Node Configuration

In GridGain 9, configuration is managed using the [CLI utility](../cli-tool.md). Configuration is stored in HOCON format and can be modified both at startup and during runtime.

You can define and maintain configuration in either HOCON or JSON. The configuration file must have a single root node, `ignite`, and all configuration sections are children, grandchildren, etc., of that node.

## Updating Configuration from the CLI

### Viewing Cluster and Node Configuration

To view the cluster configuration, use:

```
cluster config show
```

To view the configuration of the node you're connected to, use:

```
node config show
```

### Updating Cluster and Node Configuration

To update configuration, use the `cluster config update` or `node config update` command with a valid HOCON string.

#### Updating a Single Parameter

Update a single parameter by specifying its path and new value:

```
node config update ignite.network.shutdownTimeoutMillis=20000
```

You can also modify cluster configuration via [non-interactive](../cli-tool.md#non-interactive-cli-mode) CLI mode without starting the tool first.

#### Updating Multiple Parameters

To update multiple parameters, provide a full valid HOCON string. The CLI parses and applies all changes atomically:

```bash
cluster config update "ignite.security.authentication.providers.default.users:{admin_user:{displayName=\"admin\",password=admin_password,passwordEncoding=PLAIN,roles:[system]}}"
```

If applied correctly, new configuration item will appear in `cluster config show` output, in this example:

```
providers {
    default {
        type=basic
        users {
            "admin_user" {
                displayName=admin
                password="********"
                passwordEncoding=PLAIN
                roles=[
                    system
                ]
            }
            ignite {
                displayName=ignite
                password="********"
                passwordEncoding=PLAIN
                roles=[
                    system
                ]
            }
        }
    }
}
```

## Configuration Files

When a node starts, it reads initial configuration from `etc/gridgain-config.conf`. You can modify this file to ensure consistent node startup configuration.

Cluster configuration is distributed and synchronized across all nodes automatically. Use the CLI tool to manage it.

GridGain also loads system-level parameters from `etc/vars.env`. Use this file to configure JVM properties, working directories, and additional arguments through the `GRIDGAIN9_EXTRA_JVM_ARGS` variable.
