---
description: >-
  Cloud-based IP finders for GridGain node discovery, including Amazon S3,
  Amazon ELB, and Google Cloud Storage.
---

# Discovery in the Cloud

Nodes discovery on a cloud platform is usually proven to be more
challenging because most virtual environments are subject to the
following limitations:

* Multicast is disabled;
* TCP addresses change every time a new image is started.

Although you can use TCP-based discovery in the absence of the
Multicast, you still have to deal with constantly changing IP addresses.
This causes a serious inconvenience and makes configurations based on
static IPs virtually unusable in such environments.

To mitigate the constantly changing IP addresses problem, GridGain
supports a number of IP finders designed to work in the cloud:

* Amazon S3 IP Finder
* Amazon ELB IP Finder
* Google Cloud Storage IP Finder

{% hint style="info" %}
Cloud-based IP Finders allow you to create your configuration once and reuse it for all instances.
{% endhint %}

## Amazon S3 IP Finder

Amazon S3-based discovery allows GridGain nodes to register their IP
addresses on start-up in an Amazon S3 store. This way other nodes can try
to connect to any of the IP addresses stored in S3 and initiate
automatic node discovery. To use S3 based automatic node discovery,
you need to configure the TcpDiscoveryS3IpFinder type of ipFinder.

{% tabs %}
{% tab title="Current" %}
{% hint style="info" %}
From GridGain 8.10:
{% endhint %}

The `ignite-aws` module is removed. To use the S3 IP finder, add the Apache `ignite-aws-ext` extension (`org.apache.ignite:ignite-aws-ext`) and its dependencies to the classpath of every node, including thick clients. The classes keep their `org.apache.ignite.*` package names, so the configuration examples below do not change. Without the extension, a configuration that references `TcpDiscoveryS3IpFinder` fails with `ClassNotFoundException`.

If you upgrade from 8.9.x and use `AwsKmsEncryptionService`, read the upgrade notes in the 8.9.x tab first.

{% hint style="warning" %}
Version 1.0.0 of `ignite-aws-ext` depends on older third-party libraries than `ignite-aws`, and some of them have known vulnerabilities. Check the extension's dependencies against your security policy before you use it.

The KMS support in the extension works only with AWS Encryption SDK 1.x. With AWS Encryption SDK 2.x, it fails with `NoSuchMethodError`.
{% endhint %}
{% endtab %}

{% tab title="8.9.x" %}
{% hint style="info" %}
In GridGain 8.9.x:
{% endhint %}

