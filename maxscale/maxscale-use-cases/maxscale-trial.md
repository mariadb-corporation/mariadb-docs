---
description: >-
  Evaluate MariaDB MaxScale with a free trial license key. Install the standard
  MaxScale packages, add the trial key, and switch to a production key later
  without reinstalling.
---

# MaxScale Trial

You can evaluate MariaDB MaxScale free of charge with a trial license key, under a
[proprietary license](https://mariadb.com/terms/). The trial license key determines the length of
your evaluation period.

Starting with MaxScale 26.10, there is no separate trial edition. A trial uses the standard
MaxScale packages, and MaxScale accepts either a trial license key or a production license key.
When your evaluation ends and you have an Enterprise Platform subscription, you replace the trial
key with a production key, without reinstalling MaxScale.

{% hint style="info" %}
MaxScale 25.10 had a separate MaxScale Trial edition, in the `maxscale-trial` package. If you are
running it, see [Moving from MaxScale 25.10 Trial](#moving-from-maxscale-25-10-trial).
{% endhint %}

### Getting the License Key

To evaluate MaxScale, you must first obtain a trial license key from the MariaDB Customer Portal.
This key validates your trial and determines the duration of your evaluation period.

1. **Log in to MariaDB ID**: Navigate to the [MaxScale Trial License page](https://customers.mariadb.com/license/maxscale-trial/).
   You will be prompted to sign in with your MariaDB ID. If you do not have an account,
   you can create one using your email, Google, GitHub, or LinkedIn credentials.
2. **Generate the Key**: Once logged in, follow the on-screen instructions
   to generate your unique MaxScale Trial license key.
3. **Save the Key**: Copy or download the generated key. You will need to provide
   this key during the MaxScale configuration process.

### Downloading MaxScale

Download MaxScale for your operating system from the
[MaxScale Trial download page](https://mariadb.com/downloads/trials/maxscale-trial/). It offers the
same packages as the [MaxScale download page](https://mariadb.com/downloads/enterprise/enterprise-maxscale/)
for Enterprise Platform subscribers.

### Installing MaxScale <a href="#installing-maxscale-trial" id="installing-maxscale-trial"></a>

Install the packages as described in the
[MaxScale Installation Guide](../maxscale-management/installation-and-configuration/maxscale-installation-guide.md).

If `/etc/maxscale.cnf` does not exist yet, the installation copies the template
`/etc/maxscale.cnf.template` to `/etc/maxscale.cnf`. The template is for reference, and
`/etc/maxscale.cnf` is the file MaxScale uses. The configuration file has been written with
the assumption that a MariaDB server is running on the same machine where MaxScale is installed.

Before starting MaxScale, the license key must be specified and the database
users needed by MaxScale must be created.

#### Configuring the License Key

Open `/etc/maxscale.cnf` and add a `license_key` entry to the `[maxscale]` section.
```
[maxscale]
...
license_key=...
```
The value of `license_key` can either be the license key itself or the
_absolute_ path to a file containing the license.

**NOTE** If the license is read from a file, it must be readable by the user `maxscale`.

MaxScale does not start without a valid license key. For the error messages MaxScale logs when the
key is missing, invalid, or expired, see
[Install a MaxScale License Key](../maxscale-management/installation-and-configuration/maxscale-license-key.md#troubleshoot).

#### Database Users used by MaxScale <a href="#database-users-used-by-maxscale" id="database-users-used-by-maxscale"></a>

MaxScale needs two database users for its own use; one user used by a MaxScale
[service](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#service)
for fetching user account information and another user used by the MaxScale
[monitor](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#monitor)
for monitoring the health of the MariaDB server and for performing operations on it.
The same user can be used for both purposes, provided the user has all the grants
needed by services and monitors.

In the following, the host is specified using '%', which means that MaxScale can access
the server from anywhere. In a non-trial context, it is advisable to use the specific
IP where MaxScale is running.

If you use the same user names and passwords - that is, `service_user/service_pw` and
`monitor_user/monitor_pw` - you do not need to modify `/etc/maxscale.cnf`.
Otherwise the user names and passwords must be updated accordingly.

**Service User**

The service user can be created with the following commands, executed
using the mariadb command line utility.

```sql
CREATE USER 'service_user'@'%' IDENTIFIED BY 'service_pw';
GRANT SELECT ON mysql.user TO 'service_user'@'%';
GRANT SELECT ON mysql.db TO 'service_user'@'%';
GRANT SELECT ON mysql.tables_priv TO 'service_user'@'%';
GRANT SELECT ON mysql.columns_priv TO 'service_user'@'%';
GRANT SELECT ON mysql.procs_priv TO 'service_user'@'%';
GRANT SELECT ON mysql.proxies_priv TO 'service_user'@'%';
GRANT SELECT ON mysql.roles_mapping TO 'service_user'@'%';
GRANT SELECT ON mysql.global_priv TO 'service_user'@'%';
GRANT SHOW DATABASES ON *.* TO 'service_user'@'%';
```

**Monitor User**

Creating the monitor user is more complicated, because the required GRANTs depend
both on what monitor is used and on the exact server version. The GRANTs needed
by the MariaDB Monitor, used for monitoring a regular MariaDB primary/replica
cluster can be found
[here](../reference/maxscale-monitors/mariadb-monitor/README.md#required-grants),
but for initial testing the user can be given blanket rights:

```sql
CREATE USER 'monitor_user'@'%' IDENTIFIED BY 'monitor_pw';
GRANT ALL ON *.* TO 'monitor_user'@'%';
```

In a non-trial context, the monitor user should be granted only the GRANTs it really needs.

#### Configuring the REST-API

The command line utility `maxctrl` and the web UI _MaxGUI_ communicate with
MaxScale using a REST-API. By default, MaxGUI requires that TLS is enabled
and it is configured as explained
[here](../maxscale-security/securing-your-maxscale-deployment.md#secure-gui-and-admin-interface-connections).

Alternatively, the requirement of TLS can be turned off by adding the entry
```
admin_secure_gui=false
```
to the `[maxscale]` section in the MaxScale configuration file.

Please note that unless TLS is configured, your administrative credentials
will be exposed in plain text over the network. Not using TLS should only
be in a trial context in a controlled environment.

#### Starting MaxScale <a href="#starting-maxscale-trial" id="starting-maxscale-trial"></a>

Once the database users have been created, MaxScale can be started.

```bash
sudo systemctl start maxscale.service
```

If no errors are shown by the command, which indicates that MaxScale started,
the error log of MaxScale should be checked.

```bash
sudo cat /var/log/maxscale/maxscale.log
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

If TLS has been configured, the secure mode must be enabled with the flag `--secure`
and the relevant parameters provided using the `--tls...` flags. Invoke `maxctrl`
with the flag `--help` for the details.

After that the web-browser can be pointed to `http://127.0.0.1:8989`.
Logging in is done using the username `admin` and the password `mariadb`.
If TLS has not been disabled by the setting `admin_secure_gui=false`, `https`
must be used.

Note that by default MaxScale listens only on the interface 127.0.0.1, which means that
you must access MaxScale from the same machine on which MaxScale is running. If you want
to access MaxScale over the network, you need to add

```bash
admin_host=0.0.0.0
```

to the `[maxscale]` section in `/etc/maxscale.cnf`.

<figure><img src="../.gitbook/assets/MaxGUI_login.png" alt="MaxScale login dialog, containing two form fields to input user name and password, a Remember me checkbox, and a Sign In button."><figcaption><p>MaxScale Login Dialog</p></figcaption></figure>

### Moving to a Production License Key <a href="#upgrading-to-maxscale" id="upgrading-to-maxscale"></a>

A trial and a production installation use the same MaxScale packages and the same configuration
file. To move from a trial to production, replace the trial key in `license_key` with a production
license key. You do not need to reinstall MaxScale. To get a production key, see
[Install a MaxScale License Key](../maxscale-management/installation-and-configuration/maxscale-license-key.md#get-your-license-key).

You can also change the key on a running MaxScale, without a restart:

```bash
maxctrl alter maxscale license_key=<new-key>
```

MaxScale rejects the change if the new key is not valid.

### Moving from MaxScale 25.10 Trial <a href="#moving-from-maxscale-25-10-trial" id="moving-from-maxscale-25-10-trial"></a>

MaxScale 25.10 Trial was a separate edition, installed from the `maxscale-trial` package. That
package conflicts with the standard `maxscale` package, so the two cannot be installed on the same
machine. To move from MaxScale 25.10 Trial to MaxScale 26.10:

1. Make a backup of `/etc/maxscale.cnf`. Uninstalling MaxScale Trial does not remove it, but the
   backup protects your configuration.
2. Uninstall the `maxscale-trial` package. Uninstalling it stops MaxScale.
3. Install MaxScale 26.10, as described in [Installing MaxScale](#installing-maxscale-trial).
   The installation keeps your existing `/etc/maxscale.cnf`.
4. Make sure `license_key` holds a valid license key: a trial key or a production key. The 25.10
   Trial configuration file already has a `license_key` entry, and MaxScale 26.10 reads it the
   same way.
5. Start MaxScale.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
