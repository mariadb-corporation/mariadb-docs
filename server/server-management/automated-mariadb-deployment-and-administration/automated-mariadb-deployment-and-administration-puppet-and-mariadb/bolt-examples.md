---
description: >-
  Demonstrates how to use Bolt, an orchestration tool in the Puppet ecosystem,
  to run ad-hoc commands, scripts, and tasks on remote MariaDB servers without a
  permanent agent.
---

# Bolt Examples

This page shows some examples of what we can do with Bolt to administer a set of MariaDB servers. Bolt is a tool that is part of the [Puppet](./) ecosystem.

For information about installing Bolt, see [Installing Bolt](https://puppet.com/docs/bolt/latest/bolt_installing.html) in Bolt documentation.

## Inventory Files

The simplest way to call Bolt and instruct it to do something on some remote targets is the following:

```bash
bolt ... --nodes 100.100.100.100,200.200.200.200,300,300,300,300
```

However, for non-trivial setups it is usually better to use an inventory file. An example:

```yaml
targets:
  - uri: maria-1.example.com
    name: maria_1
    alias: mariadb_main
  ...
```

In this way, it will be possible to refer the target by name or alias.

We can also define groups, followed by the group members. For example:

```yaml
groups:
  - name: mariadb-staging
    targets:
        - uri: maria-1.example.com
        name: maria_1
        - uri: maria-2.example.com
        name: maria_2
  - name: mariadb-production
    targets:
      ...
...
```

With an inventory of this type, it will be possible to run Bolt actions against all the targets that are members of a group:

```bash
bolt ... --nodes mariadb-staging
```

In the examples in the rest of the page, the `--targets` parameter will be indicated in this way, for simplicity: `--targets <targets>`.

## Running Commands on Targets

The simplest way to run a command remotely is the following:

```bash
bolt command run 'mariadb-admin start-all-slaves' --targets <targets>
```

## Copying Files

To copy a file or a whole directory to targets:

```bash
bolt file upload /path/to/source /path/to/destination --targets <targets>
```

To copy a file or a whole directory from the targets to the local host:

```bash
bolt file download /path/to/source /path/to/destination --targets <targets>
```

## Running Scripts on Targets

We can use Bolt to run a local script on remote targets. Bolt will temporarily copy the script to the targets, run it, and delete it from the targets. This is convenient for scripts that are meant to only run once.

```bash
bolt script run rotate_logs.sh --targets <targets>
```

## Running Tasks on Targets

Puppet tasks are not always as powerful as custom scripts, but they are simpler and many of them are idempotent. The following task stops MariaDB replication:

```bash
bolt task run mysql::sql --targets <targets> sql="STOP REPLICA"
```

## Applying Puppet Code on Targets

It is also possible to apply whole manifests or portions of Puppet code (resources) on the targets.

To apply a manifest:

```bash
bolt apply manifests/server.pp  --targets <targets>
```

To apply a resource description:

```bash
bolt apply --execute "file { '/etc/mysql/my.cnf': ensure => present }" --targets <targets>
```

## Bolt Resources and References

* [Bolt documentation](https://puppet.com/docs/bolt/latest/bolt.html).
* [Bolt on GitHub](https://github.com/puppetlabs/bolt).

Further information about the concepts explained in this page can be found in Bolt documentation:

* [Inventory Files](https://help.puppet.com/bolt/current/topics/inventory_files.htm) in Bolt documentation.
* [Applying Puppet code](https://puppet.com/docs/bolt/latest/applying_manifest_blocks.html) in Bolt documentation.

Content initially contributed by [Vettabase Ltd](https://vettabase.com/).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
