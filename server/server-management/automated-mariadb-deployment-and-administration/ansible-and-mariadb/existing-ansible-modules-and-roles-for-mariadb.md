---
description: >-
  Lists the Ansible modules for managing MariaDB, from the ansible.mariadb
  collection, such as mariadb_db, mariadb_user, and mariadb_variables, plus
  other useful modules and roles.
---

# Existing Ansible Modules and Roles for MariaDB

This page contains links to Ansible modules and roles that can be used to automate MariaDB deployment and configuration. The list is not meant to be exhaustive. Use it as a starting point, but then please do your own research.

## Modules

The [MariaDB collection](https://docs.ansible.com/projects/ansible/latest/collections/ansible/mariadb/index.html), `ansible.mariadb`, contains Ansible modules for MariaDB. It's included in the Ansible package and is also available from [Ansible Galaxy](https://galaxy.ansible.com/ui/repo/published/ansible/mariadb/). It contains the following modules:

* [mariadb\_binlog\_info](https://docs.ansible.com/projects/ansible/latest/collections/ansible/mariadb/mariadb_binlog_info_module.html): gathers binary log information.
* [mariadb\_db](https://docs.ansible.com/projects/ansible/latest/collections/ansible/mariadb/mariadb_db_module.html): adds or removes databases.
* [mariadb\_info](https://docs.ansible.com/projects/ansible/latest/collections/ansible/mariadb/mariadb_info_module.html): gathers information about a MariaDB server.
* [mariadb\_password\_policy](https://docs.ansible.com/projects/ansible/latest/collections/ansible/mariadb/mariadb_password_policy_module.html): manages password policy settings.
* [mariadb\_perf\_schema](https://docs.ansible.com/projects/ansible/latest/collections/ansible/mariadb/mariadb_perf_schema_module.html): manages the Performance Schema setup tables.
* [mariadb\_query](https://docs.ansible.com/projects/ansible/latest/collections/ansible/mariadb/mariadb_query_module.html): runs SQL queries.
* [mariadb\_replication](https://docs.ansible.com/projects/ansible/latest/collections/ansible/mariadb/mariadb_replication_module.html): configures and operates replication.
* [mariadb\_replication\_filter](https://docs.ansible.com/projects/ansible/latest/collections/ansible/mariadb/mariadb_replication_filter_module.html): manages replication filters.
* [mariadb\_role](https://docs.ansible.com/projects/ansible/latest/collections/ansible/mariadb/mariadb_role_module.html): adds, removes, or updates roles.
* [mariadb\_slow\_log](https://docs.ansible.com/projects/ansible/latest/collections/ansible/mariadb/mariadb_slow_log_module.html): manages slow query log settings.
* [mariadb\_user](https://docs.ansible.com/projects/ansible/latest/collections/ansible/mariadb/mariadb_user_module.html): adds or removes users.
* [mariadb\_variables](https://docs.ansible.com/projects/ansible/latest/collections/ansible/mariadb/mariadb_variables_module.html): manages server variables.

Note that some modules only exist as shortcuts, and it is possible to use mariadb\_query instead. However, it is important to notice that mariadb\_query is not idempotent. Ansible does not understand SQL queries, therefore it cannot check whether a query needs to be run or not.

To install this collection locally:

```bash
ansible-galaxy collection install ansible.mariadb
```

{% hint style="info" %}
`ansible.mariadb` is a fork of the MySQL collection, `ansible.mysql`, which was previously named `community.mysql`. The MySQL collection still works with MariaDB, but only receives bug fixes and security fixes for it, and drops MariaDB support in its release 6.0.0. If your playbooks use the MySQL collection's modules with MariaDB, change their names to the MariaDB collection's, for example `community.mysql.mysql_user` to `ansible.mariadb.mariadb_user`. The parameters are the same.
{% endhint %}

MariaDB Corporation maintains a [ColumnStore playbook](https://github.com/mariadb-corporation/columnstore-ansible) on GitHub.

### Other Useful Modules

Let's see some other modules that are useful to manage MariaDB servers.

#### shell and command

Modules like [shell](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/command_module.html#ansible-collections-ansible-builtin-command-module) and [command](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/command_module.html#ansible-collections-ansible-builtin-command-module) allow one to run system commands.

To deploy on Windows, [win\_shell](https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_shell_module.html#ansible-collections-ansible-windows-win-shell-module) and [win\_command](https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_command_module.html#ansible-collections-ansible-windows-win-command-module) can be used.

Among other things, it is possible to use one of these modules to run MariaDB queries:

```yaml
- name: Make the server read-only
  # become root to log into MariaDB with UNIX_SOCKET plugin
  become: yes
  shell: $( which mariadb ) -e "SET GLOBAL read_only = 1;"
```

The main disadvantage with these modules is that they are not idempotent, because they're meant to run arbitrary system commands that Ansible can't understand. They are still useful in a variety of cases:

* To run queries, because mariadb\_query is also not idempotent.
* In cases when other modules do not allow us to use the exact arguments we need to use, we can achieve our goals by writing shell commands ourselves.
* To run custom scripts that implement non-trivial logic. Implementing complex logic in Ansible tasks is possible, but it can be tricky and inefficient.
* To call [command-line tools](../../../clients-and-utilities/). There may be specific roles for some of the most common tools, but most of the times using them is an unnecessary complication.

#### copy and template

An important part of configuration management is copying [configuration files](../../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) to remote servers.

The [copy module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/copy_module.html) allows us to copy files to target hosts. This is convenient for static files that we want to copy exactly as they are. An example task:

```yaml
- name: Copy my.cnf
  copy:
    src: ./files/my.cnf.1
    dest: /etc/mysql/my.cnf
```

As you can see, the local name and the name on remote host don't need to match. This is convenient, because it makes it easy to use different configuration files with different servers. By default, files to copy are located in a `files` subdirectory in the role.

However, typically the content of a configuration file should vary based on the target host, the group and various variables. To do this, we can use the [template](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/template_module.html) module, which compiles and copies templates written in [Jinja](https://jinja.palletsprojects.com/en/2.11.x/).

A simple template task:

```yaml
- name: Compile and copy my.cnf
  template:
    src: ./templates/my.cnf.j2
    dest: /etc/mysql/my.cnf
```

Again, the local and the remote names don't have to match. By default, Jinja templates are located in a `templates` subdirectory in the role, and by convention they have the `.j2` extension. This is because Ansible uses Jinja version 2 for templating, at the time writing.

A simple template example:

```ini
## WARNING: DO NOT EDIT THIS FILE MANUALLY !!
## IF YOU DO, THIS FILE WILL BE OVERWRITTEN BY ANSIBLE

[mysqld]
innodb_buffer_pool_size = {{ innodb_buffer_pool_size }}
{{ 'connect_work_size = ' ~ connect_work_size if connect_work_size is defined else '' }}
```

The second line writes `connect_work_size` only if the variable is defined.

#### Other Common Modules

The following modules are also often used for database servers:

* [package](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/package_module.html), [apt](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_module.html) or [yum](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/yum_module.html). Package is package manager-agnostic. Use them to install, uninstall and upgrade packages.
* [user](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/user_module.html), useful to create the system user and group that run MariaDB binary.
* [file](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/file_module.html) can be used to make sure that MariaDB directories (like the data directory) exist and have proper permissions. It can also be used to upload static files.
* [template](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/template_module.html) allows to create configuration files (like `my.cnf`) more dynamically, using the [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) template language.
* [service](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/service_module.html) is useful after installing MariaDB as a service, to start it, restart it or stop it.

## Roles

Specific roles exist for MariaDB in Ansible Galaxy. Using them for MariaDB is generally preferable, to be sure to avoid [incompatibilities](../../../editions-and-compatibility/comparisons-with-other-databases/mariadb-vs-mysql-compatibility.md) and to probably be able to use some MariaDB specific [features](../../../editions-and-compatibility/comparisons-with-other-databases/mariadb-vs-mysql-features.md). However, using MySQL or Percona Server roles is also possible. This probably makes sense for users who also administer MySQL and Percona Server instances.

To find roles that suits you, check [Ansible Galaxy search page](https://galaxy.ansible.com/search?deprecated=false\&keywords=\&order_by=-relevance). Most roles are also available on GitHub.

You can also search roles using the [ansible-galaxy](https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html) tool:

```bash
ansible-galaxy search mariadb
```

## See Also

* [MariaDB Deployment and Management with Ansible](https://youtu.be/CV8-56Fgjc0) (video)

Content initially contributed by [Vettabase Ltd](https://vettabase.com/).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
