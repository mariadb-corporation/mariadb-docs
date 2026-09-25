---
description: >-
  How to select, obtain, and launch the GridGain AMI from AWS Marketplace,
  provide a license, configure IAM roles, and set up node discovery on EC2.
---

# Using GridGain AMI

GridGain provides an AMI with the latest version of GridGain preinstalled.

## Prerequisites

- An existing AWS account

## Considerations

Choose the right type of instances that suit your needs. The following instance types are supported:

| Instance type family | Instance type |
|---|---|
| M6i | m6i.xlarge, m6i.2xlarge, m6i.4xlarge, m6i.8xlarge, m6i.12xlarge, m6i.16xlarge, m6i.24xlarge, m6i.32xlarge, m6i.metal |
| T3 | t3.large, t3.xlarge, t3.2xlarge |
| C5 | c5.large, c5.xlarge, c5.2xlarge, c5.4xlarge, c5.9xlarge, c5.12xlarge, c5.18xlarge, c5.24xlarge, c5.metal |
| C5d | c5d.large, c5d.xlarge, c5d.2xlarge, c5d.4xlarge, c5d.9xlarge, c5d.12xlarge, c5d.18xlarge, c5d.24xlarge, c5d.metal |
| R5 | r5.large, r5.xlarge, r5.2xlarge, r5.4xlarge, r5.8xlarge, r5.12xlarge, r5.16xlarge, r5.24xlarge, r5.metal |
| R5d | r5d.large, r5d.xlarge, r5d.2xlarge, r5d.4xlarge, r5d.8xlarge, r5d.12xlarge, r5d.16xlarge, r5d.24xlarge, r5d.metal |
| R6i | r6i.large, r6i.xlarge, r6i.2xlarge, r6i.4xlarge, r6i.8xlarge, r6i.12xlarge, r6i.16xlarge, r6i.24xlarge, r6i.32xlarge, r6i.metal |

Consider the following points:

- **RAM:** If you are going to use GridGain as an in-memory storage, make sure to select an instance with enough RAM to fit all your data.
- **Disk space:** If you are launching a cluster with a [persistent storage](../../../architecture/storage/native-persistence.md), provide enough size to accommodate all your data when configuring the instance's volume.

  You may want to uncheck the **Delete on Termination** option for your storage.
