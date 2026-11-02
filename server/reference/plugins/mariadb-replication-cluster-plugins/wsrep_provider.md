---
description: >-
  The wsrep_provider plugin exposes Galera Cluster provider options as
  individual system variables, allowing for easier configuration and validation
  of cluster settings.
---

# wsrep\_provider

This plugin is for [Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/). It splits up the `wsrep_provider_options` setting into individual configuration variables.

{% hint style="info" %}
The plugin is available from MariaDB 11.0, and built in to the server, but not enabled by default.
{% endhint %}

Without that plugin, options are grouped together, like this:

```ini
wsrep_provider_options="base_dir = /var/lib/mysql/; base_host = node-1;..."
```

With this plugin loaded, you can configure individual variables, like this:

```ini
wsrep_provider_base_dir  = /var/lib/mysql/
wsrep_provider_base_host = node-1
...
```

This makes managing provider options easier, and helps avoid the problem of wsrep\_provider\_options exceeding the maximum length of 2048 characters for an individual variable.

To enable the plugin, add the following line to the `[mariadbd]`, `[server]`, or `[galera]` sections of your [server option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```ini
plugin-wsrep-provider=ON
```

Alternatively, start the server with the `--plugin-wsrep-provider` option.

## Changing Provider Options at Runtime

When the plugin is enabled, `wsrep_provider_options` can no longer be changed while the server is running. A `SET GLOBAL wsrep_provider_options=...` statement fails, even for options that are dynamic. Set the individual system variable for the option instead. Its name is `wsrep_provider_` followed by the option name, with dots replaced by underscores. For example, to bootstrap a new Primary Component:

```sql
-- Fails when the plugin is enabled:
SET GLOBAL wsrep_provider_options='pc.bootstrap=YES';

-- Use this instead:
SET GLOBAL wsrep_provider_pc_bootstrap=ON;
```

The failing statement returns this error from MariaDB 11.4.13, 11.8.9, 12.3.3, and 13.0.2:

```
ERROR 1210 (HY000): wsrep_provider_options cannot be changed while the wsrep-provider plugin is loaded
```

Earlier releases report the variable as read-only instead:

```
ERROR 1238 (HY000): Variable 'wsrep_provider_options' is a read only variable
```

The same applies to every other dynamic option. For example, set `wsrep_provider_pc_weight` instead of `pc.weight` in `wsrep_provider_options`.

See the [wsrep\_provider\_options](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/wsrep-variable-details/wsrep_provider_options) page for what you can configure for Galera Cluster.

For plugin version and maturity level, see [this page](../information-on-plugins/list-of-plugins.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
