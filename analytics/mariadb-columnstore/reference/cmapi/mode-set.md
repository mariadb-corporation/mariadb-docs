---
description: >-
  The CMAPI mode-set endpoint configures all MariaDB Enterprise ColumnStore
  nodes to read-only or read-write operation via HTTPS PUT with x-api-key
  authentication.
---

# mode-set

Sets all ColumnStore nodes to read-only or read-write.

See [CMAPI](./) for detail on REST API endpoint, required headers, and other available actions.

## Description

Upon successful `mode-set` call CMAPI re-configures MariaDB Enterprise ColumnStore to the designated mode, either read-only or read/write operation.

Call made via HTTPS `PUT`, with authentication via shared secret using the `x-api-key` header.

JSON data required for this call:

| Key       | Value                                                                  |
| --------- | ---------------------------------------------------------------------- |
| `timeout` | Maximum time in seconds to wait for completion of `mode-set` operation |
| `mode`    | Accepted values: `readonly` for read-only, `readwrite` for read/write. |

Bash aliases `mcsReadOnly` and `mcsReadWrite` are available starting with Enterprise ColumnStore 5.5.2.

## Examples

### Executing cURL Manually

CMAPI calls can be made from the command-line using cURL.

Replace the CMAPI\_API\_KEY and sample data in the following example:

```bash
curl -k -s -X PUT https://mcs1:8640/cmapi/0.4.0/cluster/mode-set \
   --header 'Content-Type:application/json' \
   --header 'x-api-key:<CMAPI_API_KEY>' \
   --data '{"timeout": 20, "mode": "readwrite"}' \
   | jq .
```

In this example, `jq` produces human-readable output from the returned JSON response.

### Executing the Bash Aliases

Starting with Enterprise ColumnStore 5.5.2, if your `bash` shell is configured to source the `columnstoreAlias` shell script, this command can be executed using the `mcsReadOnly` and `mcsReadWrite` aliases. The alias executes `curl` and `jq`, so both programs must be installed on the system.

The aliases automatically retrieve the IP address for the primary node using the `mcsGetConfig` command. The aliases automatically retrieve the API key by reading `/etc/columnstore/cmapi_server.conf`.

To set the deployment's mode to read-only:

```bash
mcsReadOnly
```

To set the deployment's mode to read-write:

```bash
mcsReadWrite
```

These aliases use `jq` produces human-readable output from the returned JSON response.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
