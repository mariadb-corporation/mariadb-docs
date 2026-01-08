---
description: >-
  Introduction to Puppet's architecture (agent-master vs. standalone), concepts
  like manifests and catalogs, and how it can be used for configuration
  management of MariaDB servers.
---

# Puppet Overview

Puppet is a tool to automate servers configuration management. It is produced by Puppet Inc, and released under the terms of the Apache License, version 2.

It is entirely possible to use Ansible to automate MariaDB deployments and configuration. This page contains generic information for MariaDB users who want to learn, or evaluate, Puppet.

Puppet modules can be searched using [Puppet Forge](https://forge.puppet.com/). Most of them are also published on GitHub with open source licenses. Puppet Forge allows filtering modules to only view the most reliable: supported by Puppet, supported by a Puppet partner, or approved.

For information about installing Puppet, see [Installing and upgrading](https://puppet.com/docs/puppet/7.3/architecture.html) in Puppet documentation.

## Design Principles

With Puppet, you write **manifests** that describe the resources you need to run on certain servers and their **attributes**.

Therefore manifests are **declarative**. You don't write the steps to achieve the desired result. Instead, you describe the desired result. When Puppet detects differences between your description and the current state of a server, it decides what to do to fix those differences.

Manifests are also **idempotent**. You don't need to worry about the effects of applying a manifest twice. This may happen (see Architecture below) but it won't have any side effects.

### Defining Resources

Here's an example of how to describe a resource in a manifest:

```puppet
file { '/etc/motd':
  content => '',
  ensure => present,
}
```

This block describes a resource. The resource type is `file`, while the resource itself is `/etc/motd`. The description consists of a set of attributes. The most important is `ensure`, which in this case states that the file must exist. It is also common to use this resource to indicate that a file (probably created by a previous version of the manifest) doesn't exist.

These classes of resource types exist:

* Built-in resources, or Puppet core resources: Resources that are part of Puppet, maintained by the Puppet team.
* Defined resources: Resources that are defined as a combination of other resources. They are written in the Puppet domain-specific language.
* Custom resources: Resources that are written by users, in the Ruby language.

To obtain information about resources:

```bash
# list existing resource types
puppet resource --typesupp
# print information about the file resource type
puppet describe file
```

To group several resources in a reusable class:

```puppet
class ssh_server {
  file { '/etc/motd':
    content => '',
    ensure => present,
  }
  file { '/etc/issue.net':
    content => '',
    ensure => present,
  }
}
```

There are several ways to include a class. For example:

```puppet
include Class['ssh_server']
```

### Defining Nodes

Puppet has a **main manifest** that could be a `site.pp` file or a directory containing `.pp` files. For simple infrastructures, we can define the nodes here. For more complex infrastructures, we may prefer to import other files that define the nodes.

Nodes are defined in this way:

```puppet
node 'maria-1.example.com' {
  include common
  include mariadb
}
```

The resource type is `node`. Then we specify a hostname that is used to match this node to an existing host. This can also be a list of hostnames, a regular expression that matches multiple nodes, or the `default` keyword that matches all hosts. To use a regular expression:

```puppet
node /^(maria|mysql)-[1-3]\.example\.com$/ {
  include common
}
```

## Concepts

The most important Puppet concepts are the following:

| Concepts      | Definition                                                                                                         |
| ------------- | ------------------------------------------------------------------------------------------------------------------ |
| Target        | A host whose configuration is managed via Puppet.                                                                  |
| Group         | A logical group of targets. Example: `mariadb` group.                                                              |
| Facts         | Information collected from targets (e.g., system name/version) using Facter. Can be core or custom facts.          |
| Manifest      | A description that can be applied to a target.                                                                     |
| Catalog       | A compiled manifest.                                                                                               |
| Apply         | Modifying a target's state to reflect its manifest description.                                                    |
| Module        | A set of manifests.                                                                                                |
| Resource      | A minimal piece of description in a manifest describing system components like files or services.                  |
| Resource Type | Determines the class of a resource, e.g., `file` resource type with multiple resources describing different files. |
| Attribute     | Characteristic of a resource, like file owner or mode.                                                             |
| Class         | A group of resources reusable across several manifests.                                                            |

## Architecture

Depending on how the user decides to deploy changes, Puppet can use two different architectures:

* An Agent-master architecture. This is the preferred way to use Puppet.
* A standalone architecture, that is similar to [Ansible architecture](../ansible-and-mariadb/ansible-overview-for-mariadb-users.md#architecture).

### Agent-master Architecture

A **Puppet master** stores a catalog for each target. There may be more than one Puppet master, for redundancy.

Each target runs a **Puppet agent** in background. Each Puppet agent periodically connects to the Puppet master, sending its facts. The Puppet master compiles the relevant manifest using the facts it receives, and send back a catalog. Note that it is also possible to store the catalogs in PuppetDB instead.

Once the Puppet agent receives the up-to-date catalog, it checks all resources and compares them with its current state. It applies the necessary changes to make sure that its state reflects the resources present in the catalog.

### Standalone Architecture

With this architecture, the targets run **Puppet apply**. This application usually runs as a Linux cron job or a Windows scheduled task, but it can also be manually invoked by the user.

When Puppet apply runs, it compiles the latest versions of manifests using the local facts. Then it checks every resource from the resulting catalogs and compares it to the state of the local system, applying changes where needed.

Newly created or modified manifests are normally deployed to the targets, so Puppet apply can read them from the local host. However it is possible to use PuppetDB instead.

### PuppetDB

PuppetDB is a Puppet node that runs a PostgreSQL database to store information that can be used by other nodes. PuppetDB can be used with both the Agent-master and the standalone architectures, but it is always optional. However it is necessary to use some advanced Puppet features.

PuppetDB stored the following information:

* The latest facts from each target.
* The latest catalogs, compiled by Puppet apply or a Puppet master.
* Optionally, the recent history of each node activities.

### External Node Classifiers

With both architectures, it is possible to have a component called an External Node Classifier (ENC). This is a script or an executable written in any language that Puppet can call to determine the list of classes that should be applied to a certain target.

An ENC received a node name in input, and should return a list of classes, parameters, etc, as a YAML hash.

### Bolt

Bolt can be used in both architectures to run operations against a target or a set of targets. These operations can be commands passed manually to Bolt, scripts, Puppet tasks or plans. Bolt directly connects to targets via ssh and runs system commands.

See [Bolt Examples](bolt-examples.md) to get an idea of what you can do with Bolt.

## hiera

hiera is a hierarchical configuration system that allows us to:

* Store configuration in separate files;
* Include the relevant configuration files for every server we automate with Puppet.

See [Puppet hiera Configuration System](puppet-hiera-configuration-system.md) for more information.

## Puppet Resources

* [Puppet documentation](https://puppet.com/docs/).
* [forge.puppet.com](https://forge.puppet.com/).
* [Puppet on GitHub](https://github.com/puppetlabs/puppet).
* [Puppet on Wikipedia](https://en.wikipedia.org/wiki/Puppet_\(company\)).

More information about the topics discussed in this page can be found in the Ansible documentation:

* [Puppet Glossary](https://puppet.com/docs/puppet/latest/glossary.html) in Puppet documentation.
* [Overview of Puppet's architecture](https://puppet.com/docs/puppet/latest/architecture.html) in Puppet documentation.
* [PuppetDB documentation](https://puppet.com/docs/puppetdb/latest/index.html).
* [Classifying nodes](https://puppet.com/docs/puppet/latest/nodes_external.html) in Puppet documentation.
* [Hiera](https://puppet.com/docs/puppet/latest/hiera_intro.html) in Puppet documentation.
* [Bolt documentation](https://puppet.com/docs/bolt/latest/bolt.html).

Content initially contributed by [Vettabase Ltd](https://vettabase.com/).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
