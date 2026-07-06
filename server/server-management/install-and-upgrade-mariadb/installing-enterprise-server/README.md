---
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
  tags:
    visible: true
---

# Installing Enterprise Server

{% columns %}
{% column %}
{% content-ref url="token.md" %}
[token.md](token.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Instructions on how to retrieve and use a Customer Download Token to access MariaDB Enterprise Server packages and binaries.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../../architecture/topologies/single-node-topologies/enterprise-server.md#installation" %}
[enterprise-server.md#installation](../../../architecture/topologies/single-node-topologies/enterprise-server.md#installation)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A guide to installing MariaDB Enterprise Server on various operating systems using package managers (YUM, APT, ZYpp) or binary tarballs.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../../architecture/topologies/primary-replica/" %}
[primary-replica](../../../architecture/topologies/primary-replica/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This page explains how to set up a standard Primary/Replica replication topology for MariaDB Enterprise Server.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../../architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-local-storage/" %}
[enterprise-server-with-columnstore-local-storage](../../../architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-local-storage/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Deployment instructions for a single-node MariaDB Enterprise Server instance with the ColumnStore engine using local storage.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../../architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage/" %}
[enterprise-server-with-columnstore-object-storage](../../../architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Deployment instructions for a single-node MariaDB Enterprise Server instance with the ColumnStore engine using S3-compatible object storage.
{% endcolumn %}
{% endcolumns %}
