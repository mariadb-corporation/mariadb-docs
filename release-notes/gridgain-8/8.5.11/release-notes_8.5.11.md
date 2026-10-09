---
description: >-
  GridGain 8.5.11 adds tracking of system and user time spent on transactions,
  a new clustername REST command, and communication message transmission time
  statistics, along with a number of bug fixes.
hidden: true
---

# GridGain 8.5.11 Release Notes

## What's New in This Release

### Introduction

This release introduces several new features and includes a number of bug fixes.

## New Feature: Tracking System and User Time Spent on Transactions

You can track the amount of *System* or *User* time spent on transactions:

- System time is the time that is spent for system activities: time spent while acquiring locks, "get/put" operations, preparing, committing, etc.
- User time is the time that is spent for user activities (calculations, etc.) that are run on the node as part of a transaction. User time is the total time minus the system time.

You can configure logging to include information about transactions that exceed a threshold execution timeout. You can also configure logging to include a random sampling of some percentage of all completed transactions. These thresholds are set via [Related JMX Parameters and JVM Options](#related-jmx-parameters-and-jvm-options). The information about transactions will be added to the *logs on the node where transactions are executed*.

The log records for long-running transactions look like this:

```text
[2019-08-09 13:39:49,130][WARN ][sys-stripe-1-#101%client%]
[root] Long transaction time dump [startTime=13:39:47.970, totalTime=1160, systemTime=157,
userTime=1003, cacheOperationsTime=141, prepareTime=15, commitTime=0, tx=GridNearTxLocal [...]]
```

Log records with a random sampling of completed transactions look like this:

```text
[2019-08-09 13:39:54,079][INFO ][sys-stripe-2-#102%client%]
[root] Transaction time dump [startTime=13:39:54.063, totalTime=15, systemTime=6,
userTime=9, cacheOperationsTime=2, prepareTime=3, commitTime=0, tx=GridNearTxLocal [...]]
```

Also, Ignite logging can be configured so that some transactions can be skipped in order to not overflow the log, through a process called Log Throttling. In those cases, information about log throttling looks like this:

```text
[2019-08-09 13:39:55,109][INFO ][sys-stripe-0-#100%client%][root]
Transaction time dumps skipped because of log throttling: 2
```

### Related JMX Parameters and JVM Options

JMX parameters and JVM options used to control the system and user time tracking behavior:

#### Long-Running Query Threshold

*JVM option*: `IGNITE_LONG_TRANSACTION_TIME_DUMP_THRESHOLD`

*JMX parameter*: `TransactionsMXBean.longTransactionTimeDumpThreshold`

Threshold timeout in milliseconds for long transactions. If a transaction exceeds it, it will be dumped in the log with information about how much time it spent in system time and user time. Default value is 0. No information about system/user time of long transactions is dumped to the log if this parameter is not set.

#### Sampling Percentage

*JVM option*: `IGNITE_TRANSACTION_TIME_DUMP_SAMPLES_COEFFICIENT`

*JMX parameter*: `TransactionsMXBean.transactionTimeDumpSamplesCoefficient`

This is the coefficient for samples of completed transactions that will be dumped to the log. Must be a float value between 0.0 and 1.0 inclusive. Default value is 0.0.

*JVM option*: `IGNITE_TRANSACTION_TIME_DUMP_SAMPLES_PER_SECOND_LIMIT`

*JMX parameter*: `TransactionsMXBean.transactionTimeDumpSamplesPerSecondLimit`

The limit of samples of completed transactions that will be dumped to the log per second. Must be an integer value greater than 0. Default value is `5`.

Log throttling and information about skipped transactions are tied to the limit set by `TransactionsMXBean.transactionTimeDumpSamplesPerSecondLimit`. For example, say you have 100 transactions per second, and you want to sample just a part of them, maybe 50%. So you set the percentage to 0.5 via `TransactionsMXBean.transactionTimeDumpSamplesCoefficient`. Now 50 transactions per second will be sampled in the log.

Now suppose you realize you don't need to see that many, so you set the limit to 15 via `TransactionsMXBean.transactionTimeDumpSamplesPerSecondLimit`. Now the log will show a maximum of 15 transactions per second, and also that 35 were skipped because of log throttling.

### Related Metrics

New metrics used to monitor system and user time for a single node:

- `TransactionMetricsMxBean.totalNodeSystemTime`: Total transactions system time on node.
- `TransactionMetricsMxBean.totalNodeUserTime`: Total transactions user time on node.
- `TransactionMetricsMxBean.nodeSystemTimeHistogram`: Transactions system times on node represented via histogram.
- `TransactionMetricsMxBean.nodeUserTimeHistogram`: Transactions user times on node represented via histogram.

Histogram metrics are exported as JSON strings and look like this:

```json
{
  "bounds":
    [1,2,4,8,16,25,50,75,100,250,500,750,1000,3000,5000,10000,25000,60000],
  "values":
    [
      {"fromInclusive":0,"toInclusive":1,"value":0},
      {"fromExclusive":1,"toInclusive":2,"value":0},
      {"fromExclusive":2,"toInclusive":4,"value":0},
      {"fromExclusive":4,"toInclusive":8,"value":0},
      {"fromExclusive":8,"toInclusive":16,"value":0},
      {"fromExclusive":16,"toInclusive":25,"value":0},
      {"fromExclusive":25,"toInclusive":50,"value":0},
      {"fromExclusive":50,"toInclusive":75,"value":2},
      {"fromExclusive":75,"toInclusive":100,"value":0},
      {"fromExclusive":100,"toInclusive":250,"value":0},
      {"fromExclusive":250,"toInclusive":500,"value":0},
      {"fromExclusive":500,"toInclusive":750,"value":0},
      {"fromExclusive":750,"toInclusive":1000,"value":0},
      {"fromExclusive":1000,"toInclusive":3000,"value":1},
      {"fromExclusive":3000,"toInclusive":5000,"value":0},
      {"fromExclusive":5000,"toInclusive":10000,"value":0},
      {"fromExclusive":10000,"toInclusive":25000,"value":0},
      {"fromExclusive":25000,"toInclusive":60000,"value":0},
      {"fromExclusive":60000,"value":0}
    ]
}
```

In the histogram, "bounds" is metadata, separate from the actual time values, and is used to break the spectrum of data values into buckets. For example, in the histogram above, if a datapoint/value for System Time is `1500` milliseconds, it will fall into the `1000 - 3000` bucket and result in the "value" for that bucket being incremented (`"value":1`).

### System Warnings

System warnings for long-running transactions now include information about the current system and user time spent on the transaction:

```text
[2019-08-09 14:10:31,835][WARN ][grid-timeout-worker-#122%client%][root] First 10 long running transactions [total=1]
[2019-08-09 14:10:31,835][WARN ][grid-timeout-worker-#122%client%][root] >>> Transaction [startTime=14:10:31.170, curTime=14:10:31.750, systemTime=32, userTime=548, tx=GridNearTxLocal [...]]
```

## New REST API command: clustername

The `clustername` command returns the name of the cluster if it's configured or the autogenerated ID otherwise.

```shell
$ curl http://localhost:8080/ignite?cmd=clustername
{"successStatus":0,"sessionToken":null,"error":null,"response":"1b4ce8a1d61-25c0dec2-8aa3-4773-a708-5c512f489d5e"}
```

## New Feature: Tracking Communication Message Transmission Time

You can get statistics on the amount of time communication messages take between the nodes. This can help identify network problems in your environment. The transmission time is the time from when a message is sent to another node till this node receives a response.

The statistics is available as an attribute of the following JMX-bean.

```
group=SPIs,name=TcpCommunicationSpi,attribute=OutMetricsByNodeByMsgClass
```

The attribute returns the statistics that is grouped by node ID and the type of messages, and the value is represented as a histogram.

Transmission time statistics is disabled by default. To enable it, use the following JVM option:

```shell
-DIGNITE_ENABLE_MESSAGES_TIME_LOGGING=true
```

You can define the buckets' size of the histogram using the following JVM option:

```shell
-DIGNITE_COMM_SPI_TIME_HIST_BOUNDS="10, 20, 40, 80, 160, 320, 500, 1000, 2000, 4000"
```

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

## Fixed Issues

### GridGain Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-24640 | Communication | Added cache messages network time histograms. |
| GG-24639 | SQL | Additional sql mixed processing benchmark. |
| GG-24628 | Storage Engine | Hide sensible data in case of CorruptedTreeException. |
| GG-24623 | SQL | SQL: Added IGNITE.INDEXES system view |
| GG-24616 | Deployment | Improvement search classes when peer class loading enabled. |
| GG-24611 | SQL | Sql 'IN' clause use proper index instead full_scan. |
| GG-24520 | SQL | Added information about cache name, group name and index name into logging of CorruptedTreeException. |
| GG-24496 | Control.(sh\|bat) | Control utility: start time, end time and duration of operation were added to output. |
| GG-24323 | Transactions | Fixed assertion error in preparing state transaction. |
| GG-24322 | Storage Engine | Improved diagnostic info in case of assertion error in page memory. |
| GG-24321 | Transactions | Added ability to track system and user time for transactions. |
| GG-24319 | Control.(sh\|bat) | Cluster name was added to prompt message on cluster deactivation from control utility. |

### GridGain Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-24672 | Snapshot utility | Archive and parallelism parameters added to snapshot scheduling arguments in snapshot utility. |
| GG-24569 | Visor | Visor: Added possibility to configure timeout of long operations. |

## Related Information

### We Value Your Feedback

The GridGain documentation team is focused on constantly improving the product documentation. Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
