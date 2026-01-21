# Metrics Retention Configuration

By default, MariaDB Enterprise Manager retains detailed metrics for **30 days**. You can configure this data retention period to balance your need for historical data with storage costs.

This guide explains how to change the retention period and how the underlying storage system works.

## How to Change the Retention Period

Changing the retention time is done by editing the environment file for Enterprise Manager and then restarting the services.

{% stepper %}
{% step %}
#### Locate and edit the .env file

Navigate to your Enterprise Manager installation directory and open the `.env` file in a text editor.

{% code title="# .env location" %}
```bash
cd enterprise-manager/
vim .env
```
{% endcode %}
{% endstep %}

{% step %}
#### Modify the retention time variable

Find the line containing `PROMETHEUS_RETENTION_TIME` and change its value. The change will only take effect after the Prometheus service is restarted.

Examples:

{% code title="# Set retention to 90 days" %}
```bash
PROMETHEUS_RETENTION_TIME=90d
```
{% endcode %}

{% code title="# Set retention to 52 weeks (one year)" %}
```bash
PROMETHEUS_RETENTION_TIME=52w
```
{% endcode %}

{% hint style="info" %}
Changes to `PROMETHEUS_RETENTION_TIME` take effect only after the Prometheus service is restarted.
{% endhint %}
{% endstep %}

{% step %}
#### Restart services to apply the change

You must restart the services for the new retention period to be applied.

{% code title="# Restart services" %}
```bash
docker compose up -d
```
{% endcode %}
{% endstep %}
{% endstepper %}

## Data Retention Policy

Prometheus, the time-series database used by Enterprise Manager, does not delete expired data instantly.

* Block-Based Storage: Prometheus stores metrics data in **blocks**, which are typically two-hour chunks of time. In the background, these small blocks are compacted into larger ones.
* Delayed Cleanup: Data is not deleted on a sample-by-sample basis. Instead, Prometheus removes an entire block once all the data within it has passed the retention period. This cleanup process runs in the background and may not be immediate.

{% hint style="info" %}
**Delayed metrics removal for deleted databases**

After you delete a database from MariaDB Enterprise Manager, you may continue to see its historical metrics in Grafana dashboards for a period of time.

This is expected behavior. Enterprise Manager does not immediately delete a database's metric history from Prometheus. Instead, the data is removed automatically by Prometheus's own cleanup process once it passes the configured retention period.

These old metrics will no longer receive new data and will eventually disappear from the dashboards on their own.
{% endhint %}

## Valid Retention Time Units

When setting `PROMETHEUS_RETENTION_TIME`, you can use the following units:

* `y` - years
* `w` - weeks
* `d` - days
* `h` - hours
* `m` - minutes
* `s` - seconds

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
