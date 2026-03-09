# The Debug Sync Facility

The Debug Sync Facility allows placement of synchronization points in\
the server code by using the DEBUG\_SYNC macro:

```
open_tables(...)

DEBUG_SYNC(thd, "after_open_tables");

lock_tables(...)
```

When activated, a sync point can

* Emit a signal and/or
* Wait for a signal

| Nomenclature      | Description                                                                                                                                                                                                                    |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| signal            | A value of a global variable that persists until overwritten by a new signal. The global variable can also be seen as a "signal post" or "flag mast". Then the signal is what is attached to the "signal post" or "flag mast". |
| emit a signal     | Assign the value (the signal) to the global variable ("set a flag") and broadcast a global condition to wake those waiting for a signal.                                                                                       |
| wait for a signal | Loop over waiting for the global condition until the global value matches the wait-for signal.                                                                                                                                 |

By default, all sync points are inactive. They do nothing (except to\
burn a couple of CPU cycles for checking if they are active).

A sync point becomes active when an action is requested for it.\
To do so, put a line like this in the test case file:

```
SET DEBUG_SYNC= 'after_open_tables SIGNAL opened WAIT_FOR flushed';
```

This activates the sync point`'after_open_tables'`. It requests it to emit the\
signal `'opened'` and wait for another thread to emit\
the signal `'flushed'` when the thread's execution\
runs through the sync point.

For every sync point there can be one action per thread only. Every\
thread can request multiple actions, but only one per sync point. In\
other words, a thread can activate multiple sync points.

Here is an example how to activate and use the sync points:

```
--connection conn1
SET DEBUG_SYNC= 'after_open_tables SIGNAL opened WAIT_FOR flushed';
send INSERT INTO t1 VALUES(1);
    --connection conn2
    SET DEBUG_SYNC= 'now WAIT_FOR opened';
    SET DEBUG_SYNC= 'after_abort_locks SIGNAL flushed';
    FLUSH TABLE t1;
```

When `conn1` runs through the`INSERT` statement, it hits the sync point`'after_open_tables'`. It notices that it is active\
and executes its action. It emits the signal`'opened'` and waits for another thread to emit the\
signal `'flushed'`.

`conn2` waits immediately at the special sync point `'now'` for another thread to emit the `'opened'` signal.

A signal remains in effect until it is overwritten. If`conn1` signals `'opened'` before`conn2` reaches `'now'`,`conn2` will still find the`'opened'` signal. It does not wait in this case.

When `conn2` reaches `'after_abort_locks'`, it signals `'flushed'`, which lets `conn1` awake.

Normally the activation of a sync point is cleared when it has been\
executed. Sometimes it is necessary to keep the sync point active for\
another execution. You can add an execute count to the action:

```
SET DEBUG_SYNC= 'name SIGNAL sig EXECUTE 3';
```

This sets the signal point's activation counter to 3. Each execution\
decrements the counter. After the third execution the sync point\
becomes inactive.

One of the primary goals of this facility is to eliminate sleeps from\
the test suite. In most cases it should be possible to rewrite test\
cases so that they do not need to sleep. (But this facility cannot\
synchronize multiple processes.) However, to support test development,\
and as a last resort, sync point waiting times out. There is a default\
timeout, but it can be overridden:

```
SET DEBUG_SYNC= 'name WAIT_FOR sig TIMEOUT 10 EXECUTE 2';
```

`TIMEOUT 0` is special: If the signal is not present,\
the wait times out immediately.

When a wait timed out (even on `TIMEOUT 0`), a\
warning is generated so that it shows up in the test result.

You can throw an error message and kill the query when a synchronization\
point is hit a certain number of times:

```
SET DEBUG_SYNC= 'name HIT_LIMIT 3';
```

Or combine it with signal and/or wait:

```
SET DEBUG_SYNC= 'name SIGNAL sig EXECUTE 2 HIT_LIMIT 3';
```

Here the first two hits emit the signal, the third hit returns the error\
message and kills the query.

For cases where you are not sure that an action is taken and thus\
cleared in any case, you can force to clear (deactivate) a sync point:

```
SET DEBUG_SYNC= 'name CLEAR';
```

If you want to clear all actions and clear the global signal, use:

```
SET DEBUG_SYNC= 'RESET';
```

This is the only way to reset the global signal to an empty string.

For testing of the facility itself you can execute a sync point just\
as if it had been hit:

```
SET DEBUG_SYNC= 'name TEST';
```

### Formal Syntax

The string to "assign" to the DEBUG\_SYNC variable can contain:

```
RESET |
<sync point name> TEST |
<sync point name> CLEAR |
<sync point name> {{SIGNAL <signal name> |
                   WAIT_FOR <signal name> [TIMEOUT <seconds>]}
                   [EXECUTE <count>] &| HIT_LIMIT <count>}
```

Here '&|' means 'and/or'. This means that one of the sections\
separated by '&|' must be present or both of them.

### Activation/Deactivation

With a [MariaDB for debug build](/broken/spaces/WCInJQ9cmGjq1lsTG91E/pages/MMYhmTTercFhxHtmbvW7), it can be enabled by a mysqld command line option:

```
--debug-sync-timeout[=default_wait_timeout_value_in_seconds]
```

`'default_wait_timeout_value_in_seconds'` is the default timeout for the `WAIT_FOR` action. If set to zero, the facility stays disabled.

The facility is enabled by default in the test suite, but can be\
disabled with:

```
mariadb-test-run.pl ... --debug-sync-timeout=0 ...
```

Likewise the default wait timeout can be set:

```
mariadb-test-run.pl ... --debug-sync-timeout=10 ...
```

