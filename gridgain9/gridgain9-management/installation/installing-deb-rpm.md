---
description: >-
  Install GridGain 9 from DEB or RPM packages and run it as a service or a
  stand-alone process.
---

# Installing Using DEB and RPM Package

GridGain can be installed by using the standard package managers for the platform.

## Prerequisites

### Recommended Operating System

{% include "../../.gitbook/includes/prereqs-os.md" %}

### Recommended Java Version

{% include "../../.gitbook/includes/prereqs-java.md" %}

## Version Lifecycle

The information about versioning and lifecycle of GridGain 9 is available on the [Versioning page](https://www.gridgain.com/versioning-and-support-lifecycle).

## Installing Deb or RPM Package

Install the GridGain 9 packages:

{% tabs %}
{% tab title="deb" %}
```bash
sudo apt-get install ./gridgain9-db-9.1_all.deb --no-install-recommends
sudo apt-get install ./gridgain9-cli-9.1_all.deb --no-install-recommends
```
{% endtab %}

{% tab title="RPM" %}
```bash
sudo rpm -i gridgain9-db-9.1_all.noarch.rpm
sudo rpm -i gridgain9-cli-9.1_all.noarch.rpm
```
{% endtab %}
{% endtabs %}

The packages will be installed in the following way:

| Folder | Description |
| --- | --- |
| /usr/lib/gridgain9db | The root installation of GridGain. |
| /etc/gridgain9db | The location of configuration files. |
| /var/log/gridgain9db | The location of node logs. |
| /var/lib/gridgain9db | The node work directory, where GridGain stores data. |
| /usr/bin/gridgain9 | The CLI tool executable. |
| /usr/lib/gridgain9 | The location of the CLI tool libraries. |

## Running GridGain as a Service

{% hint style="info" %}
When running on Windows 10 WSL or Docker, you should start GridGain as a stand-alone process (not as a service). We recommend to [install GridGain 9 using ZIP archive](installing-using-zip.md) in these environments.
{% endhint %}

To start a GridGain node with a custom configuration, run the following command:

```bash
sudo systemctl start gridgain9db
```

To launch the node at system startup, run the following command:

```bash
sudo systemctl enable gridgain9db
```

## Running GridGain as a Stand-Alone Process

Generally, you would want to run GridGain as a service. However, GridGain also provides a startup script that can be used to start it as a stand-alone application. To run it, use the following command:

```bash
sudo bash /usr/lib/gridgain9db/start.sh 1>/tmp/gridgain9-start.log 2>&1 &
```

## Next Steps

With the GridGain installed, you can proceed with the [Getting Started](../../gridgain9-get-started/quick-start.md) or [use the available APIs](../../gridgain9-usage/table-api.md) immediately.
