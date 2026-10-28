---
description: >-
  Run federated join and union queries across GridGain and Hadoop (Hive) by using Spark SQL and the GridGain Spark integration.
---

# Cross-Database Queries

Spark SQL Queries can access multiple tables simultaneously in such a way that multiple rows of each table are being processed at the same time. The tables could be located in the same or different databases.

GridGain supports advanced integration with Spark. You can include it in your maven project by adding the following dependencies:

```xml
<dependency>
    <groupId>org.gridgain</groupId>
    <artifactId>ignite-spark</artifactId>
    <version>${gridgain.version}</version>
    <exclusions>
        <exclusion>
          <!-- This dependency is not available with java 9+ -->
          <groupId>jdk.tools</groupId>
          <artifactId>jdk.tools</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

## Join Federated Queries

A query that accesses different tables simultaneously is called a join query.

The following example shows the joins between the `cities` table in Hive and the `Person` table in GridGain, via the `city_id` field.

The `cities` table in Hive:

```sql
CREATE TABLE `cities`(
`city_id` int,
`city_name` string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS INPUTFORMAT
  'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  'hdfs://localhost:9090/user/hive/warehouse/cities'
TBLPROPERTIES (
'COLUMN_STATS_ACCURATE'='true',
'numFiles'='1');
```

The `Person` table in GridGain:

```xml
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
```

Federated join requests can be executed like this:

```java
package org.gridgain.examples;

import org.apache.ignite.spark.IgniteDataFrameSettings;
import org.apache.spark.SparkConf;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;

public class FederatedJoinExample {
    public static void main(String[] args) {
        if (args.length < 1)
            throw new IllegalArgumentException("You should set the path to client configuration file.");

        String configPath = args[0];

        //you can set different options using spark configuration. Not only that you can find in GridGainSparkLoaderBuilder.
        SparkConf sparkConf = new SparkConf()
                .setAppName("FederatedQueriesExample") //comment this line in case if you are going to use spark submit with application name option
                .setMaster("local") //comment this line in case if you are going to use spark submit with master option
                .set("spark.some.config.option", "some-value");

        SparkSession session = SparkSession.builder()
                .config(sparkConf)
                .enableHiveSupport()
                .getOrCreate();

        //prepare the Hive data set
        Dataset<Row> hiveDS =
                session.table("default.cities")
                        .select("city_id", "city_name"); //fields should contain the join field (city_id)

        //prepare the GridGain data set
        Dataset<Row> gridgainDS = session.read()
                .format(IgniteDataFrameSettings.FORMAT_IGNITE()) //Data source
                .option(IgniteDataFrameSettings.OPTION_TABLE(), "Person") //Table to read.
                .option(IgniteDataFrameSettings.OPTION_CONFIG_FILE(), configPath) //Ignite config.
                .load()
                .select("id", "city_id", "name", "age", "company"); //fields should contain the join field (city_id)

        //INNER JOIN
        hiveDS.join(gridgainDS, hiveDS.col("city_id").equalTo(gridgainDS.col("city_id"))).show();

        //OUTER_JOIN
        hiveDS.join(gridgainDS, hiveDS.col("city_id").equalTo(gridgainDS.col("city_id")), "outer").show();

        //FULL_JOIN
        hiveDS.join(gridgainDS, hiveDS.col("city_id").equalTo(gridgainDS.col("city_id")), "full").show();

        //FULL OUTER_JOIN
        hiveDS.join(gridgainDS, hiveDS.col("city_id").equalTo(gridgainDS.col("city_id")), "fullouter").show();

        //LEFT OUTER_JOIN
        hiveDS.join(gridgainDS, hiveDS.col("city_id").equalTo(gridgainDS.col("city_id")), "leftouter").show();

        //LEFT JOIN
        hiveDS.join(gridgainDS, hiveDS.col("city_id").equalTo(gridgainDS.col("city_id")), "left").show();

        //RIGHT OUTER JOIN
        hiveDS.join(gridgainDS, hiveDS.col("city_id").equalTo(gridgainDS.col("city_id")), "rightouter").show();

        //RIGHT JOIN
        hiveDS.join(gridgainDS, hiveDS.col("city_id").equalTo(gridgainDS.col("city_id")), "right").show();

        //CROSS JOIN
        hiveDS.join(gridgainDS, hiveDS.col("city_id").equalTo(gridgainDS.col("city_id")), "cross").show();

        session.close();
    }
}
```

## Union Federated Queries

Spark supports union queries between different data sources that return a new dataset containing the union of the elements in the source dataset and the argument. Data sources can be related to different database tables.

The following example shows the union query between the Hive `person` table and the GridGain `Person` table.

The `person` table in Hive:

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
  'hdfs://localhost:9090/user/hive/warehouse/person'
TBLPROPERTIES (
'COLUMN_STATS_ACCURATE'='true',
'numFiles'='1');
```

Federated union requests can be executed like this:

```java
package org.gridgain.examples;

import org.apache.ignite.spark.IgniteDataFrameSettings;
import org.apache.spark.SparkConf;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;

/**
 * Example of Spark cross-database union query between Hive and GridGain.
 */
public class FederatedQueriesExample {
    public static void main(String[] args) {
        if (args.length < 1)
            throw new IllegalArgumentException("You should set the path to client configuration file.");

        String configPath = args[0];

        //you can set different options using spark configuration. Not only that you can find in GridGainSparkLoaderBuilder.
        SparkConf sparkConf = new SparkConf()
                .setAppName("FederatedQueriesExample") //comment this line in case if you are going to use spark submit with application name option
                .setMaster("local") //comment this line in case if you are going to use spark submit with master option
                .set("spark.some.config.option", "some-value");

        SparkSession session = SparkSession.builder()
                .config(sparkConf)
                .enableHiveSupport()
                .getOrCreate();

        //prepare the Hive data set
        Dataset<Row> hiveDS =
                session.table("default.person")
                .select("id", "city_id", "name", "age", "company"); //order of the fields should be the same for both data sets

        //prepare the GridGain data set
        Dataset<Row> gridgainDS = session.read()
                .format(IgniteDataFrameSettings.FORMAT_IGNITE()) //Data source
                .option(IgniteDataFrameSettings.OPTION_TABLE(), "Person") //Table to read.
                .option(IgniteDataFrameSettings.OPTION_CONFIG_FILE(), configPath) //Ignite config.
                .load()
                .select("id", "city_id", "name", "age", "company"); //order of the fields should be the same for both data sets

        //run union query and print the result
        Dataset<Row> joinResult = hiveDS.union(gridgainDS);

        joinResult.show();

        session.close();
    }
}
```
