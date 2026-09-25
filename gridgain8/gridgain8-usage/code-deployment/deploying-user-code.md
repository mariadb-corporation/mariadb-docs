---
description: >-
  Deploying user code in GridGain by configuring UriDeploymentSpi to load
  libraries from a local directory or an HTTP(S) URL.
---

# Deploying User Code

In addition to [peer class loading](peer-class-loading.md), you can deploy user code by configuring `UriDeploymentSpi`. With this approach, you specify the location of your libraries in the node configuration.
GridGain scans the location periodically and redeploys the classes if they change.
The location may be a file system directory or an HTTP(S) location.
When GridGain detects that the libraries are removed from the location, the classes are undeployed from the cluster.

You can specify multiple locations (of different types) by providing both directory paths and http(s) URLs.

Items that can be deployed via `UriDeploymentSpi` are:

- GridGain compute tasks
- GridGain services
- Java POJO that aren't included in the classpath

For a more detailed description of all `UriDeploymentSpi`-based deployment cases, see [this tutorial](https://www.gridgain.com/docs/tutorials/code-deployment/code-deployment-tutorial).

## Deploying from a Local Directory

To deploy libraries from a file system directory, add the directory path to the list of URIs in the `UriDeploymentSpi` configuration.
The directory must exist on the nodes where it is specified and contain jar files with the classes you want to deploy.

{% hint style="info" %}
The path must be specified using the `file://` scheme.
You can specify different directories on different nodes.
{% endhint %}

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="deploymentSpi">
        <bean class="org.apache.ignite.spi.deployment.uri.UriDeploymentSpi">
            <property name="temporaryDirectoryPath" value="/tmp/temp_ignite_libs"/>
            <property name="uriList">
                <list>
                    <value>file://freq=2000@localhost/home/username/user_libs</value>
                </list>
            </property>
        </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();

UriDeploymentSpi deploymentSpi = new UriDeploymentSpi();

deploymentSpi.setUriList(Arrays.asList("file://freq=2000@localhost/home/username/user_libs"));

cfg.setDeploymentSpi(deploymentSpi);

try (Ignite ignite = Ignition.start(cfg)) {
    //execute the task represented by a class located in the "user_libs" directory 
    ignite.compute().execute("org.mycompany.HelloWorldTask", "My Args");
}
```
{% endtab %}

{% tab title="C#/.NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

You can pass the following parameter in the URL:

|Parameter | Description | Default Value|
|---|---|---|
| `freq` |  Scanning frequency in milliseconds. | `5000`|

## Deploying from a URL

To deploy libraries from an http(s) location, add the URL to the list of URIs in the `UriDeploymentSpi` configuration.

GridGain parses the HTML file to find the HREF attributes of all `<a>` tags on the page.
The references must point to the jar files you want to deploy.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="deploymentSpi">
        <bean class="org.apache.ignite.spi.deployment.uri.UriDeploymentSpi">
            <property name="temporaryDirectoryPath" value="/tmp/temp_ignite_libs"/>
            <property name="uriList">
                <list>
                    <value>http://username:password;freq=10000@www.mysite.com:110/ignite/user_libs</value>
                </list>
            </property>
        </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();

UriDeploymentSpi deploymentSpi = new UriDeploymentSpi();

deploymentSpi.setUriList(Arrays
        .asList("http://username:password;freq=10000@www.mysite.com:110/ignite/user_libs"));

cfg.setDeploymentSpi(deploymentSpi);

try (Ignite ignite = Ignition.start(cfg)) {
    //execute the task represented by a class located in the "user_libs" url 
    ignite.compute().execute("org.mycompany.HelloWorldTask", "My Args");
}
```
{% endtab %}

{% tab title="C#/.NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

You can pass the following parameter in the URL:

|Parameter | Description | Default Value|
|---|---|---|
| `freq` |  Scanning frequency in milliseconds. | `300000`|

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
