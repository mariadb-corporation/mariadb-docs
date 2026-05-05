---
description: >-
  The CMAPI start endpoint starts MariaDB ColumnStore on every cluster node
  via HTTPS PUT with x-api-key authentication; also available as the mcsStart
  alias from CS 5.5.2.
---

# start

Starts ColumnStore on all nodes.

See [CMAPI](./) for detail on REST API endpoint, required headers, and other available actions.

## Description

Upon successful `start` call CMAPI connects to each MariaDB Enterprise ColumnStore node and performs start-up.

Call made via HTTPS `PUT`, with authentication via shared secret using the `x-api-key` header.

JSON data required for this call:

| Key       | Value                                                                  |
| --------- | ---------------------------------------------------------------------- |
| `timeout` | Maximum time in seconds to wait for completion of `add-node` operation |

Bash alias `mcsStart` is available starting with Enterprise ColumnStore 5.5.2.

## Examples

### Executing cURL Manually

CMAPI calls can be made from the command-line using cURL.

Replace the CMAPI\_API\_KEY and sample data in the following example:

```bash
curl -k -s -X PUT https://mcs1:8640/cmapi/0.4.0/cluster/start \
   --header 'Content-Type:application/json' \
   --header 'x-api-key:<CMAPI_API_KEY>' \
   --data '{"timeout":20}' \
   | jq .
```

The command returns a JSON payload. Piping it to `jq` makes the output more human-readable.

### Executing the Bash Alias

Starting with Enterprise ColumnStore 5.5.2, if your `bash` shell is configured to source the `columnstoreAlias` shell script, this command can be executed using the `mcsStart` alias. The alias executes `curl` and `jq`, so both programs must be installed on the system.

The alias automatically retrieves the IP address for the primary node using the [mcsGetConfig](http://localhost:8000/docs/columnstore/ref/col/cli/mcsGetConfig/) command. The alias automatically retrieves the API key by reading `/etc/columnstore/cmapi_server.conf`.

```bash
mcsStart
```

These aliases use `jq` produces human-readable output from the returned JSON response.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
