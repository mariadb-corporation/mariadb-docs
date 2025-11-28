---
description: >-
  The Feedback plugin collects and sends anonymous server usage and
  configuration data to MariaDB to help improve the software.
---

# Feedback Plugin

The `feedback` plugin is designed to collect and, optionally, upload\
configuration and usage information to [MariaDB.org](https://mariadb.org/) or to any other configured URL.

See the [MariaDB User Feedback](https://mariadb.org/feedback-plugin/) page on MariaDB.org to see collected MariaDB usage statistics.

MariaDB is usually distributed with this plugin included, but it is not enabled by default.\
On Windows, this plugin is part of the server and has a special checkbox in the installer window. Either way, you need to explicitly install and enable it in order for feedback data to be sent.

## Verifying the Plugin's Status

To verify whether the `feedback` plugin is installed and enabled, execute the [SHOW PLUGINS](../../sql-statements/administrative-sql-statements/show/show-plugins.md) statement or query the [information\_schema.plugins](../../system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md) table:

```sql
SELECT plugin_status FROM information_schema.plugins 
  WHERE plugin_name = 'feedback';
+---------------+
| plugin_status |
+---------------+
| DISABLED      |
+---------------+
```

If that `SELECT` returns no rows, then you still need to install the plugin.

When the plugin is installed and enabled, you will see:

```sql
SELECT plugin_status FROM information_schema.plugins 
  WHERE plugin_name = 'feedback';
+---------------+
| plugin_status |
+---------------+
| ACTIVE        |
+---------------+
```

## Installing the Plugin

In some releases, the plugin's shared library is distributed with MariaDB by default, but the plugin is not actually installed by MariaDB. There are two methods that can be used to install the plugin with MariaDB.

The first method can be used to install the plugin without restarting the server. You can install the plugin dynamically by executing [INSTALL SONAME](../../sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) or [INSTALL PLUGIN](../../sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md):

```
INSTALL SONAME 'feedback';
```

The second method can be used to tell the server to load the plugin when it starts up. The plugin can be installed this way by providing the [--plugin-load](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#plugin-load) or the [--plugin-load-add](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#plugin-load-add) options. This can be specified as a command-line argument to mariadbd, or it can be specified in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```ini
[mariadb]
...
plugin_load_add = feedback
```

## Uninstalling the Plugin

You can uninstall the plugin dynamically by executing [UNINSTALL SONAME](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md):

```sql
UNINSTALL SONAME 'feedback';
```

If you installed the plugin by providing the [`--plugin-load`](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or the [`--plugin-load-add`](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) options in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), then those options should be removed to prevent the plugin from being loaded the next time the server is restarted.

## Enabling the Plugin

You can enable the plugin by setting the [`feedback`](feedback-plugin.md#feedback) option to `ON` in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```ini
[mariadb]
...
feedback=ON
```

In Windows, the plugin can also be enabled during a new [MSI](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-msi-packages-on-windows.md) installation. The MSI GUI installation provides the "Enable feedback plugin" checkbox to enable the plugin. The MSI command-line installation provides the `FEEDBACK=1` command-line option to enable the plugin.

See the next section for how to verify the plugin is installed and active and (if needed) install the plugin.

## Collecting Data

The `feedback` plugin collects the following data:

* Certain rows from [SHOW STATUS](../../sql-statements/administrative-sql-statements/show/show-status.md) and [SHOW VARIABLES](../../sql-statements/administrative-sql-statements/show/show-variables.md).
* All installed [plugins](../) and their versions.
* System information such as CPU count, memory, architecture, and OS/linux distribution.
* The [feedback\_server\_uid](feedback-plugin.md#feedback_server_uid), which is a SHA1 hash of the MAC address of the first network interface and the TCP port that the server listens on.

The `feedback` plugin creates the [FEEDBACK](../../system-tables/information-schema/information-schema-tables/information-schema-feedback-table.md) table in the [INFORMATION\_SCHEMA](../../system-tables/information-schema/) database. To see the data that has been collected by the plugin, you can execute:

```sql
SELECT * FROM information_schema.feedback;
```

Only the contents of this table are sent to the [feedback\_url](feedback-plugin.md#feedback_url).

MariaDB stores collation usage statistics. Each collation that has been used by the server\
will have a record in output of `SELECT * FROM information_schema.feedback` , for example:

```
+----------------------------------------+---------------------+
| VARIABLE_NAME                          | VARIABLE_VALUE      |
+----------------------------------------+---------------------+
| Collation used utf8_unicode_ci         | 10                  |
| Collation used latin1_general_ci       | 20                  |
+----------------------------------------+---------------------+
```

Collations that have not been used will not be included in the result.

## Sending Data

The `feedback` plugin sends the data using a `POST` request to any URL or a list of URLs\
that you specify by setting the [feedback\_url](feedback-plugin.md#feedback_url) system variable. By default, this is set to the following URL:

* https://feedback.mariadb.org/rest/v1/post

Both HTTP and HTTPS protocols are supported.

If HTTP traffic requires a proxy in your environment, then you can specify the proxy by setting the [feedback\_http\_proxy](feedback-plugin.md#feedback_http_proxy) system variable.

If the [feedback\_url](feedback-plugin.md#feedback_url) system variable is not set to an empty string, then the\
plugin will automatically send a report to all URLs in the list a few minutes after the server starts up and then once a week after that.

If the [feedback\_url](feedback-plugin.md#feedback_url) system variable is set to an empty string, then the\
plugin will **not** automatically send any data. This may be necessary if outbound HTTP communication from your database server is not permitted. In this case, you can still upload the data manually, if you'd like.

First, generate the report file with the MariaDB command-line [mariadb](../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) client:

```bash
$ mariadb -e 'select * from information_schema.feedback' > report.txt
```

Then, you can upload the generated `report.txt` [here](https://feedback.mariadb.org/rest/v1/post) from the command line with tools such as [curl](https://curl.haxx.se/docs/manpage.html):

```bash
$ curl -F data=@report.txt https://feedback.mariadb.org/rest/v1/post
```

Manual uploading allows you to be absolutely sure that we receive only the data shown in the [INFORMATION\_SCHEMA.FEEDBACK](../../system-tables/information-schema/information-schema-tables/information-schema-feedback-table.md) table and that no private or sensitive information is being sent.

## System Variables

### `feedback_http_proxy`

* Description: Proxy server for use when http calls cannot be made, such as in a firewall environment. The format is `host:port`.
* Command line: `--feedback-http=proxy=value`
* Read-only: Yes
* Data Type: string
* Default Value: `''` (empty)

### `feedback_send_retry_wait`

* Description: Time in seconds before retrying if the plugin failed to send the data for any reason.
* Command line: `--feedback-send-retry-wait=#`
* Scope: Global
* Dynamic: Yes
* Data Type: numeric
* Default Value: `60`
* Valid Values: `1` to `86400`

### `feedback_send_timeout`

* Description: An attempt to send the data times out and fails after this many seconds.
* Command line: `--feedback-send-timeout=#`
* Scope: Global
* Dynamic: Yes
* Data Type: numeric
* Default Value: `60`
* Valid Values: `1` to `86400`

### `feedback_server_uid`

* Description: Automatically calculated server unique id hash.
* Scope: Global
* Dynamic: No
* Data Type: string

### `feedback_url`

* Description: URL to which the data is sent. More than one URL, separated by spaces, can be specified. Set it to an empty string to disable data sending.
* Command line: `--feedback-url=url`
* Scope: Global
* Dynamic: No
* Data Type: string
* Default Value: https://feedback.mariadb.org/rest/v1/post

### `feedback_user_info`

* Description: The value of this option is not used by the plugin, but it is included in the feedback data. It can be used to add any user-specified string to the report. This could be used to help to identify it. For example, a support contract number, or a computer name (if you collect reports internally by specifying your own `feedback-url`).
* Command line: `--feedback-user-info=string`
* Scope: Global
* Dynamic: No
* Data Type: string
* Default Value: Empty string

## Options

### `feedback`

* Description: Controls how the server should treat the plugin when the server starts up.
  * Valid values are:
    * `OFF` - Disables the plugin without removing it from the [mysql.plugins](../../system-tables/the-mysql-database-tables/mysql-plugin-table.md) table.
    * `ON` - Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.
    * `FORCE` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.
    * `FORCE_PLUS_PERMANENT` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with [UNINSTALL SONAME](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) while the server is running.
  * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
* Command line: `--feedback=value`
* Data Type: `enumerated`
* Default Value: `ON`
* Valid Values: `OFF`, `ON`, `FORCE`, `FORCE_PLUS_PERMANENT`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
