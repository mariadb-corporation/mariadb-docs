---
description: >-
  Configuration reference for the official MariaDB Enterprise container images —
  environment variables, command-line flags, and sidecar patterns for
  production deployments.
---

# MariaDB Enterprise Container Image Configuration Reference

Orchestrating a MariaDB Enterprise deployment within containerized environments involves more than just launching a database instance; it requires the precise alignment of server logic, intelligent traffic routing, and robust observability tools. This reference serves as the definitive technical roadmap for configuring the official images provided by the MariaDB Enterprise Docker Registry. It details the standardized environment variables, specialized sidecar patterns, and command-line flags required to transform raw images into a production-ready, cloud-native ecosystem.

## MariaDB Enterprise Server (Standard and Tiered)

The MariaDB Enterprise Docker Registry provides Docker images for MariaDB Enterprise Server 10.6 and later. These images include standard storage engines such as InnoDB, Aria, MyISAM, and others by default.

### Environment Variables

MariaDB Enterprise Server containers are primarily configured using [environment variables](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md#environment-variables) during initialization:

* `MARIADB_ROOT_PASSWORD`: Specifies the password for the MariaDB `root` user. It can be set to a specific string, `RANDOM` to generate a password, or `EMPTY` for no password.
* `MARIADB_DATABASE`: If provided, the container creates this database on startup if it does not already exist.
* `MARIADB_USER` and `MARIADB_PASSWORD`: These must be used together to create a non-root user account with the specified credentials.
* `MARIADB_ROOT_HOST`: Defines the host from which the `root` user is allowed to connect, defaulting to `%` (any host).
* `MARIADB_UNIX_SOCKET_AUTHENTICATION`: When set to `1`, this enables Unix socket-based authentication for the root user, allowing passwordless access when connecting locally.
* `MARIADB_INITDB_SKIP_TZINFO`: Setting this to any non-empty value prevents the automatic loading of timezone data into the system tables.
* `SKIP_INIT_WSREP_OFF`: When set, the temporary server used during initialization is allowed to start with Galera Cluster replication (`wsrep`) enabled.

## MariaDB Prometheus Exporter

{% hint style="warning" %}
**Configuration Methodology** \
For optimal security and management, exporter configuration is executed via command-line flags or configuration files. Environment variables are utilized strictly for sensitive data, ensuring credentials remain protected from exposure in configuration logs.
{% endhint %}

The MariaDB Prometheus Exporter (based on [`mysqld_exporter`](https://github.com/prometheus/mysqld_exporter)) is a tool for scraping metrics from MariaDB instances.

### Database Permissions

A dedicated database user is required to allow the exporter to scrape metrics:

```sql
CREATE USER 'exporter'@'localhost' IDENTIFIED BY 'XXXXXXXX' WITH MAX_USER_CONNECTIONS 3;
GRANT PROCESS, REPLICATION CLIENT, SELECT ON *.* TO 'exporter'@'localhost';
```

> Note: Limiting connections is recommended to prevent monitoring traffic from impacting server performance, though some versions like MariaDB 10.1 do not support resource limits.

### Configuration and Usage

* Configuration File (`.my.cnf`): Credentials should be placed in a `[client]` section. The exporter reads this file from the current directory or a path specified by `--config.my-cnf`.
* Environment Variables: The `MYSQLD_EXPORTER_PASSWORD` variable can be used to provide the connection password securely.
* Collector Flags: Specific metric groups can be toggled using flags such as `--collect.binlog_size`, `--collect.engine_innodb_status`, and `--collect.info_schema.userstats`.
* Multi-Target Support: The exporter can act as a proxy for multiple MariaDB instances via the `/probe` endpoint using the `target` parameter. Authentication for different targets is managed using `auth_module` sections in the configuration file.

## MaxScale Prometheus Exporter

{% hint style="warning" %}
**Configuration Methodology** \
For optimal security and management, exporter configuration is executed via command-line flags or configuration files. Environment variables are utilized strictly for sensitive data, ensuring credentials remain protected from exposure in configuration logs.
{% endhint %}

The MaxScale Exporter collects metrics from the MaxScale REST API.

### Prerequisites

* A MaxScale REST API user with read privileges must be created using `maxctrl`: `maxctrl create user monitor-user monitor-password`.

### Configuration and Security

Configuration options follow a hierarchy where environment variables override command-line flags, which override configuration files.

* Environment Variables: Use `MAXSCALE_USERNAME` and `MAXSCALE_PASSWORD` to provide REST API credentials.
* Command Line Flags: Standard flags include `--maxscale-host`, `--maxscale-port` (default `8989`), and listener settings.
* TLS/SSL: Encrypted connections to MaxScale require the flags `--tls-ca-cert-file`, `--tls-private-key-file`, and `--tls-key-cert-file`. Use `--tls-insecure-skip-verify` for self-signed certificates.
* Encryption: The exporter can generate and use encrypted passwords via the `--secrets` and `--encrypt` flags.

## MariaDB Enterprise nslcd Sidecar

The [nslcd](https://app.gitbook.com/s/kuTXWg0NDbRx6XUeYpGD/mariadb-enterprise-operator/plugins/pam#nslcd.conf) sidecar is utilized for integrating MariaDB with LDAP or Active Directory authentication through the Pluggable Authentication Module (PAM) framework.

### Configuration Requirements

* `nslcd.conf`: This file configures the `nslcd` daemon, specifying the LDAP server URI, search base, and service account credentials (`binddn`/`bindpw`).
* Identity Management: The `nslcd` daemon must be configured to run as the `mysql` user and group (`uid mysql`, `gid mysql`).
* `nsswitch.conf`: This file determines the sources for name-service information and must include `ldap` for `passwd`, `group`, and `shadow` entries.
* Shared Socket: The daemon communicates with the MariaDB container via a shared Unix socket, typically mounted at `/var/run/nslcd`.

### Integration with MariaDB

To enable this functionality, the MariaDB Custom Resource must be configured to load the `auth_pam` plugin using the `plugin_load_add` option in the `myCnf` section.

## MaxScale and MaxScale Enterprise

The core MaxScale images do not rely on Docker-specific environment variables for internal configuration. Instead, MaxScale is configured using standard `.cnf` files or through the REST API. For monitoring deployments, it is paired with the MaxScale Prometheus Exporter as detailed above.
