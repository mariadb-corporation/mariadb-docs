---
description: >-
  Lists available Puppet modules for MariaDB from the Puppet Forge and GitHub,
  noting that while no official module exists, community and generic MySQL
  modules are often used.
---

# Existing Puppet Modules for MariaDB

This page contains links to Puppet modules that can be used to automate MariaDB deployment and configuration. The list is not meant to be exhaustive. Use it as a starting point, but then please do your own research.

## Puppet Forge

Puppet Forge is the website to search for Puppet modules, maintained by the Puppet company. Modules are searched by the technology that needs to be automated, and the target operating system.

Search criteria include whether the modules are supported by Puppet or its partners, and whether a module is approved by Puppet. Approved modules are certified by Puppet based on their quality and maintenance standards.

## Acceptance Tests

Some modules that support the Puppet Development Kit allow some types of acceptance tests.

We can run a static analysis on a module's source code to find certain bad practices that are likely to be a source of bugs:

```bash
pdk validate
```

If a module's authors wrote unit tests, we can run them in this way:

```bash
pdk test unit
```

## Supported Modules for MariaDB

At the time of writing, there are no supported or approved modules for MariaDB.

However there is a [mysql module](https://forge.puppet.com/modules/puppetlabs/mysql) supported by Puppet, that supports the Puppet Development Kit. Though it doesn't support MariaDB-specific features, it works with MariaDB. Its documentation shows how to use the module to install MariaDB on certain operating systems.

Several unsupported and not approved modules exist for MariaDB and MaxScale.

## Resources and References

* [Puppet Forge](https://forge.puppet.com/) website.
* [Puppet Development Kit](https://puppet.com/docs/pdk/1.x/pdk.html) documentation.
* [Modules overview](https://puppet.com/docs/puppet/7.1/modules_fundamentals.html) in Puppet documentation.
* [Beginner's guide to writing modules](https://puppet.com/docs/puppet/7.1/bgtm.html) in Puppet documentation.
* [Puppet Supported Modules](https://forge.puppet.com/supported) page in Puppet Forge.

Content initially contributed by [Vettabase Ltd](https://vettabase.com/).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
