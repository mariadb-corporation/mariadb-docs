# Existing Ansible Modules and Roles for MariaDB

This page contains links to Ansible modules and roles that can be used to automate MariaDB deployment and configuration. The list is not meant to be exhaustive. Use it as a starting point, but then please do your own research.

## Modules

At the time of writing, there are no MariaDB-specific modules in Ansible Galaxy. MySQL modules can be used. Trying to use MySQL-specific features may result in errors or unexpected behavior. However, the same applies when trying to use a feature not supported by the MySQL version in use.

Currently, the [MySQL collection](https://galaxy.ansible.com/community/mysql?extIdCarryOver=true\&sc_cid=701f2000001OH7YAAW) in Ansible Galaxy contains at least the following modules:

* [mysql\_db](https://docs.ansible.com/ansible/latest/collections/community/mysql/mysql_db_module.html): manages MySQL databases.
* [mysql\_info](https://docs.ansible.com/ansible/latest/collections/community/mysql/mysql_info_module.html): gathers information about a MySQL server.
* [mysql\_query](https://docs.ansible.com/ansible/latest/collections/community/mysql/mysql_query_module.html): runs SQL queries against MySQL.
* [mysql\_replication](https://docs.ansible.com/ansible/latest/collections/community/mysql/mysql_replication_module.html): configures and operates asynchronous replication.
* [mysql\_user](https://docs.ansible.com/ansible/latest/collections/community/mysql/mysql_user_module.html): creates, modifies and deletes MySQL users.
* [mysql\_variables](https://docs.ansible.com/ansible/latest/collections/community/mysql/mysql_variables_module.html): manages MySQL configuration.

Note that some modules only exist as shortcuts, and it is possible to use mysql\_query instead. However, it is important to notice that mysql\_query is not idempotent. Ansible does not understand MySQL queries, therefore it cannot check whether a query needs to be run or not.

To install this collection locally:

```
ansible-galaxy collection install community.mysql
```

MariaDB Corporation maintains a [ColumnStore playbook](https://github.com/mariadb-corporation/columnstore-ansible) on GitHub.

### Other Useful Modules

Let's see some other modules that are useful to manage MariaDB servers.

#### shell and command

Modules like [shell](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/command_module.html#ansible-collections-ansible-builtin-command-module) and [command](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/command_module.html#ansible-collections-ansible-builtin-command-module) allow one to run system commands.

To deploy on Windows, [win\_shell](https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_shell_module.html#ansible-collections-ansible-windows-win-shell-module) and [win\_command](https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_command_module.html#ansible-collections-ansible-windows-win-command-module) can be used.

Among other things, it is possible to use one of these modules to run MariaDB queries:

```
- name: Make the server read-only
  # become root to log into MariaDB with UNIX_SOCKET plugin
  become: yes
  shell: $( which mysql ) -e "SET GLOBAL read_only = 1;"
```

The main disadvantage with these modules is that they are not idempotent, because they're meant to run arbitrary system commands that Ansible can't understand. They are still useful in a variety of cases:

* To run queries, because mysql\_query is also not idempotent.
* In cases when other modules do not allow us to use the exact arguments we need to use, we can achieve our goals by writing shell commands ourselves.
* To run custom scripts that implement non-trivial logic. Implementing complex logic in Ansible tasks is possible, but it can be tricky and inefficient.
* To call [command-line tools](../../../../../../clients-and-utilities/). There may be specific roles for some of the most common tools, but most of the times using them is an unnecessary complication.

#### copy and template

An important part of configuration management is copying [configuration files](../../../../configuring-mariadb/configuring-mariadb-with-option-files.md) to remote servers.

The [copy module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/copy_module.html) allows us to copy files to target hosts. This is convenient for static files that we want to copy exactly as they are. An example task:

```
- name: Copy my.cnf
  copy:
    src: ./files/my.cnf.1
    dest: /etc/mysql/my.cnf
```

As you can see, the local name and the name on remote host don't need to match. This is convenient, because it makes it easy to use different configuration files with different servers. By default, files to copy are located in a `files` subdirectory in the role.

However, typically the content of a configuration file should vary based on the target host, the group and various variables. To do this, we can use the [template](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/template_module.html) module, which compiles and copies templates written in [Jinja](https://jinja.palletsprojects.com/en/2.11.x/).

A simple template task:

```
- name: Compile and copy my.cnf
  copy:
    src: ./templates/my.cnf.j2
    dest: /etc/mysql/my.cnf
```

Again, the local and the remote names don't have to match. By default, Jinja templates are located in a `templates` subdirectory in the role, and by convention they have the `.j2` extension. This is because Ansible uses Jinja version 2 for templating, at the time writing.

A simple template example:

```
## WARNING: DO NOT EDIT THIS FILE MANUALLY !!
## IF YOU DO, THIS FILE WILL BE OVERWRITTEN BY ANSIBLE

[mysqld]
innodb_buffer_pool_size = {{ innodb_buffer_pool_size }}

<div data-gb-custom-block data-tag="if" data-0='true' data-1='true' data-2='true' data-3='true'>

connect_work_size = {{ connect_work_size }}

</div>
```

#### Other Common Modules

The following modules are also often used for database servers:

* [package](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/package_module.html), [apt](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_module.html) or [yum](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/yum_module.html). Package is package manager-agnostic. Use them to install, uninstall and upgrade packages.
* [user](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/user_module.html), useful to create the system user and group that run MariaDB binary.
* [file](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/file_module.html) can be used to make sure that MariaDB directories (like the data directory) exist and have proper permissions. It can also be used to upload static files.
* [template](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/template_module.html) allows to create configuration files (like my.cnf) more dynamically, using the [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) template language.
* [service](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/service_module.html) is useful after installing MariaDB as a service, to start it, restart it or stop it.

## Roles

Specific roles exist for MariaDB in Ansible Galaxy. Using them for MariaDB is generally preferable, to be sure to avoid [incompatibilities](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/compatibility-and-differences/mariadb-vs-mysql-compatibility) and to probably be able to use some MariaDB specific [features](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/compatibility-and-differences/mariadb-vs-mysql-features). However, using MySQL or Percona Server roles is also possible. This probably makes sense for users who also administer MySQL and Percona Server instances.

To find roles that suits you, check [Ansible Galaxy search page](https://galaxy.ansible.com/search?deprecated=false\&keywords=\&order_by=-relevance). Most roles are also available on GitHub.

You can also search roles using the [ansible-galaxy](https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html) tool:

```
ansible-galaxy search mariadb
```

## See Also

* [MariaDB Deployment and Management with Ansible](https://youtu.be/CV8-56Fgjc0) (video)

Content initially contributed by [Vettabase Ltd](https://vettabase.com/).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
