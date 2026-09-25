---
description: >-
  Work with a GridGain 9 cluster over its REST API, including the OpenAPI
  specification, connector configuration, and authentication.
---

# REST API

GridGain 9 clusters provide an [OpenAPI](https://www.openapis.org/) specification that lets you monitor and manage the cluster using standard REST methods. You can run SQL, create snapshots, deploy code, and perform other management operations over HTTP.

- [Overview](overview.md) — the OpenAPI specification, REST connector configuration, using HTTP tools, and running SQL over REST.
- [REST Authentication](rest-authentication.md) — Basic and JWT Bearer authentication for REST requests.

{% columns %}
{% column %}
{% content-ref url="overview.md" %}
[Overview](overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Use the GridGain 9 REST API to monitor and manage a cluster over HTTP, run SQL statements and scripts, page through results, and generate a Java client.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="rest-authentication.md" %}
[REST Authentication](rest-authentication.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Authenticate GridGain 9 REST API requests using Basic authentication or token-based JWT Bearer authentication, and revoke issued tokens.
{% endcolumn %}
{% endcolumns %}
