---
description: >-
  How to specify, switch, update, and manage GridGain Enterprise and Ultimate
  Edition license files, including Java dependencies and license expiration.
---

# Licensing

You will need a new license file when installing (or updating to) GridGain Enterprise Edition (EE) or Ultimate Edition (UE).
To get a new license file, contact your GridGain representative.

## Specifying License

There are several ways you can specify a license file:

* If you launch GridGain nodes by executing `ignite.sh`, you can replace the default license file in the GridGain installation directory with your license file. Place the license file in the `$GRIDGAIN_HOME/gridgain-license.xml` path.
* You can also manually specify the path to your licence file in configuration. This url can be on a local machine, HTTP or FTP url. Specify the `GridGainConfiguration.licenseUrl` property in the node configuration file:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="pluginConfigurations">
        <list>
            <bean class="org.gridgain.grid.configuration.GridGainConfiguration">
                <property name="licenseUrl" value="/my/directory/gridgain-license.xml"/>
            </bean>
        </list>
    </property>
</bean>
```
{% endtab %}
{% tab title="Java" %}
```java
GridGainConfiguration ggCfg = new GridGainConfiguration();

ggCfg.setLicenseUrl("/my/directory/gridgain-license.xml");

IgniteConfiguration cfg = new IgniteConfiguration();

cfg.setPluginConfigurations(ggCfg);

Ignite ignite = Ignition.start(cfg);
```
{% endtab %}
{% tab title=".NET/C#" %}
```csharp
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

  The license URL can be:

  * An absolute path on the file system;
  * A relative path, which is interpreted relative to the directory from where you launch the node.
  * A URL to a HTTP resource.

* If you are running  GridGain in kubernetes, you can also provide a license by using ConfigMap. Here is an example of how to do this:

```xml
apiVersion: v1
kind: ConfigMap
metadata:
  name: gridgain-license
  namespace: gridgain
data:
  gridgain-license.xml: |
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <gridgain-license version="2.1">
      <id>6952079f-b9c0-4cba-9825-4d7cd5f26828</id>
      <issue-date>07/27/2023</issue-date>
      <maintenance-time>0</maintenance-time>
      <user-org>user</user-org>
      <license-note>sample license</license-note>
      <type>ENT</type>
      <expire-date>07/27/2024</expire-date>
      <max-nodes>0</max-nodes>
      <max-cpus>0</max-cpus>
      <max-computers>0</max-computers>
      <grace-period>4320</grace-period>
      <max-uptime>0</max-uptime>
      <signature>302D0215001135F611860445D3223EB07EF54B42875EDFC1FE021402B33AE13BE4CB0B98965C5A722E17AC5C7B3B31</signature>
      <enabled-feature name="ultimate"/>
    </gridgain-license>
```

## Switching Between GridGain Editions

The easiest way to transition between GridGain editions is to:

1. Get a new license from GridGain.
2. Download new binaries from the GridGain site and unzip them into a new directory.
3. Put your license file into the root folder of your new installation.

{% hint style="info" %}
GridGain Enterprise and Ultimate come with a 30-day trial license.
{% endhint %}

If you switch between GridGain editions, you must update your dependencies to match. See [GridGain Editions and Java Dependencies](#gridgain-editions-and-java-dependencies).

## GridGain Editions and Java Dependencies

When switching between GridGain Enterprise and Ultimate Editions, you need to update your dependencies in your `.pom` file.

### Base Dependencies

All GridGain projects require the GridGain Maven repository. Add it to your `.pom` file:

```xml
<repositories>
    <repository>
        <id>GridGain External Repository</id>
        <url>https://www.gridgainsystems.com/nexus/content/repositories/external</url>
    </repository>
</repositories>
```

Then add the base `ignite-core` dependency:

```xml
<dependency>
    <groupId>org.gridgain</groupId>
    <artifactId>ignite-core</artifactId>
    <version>${gridgain.version}</version>
</dependency>
```

Set `gridgain.version` to the GridGain version you are using (`8.10`, for example).

### Enterprise Edition Dependencies

GridGain Enterprise Edition requires the `gridgain-core` dependency in addition to the base dependencies:

```xml
<dependency>
    <groupId>org.gridgain</groupId>
    <artifactId>gridgain-core</artifactId>
    <version>${gridgain.version}</version>
</dependency>
```

Where `gridgain.version` is 8.x.x.

### Ultimate Edition Dependencies

GridGain Ultimate Edition requires the `gridgain-ultimate` dependency in addition to the Enterprise Edition dependencies:

```xml
<dependency>
    <groupId>org.gridgain</groupId>
    <artifactId>gridgain-ultimate</artifactId>
    <version>${gridgain.version}</version>
</dependency>
```

Where `gridgain.version` is 8.x.x.

## License Expiration

A license is valid through the end of the day defined in its `expire-date` field and stops working at `00:00:00` on the following day.
For example, a license that expires at `08/11/2026` is valid for the whole of August 11 and stops working at `00:00:00` on August 12.

All dates in the license file, including `issue-date` and `expire-date`, are interpreted in UTC, not in the local time zone of the node that reads the file.
Every node in the cluster therefore treats the license as expiring at the same moment, regardless of the time zone it runs in.

GridGain logs a warning once a day while the expiration date is less than 90 days away.

## Updating GridGain License

When you need to provide a new license to a running cluster, be it due to an update to a different edition or the old license running out, you need to provide GridGain with a new license file.

### Update with Downtime

If you can afford the cluster downtime, restart each node in cluster while updating the license file for them.

### Update without Downtime

If downtime is not acceptable for the cluster, there are ways to update the license on the running cluster.

* If you provide a URL to a license file, you can hotswap the license file on each node. The node will automatically reload the license file after the change. GridGain automatically handles having different licenses on the cluster and keeps the cluster running for the duration of the update.
* If your cluster runs in Kubernetes and you use ConfigMap to specify the license file, change the license in ConfigMap. The nodes running in the cluster will automatically update the license once the new ConfigMap is provided.

  {% hint style="info" %}
  Containers that use ConfigMap as a subPath will not receive the update. In this case, use the rolling update option.
  {% endhint %}

* If neither of the above options is possible, you can perform the update on a per-node basis with rolling restart of cluster nodes. Note that this will negatively affect performance for the duration of the update. For detailed instructions on performing rolling restart, see [Performing a Rolling Restart](upgrade/rolling-upgrades.md) section.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
