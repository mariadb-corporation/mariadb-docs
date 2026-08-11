# mysql\_zap

{% hint style="danger" %}
mysql\_zap was removed from MariaDB. pkill can be used [as an alternative](mysql_zap.md#pkill-as-an-alternative).
{% endhint %}

_mysql\_zap_ kills processes that match a pattern. It uses the _ps_ command and Unix signals, so it runs on Unix and Unix-like systems.

Invoke mysql\_zap like this:

```
shell> mysql_zap [-signal] [-?Ift]
```

A process matches if its output line from the _ps_ command contains the pattern. By default, mysql\_zap asks for confirmation for each process. Respond _y_ to kill the process, or _q_ to exit mysql\_zap. For any other response, mysql\_zap does not attempt to kill the process.

If the _-signal_ option is given, it specifies the name or number of the signal to send to each
process. Otherwise, mysql\_zap tries first with TERM (signal 15) and then with KILL (signal 9).

mysql\_zap supports the following additional options:

| Option         | Description                                                                |
| -------------- | -------------------------------------------------------------------------- |
| --help, -?, -I | Display a help message and exit.                                           |
| -f             | Force mode. mysql\_zap attempts to kill each process without confirmation. |
| -t             | Test mode. Display information about each process but do not kill it.      |

## Example

```
localhost:~# mysql_zap -t mysql
stty: standard input: unable to perform all requested operations
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root      4073  0.0  0.2   3804  1308 ?        S    08:51   0:00 /bin/bash /usr/bin/mysqld_safe
mysql     4258  3.3 15.7 939740 81236 ?        Sl   08:51  30:18 /usr/sbin/mysqld --basedir=/usr --datadir=/var/lib/mysql --user=mysql --pid-file=/var/run/mysqld/mysqld.pid --socket=/var/run/mysqld/mysqld.sock --port=3306
```

## pkill as an Alternative

_pkill_ can be used as an alternative to _mysql\_zap_, although an important distinction between pkill and mysql\_zap is that mysql\_zap kills the server 'gently' first (with signal 15) and only if the server doesn't die in a limited time then tries -9.

To use pkill in the same way, one must run it twice; `pkill --signal 15 mysqld ; sleep(10) ; pkill -f --signal 9 pattern`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
