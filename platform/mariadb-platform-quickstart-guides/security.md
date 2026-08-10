---
cover: ../.gitbook/assets/MDB-asset-image-27.jpg
coverY: 0
---

# Security

_This Quickstart Guide details essential MariaDB security measures. It covers using `mariadb-secure-installation` for initial setup, enforcing least privilege for user accounts, and securing network access with firewalls and binding addresses. Key practices include data encryption (SSL/TLS, TDE), hardening configurations (disabling `LOCAL INFILE`, enabling logging), and regular updates and auditing._

### Quickstart Guide: MariaDB Security

Securing your MariaDB installation is crucial to protect your data. This quickstart guide outlines essential steps and best practices to enhance your MariaDB server's security.

#### 1. Initial Installation Security (`mariadb-secure-installation`)

Immediately after installing MariaDB, run the `mariadb-secure-installation` script (or `mysql_secure_installation` on older systems or symlinked versions). This script guides you through critical initial security configurations:

* **Set a Strong Root Password:** This is the most important step to prevent unauthorized administrative access.
* **Remove Anonymous Users:** Anonymous user accounts are created by default for testing and should be removed from production environments.
* **Disallow Remote Root Login:** Prevent the `root` user from connecting to the database from outside the local machine. This mitigates brute-force attacks.
* **Remove Test Database:** The `test` database and its associated privileges are created by default for testing. Remove them to eliminate a potential security risk.
* **Reload Privilege Tables:** Ensure all changes take effect immediately.

**Example Command:**

```bash
sudo mariadb-secure-installation
```

Follow the prompts to configure your security settings.

#### 2. User Account Management and Privileges

* **Principle of Least Privilege:** Grant users only the minimum necessary privileges required for their tasks. Avoid giving `ALL PRIVILEGES` unless absolutely necessary for specific administrative accounts.
* **Create Dedicated Users:** Do not use the `root` account for regular application operations. Create specific users for your applications with limited privileges.
* **Strong Passwords:** Enforce strong, unique passwords for all database user accounts.
* **Limit Host Access:** Restrict user accounts to connect only from specific IP addresses or hostnames where they are expected to connect (e.g., `user@'localhost'` or `user@'192.168.1.100'`).

#### 3. Network Security

* **Firewall Configuration:** Configure your operating system's firewall (e.g., `ufw` on Linux, Windows Firewall) to allow connections to MariaDB only from trusted IP addresses or subnets.
* **Change Default Port (Optional but Recommended):** MariaDB typically listens on port 3306. Changing this default port can add a layer of obscurity, deterring automated scanning attempts.
  * Edit your MariaDB configuration file (e.g., `/etc/mysql/mariadb.conf.d/50-server.cnf` or `my.cnf` on Linux, `my.ini` on Windows).
  * Change the `port` directive to a different value.
  * Restart the MariaDB service.
* **Bind Address:** Configure MariaDB to listen only on specific network interfaces (e.g., `bind-address = 127.0.0.1` for local connections only, or a specific private IP address for network-restricted access).

#### 4. Data Encryption

* **Encryption in Transit (SSL/TLS):** Encrypt communication between clients and the MariaDB server using SSL/TLS. This protects data from eavesdropping as it travels across the network.
* **Encryption at Rest (TDE):** For highly sensitive data, consider using MariaDB's Transparent Data Encryption (TDE) to encrypt data stored on disk.

#### 5. Configuration Hardening

*   **Disable `LOCAL INFILE`:** This feature can be a security risk as it allows clients to read files from the server's filesystem. Disable it in your MariaDB configuration:

    ```
    local-infile=0
    ```
*   **Enable Logging:** Configure MariaDB to log errors and general queries. This helps in auditing activities and troubleshooting security incidents.

    ```
    log_error = /var/log/mysql/error.log
    general_log = 1
    general_log_file = /var/log/mysql/mysql.log
    ```
* **Run as Non-Root User:** MariaDB should never run as the `root` user in production environments. It should run under a dedicated, unprivileged system user (e.g., `mysql` or `mariadb`).

#### 6. Regular Maintenance and Auditing

* **Keep Software Updated:** Regularly update MariaDB Server and your operating system to the latest stable versions to benefit from security fixes.
* **Audit Database Activity:** Implement auditing to track database operations, especially for sensitive data or administrative actions. MariaDB provides an Audit Plugin for this purpose.
* **Regular Security Audits:** Periodically review your MariaDB server's security configuration and user privileges.

#### Resources:

* [MariaDB `mariadb-secure-installation` documentation](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/deployment-tools/mariadb-secure-installation)
* [Top 9 Tips to Achieve MySQL and MariaDB Security - SnapShooter Tutorials](https://snapshooter.com/learn/mysql/top-tips-secure-mysql)
* [How to Secure MySQL and MariaDB Databases in a Linux VPS | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-secure-mysql-and-mariadb-databases-in-a-linux-vps)

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
