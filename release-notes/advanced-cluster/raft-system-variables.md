---
description: >-
  A detailed reference for the system variables used by the RAFT consensus
  implementation. These variables configure cluster heartbeat behavior, election
  timeouts, log management, and flow control
---

# RAFT System Variables

## List of RAFT System Variables

### raft-candidate-timeout

Initial timeout for candidate waiting for votes during election (milliseconds). Uses exponential backoff up to raft\_max\_candidate\_timeout.

| Property     | Value             |
| ------------ | ----------------- |
| Command Line |                   |
| Scope        | Global            |
| Dynamic      | No                |
| Data Type    | Numeric (ms)      |
| Range        | 100 to 4294967295 |
| Default      | 200               |

### raft-data-dir

Data directory where to store replication logs and other node persistent state.

| Property     | Value  |
| ------------ | ------ |
| Command Line |        |
| Scope        | Global |
| Dynamic      | No     |
| Data Type    | String |
| Range        |        |
| Default      | ./     |

### raft-event-store-file-size

Maximum size of single log file in bytes. When a log file reaches this size, a new file is created.

| Property     | Value                                  |
| ------------ | -------------------------------------- |
| Command Line |                                        |
| Scope        | Global                                 |
| Dynamic      | No                                     |
| Data Type    | Numeric (Bytes)                        |
| Range        | 1048576 (1 MB) to 1048576000 (1000 MB) |
| Default      | 128MB                                  |

### raft-event-store-max-memory

Maximum size of the in-memory event store buffer in bytes. Events are cached in memory for faster access before being written to disk.

| Property     | Value                                    |
| ------------ | ---------------------------------------- |
| Command Line |                                          |
| Scope        | Global                                   |
| Dynamic      | No                                       |
| Data Type    | Numeric (Bytes)                          |
| Range        | 1048576 (1 MB) to 10485760000 (10000 MB) |
| Default      | 32MB                                     |

### raft-event-store-max-size

Maximum total size of the event store on disk in bytes. Older log files are purged when this limit is exceeded.

| Property     | Value                                        |
| ------------ | -------------------------------------------- |
| Command Line |                                              |
| Scope        | Global                                       |
| Dynamic      | No                                           |
| Data Type    | Numeric (Bytes)                              |
| Range        | 1048576 (1 MB) to 1048576000000 (1000000 MB) |
| Default      | 512MB                                        |

### raft-flow-control-drift-limit

Maximum index drift allowed between nodes before flow control throttling activates. When the difference between the slowest and fastest node commit positions exceeds this limit, the leader begins throttling requests.

| Property     | Value           |
| ------------ | --------------- |
| Command Line |                 |
| Scope        | Global          |
| Dynamic      | Yes             |
| Data Type    | Numeric         |
| Range        | 0 to 4294967295 |
| Default      | 100             |

### raft-flow-control-max-throttle-rate

Maximum request rate (requests per second) to sustain when flow control throttling is active. Lower values provide more aggressive throttling.

| Property     | Value           |
| ------------ | --------------- |
| Command Line |                 |
| Scope        | Global          |
| Dynamic      | Yes             |
| Data Type    | Numeric         |
| Range        | 0 to 4294967295 |
| Default      | 100             |

### raft-follower-timeout

Time follower waits without leader messages before starting election (milliseconds). Should be significantly larger than raft\_heartbeat\_timeout to avoid unnecessary elections.

| Property     | Value             |
| ------------ | ----------------- |
| Command Line |                   |
| Scope        | Global            |
| Dynamic      | No                |
| Data Type    | Numeric (ms)      |
| Range        | 500 to 4294967295 |
| Default      | 5000              |

### raft-heartbeat-timeout

Interval at which leader sends heartbeat messages (milliseconds). Shorter intervals provide faster failure detection but increase network traffic.

| Property     | Value             |
| ------------ | ----------------- |
| Command Line |                   |
| Scope        | Global            |
| Dynamic      | No                |
| Data Type    | Numeric (ms)      |
| Range        | 100 to 4294967295 |
| Default      | 1000              |

### raft-listen-port

Port to listen for incoming cluster connections.

| Property     | Value          |
| ------------ | -------------- |
| Command Line |                |
| Scope        | Global         |
| Dynamic      | No             |
| Data Type    | Numeric (Port) |
| Range        | 0 to 65535     |
| Default      | 50002          |

