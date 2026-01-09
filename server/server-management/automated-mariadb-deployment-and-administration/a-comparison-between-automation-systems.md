---
description: >-
  Compares different automation tools like Ansible and Puppet, highlighting
  differences in their architecture (agentless vs. agent-based) and code
  structure to help users choose the right tool.
---

# Comparison Between Automation Systems

This page compares the automation systems that are covered by this section of the MariaDB documentation. More information about these systems are presented in the relevant pages, and more systems may be added in the future.

## Code Structure Differences

Different automation systems provide different ways to describe our infrastructure. Understanding how they work is the first step to evaluate them and choose one for our organization.

{% tabs %}
{% tab title="Ansible" %}
Ansible code consists of the following components:

* An inventory determines which hosts Ansible should be able to deploy. Each host may belong to one or more groups. Groups may have children, forming a hierarchy. This is useful because it allows us to deploy on a group, or to assign variables to a group.
* A role describes the state that a host, or group of hosts, should reach after a deploy.
* A play associates hosts or groups to their roles. Each role/group can have more than one role.
* A role consists of a list of tasks. Despite its name a task is not necessarily something to do, but something that must exist in a certain state.
* Tasks can use variables. They can affect how a task is executed (for example a variable could be a file name), or even whether a task is executed or not. Variables exist at role, group or host level. Variables can also be passed by the user when a play is applied.
* Playbooks are the code that is used to define tasks and variables.
* Facts are data that Ansible retrieves from remote hosts before deploying. This is a very important step, because facts may determine which tasks are executed or how they are executed. Facts include, for example, the operating system family or its version. A playbook sees facts as pre-set variables.
* Modules implement actions that tasks can use. Action examples are file (to declare that files and directories must exist) or mysql\_variables (to declare MySQL/MariaDB variables that need to be set).

See [Ansible Overview - concepts](ansible-and-mariadb/ansible-overview-for-mariadb-users.md) for more details and an example.
{% endtab %}

{% tab title="Puppet" %}
Puppet code consists of the following components:

* An inventory file defines a set of groups and their targets (the members of a group). plugins can be used to retrieve groups and target dynamically, so they are equivalent to Ansible dynamic inventories.
* A manifest is a file that describes a configuration.
* A resource is a component that should run on a server. For example, "file" and "service" are existing support types.
* An attribute relates to a resource and affects the way it is applied. For example, a resource of type "file" can have attributes like "owner" and "mode".
* A class groups resources and variables, describing a logical part of server configuration. A class can be associated to several servers. A class is part of a manifest.
* A module is a set of manifests and describes an infrastructure or a part of it.
* Classes can have typed parameters that affect how they are applied.
* Properties are variables that are read from the remote server, and cannot be arbitrarily assigned.
* Facts are pre-set variables collected by Puppet before applying or compiling a manifest.
{% endtab %}
{% endtabs %}

## Architectural Differences

The architecture of the various systems is different. Their architectures determine how a deploy physically works, and what is needed to be able to deploy.

{% tabs %}
{% tab title="Ansible" %}
Ansible architecture is simple. Ansible can run from any host, and can apply its playbooks on remote hosts. To do this, it runs commands via SSH. In practice, in most cases the commands will be run as superuser via `sudo`, though this is not always necessary.

Inventories can be dynamic. In this case, when we apply a playbook Ansible connects to remote services to discover hosts.

Ansible playbooks are applied via the `ansible-playbook` binary. Changes to playbooks are only applied when we perform this operation.

To recap, Ansible does not need to be installed on the server is administers. It needs an SSH access, and normally its user needs to be able to run `sudo`. It is also possible to configure a dynamic inventory, and a remote service to be used for this purpose.
{% endtab %}

{% tab title="Puppet" %}
**Puppet Architecture**

Puppet supports two types of architecture: agent-master or standalone. The agent-master architecture is recommended by Puppet Labs, and it is the most popular among Puppet users. For this reason, those who prefer a standalone architecture tend to prefer Ansible.

**Agent-Master Architecture**

