# Backup & Restore of Enterprise Manager

Note: This is about backing up the data, configuration and collected metrics of the Enterprise Manager (EM), not the databases.

## Backing up Enterprise Manager Server

{% stepper %}
{% step %}
**Stop the Enterprise Manager**

1. Go to the Enterprise Manager installation directory
2. Run `docker compose stop` to stop the Enterprise Manager
{% endstep %}

{% step %}
**Create a directory for backups**

{% code title="Create the `backups` directory" %}
```bash
mkdir backups
```
{% endcode %}
{% endstep %}

{% step %}
**Take a backup of all the volumes**

{% code title="Back up all volumes" %}
```bash
docker run --rm --volumes-from enterprise-manager-grafana -v $(pwd)/backups/:/backups/ alpine:latest tar -czf /backups/grafana-backup.tar.gz /var/lib/grafana/
docker run --rm --volumes-from enterprise-manager-prometheus -v $(pwd)/backups/:/backups/ alpine:latest tar -czf /backups/prometheus-backup.tar.gz /prometheus/
docker run --rm --volumes-from enterprise-manager-supermax -v $(pwd)/backups/:/backups/ alpine:latest tar -czf /backups/supermax-backup.tar.gz /var/lib/supermax/
```
{% endcode %}

The `backups` directory now contains the data from the Enterprise Manager.
{% endstep %}

{% step %}
#### Start the Enterprise Manager

1. Go to the Enterprise Manager installation directory
2. Run `docker compose up -d` to start the Enterprise Manager
{% endstep %}
{% endstepper %}

## Restoring Enterprise Manager Server

{% stepper %}
{% step %}
#### Stop the Enterprise Manager

1. Go to the Enterprise Manager installation directory
2. Run `docker compose stop` to stop the Enterprise Manager
{% endstep %}

{% step %}
#### Restore the backup of all volumes

The backups are stored in the `~/backups/` directory.

{% code title="Restore backup to all volumes" %}
```bash
# Clear out any existing data first
docker run --rm --volumes-from enterprise-manager-grafana -v $(pwd)/backups/:/backups/ alpine:latest find /var/lib/grafana/ -delete -mindepth 1
docker run --rm --volumes-from enterprise-manager-prometheus -v $(pwd)/backups/:/backups/ alpine:latest find /prometheus/ -delete -mindepth 1
docker run --rm --volumes-from enterprise-manager-supermax -v $(pwd)/backups/:/backups/ alpine:latest find /var/lib/supermax/ -delete -mindepth 1

# Restore the data from the backups
docker run --rm --volumes-from enterprise-manager-grafana -v $(pwd)/backups/:/backups/ alpine:latest tar -C / -xzf /backups/grafana-backup.tar.gz
docker run --rm --volumes-from enterprise-manager-prometheus -v $(pwd)/backups/:/backups/ alpine:latest tar -C / -xzf /backups/prometheus-backup.tar.gz
docker run --rm --volumes-from enterprise-manager-supermax -v $(pwd)/backups/:/backups/ alpine:latest tar -C / -xzf /backups/supermax-backup.tar.gz
```
{% endcode %}
{% endstep %}

{% step %}
#### Start the Enterprise Manager

1. Go to the Enterprise Manager installation directory
2. Run `docker compose up -d` to start the Enterprise Manager
{% endstep %}
{% endstepper %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
