# MaxScale Trial

With the release of MaxScale 25.01 under a proprietary license, MariaDB has introduced MaxScale Trial, a free version that lets users explore the latest GA features in 24-hour increments, up to one week from install. MaxScale Trial offers limited performance capacity, providing a hands-on way to evaluate MaxScale’s capabilities before committing to an enterprise subscription

### Installing MaxScale Trial <a href="#installing-maxscale-trial" id="installing-maxscale-trial"></a>

When the MaxScale Trial package has been installed, a template MaxScale configuration file will be copied to `/etc/maxscale.cnf.template` and `/etc/maxscale.cnf`; the former for reference and the latter for actual use. The configuration file has been written with the assumption that a MariaDB server is running on the same machine where MaxScale is installed.

Before starting MaxScale, the database users needed by MaxScale must be created.

#### Database Users used by MaxScale <a href="#database-users-used-by-maxscale" id="database-users-used-by-maxscale"></a>

MaxScale needs two database users for its own use; one user used by a MaxScale [service](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md#service) for fetching user account information and another user used by the MaxScale [monitor](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md#monitor) for monitoring the health of the MariaDB server and for performing operations on it. The same user can be used for both purposes, provided the user has all the grants needed by services and monitors.

In the following, the host is specified using '%', which means that MaxScale can access the server from anywhere. In a non-trial context, it is advisable to use the specific IP where MaxScale is running.

If you use the same user names and passwords - that is, `service_user/service_pw` and `monitor_user/monitor_pw` - you do not need to modify `/etc/maxscale.cnf`. Otherwise the user names and passwords must be updated accordingly.

**Service User**

The service user can be created with the following commands, executed using the mariadb command line utility.

```sql
CREATE USER 'service_user'@'%' IDENTIFIED BY 'service_pw';
GRANT SELECT ON mysql.user TO 'service_user'@'%';
GRANT SELECT ON mysql.db TO 'service_user'@'%';
GRANT SELECT ON mysql.tables_priv TO 'service_user'@'%';
GRANT SELECT ON mysql.columns_priv TO 'service_user'@'%';
GRANT SELECT ON mysql.procs_priv TO 'service_user'@'%';
GRANT SELECT ON mysql.proxies_priv TO 'service_user'@'%';
GRANT SELECT ON mysql.roles_mapping TO 'service_user'@'%';
GRANT SHOW DATABASES ON *.* TO 'service_user'@'%';
```

**Monitor User**

Creating the monitor user is more complicated, because the required GRANTs depend both on what monitor is used and on the exact server version. The GRANTs needed by the MariaDB Monitor, used for monitoring a regular MariaDB primary/replica cluster can be found here, but for initial testing the user can be given blanket rights:

```sql
CREATE USER 'monitor_user'@'%' IDENTIFIED BY 'monitor_pw';
GRANT ALL ON *.* TO 'monitor_user'@'%';
```

In a non-trial context, the monitor user should be granted only the GRANTs it really needs.

#### Starting MaxScale Trial <a href="#starting-maxscale-trial" id="starting-maxscale-trial"></a>

Once the database users have been created, MaxScale Trial can be started.

```bash
sudo service maxscale start
```

If no errors are shown by the command, which indicates that MaxScale started, the error log of MaxScale should be checked.

```bash
cat /var/log/maxscale/maxscale.log
```

If there are no error entries, MaxScale is running and can be used.

**Smoketests**

With the following command it can be checked that MaxScale can connect to the server

```bash
maxctrl list servers
```

and with the following command that the service is running

```bash
maxctrl list services
```

After that the web-browser can be pointed to [http://127.0.0.1:8989](http://127.0.0.1:8989/). Logging in is done using the username admin and the password mariadb.

Note that by default MaxScale listens only on the interface 127.0.0.1, which means that you must access MaxScale from the same machine on which MaxScale is running. If you want to access MaxScale over the network, you need to add

```bash
admin_host=0.0.0.0
```

to the `[maxscale]` section in `/etc/maxscale.cnf`.

<figure><img src="../.gitbook/assets/MaxGUI_login.png" alt="MaxScale Trial login dialog, containing two form fields to input user name and password, a Remember me checkbox, and a Sign In button."><figcaption><p>MaxScale Trial Login Dialog</p></figcaption></figure>

### Limitations of MaxScale Trial <a href="#limitations-of-maxscale-trial" id="limitations-of-maxscale-trial"></a>

Apart from the following limitations, MaxScale Trial is identical to MaxScale.

| #filters         | 2                                                               |
| ---------------- | --------------------------------------------------------------- |
| #servers         | 2                                                               |
| #services        | 1                                                               |
| #connections     | 15                                                              |
| Capture          | Capture size limited to 10MB and capture duration to 5 minutes. |
| Process lifetime | 24 hours after which the MaxScale Trial process will exit.      |
| Trial period     | 1 week from installation date.                                  |

At startup, if any of the limitations on the number of filters, servers or services is exceeded, MaxScale will not start and an error like the following will be logged:

```
2025-03-25 12:17:34   error  : (Read-Only-Service); The maximum limit of 1 services in MaxScale Trial has been reached. If insufficient, consider upgrading to MaxScale Enterprise: https://mariadb.com/maxscale-contact/
2025-03-25 12:17:34   error  : (Read-Only-Service); Service 'Read-Only-Service' creation failed.
2025-03-25 12:17:34   error  : 1 errors were encountered while processing configuration.
2025-03-25 12:17:34   alert  : Failed to process the MaxScale configuration file /etc/maxscale.cnf.
```

If the limit is exceeded at runtime with maxctrl, the operation will fail with an error like the following:

```
maxctrl create service Read-Only-Service router=readconnroute user=service_users
Error: Server at http://127.0.0.1:8989 responded with 400 Bad Request to `POST services`
{
    "errors": [
        {
            "detail": "The maximum limit of 1 services in MaxScale Trial has been reached. If insufficient, consider upgrading to MaxScale Enterprise: https://mariadb.com/maxscale-contact/"
        },
        {
            "detail": "Could not create service 'Read-Only-Service' with module 'router=readconnroute'"
        }
    ]
}
```

If the limit is exceeded at runtime using MaxGUI, the operation will fail with the following error message.

![MaxGUI\_error-message](../.gitbook/assets/MaxGUI_error-message.png)

If the connection limit is exceeded, the connection attempt will fail, and note that no error message will be displayed.

An attempt to explicitly raise [max\_connections](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md#max_connections) beyond the maximum of 15, will prevent MaxScale from running at startup and at runtime fail with a runtime error.

If the configured capture [size](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-workload-capture-and-replay.md#capture_size) or [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-workload-capture-and-replay.md#capture_duration) exceeds the maximum limit of MaxScale Trial, the value will be adjusted down to the allowed maximum value and an error will be logged.

### Upgrading to MaxScale <a href="#upgrading-to-maxscale" id="upgrading-to-maxscale"></a>

The configuration file of MaxScale Trial is 100% compatible with MaxScale. To replace MaxScale Trial with MaxScale, only the following steps are needed:

* Uninstall MaxScale Trial.
* Install MaxScale 25.01 or higher.

Although the uninstallation of MaxScale Trial will not cause the configuration file to be erased, it is recommended to make a backup of it before the operation.

It is not possible to have MaxScale Trial and MaxScale installed simultaneously on the same machine.

MaxScale configurations are not guaranteed to work in MaxScale Trial as MaxScale Trial has restrictions based on the documented limitations above which would block startup.\

{% @marketo/form formId="4316" %}
