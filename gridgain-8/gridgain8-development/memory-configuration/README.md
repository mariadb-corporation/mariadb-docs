---
description: >-
  Configuring GridGain memory usage, including data regions, eviction policies,
  and page replacement policies.
---

# Memory Configuration

{% columns %}
{% column %}
{% content-ref url="data-regions.md" %}
[Configuring Data Regions](data-regions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configuring GridGain data regions to control RAM usage per cache, including the default region, custom regions, system regions, and cache warm-up strategy.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="eviction-policies.md" %}
[Eviction Policies](eviction-policies.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configuring off-heap memory eviction in GridGain, including the Random-LRU and Random-2-LRU page selection algorithms and on-heap cache eviction.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="replacement-policies.md" %}
[Replacement Policies](replacement-policies.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configuring page replacement in GridGain when Native Persistence is on, including the Random-LRU, Segmented-LRU, and CLOCK page replacement algorithms.
{% endcolumn %}
{% endcolumns %}
