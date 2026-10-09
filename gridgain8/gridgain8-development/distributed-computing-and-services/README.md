---
description: >-
  Run computations and services across the cluster — the compute APIs, data colocation, services, and code deployment.
---

# Distributed Computing and Services

{% columns %}
{% column %}
{% content-ref url="../distributed-computing/" %}
[Distributed Computing](../distributed-computing/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain distributes computations across cluster nodes in a balanced and fault-tolerant manner, with support for the MapReduce pattern, cluster groups, load balancing, and job scheduling.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../colocating-computations.md" %}
[Colocating Computations with Data](../colocating-computations.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to colocate computations with data in GridGain using affinityCall and affinityRun, by key or partition, plus entry processors.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../services/services.md" %}
[Services](../services/services.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to implement, deploy, access, and re-deploy GridGain services, including deployment strategies, interceptors, and the IgniteServices framework.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../code-deployment/" %}
[Code Deployment](../code-deployment/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Overview of code deployment in GridGain, covering how user code and classes are made available across cluster nodes.
{% endcolumn %}
{% endcolumns %}
