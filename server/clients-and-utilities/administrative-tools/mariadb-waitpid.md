# mariadb-waitpid

`mariadb_waitpid` is a utility for terminating processes. 

{% hint style="info" %}
It runs on Unix-like systems, making use of the `kill()` system call.
{% endhint %}

Previously, the client was called `mysql_waitpid`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.

## Usage

```
mariadb-waitpid [options] pid time
```

## Description

`mariadb-waitpid` sends signal `0` to the process _pid_ and waits up to _time_ seconds for the process to terminate. _pid_. _time_ must be positive integers.

Returns `0` if the process terminates in time or does not exist, and `1` otherwise.

Signal `1` is used if the `kill()` system call cannot handle signal `0`.

## Options

| Option        | Description                                                       |
| ------------- | ----------------------------------------------------------------- |
| -?, --help    | Display help and exit.                                            |
| -I, --help    | Synonym for `-?`.                                                 |
| -v, --verbose | Be more verbose. Give a warning, if kill can't handle signal `0`. |
| -V, --version | Print version information and exit.                               |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
