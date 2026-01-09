---
description: >-
  A guide on creating and configuring a `Vagrantfile` to define the
  characteristics of a MariaDB virtual machine, including box selection and
  provisioning steps.
---

# Creating a Vagrantfile

In this page we discuss how to create a Vagrantfile, which you can use to create new boxes or machines. This content is specifically written to address the needs of MariaDB users.

## A Basic Vagrantfile

A Vagrantfile is a Ruby file that instructs Vagrant to create, depending on how it is executed, new Vagrant machines or boxes. You can see a box as a compiled Vagrantfile. It describes a type of Vagrant machines. From a box, we can create new Vagrant machines. However, while a box is easy to distribute to a team or to a wider public, a Vagrantfile can also directly create one or more Vagrant machines, without generating any box.

Here is a simple Vagrantfile example:

```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.provider "virtualbox"
  config.vm.provision :shell, path: "bootstrap.sh"
end
```

`Vagrant.configure("2")` returns the Vagrant configuration object for the new box. In the block, we'll use the `config` alias to refer this object. We are going to use version 2 of Vagrant API.

`vm.box` is the base box that we are going to use. It is Ubuntu BionicBeaver (18.04 LTS), 64-bit version, provided by HashiCorp. The schema for box names is simple: the maintainer account in [Vagrant Cloud](https://app.vagrantup.com/boxes/search) followed by the box name.

We use `vm.provision` to specify the name of the file that is going to be executed at the machine creation, to provision the machine. `bootstrap.sh` is the conventional name used in most cases.

To create new Vagrant machines from the Vagrantfile, move to the directory that contains the Vagrant project and run:

```bash
vagrant up
```

To compile the Vagrantfile into a box:

```bash
vagrant package
```

These operations can take time. To preventively check if the Vagrantfile contains syntax errors or certain types of bugs:

```bash
vagrant validate
```

## Providers

A provider allows Vagrant to create a Vagrant machine using a certain technology. Different providers may enable a virtual machine manager ([VirtualBox](https://www.vagrantup.com/docs/providers/virtualbox), [VMWare](https://www.vagrantup.com/docs/providers/vmware), [Hyper-V](https://www.vagrantup.com/docs/providers/hyperv)...), a container manager ([Docker](https://www.vagrantup.com/docs/providers/docker)), or remote cloud hosts ([AWS](https://github.com/mitchellh/vagrant-aws), [Google Compute Engine](https://github.com/mitchellh/vagrant-google)...).

Some providers are developed by third parties. [app.vagrant.com](https://app.vagrantup.com/) supports search for boxes that support the most important third parties providers. To find out how to develop a new provider, see [Plugin Development: Providers](https://www.vagrantup.com/docs/plugins/providers).

Provider options can be specified. Options affect the type of Vagrant machine that is created, like the number of virtual CPUs. Different providers support different options.

It is possible to specify multiple providers. In this case, Vagrant will try to use them in the order they appear in the Vagrantfile. It will try the first provider; if it is not available it will try the second; and so on.

Here is an example of providers usage:

```ruby
Vagrant.configure("2") do |config|
    config.vm.box = "hashicorp/bionic64"
    config.vm.provider "virtualbox" do |vb|
        vb.customize ["modifyvm", :id, "--memory", 1024 * 4]
    end
    config.vm.provider "vmware_fusion"
end
```

In this example, we try to use VirtualBox to create a virtual machine. We specify that this machine must have 4G of RAM (1024M \* 4). If VirtualBox is not available, Vagrant will try to use VMWare.

This mechanism is useful for at least a couple of reasons:

* Different users may use different systems, and maybe they don't have the same virtualization technologies installed.
* We can gradually move from one provider to another. For a period of time, some users will have the new virtualization technology installed, and they will use it; other users will only have the old technology installed, but they will still be able to create machines with Vagrant.

## Provisioners

We can use different methods for provisioning. The simplest provisioner is `shell`, that allows one to run a Bash file to provision a machine. Other provisioners allow setting up the machines using automation software, including Ansible, Puppet, Chef and Salt.

To find out how to develop a new provisioner, see [Plugin Development: Provisioners](https://www.vagrantup.com/docs/plugins/provisioners).

### The `shell` Provisioner

In the example above, the [shell](https://www.vagrantup.com/docs/provisioning/shell) provisioner runs boostrap.sh inside the Vagrant machine to provision it. A simple bootstrap.sh may look like the following:

```bash
#!/bin/bash

apt-get update
apt-get install -y
```

To find out the steps to install MariaDB on your system of choice, see the [Getting, Installing, and Upgrading MariaDB](../../install-and-upgrade-mariadb/) section.

You may also want to restore a database backup in the new Vagrant machine. In this way, you can have the database needed by the application you are developing. To find out how to do it, see [Backup and Restore Overview](../../../server-usage/backup-and-restore/backup-and-restore-overview.md). The most flexible type of backup (meaning that it works between different MariaDB versions, and in some cases even between MariaDB and different DBMSs) is a [dump](../../../clients-and-utilities/legacy-clients-and-utilities/mysqldump.md).

On Linux machines, the `shell` provisioner uses the default shell. On Windows machines, it uses PowerShell.

### Uploading Files

If we use the `shell` provisioner, we need a way to upload files to the new machine when it is created. We could use the `file` provisioner, but it works by connecting the machine via ssh, and the default user doesn't have permissions for any directory except for the synced folders. We could change the target directory owner, or we could add the default user to a group with the necessary privileges, but these are not considered good practices.

Instead, we can just put the file we need to upload somewhere in the synced folder, and then copy it with a shell command:

```bash
cp ./files/my.cnf /etc/mysql/conf.d/
```

### Provisioning Vagrant with Ansible

Here is an example of how to provision a Vagrant machine or box by running Ansible:

```ruby
Vagrant.configure("2") do |config|
  ...
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "vagrant.yml"
  end
end
```

With the [Ansible provisioner](https://www.vagrantup.com/docs/provisioning/ansible), Ansible runs in the host system and applies a playbook in the guest system. In this example, it runs a playbook called `vagrant.yml`. The [Ansible Local provisioner](https://www.vagrantup.com/docs/provisioning/ansible_local) runs the playbook in the vagrant machine.

For more information, see [Using Vagrant and Ansible](https://docs.ansible.com/ansible/latest/reference_appendices/config.html) in the Ansible documentation. For an introduction to Ansible for MariaDB users, see [Ansible and MariaDB](../ansible-and-mariadb/).

### Provisioning Vagrant with Puppet

To provision a Vagrant machine or box by running Puppet:

```ruby
Vagrant.configure("2") do |config|
  ...
  config.vm.provision "puppet" do |puppet|
    puppet.manifests_path = "manifests"
    puppet.manifest_file = "default.pp"
  end
end
```

In this example, Puppet Apply runs in the host system and no Puppet Server is needed. Puppet expects to find a `manifests` directory in the project directory. It expects it to contain `default.pp`, which will be used as an entry point. Note that `puppet.manifests_path` and `puppet.manifest_file` are set to their default values.

Puppet needs to be installed in the guest machine.

To use a Puppet server, the `puppet_server` provisioner can be used:

```ruby
Vagrant.configure("2") do |config|
  ...
  config.vm.provision "puppet_server" do |puppet|
    puppet.puppet_server = "puppet.example.com"
  end
end
```

See the [Puppet Apply provisioner](https://www.vagrantup.com/docs/provisioning/puppet_apply) and the [Puppet Agent Provisioner](https://www.vagrantup.com/docs/provisioning/puppet_agent).

For an introduction to Puppet for MariaDB users, see [Puppet and MariaDB](../automated-mariadb-deployment-and-administration-puppet-and-mariadb/).

## Sharing Files Between the Host and a Guest System

To restore a backup into MariaDB, in most cases we need to be able to copy it from the host system to the box. We may also want to occasionally copy MariaDB logs from the box to the host system, to be able to investigate problems.

The project directory (the one that contains the Vagrantfile) by default is shared with the virtual machine and mapped to the `/vagrant` directory (the synced folder). It is a good practice to put there all files that should be shared with the box when it is started. Those files should normally be versioned.

The synced folder can be changed. In the above example, we could simply add one line:

```ruby
config.vm.synced_folder "/host/path", "/guest/path"
```

The synced folder can also be disabled:

```ruby
config.vm.synced_folder '.', '/vagrant', disabled: true
```

Note that multiple Vagrant machines may have synced folders that point to the same directory on the host system. This can be useful in some cases, if you prefer to test some functionalities quickly, rather that replicating production environment as faithfully as possible. For example, to test if you're able to take a backup from one machine and restore it to another, you can store the backup in a common directory.

## Network Communications

It is often desirable for a machine to be able to communicate with "the outside". This can be done in several ways:

* Private networks;
* Public networks;
* Exposing ports to the host.

Remember that Vagrant doesn't create machines itself; instead, it asks a provider to create and manage them. Some providers support all of these communication methods, while others may only support some of them, or even none at all. When you create a Vagrantfile that uses one of these networking features, it is implicit that this can only happen if the provider you are using supports them. Check your provider's documentation to find out which features it supports.

The default provider, VirtualBox, supports all of these communication methods, including multiple networks.

### Private Networks

A private network is a networks that can only be accesses by machines that run on the same host. Usually this also means that the machines must run on the same provider (for example, they all must be VirtualBox virtual machines).

Some providers support multiple private networks. This means that every network has a different name and can be accessed by different machines.

The following line shows how to create or join a private network called "example", where this machine's IP is assigned by the provider via DHCP:

```ruby
config.vm.network 'private_network', name: 'example', type: 'dhcp'
```

While this is very convenient to avoid IP conflicts, sometimes you prefer to assign some IP's manually, in this way:

```ruby
config.vm.network 'private_network', name: 'example', ip: '111.222.111.222'
```

### Public Networks

As explained above, public networks are networks that can be accessed by machines that don't run on the same host with the same provider.

To let a machine join a public network:

```ruby
# use provider DHCP:
config.vm.network "public_network", use_dhcp_assigned_default_route: true

# assign ip manually:
config.vm.network "public_network", ip: "111.222.111.222"
```

To improve security, you may want to configure a gateway:

```ruby
config.vm.provision "shell", run: "always", inline: "route add default gw 111.222.111.222"
```

### Exposing Ports

Vagrant allows us to map a TCP or UDP port in a guest system to a TCP or UDP port in the host system. For example, you can map a virtual machine port 3306 to the host port 12345. Then you can connect MariaDB in this way:

```bash
mariadb -hlocalhost -P12345 -u<user> -p<password>
```

You are not required to map a port to a port with a different number. In the above example, if the port 3306 in your host is not in use, you are free to map the guest port 3306 to the host port 3306.

There are a couple of caveats:

* You can't map a single host port to multiple guest ports. If you want to expose the port 3306 from multiple Vagrant machines, you'll have to map them to different host ports. When running many machines this can be hard to maintain.
* Ports with numbers below 1024 are privileged ports. Mapping privileged ports requires root privileges.

To expose a port:

```ruby
config.vm.network 'forwarded_port', guest: 3306, host: 3306
```

### Use Cases

Suppose you run MariaDB and an application server in two separate Vagrant machines. It's usually best to let them communicate via a private network, because this greatly increases your security. The application server will still need to expose ports to the host, so the application can be tested with a web browser.

Suppose you have multiple environments of the same type, like the one described above. They run different applications that don't communicate with each other. In this case, if your provider supports this, you will run multiple private networks. You will need to expose the applications servers ports, mapping them to different host ports.

You may even want to implement different private networks to create an environment that reflects production complexity. Maybe in production you have [a cluster](../../../architecture/topologies/galera-cluster/) of three MariaDB servers, and the application servers communicate with them via a proxy layer (ProxySQL, HAProxy, or [MaxScale](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/)). So the applications can communicate with the proxies, but have no way to reach MariaDB directly. So there is a private network called "database" that can be accessed by the MariaDB servers and the proxy servers, and another private network called "application" that can be accessed by the proxy servers and the application servers. This requires that your provider supports multiple private networks.

Using public networks instead of private one will allow VMs that run on different hosts to be part of your topology. In general this is considered as an insecure practice, so you should probably ask yourself if you really need to do this.

## References

The [vagrant-mariadb-examples](https://github.com/Vettabase/vagrant-mariadb-examples) repository is an example of a Vagrantfile that creates a box containing MariaDB and some useful tools for developers.

Further information can be found in Vagrant documentation.

* [Vagrantfile](https://www.vagrantup.com/docs/vagrantfile).
* [Providers](https://www.vagrantup.com/docs/providers).
* [Synced Folders](https://www.vagrantup.com/docs/synced-folders).
* [Ansible Provisioner](https://www.vagrantup.com/docs/provisioning/ansible).
* [Puppet Apply Provisioner](https://www.vagrantup.com/docs/provisioning/puppet_apply).
* [Puppet Agent Provisioner](https://www.vagrantup.com/docs/provisioning/puppet_agent).

See also [Ruby documentation](https://www.ruby-lang.org/en/documentation/).

Content initially contributed by [Vettabase Ltd](https://vettabase.com/).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
