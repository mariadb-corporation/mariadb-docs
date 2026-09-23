---
description: >-
  GridGain 9.1.9 adds support for WebAssembly compute jobs and the ability to drop cached SQL plans from the CLI.
---

# GridGain 9.1.9 Release Notes

## Overview

GridGain 9.1.9 is a private release that fixes the known issue from the previous release and provides support for WASM compute jobs.

## New Features

### Support for WebAssembly Computing

{% hint style="warning" %}
This is an experimental API. This API can be changed in subsequent releases.
{% endhint %}

This release provides support for using [WebAssembly](https://webassembly.org/) compute jobs in GridGain 9, expanding the options for creating computing jobs. You can compile your code to WebAssembly and then load the binaries as [deployment units](../../developers-guide/code-deployment/code-deployment.md) and execute the code on cluster nodes.

The example below shows how you can execute your code, and assumes it is already deployed to the cluster:

```java
try (IgniteClient client = IgniteClient.builder()
        .addresses("127.0.0.1:10800")
        .build()
) {

    IgniteCompute compute = client.compute();

    JobExecutionOptions jobOptions = JobExecutionOptions.builder()
            .executorType(JobExecutorType.WASM_EMBEDDED)
            .build();

    JobDescriptor<String, String> helloDesc = JobDescriptor.<String, String>builder(HELLO_FUNC)
            .units(DEPLOYMENT_UNIT)
            .options(jobOptions)
            .build();

    JobTarget target = JobTarget.anyNode(client.cluster().nodes());

    String helloRes = compute.execute(target, helloDesc, "World");
    System.out.println("Wasm job result: " + helloRes);

}
```

For step-by-step instructions, see [WebAssembly Compute Jobs](../../developers-guide/compute/wasm.md) documentation.

### Dropping SQL Plans

{% hint style="warning" %}
This is an experimental API. This API can be changed in subsequent releases.
{% endhint %}

When executing SQL queries, GridGain caches execution plans and reuses them for later queries. These plans may become outdated as data is updated on the cluster. This release adds a new CLI command that can be used to drop a cache for an individual table, or multiple tables at the same time.

The example below invalidates the cache for a single table:

```
sql planner invalidate-cache --tables=PUBLIC.Person
```

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-28771 | Cluster Storage Engine | Fixed an issue that made it impossible to add new values to arrays in configuration. |
| IGN-28671 | General | You can no longer create a distribution zone that would not include any nodes. |
| IGN-28486 | Cluster SQL Engine | You can now drop SQL plans from CLI. |
| IGN-28349 | Cluster SQL Engine | Improved row estimation for all JOIN type operations to improve SQL performance. |
| IGN-27839 | Code Deployment | You can now load deployment unit code from files on node startup. |
| GG-45105 | Cluster SQL Engine | Updated parquet from version 1.15.2 to version 1.16.0 and iceberg from version 1.9.2 to version 1.10.0. |
| GG-44960 | Cluster Storage Engine | Fixed rare cases where table with secondary storage could produce an error in logs. |
| GG-44919 | Distributed Computing | Added experimental support for WebAssembly compute jobs. |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.8`

{% hint style="info" %}
When updating from older versions, we recommend updating to version `9.1.8` first, before performing an update to current version.
{% endhint %}

## Known Limitations

### Data Restoration After Data Rebalance

Currently, data rebalance may cause partition distribution to change and cause issues with snapshots and data recovery. In particular:

- It is currently not possible to restore a `LOCAL` snapshot if data rebalance happened after snapshot creation. This will be addressed in one of the upcoming releases.
- It is currently not possible to perform point-in-time recovery if data rebalance happened after table creation. This will be addressed in one of the upcoming releases.

### SQL Performance in Complex Scenarios

There are known issues with the performance of SQL read-write transactions in complex read-write scenarios. These issues will be addressed in an upcoming releases.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
