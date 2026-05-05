---
description: >-
  The CMAPI node PUT endpoint adds a new MariaDB Enterprise ColumnStore node
  and configures a dbroot for it, called via HTTPS PUT with x-api-key
  authentication.
---

# node PUT

Adds a ColumnStore node.

See [CMAPI](./) for detail on REST API endpoint, required headers, and other available actions.

## Description

Upon successful `node` PUT call CMAPI configures MariaDB Enterprise ColumnStore to add the new node and a dbroot for that node.

Call made via HTTPS `PUT`, with authentication via shared secret using the `x-api-key` header.

JSON data required for this call:

| Key       | Value                                                                  |
| --------- | ---------------------------------------------------------------------- |
| `timeout` | Maximum time in seconds to wait for completion of `add-node` operation |
| `node`    | IP address of the node to add                                          |

## Examples

### Executing cURL Manually

CMAPI calls can be made from the command-line using cURL.

Replace the CMAPI\_API\_KEY and sample data in the following example:

```bash
curl -k -s -X PUT https://mcs1:8640/cmapi/0.4.0/cluster/node \
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
