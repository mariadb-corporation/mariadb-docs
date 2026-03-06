---
description: >-
  Guide to resolving common installation, configuration, agent connectivity, and
  metrics collection issues.
---

# Troubleshooting Enterprise Manager

Troubleshooting installation/deployment issues for Enterprise Manager and Agent

<details>

<summary>Is the MariaDB Enterprise repository configured correctly?</summary>

The agent is distributed as a native OS package that can be installed from the MariaDB Enterprise repositories. The repositories can be installed by following the [repository installation instructions](https://mariadb.com/docs/server/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage).

Make sure to use the `mariadb_es_repo_setup` script with your Customer Download Token.

</details>

<details>

<summary>Was the agent installed successfully?</summary>

The agent installation can be done with the native package manager for your OS.

```bash
# For Red Hat/CentOS/Rocky
sudo dnf install -y mema-agent

# For Debian/Ubuntu
sudo apt install -y mema-agent
```

</details>

<details>

<summary>Did the agent setup complete successfully without errors?</summary>

The `mema-agent setup` command should produce no errors if it is successful. You can always run the setup again by generating the installation command from the GUI and then executing it again on the target server.

**Did the setup fail on a MariaDB node?**

Make sure that MariaDB is listening on the loopback adapter address. If MariaDB cannot be accessed on port `3306` on `localhost`, the setup command should define the port with `--mariadb-port` and the host with `--mariadb-host`. To use a UNIX domain socket, use `--mariadb-socket` instead.

**Did the setup fail on a MaxScale node?**

Make sure that the `--maxscale-host` uses the correct protocol. If MaxScale REST-API is configured to use HTTPS use `--maxscale-host=https://127.0.0.1:8989`. If the TLS certificates used in the MaxScale REST-API are self-signed, you can disable TLS certificate verification by adding the `--maxscale-insecure` option to the setup command.

</details>

<details>

<summary>Did the agent processes start up successfully?</summary>

The agent processes run as systemd services. Use normal systemd commands to inspect the state of the agent.

**Show the agent status**

{% code title="Show status" %}
```bash
sudo systemctl status mema-agent.slice
```
{% endcode %}

If the agent didn't start, errors will be shown in the status output. Once errors are fixed, start the agent again.

{% code title="Start agent" %}
```bash
sudo systemctl start mema-agent.target
```
{% endcode %}

For a more detailed analysis of errors, inspect the agent logs.

**Show the agent logs**

The agent uses the systemd journal for logging:

{% code title="Agent logs" %}
```bash
sudo journalctl -u mema-agent.slice --no-pager
```
{% endcode %}

</details>

<details>

<summary>Can the agent collect MariaDB metrics?</summary>

The credentials that the agent uses to connect to MariaDB require certain grants in order to collect all metrics. Check the [Quickstart Guide](quickstart-guide.md) for the set of grants and verify that the user provided with `--mariadb-user` has the necessary grants.

If the MariaDB metrics agent is working correctly, the logs should not have any errors. Check the logs with:

{% code title="MariaDB exporter logs" %}
```bash
sudo journalctl -u mema-agent-mariadb-exporter.service
```
{% endcode %}

To verify the MariaDB metrics agent is running, inspect the raw metrics output:

{% code title="Raw metrics check" %}
```bash
curl -s http://127.0.0.1:18902/metrics | wc -l
```
{% endcode %}

The output should contain about 3000 lines if everything is working.

</details>

<details>

<summary>Is MaxScale able to send metrics?</summary>

Make sure that the version of MaxScale you have installed is 25.10 or greater. Older versions do not support sending metrics.

Any errors in metrics exporting are logged on the info level in MaxScale. To enable info logging, run:

{% code title="Enable MaxScale info logging" %}
```bash
maxctrl alter maxscale log_info=true
```
{% endcode %}

Info level logging is verbose and may cause large log volumes. Once issues are resolved, disable info logging:

{% code title="Disable MaxScale info logging" %}
```bash
maxctrl alter maxscale log_info=false
```
{% endcode %}

</details>

<details>

<summary>Can the agent connect to the Enterprise Manager?</summary>

To check connectivity between the agent host and the Enterprise Manager, use `curl`. If your Enterprise Manager is at 192.168.122.16, the following commands show the expected responses:

{% code title="Expected curl checks" %}
```bash
$ curl http://192.168.122.16:4318
Client sent an HTTP request to an HTTPS server.

$ curl -k https://192.168.122.16:4318
404 page not found
```
{% endcode %}

* The first command should report an HTTP-to-HTTPS error.
* The second command should return `404 page not found`.

If there are errors, check that port 4318 is open on the Enterprise Manager server and that network connectivity between the agent host and the Enterprise Manager is working.

If the `curl` commands produce the expected output and the agent status does not report errors after five minutes of startup, the agent is successfully sending metrics to the Enterprise Manager.

</details>

<details>

<summary>Are the metrics available in the Enterprise Manager?</summary>

To verify metrics are stored in the time series database, query a system OS metric. Example (assumes Enterprise Manager at 192.168.122.16 and default `admin:mariadb` credentials):

{% code title="Query metric" overflow="wrap" %}
```bash
curl -u admin:mariadb -k "https://192.168.122.16:8090/prometheus/api/v1/query?query=node_os_info"
```
{% endcode %}

The result should be a JSON object with one object per node in the `data.result` array.

</details>

<details>

<summary>Is the time synchronized between Enterprise Manager and agents?</summary>

When agents push metrics they include the agent’s timestamp and Enterprise Manager assumes those timestamps are accurate. If Enterprise Manager and monitored instances are not time-synchronized, you can observe:

* Misaligned graphs
* Missed alerts
* Dropped/future/old samples that create “no data” gaps
* Poor alignment with logs/traces/events

Ensure clocks are synchronized (for example using NTP/chrony) to avoid these issues.

</details>

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
