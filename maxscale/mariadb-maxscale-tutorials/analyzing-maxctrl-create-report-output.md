---
description: >-
  Learn to inspect MaxScale's runtime state using the JSON report from maxctrl.
  Use jq to query servers services and monitors for detailed debugging and
  analysis.
---

# Analyzing MaxCtrl Create Report Output

The output of the `maxctrl create report` command produces a JSON payload that contains the current state of MaxScale. This includes the runtime configuration and the status all objects in MaxScale.

The `maxctrl create report` command was added in MaxScale 2.5.20.

## Creating a MaxCtrl Report

The report can be created with:

```
maxctrl create report maxctrl-report.json
```

After the command completes, the data is in `maxctrl-report.json`.

The file in which the output is stored is the only argument to this command. Recent versions of maxctrl pipe the output to the standard output if no filename is given. This can be useful for environments where copying files may be difficult (e.g. docker).

## Using `jq`

The easiest way to inspect the JSON output is to use the jq program:

It is usually available as a package in most operating systems.

### List servers

```
jq '.servers.data[].id' < maxctrl-report.json
```

### List services

```
jq '.services.data[].id' <  maxctrl-report.json
```

### List monitors

```
jq '.monitors.data[].id' < maxctrl-report.json
```

### List listeners

```
jq '.listeners.data[].id' <  maxctrl-report.json
```

### List filters

```
jq '.filters.data[].id' <  maxctrl-report.json
```

### List keys of objects

```
jq 'keys' < maxctrl-report.json
```

This can be combined with the object field access to list the fields of sub-objects. The following lists the keys in the first server object.

```
jq '.servers.data[0]|keys' < maxctrl-report.json
```

### Get a specific service

Change the `RW-Split-Router` to the name of the service you're looking for.

```
jq '.services.data|map(select(.id == "RW-Split-Router"))' < maxctrl-report.json
```

### Get a specific monitor

Change the `MariaDB-Monitor` to the name of the monitor you're looking for.

```
jq '.monitors.data|map(select(.id == "MariaDB-Monitor"))' < maxctrl-report.json
```

### Get a specific server

Change the `DB-1` to the name of the server you're looking for.

```
jq '.servers.data|map(select(.id == "DB-1"))' < maxctrl-report.json
```

### Find the monitor for a server

Change `DB-1` to the name of the server you're looking for.

```
jq '.servers.data|map(select(.id == "DB-1"))|.[].relationships.monitors.data' < maxctrl-report.json
```

### Memory used by the query classifier cache

```
jq '[.threads.data[].attributes.stats.query_classifier_cache.size]|add' < maxctrl-report.json
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
