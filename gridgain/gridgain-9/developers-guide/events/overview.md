---
description: >-
  Enable events in GridGain 9 by configuring event channels and sinks, and learn
  the structure of cluster events.
---

# Working with Events

GridGain can generate events for a variety of operations happening in the cluster and notify your application about those operations. There are many types of events, including cache events, node discovery events, distributed task execution events, and many more.

## Enabling Events

### Creating Event Channel

In GridGain 9, events are configured cluster-wide, in [cluster configuration](../../administrators-guide/config/cluster-config.md). Events are organized in *channels*, each channel tracking one or more event types. You cannot enable or disable individual events, instead you need to disable event channels.

To create an event channel:

```bash
cluster config update ignite.eventlog.channels.exampleChannel.events=["USER_AUTHENTICATION_SUCCESS"]
```

This channel will track the `USER_AUTHENTICATION_SUCCESS`, but not trigger yet. For the events to trigger, an event *sink* must be configured. A single event channel can be connected to any number of sinks.

### Creating Event Sink

An event sink handles events and sends them to the user. Here is how you can enable a simple log sink by using the CLI tool:

```bash
cluster config update ignite.eventlog.sinks.exampleSink = {type="log", channel="exampleChannel"}
```

This sink sends the event information to the configured logger category at the configured level. Now, the authorization events will be written to the log. Here is how the event may look like:

```
2024-06-04 16:19:29:840 +0300 [INFO][%defaultNode%sql-execution-pool-1][EventLog] {"type":"USER_AUTHORIZATION_SUCCESS","timestamp":1717507169840,"productVersion":"9.1","user":{"username":"ignite","authenticationProvider":"basic"},"fields":{"privileges":[{"action":"CREATE_TABLE","on":{"objectType":"TABLE","objectName":"TEST2","schema":"PUBLIC"}}],"roles":["system"]}}
```

Here is an example of a REST API event:

```
2026-02-13 15:45:12:123 +0300 [INFO][http-server-worker-1][EventLog] {"type":"REST_API_REQUEST_FINISHED","timestamp":1739453112123,"productVersion":"9.1.19","user":{"username":"admin","authenticationProvider":"basic"},"fields":{"requestId":"a1b2c3d4-e5f6-7890-abcd-ef1234567890","timestamp":"2026-02-13T12:45:12.050Z","method":"GET","endpoint":"/management/v1/cluster/state","nodeName":"node1","status":200,"durationMs":73}}
```

Below is the cluster configuration config in JSON.

{% hint style="info" %}
In GridGain 9, you can create and maintain the configuration in either JSON or HOCON format.
{% endhint %}

```json
{
  "ignite" : {
    "eventlog" : {
        "channels" : [ {
          "enabled" : true,
          "events" : [ "USER_AUTHENTICATION_SUCCESS" ],
          "name" : "exampleChannel"
        } ],
        "sinks" : [ {
          "channel" : "exampleChannel",
          "criteria" : "EventLog",
          "format" : "JSON",
          "level" : "INFO",
          "name" : "sampleSink",
          "type" : "log"
        } ]
    }
  }
}
```

## Event Sinks

### Log Sink

This sink prints information to the log, using the configured logging level.

```json
{
  "ignite" : {
    "eventlog" : {
      "sinks" : [ {
        "name" : "sampleSink",
        "type" : "log",
        "channel" : "exampleChannel",
        "criteria" : "EventLog",
        "format" : "JSON",
        "level" : "INFO"
      } ]
    }
  }
}
```

| Field | Description |
| --- | --- |
| channel | The name of the event channel the data sink logs data for. |
| criteria | Logging criteria. By default, only EventLog messages are logged. |
| format | Output format. Currently, only `JSON` messages are supported. |
| level | The level the messages are posted to the log at. Supported values: `ALL`, `TRACE`, `DEBUG`, `INFO`, `WARNING`, `ERROR`, `OFF`. Default value: `INFO`. |
| name | Arbitrary sink name. |
| type | Type of event sink. Currently, only `log` sink is supported, and is used to write events to log. |

### Webhook Sink

Webhook sink sends event data to an HTTP or HTTPS endpoint. Events from the channel are first put into internal queue, and then batched and sent as JSON arrays via HTTP POST requests.

