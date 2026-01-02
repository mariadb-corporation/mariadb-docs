---
description: >-
  Automate recovery after primary failure. This guide explains how to use the
  master_reconnection parameter to seamlessly move client connections to a new
  primary server.
---

# Reconnecting to the Primary Server with MaxScale's Read/Write Split Router

The Read/Write Split Router (readwritesplit) routes write queries to the primary server and load balances read-only queries between one or more replica servers. If the primary server fails, then the router can automatically reconnect existing client connections to the new primary server.

## Configuring Automatic Primary Server Re-connection

1. Configure automatic primary server re-connection by configuring several parameters for the Read/Write Split Router in maxscale.cnf.

| Parameter             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| master\_reconnection  | • When this parameter is enabled, if the primary server fails and if master\_failure\_mode is not set to fail\_instantly, then existing client connections will be automatically reconnected to the new primary server. • This parameter is disabled by default.                                                                                                                                                                                                                                                                                            |
| master\_failure\_mode | • This parameter defines how client connections are handled when the primary server fails. • This parameter must be set to either fail\_on\_write or error\_on\_write to allow automatic primary server reconnection. • When this parameter is set to fail\_on\_write, the client connection is closed if a write query is received when no primary is available. • When this parameter is set to error\_on\_write, if no primary server is available and a write query is received, an error is returned stating that the connection is in read-only mode. |

For example:

```
[split-router]
type                     = service
router                   = readwritesplit
...
master_reconnection            = true
master_failure_mode            = fail_on_write
```

2. Restart the MaxScale instance.

```
$ sudo systemctl restart maxscale
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
