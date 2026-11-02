---
description: >-
  Fixes for common GridGain for Spark problems: IgniteRDD actions that hang and
  ClassNotFoundException errors from the Java logger.
---

# Troubleshooting

- My Spark application or Spark shell hangs when I invoke any action on IgniteRDD

  This will happen if you have created `IgniteContext` in client mode (which is the default mode) and you do not have any GridGain server nodes started up. In this case, the GridGain client will wait until server nodes are started or fail after cluster join timeout has elapsed. You should start at least one GridGain server node when using `IgniteContext` in client mode.

- I am getting `java.lang.ClassNotFoundException` `org.apache.ignite.logger.java.JavaLoggerFileHandler` when using IgniteContext

  This issue appears when you do not have any loggers included in classpath and GridGain tries to use standard Java logging. By default, Spark loads all user jar files using separate class loader. Java logging framework, on the other hand, uses application class loader to initialize log handlers. To resolve this, you can either add `ignite-log4j2` module to the list of the used jars so that Ignite would use Log4j2 as a logging subsystem, or alter default Spark classpath as described [here](installation.md).
