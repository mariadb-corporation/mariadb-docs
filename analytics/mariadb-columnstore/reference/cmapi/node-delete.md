---
description: >-
  The CMAPI node DELETE endpoint removes a MariaDB Enterprise ColumnStore node
  from the cluster via HTTPS DELETE with x-api-key authentication.
---

# node DELETE

Removes a ColumnStore node.

See [CMAPI](./) for detail on REST API endpoint, required headers, and other available actions.

## Description

Upon successful `node` DELETE call CMAPI configures MariaDB Enterprise ColumnStore to remove the specified node.

Call made via HTTPS `DELETE`, with authentication via shared secret using the `x-api-key` header.

JSON data required for this call:

| Key       | Value                                                                  |
| --------- | ---------------------------------------------------------------------- |
| `timeout` | Maximum time in seconds to wait for completion of `add-node` operation |
| `node`    | IP address of the node to remove                                       |

## Examples

### Executing cURL Manually

CMAPI calls can be made from the command-line using cURL.

Replace the CMAPI\_API\_KEY and sample data in the following example:

```bash
curl -k -s -X DELETE https://mcs1:8640/cmapi/0.4.0/cluster/node \
   --header 'Content-Type:application/json' \
   --header 'x-api-key:<CMAPI_API_KEY>' \
   --data '{"timeout": 20, "node": "192.0.2.2"}' \
   | jq .
```

In this example, `jq` produces human-readable output from the returned JSON response:

```json
{
  "timestamp": "2020-10-28 00:42:42.796050",
  "node_id": "192.0.2.2"
}
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
