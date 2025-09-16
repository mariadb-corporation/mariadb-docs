# Firewall

## Overview

The database firewall acts as a protective barrier for a database,
ensuring that only expected queries are allowed through. It learns
the typical patterns of queries during a training period and then
uses this knowledge to block any queries that do not match what it
has learned. This helps safeguard the database from unauthorized
access or potentially harmful operations.

The firewall has two primary modes; a _learning_ mode during which it
learns what kind of statements are allowed and an _enforcing_ mode
during which it rejects or warns about non-allowed statements. In
addition there is an _idle_ mode, when the filter neither learns, nor
enforces and a _supervising_ mode, when the filter checks the
incoming statements but takes no action but only warns about
non-allowed statements.

When in the learning mode a _representative_ workload should be run
through the filter. While the learning mode is active, the filter
collects the canonical form of all statements that pass through it.
The canonical form of a statement is the statement with all literals
replaced with a question mark.
For instance, the following two statements
```
SELECT * FROM t WHERE f = 10
SELECT * FROM t WHERE f = 20
```
are different, but the canonical form of both is
`SELECT * FROM t WHERE f = ?`.

When the learning mode is finished, the allowed statements are
persistently stored in a [file](#allow-list).
The file is not specific to the MaxScale instance where it was
created and can be copied to other MaxScale installations.

When in the enforcing mode, the filter checks whether the canonical
form of a statement is found in the set of allowed canonical
statements. If it is, the statement is let through. If it is not,
the behaviour depends upon the value of [action](#action).

As an example, suppose the firewall is in the learning mode and it
encounters the following statements:
```
SELECT * FROM t WHERE f > 5
SELECT * FROM t WHERE f = 10
INSERT INTO t VALUES (42)
DELETE FROM t WHERE f > 20
SELECT * FROM users WHERE username = 'input' AND password = 'input'
```
That results in the following canonical statements:
```
SELECT * FROM t WHERE f > ?
SELECT * FROM t WHERE f = ?
INSERT INTO t VALUES (?)
DELETE FROM t WHERE f > ?
SELECT * FROM users WHERE username = ? AND password = ?
```
When switched to the enforcing mode, the following statements
will be let through
```
SELECT * FROM t WHERE f > 100
SELECT * FROM t WHERE f = 42
INSERT INTO t VALUES (84)
DELETE FROM t WHERE f > 200
SELECT * FROM users WHERE username = 'joe' AND password = 'secret'
```
but the following will not
```
# != is neither > nor =
SELECT * FROM t WHERE f != 10
# During learning only one value was inserted
INSERT INTO t VALUES (1), (2)
# During learning DELETE was always accompanied by a WHERE clause
DELETE FROM t
# An apparent SQL-injection attack does not match what was learnt.
SELECT * FROM users WHERE username = '' OR '1'='1' AND password = ''
```

While learning, the user information will be retained and saved
together with the statements. When enforcing, the value of
[user_scope](#user_scope) defines whether the allowed statements
are user specific or whether the union of all statements will
be allowed for all users.

## Allow List

The allowed canonical statements will be stored in a file in the
sub-directory `firewall` in the data directory of MaxScale, which
typically is `/var/lib/maxscale`. The name of the file will be
`<Filter>-allowed_statements.json`, where `<Filter>` is the name of the
firewall filter in the MaxScale configuration file.

For instance, with a configuration like
```
[MyFirewall]
type=filter
module=firewall
```
the name of the file will be `MyFirewall-allowed_statements.json`.

The file is not specific to the MaxScale instance where it was
created, but can, for instance, in an HA setup be copied to another
MaxScale.

The firewall filter saves the allow list when its [mode](#mode)
is switched from _learning_ to something else but `idle`. If the old
allow list needs to be retained, it should be copied before the
firewall filter is taken out from the learning mode.

The format of the file is JSON and sufficiently self-explanatory that
it can be edited manually. With caution, since, if there are syntax
errors that prevent it from being read, MaxScale will not start.

## Settings

### `mode`

- **Type**: [enum](../Getting-Started/Configuration-Guide.md#enumerations)
- **Mandatory**: No
- **Dynamic**: Yes
- **Values**: `idle`, `learn-clear`, `learn-append`, `supervise`, `enforce`
- **Default**: `idle`

This enumeration option specifies the mode of the firewall.

   * `idle`: The firewall is idle, it neither learns nor enforces.
   * `learn-clear`: The firewall first clears the existing allow list
      and then learns the valid statements from the traffic passing
      through it.
   * `learn-append`: The firewall learns the valid statements from
      the traffic passing through it and appends them to the existing
      list.
   * `supervise`: The firewall only warns about statements that are
      not allowed.
   * `enforce`: The firewall acts as specified by [action](#action)
      when it encounters a statement that is not allowed.

If the firewall is in a learning mode, switching it to any other
non-learning mode *but* `idle`, will cause the allow list to be saved.
Switching the firewall from a learning mode to `idle`, will cause the
learnt statements to be discarded and a possible existing
[allow list](#allow-list) will be left unchanged.

Even if there is no allow list, the firewall can be put in the
`supervise` or the `enforce` mode. The result is equivalent with having
and empty allow list, that is, no statements will be allowed.

### `action`

- **Type**: [enum](../Getting-Started/Configuration-Guide.md#enumerations)
- **Mandatory**: No
- **Dynamic**: Yes
- **Values**: `return-error`, `disconnect`
- **Default**: `return-error`

This enumeration option specifies the following action, if the firewall is in
_enforcing_ mode and it encounters a statement that is not allowed:

   * `return-error`: An error is returned to the client.
   * `disconnect`: The client is disconnected.

### `user_scope`

- **Type**: [enum](../Getting-Started/Configuration-Guide.md#enumerations)
- **Mandatory**: No
- **Dynamic**: Yes
- **Values**: `collective`, `individual`
- **Default**: `collective`

This enumeration option specifies whether the firewall blocks a user
based upon the statements executed by that user during the learning
mode, or whether it blocks all users based upon the union of statements
executed by all users during the learning mode.

If the scope is `collective` a user not active during the learning
mode will be able to execute the same statements the users that were
active during the learning mode will. However, if the scope is
`individual`, a user not active during the learning mode, will not
be able to execute any statements.

With [exclude_users](#exclude_users) users, e.g. admins, whose
statements should not be subject to the firewall can be listed.

### `exclude_users`

- **Type**: stringlist
- **Mandatory**: No
- **Dynamic**: Yes
- **Default**: `""`

This string list option specifies users that are excluded and whose statements
will not be subject to the firewall. The users can be specified with or
without a host and quoting can be used.
```
exclude_users=admin, 'super'@'192.168.02.1'
```
## Logging

When the firewall is in `supervise` mode, a firewall violation will
cause a warning to be logged:
```
2024-11-18 08:01:47   warning: (1) [firewall] (Service); Firewall incident (user@127.0.0.1): DELETE FROM t
```
When the firewall is in 'enforce' mode, a firewall violation will
cause the event [firewall_incident](../Getting-Started/Configuration-Guide.md#firewall_incident),
which, by default, will cause a warning to be logged to the MaxScale
log file, if [maxlog](../Getting-Started/Configuration-Guide.md#maxlog) is enabled,
and a syslog event to be generated, if [syslog](../Getting-Started/Configuration-Guide.md#syslog)
is enabled.

## Workflow

The first step when taking the firewall into use, is to create the filter
```
[MyFirewall]
type=filter
module=firewall
```
and add it to the service
```
[MyService]
type=service
router=readwritesplit
...
filters=MyFirewall
```
Since the firewall filter was just configured, the firewall will
start up in the `idle` mode.

The second step is to switch the firewall to the learning mode.
```
maxctrl alter filter MyFirewall mode=learn-clear
```
The firewall will switch to the learning mode and start collecting the
canonical form of the statements that flow through it. While the
firewall is learning, a representative workload should be run through
it. In this case, since there was no allow list, it does not matter
whether the mode is set to to `learn-clear` or `learn-append`.

The third step, once there is confidence that the firewall has seen all
relevant statements, is to switch the firewall to supervising mode.
```
maxctrl alter filter MyFirewall mode=supervise
```
At this point, the canonical statements will be saved to the file
`<datadir>/firewall/MyFirewall-allowed_statements.json`.

Since the firewall is now in the `supervise` mode, all statements
will be checked, but no action will be taken in case of a statement
that is not allowed. A warning will be logged, which allows it to
be detected whether there are statements that currently are not
allowed that should be allowed.

The last step is to switch the firewall to the enforcing mode.
```
maxctrl alter filter MyFilter mode=enforce
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
