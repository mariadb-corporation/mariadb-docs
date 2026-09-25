---
description: >-
  An empirical approach to estimating how much disk space your data will require
  when loaded into GridGain's internal binary format.
---

# Empirical Estimation of Disk Capacity Usage

This page describes an empirical approach to estimating the amount of disk space your data will require when loaded into GridGain.

There is no one-to-one correspondence between the data size stored in a database (or in a CSV file) and the data stored in the persistent storage. The reason is that GridGain uses its own internal binary format that introduces some overhead in terms of data size. Moreover, the data size depends on the data model (e.g. how many fields you have, the types of fields, which fields are indexed, etc.). For example, records stored in a CSV-file can be represented as objects with multiple fields of different types.

The basic steps of the empirical approach are as follows:

- Define your data model, including data types and indexes. You should evaluate the size with the same data model that you would use in production.
- Upload a sample of data into a node and measure how much space the data takes when saved on disk.
- Extrapolate to the entire data set.

Let's look at each step in detail. For the sake of simplicity, we will consider a single cache containing key-value pairs where the key is an integer and the value is a Java object with `int`, `String`, and `Timestamp` fields. If you have multiple caches (tables) with different data structure, you should estimate the size of each cache separately.

## Defining data model

The Value class has three fields: `id (int)`, `name (String)`, and `date (Timestamp)`. The length of the name field is variable; therefore, we need to analyze the length distribution of that field and use a sample that contains objects with the average length. (You can use an upper estimate for the name field; however, using an upper estimate may lead to unnecessary over-provisioning). We will assume that the average length across the entire dataset is 10 characters. Other fields have fixed-length types.

{% code title="Java" %}
```java
class Value {
    public int id;

    public String name;

    public Timestamp date;

    public Value(int id, String name, Timestamp date) {
        this.id = id;
        this.name = name;
        this.date = date;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public Timestamp getDate() {
        return date;
    }
}
```
{% endcode %}

## Uploading sample into a node

Configure a cache with a single partition and enable metrics. An example configuration is provided below.

{% code title="config-data-size-estimation.xml" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

    <property name="dataStorageConfiguration">
      <bean class="org.apache.ignite.configuration.DataStorageConfiguration">
        <property name="metricsEnabled" value="true"/>
        <!-- write-ahead log is disabled for better performance. Do not use this  mode in production -->
        <property name="walMode" value="NONE"/>

        <property name="defaultDataRegionConfiguration">
          <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
            <!-- enable persistent storage -->
            <property name="persistenceEnabled" value="true"/>
            <property name="metricsEnabled" value="true"/>
          </bean>
        </property>
      </bean>
    </property>

    <property name="cacheConfiguration">
      <bean class="org.apache.ignite.configuration.CacheConfiguration">
        <property name="name" value="myCache"/>
        <property name="affinity">
          <bean class="org.apache.ignite.cache.affinity.rendezvous.RendezvousAffinityFunction">
            <property name="partitions" value="1"/>
          </bean>
        </property>
      </bean>
    </property>

    <!-- other properties -->

</bean>
```
{% endcode %}

Upload data into the cache. You can use the code provided in the following snippet to start a node and upload a sample of 2,000,000 entries. Make sure to add the [required libraries to the classpath](../gridgain8-usage/setup.md).

Change the `createSampleValue` method to return objects of your specific type.

{% code title="Java" %}
```java
package test;

import java.sql.Timestamp;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.cache.query.annotations.QuerySqlField;
import org.apache.ignite.configuration.CacheConfiguration;
import org.apache.ignite.internal.util.typedef.internal.U;

public class DataSizeEstimation {

    static class Value {
        public int id;

        public String name;

        public Timestamp date;

        public Value(int id, String name, Timestamp date) {
            this.id = id;
            this.name = name;
            this.date = date;
        }

        public int getId() {
            return id;
        }

        public String getName() {
            return name;
        }

        public Timestamp getDate() {
            return date;
        }
    }

    private static Value createSampleValue(int i) {
        return new Value(i, "123456789" + i, new Timestamp(System.currentTimeMillis()));
    }

    public static void main(String[] args) {
        try (Ignite ignite = Ignition.start("config-data-size-estimation.xml")) {

            ignite.cluster().active(true);

            System.out.println("Populating the cache...");

            IgniteCache<Long, Value> cache = ignite.cache("myCache");

            for (int i = 0; i <= 2_000_000; i++) {
                cache.put((long) i, createSampleValue(i));
            }

            System.out.println("Total storage size: "
                    + U.readableSize(ignite.dataStorageMetrics().getTotalAllocatedSize(), false));

            ignite.cluster().active(false);
        }
    }
}
```
{% endcode %}

{% hint style="info" %}
If you use GridGain or Ignite via the SQL API only, you can create a table with the required field definitions and upload a data sample into it.
{% endhint %}

To find out the amount of space taken up by the data, check the value of the `DataRegionMetrics.default.TotalAllocatedSize` metric. It returns the total size of the data on disk. The code provided above will produce 271.1 MB of data.

## Extrapolating to the entire data set

When the size of the data sample is known, the total size of the entire dataset can be obtained from linear interpolation. Continuing the example considered above, if we upload 10 million records, we will have:

`5 * 271.1 = 1355.5 MB`

This is the size of the data converted into the internal binary format. The total size of the persistent storage includes the backup copies (if they are configured), WAL files, and a negligible amount of metadata. See [this page](capacity-planning.md#disk-space-usage-example) for details.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
