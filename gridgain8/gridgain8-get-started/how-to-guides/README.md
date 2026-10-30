---
description: >-
  Task-focused guides for GridGain 8: security, monitoring, performance, operations, and integrations.
---

# How-To Guides

Each guide solves one task from start to finish.

## Security and operations

{% columns %}
{% column %}
{% content-ref url="ssl-tls-step-by-step.md" %}
[How to Configure SSL/TLS/HTTPS Security](ssl-tls-step-by-step.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Set up SSL/TLS to secure GridGain node-to-node, thin-client (ODBC/JDBC), and HTTPS REST traffic with a self-signed certificate authority.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="encrypt-traffic-istio.md" %}
[How to Encrypt Cluster Traffic With Istio mTLS on Kubernetes](encrypt-traffic-istio.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Enforce mutual TLS across GridGain 8 cluster, thin-client, and external traffic with an Istio service mesh, without changing the cluster's own configuration.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="encrypt-traffic-linkerd.md" %}
[How to Encrypt Inter-Node Cluster Traffic With Linkerd on Kubernetes](encrypt-traffic-linkerd.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Encrypt GridGain 8 discovery and communication traffic with automatic mTLS from a Linkerd service mesh, with no keystores and no cluster configuration changes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="prometheus-grafana-step-by-step.md" %}
[How to Monitor GridGain 8 With Prometheus and Grafana](prometheus-grafana-step-by-step.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Export GridGain 8 metrics to Prometheus with the OpenCensus exporter, then connect Prometheus to Grafana and import a prebuilt dashboard.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="new-relic.md" %}
[How to Monitor GridGain Clusters With New Relic](new-relic.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Export GridGain 8 metrics and logs to New Relic using the OpenTelemetry Java agent, then visualize them with a prebuilt dashboard.
{% endcolumn %}
{% endcolumns %}

## Performance

{% columns %}
{% column %}
{% content-ref url="choose-partition-count.md" %}
[How to Choose a Partition Count for Your Workload](choose-partition-count.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Pick a partition count for a partitioned cache on GridGain 8. Default is 1024.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="debug-hot-partition.md" %}
[How to Debug a Hot Partition](debug-hot-partition.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Diagnose and fix a hot partition on GridGain 8. Three-step procedure identifies the partition, its owner, and the skew pattern.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="numa-memory-allocation.md" %}
[How to Configure NUMA-Aware Memory Allocation](numa-memory-allocation.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Enable NUMA-aware memory allocation in GridGain 8 so data regions optimize memory access patterns on multiprocessor Linux hardware for higher performance.
{% endcolumn %}
{% endcolumns %}

## Development

{% columns %}
{% column %}
{% content-ref url="uri-deployment-spi.md" %}
[How to Deploy Code With UriDeploymentSpi](uri-deployment-spi.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Deploy and redeploy Java compute tasks, services, and POJOs to a running GridGain 8 cluster without restarting nodes, using UriDeploymentSpi.
{% endcolumn %}
{% endcolumns %}

## Integrations

{% columns %}
{% column %}
{% content-ref url="example-running-on-amazon-msk.md" %}
[How to run the GridGain Kafka Connector on Amazon MSK](example-running-on-amazon-msk.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Run Kafka on Amazon MSK with the GridGain Kafka Connector on EC2 to source and sink data between MSK and a GridGain cluster in AWS.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="export-data-iceberg-aws.md" %}
[How to Export Data to Apache Iceberg on AWS](export-data-iceberg-aws.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Batch-export GridGain 8 data to an Apache Iceberg table in AWS Glue and Amazon S3 with COPY FROM ... INTO, query it in Athena, then import it back.
{% endcolumn %}
{% endcolumns %}

## AI and machine learning

{% columns %}
{% column %}
{% content-ref url="langchain-rag-tutorial.md" %}
[How to Build Retrieval-Augmented Generation With GridGain and LangChain](langchain-rag-tutorial.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Use GridGain 8 distributed vector search as the unified backend for a LangChain RAG application, with a working laptop-recommendation demo.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="langflow-rag-tutorial.md" %}
[How to Build a Low-Code RAG Application With GridGain and Langflow](langflow-rag-tutorial.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Build a visual RAG application on Langflow, using GridGain 8 vector search with HNSW as the vector store and chat memory, no code required.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="feast-feature-store-tutorial.md" %}
[How to Build a Machine Learning Feature Store With GridGain and Feast](feast-feature-store-tutorial.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Use GridGain 8 as a low-latency Feast online store for real-time machine learning feature serving, illustrated with a CGM glucose-prediction demo.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="cache-ml-predictions-bigquery.md" %}
[How to Cache Machine Learning Predictions With GridGain and BigQuery](cache-ml-predictions-bigquery.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Serve BigQuery ML predictions with sub-millisecond latency by caching them in GridGain 8, using a Google Analytics product recommendation demo as the reference.
{% endcolumn %}
{% endcolumns %}
