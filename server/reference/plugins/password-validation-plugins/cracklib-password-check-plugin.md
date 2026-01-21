---
description: >-
  The Cracklib Password Check Plugin enforces password strength by validating
  new passwords against the CrackLib library and its dictionary.
---

# Cracklib Password Check Plugin

`cracklib_password_check` is a [password validation](./) plugin. It uses the [CrackLib](https://github.com/cracklib/cracklib) library to check the strength of new passwords. CrackLib is installed by default in many Linux distributions, since the system's [Pluggable Authentication Module (PAM)](https://en.wikipedia.org/wiki/Pluggable_authentication_module) authentication framework is usually configured to check the strength of new passwords with the [pam\_cracklib](https://linux.die.net/man/8/pam_cracklib) PAM module.

Note that passwords can be directly set as a hash, bypassing the password validation, if the [strict\_password\_validation](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#strict_password_validation) variable is `OFF` (it is `ON` by default).

The plugin requires at least cracklib 2.9.0, so it is not available on Debian/Ubuntu builds before Debian 8 Jessie/Ubuntu 14.04 Trusty, RedHat Enterprise Linux / CentOS 6.

## Installing the Plugin's Package

The `cracklib_password_check` plugin's shared library is included in MariaDB packages as the `cracklib_password_check.so` or `cracklib_password_check.dll` shared library on systems where it can be built.

### Installing on Linux

The `cracklib_password_check` plugin is included in `systemd` [binary tarballs](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-binary-tarballs.md) on Linux, but not in the older generic and `glibc_214` tarballs.

#### Installing with a Package Manager

The `cracklib_password_check` plugin can also be installed via a package manager on Linux. In order to do so, your system needs to be configured to install from one of the MariaDB repositories.

You can configure your package manager to install it from MariaDB Corporation's MariaDB Package Repository by using the [MariaDB Package Repository setup script](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md).

You can also configure your package manager to install it from MariaDB Foundation's MariaDB Repository by using the [MariaDB Repository Configuration Tool](https://downloads.mariadb.org/mariadb/repositories/).

**Installing with yum/dnf**

On RHEL, CentOS, Fedora, and other similar Linux distributions, it is highly recommended to install the relevant [RPM package](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/) from MariaDB's repository using [yum](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/yum.md) or [dnf](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/yum.md). Starting with RHEL 8 and Fedora 22, `yum` has been replaced by `dnf`, which is the next major version of `yum`. However, `yum` commands still work on many systems that use `dnf`:

```bash
sudo yum install MariaDB-cracklib-password-check
```

**Installing with apt-get**

On Debian, Ubuntu, and other similar Linux distributions, it is highly recommended to install the relevant [DEB package](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-deb-files.md) from MariaDB's repository using [apt-get](https://wiki.debian.org/apt-get):

```sql
sudo apt-get install mariadb-plugin-cracklib-password-check
```

**Installing with zypper**

On SLES, OpenSUSE, and other similar Linux distributions, it is highly recommended to install the relevant [RPM package](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/) from MariaDB's repository using [zypper](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper.md):

```bash
sudo zypper install MariaDB-cracklib-password-check
```

## Installing the Plugin

Once the shared library is in place, the plugin is not actually installed by MariaDB by default. There are two methods that can be used to install the plugin with MariaDB.

The first method can be used to install the plugin without restarting the server. You can install the plugin dynamically by executing [INSTALL SONAME](../../sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) or [INSTALL PLUGIN](../../sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md):

```sql
INSTALL SONAME 'cracklib_password_check';
```

The second method can be used to tell the server to load the plugin when it starts up. The plugin can be installed this way by providing the [--plugin-load](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#plugin-load) or the [--plugin-load-add](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#plugin-load-add) options. This can be specified as a command-line argument to mariadbd, or it can be specified in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```ini
[mariadb]
...
plugin_load_add = cracklib_password_check
```

## Uninstalling the Plugin

You can uninstall the plugin dynamically by executing [UNINSTALL SONAME](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md):

```sql
UNINSTALL SONAME 'cracklib_password_check';
```

If you installed the plugin by providing the [--plugin-load](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#plugin-load) or the [--plugin-load-add](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#plugin-load-add) options in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), then those options should be removed to prevent the plugin from being loaded the next time the server is restarted.

## Viewing CrackLib Errors

If password validation fails, then the original CrackLib error message can be viewed by executing [SHOW WARNINGS](../../sql-statements/administrative-sql-statements/show/show-warnings.md).

## Example

When creating a new password, if the criteria are not met, the following error is returned:

```sql
SET PASSWORD FOR 'bob'@'%.loc.gov' = PASSWORD('abc');
ERROR 1819 (HY000): Your password does not satisfy the current policy requirements
```

## Known Issues

### SELinux

When using the standard [SELinux](../../../security/securing-mariadb/selinux.md) policy with the [mode](../../../security/securing-mariadb/selinux.md#changing-selinuxs-mode) set to `enforcing`, `mariadbd` does not have access to `/usr/share/cracklib`, and you may see the following error when attempting to use the `cracklib_password_check` plugin:

```sql
CREATE USER `user`@`hostname` IDENTIFIED BY 's0mePwd123.';
ERROR 1819 (HY000): Your password does not satisfy the current policy requirements

SHOW WARNINGS;
+---------+------+----------------------------------------------------------------+
| Level   | Code | Message                                                        |
+---------+------+----------------------------------------------------------------+
| Warning | 1819 | cracklib: error loading dictionary                             |
| Error   | 1819 | Your password does not satisfy the current policy requirements |
| Error   | 1396 | Operation CREATE USER failed for 'user'@'hostname'             |
+---------+------+----------------------------------------------------------------+
```

And the SELinux `audit.log` contains errors like these:

```
type=AVC msg=audit(1548371977.821:66): avc:  denied  { read } for  pid=3537 comm="mysqld" name="pw_dict.pwd" dev="xvda2" ino=564747 scontext=system_u:system_r:mysqld_t:s0 tcontext=system_u:object_r:crack_db_t:s0 tclass=file
type=SYSCALL msg=audit(1548371977.821:66): arch=c000003e syscall=2 success=no exit=-13 a0=7fdd2a674580 a1=0 a2=1b6 a3=1b items=0 ppid=1 pid=3537 auid=4294967295 uid=995 gid=992 euid=995 suid=995 fsuid=995 egid=992 sgid=992 fsgid=992 tty=(none) ses=4294967295 comm="mysqld" exe="/usr/sbin/mysqld" subj=system_u:system_r:mysqld_t:s0 key=(null)
```

This can be fixed by creating an SELinux policy that allows `mysqld` to load the CrackLib dictionary:

```bash
cd /usr/share/mysql/policy/selinux/
tee ./mariadb-plugin-cracklib-password-check.te <<EOF

module mariadb-plugin-cracklib-password-check 1.0;

require {
        type mysqld_t;
        type crack_db_t;
        class file { execute setattr read create getattr execute_no_trans write ioctl open append unlink };
        class dir { write search getattr add_name read remove_name open };
}

allow mysqld_t crack_db_t:dir { search read open };
allow mysqld_t crack_db_t:file { getattr read open };
EOF
sudo yum install selinux-policy-devel
make -f /usr/share/selinux/devel/Makefile mariadb-plugin-cracklib-password-check.pp
sudo semodule -i mariadb-plugin-cracklib-password-check.pp
```

See [MDEV-18374](https://jira.mariadb.org/browse/MDEV-18374) for more information.

## System Variables

#### `cracklib_password_check_dictionary`

* Description: Sets the path to the CrackLib dictionary. If not set, the default CrackLib dictionary path is used. The parameter expects the base name of a cracklib dictionary (a set of three files with endings `.hwm`, `.pwd`, `.pwi`), not a directory path.
* Command line: `--cracklib-password-check-dictionary=value`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: Depends on the system. Often `/usr/share/cracklib/pw_dict`

## Options

#### `cracklib_password_check`

* Description: Controls how the server should treat the plugin when the server starts up.
  * Valid values are:
    * `OFF` - Disables the plugin without removing it from the [mysql.plugins](../../system-tables/the-mysql-database-tables/mysql-plugin-table.md) table.
    * `ON` - Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.
    * `FORCE` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.
    * `FORCE_PLUS_PERMANENT` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with [UNINSTALL SONAME](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) while the server is running.
  * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
* Command line: `--cracklib-password-check=value`
* Data Type: `enumerated`
* Default Value: `ON`
* Valid Values: `OFF`, `ON`, `FORCE`, `FORCE_PLUS_PERMANENT`

## See Also

* [Password Validation](./)
* [simple\_password\_check plugin](simple-password-check-plugin.md) - permits the setting of basic criteria for passwords

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