The S3 IP finder is part of the `ignite-aws` module, which is in the `libs/optional` folder of the distribution. [Enable the module](../../gridgain8-development/project-setup.md#enabling-modules) before you use the IP finder. In a Maven project, add the `org.gridgain:ignite-aws` dependency.

Starting with GridGain 8.9.39, the module is deprecated. Its replacement is the Apache `ignite-aws-ext` extension (`org.apache.ignite:ignite-aws-ext`). If you switch, do not use both modules on the same node: remove `ignite-aws` first (the `libs/ignite-aws` folder of a standalone node, or the `ignite-aws` dependency of a Maven project), and then add `ignite-aws-ext`. If both are on the classpath, two jars define the same classes, and the classpath order decides which one is loaded.

{% hint style="warning" %}
This applies only if you use `AwsKmsEncryptionService`. The S3 IP finder without KMS has no such restriction.

If you switch from `ignite-aws` to `ignite-aws-ext`, for example when you upgrade to 8.10, the switch is not a rolling upgrade. The extension reads only the data that it encrypted itself, so nodes that use the two modules cannot read each other's entries in the S3 bucket. Switch all nodes at the same time, including thick clients, and set a new `keyPrefix` on the IP finder. The extension also has only `setRegion(Region)` and no `setRegion(String)`, so a Spring XML file that passes the region as a string must use a `RegionUtils.getRegion` factory bean instead.
{% endhint %}
{% endtab %}
{% endtabs %}

Here is an example of how to configure Amazon S3 based IP finder:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

  <property name="discoverySpi">
    <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
      <property name="ipFinder">
        <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.s3.TcpDiscoveryS3IpFinder">
          <property name="awsCredentials" ref="aws.creds"/>
          <property name="bucketName" value="YOUR_BUCKET_NAME"/>
        </bean>
      </property>
    </bean>
  </property>
</bean>

<!-- AWS credentials. Provide your access key ID and secret access key. -->
<bean id="aws.creds" class="com.amazonaws.auth.BasicAWSCredentials">
  <constructor-arg value="YOUR_ACCESS_KEY_ID" />
  <constructor-arg value="YOUR_SECRET_ACCESS_KEY" />
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
TcpDiscoverySpi spi = new TcpDiscoverySpi();

BasicAWSCredentials creds = new BasicAWSCredentials("yourAccessKey", "yourSecreteKey");

TcpDiscoveryS3IpFinder ipFinder = new TcpDiscoveryS3IpFinder();
ipFinder.setAwsCredentials(creds);
ipFinder.setBucketName("yourBucketName");

spi.setIpFinder(ipFinder);

IgniteConfiguration cfg = new IgniteConfiguration();

// Override default discovery SPI.
cfg.setDiscoverySpi(spi);

// Start a node.
Ignition.start(cfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

You can also use **Instance Profile** for AWS credentials provider.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

  <property name="discoverySpi">
    <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
      <property name="ipFinder">
        <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.s3.TcpDiscoveryS3IpFinder">
          <property name="awsCredentialsProvider" ref="aws.creds"/>
          <property name="bucketName" value="YOUR_BUCKET_NAME"/>
        </bean>
      </property>
    </bean>
  </property>
</bean>

<!-- Instance Profile based credentials -->
<bean id="aws.creds" class="com.amazonaws.auth.InstanceProfileCredentialsProvider">
  <constructor-arg value="false" />
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
TcpDiscoverySpi spi = new TcpDiscoverySpi();

AWSCredentialsProvider instanceProfileCreds = new InstanceProfileCredentialsProvider(false);

TcpDiscoveryS3IpFinder ipFinder = new TcpDiscoveryS3IpFinder();
ipFinder.setAwsCredentialsProvider(instanceProfileCreds);
ipFinder.setBucketName("yourBucketName");

spi.setIpFinder(ipFinder);

IgniteConfiguration cfg = new IgniteConfiguration();

// Override default discovery SPI.
cfg.setDiscoverySpi(spi);

// Start a node.
Ignition.start(cfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Amazon ELB Based Discovery

AWS ELB-based IP finder does not require nodes to register their IP
addresses. The IP finder automatically fetches addresses of all the
nodes connected under an ELB and uses them to connect to the cluster.

{% hint style="info" %}
Unlike in [Amazon S3 IP Finder](#amazon-s3-ip-finder), only `basic` option is available for AWS credentials (no `instanceprofile`).
{% endhint %}

To use ELB based automatic node discovery, you need to configure the
`TcpDiscoveryElbIpFinder` type of `ipFinder`.

{% tabs %}
{% tab title="Current" %}
{% hint style="info" %}
From GridGain 8.10:
{% endhint %}

The `ignite-aws` module is removed. Add the Apache `ignite-aws-ext` extension (`org.apache.ignite:ignite-aws-ext`) to the classpath of every node. See [Amazon S3 IP Finder](#amazon-s3-ip-finder).
{% endtab %}

{% tab title="8.9.x" %}
{% hint style="info" %}
In GridGain 8.9.x:
{% endhint %}

The ELB IP finder is part of the `ignite-aws` module. [Enable the module](../../gridgain8-development/project-setup.md#enabling-modules) before you use it. Starting with GridGain 8.9.39, the module is deprecated. For the replacement, see [Amazon S3 IP Finder](#amazon-s3-ip-finder).
{% endtab %}
{% endtabs %}

Here is an example of how to configure Amazon ELB based IP finder:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

  <property name="discoverySpi">
    <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
      <property name="ipFinder">
        <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.elb.TcpDiscoveryElbIpFinder">
          <property name="credentialsProvider">
              <bean class="com.amazonaws.auth.AWSStaticCredentialsProvider">
                  <constructor-arg ref="aws.creds"/>
              </bean>
          </property>
          <property name="region" value="YOUR_ELB_REGION_NAME"/>
          <property name="loadBalancerName" value="YOUR_AWS_ELB_NAME"/>
        </bean>
      </property>
    </bean>
  </property>
</bean>

<!-- AWS credentials. Provide your access key ID and secret access key. -->
<bean id="aws.creds" class="com.amazonaws.auth.BasicAWSCredentials">
  <constructor-arg value="YOUR_ACCESS_KEY_ID" />
  <constructor-arg value="YOUR_SECRET_ACCESS_KEY" />
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
TcpDiscoverySpi spi = new TcpDiscoverySpi();

BasicAWSCredentials creds = new BasicAWSCredentials("yourAccessKey", "yourSecreteKey");

TcpDiscoveryElbIpFinder ipFinder = new TcpDiscoveryElbIpFinder();
ipFinder.setRegion("yourElbRegion");
ipFinder.setLoadBalancerName("yourLoadBalancerName");
ipFinder.setCredentialsProvider(new AWSStaticCredentialsProvider(creds));

spi.setIpFinder(ipFinder);

IgniteConfiguration cfg = new IgniteConfiguration();

// Override default discovery SPI.
cfg.setDiscoverySpi(spi);

// Start the node.
Ignition.start(cfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Google Compute Discovery

GridGain supports automatic node discovery by utilizing Google Cloud Storage store. This mechanism is implemented in `TcpDiscoveryGoogleStorageIpFinder`. On start-up, each node registers its IP address in the storage and discovers other nodes by reading the storage.

{% hint style="warning" %}
To use `TcpDiscoveryGoogleStorageIpFinder`, enable the `ignite-gce` [module](../../gridgain8-development/project-setup.md#enabling-modules) in your application.
{% endhint %}

Here is an example of how to configure Google Cloud Storage based IP finder:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

  <property name="discoverySpi">
    <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
      <property name="ipFinder">
        <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.gce.TcpDiscoveryGoogleStorageIpFinder">
          <property name="projectName" value="YOUR_GOOGLE_PLATFORM_PROJECT_NAME"/>
          <property name="bucketName" value="YOUR_BUCKET_NAME"/>
          <property name="serviceAccountId" value="YOUR_SERVICE_ACCOUNT_ID"/>
          <property name="serviceAccountP12FilePath" value="PATH_TO_YOUR_PKCS12_KEY"/>
        </bean>
      </property>
    </bean>
  </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
TcpDiscoverySpi spi = new TcpDiscoverySpi();

TcpDiscoveryGoogleStorageIpFinder ipFinder = new TcpDiscoveryGoogleStorageIpFinder();

ipFinder.setServiceAccountId("yourServiceAccountId");
ipFinder.setServiceAccountP12FilePath("pathToYourP12Key");
ipFinder.setProjectName("yourGoogleClourPlatformProjectName");

// Bucket name must be unique across the whole Google Cloud Platform.
ipFinder.setBucketName("your_bucket_name");

spi.setIpFinder(ipFinder);

IgniteConfiguration cfg = new IgniteConfiguration();

// Override default discovery SPI.
cfg.setDiscoverySpi(spi);

// Start the node.
Ignition.start(cfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}