### raft-log-filter

In order to reduce amount of logging on DEBUG level, this filter can be used to select output from specific operations. The format is comma separated list of strings, e.g. 'rvc\_send,rvc\_recv'. The actual useful values for filter depend on underlying Craft implementation and is subject to change.

| Property     | Value                                    |
| ------------ | ---------------------------------------- |
| Command Line |                                          |
| Scope        | Global                                   |
| Dynamic      | Yes                                      |
| Data Type    | String                                   |
| Range        |                                          |
| Default      | admin,client,server,replication\_service |

### raft-log-level

Verbosity level for logging. Supported values are ERROR, WARN, INFO and DEBUG. The DEBUG setting may get very verbose, so it should be used sparingly (see also raft\_log\_filter).

| Property     | Value                    |
| ------------ | ------------------------ |
| Command Line |                          |
| Scope        | Global                   |
| Dynamic      | Yes                      |
| Data Type    | Enumeration              |
| Range        | ERROR, WARN, INFO, DEBUG |
| Default      | INFO                     |

### raft-max-candidate-timeout

Maximum candidate timeout after exponential backoff (milliseconds). Limits how long a candidate will wait between election attempts.

| Property     | Value             |
| ------------ | ----------------- |
| Command Line |                   |
| Scope        | Global            |
| Dynamic      | No                |
| Data Type    | Numeric (ms)      |
| Range        | 100 to 4294967295 |
| Default      | 1500              |

### raft-max-reconnect-attempts

Number of attempts to reconnect to the cluster after ending up in non-primary state.

| Property     | Value           |
| ------------ | --------------- |
| Command Line |                 |
| Scope        | Global          |
| Dynamic      | Yes             |
| Data Type    | Numeric         |
| Range        | 1 to 4294967295 |
| Default      | 5               |

### raft-node-id

Unique node identifier. The identifier can be either a human-readable string up to 15 characters long or a UUID. If human-readable name is used, it must be unique within the cluster. If another node with the same name already exists in the cluster, the newly added node will fail connecting the cluster. The special value 'auto' is reserved for generating a UUID whenever the server starts from a clean state. This is mainly useful for test scenarios where the grastate.dat is removed, and the node is expected to rejoin the cluster before the previous instance is evicted from the group.

| Property     | Value                                        |
| ------------ | -------------------------------------------- |
| Command Line |                                              |
| Scope        | Global                                       |
| Dynamic      | No                                           |
| Data Type    | String                                       |
| Range        | Human-readable string (max 15 chars) or UUID |
| Default      | auto                                         |

### raft-node-weight

Node weight for replication and voting quorum. The default weight is 1, all nodes in the cluster have the same weight in voting and replication.&#x20;

{% hint style="danger" %}
**PRODUCTION WARNING:** Using unequal weights in a cluster is unsafe for production workloads. Weighted quorum does not guarantee that data is replicated on the majority of servers before log events are committed on the leader, which can lead to data loss scenarios. This setting is mainly useful for testing and should not be used in production.
{% endhint %}

| Property     | Value    |
| ------------ | -------- |
| Command Line |          |
| Scope        | Global   |
| Dynamic      | No       |
| Data Type    | Numeric  |
| Range        | 1 to 256 |
| Default      | 1        |

### raft-non-primary-timeout

Timeout after which the node is considered to be in non-primary state. If no replication events appear in the log within this time period, the node will be considered to be in non-primary state (seconds).

| Property     | Value             |
| ------------ | ----------------- |
| Command Line |                   |
| Scope        | Global            |
| Dynamic      | No                |
| Data Type    | Numeric (seconds) |
| Range        | 1 to 4294967295   |
| Default      | 20                |

### raft-session-timeout

Timeout after which session to replication system is considered expired if there is no activity. If the node cannot communicate with the leader within this time period, it will be evicted from the cluster (seconds).

| Property     | Value             |
| ------------ | ----------------- |
| Command Line |                   |
| Scope        | Global            |
| Dynamic      | No                |
| Data Type    | Numeric (seconds) |
| Range        | 1 to 4294967295   |
| Default      | 15                |

### raft-sst-listen-port

Port to listen for SST requests.

