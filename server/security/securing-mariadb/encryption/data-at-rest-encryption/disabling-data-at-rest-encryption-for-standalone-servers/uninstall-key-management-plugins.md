# Uninstall Key Management Plugins

Once all data and logs have been decrypted, you can safely remove key management plugins, if desired. For example, if using the file key management plugin:

```ini
Comment out or remove the following lines 
plugin_load_add = file_key_management 
file_key_management_filename = /etc/mysql/encryption/keyfile
```

Restart the server after editing the configuration.

* Ensure that all tables no longer report encryption in `CREATE_OPTIONS`.
* Confirm that redo logs and binary logs are unencrypted by checking server variables and log headers.
* Confirm that no key management plugin is loaded:

```sql
SHOW PLUGINS;
```
