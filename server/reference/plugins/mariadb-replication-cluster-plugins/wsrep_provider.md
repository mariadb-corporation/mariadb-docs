# wsrep\_provider

This plugin is for [Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/). It splits up the `wsrep_provider_options` setting into individual configuration variables.

{% hint style="info" %}
The plugin is available from MariaDB 11.4, and built in to the server, but not enabled by default.
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

See the [wsrep\_provider\_options](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/wsrep-variable-details/wsrep_provider_options) page for what you can configure for Galera Cluster.

For plugin version and maturity level, see [this page](../information-on-plugins/list-of-plugins.md).
