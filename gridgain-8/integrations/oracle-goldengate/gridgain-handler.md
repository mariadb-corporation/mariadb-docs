---
description: >-
  Install and configure the GridGain handler for Oracle GoldenGate for Big Data, set up the replicat process, and troubleshoot common errors.
---

# GridGain Handler

## Prerequisites

JDK 8.x

## Install GoldenGate

1. Download [GoldenGate for Big Data](https://www.oracle.com/il-en/middleware/technologies/goldengate-downloads.html).
2. Extract the distribution and navigate to its root directory.
3. Check that GoldenGate is working by running Command Interpreter (`ggsci`).

## Run Java Handler

1. Launch GoldenGate Command Interpreter (`ggsci`).
2. Verify that Manager is running:

   ```
   info manager
   ```

3. If the manager has stopped, start it:

   ```
   start manager
   ```

4. Run the following command to start creating configuration for the `replicat` process (a.k.a. `javarepl`):

   ```
   edit params javarepl
   ```

5. Copy the GridGain GoldenGate connector directory (available in `integration/gridgain-goldengate-19`) from the GridGain distribution to the GoldenGate distribution under `ggjava/lib`.

   Example configuration for the `replicat` process:

   ```
   REPLICAT javarepl
   TARGETDB LIBFILE libggjava.so SET property=dirprm/javarepl.props
   REPORTCOUNT EVERY 1 MINUTES, RATE
   GROUPTRANSOPS 1000
   MAP MYSCHEMA.*, TARGET MYSCHEMA.*;
   ```

6. Create an additional configuration file for Java runtime in the `dirprm` directory, next to `javarepl.prm` created in the previous step:

   ```
   #javarepl.props
   gg.handlerlist=gridgain
   gg.handler.gridgain.type=org.gridgain.oracle.goldengate.GridGainHandler
   gg.handler.gridgain.configurationPath=dirprm/gridgain-config.xml
   gg.handler.gridgain.operationHandlerBeanName=fooHandler

   goldengate.userexit.writers=javawriter
   javawriter.stats.display=TRUE
   javawriter.stats.full=TRUE
   gg.log=log4j
   gg.log.level=INFO
   gg.report.time=30sec
   gg.classpath=ggjava/lib/gridgain-goldengate-19/*
   javawriter.bootoptions=-Xmx512m -Xms32m -Djava.class.path=.:./ggjava/ggjava.jar:./dirprm
   ```

7. Create a GridGain configuration file, `dirprm/gridgain-config.xml`. Example:

   ```xml
   <beans xmlns="http://www.springframework.org/schema/beans"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://www.springframework.org/schema/beans
           http://www.springframework.org/schema/beans/spring-beans.xsd">
       <bean id="personOpHandler" name="personOpHandler" class="org.gridgain.oracle.goldengate.handler.PersonOperationHandler"/>

       <bean id="ignite.cfg" class="org.apache.ignite.configuration.IgniteConfiguration">
           <property name="localHost" value="127.0.0.1"/>

           <property name="cacheConfiguration">
               <list>
                   <bean class="org.apache.ignite.configuration.CacheConfiguration">
                       <property name="name" value="person"/>
                       <property name="atomicityMode" value="ATOMIC"/>
                       <property name="backups" value="1"/>
                   </bean>
                   <bean class="org.apache.ignite.configuration.CacheConfiguration">
                       <property name="name" value="address"/>
                       <property name="atomicityMode" value="TRANSACTIONAL"/>
                       <property name="backups" value="1"/>
                   </bean>
               </list>
           </property>
       </bean>
   </beans>
   ```

8. Add the `replicat` process:

   ```
   add replicat javarepl, exttrail dirdat/tr
   ```

   {% hint style="info" %}
   The two-character `trail` name comes from the `extract` process configuration.
   {% endhint %}

9. Start the replication process:

   ```
   start replicat javarepl
   ```

10. Check the process status using the `info javarepl` (basic) or `view report javarepl` (verbose) command.
11. For process log, see `dirrpt/JAVAREPL.LOG`.

## Errors and Remedies

**Problem:**

The `./ggsci: error while loading shared libraries: "libjvm.so: cannot open shared object file: No such file or directory".

**Reason:**

Some Java variables are not configured correctly.

**Remedy:**

1. Set the variables as follows:

   ```
   export JAVA_HOME=<valid-jdk-8-path>
   export PATH=$JAVA_HOME/bin:$PATH 
   export LD_LIBRARY_PATH=$JAVA_HOME/jre/lib/amd64/server:$LD_LIBRARY_PATH
   ```

2. Place the GoldenGate trail files into the `dirdat` directory.
