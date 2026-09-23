---
description: >-
  How GridGain 9 clients and servers upgrade independently, the compatibility
  model between versions, and the recommended client-upgrade procedure.
---

# Client Upgrade

GridGain clients and servers upgrade independently of each other: the cluster can be upgraded without touching client applications, and clients can be upgraded without touching the cluster.

## Compatibility Model

### Server-Reported Product Version

On every successful connection, the server reports its running GridGain product version to the client. Application code can read this version per connection. A client connected to multiple nodes during a rolling upgrade may observe different product versions per connection.

### Optional Feature Flags

Clients and servers advertise their supported optional features when a connection is established. The connection operates with the intersection — the features both client and server support — for its lifetime. Newer clients can connect to older servers, but features the older server does not advertise are not available on that connection. An older client connected to a newer server likewise sees only the features both sides understand.

When application code attempts to use an optional feature that the server has not advertised, the call fails with `IgniteClientFeatureNotSupportedByServerException` naming the feature.

See [Client Features](../../developers-guide/clients/overview.md#client-features) for the list of features supported by the client.

## Compatibility Scenarios

### Client and Server on the Same Version

Always works. All features that the client supports are supported on both sides.

### Client Newer Than Server

The connection operates on the mutually supported feature set, which excludes any features the newer client supports but the server does not. Calls into those features fail with `IgniteClientFeatureNotSupportedByServerException`. All other operations work normally.

### Client Older Than Server

The connection operates on the mutually supported feature set, which is what the older client supports. New server-only features are invisible to the older client.

### Client Connected During a Server-Side Rolling Upgrade

The cluster runs in mixed-version state during a rolling upgrade. Connections to different nodes may report different product versions and advertise different feature sets. Existing client connections to nodes that are restarted will drop, and the client will reconnect to a different node.

## Recommended Client-Upgrade Procedure

### Upgrade the Cluster First

Upgrade the cluster before rolling out new client versions in your applications. Older clients continue to work against newer servers — they operate on the older client's feature set — so you can stagger client-side updates over your own deployment cadence.

A newer client connected to an older server may fail when application code uses features the older server does not yet advertise. Upgrading the cluster first avoids this.

### Roll Out Client Updates Application-by-Application

Replace the client artifact in each application as part of its normal deployment process. There is no cluster-side coordination required for a client upgrade.

### Plan for Reconnection During Cluster Upgrades

Long-lived client connections will drop when the node they are connected to restarts. Applications must be prepared to reconnect as required.
