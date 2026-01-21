# Export metrics

MariaDB Enterprise Manager provides two primary methods for exporting metrics, allowing you to integrate with external observability platforms for aggregation or long-term retention.

{% stepper %}
{% step %}
#### Scraping the built-in Prometheus endpoint (Server-to-Server)

The Prometheus server integrated within MariaDB Enterprise Manager exposes its metrics via a standard federation endpoint. You can configure your own external Prometheus server (or any Prometheus-compatible system) to "scrape" these metrics.

**Identify the Federation Endpoint**

The endpoint is located on your MariaDB Enterprise Manager server at the `/prometheus/federate` path. The full URL will be:

`https://<Enterprise_Manager_IP>:8090/prometheus/federate`

**Configure Your External Prometheus**

In your external Prometheus server's configuration file (`prometheus.yml`), add a new scrape job to target the Enterprise Manager endpoint.

{% code title="# prometheus.yml" %}
```yaml
scrape_configs:
  - job_name: 'mem-federation'
    scrape_interval: 60s
    honor_labels: true
    metrics_path: '/prometheus/federate'
    params:
      'match[]':
        - '{job=~".+"}' # This parameter tells the endpoint to return all series.
    static_configs:
      - targets: ['<Enterprise_Manager_IP>:8090']
    scheme: https
    basic_auth:
      username: admin # default username for Enterprise Manager
      password: mariadb # default password for admin user
    # You may need to add TLS and authentication configurations
    # depending on your network setup and security requirements.
    # tls_config:
    #   insecure_skip_verify: true
```
{% endcode %}

After adding this configuration and restarting your external Prometheus, it will begin scraping and storing all metrics from your MariaDB Enterprise Manager instance.
{% endstep %}

{% step %}
#### Pushing metrics with the OpenTelemetry agent (Agent-to-External)

The `mema-agent` can be configured to push metrics directly to a third-party monitoring system that supports the OpenTelemetry Protocol (OTLP). This method sends data straight from the agent to your external endpoint, bypassing the built-in Prometheus server.

To configure this, run the `mema-agent setup` command on your MariaDB Server or MaxScale host with the appropriate flags.

**Command examples**

* For a MariaDB Server host:

{% code title="MariaDB Server host" %}
```bash
sudo mema-agent setup --cluster-name=MyCluster \
  --endpoint=https://<external_ip> --otlp-port=<external_port> \
  --mariadb --host-name=<hostname> \
  --mariadb-user=<user> --mariadb-password=<password> \
  --otlp-insecure --otlp-interval=60s
```
{% endcode %}

* For a MaxScale host:

{% code title="MaxScale host" %}
```bash
sudo mema-agent setup --cluster-name=MyCluster \
  --endpoint=https://<external_ip> --otlp-port=<external_port> \
  --maxscale --host-name=<hostname> \
  --maxscale-user=admin --maxscale-password=mariadb \
  --otlp-insecure --otlp-interval=60s
```
{% endcode %}

**Flag descriptions**

| Flag                  | Description                                                                      |
| --------------------- | -------------------------------------------------------------------------------- |
| `--endpoint`          | The address of your external OTLP-compatible monitoring system.                  |
| `--otlp-port`         | The port on the external system that accepts OTLP data.                          |
| `--cluster-name`      | An informational name for the cluster this host belongs to.                      |
| `--host-name`         | An informational name for this specific host.                                    |
| `--mariadb-user`      | The database user for scraping MariaDB Server metrics.                           |
| `--mariadb-password`  | The password for the MariaDB user.                                               |
| `--maxscale-user`     | The MaxScale API user for scraping MaxScale metrics.                             |
| `--maxscale-password` | The password for the MaxScale user.                                              |
| `--otlp-insecure`     | Disables TLS certificate validation (use for testing or with self-signed certs). |
| `--otlp-interval`     | The interval at which the agent should push metrics (e.g., `60s`).               |

{% hint style="success" %}
For a full list of all available flags and their descriptions, run `mema-agent help setup` on the host where the agent is installed.
{% endhint %}
{% endstep %}
{% endstepper %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
