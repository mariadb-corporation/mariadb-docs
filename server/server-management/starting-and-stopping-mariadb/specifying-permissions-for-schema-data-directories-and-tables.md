---
description: >-
  Explains default file permissions for data directories and how to customize
  them using `UMASK` and `UMASK_DIR` environment variables.
---

# Specifying Permissions for Schema (Data) Directories and Tables

## Default File Permissions

By default MariaDB uses the following permissions for files and directories:

| Object Type | Default Mode | Default Permissions |
| ----------- | ------------ | ------------------- |
| Files       | 0660         | -rw-rw----          |
| Directories | 0700         | drwx------          |

## Configuring File Permissions with Environment Variables

You can configure MariaDB to use different permissions for files and directories by setting the following [environment variables](../install-and-upgrade-mariadb/configuring-mariadb/mariadb-environment-variables.md) before you start the server:

| Object Type | Environment Variable |
| ----------- | -------------------- |
| Files       | UMASK                |
| Directories | UMASK\_DIR           |

In other words, if you would run the following in a shell:

```
export UMASK=0640
export UMASK_DIR=0750
```

These environment variables do not set the umask. They set the default file system permissions. See [MDEV-23058](https://jira.mariadb.org/browse/MDEV-23058) for more information.

### Configuring File Permissions With systemd

If your server is started by [systemd](systemd.md), then there is a specific way to configure the umask. See [Systemd: Configuring the umask](systemd.md#configuring-the-umask) for more information.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
