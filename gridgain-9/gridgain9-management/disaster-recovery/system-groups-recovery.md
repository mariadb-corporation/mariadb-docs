---
description: >-
  Disaster recovery operations for GridGain 9 system RAFT groups — recovering the
  Cluster Management Group and the Metastorage Group after permanent majority loss.
---

# Disaster Recovery for System Groups

A GridGain 9 cluster includes two system RAFT groups, both of which are essential for the cluster's normal operation:

- [Cluster Management Group (CMG)](../../architecture/cluster-lifecycle.md#cluster-management-group)
- [Metastorage Group (MG)](../../architecture/cluster-lifecycle.md#cluster-metastorage-group)

You perform _disaster recovery_ operations on _system RAFT groups_ to recover permanent _majority loss_. When a system RAFT group loses majority, it becomes unavailable. When CMG is unavailable, the cluster itself remains available with limitations: it can still process most of the operations, but it cannot join new nodes, start/restart existing nodes, and start building new indexes. When MG is unavailable, the cluster becomes unusable; it cannot handle even GET/PUT/SQL requests.

{% hint style="info" %}
Disaster recovery for [data partitions](data-recovery.md) is described in a separate page.
{% endhint %}

You can also check the state of the groups with the [`cluster system-groups`](#checking-system-group-state) command. You see that the majority has been lost in cluster logs in the console or in the [rotated log files](https://en.wikipedia.org/wiki/Log_rotation). When a RAFT group becomes unavailable, the logs would show something like
`Send with retry timed out [retryCount = 11, groupId = cmg_group].`
or
`Send with retry timed out [retryCount = 11, groupId = metastorage_group].`.

An indicator that CMG is down is when a node does not start after a `restart` command. This is reflected in the log as `Local CMG state recovered, starting the CMG`, not followed by `Successfully joined the cluster`.

If a node tries to start when CMG is available, but MG is not, the log shows `Metastorage info on start` not followed by `Performing MetaStorage recovery`.

{% hint style="danger" %}
Exercise caution when applying disaster recovery commands to system node groups. These commands might result in _split brain_ (split your cluster into two clusters). Use the recovery commands as the last resort, only if the majority for CMG/MG is lost permanently.
{% endhint %}

{% hint style="info" %}
When authorization is enabled, `recovery cluster reset` requires the `RESET_CLUSTER` privilege, and `recovery cluster migrate` requires the `MIGRATE_CLUSTER` privilege on the old cluster, the one that `--old-cluster-url` points to. Without the privilege, the request fails with HTTP status `403`. See [User Permissions and Roles](../../security/user-permissions-and-roles.md#cluster-management).
{% endhint %}

## Checking System Group State

Before you apply any recovery command, check which nodes hold the leader of each system group and whether the group still has a quorum. You can use this information to restart only the leader of a stuck group instead of the whole cluster, and to confirm that a majority is actually lost before you run `recovery cluster reset`.

The state of the system groups is available from the CLI and from the REST API. Both work when a group has no leader or no quorum, and on a node that has not joined the cluster yet.

| Task | CLI command | REST endpoint |
|---|---|---|
| State of the CMG and MG RAFT nodes on every node, with a summary per group | [`cluster system-groups`](../../reference/cli-tool.md#cluster-system-groups) | `GET /management/v1/cluster/system-groups` |
| State of the CMG and MG RAFT nodes on one node, as that node sees it | [`node system-groups`](../../reference/cli-tool.md#node-system-groups) | `GET /management/v1/node/system-groups` |

For example:

```bash
cluster system-groups --url http://localhost:10301
```

The `cluster system-groups` request is sent to one node, which asks every node of the physical topology for the state of its CMG and MG RAFT nodes. A node that does not answer is reported with an error and does not stop the others from being listed.

### Node Rows

The table has one row for each system group on each node.

| Column | Description |
|---|---|
| `node` | Node name. |
| `group` | `CMG` or `METASTORAGE`. |
| `role` | Role of the RAFT node on this node, for example `LEADER`, `FOLLOWER`, `CANDIDATE`, or `LEARNER`. |
| `term` | Current RAFT term of the node. |
| `leader` | Name of the leader this node knows of. Empty if the node knows none. |
| `leaderless for` | How long this node has not known a leader. Empty if it knows one. |
| `last log index` | Index of the last entry in the local RAFT log. |
| `peers` | Voting members in the latest group configuration this node has seen. |

A node that is not a member of a group has no row for it. A node that answered but is a member of no system group is shown as one row with `no system group replicas`.

A row whose `role` column starts with `ERROR: <reason>` means the state could not be read. The reason is followed by a message for a human reader. Match on the reason, not on the message, because the message can change between versions.

| Reason | Meaning |
|---|---|
| `LOCK_HELD` | The RAFT node of the group held its lock for too long, so it is stuck even though its node answers. The role is shown on a best-effort basis; a learner is shown as `FOLLOWER`. Other groups on the same node are still read. |
| `NO_ANSWER` | The node did not return its states in time. |
| `UNREACHABLE` | The request could not be delivered to the node. |
| `VERSION_UNKNOWN` | There is no connection to the node, so it is unknown whether its version supports the request. |
| `UNSUPPORTED_VERSION` | The version of the node does not support the request. |
| `NODE_STOPPING` | The node is stopping. |
| `INTERNAL_ERROR` | Any other failure. Treat a reason that is not in this list as `INTERNAL_ERROR`. |

### Group Summary

Below the table, `cluster system-groups` prints one line for each group.

| Summary | Meaning |
|---|---|
| `leader <node>, term <n>, quorum confirmed (k of n voters reported following the leader)` | The leader of the highest reported term has been read, claims leadership, and a majority of the voters report following it. |
| `... QUORUM NOT CONFIRMED ...` | The answers do not confirm that a majority follows the leader. This does not mean the group has no quorum: voters that did not answer may still follow the leader. |
| `... leader's own state not read ...` | The voters are taken from the member with the highest term and the longest log, because the leader did not answer. The counts then depend on that member's view of the configuration. |
| `CONFLICTING LEADERS in term <n>: ...` | More than one node claims leadership in the same term. RAFT allows one leader per term, so the answers contradict each other. Treat the group as unconfirmed. |
| `NO LEADER, highest term <n>, leaderless for up to <duration>` | No node reporting the highest term knows a leader, or the node they name does not claim leadership. In the second case the rows can show a leader that the summary does not confirm. |
| `missing voters: <node> <reason>` | Voters whose state is unknown. The reason is `NOT_IN_TOPOLOGY` (the node is not in the physical topology), `NO_RAFT_NODE` (the node answered but runs no RAFT node of the group), or `NOT_READ` (the state could not be read; the error reason follows in parentheses). |
| `VOTERS UNKNOWN, unread nodes: ...` | The state of the group could not be read on any node, so the voters are unknown. The unread nodes are listed with their error reasons. |
| `NO REPLICA FOUND: no queried node runs a <group> Raft node` | Nodes answered, but none of them runs a RAFT node of this group. |

Learners are not counted as voters. The summary counts voters of the latest configuration only, so during a membership change it does not account for the voters of the old configuration.

{% hint style="info" %}
The CLI waits up to 60 seconds for the cluster-wide answer. A node waits for each node it asks for 1 second per system group plus 5 seconds, which is 7 seconds with the two system groups, before it reports that node as `NO_ANSWER`. To change this wait, set the `GG_RAFT_STATUS_RESPONSE_TIMEOUT_MILLIS` system property on the node that handles the request. If you set it higher than the CLI wait, the CLI reports a timeout instead of the node that did not answer.
{% endhint %}

### Example: Majority Lost

In a three-node cluster where `n2` and `n3` are both down, the remaining node `n1` has no leader for either group. Nodes that already left the physical topology are not listed in the table and show up as `NOT_IN_TOPOLOGY` in the summary:

```
╔══════╤═════════════╤══════════╤══════╤════════╤════════════════╤════════════════╤════════════╗
║ node │ group       │ role     │ term │ leader │ leaderless for │ last log index │ peers      ║
╠══════╪═════════════╪══════════╪══════╪════════╪════════════════╪════════════════╪════════════╣
║ n1   │ CMG         │ FOLLOWER │ 1    │        │ 26s            │ 11             │ n2, n3, n1 ║
╟──────┼─────────────┼──────────┼──────┼────────┼────────────────┼────────────────┼────────────╢
║ n1   │ METASTORAGE │ FOLLOWER │ 1    │        │ 25s            │ 248            │ n2, n1, n3 ║
╚══════╧═════════════╧══════════╧══════╧════════╧════════════════╧════════════════╧════════════╝

CMG: NO LEADER, highest term 1, leaderless for up to 26s; voters as reported by the member with the highest term and log; missing voters: n2 NOT_IN_TOPOLOGY, n3 NOT_IN_TOPOLOGY
METASTORAGE: NO LEADER, highest term 1, leaderless for up to 25s; voters as reported by the member with the highest term and log; missing voters: n2 NOT_IN_TOPOLOGY, n3 NOT_IN_TOPOLOGY
```

A node that is down but still in the physical topology is shown as a row with `ERROR: VERSION_UNKNOWN`, because the node the command is sent to has no connection to it. In that case the summary reports it as `missing voters: <node> NOT_READ (VERSION_UNKNOWN)`. The group keeps its confirmed quorum as long as a majority of the voters reports following the leader.

### Using the REST API

Both the `GET /management/v1/cluster/system-groups` and `GET /management/v1/node/system-groups` endpoints return JSON. The cluster endpoint returns a `nodes` list, ordered by node name, with the data of the table rows, and a `groups` list with one summary for each system group.

```bash
curl http://localhost:10300/management/v1/cluster/system-groups
```

Each summary has these fields:

| Field | Description |
|---|---|
| `group` | The system group, `CMG` or `METASTORAGE`. |
| `leader` | Name of the leader of the highest term reported. Absent if the voters are unknown, if no member reporting that term knows a leader, or if the node they name does not claim leadership. |
| `conflictingLeaders` | Names of the nodes that claim leadership in the highest term, if more than one does. Empty unless the answers contradict each other. |
| `term` | Highest term reported by any member. `0` if `votersKnown` is `false`. |
| `voters` | Names of the voting members of the group, from the leader or, if its own state was not read, from the member with the highest term and the longest log. Only the latest configuration counts. Empty if `votersKnown` is `false`. |
| `votersKnown` | `false` if no member's state of the group could be read. Then `voters` and `missingVoters` are empty. |
| `votersFromLeader` | `true` if the voters are the peers that the leader itself reported. `false` if there is no leader or its own state was not read. |
| `votersFollowingLeader` | Number of voters, the leader included, that reported following the leader in its term. `0` if there is no leader. |
| `missingVoters` | Voters whose state is unknown, each with a `nodeName`, a `reason` (`NOT_IN_TOPOLOGY`, `NO_RAFT_NODE`, or `NOT_READ`), and, for `NOT_READ`, the `error`. Empty if `votersKnown` is `false`. |
| `unreadNodes` | Empty unless `votersKnown` is `false`. Then it lists the queried nodes whose state could not be read, each with a `nodeName` and an `error`. It can include nodes that are not voters. |
| `quorumConfirmed` | `true` if the answers confirm that a majority of the voters follows the leader. `false` means the quorum is not confirmed, not that the group has none. |
| `longestLeaderlessDurationMs` | Longest time, in milliseconds, that any voter whose state was read has not known a leader. |

The node endpoint returns a single entry of the `nodes` list for the node it is sent to. Durations are in milliseconds.

Each group state in the `nodes` list also has a `learners` list, the learners in the latest group configuration the node has seen. The CLI table does not show it.

The full schemas are in the OpenAPI specification of the management API.

## Cluster Management Group

If CMG loses majority:

1. Restart CMG nodes to restore the lost majority.
2. If the above fails, forcefully assign a new majority using the following [CLI command](../../reference/cli-tool.md#disaster-recovery-commands) (manually or via REST): `recovery cluster reset --url=<node-url> --cluster-management-group=<new-cmg-nodes>`.

   The command is sent to the node indicated by the `--url` parameter, which must belong to the `new-cmg-nodes` RAFT group. This node becomes the _Repair Conductor_, and it initiates the `reset` procedure.

   The above procedure might fail for the following reasons:

   - Some of the nodes specified in `new-cmg-nodes` are not in the physical topology.
   - The Repair Conductor does not have all the information it needs to start the procedure.
3. If some nodes were down or were unavailable due to a network partition (and hence did not participate in the repair):
   1. Start these nodes (or restore network connectivity and restart them).
   2. Migrate these nodes to the repaired cluster using the following [CLI command](../../reference/cli-tool.md#disaster-recovery-commands) (manually or via REST): `recovery cluster migrate --old-cluster-url=<url-of-old-cluster-node> --new-cluster-url=<url-of-new-cluster-node>`.

## Metastorage Group

If MG loses majority:

1. Restart MG nodes (or at least their RAFT nodes inside GridGain nodes).
2. If the above fails:
   1. Make sure that every node that could be started had started and joined the cluster.
   2. Forcefully assign a new majority using the following [CLI command](../../reference/cli-tool.md#disaster-recovery-commands) (manually or via REST): `recovery cluster reset --url=<existing-node-url> [--cluster-management-group=<new-cmg-nodes>] --metastorage-replication-factor=N`.

      `N` is the requested number of the voting RAFT nodes in the MG after repair. If you omit `--cluster-management-group`, the command takes the current CMG voting members set from the CMG leader; if CMG is not available, the command fails.

      The command is sent to the node specified by `--url`. This node becomes the _Repair Conductor_, and it initiates the `reset` procedure.

      If the Repair Conductor fails to repair MG, the procedure has to be repeated manually (there is no failover).
3. If some nodes were down or were unavailable due to a network partition (and hence did not participate in the repair):
   1. Start these nodes (or restore network connectivity and restart them).
   2. Migrate these nodes to the repaired cluster using the following [CLI command](../../reference/cli-tool.md#disaster-recovery-commands) (manually or via REST): `recovery cluster migrate --old-cluster-url=<url-of-old-cluster-node> --new-cluster-url=<url-of-new-cluster-node>`.

{% hint style="info" %}
If one of the nodes has a revision in its metastorage that is not present on any of the nodes that had participated in the repair, this means that its metastorage has diverged from the MG leader's metastorage. Such a node will not be allowed to join the cluster. Its startup will fail with `MetastorageDivergedException (error code META-7)`. Remove the data from the above metastorage-divergent node and have it join the cluster as a blank node.
{% endhint %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
