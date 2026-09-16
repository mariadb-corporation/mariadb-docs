---
description: >-
  Restore a GridGain 9 cluster to any point in time within the low watermark
  window with point-in-time recovery (PITR).
---

# Point-in-Time Recovery

{% hint style="info" %}
This feature is only available as a part of GridGain 9 Ultimate edition.
{% endhint %}

By using the point in time recovery (PITR) feature, you can restore cluster status to any point above the [low watermark](../storage/low-watermark.md) point.

GridGain 9 recovers to a point in time only within the low watermark window. There is no roll-forward of changes onto a restored snapshot. To recover to a state older than the low watermark, restore a snapshot taken at or before that point.

## Limitations

- Point in time recovery can only be performed for data above the [low watermark](../storage/low-watermark.md) (600000ms by default). Older data can only be recovered by restoring a [snapshot](snapshots-and-recovery.md).
- Recovery of large amounts of data may require additional storage space, as both versions will be temporarily kept available in case the recovery fails.

{% hint style="warning" %}
Do not run a point-in-time recovery and a snapshot restore at the same time.
{% endhint %}

## Performing Point in Time Recovery

To start point in time recovery, use the `recovery tables start` command and specify the table or tables to recover. Table names can be schema-qualified.

```
recovery tables start --tables Person,PUBLIC.Accounts --timestamp 2024-09-10T10:53:00+01:00
```

Once replication is started, it will return the operation ID.

## Monitoring Recovery

Point in time recovery may take a long time. You can monitor current replication status by using the `recovery tables state` command and passing the ID of data recovery to it:

```
recovery tables state --id=944e4abe-b655-4283-9d78-449b5186a7ac
```
