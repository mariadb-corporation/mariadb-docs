---
description: >-
  Deploy and redeploy Java compute tasks, services, and POJOs to a running GridGain 8 cluster without restarting nodes, using UriDeploymentSpi.
---

# How to Deploy Code With UriDeploymentSpi

## Prerequisites

- A running **GridGain 8** cluster
- A network folder accessible by all cluster nodes
- **JDK 17** and **Maven** to build the deployment JAR

## Overview

"Deploying code" means putting your application code in a remote environment where your app can run and serve your users. In Java, you usually deploy your app code by yourself, by updating the classpath and restarting the application to apply the changes.

Some web servers, such as TomCat, can deploy web applications using JAR and WAR files. When these files are updated, they deploy a new version of the web application without restarting the entire web server.

You can use a similar concept in Java. The Java classloaders feature enables you to load classes from different sources. By default, all the classes are loaded from the system classloader, which usually gets classes from the application classpath. However, it is possible to load classes that are not included in the JAVA classpath from another location.

With `UriDeploymentSpi`, you can deploy new versions of Java classes used by GridGain. This lets you update your Java classes without having to restart the Java application that runs the GridGain server.

## What can be Deployed via UriDeploymentSpi

Unfortunately, not everything can be deployed via `UriDeploymentSpi`. Here is the list of supported items:

- GridGain compute tasks
- GridGain services
- Java POJO that aren't included in the classpath

This guide reviews all the relevant cases.

## GridGain Configuration

Every GridGain node should have `UriDeploymentSpi` configured as follows:

```xml
<property name="deploymentSpi">
    <bean class="org.apache.ignite.spi.deployment.uri.UriDeploymentSpi">
        <property name="temporaryDirectoryPath" value="C:\\Users\\alexs\\UriDeploymentTest\\tmp_folder"/>
        <property name="uriList">
            <list>
                <value>file://freq=2000@192.168.0.18/Users/alexs/UriDeploymentTest/deployment_folder</value>
            </list>
        </property>
    </bean>
</property>
```

You need to prepare two folders:

- `temporaryDirectoryPath` - GridGain will unzip the new classes here for further loading
- `uriList` - set of URI addresses to be scanned for JARs

You are advised to use a network folder which all nodes can access inside `uriList`. It will help avoid the situation where different nodes have different versions of the classes.

Note the `freq=2000` parameter. Its value, in milliseconds, defines how often the location will be checked for new classes. You can set this parameter to a low value to avoid delay in class loading. The default is 5000 ms for the `file:` scanner and 300000 ms for the HTTP scanner (`http:` and `https:`).

Out of the box, this SPI supports the following protocols:

- `file:` - file protocol
- `http:` - HTTP protocol
- `https:` - secure HTTP protocol

## UriCodeDeployment Limitations

`UriDeploymentSpi` has the following limitations:

- You must prepare JAR files that contain all the related classes together (constructor parameters, classes used in compute tasks and services, etc.).
- Each JAR file must contain the `ignite.xml` file that lists the names of all the deployed classes. Otherwise, only compute tasks will be deployed.
- All nodes should use the same URI location to avoid delays when updating the scannable files.
- Service redeployment relies on the event-driven service processor, which is enabled by default. Set `-DIGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED=false` only if you want to turn it off, and note that redeployment then does not work.
- You cannot have the same class in the JVM classpath and in UriDeploymentSPI. In such a case, the JVM one will be used because Java does not allow multiple versions of the same class.

## Prepare the JAR File

Your JAR must have the following structure:

```text
META-INF/
META-INF/MANIFEST.MF
com/
com/gridgain/
com/gridgain/compute/
com/gridgain/models/
com/gridgain/service/
com/gridgain/compute/CacheSizeJob.class
com/gridgain/compute/TestComputeTask.class
com/gridgain/models/ModelClass.class
com/gridgain/service/RedeployServiceComputeTask$RedeployService.class
com/gridgain/service/RedeployServiceComputeTask.class
com/gridgain/service/TestService.class
META-INF/ignite.xml
META-INF/maven/
META-INF/maven/org.gridgain/
META-INF/maven/org.gridgain/UriDeploymentTest/
META-INF/maven/org.gridgain/UriDeploymentTest/pom.xml
META-INF/maven/org.gridgain/UriDeploymentTest/pom.properties
```

