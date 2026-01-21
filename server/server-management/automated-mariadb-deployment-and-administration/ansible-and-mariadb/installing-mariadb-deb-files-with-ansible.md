---
description: >-
  Detailed instructions for automating the installation of MariaDB on
  Debian/Ubuntu systems, including tasks for adding repositories, importing GPG
  keys, and installing packages.
---

# Installing MariaDB .deb Files with Ansible

This page refers to the operations described in [Installing MariaDB .deb Files](../../install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-deb-files.md). Refer to that page for a complete list and explanation of the tasks that should be performed.

Here we discuss how to automate such tasks using Ansible. For example, here we show how to install a package or how to import a GPG key; but for an updated list of the necessary packages and for the keyserver to use, you should refer to [Installing MariaDB .deb Files](../../install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-deb-files.md).

## Adding apt Repositories

To [add a repository](../../install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-deb-files.md#executing-add-apt-repository):

```yaml
- name: Add specified repository into sources list
  ansible.builtin.apt_repository:
    repo: deb [arch=amd64,arm64,ppc64el] http://sfo1.mirrors.digitalocean.com/mariadb/repo/10.3/ubuntu bionic main
    state: present
```

If you prefer to keep the repository information in a [source list file](../../install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-deb-files.md#creating-a-source-list-file) in the Ansible repository, you can upload that file to the target hosts in this way:

```yaml
- name: Create a symbolic link
  ansible.builtin.file:
    src: ./file/mariadb.list
    dest: /etc/apt/sources.list.d/
    owner: root
    group: root
    mod: 644
    state: file
```

## Updating the Repository Cache

Both the Ansible modules [ansible.builtin.apt](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_module.html) and [ansible.builtin.apt\_repository](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_repository_module.html) have an `update_cache` attribute. In ansible.builtin.apt it is set to "no" by default. Whenever a task sets it to 'yes', `apt-get update` is run on the target system. You have three ways to make sure that repositories are updated.

The first is to use ansible.builtin.apt\_repository to add the desired repository, as shown above. So you only need to worry about updating repositories if you use the file method.

The second is to make sure that `update_cache` is set to 'yes' when you install a repository:

```yaml
- name: Install foo
  apt:
    name: foo
    update_cache: yes
```

But if you run certain tasks conditionally, this option may not be very convenient. So the third option is to update the repository cache explicitly as a separate task:

```yaml
- name: Update repositories
  apt:
    - update_cache: yes
```

## Importing MariaDB GPG Key

To [import the GPG key](../../install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-deb-files.md#importing-the-mariadb-gpg-public-key) for MariaDB we can use the [ansible.builtin.apt\_key](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_key_module.html) Ansible module. For example:

```yaml
- name: Add an apt key by id from a keyserver
  ansible.builtin.apt_key:
    keyserver: hkp://keyserver.ubuntu.com:80
    id: 0xF1656F24C74CD1D8
```

## Installing Packages

To install Deb packages into a system:

```yaml
- name: Install software-properties-common
  apt:
    name: software-properties-common
    state: present
```

To make sure that a specific version is installed, performing an upgrade or a downgrade if necessary:

```yaml
- name: Install foo 1.0
  apt:
    name: foo=1.0
```

To install a package or upgrade it to the latest version, use: `state: latest`.

To install multiple packages at once:

```yaml
- name: Install the necessary packages
  apt:
    pkg:
    - pkg1
    - pkg2=1.0
```

If all your servers run on the same system, you will always use ansible.builtin.apt and the names and versions of the packages will be the same for all servers. But suppose you have some servers running systems from the Debian family, and others running systems from the Red Hat family. In this case, you may find convenient to use two different task files for two different types of systems. To include the proper file for the target host's system:

```yaml
- include: mariadb-debian.yml
  when: "{{ ansible_facts['os_family'] }} == 'Debian'
```

The variables you can use to run the tasks related to the proper system are:

* [ansible\_fact \['distribution'\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_conditionals.html#ansible-facts-distribution)
* [ansible\_fact \['distribution\_major\_version'\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_conditionals.html#ansible-facts-distribution-major-version)
* [ansible\_fact \['os\_family'\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_conditionals.html#ansible-facts-os-family)

There is also a system-independent [package module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/package_module.html), but if the package names depend on the target system using it may be of very little benefit.

## See Also

* [Installing MariaDB .deb Files](../../install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-deb-files.md)

Content initially contributed by [Vettabase Ltd](https://vettabase.com/).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