| Property     | Value          |
| ------------ | -------------- |
| Command Line |                |
| Scope        | Global         |
| Dynamic      | No             |
| Data Type    | Numeric (Port) |
| Range        | 0 to 65535     |
| Default      | 50001          |

### raft-have-ssl

Indicates whether SSL/TLS is enabled for cluster communication. Possible values are YES, NO, DISABLED, or VERIFY\_PEER. This is a read-only variable that reflects the current SSL state.

| Property     | Value                           |
| ------------ | ------------------------------- |
| Command Line |                                 |
| Scope        | Global                          |
| Dynamic      | No                              |
| Data Type    | Enumeration                     |
| Range        | YES, NO, DISABLED, VERIFY\_PEER |
| Default      | NO                              |

### raft-ssl-key

Path to the SSL private key file in PEM format. This variable is read-only and must be set at server startup.

| Property     | Value   |
| ------------ | ------- |
| Command Line |         |
| Scope        | Global  |
| Dynamic      | No      |
| Data Type    | String  |
| Range        |         |
| Default      | (empty) |

### raft-ssl-cert

Path to the SSL certificate file in PEM format. This variable is read-only and must be set at server startup.

| Property     | Value   |
| ------------ | ------- |
| Command Line |         |
| Scope        | Global  |
| Dynamic      | No      |
| Data Type    | String  |
| Range        |         |
| Default      | (empty) |

### raft-ssl-ca

Path to the CA certificate file in PEM format used to verify peer certificates. This variable is read-only and must be set at server startup.

| Property     | Value   |
| ------------ | ------- |
| Command Line |         |
| Scope        | Global  |
| Dynamic      | No      |
| Data Type    | String  |
| Range        |         |
| Default      | (empty) |

### raft-ssl-capath

Path to a directory containing CA certificate files in PEM format. This variable is read-only and must be set at server startup.

| Property     | Value   |
| ------------ | ------- |
| Command Line |         |
| Scope        | Global  |
| Dynamic      | No      |
| Data Type    | String  |
| Range        |         |
| Default      | (empty) |

### raft-ssl-cipher

OpenSSL cipher list for TLS 1.2 and below. Uses OpenSSL cipher string format. This variable is read-only and must be set at server startup.

| Property     | Value   |
| ------------ | ------- |
| Command Line |         |
| Scope        | Global  |
| Dynamic      | No      |
| Data Type    | String  |
| Range        |         |
| Default      | (empty) |

### raft-ssl-crl

Path to the Certificate Revocation List (CRL) file. This variable is read-only and must be set at server startup.

| Property     | Value   |
| ------------ | ------- |
| Command Line |         |
| Scope        | Global  |
| Dynamic      | No      |
| Data Type    | String  |
| Range        |         |
| Default      | (empty) |

### raft-ssl-crlpath

Path to a directory containing Certificate Revocation List files. This variable is read-only and must be set at server startup.

| Property     | Value   |
| ------------ | ------- |
| Command Line |         |
| Scope        | Global  |
| Dynamic      | No      |
| Data Type    | String  |
| Range        |         |
| Default      | (empty) |

### raft-tls-version

Comma-separated list of allowed TLS protocol versions. Supported values include TLSv1.2 and TLSv1.3. Default includes both TLSv1.2 and TLSv1.3. This variable is read-only and must be set at server startup.

| Property     | Value            |
| ------------ | ---------------- |
| Command Line |                  |
| Scope        | Global           |
| Dynamic      | No               |
| Data Type    | String           |
| Range        | TLSv1.2, TLSv1.3 |
| Default      | TLSv1.2,TLSv1.3  |

### raft-ssl-ciphersuites

List of permitted TLS 1.3 ciphersuites. This is separate from raft\_ssl\_cipher which applies to earlier TLS versions. This variable is read-only and must be set at server startup.

| Property     | Value   |
| ------------ | ------- |
| Command Line |         |
| Scope        | Global  |
| Dynamic      | No      |
| Data Type    | String  |
| Range        |         |
| Default      | (empty) |

### raft-ssl-verify-depth

Maximum depth for certificate chain verification. This variable is read-only and must be set at server startup.

| Property     | Value           |
| ------------ | --------------- |
| Command Line |                 |
| Scope        | Global          |
| Dynamic      | No              |
| Data Type    | Numeric         |
| Range        | 0 to 4294967295 |
| Default      | 9               |