To build a JAR with the above structure:

1. Create a Maven project with the following `pom.xml`:

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <project xmlns="http://maven.apache.org/POM/4.0.0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
       <modelVersion>4.0.0</modelVersion>

       <groupId>org.gridgain</groupId>
       <artifactId>UriDeploymentTest</artifactId>
       <version>1.0-SNAPSHOT</version>

       <repositories>
           <repository>
               <id>GridGain External Repository</id>
               <url>https://www.gridgainsystems.com/nexus/content/repositories/external</url>
           </repository>
       </repositories>

       <properties>
           <maven.compiler.source>17</maven.compiler.source>
           <maven.compiler.target>17</maven.compiler.target>
           <ignite.version>8.10.0</ignite.version>
       </properties>

       <build>
           <plugins>
               <plugin>
                   <groupId>org.apache.maven.plugins</groupId>
                   <artifactId>maven-jar-plugin</artifactId>
                   <configuration>
                       <archive>
                           <manifest>
                               <addClasspath>true</addClasspath>
                           </manifest>
                           <manifestEntries>
                               <Class-Path>lib/</Class-Path>
                           </manifestEntries>
                       </archive>
                   </configuration>
               </plugin>
           </plugins>
       </build>

       <dependencies>
           <dependency>
               <groupId>org.gridgain</groupId>
               <artifactId>ignite-core</artifactId>
               <version>${ignite.version}</version>
           </dependency>
           <dependency>
               <groupId>org.gridgain</groupId>
               <artifactId>gridgain-core</artifactId>
               <version>${ignite.version}</version>
           </dependency>
           <dependency>
               <groupId>org.gridgain</groupId>
               <artifactId>ignite-spring</artifactId>
               <version>${ignite.version}</version>
           </dependency>
       </dependencies>
   </project>
   ```

1. Inside the Maven resources folder, create the `META-INF/ignite.xml` file with the following content:

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <beans xmlns="http://www.springframework.org/schema/beans"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xmlns:util="http://www.springframework.org/schema/util"
          xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-3.0.xsd
       http://www.springframework.org/schema/util http://www.springframework.org/schema/util/spring-util-2.5.xsd">

       <util:list id="testComputeTask" value-type="java.lang.String">
           <value>com.gridgain.compute.TestComputeTask</value>
       </util:list>

       <util:list id="testComputeTaskJob" value-type="java.lang.String">
           <value>com.gridgain.compute.CacheSizeJob</value>
       </util:list>

       <util:list id="testModelClass" value-type="java.lang.String">
           <value>com.gridgain.models.ModelClass</value>
       </util:list>

       <util:list id="testServiceDeployCompute" value-type="java.lang.String">
           <value>com.gridgain.service.RedeployServiceComputeTask</value>
       </util:list>

       <util:list id="testServiceDeployComputeJob" value-type="java.lang.String">
           <value>com.gridgain.service.RedeployServiceComputeTask$RedeployService</value>
       </util:list>

       <util:list id="testService" value-type="java.lang.String">
           <value>com.gridgain.service.TestService</value>
       </util:list>
   </beans>
   ```

1. Create a network folder (common for all hosts) named `deployment_folder`.
1. On every host, create a tmp folder named `tmp_folder`.
1. Build your project with the `mvn clean package` command.
1. Put the generated JAR into `deployment_folder`.

## Add the `ignite-urideploy` Dependency

The `ignite-urideploy` dependency is optional. This is why you need to add it explicitly, in one of the following ways:

1. If you run the node from the binaries, copy the `ignite-urideploy` dependency from optional libraries:

   ```bash
   cp -R $IGNITE_HOME/libs/optional/ignite-urideploy $IGNITE_HOME/libs/ignite-urideploy
   ```

1. If you use Maven, add the `ignite-urideploy` dependency to pom.xml:

   ```xml
   <dependency> 
       <groupId>org.gridgain</groupId> 
       <artifactId>ignite-urideploy</artifactId> 
       <version>${ignite.version}</version> 
   </dependency>
   ```

Now you can start your server node and use the classes from `deployment_folder` as described below.

