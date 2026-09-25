---
description: >-
  Cloud-based IP finders for GridGain node discovery, including Apache jclouds,
  Amazon S3, Amazon ELB, and Google Cloud Storage.
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

* Apache jclouds IP Finder (deprecated)
* Amazon S3 IP Finder
* Amazon ELB IP Finder
* Google Cloud Storage IP Finder

{% hint style="info" %}
Cloud-based IP Finders allow you to create your configuration once and reuse it for all instances.
{% endhint %}

## Apache jclouds IP Finder

{% hint style="warning" %}
The `ignite-cloud` module is deprecated and will be removed in a future release. Use [Amazon S3 IP Finder](#amazon-s3-ip-finder), [Amazon ELB Based Discovery](#amazon-elb-based-discovery), or [Google Compute Discovery](#google-compute-discovery) instead.
{% endhint %}

To mitigate the constantly changing IP addresses problem, GridGain supports
automatic node discovery by utilizing Apache jclouds multi-cloud toolkit
via `TcpDiscoveryCloudIpFinder`. For information about Apache jclouds
please refer to [jclouds.apache.org](https://jclouds.apache.org).

The IP finder forms nodes addresses by getting the private and public IP
addresses of all virtual machines running on the cloud and adding a port
number to them. The port is the one that is set with either
`TcpDiscoverySpi.setLocalPort(int)` or `TcpDiscoverySpi.DFLT_PORT`. This
way all the nodes can try to connect to any formed IP address and
initiate automatic node discovery.

Refer to [Apache jclouds providers section](https://jclouds.apache.org/reference/providers/#compute) to get the list of supported cloud platforms.

{% hint style="warning" %}
All virtual machines must start GridGain instances on the same port, otherwise they will not be able to discover each other using this IP finder.
{% endhint %}

Here is an example of how to configure Apache jclouds based IP finder:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
  <property name="discoverySpi">
    <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
      <property name="ipFinder">
        <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.cloud.TcpDiscoveryCloudIpFinder">
            <!-- Configuration for Google Compute Engine. -->
            <property name="provider" value="google-compute-engine"/>
            <property name="identity" value="YOUR_SERVICE_ACCOUNT_EMAIL"/>
            <property name="credentialPath" value="PATH_YOUR_PEM_FILE"/>
            <property name="zones">
            <list>
                <value>us-central1-a</value>
                <value>asia-east1-a</value>
            </list>
            </property>
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

TcpDiscoveryCloudIpFinder ipFinder = new TcpDiscoveryCloudIpFinder();

// Configuration for AWS EC2.
ipFinder.setProvider("aws-ec2");
ipFinder.setIdentity("yourAccountId");
ipFinder.setCredential("yourAccountKey");
ipFinder.setRegions(Collections.singletonList("us-east-1"));
ipFinder.setZones(Arrays.asList("us-east-1b", "us-east-1e"));

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

## Amazon S3 IP Finder

Amazon S3-based discovery allows GridGain nodes to register their IP
addresses on start-up in an Amazon S3 store. This way other nodes can try
to connect to any of the IP addresses stored in S3 and initiate
automatic node discovery. To use S3 based automatic node discovery,
you need to configure the TcpDiscoveryS3IpFinder type of ipFinder.

{% hint style="warning" %}
You must [enable the 'ignite-aws' module](../setup.md#enabling-modules).
{% endhint %}

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

{% hint style="warning" %}
You must [enable the 'ignite-aws' module](../setup.md#enabling-modules).
{% endhint %}

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
To use `TcpDiscoveryGoogleStorageIpFinder`, enable the `ignite-gce` [module](../setup.md#enabling-modules) in your application.
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

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
