---
description: >-
  Understand how triggers behave under row-based replication. Learn when and why
  triggers are not executed on the replica and how to manage complex logic in
  this mode.
---

# Running Triggers on the Replica for Row-based Events

{% hint style="info" %}
The terms _master_ and _slave_ have historically been used in replication, and MariaDB has begun the process of adding _primary_ and _replica_ synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.
{% endhint %}

MariaDB can force the replica thread to run [triggers](../../server-usage/triggers-events/triggers/) for row-based binlog events.

The setting is controlled by the [slave\_run\_triggers\_for\_rbr](replication-and-binary-log-system-variables.md) global variable. It can be also specified as a command-line option or in my.cnf.

Possible values are:

| Value        | Meaning                                                                                                                                                                                                                              |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| NO (Default) | Don't invoke triggers for row-based events                                                                                                                                                                                           |
| YES          | Invoke triggers for row-based events, don't log their effect into the binary log                                                                                                                                                     |
| LOGGING      | Invoke triggers for row-based events, and log their effect into the binary log                                                                                                                                                       |
| ENFORCE      | From [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.2) only. Triggers will always be run on the replica, even if there are triggers on the master. ENFORCE implies LOGGING. |

**Note that if you just want to use triggers together with replication, you most likely don't need this option.** Read below for details.

## When to Use slave\_run\_triggers\_for\_rbr

### Background

Normally, MariaDB's replication system can replicate trigger actions automatically.

* When one uses statement-based replication, the binary log contains SQL statements. Replica server(s) execute the SQL statements. Triggers are run on the master and on each replica, independently.
* When one uses row-based replication, the binary log contains row changes. It will have both the changes made by the statement itself, and the changes made by the triggers that were invoked by the statement. Replica server(s) do not need to run triggers for row changes they are applying.

### Target Usecase

One may want to have a setup where a replica has triggers that are not present on the master (Suppose the replica needs to update summary tables or perform some other ETL-like process).

If one uses statement-based replication, they can just create the required triggers on the replica. The replica will run the statements from the binary log, which will cause the triggers to be invoked.

However, there are cases where you have to use row-based replication. It could be because the master runs non-deterministic statements, or the master could be a node in a Galera cluster. In that case, you would want row-based events to invoke triggers on the replica. This is what the `slave_run_triggers_for_rbr` option is for. Setting the option to `YES` will cause the SQL replica thread to invoke triggers for row-based events; setting it to `LOGGING` will also cause the changes made by the triggers to be written into the binary log.

The following triggers are invoked:

* Update\_row\_event runs an UPDATE trigger
* Delete\_row\_event runs a DELETE trigger
* Write\_row\_event runs an INSERT trigger. Additionally it runs a DELETE trigger if there was a conflicting row that had to be deleted.

## Preventing Multiple Trigger Invocations

There is a basic protection against triggers being invoked both on the master and replica.\
If the master modifies a table that has triggers, it will produce row-based binlog events with the "triggers were invoked for this event" flag. The replica will not invoke any triggers for flagged events.

## See Also

* Task in Jira, [MDEV-5095](https://jira.mariadb.org/browse/MDEV-5095).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