## How to use the Deployed Classes

### POJO Classes

In Java, to use classes that are not included in the classpath, you have to load them from a special classloader. UriDeploymentSPI has its own classloader that you can get like this:

```java
ignite.configuration()
	.getDeploymentSpi()
	.findResource("com.gridgain.models.ModelClass")
	.getClassLoader());
```

The limitation of the above approach is that you need to use the Java reflection to create objects and work with them. This can be a little tricky. For example, here is the code where you create a `ModelClass` object and call its method:

```java
Class<?> modelClassFromURI = Class.forName("com.gridgain.models.ModelClass", true, ignite.configuration()
	.getDeploymentSpi()
	.findResource("com.gridgain.models.ModelClass")
	.getClassLoader());

Constructor<?> ctor = modelClassFromURI.getConstructor(long.class);

Method sumInstanceMethod = modelClassFromURI.getMethod("getValue");

Object object = ctor.newInstance(10L);

long result = (long) sumInstanceMethod.invoke(object);

System.out.println("Results from Model Class - " + result);
```

However, typically you only need to use this approach for POJO classes and services if you intend to deploy them from your code. Compute tasks can be deployed by name. Services can also be deployed using compute tasks.

### Compute Tasks

Here is how you can deploy a compute task:

```java
System.out.println("Results from compute - " +
                    ignite.compute().execute("com.gridgain.compute.TestComputeTask", "myCache"));
```

Compute tasks can be loaded by name. See example of this compute task in the [sample project](https://github.com/GridGain-Demos/uri-code-deployment-example).

### Services

You can deploy services in two ways:

1. From the compute task called by name:

   ```java
   package com.gridgain.service;

   import org.apache.ignite.Ignite;
   import org.apache.ignite.IgniteException;
   import org.apache.ignite.IgniteServices;
   import org.apache.ignite.cluster.ClusterNode;
   import org.apache.ignite.compute.ComputeJob;
   import org.apache.ignite.compute.ComputeJobResult;
   import org.apache.ignite.compute.ComputeJobResultPolicy;
   import org.apache.ignite.compute.ComputeTask;
   import org.apache.ignite.resources.IgniteInstanceResource;

   import java.util.Collections;
   import java.util.List;
   import java.util.Map;

   public class RedeployServiceComputeTask implements ComputeTask<String, Long> {
       @Override
       public Map<? extends ComputeJob, ClusterNode> map(List<ClusterNode> list, String arg) throws IgniteException {
           return Collections.singletonMap(new RedeployService(arg), list.iterator().next());
       }

       @Override
       public ComputeJobResultPolicy result(ComputeJobResult computeJobResult, List<ComputeJobResult> list) throws IgniteException {
           return ComputeJobResultPolicy.REDUCE;
       }

       @Override
       public Long reduce(List<ComputeJobResult> results) throws IgniteException {
           return results.iterator().next().getData();
       }

       private class RedeployService implements ComputeJob {
           /** */
           private String cacheName;

           /** */
           @IgniteInstanceResource
           private Ignite ignite;

           /** */
           public RedeployService(String arg) {
               this.cacheName = arg;
           }

           /** */
           @Override public void cancel() {
               // No-op.
           }

           /** */
           @Override public Long execute() {
               IgniteServices svcs = ignite.services();

               svcs.cancel("mySingleton");

               svcs.deployClusterSingleton("mySingleton", new TestService("myCache"));

               return 0L;
           }
       }
   }
   ```

1. Using a reflection:

   ```java
   //service loaded from the URI
   IgniteServices svcs = ignite.services();

   Class<?> serviceClassFromURI = Class.forName("com.gridgain.service.TestService", true, ignite.configuration()
   		.getDeploymentSpi()
   		.findResource("com.gridgain.service.TestService")
   		.getClassLoader());

   Constructor<?> serCtor = serviceClassFromURI.getConstructor(String.class);

   svcs.cancel("mySingleton");
   svcs.deployClusterSingleton("mySingleton", (Service) serCtor.newInstance("myCache"));
   ```

## Related

- [URI code deployment sample project](https://github.com/GridGain-Demos/uri-code-deployment-example) - The complete example referenced throughout this guide.
