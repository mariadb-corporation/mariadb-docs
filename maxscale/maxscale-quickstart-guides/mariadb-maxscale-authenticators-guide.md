---
description: >-
  Configure secure access to your database. This guide explains how to set up
  authenticators in MaxScale to manage client credentials and validate
  connections to backend servers.
---

# MariaDB MaxScale Authenticators Guide

### Quickstart Guide: MariaDB MaxScale Authentication Modules

MariaDB MaxScale incorporates robust authentication modules to manage client access and ensure secure communication with your backend MariaDB servers. Understanding these modules is crucial for securing your database deployments when using MaxScale.

#### 1. What are MaxScale Authentication Modules?

MaxScale's authentication modules (often referred to as "authenticator plugins") are components that handle client authentication. They determine how incoming clients verify their identity to MaxScale and, in turn, how MaxScale authenticates itself to the backend MariaDB servers. This process is similar to how authentication works directly with MariaDB Server using the MySQL protocol.

#### 2. How Authentication Works in MaxScale

MaxScale employs a **User Account Manager (UAM)** for services that use a MariaDB protocol listener.

* The UAM is responsible for storing and managing user account information.
* It typically queries the `mysql` database on your backend MariaDB servers (usually the primary) to retrieve user account details.
* Using this information, the UAM authenticates connecting clients, verifies their passwords, and checks their database access rights.
* The `user` and `password` settings within your MaxScale service configuration define the credentials MaxScale uses to fetch these user accounts from the backend databases.

#### 3. Available Authentication Plugins

MaxScale supports various authentication schemes through different plugins:

* **Standard MySQL Password:** This is the most common authentication method, verifying user credentials against those stored in the backend MariaDB server's `mysql.user` table (or similar).
* **GSSAPI (Generic Security Service Application Programming Interface):** Provides secure authentication methods, often used in enterprise environments with Kerberos or similar systems.
* **PAM (Pluggable Authentication Modules):** Allows MaxScale to integrate with PAM, enabling authentication against external systems like Unix system users, LDAP, or Active Directory.

#### 4. Basic Configuration Concepts

Authentication options are primarily defined within the listener configuration of your MaxScale service in the `maxscale.cnf` file.

a. Specifying the Authenticator:

The authenticator parameter specifies which authentication plugin to use for a particular listener.

**Example `maxscale.cnf` snippet (simplified):**

Ini, TOML

```ini
[my_service]
type=service
router=readwritesplit
servers=server1,server2
user=maxscale_user # User MaxScale uses to connect to backend MariaDB for UAM
password=maxscale_password

[my_listener]
type=listener
service=my_service
protocol=MariaDBClient
port=3306
authenticator=MariaDBAuth # Example: Use the standard MariaDB password authentication
# authenticator=GSSAPIAuth # Or GSSAPI authentication
# authenticator=PAMAuth    # Or PAM authentication
```

b. Authenticator Options (authenticator\_options):

Additional settings can be passed to the authenticator plugin using authenticator\_options. These are comma-separated key-value pairs.

**Common `authenticator_options`:**

* **`skip_authentication=true`:** (Use with extreme caution, typically only for development/testing). This option bypasses password checks for connecting clients. Clients will still need a valid username in the backend database, but their password will not be verified.
* **`match_host=false`:** Disables host matching for user accounts. By default, MariaDB (and thus MaxScale's UAM) matches user accounts based on both username and host (e.g., `'user'@'localhost'`). Setting this to `false` means only the username needs to match.
* **`lower_case_table_names=true/false`:** Controls how database names are matched during authentication, similar to the `lower_case_table_names` system variable in MariaDB Server.

**Example with options:**

Ini, TOML

```ini
[my_listener]
# ... other settings ...
authenticator=MariaDBAuth
authenticator_options=skip_authentication=true,match_host=false
```

By configuring these authentication modules, you can control how clients connect to your MariaDB through MaxScale, enforce security policies, and integrate with existing authentication infrastructure.

#### Further Resources:

* [MariaDB MaxScale Authentication Modules Documentation](../maxscale-security/authentication-modules.md)
* [MariaDB MaxScale Documentation](../maxscale-use-cases/maxscale-overview.md)