When this architecture is chosen, manifests are sent to the **Puppet master**. There can be more than one master, for high availability reasons. All target hosts run a **Puppet agent**. Normally this is a service that automatically starts at system boot. The agent contacts a master at a given interval. It sends facts, and uses them to compile a **catalog** from the manifests. A catalog is a description of what exactly an individual server should run. The agent receives the catalog and checks if there are differences between its current configuration and the catalog. If differences are found, the agent applies the relevant parts of the catalog.

An optional component is **PuppetDB**. This is a central place where some data are stored, including manifests, retrieved facts and logs. PuppetDB is based on PostgreSQL and there are no plans to support MariaDB or other DBMSs.

If a manual change is made to a remove server, it will likely be overwritten the next time Puppet agent runs. To avoid this, the Puppet agent service can be stopped.

**Standalone Architecture**

As mentioned, this architecture is not recommended by Puppet Labs nor popular amongst Puppet users. It is similar to Ansible architecture.

Users can apply manifests from any host with Puppet installed. This could be their laptop but, in order to emulate the behavior of an agent-master architecture, normally Puppet runs on a dedicated node as a cronjob. The **Puppet apply** application will require facts from remote hosts, it will compile a catalog for each host, will check which parts of it need to be applied, and will apply them remotely.

If a manual change is made to a remove server, it will be overwritten the next time Puppet apply runs. To avoid this, comment out any cron job running Puppet apply, or comment out the target server in the inventory.

**Inventory**

As mentioned, Puppet supports plugins to retrieve the inventory dynamically from remote services. In an agent-master architecture, one has to make sure that each target host has access to these services. In a standalone architecture, one has to make sure that the hosts running Puppet apply have access to these services.
{% endtab %}
{% endtabs %}

## Storing Secrets

Often our automation repositories need to contain secrets, like MariaDB user passwords or private keys for SSH authentication.

Both Ansible and Puppet support integration with secret stores, like Hashicorp Vault.

{% tabs %}
{% tab title="Ansible" %}
Ansible allows encrypting secrets in playbooks and decrypting them during execution using [ansible-vault](https://docs.ansible.com/ansible/latest/user_guide/vault.html). This implies a minimal effort to handle secrets. However, it is not the most secure way to store secrets. The passwords to disclose certain secrets need to be shared with the users who have the right to use them. Also, brute force attacks are possible.
{% endtab %}

{% tab title="Puppet" %}
For Puppet integration, see [Integrations with secret stores](https://puppet.com/docs/puppet/6.17/integrations_with_secret_stores.html).
{% endtab %}
{% endtabs %}

## Ecosystems and Communities

Automation software communities are very important, because they make available a wide variety of modules to handle specific software.

{% tabs %}
{% tab title="Ansible" %}
Ansible is open source, released under the terms of the GNU GPL. It is produced by RedHat. RedHat has a page about [Red Hat Ansible Automation Platform Partners](https://www.ansible.com/partners), who can provide support and consulting.

[Ansible Galaxy](https://galaxy.ansible.com/) is a big repository of Ansible roles produced by both the vendor and the community. Ansible comes with `ansible-galaxy`, a tool that can be used to create roles and upload them to Ansible Galaxy.

At the time of this writing, Ansible does not have specific MariaDB official modules. MySQL official modules can be used. However, be careful not try to use features that only apply to MySQL. There are several community-maintained MariaDB roles.
{% endtab %}

{% tab title="Puppet" %}
Puppet is open source, released under the GNU GPL. It is produced by a homonym company. The page [Puppet Partners](https://puppet.com/partners/) lists partners that can provide support and consulting about Puppet.

[Puppet Forge](https://forge.puppet.com/) is a big repository of modules produced by the vendor and by the community, as well as how-to guides.

Currently Puppet has many MariaDB modules.
{% endtab %}
{% endtabs %}

## See Also

For more information about the systems mentioned in this page, from MariaDB users perspective:

* [Ansible and MariaDB](ansible-and-mariadb/).
* [Puppet and MariaDB](automated-mariadb-deployment-and-administration-puppet-and-mariadb/).

Content initially contributed by [Vettabase Ltd](https://vettabase.com/).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
