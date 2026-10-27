---
description: >-
  Work with a GridGain 9 cluster over its REST API, including the OpenAPI
  specification and authentication.
---

# REST API

GridGain 9 clusters provide an [OpenAPI](https://www.openapis.org/) specification that lets you monitor and manage the cluster using standard REST methods. You can run SQL, create snapshots, deploy code, and perform other management operations over HTTP.

For the OpenAPI specification, connector configuration, using HTTP tools, and running SQL over REST, see [Using the REST API](../../gridgain9-development/rest-api.md).

- [REST Authentication](rest-authentication.md) — Basic and JWT Bearer authentication for REST requests.

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
