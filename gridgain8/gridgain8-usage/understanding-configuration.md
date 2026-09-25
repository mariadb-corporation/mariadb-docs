---
description: >-
  Different ways of configuring a GridGain cluster, including Spring XML
  configuration and programmatic configuration.
---

# Understanding Configuration

This chapter explains different ways of configuring a GridGain cluster.

## Overview

When you start a GridGain node, you need to provide configuration parameters to the node.
Basically, all configuration parameters are defined in an instance of the `IgniteConfiguration` class.
You can set the parameters either programmatically or via an XML configuration file.
These 2 ways are fully interchangeable.

The XML configuration file is a Spring Bean definition file that must contain the `IgniteConfiguration` bean.
When starting a node from the command line, pass the configuration file as a parameter to the `ignite.sh|bat` script, as follows:

```shell
ignite.sh ignite-config.xml
```

If you don't specify a configuration file, the default file `{GRIDGAIN_HOME}/config/default-config.xml` is used.

## Spring XML Configuration

To create a configuration in a Spring XML format, you need to define the
`IgniteConfiguration` bean and set the parameters that you want to be different from the default. For detailed information on how to use XML Schema-based configuration, see the
[official Spring documentation](https://docs.spring.io/spring/docs/4.2.x/spring-framework-reference/html/xsd-configuration.html).

In the example below, we create an `IgniteConfiguration` bean, set the `workDirectory` property, and configure a [partitioned cache](../architecture/data-modeling/data-partitioning.md#partitioned).

```xml
<?xml version="1.0" encoding="UTF-8"?>

<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
        http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean class="org.apache.ignite.configuration.IgniteConfiguration">
        <property name="workDirectory" value="/path/to/work/directory"/>

        <property name="cacheConfiguration">
            <bean class="org.apache.ignite.configuration.CacheConfiguration">
                <!-- Set the cache name. -->
                <property name="name" value="myCache"/>
                <!-- Set the cache mode. -->
                <property name="cacheMode" value="PARTITIONED"/>
                <!-- Other cache parameters. -->
            </bean>
        </property>
    </bean>
</beans>
```

## Programmatic Configuration

Create an instance of the `IgniteConfiguration` class and set the required
parameters, as shown in the example below.

{% tabs %}
{% tab title="Java" %}
```java
IgniteConfiguration igniteCfg = new IgniteConfiguration();

//setting the work directory
igniteCfg.setWorkDirectory("/path/to/work/directory");

//defining a partitioned cache
CacheConfiguration cacheCfg = new CacheConfiguration("myCache");
cacheCfg.setCacheMode(CacheMode.PARTITIONED);

igniteCfg.setCacheConfiguration(cacheCfg);
```

See the `IgniteConfiguration` javadoc for the complete list of parameters.
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var igniteCfg = new IgniteConfiguration
{
    WorkDirectory = "/path/to/work/directory",
    CacheConfiguration = new[]
    {
        new CacheConfiguration
        {
            Name = "myCache",
            CacheMode = CacheMode.Partitioned
        }
    }
};
```

See the [API docs](https://www.gridgain.com/sdk/ce/8.10/dotnetdoc/api/Apache.Ignite.Core.IgniteConfiguration.html) for details.
{% endtab %}

{% tab title="C++" %}
```cpp
IgniteConfiguration cfg;

cfg.igniteHome = "/path/to/work/directory";
```
{% endtab %}
{% endtabs %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