- **Networking:** GridGain nodes discover and communicate with each other by TCP/IP. A number of ports must be open for this communication. See [Configuring Security Group](#configuring-security-group).

Visit our [Capacity Planning](../../../ha-and-performance/capacity-planning.md) page for information about ways to estimate hardware requirements for your use case.

## Selecting and Obtaining GridGain AMI

Visit the product page on AWS Marketplace, corresponding to the edition you need, and launch the AMI from there.

| Image Edition | Amazon Marketplace Link |
|---|---|
| BYOL (Bring Your Own License) | https://aws.amazon.com/marketplace/pp/prodview-mhesijebeozle |
| Enterprise | https://aws.amazon.com/marketplace/pp/prodview-exrjq4ox4kuim |
| Ultimate | https://aws.amazon.com/marketplace/pp/prodview-irktgogccfkhs |

## Providing a license

License is included in Enterprise and Ultimate edition AMI images. BYOL (Bring Your Own License) AMI image expects a [license](../../licensing.md) at `/opt/gridgain/config/license.xml`.

[Instance userdata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html) can be used to provide license during instance startup:

```
#cloud-config
# vim: syntax=yaml

write_files:
  - path: /opt/gridgain/config/license.xml
    content: |
      <license>
```

The BYOL image starts the GridGain edition that matches the license you provide. For more information about GridGain licenses, see [GridGain Licensing](../../licensing.md).

## Configuring IAM Role and Instance Profile

Optionally, you can attach IAM role to instances via Instance Profile. These are recommended policies to attach to this role:

- `arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore` - to allow [Amazon Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) to manage the instance and to allow connections from [Amazon Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html).
- `arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy` - to allow [CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) on the instance write logs to [CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html).

Additionally, we recommend you to attach following permissions:

### For Amazon ELB

Set the following permissions for [automatic discovery using Amazon ELB](../../../gridgain8-usage/clustering/discovery-in-the-cloud.md#amazon-elb-based-discovery):

```
elasticloadbalancing:DescribeLoadBalancerAttributes
elasticloadbalancing:DescribeLoadBalancers
elasticloadbalancing:DescribeTags
elasticloadbalancing:DescribeLoadBalancerPolicies
elasticloadbalancing:DescribeLoadBalancerPolicyTypes
elasticloadbalancing:DescribeInstanceHealth
elasticloadbalancing:DescribeAccountLimits
elasticloadbalancing:DescribeListenerAttributes
elasticloadbalancing:DescribeListenerCertificates
elasticloadbalancing:DescribeListeners
elasticloadbalancing:DescribeTargetGroupAttributes
elasticloadbalancing:DescribeTargetGroups
elasticloadbalancing:DescribeTargetHealth
elasticloadbalancing:DescribeTrustStoreAssociations
elasticloadbalancing:DescribeTrustStoreRevocations
elasticloadbalancing:DescribeTrustStores
elasticloadbalancing:GetResourcePolicy
```

### For S3 Bucket

Set the following permissions for [automatic discovery using S3 bucket](../../../gridgain8-usage/clustering/discovery-in-the-cloud.md#amazon-s3-ip-finder):

```
s3:ListBucket
s3:PutObject
s3:PutObjectAcl
s3:GetObject
s3:GetObjectAcl
s3:DeleteObject
```

## Configuring Security Group

The security group configuration is the same as for a manual EC2 installation. See [Configuring Security Group](manual-install-on-ec2.md#configuring-security-group).
## Launching GridGain Nodes

You can use [GridGain Terraform AWS Module](https://registry.terraform.io/modules/gridgain/gridgain/aws/latest) to create EC2 instances and all supplementary resources (VPC, EIPs, S3 bucket, ELB, etc). See [GridGain Terraform AWS Module](terraform.md) documentation for more details.

Connect to the EC2 instance via ssh as per the AWS documentation.
Make sure to provide the same credentials that were used to launch the EC2 instance.

The default user name is `gg_rw_user`.
The ssh command would look like (change the IP address with the actual public IP of your image):

```shell
ssh -i your_key.pem gg_rw_user@54.173.158.228
```

You can change the user name after first login, if needed.
For information on how to create a custom user name, see [AWS documentation for Linux user accounts](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/managing-users.html).

GridGain is installed in the `/opt/gridgain/binaries/latest/` directory. You can start it with the default settings by running the following command:

```shell
$ systemctl start gridgain
```

Because the service is enabled by default, it should start automatically and be up and running soon after the instance launch.

## Configuring Discovery

Cluster nodes launched in different EC2 instances must be able to connect to each other.
This is achieved by configuring the discovery mechanisms on each node. There are two ways you can do that:

- Manually provide the IP addresses of all instances in the [Static IP Finder configuration](../../../gridgain8-usage/clustering/tcp-ip-discovery.md) of each node.
- Use one of the [IP Finders designed for AWS](../../../gridgain8-usage/clustering/discovery-in-the-cloud.md).

{% hint style="info" %}
We recommend using one of the [Amazon IP Finders](../../../gridgain8-usage/clustering/discovery-in-the-cloud.md).
They allow you to add more instances to the cluster without updating the discovery configuration of the running nodes.
{% endhint %}

### Discovering Nodes by TCP/IP

To configure discovery by TCP/IP, specify the private IP addresses of each instance in the node's configuration file. Configuration file used by default is stored in `/opt/gridgain/config/server.xml`.

```xml
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:util="http://www.springframework.org/schema/util"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="         http://www.springframework.org/schema/beans
    http://www.springframework.org/schema/beans/spring-beans.xsd
    http://www.springframework.org/schema/util
    http://www.springframework.org/schema/util/spring-util.xsd">
    <bean class="org.apache.ignite.configuration.IgniteConfiguration">

        <!-- other properties -->

        <!-- Discovery configuration -->
        <property name="discoverySpi">
            <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
                <property name="ipFinder">
                    <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                        <property name="addresses">
                            <list>
                                <value>172.31.28.36</value>
                                <value>172.31.23.105</value>
                            </list>
                        </property>
                    </bean>
                </property>
            </bean>
        </property>
    </bean>
</beans>
```

{% hint style="info" %}
Make sure that the IP finder configuration of at least one node contains the local IP address of the instance. You can specify either the private IP address or `127.0.0.1`.
{% endhint %}

1. Connect to each instance via ssh.
2. Stop the service: `systemctl stop gridgain`.
3. Adjust the configuration.
4. Restart the service: `systemctl start gridgain`.

### Automatic Discovery Using Amazon S3

You can use the [Amazon S3 IP Finder](../../../gridgain8-usage/clustering/discovery-in-the-cloud.md#amazon-s3-ip-finder) to configure automatic discovery of nodes.

The 'ignite-aws' module is already enabled.

Go to the [Amazon S3 Management Console](https://s3.console.aws.amazon.com/s3/home) and create a simple bucket with default settings. Our bucket is named 'gg-ip-finder-bucket':

![](../../../.gitbook/assets/gg8-aws-s3-bucket.png)

Provide the name of the bucket in the node's configuration file, `/opt/gridgain/config/server.xml`, as follows:

```xml
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:util="http://www.springframework.org/schema/util"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="         http://www.springframework.org/schema/beans
    http://www.springframework.org/schema/beans/spring-beans.xsd
    http://www.springframework.org/schema/util
    http://www.springframework.org/schema/util/spring-util.xsd">
    <bean class="org.apache.ignite.configuration.IgniteConfiguration">
        <!-- other properties -->
        <property name="discoverySpi">
            <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
                <property name="ipFinder">
                    <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.s3.TcpDiscoveryS3IpFinder">
                        <property name="awsCredentials" ref="aws.creds"/>
                        <property name="bucketName" value="gg-ip-finder-bucket"/>
                    </bean>
                </property>
            </bean>
        </property>
    </bean>
    <!-- AWS credentials. Provide your access key ID and secret access key. -->
    <bean class="com.amazonaws.auth.BasicAWSCredentials" id="aws.creds">
        <constructor-arg value="YOUR_ACCESS_KEY_ID"/>
        <constructor-arg value="YOUR_SECRET_ACCESS_KEY"/>
    </bean>
</beans>
```

Replace the `YOUR_ACCESS_KEY_ID` and `YOUR_SECRET_ACCESS_KEY` values with your access key and secret access key. Refer to the [Where's My Secret Access Key?](https://aws.amazon.com/blogs/security/wheres-my-secret-access-key/) page for details.

1. Connect to each instance via ssh.
2. Stop the service: `systemctl stop gridgain`.
3. Adjust the configuration.
4. Restart the service: `systemctl start gridgain`.

## Troubleshooting Your AWS Deployment

GridGain Systems offers 14 days of free [GridGain Standard Enterprise Support](https://www.gridgain.com/partners/aws-support) to new organizations that deploy the GridGain Enterprise Edition on AWS through the AWS Marketplace. This offer is limited to one 14-day period of free support per organization. Our standard annual support subscriptions are available at any time. Just complete the form to register for your 14 days of complementary support services.

To receive better support, provide node logs. If you provided [CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) policy, instances will publish logs to [CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html). Agent on the instances is already pre-configured to publish GridGain node logs. Pre-configured loggroup is `/gridgain/<EDITION>/8.10`, where &lt;EDITION&gt; is the edition of your GridGain instance.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
