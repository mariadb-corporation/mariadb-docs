---
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# ColumnStore Minimum Hardware Specification

The following table outlines the minimum recommended production server specifications which can be followed for both on premise and cloud deployments:

## Per Server

| Item            | Development Environment  | Production Environment     |
| --------------- | ------------------------ | -------------------------- |
| Physical Server | 8 Core CPU, 32 GB Memory | 64 Core CPU, 128 GB Memory |
| Storage         | Local disk               | StorageManager (S3)        |

## Network

|                      |                                                                                                                      |
| -------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Network Interconnect | In a multi server deployment data will be passed around via TCP/IP networking. At least a 1G network is recommended. |

## Details

These are minimum recommendations and in general the system will perform better with more hardware:

* More CPU cores and servers will improve query processing response time.
* More memory will allow the system to cache more data blocks in memory. We have users running system with anywhere from 64G RAM to 512 G RAM for UM and 32 to 64 G RAM for PM.
* Faster network will allow data to flow faster between UM and PM nodes.
* SSD's may be used, however the system is optimized towards block streaming which may perform well enough with HDD's for lower cost.
* Where it is an option, it is recommended to use bare metal servers for additional performance since ColumnStore will fully consume CPU cores and memory.
* In general it makes more sense to use a higher core count / higher memory server for single server or 2 server combined deployments.
* In a deployment with multiple UM nodes the system will round robin requests from the mysqld handling the query to any ExeMgr in the cluster for load balancing. A higher bandwidth network such as 10g or 40g will be of benefit for large result set queries.

### AWS instance sizes

For AWS our own internal testing generally uses m4.4xlarge instance types as a cost effective middle ground. The R4.8xlarge has also been tested and performs about twice as fast for about twice the price.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
