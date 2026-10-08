---
description: >-
  Use Spark Data Loader to load data from Hadoop, Hive, CSV, and JSON sources into GridGain. This example creates a table in Hadoop, populates it, and loads it into a GridGain cluster.
---

# Loading Data With Spark

Spark Data Loader can be used to load data from Hadoop as well as other sources into GridGain.

Spark Data Loader supports the following structured data sources:

- CSV
- JSON
- Hive and other databases that support Spark SQL

In this example, we create a table in Hadoop and populate it with data. Then we load the data from Hadoop into GridGain.

The source code files for this example are available in the Hadoop Connector distribution package. Download the GridGain Hadoop Connector from [https://www.gridgain.com/tryfree](https://www.gridgain.com/tryfree#gridgain8-ultimateedition) and unpack the archive into a directory. We will refer to this directory as `GG_HADOOP_CONNECTOR_HOME`.

## Prerequisites

Spark Data Loader was tested with the following components.

| NAME | VALUE |
|---|---|
| OS | Linux (any flavor) |
| JDK | Oracle JDK 8 or 11<br>Open JDK 8 or 11 |
| HDFS | 2.6 or later release of 2.X |
| GridGain | 8.7.5 |
| Hive | 2.1 or later release of 2.X |
| Spark | 2.3.0, 2.4.0 |

## Configuring Hadoop, Spark, and Hive

We assume that you already have a running Hadoop cluster and have configured Spark to run on top of it.

Refer to the following guides for the installation of HDFS:

1. https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html
2. https://spark.apache.org/docs/latest/spark-standalone.html
3. https://cwiki.apache.org/confluence/display/Hive/GettingStarted

### Keep the Following In Mind:

1. You should check that the `HADOOP_CONF_DIR` variable is set.
2. In case your HIVE uses the DERBY database as `metastore_db` (part of the Hive Getting Started guide) then you should add the path to your `metastore_db location` to the configuration files:

   To your Spark configuration file:

   ```
   spark.executor.extraJavaOptions -Dderby.system.home=/home/user/hive/metastore_db
   ```

   To your Hive configuration file:

   ```xml
   <property>
       <name>
         javax.jdo.option.ConnectionURL
       </name>
       <value>
         jdbc:derby:;databaseName=/home/user/hive/metastore_db;create=true
       </value>
       <description>
         JDBC connect string for a JDBC metastore.
         To use SSL to encrypt/authenticate the connection, provide database-specific SSL flag in the connection URL.
         For example, jdbc:postgresql://myhost/db?ssl=true for postgres database.
       </description>
   </property>
   ```
3. The examples expect that HDFS will be available via `hdfs://localhost:9000`

### Loading Data into Hadoop using Hive

Run the Hive CLI and paste the following command into the prompt:

```sql
CREATE TABLE `person`(
`id` int,
`city_id` int,
`name` string,
`age` int,
`company` string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS INPUTFORMAT
  'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  'hdfs://localhost:9000/user/hive/warehouse/person'
TBLPROPERTIES (
'COLUMN_STATS_ACCURATE'='true',
'numFiles'='1');
```

Once the table is created, load the test data into the table by running the following command:

```sql
LOAD DATA LOCAL INPATH '<BIG_DATA_ACCELERATOR_HOME>/examples/gridgain-spark-loader-examples/config/person.csv' INTO TABLE person;
```

## Running GridGain Cluster

To load data from Hadoop, you need to define a cache configuration that corresponds to the Hadoop data model.
You can define the data model in the configuration via QueryEntities or using the [CREATE TABLE](../../reference/sql/ddl.md#create-table) command.

Spark Data Loader can also create tables in GridGain at runtime.

In this example, the five columns (`id`, `city_id`, `name`, `age`, `company`) in the `Person` table will be mapped to five fields with corresponding types. The following configuration file specifies a cache named Person which will store objects loaded from Hadoop.

{% code title="server.xml" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>

<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:util="http://www.springframework.org/schema/util"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
                           http://www.springframework.org/schema/beans/spring-beans.xsd
                           http://www.springframework.org/schema/util
                           http://www.springframework.org/schema/util/spring-util.xsd">
    <bean class="org.apache.ignite.configuration.IgniteConfiguration">

        <property name="discoverySpi">
            <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
                <property name="ipFinder">
                    <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                        <property name="addresses">
                            <list>
                                <value>127.0.0.1:47500..47510</value>
                            </list>
                        </property>
                    </bean>
                </property>
            </bean>
        </property>

        <property name="cacheConfiguration">
            <list>
                <bean class="org.apache.ignite.configuration.CacheConfiguration">
                    <property name="name" value="Person"/>
                    <property name="cacheMode" value="PARTITIONED"/>
                    <property name="atomicityMode" value="ATOMIC"/>
                    <property name="sqlSchema" value="PUBLIC"/>

                    <property name="queryEntities">
                        <list>
                            <bean class="org.apache.ignite.cache.QueryEntity">
                                <property name="keyType" value="PersonKey"/>
                                <property name="valueType" value="PersonValue"/>
                                <property name="tableName" value="Person"/>

                                <property name="keyFields">
                                    <list>
                                        <value>id</value>
                                        <value>city_id</value>
                                    </list>
                                </property>

                                <property name="fields">
                                    <map>
                                        <entry key="id" value="java.lang.Integer"/>
                                        <entry key="city_id" value="java.lang.Integer"/>
                                        <entry key="name" value="java.lang.String"/>
                                        <entry key="age" value="java.lang.Integer"/>
                                        <entry key="company" value="java.lang.String"/>
                                    </map>
                                </property>

                                <property name="aliases">
                                    <map>
                                        <entry key="id" value="id"/>
                                        <entry key="city_id" value="city_id"/>
                                        <entry key="name" value="name"/>
                                        <entry key="age" value="age"/>
                                        <entry key="company" value="company"/>
                                    </map>
                                </property>
                            </bean>
                        </list>
                    </property>
                </bean>
            </list>
        </property>
    </bean>
</beans>
```
{% endcode %}

Start a server node with the above configuration:

{% tabs %}
{% tab title="UNIX" %}
```bash
${GRIDGAIN_HOME}/bin/ignite.sh config.xml
```
{% endtab %}

{% tab title="Windows" %}
```bash
${GRIDGAIN_HOME}\bin\ignite.bat config.xml
```
{% endtab %}
{% endtabs %}

## Running Spark Data Loader Example

Now, let's load the data from Hadoop into the GridGain cluster that we started on the previous step. Before running the examples, add Spark Data Loader libraries to your project. You can do it in either of the following two ways:

1. If you use Maven, add the following dependency to your project:

   ```xml
   <dependency>
       <groupId>org.gridgain.plugins</groupId>
       <artifactId>gridgain-spark-loader</artifactId>
       <version>${hadoop.connector.version}</version>
   </dependency>
   ```
2. Or add the libraries from `${GG_HADOOP_CONNECTOR_HOME}/libs/gridgain-spark-loader/` to your project.

You can load data from a specific table in Hive by specifying the table name and schema, or you can use a SELECT query. A typical procedure for doing this involves the following steps:

1. Create an instance of `GridGainSparkLoader` and set relevant Spark parameters.
2. Use one of the `GridGainSparkLoader` methods to create an object of the `GridGainSparkDataset` class, which defines how data can be loaded. Use this object to filter the data before saving it into GridGain.
3. Call `GridGainSparkDataset.save()` and `GridGainSparkLoader.closeSession()`.

The following code snippets demonstrate how to perform the steps described above.

{% tabs %}
{% tab title="Hive table schema and name" %}
```java
package org.gridgain.examples.sparkloader;

import org.apache.spark.SparkConf;
import org.gridgain.sparkloader.GridGainSparkLoader;

public class LoadingFromHiveExample {
    public static void main(String[] args) {
        if (args.length < 1)
            throw new IllegalArgumentException("You should set the path to client configuration file.");

        String configPath = args[0];

        GridGainSparkLoader sparkLoader;

        sparkLoader = new GridGainSparkLoader.GridGainSparkLoaderBuilder()
                    .setApplicationName("LoadingFromHiveExample") //comment out this line in case you are going to use spark submit with application name option
                    .setMaster("local") //comment out this line in case you are going to use spark submit with master option
                    .setIsHive(true)
                    .build(configPath);

        sparkLoader.loadTableToExistingCache("default", "person", "Person")
                .filter("company = 'bank'")
                .save();

        sparkLoader.closeSession();
    }
}
```
{% endtab %}

{% tab title="SQL Select statement from Hive" %}
```java
package org.gridgain.examples.sparkloader;

import org.apache.spark.SparkConf;
import org.gridgain.sparkloader.GridGainSparkLoader;

public class LoadingFromSelectExample {
    public static void main(String[] args) {
        if (args.length < 1 || args.length > 2)
            throw new IllegalArgumentException("You should set the path to client configuration file.");

        String configPath = args[0];

        Boolean advanced = args.length == 2 && args[1].contains("true");

        GridGainSparkLoader sparkLoader;

        if (advanced) {
            //you can set different options using spark configuration. Not only that you can find in GridGainSparkLoaderBuilder.
            SparkConf sparkConf = new SparkConf()
                    .setAppName("LoadingFromSelectExample") //comment this line in case if you are going to use spark submit with application name option
                    .setMaster("local") //comment this line in case if you are going to use spark submit with master option
                    .set("spark.some.config.option", "some-value");

            //Master and appName GridGainSparkLoaderBuilder options related to Spark will be ignored.
            sparkLoader = new GridGainSparkLoader.GridGainSparkLoaderBuilder()
                    .setIsHive(true)
                    .buildFromSparkConfig(sparkConf, configPath);
        } else
            sparkLoader = new GridGainSparkLoader.GridGainSparkLoaderBuilder()
                    .setApplicationName("LoadingFromSelectExample") //comment this line in case if you are going to use spark submit with application name option
                    .setMaster("local") //comment this line in case if you are going to use spark submit with master option
                    .setIsHive(true)
                    .build(configPath);

        sparkLoader.loadFromSelectToExistingCache(
                "select * from default.person where company = 'bank'",
                "Person")
                .save();

        sparkLoader.loadFromSelectToNewCache(
                "select * from default.person where company != 'bank'",
                "NotBankPersonWithoutAge",
                "id, city_id",
                "template=partitioned,backups=1")
                .select("id", "name", "city_id", "company")
                .filter("company != 'bank'")
                .save();

        sparkLoader.closeSession();
    }
}
```
{% endtab %}
{% endtabs %}

The class above takes the client node configuration file as an input parameter (an example file can be found in `${GG_HADOOP_CONNECTOR_HOME}/examples/gridgain-spark-loader-examples/config/client.xml`).

The application will create a Spark job that will stream the records from the Person table in Hive where the `company` field equals "bank" into the GridGain cluster.
