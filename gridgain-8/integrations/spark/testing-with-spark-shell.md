---
description: >-
  Start a Spark and GridGain cluster and use spark-shell to create an
  IgniteContext and IgniteRDD, save values, and check that state survives job
  restarts.
---

# Testing GridGain with Spark-shell

## Starting up the cluster

Here we will briefly cover the process of Spark and GridGain cluster startup. Refer to [Spark documentation](https://spark.apache.org/docs/latest/) for more details.

For the testing you will need a Spark master process and at least one Spark worker. Usually Spark master and workers are separate machines, but for the test purposes you can start worker on the same machine where master starts.

1. Download and unpack Spark binary distribution to the same location (let it be `SPARK_HOME`) on all nodes.
2. Download and unpack GridGain binary distribution to the same location (let it be `IGNITE_HOME`) on all nodes.
3. On master node `cd` to `$SPARK_HOME` and run the following command:

   ```bash
   sbin/start-master.sh
   ```

   The script should output the path to log file of the started process. Check the log file for the master URL which has the following format: `spark://master_host:master_port` Also check the log file for the Web UI url (usually it is `http://master_host:8080`).
4. On each of the worker nodes `cd` to `$SPARK_HOME` and run the following command:

   ```bash
   bin/spark-class org.apache.spark.deploy.worker.Worker spark://master_host:master_port
   ```

   where `spark://master_host:master_port` is the master URL you grabbed from the master log file. After workers has started check the master Web UI interface, it should show all of your workers registered in status `ALIVE`.
5. On each of the worker nodes cd to `$IGNITE_HOME` and start an Ignite node by running the following command:

   ```bash
   bin/ignite.sh
   ```

You should see GridGain nodes discover each other with default configuration. If your network does not allow multicast traffic, you will need to change the default configuration file and configure TCP discovery.

## Working with Spark-Shell

Now that you have your cluster up and running, you can run `spark-shell` and check the integration.

1. Start spark shell:

   - Either by providing Maven coordinates to Ignite artifacts (you can use `--repositories` if you need, but it may be omitted):

     ```bash
     ./bin/spark-shell
         --packages org.apache.ignite:ignite-spark-ext:2.0.0
       --master spark://master_host:master_port
       --repositories http://repo.maven.apache.org/maven2/org/apache/ignite
     ```
   - Or by providing paths to Ignite jar file paths using `--jars` parameter

     ```bash
     ./bin/spark-shell --jars path/to/ignite-core.jar,path/to/ignite-spark-ext.jar,path/to/cache-api.jar,path/to/ignite-log4j2.jar,path/to/log4j.jar --master spark://master_host:master_port
     ```

   You should see Spark shell started up.

   Note that if you are planning to use spring configuration loading, you will need to add the `ignite-spring` dependency as well:

   ```bash
   ./bin/spark-shell
       --packages org.apache.ignite:ignite-spark-ext:2.0.0,org.apache.ignite:ignite-spring:2.13.0
     --master spark://master_host:master_port
   ```
2. Let's create an instance of Ignite context using default configuration:

   ```scala
   import org.apache.ignite.spark._
   import org.apache.ignite.configuration._

   val ic = new IgniteContext(sc, () => new IgniteConfiguration())
   ```

   You should see something like

   ```
   ic: org.apache.ignite.spark.IgniteContext = org.apache.ignite.spark.IgniteContext@62be2836
   ```

   An alternative way to create an instance of IgniteContext is to use a configuration file. Note that if path to configuration is specified in a relative form, then the `IGNITE_HOME` environment variable should be globally set in the system as the path is resolved relative to `IGNITE_HOME`

   ```scala
   import org.apache.ignite.spark._
   import org.apache.ignite.configuration._

   val ic = new IgniteContext(sc, "examples/config/spark/example-shared-rdd.xml")
   ```
3. Let's now create an instance of `IgniteRDD` using "partitioned" cache in default configuration:

   ```scala
   val sharedRDD = ic.fromCache[Integer, Integer]("partitioned")
   ```

   You should see an instance of RDD created for partitioned cache:

   ```
   shareRDD: org.apache.ignite.spark.IgniteRDD[Integer,Integer] = IgniteRDD[0] at RDD at IgniteAbstractRDD.scala:27
   ```

   Note that creation of RDD is a local operation and will not create a cache in Ignite cluster.
4. Let's now actually ask Spark to do something with our RDD, for example, get all pairs where value is less than 10:

   ```scala
   sharedRDD.filter(_._2 < 10).collect()
   ```

   As our cache has not been filled yet, the result will be an empty array:

   ```
   res0: Array[(Integer, Integer)] = Array()
   ```

   Check the logs of remote spark workers and see how Ignite context will start clients on all remote workers in the cluster. You can also start command-line Visor and check that "partitioned" cache has been created.
5. Let's now save some values into Ignite:

   ```scala
   sharedRDD.savePairs(sc.parallelize(1 to 100000, 10).map(i => (i, i)))
   ```

   After running this command you can check with command-line Visor that cache size is 100000 elements.
6. We can now check how the state we created will survive job restart. Shut down the spark shell and repeat steps 1-3. You should again have an instance of Ignite context and RDD for "partitioned" cache. We can now check how many keys there are in our RDD which value is greater than 50000:

   ```scala
   sharedRDD.filter(_._2 > 50000).count
   ```

   Since we filled up cache with a sequence of number from 1 to 100000 inclusive, we should see `50000` as a result:

   ```
   res0: Long = 50000
   ```
