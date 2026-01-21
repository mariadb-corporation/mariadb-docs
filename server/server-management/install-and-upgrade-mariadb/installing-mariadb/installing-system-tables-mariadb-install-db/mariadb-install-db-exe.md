---
description: >-
  Details the use of `mariadb-install-db.exe` on Windows to create new database
  instances, set the root password, and register Windows services.
---

# Installing System Tables on Windows

The `mariadb-install-db.exe` utility is the Windows equivalent of [mariadb-install-db](../../../../clients-and-utilities/deployment-tools/mariadb-install-db.md).

## Functionality

The functionality of `mariadb-install-db.exe` is comparable with the shell script `mariadb-install-db` used on Unix, however it has been extended with both Windows specific functionality (creating a Windows service) and to generally useful functionality. For example, it can set the 'root' user password during database creation. It also creates the `my.ini` configuration file in the data directory and adds most important parameters to it (e.g port).

`mariadb-install-db.exe` is used by the MariaDB installer for Windows if the "Database instance" feature is selected. It obsoletes similar utilities and scripts that were used in the past such as `mysqld.exe` `--install`,`mysql_install_db.pl`, and `mysql_secure_installation.pl`.

| Parameter(s)                       | Description                                           |
| ---------------------------------- | ----------------------------------------------------- |
| `-?`, `--help`                     | Display help message and exit                         |
| `-d`, `--datadir=name`             | Data directory of the new database                    |
| `-S`, `--service=name`             | Name of the `Windows` service                         |
| `-p`, `--password=name`            | Password of the `root` user                           |
| `-P`, `--port=#`                   | `mysqld` port                                         |
| `-W`, `--socket=name`              | `named pipe` name                                     |
| `-D`, `--default-user`             | Create default user                                   |
| `-R`, `--allow-remote-root-access` | Allow remote access from network for user `root`      |
| `-N`, `--skip-networking`          | Do not use `TCP` connections, use `pipe` instead      |
| `-i`, `--innodb-page-size`         | `Innodb` page size, since `MariaDB 10.2.5`            |
| `-s`, `--silent`                   | Print less information                                |
| `-o`, `--verbose-bootstrap`        | Include `mysqld` bootstrap output                     |
| `-l`, `--large-pages`              | Use large pages, since `MariaDB 10.6.1`               |
| `-c`, `--config`                   | `my.ini` config template file, since `MariaDB 10.6.1` |

{% hint style="info" %}
**T**o create a Windows service, `mariadb-install-db.exe` should be run\
by a user with full administrator privileges (which means elevated command\
prompt on systems with UAC).
{% endhint %}

## Example

```
mariadb-install-db.exe --datadir=C:\db --service=MyDB --password=secret
```

will create the database in the directory `C:\db`, register the auto-start\
Windows service "MyDB", and set the root password to 'secret'.

To start the service from the command line, execute

```bash
sc start MyDB
```

## Removing Database Instances

If you run your database instance as service, to remove it completely from the\
command line, use

```bash
sc stop <servicename>
sc delete <servicename>
rmdir /s /q <path-to-datadir>
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
