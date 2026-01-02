---
description: >-
  Mask failovers from applications. Configure transaction_replay to
  automatically re-execute interrupted transactions on a new primary server
  without returning errors.
---

# Replaying Transactions with MaxScale's Read/Write Split Router

The [Read/Write Split Router (readwritesplit)](../../reference/maxscale-routers/maxscale-readwritesplit.md) routes write queries to the primary server and load balances read-only queries between one or more replica servers. If a server fails, then the router may need to replay in-progress transactions on a different server.

## Session Command History

The [Read/Write Split Router (readwritesplit)](../../reference/maxscale-routers/maxscale-readwritesplit.md) maintains connection state on replica servers by keeping a session command history. If the router has to create a new connection, then it replays these session commands from the previous connection on the new connection.

## Minimizing Memory Usage of Session Command History

The session command history can require a lot of memory if connections are long-lived. In these cases, there are two options to limit memory usage:

* Configure a maximum size for the session command history
* Disable the session command history. This option is not recommended, because you would lose out on the benefits of the session command history.

### Configuring Transaction Replay

1. Configure transaction replay by configuring several parameters for the Read/Write Split Router in `maxscale.cnf`.

| Parameter                                | Description                                                                                                                                                                                                                                                                                                                     |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| transaction\_replay                      | • When this parameter is enabled, transactions will be replayed if they are interrupted. It also implicitly enables the delayed\_retry and master\_reconnection parameters. • When this parameter is disabled, interrupted transactions will cause the client connection to be closed. • This parameter is disabled by default. |
| transaction\_replay\_max\_size           | • The maximum size of the transaction cache for each client connection. The unit is bytes, but EIC binary prefixes (Ki, Mi, Gi, and Ti) and SI prefixes (k, M, G, and T) can also be specified. • The default value is 1 MiB.                                                                                                   |
| transaction\_replay\_attempts            | • The maximum number of attempts to make when replaying a transaction. • The default value is 5.                                                                                                                                                                                                                                |
| transaction\_replay\_retry\_on\_deadlock | • When this parameter is enabled, transactions will be replayed if a deadlock occurs. • When this parameter is disabled, the client will receive an error if a deadlock occurs. • This parameter is disabled by default.                                                                                                        |

For example:

```
[split-router]
type                     = service
router                   = readwritesplit
...
transaction_replay                   = true
transaction_replay_max_size          = 10Mi
transaction_replay_attempts          = 10
transaction_replay_retry_on_deadlock = true
```

2. Restart the MaxScale instance.

```
$ sudo systemctl restart maxscale
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