The command line option influences the readable value of the [debug\_sync](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#debug_sync) system variable.

* If the facility is not compiled in, the system variable does not exist.
* If `--debug-sync-timeout=0` the value of the variable reads as `"OFF"`.
* Otherwise the value reads as `"ON - current signal: "` followed by the current signal string, which can be empty.

The readable variable value is the same, regardless if read as a global\
or session value.

Setting the [debug\_sync](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#debug_sync) system variable requires the `'SUPER'` privilege. You can never read back the\
string that you assigned to the variable, unless you assign the value\
that the variable already has. But that would give a parse\
error. A syntactically correct string is parsed into a debug sync\
action and stored apart from the variable value.

### Implementation

Pseudo code for a sync point:

```
#define DEBUG_SYNC(thd, sync_point_name)
        if (unlikely(opt_debug_sync_timeout))
          debug_sync(thd, STRING_WITH_LEN(sync_point_name))
```

The sync point performs a binary search in a sorted array of actions\
for this thread.

The `SET DEBUG_SYNC` statement adds a requested\
action to the array or overwrites an existing action for the same sync\
point. When it adds a new action, the array is sorted again.

### A typical synchronization pattern

There are quite a few places in MariaDB and MySQL where we use a\
synchronization pattern like this:

```
mysql_mutex_lock(&mutex);
thd->enter_cond(&condition_variable, &mutex, new_message);
#if defined(ENABLE_DEBUG_SYNC)
if (!thd->killed && !end_of_wait_condition)
   DEBUG_SYNC(thd, "sync_point_name");
#endif
while (!thd->killed && !end_of_wait_condition)
  mysql_cond_wait(&condition_variable, &mutex);
thd->exit_cond(old_message);
```

Here are some explanations:

`thd->enter_cond()` is used to register the condition\
variable and the mutex in `thd->mysys_var`. This is\
done to allow the thread to be interrupted (killed) from its\
sleep. Another thread can find the condition variable to signal and\
mutex to use for synchronization in this thread's `THD::mysys_var`.

`thd->enter_cond()` requires the mutex to be acquired\
in advance.

`thd->exit_cond()` unregisters the condition variable\
and mutex and releases the mutex.

If you want to have a Debug Sync point with the wait, please place it\
behind `enter_cond()`. Only then you can safely\
decide, if the wait is taken. Also you will have`THD::proc_info` correct when the sync point emits a\
signal. `DEBUG_SYNC` sets its own proc\_info, but\
restores the previous one before releasing its internal mutex. As soon\
as another thread sees the signal, it does also see the proc\_info from\
before entering the sync point. In this case it is "new\_message",\
which is associated with the wait that is to be synchronized.

In the example above, the wait condition is repeated before the sync\
point. This is done to skip the sync point, if no wait takes place.\
The sync point is before the loop (not inside the loop) to have it hit\
once only. It is possible that the condition variable is signaled\
multiple times without the wait condition to be true.

A bit off-topic: At some places, the loop is taken around the whole\
synchronization pattern:

```
while (!thd->killed && !end_of_wait_condition)
{
  mysql_mutex_lock(&mutex);
  thd->enter_cond(&condition_variable, &mutex, new_message);
  if (!thd->killed [&& !end_of_wait_condition])
  {
    [DEBUG_SYNC(thd, "sync_point_name");]
    mysql_cond_wait(&condition_variable, &mutex);
  }
  thd->exit_cond(old_message);
}
```

Note that it is important to repeat the test for thd->killed after`enter_cond()`. Otherwise the killing thread may kill\
this thread after it tested `thd->killed` in the loop\
condition and before it registered the condition variable and mutex in`enter_cond()`. In this case, the killing thread does\
not know that this thread is going to wait on a condition variable. It\
would just set `THD::killed`. But if we would not\
test it again, we would go asleep though we are killed. If the killing\
thread would kill us when we are after the second test, but still\
before sleeping, we hold the mutex, which is registered in mysys\_var.\
The killing thread would try to acquire the mutex before signaling the\
condition variable. Since the mutex is only released implicitly in`mysql_cond_wait()`, the signaling happens at the\
right place. We have a safe synchronization.

### Co-work with the DBUG facility

When running the MariaDB test suite with the`--debug-dbug` command line option, the Debug Sync\
Facility writes trace messages to the DBUG trace. The following shell\
commands proved very useful in extracting relevant information:

```
egrep 'query:|debug_sync_exec:' mysql-test/var/log/mysqld.1.trace
```

It shows all executed SQL statements and all actions executed by\
synchronization points.

Sometimes it is also useful to see, which synchronization points have\
been run through (hit) with or without executing actions. Then add`"|debug_sync_point:"` to the egrep pattern.

### Synchronizing DEBUG\_SYNC Actions

Tests may need additional synchronization mechanisms between`DEBUG_SYNC` actions, because certain combinations\
of actions can result in lost signals. More specifically, once a`SIGNAL` action is issued, it is stored in a global variable\
for any waiting threads to determine if they are depending on that signal for\
continuing. However, if a subsequent action overwrites that variable before a\
waiting thread is able to check against it, the original signal is lost. Examples\
of actions which would change the variable state are another`SIGNAL` or a `RESET`. Therefore,\
before issuing these commands, the test writer should verify the previous\
signal has been acknowledged. The following code snippets show an\
example of a problematic pattern and a potential solution.

```
SET DEBUG_SYNC='now SIGNAL sig';
SET DEBUG_SYNC='RESET'; # Problematic because sig can be cleared before a waiting thread can acknowledge it
```

```
SET DEBUG_SYNC='now SIGNAL sig';

# Don't issue the RESET until we have proven the waiting thread has received the signal
let $wait_condition= select count(*)=0 from information_schema.processlist where state like "debug sync point%";
source include/wait_condition.inc;

SET DEBUG_SYNC='RESET'; # Now this is safe
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
