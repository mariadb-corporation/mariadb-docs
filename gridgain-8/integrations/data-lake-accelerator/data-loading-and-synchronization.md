---
description: >-
  GridGain Hadoop Connector supports several ways to load data from Hadoop to GridGain and to keep the two stores synchronized.
---

# Data Loading and Synchronization

GridGain Hadoop Connector supports several ways to perform initial data loading from Hadoop to GridGain and synchronization between the two stores.

## Loading With GridGain Spark Loader

Use [GridGain Spark Loader](loading-data-with-spark.md) if you already have Spark in your architecture. Using Spark is straightforward and one of the fastest ways to load data from Hadoop to GridGain.

## Loading and Schema Import with Hive Store

Hive Store better suits deployments without Spark and it can also import a Hive schema and convert it to a GridGain configuration via GridGain Nebula. Refer to [Load and Sync With Hive Store](loading-and-synchronizing-with-hive.md) for more details.

## Bi-Directional Synchronization With Apache Sqoop

The [Sqoop integration](synchronizing-with-sqoop.md) can be used to synchronize two stores. The synchronization can be set to send updates from GridGain to Hadoop, from Hadoop to GridGain, or in a bi-directional mode.
