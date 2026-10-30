---
description: >-
  Track the system and user time GridGain 8 spends on transactions, and configure
  logging thresholds and sampling for long-running transactions.
---

# Tracking System and User Time Spent on Transactions

You can track the amount of _system_ or _user_ time spent on transactions:

- System time is the time spent on system activities: acquiring locks, "get/put" operations, preparing, committing, and so on.
- User time is the time spent on user activities (calculations, and so on) that run on a client node as part of a transaction. User time is the total time minus the system time.

You can configure logging to include information about transactions that exceed a threshold execution timeout. You can also configure logging to include a random sampling of some percentage of all completed transactions. These thresholds are set via [Related JMX Parameters and JVM Options](#related-jmx-parameters-and-jvm-options).

The log records for long-running transactions look like this:

{% code title="Log" %}
```text
[2019-08-09 13:39:49,130][WARN ][sys-stripe-1-#101%client%]
[root] Long transaction time dump [startTime=13:39:47.970, totalTime=1160, systemTime=157,
userTime=1003, cacheOperationsTime=141, prepareTime=15, commitTime=0, tx=GridNearTxLocal [...]]
```
{% endcode %}

Log records with a random sampling of completed transactions look like this:

{% code title="Log" %}
```text
[2019-08-09 13:39:54,079][INFO ][sys-stripe-2-#102%client%]
[root] Transaction time dump [startTime=13:39:54.063, totalTime=15, systemTime=6,
userTime=9, cacheOperationsTime=2, prepareTime=3, commitTime=0, tx=GridNearTxLocal [...]]
```
{% endcode %}

Also, GridGain logging can be configured so that some transactions are skipped in order to not overflow the log, through a process called log throttling. In those cases, information about log throttling looks like this:

{% code title="Log" %}
```text
[2019-08-09 13:39:55,109][INFO ][sys-stripe-0-#100%client%][root]
Transaction time dumps skipped because of log throttling: 2
```
{% endcode %}

## Related JMX Parameters and JVM Options

JMX parameters and JVM options used to control the system and user time tracking behavior:

### Long-Running Query Threshold

**JVM option**: `IGNITE_LONG_TRANSACTION_TIME_DUMP_THRESHOLD`

**JMX parameter**: `TransactionsMXBean.longTransactionTimeDumpThreshold`

Threshold timeout in milliseconds for long transactions. If a transaction exceeds it, it is dumped to the log with information about how much time it spent in system time and user time. The default value is 0. No information about system/user time of long transactions is dumped to the log if this parameter is not set.

### Sampling Percentage

**JVM option**: `IGNITE_TRANSACTION_TIME_DUMP_SAMPLES_COEFFICIENT`

**JMX parameter**: `TransactionsMXBean.transactionTimeDumpSamplesCoefficient`

This is the coefficient for samples of completed transactions that are dumped to the log. It must be a float value between 0.0 and 1.0 inclusive. The default value is 0.0.

**JVM option**: `IGNITE_TRANSACTION_TIME_DUMP_SAMPLES_PER_SECOND_LIMIT`

**JMX parameter**: `TransactionsMXBean.transactionTimeDumpSamplesPerSecondLimit`

The limit of samples of completed transactions that are dumped to the log per second, *if* `IGNITE_TRANSACTION_TIME_DUMP_SAMPLES_COEFFICIENT` is above 0.0. It must be an integer value greater than 0. The default value is `5`.

Log throttling and information about skipped transactions are tied to the limit set by `TransactionsMXBean.transactionTimeDumpSamplesPerSecondLimit`. For example, say you have 100 transactions per second, and you want to sample just a part of them, maybe 50%. So you set the percentage to 0.5 via `TransactionsMXBean.transactionTimeDumpSamplesCoefficient`. Now 50 transactions per second are sampled in the log.

Now suppose you realize you don't need to see that many, so you set the limit to 15 via `TransactionsMXBean.transactionTimeDumpSamplesPerSecondLimit`. Now the log shows a maximum of 15 transactions per second, and also that 35 were skipped because of log throttling.

## Related Metrics

Metrics used to monitor system and user time for a single node:

- `TransactionMetricsMxBean.totalNodeSystemTime`: Total transactions system time on the node.
- `TransactionMetricsMxBean.totalNodeUserTime`: Total transactions user time on the node.
- `TransactionMetricsMxBean.nodeSystemTimeHistogram`: Transactions system times on the node, represented as a histogram.
- `TransactionMetricsMxBean.nodeUserTimeHistogram`: Transactions user times on the node, represented as a histogram.

Histogram metrics are exported as JSON strings, and typically look like this:

{% code title="JSON" %}
```json
{
  "bounds":
    [1,2,4,8,16,25,50,75,100,250,500,750,1000,3000,5000,10000,25000,60000],
  "values":
    [
      {"fromExclusive":0,"toInclusive":1,"value":0},
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
{% endcode %}

For information about JSON histograms, see [Working with Histograms](../../reference/monitoring/generic-metrics.md#histograms).
