---
description: 'Step 2: Configure Shared Local Storage'
---

# Step 2: Configure Shared Local Storage

## Overview

This page details step 2 of the 9-step procedure "Deploy ColumnStore Object Storage Topology".

This step configures shared local storage on systems hosting Enterprise ColumnStore.

{% include "../../../../../.gitbook/includes/the-instructions-were-teste....md" %}

Interactive commands are detailed. Alternatively, the described operations can be performed using automation.

## Directories for Shared Local Storage

In a ColumnStore Object Storage topology, MariaDB Enterprise ColumnStore requires the Storage Manager directory to be located on shared local storage.

The Storage Manager directory is at the following path:

* `/var/lib/columnstore/storagemanager`

The Storage Manager directory must be mounted on every ColumnStore node.

## Choose a Shared Local Storage Solution

Select a Shared Local Storage solution for the Storage Manager directory:

* [EBS (Elastic Block Store) Multi-Attach](step-2-configure-shared-local-storage.md#configure-ebs-multi-attach)
* [EFS (Elastic File System)](step-2-configure-shared-local-storage.md#configure-elastic-file-system-efs)
* [Filestore](step-2-configure-shared-local-storage.md#configure-filestore)
* [GlusterFS](step-2-configure-shared-local-storage.md#configure-glusterfs)
* [NFS (Network File System)](step-2-configure-shared-local-storage.md#configure-network-file-system-nfs)

For additional information, see "[Shared Local Storage Options](step-2-configure-shared-local-storage.md#choose-a-shared-local-storage-solution)".

## Configure EBS Multi-Attach

EBS is a high-performance block-storage service for AWS (Amazon Web Services). EBS Multi-Attach allows an EBS volume to be attached to multiple instances in AWS. Only clustered file systems, such as GFS2, are supported.

For Enterprise ColumnStore deployments in AWS:

* EBS Multi-Attach is a recommended option for the Storage Manager directory.
* Amazon S3 storage is the recommended option for data.
* Consult the vendor documentation for details on how to configure EBS Multi-Attach.

## Configure Elastic File System (EFS)

EFS is a scalable, elastic, cloud-native NFS file system for AWS (Amazon Web Services)

For deployments in AWS:

* EFS is a recommended option for the Storage Manager directory.
* Amazon S3 storage is the recommended option for data.
* Consult the vendor documentation for details on how to configure EFS.

## Configure Filestore

Filestore is high-performance, fully managed storage for GCP (Google Cloud Platform).

For Enterprise ColumnStore deployments in GCP:

* Filestore is the recommended option for the Storage Manager directory.
* Google Object Storage (S3-compatible) is the recommended option for data.
* Consult the vendor documentation for details on how to configure Filestore.

## Configure GlusterFS

GlusterFS is a distributed file system. GlusterFS is a shared local storage option, but it is not one of the recommended options.

For more information, see "[Recommended Storage Options](../../../../architecture/columnstore-storage-architecture.md#recommended-storage-options)".

### Install GlusterFS

**On each Enterprise ColumnStore node**, install GlusterFS.

Install on CentOS / RHEL 8 (YUM):

```bash
$ sudo yum install --enablerepo=PowerTools glusterfs-server
```

Install on CentOS / RHEL 7 (YUM):

```bash
$ sudo yum install centos-release-gluster
$ sudo yum install glusterfs-server
```

Install on Debian (APT):

```bash
$ wget -O - https://download.gluster.org/pub/gluster/glusterfs/LATEST/rsa.pub | apt-key add -

$ DEBID=$(grep 'VERSION_ID=' /etc/os-release | cut -d '=' -f 2 | tr -d '"')
$ DEBVER=$(grep 'VERSION=' /etc/os-release | grep -Eo '[a-z]+')
$ DEBARCH=$(dpkg --print-architecture)
$ echo deb https://download.gluster.org/pub/gluster/glusterfs/LATEST/Debian/${DEBID}/${DEBARCH}/apt ${DEBVER} main > /etc/apt/sources.list.d/gluster.list
```

```bash
$ sudo apt update
```

```bash
$ sudo apt install glusterfs-server
```

Install on Ubuntu (APT):

```bash
$ sudo apt update
```

```bash
$ sudo apt install glusterfs-server
```

### Start the GlusterFS Daemon

Start the GlusterFS daemon:

```bash
$ sudo systemctl start glusterd
```

```bash
$ sudo systemctl enable glusterd
```

### Probe the GlusterFS Peers

Before you can create a volume with GlusterFS, you must probe each node from a peer node.

1. On the primary node, probe all of the other cluster nodes:

```bash
$ sudo gluster peer probe mcs2
```

```bash
$ sudo gluster peer probe mcs3
```

2. On one of the replica nodes, probe the primary node to confirm that it is connected:

```bash
$ sudo gluster peer probe mcs1
```

```
peer probe: Host mcs1 port 24007 already in peer list
```

3. On the primary node, check the peer status:

```bash
$ sudo gluster peer status
```

```sql
Number of Peers: 2

Hostname: mcs2
Uuid: 3c8a5c79-22de-45df-9034-8ae624b7b23e
State: Peer in Cluster (Connected)

Hostname: mcs3
Uuid: 862af7b2-bb5e-4b1c-8311-630fa32ed451
State: Peer in Cluster (Connected)
```

### Configure and Mount GlusterFS Volumes

Create the GlusterFS volumes for MariaDB Enterprise ColumnStore. Each volume must have the same number of replicas as the number of Enterprise ColumnStore nodes.

1. On each Enterprise ColumnStore node, create the directory for each brick in the /brick directory:

```bash
$ sudo mkdir -p /brick/storagemanager
```

2. On the primary node, create the GlusterFS volumes:

```bash
$ sudo gluster volume create storagemanager \
      replica 3 \
      mcs1:/brick/storagemanager \
      mcs2:/brick/storagemanager \
      mcs3:/brick/storagemanager \
      force
```

3. On the primary node, start the volume:

```bash
$ sudo gluster volume start storagemanager
```

4. On each Enterprise ColumnStore node, create mount points for the volumes:

```bash
$ sudo mkdir -p /var/lib/columnstore/storagemanager
```

5. On each Enterprise ColumnStore node, add the mount points to /etc/fstab:

```
127.0.0.1:storagemanager /var/lib/columnstore/storagemanager glusterfs defaults,_netdev 0 0
```

6. On each Enterprise ColumnStore node, mount the volumes:

```bash
$ sudo mount -a
```

## Configure Network File System (NFS)

NFS is a distributed file system. NFS is available in most Linux distributions. If NFS is used for an Enterprise ColumnStore deployment, the storage must be mounted with the sync option to ensure that each node flushes its changes immediately.

For on-premises deployments:

* NFS is the recommended option for the Storage Manager directory.
* Any S3-compatible storage is the recommended option for data.

Consult the documentation for your NFS implementation for details on how to configure NFS.

## Next Step

Navigation in the procedure "Deploy ColumnStore Object Storage Topology":

This page was **step 2 of 9**.

[Next: Step 3: Install MariaDB Enterprise Server.](step-3-install-mariadb-enterprise-server.md)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
