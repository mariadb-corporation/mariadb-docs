---
description: >-
  Best practices for handling sensitive information like database passwords and
  SSH keys within Ansible, recommending the use of `ansible-vault` to encrypt
  secrets.
---

# Managing Secrets in Ansible

An Ansible role often runs commands that require certain privileges, so it must perform some forms of login, using passwords or key pairs. In the context of database automation, we normally talk about: SSH access, sudo access, and access to MariaDB. If we write these secrets (passwords or private keys) in clear text in an Ansible repository, anyone who has access to the repository can access them, and this is not what we want.

Let's see how we can manage secrets.

## The SSH Password or Keys

Most of the times, Ansible connects to the target hosts via SSH. It is common to use the system username and the SSH keys installed in `/.ssh`, which is the SSH clients default. In this case, nothing has to be done on the clients to be able to allow Ansible to use SSH, as long as they are already able to connect to the target hosts.

It is also possible to specify a different username as [ANSIBLE\_REMOTE\_USER](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#envvar-ANSIBLE_REMOTE_USER) and an SSH configuration file as [ANSIBLE\_NETCONF\_SSH\_CONFIG](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#envvar-ANSIBLE_NETCONF_SSH_CONFIG). These settings can be specified in Ansible configuration file or as environment variables.

[ANSIBLE\_ASK\_PASS](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#envvar-ANSIBLE_ASK_PASS) can be specified. If this is the case, Ansible will prompt the user asking to type an SSH password.

## Avoiding Sharing Secrets

As a general rule, any configuration that implies communicating sensible information to the persons who will connects to a system implies some degree of risk. Therefore, the most common choice is to allow users to login into remote systems with their local usernames, using SSH keys.

Once Ansible is able to connect remote hosts, it can also be used to install the public keys of some users to grant them access. Sharing these keys implies no risk. Sharing private keys is never necessary, and must be avoided.

MariaDB has a [UNIX\_SOCKET](../../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md) plugin that can be used to let some users avoid entering a password, as far as they're logged in the operating system. This authentication method is used by default for the root user. This is a good way to avoid having one more password and possibly writing to a `.my.cnf` file so that the user doesn't have to type it.

Even for users who connect remotely, it is normally not necessary to insert passwords in an Ansible file. When we create a user with a password, a hash of the original password is stored in MariaDB. That hash can be found in the [mysql.user table](../../../reference/system-tables/the-mysql-database-tables/mysql-user-table.md). To know the hash of a password without even creating a user, we can use the [PASSWORD()](../../../reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/password.md) function:

```sql
SELECT PASSWORD('my_password12') AS hash;
```

When we create a user, we can actually specify a hash instead of the password the user will have to type:

```sql
CREATE USER user@host IDENTIFIED BY PASSWORD '*54958E764CE10E50764C2EECBB71D01F08549980';
```

## ansible-vault

Even if you try to avoid sharing secrets, it's likely you'll have to keep some in Ansible. For example, MariaDB users that connect remotely have passwords, and if we want Ansible to create and manage those users, the hashes must be placed somewhere in our Ansible repository. While a hash cannot be converted back to a password, treating hashes as secrets is usually a good idea. Ansible provides a native way to handle secrets: [ansible-vault](https://docs.ansible.com/ansible/latest/user_guide/vault.html).

In the simplest case, we can manage all our passwords with a single ansible-vault password. When we add or change a new password in some file (typically a file in `host_vars` or `group_vars`) we'll use ansible-vault to crypt this password. While doing so, we'll be asked to insert our ansible-vault password. When we apply a role and Ansible needs to decrypt this password, it will ask us to enter again our ansible-vault password.

ansible-vault can use more than one password. Each password can manage a different set of secrets. So, for example, some users may have the password to manage regular MariaDB users passwords, and only one may have the password that is needed to manage the root user.

Content initially contributed by [Vettabase Ltd](https://vettabase.com/).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
