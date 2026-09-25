---
description: >-
  How to obtain and launch the legacy GridGain AMI with GridGain Enterprise
  Edition preinstalled on Amazon EC2.
---

# Using Legacy GridGain AMI

GridGain provides an AMI with the latest version of GridGain Enterprise Edition preinstalled.

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

## Obtaining GridGain AMI

Visit the [GridGain product page](https://aws.amazon.com/marketplace/pp/B08D8P2QHG) on AWS Marketplace and launch the AMI from there.

## Configuring Security Group

The security group configuration is the same as for a manual EC2 installation. See [Configuring Security Group](manual-install-on-ec2.md#configuring-security-group).
## Launching GridGain Nodes

Connect to the EC2 instance via ssh as per the AWS documentation.
Make sure to provide the same credentials that were used to launch the EC2 instance.

The default user name is 'gridgain'.
The ssh command would look like (change the IP address with the actual public IP of your image):

```shell
ssh -i your_key.pem gridgain@54.173.158.228
```

You can change the user name after first login, if needed.
For information on how to create a custom user name, see [AWS documentation for Linux user accounts](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/managing-users.html).

GridGain is installed in the `/home/gridgain/gridgain-enterprise-8.10` directory. You can start it with the default settings by running the following command:

```shell
$ gridgain-enterprise-8.10/bin/ignite.sh
```

If you use a custom GridGain configuration, make sure that the `IgniteConfiguration` instance contains the following attribute:

```xml
<property name="userAttributes">
    <map>
        <entry key="iaas.vendor" value="amazonaws"/>
    </map>
</property>
```

This attribute is required when using GridGain Enterprise Edition license.

## Configuring Discovery

Discovery configuration is the same as for a manual EC2 installation. See [Configuring Discovery](manual-install-on-ec2.md#configuring-discovery).
## Troubleshooting Your AWS Deployment

GridGain Systems offers 14 days of free [GridGain Standard Enterprise Support](https://www.gridgain.com/partners/aws-support) to new organizations that deploy the GridGain Enterprise Edition on AWS through the AWS Marketplace. This offer is limited to one 14-day period of free support per organization. Our standard annual support subscriptions are available at any time. Just complete the form to register for your 14 days of complementary support services.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