```json
{
  "ignite" : {
    "eventlog" : {
      "sinks" : [ {
        "name" : "sampleWebhook",
        "type" : "webhook",
        "channel" : "exampleChannel",
        "endpoint" : "http://example.com:443",
        "protocol" : "http/json",
        "batchSize" : 500,
        "batchSendFrequencyMillis" : 5000,
        "queueSize" : 5000,
        "retryPolicy" : {
          "maxAttempts" : 3,
          "initBackoffMillis" : 2000,
          "maxBackoffMillis" : 10000,
          "backoffMultiplier" : 2
        },
        "ssl" : {
          "enabled" : true,
          "clientAuth" : "none",
          "ciphers" : "",
          "keyStore" : {
            "type" : "PKCS12",
            "path" : "/path/to/keystore.p12",
            "password" : "keystorePassword"
          },
          "trustStore" : {
            "type" : "PKCS12",
            "path" : "/path/to/truststore.p12",
            "password" : "truststorePassword"
          }
        }
      } ]
    }
  }
}
```

| Parameter | Default | Description |
| --- | --- | --- |
| `type` |  | Required. Must be `webhook` to use webhook sink. |
| `channel` |  | Required. Name of the event channel. |
| `endpoint` |  | Required. HTTP or HTTPS endpoint in `host:port` format (for example, `example.com:8080`). |
| `protocol` | `http/json` | Protocol for sending events. Only `"http/json"` is supported. |
| `batchSize` | `1000` | Maximum number of events per batch. When this limit is reached, the batch is sent immediately. Minimum value: 1. |
| `batchSendFrequencyMillis` | `10000` | Maximum time to wait before sending a batch in milliseconds. Batches are sent when either this time limit or `batchSize` is reached. Minimum value: 1. |
| `queueSize` | `10000` | Maximum number of events that can be queued. If the queue is full, new events are dropped. Should be higher than `batchSize`. Minimum value: 1. |
| `retryPolicy.maxAttempts` | `2` | Maximum number of retry attempts. 0 means retries are disabled. |
| `retryPolicy.initBackoffMillis` | `1000` | Initial delay in milliseconds before the first retry attempt. Minimum value: 1. |
| `retryPolicy.maxBackoffMillis` | `5000` | Maximum delay in milliseconds between retry attempts. Minimum value: 1. |
| `retryPolicy.backoffMultiplier` | `2` | Multiplier applied to the backoff delay after each failed attempt. Minimum value: 1. |
| `ssl.enabled` | `false` | Defines if SSL is enabled. |
| `ssl.clientAuth` | `none` | Client authentication mode. Possible values: `none`, `optional`, or `require`. |
| `ssl.ciphers` |  | Comma-separated list of ciphers. Empty string uses default ciphers. |
| `ssl.keyStore.type` | `PKCS12` | Keystore type. |
| `ssl.keyStore.path` |  | Path to the keystore file. |
| `ssl.keyStore.password` |  | Password for the keystore. |
| `ssl.trustStore.type` | `PKCS12` | Truststore type. |
| `ssl.trustStore.path` |  | Path to the truststore file. |
| `ssl.trustStore.password` |  | Password for the truststore. |

#### HTTP Request Format

Every HTTP request sent by the webhook sink includes the following headers:

| Header | Description |
| --- | --- |
| `Content-Type` | Always set to `application/json`. |
| `X-SINK-CLUSTER-ID` | The UUID of the Ignite cluster sending the events. |
| `X-SINK-NODE-NAME` | The name of the specific Ignite node that sent the batch. |

#### Expected Response Codes

The webhook endpoint must return the following codes:

- `2xx` (200-299) - Success, batch accepted
- `429` - Too Many Requests
- `502` - Bad Gateway
- `503` - Service Unavailable
- `504` - Gateway Timeout

In case one of the above codes is received, GridGain will attempt to retry sending the batch according to `retryPolicy` configuration.  Any other status code is treated as permanent failure, and no retry attempts are made.

## Event Channels

Event channel configuration in GridGain 9 has the following structure:

```json
{
    "ignite" : {
      "eventlog" : {
        "channels" : [ {
          "enabled" : true,
          "events" : [ "USER_AUTHENTICATION_SUCCESS" ],
          "name" : "exampleChannel"
        } ]
      }
    }
  }
```

| Field | Description |
| --- | --- |
| enabled | Defines if this event channel is enabled. |
| events | The list of events tracked by the event channel. For the full list of event types, see [Events List](events-list.md). |
| name | Arbitrary channel name. |

## Event Structure

All events in GridGain 9 follow the same basic structure described below. Some events provide additional context in the `data` field.

```json
{
  "type": "AUTHORIZATION",
  "user": { "username": "John", "authenticationProvider": "basic" },
  "timestamp": 1715169617,
  "productVersion": "3.0.0",
  "fields": {}
}
```

| Field | Description |
| --- | --- |
| type | The type of the event. For the full list of event types, see [Events List](events-list.md). |
| user | The name of the user, and the [authentication](../../administrators-guide/security/authentication.md) provider used to authorize. |
| timestamp | Even time in UNIX epoch time. |
| productVersion | GridGain version used by the client. |
| fields | Event-specific data. |
