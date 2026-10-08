---
description: >-
  Describes how to use the MariaDB Event Scheduler to automate recurring SQL
  tasks directly within the database server, similar to cron jobs.
---

# Automating MariaDB Tasks with Events

MariaDB has an event scheduler that can be used to automate tasks, making them run at regular intervals of time. This page is about using events for [automation](./). For more information about events themselves, and how to work with them, see [event scheduler](../../server-usage/triggers-events/event-scheduler/).

## Pros and Cons of Using Events for Automation

Events can be compared to Unix cron jobs or Windows scheduled tasks. MariaDB events have at least the following benefits compared to those tools:

* Events are system-independent. The same code can run on any system.
* Events are written in procedural SQL. There is no need to install other languages or libraries.
* If you use [user-defined functions](../../server-usage/user-defined-functions/), you can still take advantage of them in your events.
* Events run in MariaDB. An implication, for example, is that the results of queries remain in MariaDB itself and are not sent to a client. This means that network glitches don't affect events, there is no overhead due to data roundtrip, and therefore locks are held for a shorter time.

Some drawbacks of using events are the following:

* Events can only perform tasks that can be developed in SQL. So, for example, it is not possible to send alerts. Access to files or remote databases is limited.
* The event scheduler runs as a single thread. This means that events that are scheduled to run while another event is running will wait until the other event has stopped. This means that there is no guarantee that an event will run on exactly it's scheduled time. This should not be a problem as long as one ensures that events are short lived.
* For more events limitations, see [Event Limitations](../../server-usage/triggers-events/event-scheduler/event-limitations.md).

In many cases you may prefer to develop scripts in an external programming language. However, you should know that simple tasks consisting of a few queries can easily be implemented as events.

## Good Practices

When using events to automate tasks, there are good practices one may want to follow.

Move your SQL code in a stored procedure. All the event will do is to call a stored procedures. Several events may call the same stored procedure, maybe with different parameters. The procedure may also be called manually, if necessary. This will avoid code duplication. This will separate the logic from the schedule, making it possible to change an event without a risk of making changes to the logic, and the other way around.

Just like cron jobs, events should log whether if they succeed or not. Logging debug messages may also be useful for non-trivial events. This information can be logged into a dedicated table. The contents of the table can be monitored by a monitoring tool like Grafana. This allows to visualize in a dashboard the status of events, and send alerts in case of a failure.

## Examples

Some examples of tasks that could easily be automated with events:

* Copying data from a remote table to a local table by night, using the [CONNECT](../../server-usage/storage-engines/connect/) storage engine. This can be a good idea if many rows need be copied, because data won't be sent to an external client.
* Periodically delete historical data. For example, rows that are older than 5 years. Nothing prevents us from doing this with an external script, but probably this wouldn't add any value.
* Periodically delete invalid rows. In an e-commerce, they could be abandoned carts. In a messaging system, they could be messages to users that don't exist anymore.
* Add a new [partition](../../server-usage/partitioning-tables/) to a table and drop the oldest one (partition rotation).

Content initially contributed by [Vettabase Ltd](https://vettabase.com/).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
