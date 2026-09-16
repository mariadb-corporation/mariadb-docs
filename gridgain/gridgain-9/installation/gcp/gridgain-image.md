---
description: >-
  Launch GridGain 9 on Google Cloud Platform from the preinstalled OS image,
  including instance sizing, OS Login, IAM roles, firewall rules, and discovery.
---

# GridGain 9 GCP OS Image (AMI)

## Using GridGain 9 OS Image

GridGain provides an OS Image (Compute Engine resource) with the latest version of GridGain 9 preinstalled.

## Prerequisites

An existing GCP account and project are required.

## Considerations

Choose the right type of instances that suits your needs. GridGain system requirements scale depending on the size of your cluster.

When choosing instance type, consider the following points:

- *RAM:* If you are going to use GridGain as an in-memory storage, make sure to select an instance with enough RAM to fit all your data.
- *Disk space:* If you are launching a cluster with a [persistent storage](../../administrators-guide/storage/engines/aipersist.md), provide enough size to accommodate all your data when configuring the instance's volume. You may want to check *Keep disk on deletion* option for your storage.
- *Networking:* GridGain nodes discover and communicate with each other by TCP/IP. A number of ports must be open for this communication.

## Selecting and obtaining GridGain OS Image

Visit the product page on GCP Marketplace, corresponding to the edition you need, and launch the AMI from there

## Providing a license

There are 3 versions of GridGain 9 OS Image:

- Free version without a licence. To start the cluster, get a [trial license](https://www.gridgain.com/tryfree) and provide it during cluster start.
- Enterprise version with the included license that can be bought on GCP Marketplace.
- Ultimate version with the included license that can be bought on GCP Marketplace.

## Configuring OS Login

To enable OS Login for a single VM, set the following values in the interface, or through a terraform parameter:

- Enable OS Login:
  - Key: `enable-oslogin`
  - Value: `TRUE`
- (Optional) Enable two-factor authentication:
  - Key: `enable-oslogin-2fa`
  - Value: `TRUE`

## Configuring IAM Roles

If you are using a dedicated [service account](https://cloud.google.com/iam/docs/service-account-overview) for a compute instance, you may need to attach the following roles:

- `roles/logging.logWriter` - to provide permissions to write log entries
- `roles/monitoring.metricWriter` - to provide permissions needed by the Cloud Monitoring agent and other systems that send metrics
- `roles/iap.tunnelResourceAccessor` - to allow access SSH Tunnel resources which use Identity-Aware Proxy

## Configuring Firewall policies

For GridGain to work properly you must allow connection to the following ports:

| Protocol | Port | Description |
| --- | --- | --- |
| TCP | 3344 | Communication port for clustering. |
| TCP | 10300 (10400 for SSL) | Cluster management. |
| TCP | 10800 | REST API requests. |
| SSH | 22 | (Optional) SSH access to the cluster. |

These are the default ports that GridGain nodes use for discovery and communication purposes. If you want to use values other than the default ones, open them.

## Launching GridGain Nodes

You can use [GridGain 9 Terraform GCP Module](https://registry.terraform.io/modules/gridgain/gridgain9/google/latest) to create compute instances and all supplementary resources (VPC, networks, KMS, etc). Please refer to GridGain 9 Terraform GCP Module documentation.

Connect to the compute instance via OS Login or with provided SSH key:

- Connect to the VM using OS Login: `gcloud compute ssh --project=PROJECT_ID --zone=ZONE VM_NAME`
- Connect to the VM using provided SSH key: `ssh -i your_key.pem gridgain@<public-ip>`

GridGain is installed as [RPM](../deb-rpm.md). It provides [systemd service](../deb-rpm.md#running-gridgain-as-a-service) `gridgain9db`, which can be managed using systemctl.

Because the service is enabled by default, it should start automatically and be up and running soon after the instance launch.

## Configuring Discovery

Cluster nodes launched in different compute instances must be able to connect to each other. Please refer to [Network Configuration](../../administrators-guide/config/node-config.md#network-configuration) to let cluster nodes discover each other.

## Troubleshooting Your GCP Deployment

If you assigned [logging.logWriter](https://cloud.google.com/iam/docs/roles-permissions/logging) role to the attached service account, instances will publish logs to the log buckets and will be available for viewing via [Logs Explorer](https://cloud.google.com/logging/docs/view/logs-explorer-interface) interface. Ops-Agent on the instances is already pre-configured to publish GridGain node logs.
