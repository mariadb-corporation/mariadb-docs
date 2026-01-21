---
description: 'Quickstart Guide: Installing MariaDB Server'
---

# Installing MariaDB Server Guide

This guide provides step-by-step instructions for installing MariaDB Server on various operating systems, including package updates and security settings.

#### For Linux (Ubuntu/Debian/Red Hat-based distributions)

The most common way to install MariaDB on Linux is through your system's package manager.

**Steps:**

1.  Update Package List:

    Before installing, it's a good practice to update your package index.

    *   For Debian/Ubuntu:Bash

        ```bash
        sudo apt update
        ```
    *   For Red Hat/CentOS/Fedora:Bash

        ```bash
        sudo yum update # For older systems
        sudo dnf update # For newer systems
        ```
2.  Install MariaDB Server:

    Install the MariaDB server and client packages.

    *   For Debian/Ubuntu:Bash

        ```bash
        sudo apt install mariadb-server mariadb-client galera-4
        ```
    *   For Red Hat/CentOS/Fedora:Bash

        ```bash
        sudo dnf install mariadb mariadb-server
        ```
3.  Secure the Installation:

    After installation, run the security script to set a root password, remove anonymous users, and disable remote root login.

    ```bash
    sudo mariadb-secure-installation
    ```

    Follow the prompts to configure your security settings.
4.  Start and Verify the Service:

    MariaDB typically starts automatically after installation. You can check its status and manually start it if needed.

    *   Check status:

        ```bash
        sudo systemctl status mariadb
        ```
    *   Start service (if not running):Bash

        ```bash
        sudo systemctl start mariadb
        ```
    *   Verify installation by connecting as root:Bash

        ```bash
        mariadb -u root -p
        ```

        Enter the root password you set during the secure installation.

#### For Windows

For Windows, MariaDB provides an `.msi` installer for a straightforward graphical installation.

**Steps:**

1.  Download MariaDB:

    Visit the MariaDB downloads page to get the latest `.msi` installer.
2.  Run the Installer:

    Double-click the downloaded `.msi` file to start the installation wizard.
3.  Follow On-Screen Instructions:

    The installer will guide you through the process, including:

    * Accepting the end-user license agreement.
    * Selecting features and the installation directory.
    * Setting a password for the `root` user.
    * Configuring MariaDB as a service and setting the port (default is 3306).
    * Optionally, enabling UTF8 as the default server character set.

#### Important Notes:

* **Firewall:** Ensure your firewall is configured to allow connections to MariaDB on the appropriate port (default 3306) if you need remote access.
* **Root Password:** Always set a strong root password during the secure installation step.
* **Further Configuration:** For production environments, you may need to adjust further settings in the MariaDB configuration files (e.g., `my.cnf` on Linux).

#### Additional Resources:

* [Get Started with MariaDB](https://mariadb.com/get-started-with-mariadb/)
* [How To Install MariaDB on Ubuntu 22.04 - DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-mariadb-on-ubuntu-22-04)
* [Install MariaDB - MariaDBTutorial.com](https://www.mariadbtutorial.com/getting-started/install-mariadb/)

{% @marketo/form formId="4316" %}
