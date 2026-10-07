---
description: >-
  Use Apache Sqoop to import data from GridGain to Hadoop, export data from Hadoop to GridGain, and perform incremental imports (Change Data Capture).
---

# Synchronizing Data Using Apache Sqoop

Load data from/to Hadoop and GridGain clusters using Apache Sqoop, a tool for transferring data between Hadoop and structured datastores. Sqoop connects to a GridGain cluster using the JDBC driver and connection manager provided by GridGain.

This page explains how to:

- Import data from GridGain to Hadoop.
- Export data from Hadoop to GridGain.
- Perform an incremental import by loading only the data that has changed since the last synchronization (Change Data Capture).

All operations are performed by running the Sqoop command with relevant parameters.

## Setup

Download the GridGain Hadoop Connector from [http://gridgain.com/tryfree](http://gridgain.com/tryfree#gridgain8-ultimateedition) and unpack the archive into a directory. We will refer to this directory as `GG_HADOOP_CONNECTOR_HOME`.

The `GRIDGAIN_HOME` variable refers to the GridGain distribution folder.

Set the following environment variables in `${GG_HADOOP_CONNECTOR_HOME}/examples/gridgain-sqoop-examples/setenv.sh`.

{% code title="setenv.sh" %}
```bash
#Apache Ignite core library with JDBC Thin driver to be added the Hadoop classpath.
export IGNITE_CORE_LIB="<GRIDGAIN_HOME>/libs/ignite-core-<GRIDGAIN_VERSION>.jar"

#GridGain Sqoop integration library
export GRIDGAIN_SQOOP_LIB="<GG_HADOOP_CONNECTOR_HOME>/libs/gridgain-sqoop/gridgain-sqoop-<VERSION>.jar"
#Apache Hadoop home
#Example: /home/user/hadoop-2.9.2
export HADOOP_HOME="<HADOOP_HOME>"

#Apache Sqoop Home
#Example: /home/user/sqoop-1.4.7
export SQOOP_HOME="<APACHE_SQOOP_HOME>"
```
{% endcode %}

Start a GridGain server node using the following configuration file. This configuration defines a cache named Person with three fields: `id`, `name`, `last_updated`.

{% code title="server.xml" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans" xmlns:util="http://www.springframework.org/schema/util" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.springframework.org/schema/beans                            http://www.springframework.org/schema/beans/spring-beans.xsd                            http://www.springframework.org/schema/util                            http://www.springframework.org/schema/util/spring-util.xsd">
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
                                    </list>
                                </property>
                                <property name="fields">
                                    <map>
                                        <entry key="id" value="java.lang.Long"/>
                                        <entry key="name" value="java.lang.String"/>
                                        <entry key="lastUpdated" value="java.sql.Timestamp"/>
                                    </map>
                                </property>
                                <property name="aliases">
                                    <map>
                                        <entry key="id" value="id"/>
                                        <entry key="name" value="name"/>
                                        <entry key="lastUpdated" value="last_updated"/>
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

To start a node, run the following command.

{% tabs %}
{% tab title="UNIX" %}
```bash
${GRIDGAIN_HOME}/bin/ignite.sh path/to/server.xml
```
{% endtab %}

{% tab title="Windows" %}
```bash
${GRIDGAIN_HOME}\bin\ignite.bat path\to\server.xml
```
{% endtab %}
{% endtabs %}

Populate the Person cache using the sqlline tool as follows:

```bash
${GRIDGAIN_HOME}/bin/sqlline.sh -u jdbc:ignite:thin://127.0.0.1/ -f <GG_HADOOP_CONNECTOR_HOME>/examples/gridgain-sqoop-examples/config/init.sql
```

Please make sure that `JAVA_HOME` points to jdk 11 or higher and copy the GridGain and Scoop jars to the HDFS:

```bash
hdfs dfs -mkdir -p /home/user/sqoop-1.4.7/lib
hdfs dfs -put /home/user/sqoop-1.4.7/lib/* /home/user/sqoop-1.4.7/lib

hdfs dfs -put /home/user/sqoop-1.4.7/sqoop-1.4.7.jar /home/user/sqoop-1.4.7
hdfs dfs -mkdir -p /home/user/gridgain-enterprise-8.10/libs
hdfs dfs -put /home/user/gridgain-enterprise-8.10/libs/ignite-core-8.10.jar /home/user/gridgain-enterprise-8.10/libs/

hdfs dfs -mkdir -p /home/user/gridgain-hadoop-connector/libs/gridgain-sqoop
hdfs dfs -put /home/user/gridgain-hadoop-connector/libs/gridgain-sqoop/gridgain-sqoop-<version>.jar /home/user/gridgain-hadoop-connector/libs/gridgain-sqoop
```

Now we have a running GridGain cluster (consisting of one node) that contains a cache with data.

Let's import the data into HDFS.

## Import from GridGain to HDFS

Go to `${GG_HADOOP_CONNECTOR_HOME}/examples/gridgain-sqoop-examples/` and execute `import.sh|bat`. The script launches Sqoop's `import` command to load data from the Person table into HDFS as text files. You can customize the import options in the `import.txt` file.

| Parameter | Description |
|---|---|
| `--connect` | The JDBC driver connection URL.<br>To connect to a local cluster, use `jdbc:ignite:thin://localhost`. |
| `--driver and --connection-manager` | Leave unchanged. These classes are provided by GridGain and Hadoop Connector libraries. |
| `--target-dir` | The destination path in HDFS. |
| `--outdir` | Output directory for generated code. |
| `--split-by` | The column that will be used to split the data into work units. |
| `--as-textfile` | Indicates that the data will be imported as plain text. Each table row is stored as one record per line in the file located in the target-dir directory. |

## Incremental import from GridGain to HDFS

You can use an incremental import to load only the rows that have been modified since the last import. To use this feature, the table must contain a column that stores the timestamp of the time when the row was inserted. In our example, we use the `last_updated` column. The value in this column must be set to the current timestamp every time the Person table is updated.

Read more about incremental imports in the [Sqoop documentation](https://sqoop.apache.org/docs/1.4.7/SqoopUserGuide.html#_incremental_imports).

The `create-incremental-import-job.sh` script creates a saved job that performs an incremental import. The created job remembers the parameters and can be executed by its name.

The parameters for the import job are specified in the `create-incremental-import-job.txt` file.

| Parameter | Description |
|---|---|
| `--check-column` | Specifies the column to examine when determining which rows to import. |
| `--last-value` | Specifies the maximum value of the check column from the previous import. |

The `run-import-job.sh` script launches the saved job. Change the value of the `--last-value` parameter in `create-incremental-import-job.txt` and run the script to import the data.

## Export from HDFS to GridGain

The `export.sh` script launches the `export` command which loads the data from HDFS into the GridGain cluster. The scripts parses the input files (specified in `export.txt`) and loads the data into the Person table in the GridGain cluster using DML statements.

| Parameter | Description |
|---|---|
| `--export-dir` | The source directory for the export. |
| `--table` | The name of the cache in GridGain to populate. |

See the full list of parameters in the [Sqoop documentation](https://sqoop.apache.org/docs/1.4.7/SqoopUserGuide.html#_literal_sqoop_export_literal).

Here is an example a source file:

{% code title="/opt/hdfs/warehouse/Person/part-r-00000" %}
```
1,John,2019-01-01 00:00:00.0
```
{% endcode %}
